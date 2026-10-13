#!/usr/bin/env python3
"""Reproducible finite checks of a symbolic divisor-power localization theorem."""
import math
from decimal import Decimal, getcontext
getcontext().prec=70

def direct_sigma_power(n,d):
    total=0
    for a in range(1,math.isqrt(n)+1):
        if n%a==0:
            total+=a**d
            b=n//a
            if b!=a:total+=b**d
    return total

checks=0
for d in (6,8,10,12,14,16,20,30,50):
    u=Decimal(2)**(-d)
    q=(Decimal(2)/3)**d
    v=Decimal(3)**(-d)
    assert q+3*u<Decimal('0.135')
    assert q*q/u<Decimal('0.5')
    assert 6*q<Decimal('0.528')
    assert 9*u<Decimal('0.141')
    assert 1-q-3*u>Decimal('0.865')
    # worst-case error bound from exact inversion
    bound=Decimal(1)/d+3+((q+3*u)**2/u)/(1-q-3*u)
    assert bound<5,(d,bound)
    checks+=1

matches={}
for d in (6,8,10):
    upper={6:1800,8:5000,10:20000}[d]
    last=direct_sigma_power(1,d)
    pairs=[]
    for n in range(1,upper):
        nxt=direct_sigma_power(n+1,d)
        if last==nxt:
            alpha=int(n%3==0)-int((n+1)%3==0)
            # exact rational strict comparison: use high-precision Decimal
            nn=Decimal(n); dd=Decimal(d)
            target=dd*Decimal(2)**d-alpha*dd*(Decimal(4)/3)**d
            assert n%2==0 and abs(nn-target)<5*dd
            pairs.append(n)
        last=nxt
    matches[d]=pairs
print('VERIFY_OK')
print('uniform_error_bound_exponents_checked=',checks)
print('finite_neighbor_checks=',sum(({6:1800,8:5000,10:20000}[d]-1) for d in matches))
print('observed_equal_neighbor_starts=',matches)
print('non-exhaustive_finite_check=True')
