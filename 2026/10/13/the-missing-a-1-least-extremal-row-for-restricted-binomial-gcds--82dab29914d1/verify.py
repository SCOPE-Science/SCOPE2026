#!/usr/bin/env python3
from math import comb

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def vp(n,p):
    e=0
    while n and n%p==0:
        e += 1
        n//=p
    return e

def carries(a,b,p):
    c=0
    carry=0
    while a or b or carry:
        s=(a%p)+(b%p)+carry
        carry=1 if s>=p else 0
        c += carry
        a//=p; b//=p
    return c

def restricted_v(p,q):
    m=p+1
    N=m*q
    return min(carries(m*d, m*(q-d), p) for d in range(1,q))

# Exact finite replay for a broad prime sample.
primes=[p for p in range(2,100) if is_prime(p)]
for p in primes:
    m=p+1
    # Every smaller admissible multiplier has valuation 0.
    for q in range(2,p):
        assert restricted_v(p,q)==0, (p,q,restricted_v(p,q))
        # direct binomial valuation agrees for a sample of all selected indices
        N=m*q
        for d in range(1,q):
            assert vp(comb(N,m*d),p)==0, (p,q,d)
    # The first candidate q=p has exactly two carries for every selected index.
    q=p
    assert restricted_v(p,q)==2, (p,restricted_v(p,q))
    N=m*q
    for d in range(1,q):
        k=m*d
        assert carries(k,N-k,p)==2, (p,d,carries(k,N-k,p))
        if p<=43:
            assert vp(comb(N,k),p)==2, (p,d,vp(comb(N,k),p))

# The symbolic digit identities used in the proof are integer equalities:
# (p+1)q = qp+q for 2<=q<p, and (p+1)d=dp+d for 1<=d<q.
# At q=p, (p+1)p=p^2+p, while d+(p-d)=p in both low digit columns,
# forcing exactly two carries and no third carry.
for p in primes:
    for q in range(2,p):
        assert (p+1)*q == q*p+q
        for d in range(1,q):
            assert (p+1)*d == d*p+d
            assert (p+1)*(q-d) == (q-d)*p+(q-d)
    for d in range(1,p):
        assert (p+1)*d == d*p+d
        assert (p+1)*(p-d) == (p-d)*p+(p-d)
        assert d+(p-d)==p

print(f"VERIFY_OK primes={len(primes)} max_prime={primes[-1]} smaller_multipliers_zero=1 target_multiplier_two_carries=1 direct_binomial_checks_through=43")
