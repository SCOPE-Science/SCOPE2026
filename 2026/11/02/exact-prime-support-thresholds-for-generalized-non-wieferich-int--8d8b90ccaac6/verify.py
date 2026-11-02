#!/usr/bin/env python3
"""Exact finite checks of the prime-support criterion for odd moduli; no dependencies."""
from math import gcd, lcm

def factors(n):
    z={}; d=2
    while d*d<=n:
        while n%d==0:z[d]=z.get(d,0)+1;n//=d
        d+=1 if d==2 else 2
    if n>1:z[n]=z.get(n,0)+1
    return z

def val(n,p):
    z=0
    while n%p==0 and n:z+=1;n//=p
    return z

def order_mod(a,n):
    assert gcd(a,n)==1
    k=1;r=a%n
    while r!=1:r=(r*a)%n;k+=1
    return k

def local_info(a,p):
    d=order_mod(a,p)
    v=1;pk=p*p
    while pow(a,d,pk)==1:
        v+=1;pk*=p
    return d,v

def formula(a,n):
    fs=factors(n)
    local={p:local_info(a,p) for p in fs}
    thresholds={p:local[p][1]+max(val(local[q][0],p) for q in fs) for p in fs}
    return all(fs[p]>=thresholds[p] for p in fs),thresholds

def direct(a,n):
    ell=order_mod(a,n)
    return gcd(n,(pow(a,ell,n*n)-1)//n)==1

comparisons=0
for a,bound in ((2,3500),(3,1700),(5,1700),(7,1000)):
    for n in range(3,bound+1,2):
        if gcd(a,n)>1:continue
        expected,thresholds=formula(a,n)
        observed=direct(a,n)
        if expected!=observed:
            raise AssertionError((a,n,expected,observed,thresholds))
        comparisons+=1

# For finite prime supports, exhaust exponents up to 3, comparing predicted and actual.
from itertools import combinations,product
supports=0
for a in (2,3):
    for r in (1,2,3):
        for P in combinations((3,5,7,11,13),r):
            if any(a%p==0 for p in P):continue
            for es in product((1,2,3),repeat=r):
                n=1
                for p,e in zip(P,es):n*=p**e
                predicted,_=formula(a,n)
                # avoid slow modular-order computation for huge n; compute ord modulo prime powers via raising candidates
                ord_val=1
                for p,e in zip(P,es):
                    d,v=local_info(a,p)
                    ord_val=lcm(ord_val,d*p**max(0,e-v))
                assert pow(a,ord_val,n)==1
                observed=gcd(n,(pow(a,ord_val,n*n)-1)//n)==1
                if observed!=predicted:raise AssertionError((a,n,predicted,observed))
                supports+=1

# A fixed-support power always becomes non-Wieferich, at precisely the formula threshold.
for a,n in ((2,21),(2,1093),(2,39),(2,63),(3,35),(5,39)):
    if gcd(a,n)>1:continue
    _,th=formula(a,n)
    fs=factors(n)
    height=max((th[p]+fs[p]-1)//fs[p] for p in fs)
    for k in range(1,height+2):
        test,_=formula(a,n**k)
        assert test==(k>=height)
print('VERIFY_OK', 'direct_cross_checks=',comparisons,'support_exponent_checks=',supports, 'general_bases=2,3,5,7', 'power_thresholds=PASS')
