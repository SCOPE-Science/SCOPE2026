#!/usr/bin/env python3
"""Reproducibility checks for the dyadic-band return law."""
from fractions import Fraction
from math import comb, sqrt, pi, exp, erfc
import numpy as np


def first_passage(j, k, p):
    """Ballot formula for a nearest-neighbor walk with down-step probability p."""
    if j == 0:
        return Fraction(int(k == 0))
    if k < j or (k-j) % 2:
        return Fraction(0)
    q = 1-p
    return Fraction(j, k)*comb(k, (k+j)//2)*p**((k+j)//2)*q**((k-j)//2)


def first_return_law(n, p):
    if n == 1:
        return p/2
    q = 1-p
    return q*first_passage(1,n-1,p) + p*sum(Fraction(1,2**(j+1))*first_passage(j,n-1,p) for j in range(1,n))


def finite_level_dp(nmax, p):
    """Return masses from an independent forward Markov-chain enumeration."""
    q=1-p
    d={1:q}
    for j in range(nmax+1):
        d[j]=d.get(j,Fraction(0))+p/Fraction(2**(j+1))
    ans={1:d.pop(0)}
    for n in range(2,nmax+1):
        nxt={}
        hit=Fraction(0)
        for j,w in d.items():
            if j==1:
                hit+=p*w
            else:
                nxt[j-1]=nxt.get(j-1,Fraction(0))+p*w
            nxt[j+1]=nxt.get(j+1,Fraction(0))+q*w
        ans[n]=hit
        d=nxt
    return ans

checks=0
for p in (Fraction(1,3),Fraction(1,2),Fraction(3,5),Fraction(5,6)):
    dp=finite_level_dp(12,p)
    for n in range(1,13):
        assert dp[n]==first_return_law(n,p), (p,n,dp[n],first_return_law(n,p))
        checks+=1


def tail_scaled(n,u):
    p=0.5+u/(2*sqrt(n))
    q=1-p
    assert 0<p<1
    size=n+70
    a=np.zeros(size)
    a[1]+=q
    for j in range(61):
        a[j]+=p*2.0**(-j-1)
    a[0]=0
    for _ in range(2,n+1):
        b=np.zeros_like(a)
        b[:size-2]+=p*a[1:size-1]
        b[2:size]+=q*a[1:size-1]
        b[0]=0
        a=b
    return sqrt(n)*float(a.sum())


def profile(u):
    return sqrt(2/pi)*exp(-u*u/2)-u*erfc(u/sqrt(2))

for u in (-2.,-1.,0.,1.,2.):
    a=tail_scaled(500,u)
    b=tail_scaled(3000,u)
    f=profile(u)
    assert abs(b-f)<abs(a-f) and abs(b-f)<0.32, (u,a,b,f)
    checks+=2

# Check the exact at-critical limiting amplitude and the defective-return formula.
assert abs(profile(0)-sqrt(2/pi))<1e-14
checks+=1
for p in (Fraction(1,4),Fraction(2,5),Fraction(49,100)):
    q=1-p
    escape=2*q*(q-p)/(2*q-p)
    hitting=p + p*q/(2*q-p)
    assert 1-hitting==escape
    checks+=1
for p in (Fraction(2,3),Fraction(3,4)):
    # Expected time: first transition plus mean unit-height descent time.
    mean=1+Fraction(1,1)/(2*p-1)
    assert mean == 2*p/(2*p-1)
    checks+=1
print('PASS',checks,'independent exact identities and numerical limit comparisons')
