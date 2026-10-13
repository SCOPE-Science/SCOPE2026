#!/usr/bin/env python3
from itertools import product
from fractions import Fraction
from math import comb

def partitions_fixed_sum_length(total, length, minimum=1):
    """Nondecreasing positive integer tuples of given sum and length."""
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // length + 1):
        for rest in partitions_fixed_sum_length(total - first, length - 1, first):
            yield (first,) + rest

def compositions_canonical(total, length):
    """Independent brute-force route, canonicalized by sorting."""
    out = set()
    def rec(remaining, slots, acc):
        if slots == 1:
            if remaining >= 1:
                out.add(tuple(sorted(acc + [remaining])))
            return
        for x in range(1, remaining - slots + 2):
            rec(remaining - x, slots - 1, acc + [x])
    rec(total, length, [])
    return out

def simpson_num(profile):
    return sum(x * (x - 1) for x in profile)

def third_factorial_num(profile):
    return sum(x * (x - 1) * (x - 2) for x in profile)

def rarefied_expected_species(profile, m):
    N = sum(profile)
    den = comb(N, m)
    return sum(Fraction(den - (comb(N-x, m) if N-x >= m else 0), den) for x in profile)

# Independent enumeration agreement and exact Hurlbert identities.
all_profiles = {}
pair_count = 0
for N in range(1, 10):
    for S in range(1, N + 1):
        p1 = set(partitions_fixed_sum_length(N, S))
        p2 = compositions_canonical(N, S)
        assert p1 == p2, (N, S, p1 ^ p2)
        all_profiles[(N,S)] = sorted(p1)
        for p in p1:
            if N >= 2:
                D2 = Fraction(simpson_num(p), N*(N-1))
                assert rarefied_expected_species(p,2) == 2 - D2
            if N >= 3:
                D2 = Fraction(simpson_num(p), N*(N-1))
                T3 = Fraction(third_factorial_num(p), N*(N-1)*(N-2))
                assert rarefied_expected_species(p,3) == 3 - 3*D2 + T3
        pair_count += len(p1)*(len(p1)-1)//2

# Exact uniqueness through N=8, fixing both N and richness S.
collisions = []
for N in range(1, 10):
    for S in range(1, N + 1):
        buckets = {}
        for p in all_profiles[(N,S)]:
            buckets.setdefault(simpson_num(p), []).append(p)
        for q, ps in buckets.items():
            if len(ps) > 1:
                collisions.append((N,S,q,tuple(ps)))

assert collisions == [
    (9, 3, 24, ((1,4,4),(2,2,5)))
], collisions

A=(1,4,4)
B=(2,2,5)
assert simpson_num(A) == simpson_num(B) == 24
D2 = Fraction(24,9*8)
assert D2 == Fraction(1,3)
assert third_factorial_num(A) == 48
assert third_factorial_num(B) == 60
R2A=rarefied_expected_species(A,2)
R2B=rarefied_expected_species(B,2)
R3A=rarefied_expected_species(A,3)
R3B=rarefied_expected_species(B,3)
assert R2A == R2B == Fraction(5,3)
assert R3A == Fraction(44,21)
assert R3B == Fraction(89,42)
assert R3B-R3A == Fraction(1,42)

# The finite census is complete: positivity implies 1 <= S <= N.
# Count all within-(N,S) unordered profile pairs through N=9.
assert pair_count == 109

print("VERIFY_OK")
print("first_collision", collisions[0])
print("D2", D2)
print("R2", R2A)
print("R3_A", R3A)
print("R3_B", R3B)
print("R3_gap", R3B-R3A)
print("within_slice_pairs_checked", pair_count)
