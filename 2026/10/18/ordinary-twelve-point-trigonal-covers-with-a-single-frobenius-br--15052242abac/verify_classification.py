#!/usr/bin/env python3
"""Exact finite-field verification of the degree-five and degree-seven cases.

All polynomial coefficients are in F_3, with the constant coefficient first.
Only standard-library integer arithmetic is used.
"""
from itertools import product
from math import gcd

def trim(f):
    f=list(f)
    while len(f)>1 and f[-1]==0:f.pop()
    return tuple(f)

def add(f,g):
    return trim([( (f[i] if i<len(f) else 0)+(g[i] if i<len(g) else 0))%3 for i in range(max(len(f),len(g)))])

def neg(f): return tuple((-a)%3 for a in f)

def mul(f,g):
    r=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):r[i+j]=(r[i+j]+a*b)%3
    return trim(r)

def divmod_poly(f,g):
    f=list(trim(f));g=trim(g)
    q=[0]*max(1,len(f)-len(g)+1)
    while len(f)>=len(g) and f!=[0]:
        t=f[-1]*pow(g[-1],-1,3)%3;i=len(f)-len(g);q[i]=t
        for j,b in enumerate(g): f[i+j]=(f[i+j]-t*b)%3
        f=list(trim(f))
    return trim(q),tuple(f)

def rem(f,g): return divmod_poly(f,g)[1]

def gcd_poly(f,g):
    while g!=(0,): f,g=g,rem(f,g)
    return trim([(c*pow(f[-1],-1,3))%3 for c in f])

def powmod(f,e,m):
    out=(1,)
    while e:
        if e&1:out=rem(mul(out,f),m)
        f=rem(mul(f,f),m);e//=2
    return out

def primes(n):return [d for d in range(2,n+1) if n%d==0 and all(d%j for j in range(2,int(d**0.5)+1))]

def irreducible(f):
    n=len(f)-1;x=(0,1)
    if n<1:return False
    for p in primes(n):
        if gcd_poly(f,add(powmod(x,3**(n//p),f),neg(x)))!=(1,):return False
    return add(powmod(x,3**n,f),neg(x))==(0,)

def comp(f,a,b):
    result=(0,)
    for c in reversed(f):result=add(mul(result,(b,a)),(c,))
    return tuple((c*pow(a,-len(f)+1,3))%3 for c in result)

def enumerate_degree(n):
    polys={f for cs in product(range(3),repeat=n) if irreducible(f:=tuple(cs)+(1,))}
    assert len(polys)==(3**n-3)//n, (n,len(polys))
    group=[(a,b) for a in (1,2) for b in range(3)]
    orbits=[];seen=set();representatives=[]
    for f in sorted(polys):
        if f in seen:continue
        orb={comp(f,a,b) for a,b in group}
        assert orb.issubset(polys) and len(orb)==6,(n,f,orb)
        seen|=orb
        orbits.append(orb)
        representatives.append(f)
    assert len(seen)==len(polys)
    assert len(orbits)==len(polys)//6
    # Each monic irreducible polynomial has nonzero values at 0, 1, 2.
    assert all(all(sum(c*pow(x,i,3) for i,c in enumerate(f))%3 for x in range(3)) for f in polys)
    print(f"n={n}; genus={2*n-2}; polynomials={len(polys)}; F3-isomorphism classes={len(orbits)}; free affine orbit size=6")
    print("lexicographically first representative Q constant-first:", representatives[0])

if __name__=='__main__':
    for degree in (5,7):enumerate_degree(degree)
