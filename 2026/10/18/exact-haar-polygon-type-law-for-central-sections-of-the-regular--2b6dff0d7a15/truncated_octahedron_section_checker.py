#!/usr/bin/env python3
"""Reproduce the exact central-section polygon law for a regular truncated octahedron.

Python 3 standard library only. Finite checks test the analytic edge/chamber
classification and independently reconstruct sections from their facet equations.
They are not offered as substitutes for the continuum proof.
"""
from itertools import permutations, product, combinations
from collections import Counter
from math import acos, atan, sqrt, pi
import random


def dot(a, b):
    return sum(x*y for x, y in zip(a,b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a,cross(b,c))


V=sorted({v for s,t in product((-1,1), repeat=2) for v in permutations((0,s,2*t))})
E=[(i,j) for i in range(len(V)) for j in range(i) if sum((a-b)**2 for a,b in zip(V[i],V[j]))==2]
assert len(V)==24 and len(E)==36
assert set(Counter([i for edge in E for i in edge]).values())=={3}
assert all(dot(V[i],V[i])==5 and dot(V[i],V[j])==4 for i,j in E)


def cross_count(u):
    signs=[dot(u,v) for v in V]
    assert all(s!=0 for s in signs)
    return sum(signs[i]*signs[j]<0 for i,j in E)


# Each row uses an exact integer representative of the indicated strict chamber.
# The three signs refer to x-2y, x-2z, and y-2z, in x>y>z>0.
rows=[('+++',(9,4,1),8),('++-', (9,4,3),10),
      ('-++',(7,4,1),6),('-+-',(7,4,3),8),('---',(5,4,3),6)]
for pattern,u,count in rows:
    x,y,z=u
    observed=''.join('+' if q>0 else '-' for q in (x-2*y,x-2*z,y-2*z))
    assert observed==pattern and cross_count(u)==count

# Solid angle of triangle with rays e1, (4,2,1), (2,1,1).
a=(1,0,0);b=(4,2,1);c=(2,1,1)
assert abs(det(a,b,c))==1
assert (dot(a,a),dot(b,b),dot(c,c))==(1,21,6)
assert (dot(a,b),dot(b,c),dot(c,a))==(4,11,2)
D=11+3*sqrt(14)+4*sqrt(6)+2*sqrt(21)
Omega=2*atan(1/D)
p10=12*Omega/pi
alpha=acos(4/5)
mu=36*alpha/pi
p8=(mu-6)/2-2*p10
p6=1-p8-p10
assert 0<p10<p8<p6<1
assert abs((6*p6+8*p8+10*p10)-mu)<1e-13
assert abs(sum((p6,p8,p10))-1)<1e-13

# Independently construct a generic section from the 14 defining halfspaces.
# The polytope is max|x_i|<=2, sum|x_i|<=3.  Each section vertex
# is the intersection of the slicing plane with two support planes.
facets=[]
for j in range(3):
    for s in (-1,1):
        a=[0,0,0];a[j]=s;facets.append((tuple(a),2.0))
for signs in product((-1,1),repeat=3):
    facets.append((signs,3.0))
assert len(facets)==14


def facet_section_count(u):
    pts=[]
    for (n1,h1),(n2,h2) in combinations(facets,2):
        d=det(n1,n2,u)
        if abs(d)<1e-10:continue
        t1=cross(n2,u);t2=cross(u,n1)
        p=tuple((h1*t1[k]+h2*t2[k])/d for k in range(3))
        if all(dot(n,p)<h+1e-8 for n,h in facets):
            if not any(sum((p[k]-q[k])**2 for k in range(3))<1e-12 for q in pts):
                pts.append(p)
    return len(pts)

rng=random.Random(2026)
for pattern,u,n in rows:
    assert facet_section_count(u)==n,(pattern,facet_section_count(u))
for _ in range(600):
    u=tuple(rng.gauss(0,1) for _ in range(3))
    a=cross_count(u)
    b=facet_section_count(u)
    assert a==b,(u,a,b)

# Monte Carlo probability reproduction is a check, not an infinite proof.
rng=random.Random(314159)
counts=Counter(cross_count(tuple(rng.gauss(0,1) for _ in range(3))) for _ in range(120000))
for n,p in [(6,p6),(8,p8),(10,p10)]:
    assert abs(counts[n]/120000-p)<0.007,(n,counts[n]/120000,p)
assert set(counts)=={6,8,10}
print('vertices',len(V),'edges',len(E),'chambers',len(rows))
print('spherical_triangle_solid_angle',format(Omega,'.15f'))
print('p6',format(p6,'.15f'),'p8',format(p8,'.15f'),'p10',format(p10,'.15f'))
print('expected_sides',format(mu,'.15f'))
print('independent_halfspace_sections',605,'Monte_Carlo',dict(counts))
print('PASS')
