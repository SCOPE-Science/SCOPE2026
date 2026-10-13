#!/usr/bin/env python3
"""Exact finite checks for the constructible-totient intersection theorem."""
from math import isqrt

LIMIT = 300_000

def factor(n):
    assert n >= 1
    fac = []
    if n == 1:
        return fac
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    if a:
        fac.append((2, a))
    p = 3
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            fac.append((p, a))
        p += 2
    if n > 1:
        fac.append((n, 1))
    return fac

def phi_from_factor(n):
    ans = n
    for p, _ in factor(n):
        ans -= ans // p
    return ans

def sigma_from_factor(n):
    ans = 1
    for p, e in factor(n):
        ans *= (p ** (e + 1) - 1) // (p - 1)
    return ans

def difference(n):
    return phi_from_factor(sigma_from_factor(n)) - sigma_from_factor(phi_from_factor(n))

def is_prime(n):
    return n > 1 and factor(n) == [(n, 1)]

assert all(is_prime(2 ** (2 ** j) + 1) for j in range(5))
assert 2 ** 32 + 1 == 641 * 6700417 and is_prime(641)

# This is a genuine direct check, not a proof of infinite exclusion.
phis = list(range(LIMIT + 1))
for p in range(2, LIMIT + 1):
    if phis[p] == p:
        for n in range(p, LIMIT + 1, p):
            phis[n] -= phis[n] // p

predicted_ten = sorted(
    multiplier * 2 ** (2 ** t - 1)
    for t in range(1, 6)
    for multiplier in (1, 3)
)
hits = []
checked = 0
for n in range(2, LIMIT + 1):
    v = phis[n]
    if v & (v - 1):
        continue
    checked += 1
    actual = (difference(n) == 1)
    expected = (n in predicted_ten)
    assert actual == expected, (n, phis[n], difference(n), expected)
    if actual:
        hits.append(n)
assert hits == [2, 6, 8, 24, 128, 384, 32768, 98304], hits

# Verify the two very large asserted solutions and many neighboring rays independently.
ray_hits = []
for a in range(0, 36):
    for multiplier in (1, 3):
        n = multiplier * 2 ** a
        if n == 1:
            continue
        actual = difference(n) == 1
        expected = n in predicted_ten
        assert actual == expected, (a, multiplier, n, difference(n))
        if actual:
            ray_hits.append(n)
assert sorted(ray_hits) == predicted_ten

# For the first 19 dyadic exponents and the known odd Fermat factors,
# compare all constructible-totient support subsets (not only single cofactors).
fermat_primes = [3, 5, 17, 257, 65537]
subset_cases = 0
for subset in range(1 << len(fermat_primes)):
    odd = 1
    for j, q in enumerate(fermat_primes):
        if (subset >> j) & 1:
            odd *= q
    for a in range(0, 19):
        n = odd * 2 ** a
        if n < 2 or n > 2 ** 41:
            continue
        subset_cases += 1
        actual = (difference(n) == 1)
        expected = (n in predicted_ten)
        assert actual == expected, (subset, a, n, difference(n))

print("VERIFY_OK", f"phi_power2_candidates_le_{LIMIT}={checked}",
      f"hits_le_{LIMIT}={hits}",
      "dyadic_rays_exponents=0..35",
      f"all_ten={predicted_ten}",
      f"fermat_support_cases={subset_cases}",
      "F5_has_prime_factor=641")
