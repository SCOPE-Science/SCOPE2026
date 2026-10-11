#!/usr/bin/env python3
"""Numerical stress tests for explicit prime-period-two formulas.

This script checks examples; the real-parameter completeness proof is algebraic.
"""
from math import sqrt, isclose


def step(p, a, b):
    x, y = p
    return (y, a*y-y*y*y-b*x)


def close_pair(a, b, p):
    p1 = step(p,a,b)
    p2 = step(p1,a,b)
    assert all(isclose(x,y,rel_tol=1e-10,abs_tol=1e-10) for x,y in zip(p,p2))
    assert abs(p1[0]-p[0])+abs(p1[1]-p[1])>1e-9


def orbit_data(a,b):
    B=1+b
    ac=sqrt((9*B*B+(1-b)*(1-b))/2)
    r=sqrt(a+B)
    close_pair(a,b,(r,-r))
    ta=(-2*a-3*B)**2-2*b
    assert ta>1+b*b
    if a>2*B:
        u=(sqrt(a+2*B)+sqrt(a-2*B))/2
        v=(sqrt(a+2*B)-sqrt(a-2*B))/2
        assert isclose(u*v,B,rel_tol=1e-11)
        assert isclose(u*u+v*v,a,rel_tol=1e-11)
        close_pair(a,b,(u,v))
        close_pair(a,b,(-u,-v))
        tr=(a-3*u*u)*(a-3*v*v)-2*b
        assert isclose(tr,-2*a*a+9*B*B-2*b,rel_tol=1e-10,abs_tol=1e-10)
        spectral_sink=(-1-b*b<tr<1+b*b)
        assert spectral_sink==(a<ac)
    assert ac>2*B
    return ac


for b in (0.02,0.2,0.8,0.98):
    lower=2*(1+b)
    ac=sqrt((9*(1+b)**2+(1-b)**2)/2)
    for a in (0,1,lower-0.02,lower+0.01,(lower+ac)/2,ac+0.02,3*ac):
        orbit_data(a,b)
    assert isclose(-2*ac*ac+9*(1+b)**2-2*b,-1-b*b,abs_tol=1e-11)
assert isclose(orbit_data(2.55,0.2),sqrt(34/5),abs_tol=1e-12)
print('Explicit period-two formulas and sampled spectral inequalities: OK')
