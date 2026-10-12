#!/usr/bin/env python3
"""Check the fixed-support derivative/totient equality using exact arithmetic."""
from fractions import Fraction
from math import isqrt

LIMIT = 10000
sieve = bytearray(b"\1") * LIMIT
sieve[0:2] = b"\0\0"
for p in range(2, isqrt(LIMIT - 1) + 1):
    if sieve[p]:
        sieve[p * p : LIMIT : p] = b"\0" * (((LIMIT - 1 - p * p) // p) + 1)
primes = [p for p, is_prime in enumerate(sieve) if is_prime and p > 7]
assert len(primes) == 1225
matches = 0
for r in primes:
    found = []
    for a in range(1, 5):
        for b in range(1, 7):
            coefficient = 24 - 7 * a - 5 * b
            numerator = coefficient * r - 24
            if numerator <= 0 or numerator % 35:
                continue
            c = numerator // 35
            if Fraction(a, 5) + Fraction(b, 7) + Fraction(c, r) == Fraction(24 * (r - 1), 35 * r):
                found.append((a, b, c))
    expected = []
    if r % 35 == 2:
        expected = [(1, 1, (12 * r - 24) // 35)]
    elif r % 35 == 12:
        expected = [(1, 3, (2 * r - 24) // 35)]
    assert found == expected, (r, found, expected)
    matches += bool(found)
assert matches == 100

for r, a, b, c in [(37, 1, 1, 12), (47, 1, 3, 2), (107, 1, 1, 36), (257, 1, 3, 14)]:
    n = 5**a * 7**b * r**c
    derivative = n * (Fraction(a, 5) + Fraction(b, 7) + Fraction(c, r))
    totient = 4 * 5**(a-1) * 6 * 7**(b-1) * (r-1) * r**(c-1)
    assert derivative == totient

print(f"VERIFY_OK prime_cutoff={LIMIT} primes={len(primes)} qualifying_supports={matches}")
