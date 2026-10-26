#!/usr/bin/env python3
"""Exact finite cross-checks for reciprocal-series parity and A192717 membership.

This checks identities at finite indices; it does not certify the analytic
asymptotic, which depends on the classical Bombieri-Vinogradov theorem.
"""
from math import gcd, isqrt

N = 20000
# The odd divisor-sum parity support is the union of positive squares and
# twice positive squares, with a 1 at index zero.
support = sorted([j*j for j in range(1, isqrt(N)+1)]
                 + [2*j*j for j in range(1, isqrt(N//2)+1)])
reciprocal = bytearray(N+1)
reciprocal[0] = 1
for n in range(1, N+1):
    v = 0
    for s in support:
        if s > n:
            break
        v ^= reciprocal[n-s]
    reciprocal[n] = v

# Build independent least-prime-factor data for exact factorization.
spf = list(range(N+1))
for p in range(2, isqrt(N)+1):
    if spf[p] != p:
        continue
    for v in range(p*p, N+1, p):
        if spf[v] == v:
            spf[v] = p

def from_prime_factorization(n):
    if n % 8 != 3:
        return False
    odd_prime_exponent = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e & 1:
            odd_prime_exponent.append((p, e))
    return (len(odd_prime_exponent) == 1 and
            odd_prime_exponent[0][0] % 8 == 3 and
            odd_prime_exponent[0][1] % 4 == 1)

membership = [False] * (N+1)
for n in range(1, N+1):
    membership[n] = from_prime_factorization(n)
    if n % 8 == 3:
        assert membership[n] == bool(reciprocal[n]), (n, membership[n], reciprocal[n])

first = [n for n in range(1, N+1) if membership[n]][:20]
assert first == [3,11,19,43,59,67,75,83,99,107,131,139,147,163,171,179,211,227,243,251]
for m in (8, 16, 24, 40, 56, 80, 120):
    for a in range(m):
        if a % 8 != 3 or gcd(a,m) != 1:
            continue
        lhs = sum(1 for n in range(a, N+1, m) if membership[n])
        rhs = sum(1 for n in range(a, N+1, m) if reciprocal[n])
        assert lhs == rhs, (m,a,lhs,rhs)
print('VERIFY_OK: 20000 exact binary-series inversions and prime-factor tests;')
print('20 OEIS initial members; 7 sets of progression-class checks')
