#!/usr/bin/env python3
"""Exact independent finite checks for a uniform Delannoy difference theorem."""
from math import comb

def v2(a):
    assert a != 0
    z = abs(a)
    return (z & -z).bit_length() - 1

# Check the four low-degree coefficient denominators and the tail inequality.
from fractions import Fraction
coefficients = (Fraction(2), Fraction(1), Fraction(2,9), Fraction(1,36))
assert all(v2(c.denominator) <= 2 for c in coefficients)
assert all(k - (k.bit_length()-1) >= 3 for k in range(5,10001))
assert all(k + 1 - (k.bit_length()-1) >= 3 for k in range(3,10001))
assert [ (4*x+2*x*(x-1)*(2*x-1))%8 for x in range(4)] == [0,4,4,0]

N = 1500
D = [1,3]
for n in range(1,N):
    numerator = (6*n+3)*D[n]-n*D[n-1]
    assert numerator%(n+1)==0
    D.append(numerator//(n+1))
assert D[:9] == [1,3,13,63,321,1683,8989,48639,265729]

uniform_cases = 0
for x in range(128):
    poly = (4*x+2*x*(x-1)*(2*x-1))%8
    for h in (32,64,96,128):
        v = h&-h
        assert (D[x+h]-D[x])%v == 0
        q = ((D[x+h]-D[x])//v)*pow(h//v,-1,8)%8
        assert q==poly,(x,h,q,poly)
        uniform_cases += 1

shift_cases = 0
for b in range(64):
    if b%4 not in (1,2):continue
    for a in range(1,14,2):
        for r in range(5,9):
            i=b+a*2**r;j=b+a*2**(r+1)
            if j>N: continue
            assert v2(D[j]-D[i])==r+2,(b,a,r)
            shift_cases+=1
print(f'VERIFY_OK uniform_grid={uniform_cases} shift_grid={shift_cases} bound_k=10000 max_index={N}')
