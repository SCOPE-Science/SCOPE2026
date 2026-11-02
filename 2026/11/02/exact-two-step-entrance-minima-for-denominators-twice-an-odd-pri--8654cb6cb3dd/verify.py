#!/usr/bin/env python3
"""Exact independent checks for the two-step entrance theorem (stdlib only)."""
from fractions import Fraction
from math import gcd

def primes_below(n):
    sieve=[True]*n
    sieve[:2]=[False,False]
    for k in range(2,int(n**0.5)+1):
        if sieve[k]:
            for j in range(k*k,n,k):sieve[j]=False
    return [p for p in range(3,n,2) if sieve[p]]

def answer(p):
    if p==3:return 17
    if p%4==3:return p*p+3*p-3
    if p==5:return p*p+5*p-7
    if p in (13,17,29):return p*p+5*p-9
    return p*p+5*p-11

def T(x):
    q=x.numerator//x.denominator
    return q*(1+x-q)

interval_cases=0
for p in primes_below(500):
    m=2*p
    ans=answer(p)
    q0=(p+3)//2 if p%4==1 else (p+1)//2
    assert q0%2==0
    assert ans//m==q0
    r=ans%m
    assert gcd(r,m)==1
    d=m//gcd(q0,m)
    assert d>1 and (q0+(q0*r)//m)%d==0
    # At the first quotient, enumerate all reduced remainders independently.
    for z in range(1,r):
        if gcd(z,m)>1:continue
        assert (q0+(q0*z)//m)%d !=0
    # At earlier quotients prove impossibility by integer finite check.
    for q in range(2,q0):
        dd=m//gcd(q,m)
        for z in range(1,m):
            if gcd(z,m)==1:
                assert dd==1 or (q+(q*z)//m)%dd !=0
    interval_cases+=1
fraction_cases=0
for p in primes_below(110):
    m=2*p
    ans=answer(p)
    for a in range(2*m,ans+1):
        if gcd(a,m)>1:continue
        x=Fraction(a,m)
        y=T(x)
        is_exact_two=(y.denominator>1 and T(y).denominator==1)
        assert is_exact_two==(a==ans), (p,a,ans)
        fraction_cases+=1
print('VERIFY_OK', 'prime_cases='+str(interval_cases),'exact_fraction_numerators='+str(fraction_cases))
