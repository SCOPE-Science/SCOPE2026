#!/usr/bin/env python3
"""Numerical diagnostics for the Laurent-series zero asymptotic; not a proof."""
import mpmath as mp
mp.mp.dps=65
L=mp.log(2)

def F(q,S,M=150):
    total=1/L
    for m in range(1,M+1):
        total+=(2*q*m/(1-mp.power(4,-q*m)))*((S/mp.power(4,q))**m+S**(-m))
    return total

for q in (3,5,10,20,40,80):
    root=mp.findroot(lambda S:F(q,S),(-2*q*L+1,-2*q*L+3))
    assert root < -1 and abs(root) < 2**q
    other=mp.power(4,q)/root
    assert other < -2**q and abs(other) < 4**q
    assert abs(F(q,root)) < mp.mpf('1e-45')
    assert abs(F(q,other)) < mp.mpf('1e-45')
    delta=root+2*q*L
    print(f'q={q:3d} inner={mp.nstr(root,19)} correction={mp.nstr(delta,16)}')
assert abs(mp.findroot(lambda S:F(80,S),(-2*80*L+1,-2*80*L+3))+160*L-2)<mp.mpf('.015')
print('CHECK_OK')
