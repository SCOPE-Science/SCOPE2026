#!/usr/bin/env python3
from itertools import combinations

def profiles(total, richness):
    def rec(rem, k, low, prefix):
        if k == 0:
            if rem == 0:
                yield tuple(prefix)
            return
        for x in range(low, rem // k + 1):
            yield from rec(rem - x, k - 1, x, prefix + (x,))
    yield from rec(total, richness, 1, ())

def excess_partitions(r):
    # Partitions of r into any positive number of positive parts.
    if r == 0:
        yield ()
        return
    def rec(rem, low, prefix):
        if rem == 0:
            yield tuple(prefix)
            return
        for x in range(low, rem + 1):
            yield from rec(rem - x, x, prefix + (x,))
    yield from rec(r, 1, ())

def profile_from_excess(part, richness):
    assert len(part) <= richness
    return tuple(sorted((1,) * (richness - len(part)) + tuple(1 + x for x in part)))

def shannon_product(profile):
    out = 1
    for x in profile:
        out *= x ** x
    return out

def bp_max(profile):
    return max(profile)

def sign(z):
    return (z > 0) - (z < 0)

def classify_pair(a, b):
    dm = sign(bp_max(a) - bp_max(b))
    dq = sign(shannon_product(a) - shannon_product(b))
    # Larger max means lower order-infinity diversity.
    # Larger Q means lower order-one (Shannon) diversity.
    # Therefore the diversity rankings agree exactly when dm and dq agree.
    weak_disagreement = dm != dq
    strict_reversal = dm * dq < 0
    return weak_disagreement, strict_reversal

# Direct census for a broad range of richness values at the only relevant
# excess totals. This is a replay check; the proof of all-richness coverage
# uses stabilization of excess partitions once richness >= r.
weak_counts = {}
strict_counts = {}
strict_pairs_r6 = {}

for k in range(3, 13):
    weak_counts[k] = {}
    strict_counts[k] = {}
    for r in range(0, 7):
        ps = list(profiles(k + r, k))
        weak = []
        strict = []
        for a, b in combinations(ps, 2):
            w, s = classify_pair(a, b)
            if w:
                weak.append((a, b))
            if s:
                strict.append((a, b))
        weak_counts[k][r] = len(weak)
        strict_counts[k][r] = len(strict)
        if r == 6:
            strict_pairs_r6[k] = strict

# Weak orderings agree through r=3, for all checked richnesses.
for k in range(3, 13):
    for r in range(0, 4):
        assert weak_counts[k][r] == 0

# The first weak-order difference is at r=4 and is a tie split.
for k in range(3, 13):
    assert weak_counts[k][4] == 1
    assert strict_counts[k][4] == 0
    A = (1,) * (k - 2) + (3, 3)
    B = (1,) * (k - 3) + (2, 2, 3)
    w, s = classify_pair(A, B)
    assert w and not s
    assert bp_max(A) == bp_max(B) == 3
    assert shannon_product(A) == 729
    assert shannon_product(B) == 432

# No strict reversal through r=5.
for k in range(3, 13):
    for r in range(0, 6):
        assert strict_counts[k][r] == 0

# At r=6 the first strict layer has one pair for k=3 and two for every k>=4.
for k in range(3, 13):
    expected1 = (
        (1,) * (k - 2) + (4, 4),
        (1,) * (k - 3) + (2, 2, 5),
    )
    if k == 3:
        expected = [expected1]
    else:
        expected2 = (
            (1,) * (k - 3) + (3, 3, 3),
            (1,) * (k - 4) + (2, 2, 2, 4),
        )
        expected = [expected1, expected2]
    assert strict_pairs_r6[k] == expected, (k, strict_pairs_r6[k])

# Exact invariant values of the two universal mechanisms.
assert shannon_product((1,4,4)) == 65536
assert shannon_product((2,2,5)) == 50000
assert shannon_product((1,3,3,3)) == 19683
assert shannon_product((2,2,2,4)) == 16384

# Stabilization proof ingredient:
# for fixed excess r, every positive-integer profile of richness k is obtained
# by padding a partition of r with k-len(part) baseline ones, whenever len(part)<=k.
# Once k>=r every partition of r is admissible, so the comparison set no longer
# changes except for harmless added ones.
for r in range(0, 7):
    ex = list(excess_partitions(r))
    for k in range(max(3, r), max(3, r) + 4):
        direct = set(profiles(k + r, k))
        via_excess = {profile_from_excess(p, k) for p in ex if len(p) <= k}
        assert direct == via_excess

print("VERIFY_OK")
print("first_weak_excess", 4)
print("first_strict_excess", 6)
print("strict_layer_k3", strict_pairs_r6[3])
print("strict_layer_k4", strict_pairs_r6[4])
print("stabilization_checked_through_excess", 6)
