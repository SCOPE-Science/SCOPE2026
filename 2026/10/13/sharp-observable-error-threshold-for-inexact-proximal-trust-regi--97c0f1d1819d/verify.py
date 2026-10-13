#!/usr/bin/env python3
"""Exact-rational checks for scalar sharpness witnesses (not a general proof)."""
from fractions import Fraction as F

def check(k, g, u, eps, expected_q):
    x = F(0)
    r = F(1)
    p = x - r*g
    h = lambda v: (v-(x-r*g))**2/(2*r)
    assert h(u)-h(p) == eps**2/(2*r)
    assert eps <= k*abs(u-x)
    assert g*(u-x) == expected_q

for k in [F(0), F(1,10), F(1,4), F(1,2), F(3,4), F(9,10), F(99,100)]:
    check(k, -(1-k), F(1), k, -(1-k))
    assert (1-k)*2 == 1+(1-k)**2-k**2

for d in [F(1,3),F(1,100),F(1,10000)]:
    check(F(1), -d, F(1), 1-d, -d)
    assert -d < 0

for k in [F(11,10),F(5,4),F(3,2),F(2)]:
    check(k,k-1,F(1),k,k-1)
    assert k-1>0

print('VERIFY_OK')
