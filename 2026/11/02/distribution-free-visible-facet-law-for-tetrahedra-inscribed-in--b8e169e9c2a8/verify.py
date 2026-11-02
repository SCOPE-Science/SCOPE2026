#!/usr/bin/env python3
"""Exact sign-orbit and independent sampling checks for a tetrahedral visibility law.
Only the standard Python library is required. These are finite checks, not a substitute for the general proof.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from random import Random
from math import sqrt


def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def barycentric_of_origin(points):
    v1,v2,v3,v4=points
    a,b,c=[sub(v,v4) for v in (v1,v2,v3)]
    rhs=tuple(-x for x in v4)
    D=det(a,b,c)
    if D==0:raise ValueError('affinely degenerate')
    l1=det(rhs,b,c)/D
    l2=det(a,rhs,c)/D
    l3=det(a,b,rhs)/D
    return (l1,l2,l3,1-l1-l2-l3)

def visible_facets(points):
    V=0
    for i in range(4):
        a,b,c=(points[j] for j in range(4) if j!=i)
        normal=cross(sub(b,a),sub(c,a))
        vs=dot(normal,sub(points[i],a))
        os=-dot(normal,a)
        if vs==0 or os==0:raise ValueError('facet degenerate or origin coplanar')
        if vs*os<0:V+=1
    return V

# Four exact rational points on the Euclidean unit sphere.
base=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),(F(1,9),F(4,9),F(8,9)))
assert all(dot(v,v)==1 for v in base)
counts=Counter()
for signs in product((-1,1),repeat=4):
    points=[tuple(s*x for x in v) for s,v in zip(signs,base)]
    lam=barycentric_of_origin(points)
    assert all(x!=0 for x in lam)
    v=sum(x<0 for x in lam)
    assert v==visible_facets(points)
    assert v<=2
    counts[v]+=1
assert counts==Counter({0:2,1:8,2:6}),counts
print('EXACT_ALL_16_ANTIPODAL_SIGN_CONFIGURATIONS_AND_FACET_TESTS_PASSED')

# An invertible affine stretch preserves barycentric signs and visible-facet counts.
for scales in ((F(2),F(3),F(5)),(F(1,3),F(7),F(2))):
    for signs in product((-1,1),repeat=4):
        points=[tuple(s*x*k for x,k in zip(v,scales)) for s,v in zip(signs,base)]
        assert visible_facets(points)==sum(x<0 for x in barycentric_of_origin(points))
print('EXACT_TWO_DISTINCT_ELLIPSOID_SIGN_ORBITS_PASSED')

# Boundary condition is substantive: a small interior point gives three exterior facets.
inside=[(F(1,10),F(1,10),F(1,10)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
lam=barycentric_of_origin(inside)
assert lam==(F(10,7),-F(1,7),-F(1,7),-F(1,7))
assert visible_facets(inside)==3
print('EXACT_INTERIOR_SAMPLING_THREE_VISIBLE_FACETS_COUNTEREXAMPLE_PASSED')

rng=Random(803028)
expected={0:0.125,1:0.5,2:0.375}
for model in ('sphere','anisotropic_noniid_ellipsoid','anisotropic_noniid_l4_boundary'):
    n=14000
    ct=Counter()
    for _ in range(n):
        pts=[]
        for i in range(4):
            scales=(1,1,1) if model=='sphere' else (1+0.3*i,2+0.2*i,0.8+0.1*i)
            v=[rng.gauss(0,scales[j]) for j in range(3)]
            if model=='anisotropic_noniid_l4_boundary':
                norm=sum(abs(x)**4 for x in v)**.25
            else:
                norm=sqrt(sum(x*x for x in v))
            v=[x/norm for x in v]
            if model=='anisotropic_noniid_ellipsoid':v=[x*s for x,s in zip(v,(2,3,5))]
            pts.append(v)
        lam=barycentric_of_origin(pts)
        ct[sum(x<0 for x in lam)]+=1
    assert ct[3]==0
    assert all(abs(ct[k]/n-p)<0.025 for k,p in expected.items()),(model,ct)
    print('NONIID_ANTIPODAL_SURFACE_DIAGNOSTIC_PASSED',model,tuple(ct[k] for k in range(3)))
print('ALL_CHECKS_PASSED')
