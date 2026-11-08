"""Directly replay the synchronous chip-firing update, independently of phase counting."""
from itertools import product
import networkx as nx
import sympy as sp

def count_period3(G):
    vs=list(G); neigh=[[vs.index(u) for u in G.neighbors(v)] for v in vs]
    deg=[len(a) for a in neigh]
    total=0;tested=0;example=None
    for x in product(*(range(2*d) for d in deg)):
        tested+=1
        def upd(y):
            fires=[int(y[i]>=deg[i]) for i in range(len(vs))]
            return tuple(y[i]-deg[i]*fires[i]+sum(fires[j] for j in neigh[i]) for i in range(len(vs)))
        y=upd(x)
        if y==x: continue
        z=upd(y)
        if upd(z)==x:
            total+=1
            if example is None: example=x
    return total,tested,example

def graph(name):
    if name=='triangle':return nx.cycle_graph(3)
    if name=='triangle_with_tail':
        G=nx.cycle_graph(3);G.add_edges_from([(0,3),(3,4),(4,5)]);return G
    if name=='triangle_and_square':
        G=nx.cycle_graph(3);G.add_edges_from([(0,3),(3,4),(4,5),(5,0)]);return G
    if name=='two_triangles':
        G=nx.cycle_graph(3);G.add_edges_from([(0,3),(3,4),(4,0)]);return G
    if name=='square':return nx.cycle_graph(4)
    if name=='hexagon':return nx.cycle_graph(6)
    if name=='hexagon_chord':
        G=nx.cycle_graph(6);G.add_edge(0,3);return G
    if name=='theta_2_3_4':
        G=nx.Graph();G.add_edges_from([(0,2),(2,1),(0,3),(3,4),(4,1),(0,5),(5,6),(6,7),(7,1)]);return G
    raise ValueError(name)

for name,expect in [('triangle',12),('triangle_with_tail',12),('triangle_and_square',48),('two_triangles',72),('square',0),('hexagon',12),('hexagon_chord',12),('theta_2_3_4',None)]:
    G=graph(name)
    got,tested,example=count_period3(G)
    if expect is not None:assert got==expect,(name,got,expect)
    print(name,'n',len(G),'states_checked',tested,'period_three',got,'example',example)
print('DIRECT DYNAMICS PASS')
