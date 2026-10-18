#!/usr/bin/env python3
"""Independent finite example checks for the zonotope/flag-product formulas."""
from itertools import product, combinations
from math import gcd, pi
from functools import reduce
import numpy as np
from scipy.spatial import ConvexHull
from fractions import Fraction

CASES = [
    ('parallelotope', [[1,0,0],[0,1,0],[0,0,1]], 12),
    ('hexagonal prism', [[1,0,0],[0,1,0],[1,1,0],[0,0,1]], 18),
    ('generic four directions', [[1,0,0],[0,1,0],[0,0,1],[1,1,1]], 24),
    ('octagonal prism', [[1,0,0],[0,1,0],[1,1,0],[1,2,0],[0,0,1]], 24),
    ('generic five directions', [[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3]], 40),
]

def edge_count_formula(gs):
    ks=[]
    for i,g in enumerate(gs):
        normals=set()
        for j,h in enumerate(gs):
            if i==j: continue
            v=np.cross(np.asarray(g,dtype=int),np.asarray(h,dtype=int))
            d=reduce(gcd,[abs(int(z)) for z in v])
            assert d>0
            q=[int(z)//d for z in v]
            if next(z for z in q if z)!=abs(next(z for z in q if z)):
                q=[-z for z in q]
            normals.add(tuple(q))
        ks.append(len(normals))
    return 2*sum(ks),ks

def edge_count_hull(gs):
    gs=np.array(gs,dtype=float)
    points=np.array([np.sum(gs*np.array(signs)[:,None],axis=0) for signs in product([-1,1],repeat=len(gs))])
    hull=ConvexHull(points)
    # Scipy facets triangulated. Equal support-normal planes are one face.
    facets=set(tuple(np.round(eq,8)) for eq in hull.equations)
    vertices=len(hull.vertices)
    return vertices+len(facets)-2

for label,gs,expected in CASES:
    count,ks=edge_count_formula(gs)
    hull_count=edge_count_hull(gs)
    assert count==hull_count==expected,(label,count,hull_count,expected)
    print(label,'E =',count,'sector counts =',ks)

# Independent exact planar polarity and shoelace for affine-regular hexagon.
base=np.array([[1,0],[0,1],[1,1]],dtype=int)
points=np.array([sum((base[k]*s[k] for k in range(3)),start=np.zeros(2,dtype=int)) for s in product([-1,1],repeat=3)])
hull=ConvexHull(points)
verts=[tuple(map(int,points[k])) for k in hull.vertices]
def twice_area(vs):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(vs,vs[1:]+vs[:1])))
assert twice_area(verts)==24
polar=set()
for a,b in combinations(verts,2):
    det=a[0]*b[1]-a[1]*b[0]
    if det==0: continue
    x=Fraction(b[1]-a[1],det)
    y=Fraction(a[0]-b[0],det)
    if all(x*v[0]+y*v[1]<=1 for v in verts): polar.add((x,y))
assert len(polar)==6
from scipy.spatial import ConvexHull
pol=list(polar)
ph=ConvexHull(np.array(pol,dtype=float))
pv=[pol[k] for k in ph.vertices]
assert Fraction(twice_area(pv),2)==Fraction(3,4)
print('hexagon area=12, polar area=3/4, prism Mahler product=12, Winter flag bound=16')
assert 16-4*pi*pi/3>0
assert 64/3-16*pi*pi/9>16-4*pi*pi/3
print('prism gap >=',16-4*pi*pi/3, '; nonprism gap >=',64/3-16*pi*pi/9)
print('ALL EXAMPLE CHECKS PASSED')
