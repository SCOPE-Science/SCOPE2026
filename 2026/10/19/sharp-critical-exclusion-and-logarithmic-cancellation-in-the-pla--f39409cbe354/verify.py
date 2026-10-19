#!/usr/bin/env python3
"""Reproducibility checks for the Ricker critical-exclusion asymptotics.
Requires only the Python 3 standard library. Finite checks support, but do not
replace, the general analytic argument in RESULT.md.
"""
from fractions import Fraction as Q
import math

exact_cases = [
    (Q(13,10),Q(2,5),Q(3,5)),
    (Q(4,5),Q(3,10),Q(7,10)),
    (Q(8,5),Q(9,10),Q(4,5)),
    (Q(2,3),Q(1,2),Q(1,2)),
]
for r,a,b in exact_cases:
    g=1-a*b
    c=-a*g/r
    eta=g*g/2-b*c
    A=g*g-eta
    k=A/g
    assert c*r+a*g==0
    assert eta==g*g/2+a*b*g/r
    assert k==g/2-a*b/r


def snapshots(r,a,b,x,y,N):
    out={}
    for n in range(2*N+1):
        if n==N or n==2*N:
            out[n]=(x,y)
        if n<2*N:
            new_x=x*math.exp(r-x-a*y)
            new_y=y*math.exp(b*r-b*x-y)
            x,y=new_x,new_y
    return out

N=120000
for r0,a0,b0 in exact_cases:
    r,a,b=map(float,(r0,a0,b0))
    g=1-a*b
    target=g/2-a*b/r
    out=snapshots(r,a,b,r/2+0.2,0.3,N)
    x1,y1=out[N]
    x2,y2=out[2*N]
    observed=(1/y2-1/y1-g*N)/math.log(2)
    q_over_y2=(x2-r+a*y2)/(y2*y2)
    assert abs(observed-target)<0.005, (r,a,b,target,observed)
    assert abs(q_over_y2+a*g/r)<0.002, (r,a,b,q_over_y2)
    assert abs(N*y1-1/g)<0.005, (r,a,b,N*y1)
    print(f'r={r:.9g}, a={a:.9g}, b={b:.9g}: '
          f'log coefficient exact={target:.9g}, observed={observed:.9g}; '
          f'slaving ratio={q_over_y2:.9g}')
print('PASS: four exact-rational coefficient tests and four large-n trajectory tests')
