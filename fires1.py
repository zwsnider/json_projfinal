## Use the files below to compare the fires that have been burning in Australia between November and now. 
# This file contains information about the latitude and longitude, and the brightness of each fire. 
# Using what you have learnt in processing a CSV files and mapping, make a map that shows the fires. 
# You will need separate programs to represent each CSV file. One file is from Nov 27 2019 and the other is from Jan 26 2020. 
import csv

open_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt","r") 
readFile = csv.reader(open_file, delimiter =",")
NovemberData = [row for row in readFile]

brigs, lons, lats = [],[],[]
headers = NovemberData[0]

NovemberData_noheaders = NovemberData[1:868]   

lats = [x[0] for x in NovemberData_noheaders]
lons = [x[1] for x in NovemberData_noheaders]
brigs = [x[2] for x in NovemberData_noheaders]


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline


'''scl = [300,"rgb(0, 152, 255)"],[320,"rgb(44, 255, 150)"],[340,"rgb(151, 255, 0)"],\
[380,"rgb(255, 234, 0)"],[400,"rgb(255, 111, 0)"],[440,"rgb(255, 0, 0)"]'''

brigs = [float(x) for x in brigs]   


data = [{ 
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'marker':{
        'size':[.05*brig for brig in brigs],
        'color': brigs,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Brightness'} 
        },
}]

my_layout = Layout(title = "Australian Fires - November 2019", \
    geo = dict( 
        showland = True,
        lataxis = dict(range=[-37,-13]),
        lonaxis = dict(range=[111,160])
    ))

fig = {"data": data, "layout":my_layout}

offline.plot(fig,filename="november_fires.html")
