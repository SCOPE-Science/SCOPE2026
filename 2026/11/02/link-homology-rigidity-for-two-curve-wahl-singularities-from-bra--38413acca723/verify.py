#!/usr/bin/env python3
"""Independent exact-integer checks for the linked plumbing calculation.
General proof is in RESULT.md; bounded arithmetic tests do not prove it.
"""
from fractions import Fraction
from math import gcd, isqrt

def invariants(a,k):
    assert a>=1 and k>=1
    g=2*a+k+1; r=2*k; d=4*a+2*k
    b=4*g+r-1
    t=d*d-r*r
    s1=gcd(d,r)
    s2=t//s1
    w=Fraction(-r*(d+r),d-r)
    return b,t,s1,s2,w

def inverse(b,t):
    u=(b-3)//2
    disc=u*u-3*t//4
    root=isqrt(disc)
    assert root*root==disc
    a=(u-root)//2
    k=(u-4*a)//3
    assert a>=1 and k>=1 and 8*a+6*k+3==b
    return a,k

seen={}
count=0
for a in range(1,101):
    for k in range(1,101):
        b,t,s1,s2,w=invariants(a,k)
        assert s2%s1==0
        assert inverse(b,t)==(a,k)
        assert w==-2*k-Fraction(2*k*k,a)
        assert w < -2
        prev=seen.get((b,t))
        assert prev is None or prev==(a,k)
        seen[(b,t)]=(a,k)
        count+=1
for n in range(3,1001):
    if n%2==0:
        s=n//2; k=s-1; a=(s-1)**2
    else:
        s=(n-1)//2; k=s; a=2*s*s
    assert invariants(a,k)[4]==-n
assert invariants(2,1)==(25,96,2,48,Fraction(-3,1))
assert invariants(1,1)==(17,32,2,16,Fraction(-4,1))
assert invariants(8,2)==(79,1280,4,320,Fraction(-5,1))
print(f'VERIFY_OK: {count} parameter pairs; 998 integer realizations; 3 examples')
