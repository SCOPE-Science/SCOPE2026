#!/usr/bin/env python3
"""Exact finite certificate for Fano-plane spanning-time dominance.

Use: python3 verify.py. Standard library only.
"""
from collections import Counter
from itertools import combinations_with_replacement, combinations

V = range(1, 8)
planes = [frozenset(x for x in V if ((x & a).bit_count() % 2) == 0)
          for a in V]
assert len(set(planes)) == 7
assert all(len(P) == 3 for P in planes)
assert all(sum(x in P for P in planes) == 3 for x in V)
assert all(sum(x in P and y in P for P in planes) == 1
           for x, y in combinations(V, 2))

def closure(elements):
    s = frozenset([0])
    for x in elements:
        s = s | frozenset(a ^ x for a in s)
    return s

subs = sorted({closure(S) for r in range(9)
               for S in combinations(range(8), r)},
              key=lambda S: (len(S), tuple(sorted(S))))
assert len(subs) == 16
index = {S: i for i, S in enumerate(subs)}
trans = [[index[S | frozenset(y ^ x for y in S)] for x in range(8)]
         for S in subs]
start = index[frozenset([0])]
full = index[frozenset(range(8))]

def failures_mobius(counts, t):
    z = counts[0]
    # Subspaces of codimension 1, 2, 3 have Mobius weights 1, -2, 8.
    plane_sizes = [z + sum(counts[x] for x in P) for P in planes]
    line_sizes = [z + counts[x] for x in V]
    return sum(s ** t for s in plane_sizes) - 2 * sum(s ** t for s in line_sizes) + 8 * z ** t

def failures_dp(counts):
    dp = [0] * len(subs)
    dp[start] = 1
    failure = []
    for t in range(1, 7):
        new = [0] * len(subs)
        for i, val in enumerate(dp):
            if val:
                for x, mult in enumerate(counts):
                    if mult:
                        new[trans[i][x]] += val * mult
        dp = new
        f = 7**t - dp[full]
        assert sum(dp) == 7**t
        assert f == failures_mobius(counts, t)
        failure.append(f)
    return failure

base = (0, 1, 1, 1, 1, 1, 1, 1)
base_f = failures_dp(base)
assert base_f == [7, 49, 175, 553, 1687, 5089]
count_total = 0
count_full = 0
count_unique = 0
min_delta = [None] * 4
min_count = [0] * 4
minimizers = [set() for _ in range(4)]

for chosen in combinations_with_replacement(range(8), 7):
    count_total += 1
    counts = tuple(chosen.count(x) for x in range(8))
    if len(closure(chosen)) != 8:
        continue
    count_full += 1
    failure = failures_dp(counts)
    if counts == base:
        count_unique += 1
        continue
    # For any non-simplex, a Fano plane contains at least four columns.
    assert max(counts[0] + sum(counts[x] for x in P) for P in planes) >= 4
    for j, t in enumerate(range(3, 7)):
        delta = failure[t-1] - base_f[t-1]
        assert delta > 0
        if min_delta[j] is None or delta < min_delta[j]:
            min_delta[j] = delta
            min_count[j] = 1
            minimizers[j] = {counts}
        elif delta == min_delta[j]:
            min_count[j] += 1
            minimizers[j].add(counts)

assert (count_total, count_full, count_unique) == (3432, 2696, 1)
assert min_delta == [24, 192, 1080, 5280]
assert min_count == [42, 42, 42, 42]
for subset in minimizers:
    assert len(subset) == 42
    assert all(c[0] == 0 and sorted(c[1:]) == [0, 1, 1, 1, 1, 1, 2]
               for c in subset)
# For t>=7, other codes have P(T>t)>= (4/7)^t, while
# the simplex has P(T>t)=(7*3^t-14)/7^t. Since
# 4^7 > 7*3^7 and 4/3>1, the strict inequality follows.
assert 4**7 > 7 * 3**7
print('compositions', count_total, 'full-rank', count_full)
print('simplex failure numerators t=3..6', base_f[2:])
print('minimum non-simplex excess numerators', min_delta)
print('minimizer multiplicities', min_count)
print('VERIFY_OK')
