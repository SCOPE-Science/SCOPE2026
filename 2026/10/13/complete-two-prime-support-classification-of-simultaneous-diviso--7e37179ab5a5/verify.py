#!/usr/bin/env python3
"""Exact finite corroboration for a theorem about simultaneous divisor-sum primality."""
from math import isqrt

LIMIT = 1_000_000
phi = list(range(LIMIT + 1))
sigma = [1] * (LIMIT + 1)
sigma[0] = 0

# Euler totient and ordinary sigma, using independent divisor sweeps.
for p in range(2, LIMIT + 1):
    if phi[p] == p:
        for n in range(p, LIMIT + 1, p):
            phi[n] -= phi[n] // p
for d in range(2, LIMIT + 1):
    for n in range(d, LIMIT + 1, d):
        sigma[n] += d

max_sigma = max(max(sigma[n - 1], sigma[phi[n]]) for n in range(3, LIMIT + 1))
prime = bytearray(b'\x01') * (max_sigma + 1)
prime[0] = prime[1] = 0
for p in range(2, isqrt(max_sigma) + 1):
    if prime[p]:
        prime[p * p::p] = b'\x00' * ((max_sigma - p * p) // p + 1)

# Distinct-prime support via its own additive prime sieve.
omega = bytearray(LIMIT + 1)
for p in range(2, LIMIT + 1):
    if omega[p] == 0:
        for n in range(p, LIMIT + 1, p):
            omega[n] += 1

hits = []
checked = 0
for n in range(3, LIMIT + 1):
    observed = bool(prime[sigma[n - 1]] and prime[sigma[phi[n]]])
    if observed:
        hits.append(n)
    if omega[n] > 2:
        continue
    checked += 1
    # A prime in the sequence must have p-1 a power of two and
    # sigma(p-1) = 2(p-1)-1 prime; this encodes every hypothetical
    # Fermat prime, without assuming only the known ones exist.
    prime_branch = (
        bool(prime[n]) and
        ((n - 1) & (n - 2)) == 0 and
        bool(prime[2 * (n - 1) - 1])
    )
    expected = n == 10 or prime_branch
    assert observed == expected, (n, observed, expected, phi[n], sigma[n - 1])

assert hits == [3, 5, 10, 17, 65537], hits
assert omega[10] == 2
assert phi[10] == 4 and sigma[9] == 13 and sigma[4] == 7
print('VERIFY_OK', 'limit='+str(LIMIT),
      'support_le2_checked='+str(checked),
      'simultaneous_prime_hits='+str(hits),
      'max_sigma='+str(max_sigma))
