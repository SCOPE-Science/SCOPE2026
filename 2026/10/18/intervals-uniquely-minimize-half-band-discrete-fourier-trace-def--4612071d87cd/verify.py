#!/usr/bin/env python3
"""Exact finite diagnostics for the half-band trace-defect interval theorem."""
from fractions import Fraction
from itertools import combinations
from math import comb, pi

def edges(A,r):
    return sum(1 for x,y in combinations(A,2) if (y-x)%2 and (y-x)<=2*r+1)

def energy(A):
    return sum((Fraction(1,(y-x)**2) for x,y in combinations(A,2) if (y-x)%2),Fraction(0))

def components(A):
    return 1+sum(y>x+1 for x,y in zip(A,A[1:]))

count=0
for N in range(2,8):
    I=tuple(range(N))
    EI=energy(I)
    for A in combinations(range(12),N):
        for r in range(7):
            assert edges(A,r)<=edges(I,r),(A,r)
        E=energy(A)
        c=components(A)
        assert E<=EI,A
        assert EI-E>=Fraction(8,9)*(c-1),A
        assert (E==EI)==(c==1),A
        count+=1
assert energy((0,1))-energy((0,3))==Fraction(8,9)
# Independently compute the two-by-two trace deficit of kernel [1/2,1/pi;1/pi,1/2].
trT=1.0
trT2=2*(0.5**2)+2*(1/pi)**2
assert abs((trT-trT2)-(0.5-2/pi**2))<1e-14
print('PASS: exact rational subset/edge/gap checks:', count)
print('PASS: sharp two-point penalty and matrix trace normalization')
