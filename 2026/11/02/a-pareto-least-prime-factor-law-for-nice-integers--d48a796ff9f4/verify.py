#!/usr/bin/env python3
"""Finite exact-arithmetic checks for a least-prime-factor counting theorem.

This verifies finite identities and integer membership predicates; it does not
prove Mertens' theorem or the asymptotic normal-order estimates.
"""
from math import isqrt


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p::p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(n + 1) if sieve[p]]


def main():
    X = 30000
    primes = primes_up_to(X)
    smallest = list(range(X+1))
    omega = [0] * (X+1)
    for p in primes:
        for n in range(p, X+1, p):
            omega[n] += 1
            if smallest[n] == n:
                smallest[n] = p
    z = 32
    short = [0]*(X+1)
    for p in primes:
        if p > z:
            break
        for n in range(p, X+1, p):
            short[n] += 1
    assert max(abs(short[n]-omega[n]) for n in range(2,X+1)) <= 2  # z^3>X
    for cutoff in (2,3,5,7,11,13,17,23,31):
        small_primes = [p for p in primes if p <= cutoff]
        direct = sum(1 for n in range(2,X+1) if smallest[n] > cutoff)
        inc = 0
        for mask in range(1<<len(small_primes)):
            prod = 1
            parity = 0
            for k,p in enumerate(small_primes):
                if mask>>k & 1:
                    prod *= p
                    parity ^= 1
            inc += (-1 if parity else 1)*(X//prod)
        assert direct == inc-1, (cutoff,direct,inc)
    S = sum(short[1:]); Q = sum(v*v for v in short[1:])
    exactlyS = sum(X//p for p in primes if p <= z)
    exactlyQ = exactlyS + 2*sum(X//(p*q) for i,p in enumerate(primes) if p<=z for q in primes[i+1:] if q<=z)
    assert S == exactlyS and Q == exactlyQ
    assert all(omega[n]-omega[n//smallest[n]] in (0,1) for n in range(2,X+1))
    # The criterion counts *distinct* prime factors after removing one least prime.
    actual = sum(omega[n//smallest[n]] < smallest[n] for n in range(2,X+1))
    for n in range(2,X+1):
        p = smallest[n]
        assert (omega[n//p] < p) == (omega[n] - (1 if (n//p)%p else 0) < p)
    print(f'VERIFY_OK N={X} least_prime_memberships={X-1} rough_cutoffs=9 exact_moments=PASS exact_inclusion_exclusion=PASS nice_count={actual} finite_only=YES')

if __name__=='__main__':
    main()
