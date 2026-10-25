#!/usr/bin/env python3
"""Exact verification: first dyadic EOS prime-pair coverage at exponent 3/4.

Pure Python 3 standard library, no external data or unpublished imports.
"""
from math import isqrt

EXPECTED_MISSING = {1: 1, 2: 2, 3:3, 4:3, 5:5, 6:11, 7:17,
    8:30, 9:54, 10:70, 11:121, 12:162, 13:190, 14:240,
    15:216, 16:183, 17:92, 18:42, 19:7, 20:3, 21:0}
EXPECTED_WITNESSES = {20:(122299,333455,414971), 21:(745135,50923,7757)}

def odd_primes(limit):
    sieve = bytearray(b'\x01') * (limit+1)
    sieve[:2] = b'\x00' * min(2,limit+1)
    for divisor in range(2, isqrt(limit)+1):
        if sieve[divisor]:
            sieve[divisor*divisor:limit+1:divisor] = b'\x00' * ((limit-divisor*divisor)//divisor+1)
    return [n for n in range(3,limit+1,2) if sieve[n]], sieve

def calculate(m):
    q=1<<m
    cutoff=isqrt(isqrt(1<<(3*m)))  # exact floor(q^(3/4))
    primes, flags=odd_primes(cutoff)
    covered=bytearray(q//2)
    missing=q//2
    first_full=None
    last_uncovered=None
    prev_prime=None
    for j,p in enumerate(primes):
        for r in primes[:j+1]:
            key=((p*r)&(q-1))>>1
            if not covered[key]:
                covered[key]=1
                missing-=1
        if missing == 0 and first_full is None:
            first_full=p
            prev_prime=primes[j-1] if j else 1
    uncovered=[2*j+1 for j,flag in enumerate(covered) if not flag]
    assert len(uncovered)==EXPECTED_MISSING[m], (m,len(uncovered))
    # Dual obstruction check: for each absent residue a, no prime r<=cutoff
    # equals a*p^{-1} modulo q for any prime p<=cutoff.
    for a in (uncovered[:1] if m<20 else uncovered):
        assert all(not ((a*pow(p,-1,q))%q<=cutoff and flags[(a*pow(p,-1,q))%q]) for p in primes)
    if m==20:
        assert tuple(uncovered)==EXPECTED_WITNESSES[20]
    if m==21:
        a,p,r=EXPECTED_WITNESSES[21]
        assert first_full==p and p*r%q==a and flags[p] and flags[r]
        # At the immediately preceding prime cutoff, a is not representable.
        assert all(not ((a*pow(s,-1,q))%q< p and flags[(a*pow(s,-1,q))%q]) for s in primes if s<p)
        assert prev_prime==50909
    return m,cutoff,len(primes),missing,uncovered[:1],first_full

if __name__=='__main__':
    for m in range(1,22):
        print('m,cutoff,odd_prime_count,missing,first_witness,first_full',calculate(m))
    print('VERIFY_OK')
