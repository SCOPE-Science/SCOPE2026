#!/usr/bin/env python3
"""Finite reproducibility diagnostics for a generalized Cesaro diagonal commutator.
This is a finite arithmetic check, not a proof of an infinite operator theorem.
No external packages are required.
"""
from fractions import Fraction as F
import math

def finite_matrix(N, t):
    total=F(0)
    for n in range(1,N+1):
        for m in range(1,n):
            k=F(n-m,n*n*m)*t**(n-m)
            total += k*k
    return total

def finite_gap(N,t):
    out=F(0)
    for d in range(1,N):
        a=F(0)
        for m in range(1,N-d+1):
            n=m+d
            a+= F(d*d,n**4*m*m)
        out += a*t**(2*d)
    return out

count=0
for N in range(2,16):
    for t in (F(0),F(1,5),F(1,2),F(3,4),F(1)):
        assert finite_matrix(N,t)==finite_gap(N,t)
        count+=1

# Coefficients by direct summation, with explicitly finite truncation.
def coeff(alpha,d,N=120000):
    return math.fsum(((m**(-alpha)-(m+d)**(-alpha))/(m+d))**2 for m in range(1,N+1))

for alpha in (0.25,0.5,1.0):
    a100=coeff(alpha,100)
    a200=coeff(alpha,200)
    assert a100>0 and a200>0
    assert a200<a100

# The exact classical answer exceeds finite positive partial sums.
from math import pi
zeta3=sum(1.0/n**3 for n in range(1,300000))+1/(2*299999**2)
zeta4=pi**4/90
limit=zeta3-.75*zeta4
partial=float(finite_matrix(50,F(1)))
assert 0<partial<limit and abs(limit-0.39031447787624)<0.00001
print('PASS:',count,'exact rational identity cases and 3 finite coefficient diagnostics; classical corner bracketed')
