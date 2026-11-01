#!/usr/bin/env python3
"""Exact rational spectral checks for ternary simplex-product harmonic sampling.
The finite check is supplementary to the analytic all-degree argument.
"""
from fractions import Fraction as Q
from math import comb, factorial


def normalised_gegenbauer_at_h(d, kmax):
    D = 2*d
    values = [[Q(1) for _ in range(d+1)],
              [Q(2*d-3*h, 2*d) for h in range(d+1)]]
    for k in range(2, kmax+1):
        a=Q(2*k+D-4,k+D-3)
        b=Q(k-1,k+D-3)
        values.append([a*Q(2*d-3*h,2*d)*values[-1][h]-b*values[-2][h]
                       for h in range(d+1)])
    return values[:kmax+1]


def eigenvalue(d,k,j,rows):
    total=Q(0)
    for h,p in enumerate(rows[k]):
        coeff=sum((-1)**i*2**(h-i)*comb(j,i)*comb(d-j,h-i)
                  for i in range(max(0,h-(d-j)),min(j,h)+1))
        total+=coeff*p
    return total


def expected(d,k,j):
    if j>k: return False
    if k==0: return j==0
    if k==1: return j==1
    if k==2: return j in (1,2)
    return True

checks=0
for d in range(2,11):
    rows=normalised_gegenbauer_at_h(d,24)
    for k in range(25):
        assert rows[k][0]==1
        observed_rank=0
        wanted_rank=0
        for j in range(d+1):
            ev=eigenvalue(d,k,j,rows)
            assert ev>=0,(d,k,j,ev)
            assert (ev>0)==expected(d,k,j),(d,k,j,ev)
            multiplicity=comb(d,j)*2**j
            if ev: observed_rank+=multiplicity
            if expected(d,k,j): wanted_rank+=multiplicity
            checks+=1
        assert observed_rank==wanted_rank,(d,k,observed_rank,wanted_rank)
        if k>=d and k>=3:
            assert observed_rank==3**d

# Verify the null-quadric witness coefficients by independent factorial sums.
for k in range(3,61):
    if k%3==0 or k%3==1:
        term=Q(1,2*factorial(k-2))-Q(1,factorial(k-3))
        if k>=4:
            term+=Q(1,4*factorial(k-4))
        assert term==Q(k*k-9*k+16,4*factorial(k-2))
        assert term!=0
        checks+=1
    if k%3==2:
        val=Q(1,factorial(k-1))-Q(1,factorial(k-2))
        assert val==Q(2-k,factorial(k-1)) and val!=0
        checks+=1
print('TERNARY_HARMONIC_RANK_CHECK_OK',checks)
