#!/usr/bin/env python3
"""Finite exact checks for the stated Cesaro self-commutator identities.
These arithmetic checks are not an infinite-dimensional proof.
"""
from fractions import Fraction as Q
import math

def a(j): return Q(1,(j+1)**2*(j+2))

def gram_entry(i,j,T):
    return sum((a(k) for k in range(max(i,j),T)),Q(0))

def matrix_entry(i,j,T):
    m=max(i,j)
    return sum((Q(1,(k+1)**2) for k in range(m,T)),Q(0))-Q(1,m+1)+Q(1,T+1)

# The infinite-tail correction has an exact finite rational form:
# replacing the two infinite series by finite sums leaves a common tail.
for T in (10,20,40):
    for i in range(6):
        for j in range(6):
            assert gram_entry(i,j,T)==matrix_entry(i,j,T)
    assert sum((Q(j+1)*a(j) for j in range(T)),Q(0))==1-Q(1,T+1)

for n in range(1,201):
    assert a(2*n-1)>=Q(1,12*n**3)
for n in range(2,400):
    J=math.ceil(2*math.log2(n))
    assert (2**J)*n>=n**3 and J<=2*n
    counts=n
    for j in range(J):
        L=math.ceil(2**(1.5*j))
        size=(2**j)*n
        counts+=(size+L-1)//L
        assert L*L<=4*(2**(3*j))
    assert counts<=7*n, (n,counts)
print('CESARO_SELF_COMMUTATOR_CUBIC_EXACT_ARITHMETIC_OK')
