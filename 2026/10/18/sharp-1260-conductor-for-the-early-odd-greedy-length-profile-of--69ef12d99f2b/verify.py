#!/usr/bin/env python3
"""Exact integer checks for the prime odd-greedy stopping profile.

No external dependencies. The proof in RESULT.md, rather than finite tests,
establishes the assertion for all primes.
"""
from collections import Counter
from math import gcd, isqrt

M = 1260

def prime_sieve(n):
    bits = bytearray(b'\x01') * (n + 1)
    bits[:2] = b'\x00\x00'
    for j in range(2, isqrt(n) + 1):
        if bits[j]:
            bits[j*j:n+1:j] = b'\x00' * ((n - j*j)//j + 1)
    return [j for j in range(5, n + 1) if bits[j]]

def profile(p):
    if p % 4 == 1:
        return 2
    if p % 20 == 7:
        return 4
    if p % 9 in (1, 2, 4, 5) or p % 7 == 4:
        return 6
    return 8  # At least eight terms, possibly infinitely many.

def independently_iterate(p):
    a,b = 2,p
    for steps in range(1, 8):
        u = (b + a - 1)//a
        if u % 2 == 0:
            u += 1
        numerator = a*u - b
        if numerator == 0:
            return steps
        denominator = b*u
        g = gcd(numerator, denominator)
        a,b = numerator//g, denominator//g
    return 8

def main():
    primes = prime_sieve(100000)
    for p in primes:
        got = independently_iterate(p)
        want = profile(p)
        assert got == want, (p,got,want)
    classes = {r:profile(r) for r in range(M) if gcd(r,M)==1}
    counts = Counter(classes.values())
    assert len(classes) == 288
    assert counts == Counter({2:144,4:36,6:78,8:30}), counts
    witnesses = [(1,631,630),(19,439,420),(11,767,252),(43,403,180)]
    for r,s,d in witnesses:
        assert gcd(r,M)==gcd(s,M)==1
        assert r%d == s%d and profile(r)!=profile(s)
    for d in range(1,M):
        if M%d:
            continue
        seen = {}
        for r,k in classes.items():
            if r%d in seen:
                if seen[r%d] != k:
                    break
            else:
                seen[r%d] = k
        else:
            raise AssertionError(('smaller divisor period',d))
    assert all(profile(r)==profile(r+M) for r in classes)
    print('VERIFY_OK primes=%d unit_classes=288 counts=%s minimal_divisor_period=1260' %
          (len(primes),dict(sorted(counts.items()))))

if __name__ == '__main__':
    main()
