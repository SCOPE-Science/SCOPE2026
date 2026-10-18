#!/usr/bin/env python3
"""Standalone checks for the cube--octahedron family silhouette-count theorem.

Uses exact rational 3D halfspace geometry and independent exact projected-hull counts.
All endpoints and three open combinatorial chambers are tested.
"""
from fractions import Fraction as Q
from itertools import product, combinations, permutations
from collections import Counter
from math import atan, sqrt, pi
import random

AXES=[tuple(d if j==i else 0 for j in range(3)) for i in range(3) for d in (-1,1)]
DIAGS=list(product((-1,1),repeat=3))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def facets(c):
    return [(a,Q(1),'A') for a in AXES if c>1] + [(a,c,'D') for a in DIAGS if c<3]

def vertices(c):
    f=facets(c);v=set()
    for ids in combinations(range(len(f)),3):
        row=[f[k][0] for k in ids]; D=det(*row)
        if not D:continue
        y=[f[k][1] for k in ids]
        x=tuple(Q(det(*(tuple(y[i] if k==j else row[i][k] for k in range(3)) for i in range(3))),D) for j in range(3))
        if all(dot(a,x)<=b for a,b,_ in f):v.add(x)
    return sorted(v)

def edge_pairs_from_geometry(c):
    f=facets(c);v=vertices(c);edges=set()
    for i,j in combinations(range(len(f)),2):
        if sum(dot(f[i][0],x)==f[i][1] and dot(f[j][0],x)==f[j][1] for x in v)>=2:
            edges.add(tuple(sorted((f[i][0],f[j][0]))))
    return edges,v

def predicted_edges(c):
    if c==1: return {tuple(sorted((a,b))) for a,b in combinations(DIAGS,2) if sum(x!=y for x,y in zip(a,b))==1}
    if c==3: return {tuple(sorted((a,b))) for a,b in combinations(AXES,2) if dot(a,b)==0}
    e={tuple(sorted((a,s))) for a in AXES for s in DIAGS if dot(a,s)==1}
    if c<2:e|={tuple(sorted((a,b))) for a,b in combinations(DIAGS,2) if sum(x!=y for x,y in zip(a,b))==1}
    elif c>2:e|={tuple(sorted((a,b))) for a,b in combinations(AXES,2) if dot(a,b)==0}
    return e

def crossing_count(edges,u):
    assert all(dot(a,u)!=0 and dot(b,u)!=0 for a,b in edges)
    return sum((dot(a,u)>0)!=(dot(b,u)>0) for a,b in edges)

def hull_count(V,u):
    ux,uy,uz=u
    q=(-uy,ux,0) if ux or uy else (1,0,0)
    r=cross(u,q)
    P=sorted(set((dot(x,q),dot(x,r)) for x in V))
    def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    H=[]
    for p in P:
        while len(H)>=2 and cr(H[-2],H[-1],p)<=0:H.pop()
        H.append(p)
    L=[]
    for p in P[::-1]:
        while len(L)>=2 and cr(L[-2],L[-1],p)<=0:L.pop()
        L.append(p)
    return len(H[:-1])+len(L[:-1])

def predicted_count(c,u):
    vals=sorted(map(abs,u),reverse=True)
    assert vals[0]!=vals[1]+vals[2] and all(vals)
    dominant=vals[0]>vals[1]+vals[2]
    if c==1:return 4 if dominant else 6
    if c<2:return 12
    if c==2:return 8 if dominant else 6
    if c<3:return 14 if dominant else 12
    return 6

def main():
    params=[Q(1),Q(6,5),Q(3,2),Q(9,5),Q(2),Q(11,5),Q(5,2),Q(14,5),Q(3)]
    rng=random.Random(20261017)
    cases=0
    orbit_directions=sorted(set(
        tuple(signs[i]*perm[i] for i in range(3))
        for base in ((9,4,2),(6,4,3))
        for perm in permutations(base)
        for signs in product((-1,1),repeat=3)
    ))
    assert len(orbit_directions)==96
    for c in params:
        edges,v=edge_pairs_from_geometry(c);expect=predicted_edges(c)
        assert edges==expect,(c,len(edges),len(expect),edges^expect)
        for u in orbit_directions + [tuple(rng.sample(range(-37,38),3)) for _ in range(180)]:
            if not all(u) or any(dot(a,u)==0 for a,_ in edges) or sorted(map(abs,u),reverse=True)[0]==sum(sorted(map(abs,u),reverse=True)[1:]):continue
            expected=predicted_count(c,u)
            assert crossing_count(edges,u)==expected,(c,u,'edge')
            actual=hull_count(v,u)
            assert actual==expected,(c,u,actual,expected)
            cases+=1
        print('HALFSPACE_AND_EDGE_GRAPH_OK',str(c),'vertices',len(v),'facets',len(facets(c)),'edges',len(edges))
    p=12/pi*atan(3-2*sqrt(2))
    assert 0.6489<p<0.6492
    rng=random.Random(819273)
    n=400000
    count=0
    for _ in range(n):
        import math
        x=rng.gauss(0,1);y=rng.gauss(0,1);z=rng.gauss(0,1)
        t=sorted((abs(x),abs(y),abs(z)),reverse=True)
        if t[0]>t[1]+t[2]:count+=1
    empirical=count/n
    assert abs(empirical-p)<0.005,(p,empirical)
    print('ALL_96_SIGNED_CHAMBER_REPRESENTATIVES_CHECKED_OK')
    print('EXACT_RATIONAL_HULL_VS_EDGE_SILHOUETTES_OK',cases)
    print('SPHERICAL_CONE_SOLID_ANGLE_AND_HAAR_CHECK_OK',format(p,'.15f'),format(empirical,'.6f'))
    print('ALL_CUBE_OCTAHEDRON_SHADOW_CHECKS_OK')

if __name__=='__main__':main()
