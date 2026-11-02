#!/usr/bin/env python3
"""Independent finite checks for the two-bit Catalan 2-adic residue theorem.

All arithmetic is integer arithmetic. No external packages or online services.
"""
from functools import lru_cache
from math import comb

K = 16
MOD = 1 << K
# Prefix product of odd integers. The product of all odd residues modulo
# 2^K is 1 for K>=3; therefore this prefix can be repeated every 2^K.
odd_prefix = [1] * MOD
for j in range(1, MOD):
    odd_prefix[j] = odd_prefix[j - 1] * (j if j & 1 else 1) % MOD
assert odd_prefix[-1] == 1

@lru_cache(maxsize=None)
def odd_factorial_part(n):
    t = 1
    while n:
        t = (t * odd_prefix[n % MOD]) % MOD
        n //= 2
    return t

@lru_cache(maxsize=None)
def slice_term(b, r):
    assert b >= 0 and r >= 1
    n = (1 << b) * ((1 << r) + 1)
    u = odd_factorial_part(n)
    return (2 * odd_factorial_part(2 * n) * pow(u, -2, MOD)
            * pow(2 * n - 1, -1, MOD)) % MOD

def valuation_mod(x):
    if x % MOD == 0:
        return K
    return (x & -x).bit_length() - 1

# Compare independently with integral factorial binomial formula.
exact_cases = 0
for b in range(6):
    for r in range(1, 7):
        n = (1 << b) * ((1 << r) + 1)
        assert slice_term(b, r) == comb(2*n, n) // (2*(2*n - 1)) % MOD
        exact_cases += 1

horizontal_cases = vertical_cases = 0
for b in range(12):
    for r in range(1, 13):
        assert valuation_mod(slice_term(b, r+1)-slice_term(b, r)) == r+1
        horizontal_cases += 1
for b in range(1, 12):
    for r in range(1, 13):
        assert valuation_mod(slice_term(b+1, r)-slice_term(b, r)) == b+2
        vertical_cases += 1

counts = []
for k in range(3, 13):
    mod = 1 << k
    all_residues = {slice_term(b, r) % mod for b in range(k+3) for r in range(1, k+4)}
    clipped = {slice_term(b, r) % mod for b in range(k-1) for r in range(1, k)}
    assert all_residues == clipped
    t = (k-2)//2
    chosen = {slice_term(b, r) % mod for b in range(t, k-2) for r in range(1,t+1)}
    assert len(chosen) == t*(k-2-t)
    assert t*(k-2-t) <= len(clipped) <= (k-1)**2
    counts.append(len(clipped))

assert counts == [2, 4, 7, 13, 21, 33, 46, 63, 81, 102]
print('VERIFY_OK exact_integer_cases=',exact_cases,'horizontal_cases=',horizontal_cases,
      'vertical_cases=',vertical_cases,'levels=3..12')
print('distinct_residues_by_k=', counts)
print('quadratic_lower_and_upper=True')
