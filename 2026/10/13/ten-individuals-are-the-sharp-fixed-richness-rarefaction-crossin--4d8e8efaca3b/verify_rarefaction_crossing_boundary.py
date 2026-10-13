#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb


def partitions_recursive(total, parts, cap=None):
    if parts == 0:
        if total == 0:
            yield ()
        return
    if cap is None:
        cap = total
    hi = min(cap, total - parts + 1)
    for first in range(hi, 0, -1):
        for tail in partitions_recursive(total - first, parts - 1, first):
            yield (first,) + tail


def partitions_multiset(total, parts):
    out = set()
    for xs in combinations_with_replacement(range(1, total + 1), parts):
        if sum(xs) == total:
            out.add(tuple(sorted(xs, reverse=True)))
    return out


def rarefied_richness(profile, m):
    N = sum(profile)
    den = comb(N, m)
    ans = Fraction(0, 1)
    for n_i in profile:
        absent = comb(N - n_i, m) if N - n_i >= m else 0
        ans += Fraction(den - absent, den)
    return ans


def sign(x):
    return (x > 0) - (x < 0)


def crosses(a, b):
    N = sum(a)
    signs = [sign(rarefied_richness(a, m) - rarefied_richness(b, m))
             for m in range(2, N)]
    return 1 in signs and -1 in signs

# Independent completeness check: recursive integer partitions equal a direct
# multiset enumeration for every fixed richness through the claimed boundary.
for N in range(2, 11):
    for S in range(1, N + 1):
        A = set(partitions_recursive(N, S))
        B = partitions_multiset(N, S)
        assert A == B

partition_counts = {}
pair_counts = {}
crossings = {}

for N in range(2, 11):
    partition_counts[N] = 0
    pair_counts[N] = 0
    crossings[N] = []
    for S in range(1, N + 1):
        profiles = sorted(set(partitions_recursive(N, S)), reverse=True)
        partition_counts[N] += len(profiles)
        pair_counts[N] += len(profiles) * (len(profiles) - 1) // 2
        for a, b in combinations(profiles, 2):
            if crosses(a, b):
                crossings[N].append((S, a, b))

assert partition_counts == {
    2: 2, 3: 3, 4: 5, 5: 7, 6: 11,
    7: 15, 8: 22, 9: 30, 10: 42,
}
assert pair_counts == {
    2: 0, 3: 0, 4: 1, 5: 2, 6: 7,
    7: 13, 8: 30, 9: 56, 10: 109,
}
assert all(crossings[N] == [] for N in range(2, 10))
assert crossings[10] == [(3, (6, 2, 2), (5, 4, 1))]

A = (6, 2, 2)
B = (5, 4, 1)
expected = {
    1: (Fraction(1, 1), Fraction(1, 1)),
    2: (Fraction(73, 45), Fraction(74, 45)),
    3: (Fraction(61, 30), Fraction(41, 20)),
    4: (Fraction(163, 70), Fraction(242, 105)),
    5: (Fraction(23, 9), Fraction(89, 36)),
    6: (Fraction(41, 15), Fraction(109, 42)),
    7: (Fraction(43, 15), Fraction(27, 10)),
    8: (Fraction(133, 45), Fraction(14, 5)),
    9: (Fraction(3, 1), Fraction(29, 10)),
    10: (Fraction(3, 1), Fraction(3, 1)),
}
for m, pair in expected.items():
    assert (rarefied_richness(A, m), rarefied_richness(B, m)) == pair

assert rarefied_richness(A, 2) < rarefied_richness(B, 2)
assert rarefied_richness(A, 3) < rarefied_richness(B, 3)
for m in range(4, 10):
    assert rarefied_richness(A, m) > rarefied_richness(B, m)

# Endpoint identities explaining the mechanism.
N = 10
same_pair_A = sum(n * (n - 1) for n in A)
same_pair_B = sum(n * (n - 1) for n in B)
assert same_pair_A == 34 and same_pair_B == 32
assert rarefied_richness(A, 2) == 2 - Fraction(same_pair_A, N * (N - 1))
assert rarefied_richness(B, 2) == 2 - Fraction(same_pair_B, N * (N - 1))
f1_A = sum(n == 1 for n in A)
f1_B = sum(n == 1 for n in B)
assert (f1_A, f1_B) == (0, 1)
assert rarefied_richness(A, N - 1) == len(A) - Fraction(f1_A, N)
assert rarefied_richness(B, N - 1) == len(B) - Fraction(f1_B, N)

print('VERIFY_OK')
print('partition_counts', partition_counts)
print('same_richness_pair_counts', pair_counts)
print('first_crossing_total', 10)
print('first_crossing_pair', crossings[10])
print('sign_change_between_m', 3, 4)
