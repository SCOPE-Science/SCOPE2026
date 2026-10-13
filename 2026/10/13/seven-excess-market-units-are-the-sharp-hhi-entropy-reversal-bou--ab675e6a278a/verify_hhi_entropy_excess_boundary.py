#!/usr/bin/env python3
from itertools import combinations

def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for a in range(minimum, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest

def excess_quadratic(y):
    return sum(v * v for v in y)

def entropy_product_from_excess(y):
    out = 1
    for v in y:
        out *= (v + 1) ** (v + 1)
    return out

def profile_from_excess(y, k):
    assert len(y) <= k
    vals = [1 + v for v in y] + [1] * (k - len(y))
    return tuple(sorted(vals))

def hhi_numerator(profile):
    return sum(v * v for v in profile)

def entropy_product(profile):
    out = 1
    for v in profile:
        out *= v ** v
    return out

reversal_counts = {}
tie_split_counts = {}
for r in range(0, 8):
    ps = list(partitions(r))
    rev = []
    tie_split = []
    for a, b in combinations(ps, 2):
        du = excess_quadratic(a) - excess_quadratic(b)
        dw = entropy_product_from_excess(a) - entropy_product_from_excess(b)
        if du * dw < 0:
            rev.append((a, b))
        if du == 0 and dw != 0:
            tie_split.append((a, b))
    reversal_counts[r] = len(rev)
    tie_split_counts[r] = len(tie_split)

assert reversal_counts == {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:1}
assert tie_split_counts[0] == tie_split_counts[1] == tie_split_counts[2] == 0
assert tie_split_counts[3] == tie_split_counts[4] == tie_split_counts[5] == 0
assert tie_split_counts[6] == 2
assert tie_split_counts[7] == 2

r7 = list(partitions(7))
reversals = []
for a, b in combinations(r7, 2):
    du = excess_quadratic(a) - excess_quadratic(b)
    dw = entropy_product_from_excess(a) - entropy_product_from_excess(b)
    if du * dw < 0:
        reversals.append((a, b))
assert reversals == [((1, 1, 5), (3, 4))]

# Universal first strict layer for every fixed k >= 3.
for k in range(3, 101):
    N = k + 7
    B = profile_from_excess((1, 1, 5), k)
    A = profile_from_excess((3, 4), k)
    assert sum(A) == sum(B) == N
    assert hhi_numerator(A) == k + 39
    assert hhi_numerator(B) == k + 41
    assert entropy_product(A) == 800000
    assert entropy_product(B) == 746496
    # HHI says B is more concentrated; entropy says A is more concentrated
    # because Shannon entropy decreases as the product prod n_i^n_i increases.
    assert hhi_numerator(A) < hhi_numerator(B)
    assert entropy_product(A) > entropy_product(B)

# First tie split at excess r=6 for every k >= 3.
for k in range(3, 101):
    A = profile_from_excess((3, 3), k)
    B = profile_from_excess((1, 1, 4), k)
    assert hhi_numerator(A) == hhi_numerator(B)
    assert entropy_product(A) == 65536
    assert entropy_product(B) == 50000

# Direct finite checks for fixed firm counts through the sharp layer.
for k in range(3, 11):
    for r in range(0, 8):
        profiles = [profile_from_excess(y, k) for y in partitions(r) if len(y) <= k]
        profiles = sorted(set(profiles))
        rev = 0
        for a, b in combinations(profiles, 2):
            dh = hhi_numerator(a) - hhi_numerator(b)
            dp = entropy_product(a) - entropy_product(b)
            if dh * dp < 0:
                rev += 1
        assert rev == (1 if r == 7 else 0), (k, r, rev)

print("VERIFY_OK")
print("strict_reversal_counts_by_excess", reversal_counts)
print("tie_split_counts_by_excess", tie_split_counts)
print("unique_first_reversal_excess_partitions", reversals)
print("three_firm_witness_A", profile_from_excess((3,4), 3))
print("three_firm_witness_B", profile_from_excess((1,1,5), 3))
print("universal_k_checked_3_to_100")
