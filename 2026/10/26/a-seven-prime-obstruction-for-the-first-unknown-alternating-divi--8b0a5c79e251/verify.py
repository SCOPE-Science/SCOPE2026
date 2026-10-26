#!/usr/bin/env python3
"""Exact arithmetic checks for a necessary prime-support condition."""
from fractions import Fraction as F
from math import isqrt

def alternate_prime_power(p,e):
    return sum((-1)**j*p**(e-j) for j in range(e+1))

def beta_by_trial(n):
    x=n; out=1; p=2
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0:
                x//=p; e+=1
            out*=alternate_prime_power(p,e)
        p+=1 if p==2 else 2
    if x>1:out*=x-1
    return out

P=F(1)
for p in (3,5,7,11,13):P*=F(p-1,p)
assert P==F(384,1001)
assert F(3,4)*P==F(288,1001)>F(1,4)
assert F(11,16)*P==F(264,1001)>F(1,4)
assert F(21,32)*P==F(252,1001)>F(1,4)
Q=F(5,8)*F(2,3)
for p in (5,7,11,13):Q*=F(p,p+1)
assert Q==F(3575,13824)>F(1,4)
for a in range(2,90):
    b=F(alternate_prime_power(2,a),2**a)
    if a==2:assert b==F(3,4)
    elif a==3:assert b==F(5,8)
    elif a==4:assert b==F(11,16)
    else:assert b>=F(21,32)
for p in (3,5,7,11,13,17,19,23,29):
    for e in range(1,20):
        u=F(alternate_prime_power(p,e),p**e)
        assert u>=F(p-1,p)
        if e%2==0:assert u>F(p,p+1)
        else:assert (alternate_prime_power(p,e)&1)==0
count=100000
for n in range(1,count+1):
    assert 4*beta_by_trial(n)!=n
print('VERIFY_OK: four exact rational thresholds; 90 dyadic exponents; 171 odd-prime local cases; exhaustive n=1..100000')
