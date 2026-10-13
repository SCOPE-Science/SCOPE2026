#!/usr/bin/env python3
"""Exact rational spot checks of the printed QRT periodicity identities."""
from fractions import Fraction as Q

INF = None

def smooth(b, g):
    return g * ((b + 2)**2 - 4*g) * ((b - 2)**2 - 4*g) != 0

def step(pt, b, g):
    x, y = pt
    if x is INF:
        assert y in (Q(1),Q(-1))
        return (-y, INF)
    if x in (Q(1), Q(-1)):
        if y is INF:
            if b == 0:
                return (INF, x)
            t = (g-Q(1))/b
            return (-x*t,x)
        assert b != 0
        return (INF,x)
    assert y is not INF
    return (-y - b*x/(x*x-1),x)

def order_at_origin(b, g, max_steps=12):
    assert smooth(b,g)
    o = (INF,Q(1)); z=o
    for k in range(1,max_steps+1):
        z=step(z,b,g)
        if z == o:
            return k
    return None

def f5(b,g):
    return (g-1-b)*(g-1+b)**2-b**3*(g-1)

assert order_at_origin(Q(1),Q(2)) == 3
assert order_at_origin(Q(0),Q(2)) == 4
assert order_at_origin(Q(1),Q(1)) == 4
assert order_at_origin(Q(9,2),Q(10)) == 5
for t in [Q(i,2) for i in range(-13,14) if i not in (0,-2,2)]:
    b=(t-1)*(t+1)**2/t
    g=t*(t*t+t-1)
    lhs=g*((b+2)**2-4*g)*((b-2)**2-4*g)
    rhs=(t-1)**5*(t+1)**5*(t*t-4*t-1)*(t*t+t-1)/t**3
    assert lhs == rhs
    assert f5(b,g) == 0
    if smooth(b,g):
        assert order_at_origin(b,g) == 5
for b in [Q(i,2) for i in range(-14,15)]:
    if smooth(b,Q(1)):
        assert order_at_origin(b,Q(1)) == 4
    if smooth(b,Q(1)+b):
        assert order_at_origin(b,Q(1)+b) == 3
print('VERIFY_OK')
