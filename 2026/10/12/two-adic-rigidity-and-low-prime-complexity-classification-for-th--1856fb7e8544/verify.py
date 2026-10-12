#!/usr/bin/env python3
"""Finite checks for a theorem on D(sigma(2^a*p)-2^a*p).
Finite tests are illustrations; the unrestricted assertion uses the written proof.
"""
from math import isqrt

def factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d; e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

def D(n):
    if n==1: return 0
    return sum(e*(n//p) for p,e in factors(n))

def omega(n):
    return sum(e for p,e in factors(n))

def isprime(n):
    if n<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0: return n==p
    d=n-1; s=0
    while d%2==0:
        d//=2; s+=1
    # Deterministic Miller-Rabin for 0 <= n < 2**64.
    if n >= 1<<64: raise ValueError('only 64-bit primality range checked')
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        a%=n
        if a==0: continue
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True

def claimed(a,p):
    if a==2: return p==71
    t=1<<a
    q=(t*(2*t-1))//4+t-1
    return p==2*t+3 and isprime(q)

cases=solutions=restricted=0
for a in range(2,11):
    t=1<<a
    for p in range(3,3001,2):
        if not isprime(p): continue
        n=t*p; S=(t-1)*p+2*t-1
        ok=(D(S)==n)
        cases+=1
        if ok:
            solutions+=1
            assert S%8==4, (a,p,S)
            m=S//4
            assert omega(m)%2==(0 if a==2 else 1)
            if omega(m)<=2: restricted+=1
        has_low=(S%8==4 and omega(S//4)<=2)
        assert not has_low or (ok == claimed(a,p)), (a,p,ok,S)
        assert not (ok and omega(S//4)<=2) or claimed(a,p)

fam=[]
for a in range(3,19):
    t=1<<a; p=2*t+3; q=t*(2*t-1)//4+t-1
    if isprime(p) and isprime(q):
        S=(t-1)*p+2*t-1
        assert S==4*q and D(S)==t*p
        fam.append((a,t*p,p,q))
S=220
assert D(S)==284 and omega(S//4)==2
assert fam[:3] == [(3,152,19,37),(11,8394752,4099,2098687),(15,2147581952,65539,536895487)],fam
print('CHECK_OK tested_prime_pairs=%d fixed_points=%d low_odd_support=%d family=%s exceptional=284' % (cases,solutions,restricted,fam))
