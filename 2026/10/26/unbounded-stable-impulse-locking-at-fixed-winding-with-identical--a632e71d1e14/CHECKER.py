#!/usr/bin/env python3
"""Numerical finite sanity checks supporting, not replacing, the analytic proof."""
import math
from scipy.optimize import brentq

def U(j,z):
    if j == 0:
        return 1.
    a,b=1.,2.*z
    for _ in range(1,j):
        a,b=b,2.*z*b-a
    return b

for m in (1,2,3,5,8,13):
    k=4*m-1
    eta=0.5
    def g(t):
        return 4*math.sin(t)*U(m-1,math.cos(2*t))*math.cos((2*m-1)*t)
    for t in (0.,0.27,0.9,1.57,math.pi/2,2.49,3*math.pi/2):
        assert abs(math.cos(t)*g(t)-math.sin(k*t)-math.sin(t))<1e-9
    def H(t):
        return math.sin(k*t)-eta*math.cos(t)
    points=[(j+.5)*math.pi/k for j in range(2*k)]
    roots=[brentq(H,points[j],points[(j+1)%(2*k)]+(2*math.pi if j==2*k-1 else 0.)) for j in range(2*k)]
    slopes=[k*math.cos(k*t)+eta*math.sin(t) for t in roots]
    assert len(roots)==2*k and all(abs(d)>1e-8 for d in slopes)
    assert sum(d<0 for d in slopes)==k and sum(d>0 for d in slopes)==k
    assert all(abs(H(t))<1e-9 for t in roots)
    print(f"m={m} k={k} roots={len(roots)} downward={sum(d<0 for d in slopes)}")
print('CHECKS_PASS')
