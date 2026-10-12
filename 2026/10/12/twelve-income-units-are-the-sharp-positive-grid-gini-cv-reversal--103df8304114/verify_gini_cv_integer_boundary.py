#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import gcd


def partitions_pos(n, total, lo=1):
    if n == 1:
        if total >= lo:
            yield (total,)
        return
    for x in range(lo, total // n + 1):
        for rest in partitions_pos(n - 1, total - x, x):
            yield (x,) + rest


def gini_pair_num(x):
    return sum(abs(a - b) for i, a in enumerate(x) for b in x[i+1:])


def cv_scaled_num(x):
    n = len(x)
    s = sum(x)
    # CV^2 = this / (n*s^2).
    return sum((n*a - s)**2 for a in x)


def gini(x):
    return Fraction(gini_pair_num(x), len(x) * sum(x))


def cv2(x):
    n = len(x)
    s = sum(x)
    return Fraction(cv_scaled_num(x), n * s * s)

strict_counts = {}
weak_split_counts = {}
profile_counts = {}
pair_counts = {}
strict_pairs = {}
weak_splits = {}

for s in range(2, 13):
    strict = []
    splits = []
    profiles = 0
    pairs = 0
    for n in range(2, s + 1):
        ps = list(partitions_pos(n, s))
        profiles += len(ps)
        pairs += len(ps) * (len(ps) - 1) // 2
        for a, b in combinations(ps, 2):
            dg = gini_pair_num(a) - gini_pair_num(b)
            dc = cv_scaled_num(a) - cv_scaled_num(b)
            if dg * dc < 0:
                strict.append((n, a, b))
            if (dg == 0) != (dc == 0):
                splits.append((n, a, b, dg, dc))
    strict_counts[s] = len(strict)
    weak_split_counts[s] = len(splits)
    profile_counts[s] = profiles
    pair_counts[s] = pairs
    strict_pairs[s] = strict
    weak_splits[s] = splits

assert all(strict_counts[s] == 0 for s in range(2, 12))
assert strict_counts[12] == 1
assert strict_pairs[12] == [(4, (1, 2, 4, 5), (2, 2, 2, 6))]

assert all(weak_split_counts[s] == 0 for s in range(2, 10))
assert weak_split_counts[10] == 1
assert weak_splits[10][0][:3] == (3, (1, 4, 5), (2, 2, 6))

A = (1, 2, 4, 5)
B = (2, 2, 2, 6)
assert gini(A) == Fraction(7, 24)
assert gini(B) == Fraction(1, 4)
assert cv2(A) == Fraction(5, 18)
assert cv2(B) == Fraction(1, 3)
assert gini(A) > gini(B)
assert cv2(A) < cv2(B)

T1 = (1, 4, 5)
T2 = (2, 2, 6)
assert gini(T1) == gini(T2) == Fraction(4, 15)
assert cv2(T1) == Fraction(13, 50)
assert cv2(T2) == Fraction(8, 25)

# For two households the two measures are proportional: CV = 2 G.
for s in range(2, 101):
    ps = list(partitions_pos(2, s))
    for x in ps:
        assert cv2(x) == 4 * gini(x) * gini(x)

# A useful adjacent check: among exactly three households the first strict
# reversal is delayed to total 17, where it is unique.
for s in range(3, 17):
    ps = list(partitions_pos(3, s))
    assert all((gini_pair_num(a)-gini_pair_num(b))*(cv_scaled_num(a)-cv_scaled_num(b)) >= 0
               for a,b in combinations(ps,2))
ps = list(partitions_pos(3, 17))
rev3 = [(a,b) for a,b in combinations(ps,2)
        if (gini_pair_num(a)-gini_pair_num(b))*(cv_scaled_num(a)-cv_scaled_num(b)) < 0]
assert rev3 == [((1, 6, 10), (3, 3, 11))]

print('VERIFY_OK')
print('strict_counts', strict_counts)
print('weak_split_counts', weak_split_counts)
print('profile_counts', profile_counts)
print('pair_counts', pair_counts)
print('total_pair_checks_through_12', sum(pair_counts.values()))
print('first_tie_split', weak_splits[10][0])
print('first_strict_reversal', strict_pairs[12][0])
print('witness_gini', gini(A), gini(B))
print('witness_cv2', cv2(A), cv2(B))
print('three_household_first_strict', rev3)
