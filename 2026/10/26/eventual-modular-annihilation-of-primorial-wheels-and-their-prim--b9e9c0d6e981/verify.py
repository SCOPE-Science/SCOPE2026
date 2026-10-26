#!/usr/bin/env python3
"""Exact finite checks for primorial wheel congruences (not a proof of the all-k theorem)."""
from math import gcd

def primes_upto(limit):
    ans = []
    for n in range(2, limit + 1):
        if all(n % p for p in ans if p * p <= n):
            ans.append(n)
    return ans

def residues_brute(L, r):
    ans = [0] * r
    for a in range(1, L + 1):
        if gcd(a, L) == 1:
            ans[a % r] += 1
    return ans

def wheel_step(old, L, q, r, modulus=None):
    ans = [0] * r
    for j, multiplicity in enumerate(old):
        for t in range(q):
            ans[(j + t * L) % r] += multiplicity
        ans[(q * j) % r] -= multiplicity
    if modulus is not None:
        ans = [v % modulus for v in ans]
    return ans

def binary_wheel_state(L):
    return sum(1 << a for a in range(2, L + 2) if gcd(a, L) == 1)

# Independently enumerate the reduced residues for five small primorials.
L = 2
small = primes_upto(11)
for r in (2, 3, 4, 5, 8, 12):
    L = 2
    vector = residues_brute(L, r)
    for q in small[1:]:
        predicted = wheel_step(vector, L, q, r)
        L *= q
        assert predicted == residues_brute(L, r), (r, q)
        vector = predicted

assert binary_wheel_state(2) == 8
assert binary_wheel_state(6) == 160
assert binary_wheel_state(30) == 2693408896

# Check the expected annihilation of all residue-count coordinates.
for r, m, bound in ((8, 17, 149), (4, 3, 43), (6, 5, 79), (12, 7, 401)):
    L = 2
    v = [0] * r
    v[1] = 1
    candidate_q = next(q for q in primes_upto(bound) if q > 2 and (q - 1) % (r * m) == 0)
    reached = False
    for q in primes_upto(bound)[1:]:
        v = wheel_step(v, L, q, r, m)
        L *= q
        if q == candidate_q:
            reached = True
        if reached:
            assert v == [0] * r, (r, m, q, v)
    assert reached

# Explicit odd-modulus corollary: the 17-remainders stabilize to {6, 7}.
L = 2
v = [0] * 8
v[1] = 1
tracked = {}
for q in primes_upto(149)[1:]:
    v = wheel_step(v, L, q, 8, 17)
    L *= q
    if q in (137, 139, 149):
        state_residue = (sum(v[j] * pow(2, j, 17) for j in range(8)) + 2 * (pow(2, L, 17) - 1)) % 17
        expected = {2: 6, 6: 7}[L % 8]
        assert state_residue == expected
        tracked[q] = state_residue
assert tracked[137] == 7 and tracked[139] == 6
print('VERIFY_OK primorials=2,6,30,210,2310 modulus_pairs=4 first_special_prime=137 residues_after_special=7,6')
