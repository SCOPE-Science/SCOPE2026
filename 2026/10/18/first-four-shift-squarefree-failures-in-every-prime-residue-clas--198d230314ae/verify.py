#!/usr/bin/env python3
"""Exact integer-only enumeration of first prime failures of four squarefree shifts.
Run: python3 verify_erdos_mod36.py  (Python 3 standard library).
"""
from math import isqrt
from bisect import bisect_right

EXPECTED = {
 1: 280729, 5: 439601, 7: 4851151, 11: 5051,
 13: 6421, 17: 6029, 19: 1052083, 23: 6165527,
 25: 236329, 29: 6329, 31: 418783, 35: 45179,
}
OFFSETS = (1, 2, 4, 8)
FORCED_SMALL_SQUARE_OFFSETS = {
 1: 1, 5: 1, 7: 0, 11: 1, 13: 2, 17: 2,
 19: 1, 23: 0, 25: 1, 29: 2, 31: 1, 35: 1,
}
for r in EXPECTED:
    forced = sum((r-h) % 4 == 0 or (r-h) % 9 == 0 for h in OFFSETS)
    assert forced == FORCED_SMALL_SQUARE_OFFSETS[r]
B = max(EXPECTED.values())

# Classical sieve of Eratosthenes: exact primality for all n <= B.
prime_mask = bytearray(b'\x01') * (B + 1)
prime_mask[0:2] = b'\x00\x00'
for d in range(2, isqrt(B) + 1):
    if prime_mask[d]:
        start = d * d
        prime_mask[start::d] = b'\x00' * ((B - start) // d + 1)
primes = [p for p in range(2, B + 1) if prime_mask[p]]
small_primes = primes[:bisect_right(primes, isqrt(B))]

# Method I: mark exactly the nonsquarefree positive integers n <= B.
squareful = bytearray(B + 1)
for q in small_primes:
    step = q * q
    squareful[step::step] = b'\x01' * (B // step)

first_a = {}
for p in primes:
    if p <= 8:
        continue
    r = p % 36
    if r not in EXPECTED or r in first_a:
        continue
    if all(squareful[p - h] for h in OFFSETS):
        first_a[r] = p
assert first_a == EXPECTED, (first_a, EXPECTED)

# Method II: independent square-factor predicate using trial division by
# primes <= sqrt(n); do not consult method I's squareful mask.
def nonsquarefree_by_trial(n):
    assert n > 0
    for q in small_primes:
        if q * q > n:
            return False
        if n % (q * q) == 0:
            return True
    return False

first_b = {}
for p in primes:
    if p <= 8:
        continue
    r = p % 36
    if r not in EXPECTED or r in first_b:
        continue
    if all(nonsquarefree_by_trial(p-h) for h in OFFSETS):
        first_b[r] = p
assert first_b == EXPECTED, (first_b, EXPECTED)

# Independent trial-division primality check on all twelve witnesses.
def prime_by_trial(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

for r in sorted(EXPECTED):
    p = EXPECTED[r]
    assert p % 36 == r and prime_by_trial(p)
    witness = []
    for h in OFFSETS:
        q = next(q for q in small_primes if p-h >= q*q and (p-h) % (q*q) == 0)
        witness.append(q)
    assert all((p-h) % (q*q) == 0 for h,q in zip(OFFSETS, witness))
    print(f'{r:2d} {p:7d} witnesses={tuple(witness)}')
print('VERIFY_OK; 12 residue-class minima; bound', B)
