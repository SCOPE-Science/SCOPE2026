#!/usr/bin/env python3
"""Finite sanity checks for the self-contained Bessel-zero identities.

This does not prove the quantified theorem. No third-party packages required.
"""
import math
p = math.pi
D = p*p/4 - 2 - 2/(p*p)
assert D > 0

def eq(x):
    return math.sin(x) - x*math.cos(x)

def positive_zero(n):
    a=n*p+1e-9
    b=(n+0.5)*p-1e-9
    fa=eq(a)
    assert fa*eq(b)<0
    for _ in range(70):
        m=(a+b)/2
        if fa*eq(m)<=0:
            b=m
        else:
            a=m
            fa=eq(a)
    return (a+b)/2

roots=[positive_zero(n) for n in range(1,31)]
for n,x in enumerate(roots,1):
    u=(n+0.5)*p-x
    delta=((n+0.5)*p-x)*((n+0.5)*p+x)
    assert 2 < delta < 2+1/(p*p)
    assert abs(u-math.atan(1/x))<1e-9
for a in roots:
    for b in roots:
        for c in roots:
            assert abs(a*a+b*b-c*c) > D - 1e-9
for a in roots[:8]:
    for b in roots[:8]:
        for c in roots[:8]:
            for d in roots[:8]:
                if abs((a+b)-(c+d)) < 1e-10:
                    assert sorted((a,b))==sorted((c,d))
print('CHECK_OK: 30 zeros, all 27000 ordered square triples, 4096 sum quadruples; finite sanity only')
