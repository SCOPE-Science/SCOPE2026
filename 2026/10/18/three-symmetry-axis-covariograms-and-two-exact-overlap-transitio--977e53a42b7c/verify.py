#!/usr/bin/env python3
"""Independent geometric volume checks for three rhombic-dodecahedron covariograms.

Requires Python 3, numpy and scipy. No remote services or input files.
"""
from itertools import combinations,product
from math import sqrt,isclose
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import HalfspaceIntersection,ConvexHull

NORMALS=[]
for i,j in combinations(range(3),2):
    for si,sj in product((-1,1),repeat=2):
        a=[0.,0.,0.]
        a[i],a[j]=si,sj
        NORMALS.append(a)
NORMALS=np.asarray(NORMALS)

def direct_overlap(shift):
    h=np.asarray(shift,dtype=float)
    offsets=1-0.5*np.abs(NORMALS@h)
    if min(offsets)<=0:  # only strictly interior cases are passed here
        raise ValueError('Sample not in intersection interior')
    poly=HalfspaceIntersection(np.c_[NORMALS,-offsets],np.zeros(3)).intersections
    return ConvexHull(poly).volume

def A(t):
    return 2-2*t+t**3/3 if t<=1 else (2-t)**3/3 if t<=2 else 0.
def F(t):
    return (1-t)*(2-t) if t<=1 else 0.
def D(t):
    return 2-3*t if t<=0.5 else 4*(1-t)**3 if t<=1 else 0.

checks=0
for axis,formula,ts in [
    ((1,0,0),A,[.03,.13,.26,.49,.7,.92,1.07,1.43]),
    ((1,1,0),F,[.02,.16,.37,.48,.63,.84]),
    ((1,1,1),D,[.02,.14,.32,.41,.62,.75,.91])]:
    for t in ts:
        actual=direct_overlap([t*a for a in axis])
        assert isclose(actual,formula(t),rel_tol=1e-10,abs_tol=2e-11),(axis,t,actual,formula(t))
        checks+=1

def values(r):
    return D(r/sqrt(3)),F(r/sqrt(2)),A(r)
alpha=3*sqrt(2)-2*sqrt(3)
beta=brentq(lambda r: 2*r**3-9*r*r+(24-9*sqrt(2))*r-4,1,sqrt(2))
assert abs(values(alpha)[0]-values(alpha)[1])<1e-10
assert values(alpha)[0]>values(alpha)[2]
assert abs(values(beta)[1]-values(beta)[2])<1e-10
assert values(beta)[1]>values(beta)[0]
for r in [0.02,0.1,0.5,alpha/2]:
    v=values(r);assert v[0]>max(v[1:])
for r in [(alpha+beta)/2,.91,1.1]:
    v=values(r);assert v[1]>max(v[0],v[2])
for r in [1.32,1.53,1.72,1.96]:
    v=values(r);assert v[2]>max(v[:2])
assert 1<beta<sqrt(2)
print(f'PASS: {checks} halfspace intersection volumes and phase samples; alpha={alpha:.12f}, beta={beta:.12f}')
