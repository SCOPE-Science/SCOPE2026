"""Reproduce finite corroborations of sharp unicyclic-zonotope surface bounds.

Dependencies: networkx, numpy, scipy. Execute: python CHECK.py
Analytical proof and unlimited dimension claims are in RESULT.md, not this checker.
"""
from itertools import product
from math import sqrt
import networkx as nx
import numpy as np
from scipy.spatial import ConvexHull
from scipy.linalg import null_space

def f(s,n):
    return sqrt(s*(n-s))

def sun_formula(c,extras):
    n=c+sum(extras)
    a=[1+x for x in extras]
    bridge=2*c*(n-c)*sqrt(n-1)
    cyclic=sum(f(sum(a[(i+j)%c] for j in range(k)),n)
               for i in range(c) for k in range(1,c))
    return bridge+cyclic

def global_min(c,n):
    return 2*c*(n-c)*sqrt(n-1)+2*sum((c-k)*f(k,n) for k in range(1,c))

def balanced_upper(c,n):
    return 2*c*(n-c)*sqrt(n-1)+n*sum(sqrt(k*(c-k)) for k in range(1,c))

def full_formula(G):
    n=G.number_of_nodes()
    cycles=nx.cycle_basis(G)
    assert len(cycles)==1
    cyc=cycles[0];c=len(cyc);on=set(cyc)
    bridge_sum=0.
    for edge in nx.bridges(G):
        H=G.copy();H.remove_edge(*edge)
        parts=list(nx.connected_components(H))
        s=len(next(p for p in parts if not on.issubset(p)))
        bridge_sum+=f(s,n)
    H=G.copy()
    H.remove_edges_from([e for e in H.edges if e[0] in on and e[1] in on])
    a=[len(nx.node_connected_component(H,v)) for v in cyc]
    assert sum(a)==n
    return 2*c*bridge_sum+sum(f(sum(a[(i+j)%c] for j in range(k)),n)
                          for i in range(c) for k in range(1,c)),c

counts={}
for graph in nx.graph_atlas_g():
    n=graph.number_of_nodes()
    if n<4 or n>7 or graph.number_of_edges()!=n or not nx.is_connected(graph):
        continue
    area,c=full_formula(graph)
    assert area+1e-8>=global_min(c,n)
    if abs(area-global_min(c,n))<1e-8:
        degrees=[degree for _,degree in graph.degree()]
        assert max(degrees)==n-c+2 or n==c
    counts[n,c]=counts.get((n,c),0)+1
assert sum(counts.values())==53

allocation_groups=0
for c in range(3,7):
    for leaves in range(1,8):
        n=c+leaves
        scores=[]
        for extras in product(range(leaves+1),repeat=c):
            if sum(extras)!=leaves: continue
            S=sun_formula(c,extras)
            a=[1+x for x in extras]
            deviation=sum((sum(a[(i+j)%c] for j in range(k))-k*n/c)**2
                for k in range(1,c) for i in range(c))/n
            assert balanced_upper(c,n)-S>=deviation-1e-8
            scores.append(S)
        assert abs(min(scores)-global_min(c,n))<1e-8
        if n%c==0:
            assert abs(max(scores)-balanced_upper(c,n))<1e-8
        allocation_groups+=1
assert allocation_groups==28

hulls=0
for c in (3,4):
    for extras in ([1]+[0]*(c-1),[2]+[0]*(c-1),[1,1]+[0]*(c-2),[1]*c):
        n=c+sum(extras)
        edges=[(i,(i+1)%c) for i in range(c)]
        next_vertex=c
        for i,number in enumerate(extras):
            for _ in range(number):
                edges.append((i,next_vertex));next_vertex+=1
        incidence=np.zeros((n,len(edges)))
        for j,(u,v) in enumerate(edges):
            incidence[u,j]=1.;incidence[v,j]=-1.
        U=null_space(np.ones((1,n)))
        signs=np.array(list(product([-1.,1.],repeat=len(edges))))
        points=signs @ incidence.T @ U / 2
        hull=ConvexHull(points)
        assert abs(hull.area-sun_formula(c,extras))<1e-7
        assert abs(hull.volume-c*sqrt(n))<1e-7
        hulls+=1
assert hulls==8
print('VERIFY_OK atlas_graphs=53 allocation_groups=28 independent_hulls=8')
