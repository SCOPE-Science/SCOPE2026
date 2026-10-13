#!/usr/bin/env python3
"""Exact finite checks of a semiprime divisor-sum/totient classification.

Finite checks are independent corroboration, not a substitute for the proof.
"""
from math import isqrt


def sieve(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p*p, limit + 1, p):
                if spf[n] == n: spf[n] = p
    return spf


def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0: return False
    return True


def trial(limit=500000, prime_cutoff=3000):
    spf = sieve(limit)
    count = 0
    hits = []
    for n in range(4, limit + 1):
        t=n; factors=[]
        while t>1:
            p=spf[t];t//=p
            if t%p==0:
                t//=p
                if t!=1: factors=[];break
                factors=[p,p];break
            factors.append(p)
            if len(factors)>2:break
        if len(factors)!=2:continue
        count+=1;p,q=factors
        sigma=(1+p+p*p) if p==q else (p+1)*(q+1)
        phi=(p*p-p) if p==q else (p-1)*(q-1)
        obs=(n*phi)%sigma==0
        expect=p<q and ((p,q)==(2,3) or (p>2 and q==p*(p-1)-1))
        assert obs==expect,(n,p,q,obs,expect)
        if obs:hits.append(n)
    primes=[p for p in range(2,prime_cutoff+1) if prime(p)]
    family=[]
    for p in primes:
        q=p*(p-1)-1
        if p>2 and prime(q):
            assert (p*q*(p-1)*(q-1))%((p+1)*(q+1))==0
            family.append((p,q))
    assert hits[:4]==[6,15,95,287], hits[:4]
    assert (3,5) in family and (7,41) in family
    print('VERIFY_OK', 'limit=',limit, 'semiprimes_checked=',count,
          'hits=',hits, 'p_leq=',prime_cutoff,'family_prime_pairs=',len(family))

if __name__=='__main__':trial()
