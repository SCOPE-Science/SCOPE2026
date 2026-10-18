#!/usr/bin/env python3
"""Exact finite checks of the binomial-gcd prime-adic shell theorem."""
from math import comb, gcd

def vf_fact(n,p):
    ans=0
    while n:
        n//=p
        ans+=n
    return ans

def val_bin(q,k,p):
    return vf_fact(q*k,p)-vf_fact(k,p)-vf_fact((q-1)*k,p)

def primes(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

count=0
for n in range(3,1601):
    for p in primes(n):
        a=0; A=1
        while n%(A*p)==0:
            A*=p;a+=1
        if a<2:continue
        m=n//A
        if not (A//p<m<A and m%p):continue
        k=n-1;s=A//p-1;q=1+A*s
        assert 2<=q<=n
        assert val_bin(q,k,p)==1,('witness',p,a,m)
        vals=[val_bin(t,k,p) for t in range(2,n+1)]
        assert min(vals)==1,('exact-p-valuation',p,a,m)
        # Check all prime divisors of the gcd. A prime outside n is ruled out
        # by the published elementary forward-difference argument.
        for r in primes(n):
            actual=min(val_bin(t,k,r) for t in range(2,n+1))
            assert actual==(1 if r==p else 0),(n,r,actual)
        count+=1
# Completely independent direct integer gcd for smaller cases.
count_direct=0
for n in range(3,105):
    k=n-1
    g=0
    for q in range(2,n+1):
        g=gcd(g,comb(q*k,k))
        if g==1:break
    for p in primes(n):
        a=0;A=1
        while n%(A*p)==0:
            A*=p;a+=1
        m=n//A
        if a>=2 and A//p<m<A and m%p:
            assert g==p,(n,p,g)
            count_direct+=1
assert count>20
print('VERIFY_OK:',count,'full-range factorial-valuation tests;',count_direct,'direct integer-gcd tests')
