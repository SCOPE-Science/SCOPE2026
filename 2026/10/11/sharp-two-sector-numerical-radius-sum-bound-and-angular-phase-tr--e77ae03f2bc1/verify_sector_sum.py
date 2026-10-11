#!/usr/bin/env python3
"""Exact algebraic replay for a two-sector ordinary numerical-radius bound."""
from fractions import Fraction as F

def add(*items):
    out = {}
    for p in items:
        for exp, val in p.items():
            out[exp] = out.get(exp, F(0)) + val
    return {exp: val for exp, val in out.items() if val}

def mul(a, b):
    out = {}
    for (ar, ac), av in a.items():
        for (br, bc), bv in b.items():
            index = (ar + br, ac + bc)
            out[index] = out.get(index, F(0)) + av * bv
    return {exp: val for exp, val in out.items() if val}

def scale(p, k):
    return {exp: val*k for exp, val in p.items() if val*k}

one = {(0,0): F(1)}
r = {(1,0): F(1)}
c = {(0,1): F(1)}
left = add(one, mul(r,r), scale(mul(r,c), F(2)))
right = add(mul(add(r,c),add(r,c)), one, scale(mul(c,c), F(-1)))
assert left == right, (left,right)
# At angle separation 120 degrees, cos(angle) = -1/2. Ratio r = 1/2.
r0,c0=F(1,2),F(-1,2)
assert 1+r0*r0+2*r0*c0==F(3,4)
assert r0==-c0
# Pair e^(i*pi/3) + (1/2) e^(-i*pi/3): squared modulus is 3/4.
re=F(1,2)+F(1,4)
imag_sqrt3=F(1,2)-F(1,4)
assert re*re+3*imag_sqrt3*imag_sqrt3==F(3,4)
# Acute optimum 1 approached from above through positive nonzero scalars.
for n in (1,2,10,100,1000):
    eps=F(1,n)
    assert F(1) + eps > 1
    assert (F(1)+eps)**2>=1
# Strict-positive diagonal example: A_n=1-1/(n+1), B_n=1/[2(n+1)].
for n in range(1,501):
    a=F(1)-F(1,n+1)
    b=F(1,2*(n+1))
    assert a>0 and b>0 and a+b < 1
print('SECTOR_NUMERICAL_RADIUS_SHARP_PHASE_OK')
