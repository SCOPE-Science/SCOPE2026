#!/usr/bin/env python3
"""Exact finite checks of a binomial-progression gcd identity."""
from math import comb, gcd

def sieve(n):
    prime = bytearray(b'\x01') * (n+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, int(n**0.5)+1):
        if prime[p]:
            prime[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return [p for p in range(2, n+1) if prime[p]]

PRIMES = sieve(12000)

def factors(n):
    out=[]; m=n
    for p in PRIMES:
        if p*p>m: break
        if m%p == 0:
            a=0
            while m%p == 0:
                m//=p;a+=1
            out.append((p,a))
    if m>1: out.append((m,1))
    return out

def valfac(n,p):
    result=0
    while n:
        n//=p;result+=n
    return result

def valbin(q,k,p):
    return valfac(q*k,p)-valfac(k,p)-valfac((q-1)*k,p)

def digit_height(b,p):
    t=0
    while b>=p:
        b//=p;t+=1
    return t

def formula(n):
    d=1
    for p,a in factors(n):
        b=n//p**a
        t=digit_height(b,p)
        d *= p**max(0,a-t)
    return d

# Direct gcd of every defining coefficient, independent of the valuation proof.
for k in range(2,161):
    d=0
    for q in range(2,k+2):
        d=gcd(d,comb(q*k,k))
    assert d==formula(k+1),(k,d,formula(k+1))
    assert (k+1)%d==0

# Complete p-adic minimization, including all q in the definition.
rows=0
for n in range(3,1201):
    k=n-1
    for p,a in factors(n):
        b=n//p**a
        t=digit_height(b,p)
        minimum=min(valbin(q,k,p) for q in range(2,n+1))
        assert minimum==max(0,a-t), (n,p,a,b,t,minimum)
        rows+=1

# Check witnesses at substantially larger numbers, using a distinct
# direct factorial-valuation computation rather than carry enumeration.
witnesses=0
for n in range(3,12001):
    k=n-1
    for p,a in factors(n):
        b=n//p**a
        t=digit_height(b,p)
        if a>t:
            u=b-p**t
            q=p if b==1 else 1+p**a*u
            assert 2<=q<=n
            assert valbin(q,k,p)==a-t, (n,p,q)
            witnesses+=1

print('VERIFY_OK direct_gcd_k=2..160 p_adic_global_n=3..1200 local_components=%d explicit_witnesses=%d finite_proof_checks=yes' %(rows,witnesses))
