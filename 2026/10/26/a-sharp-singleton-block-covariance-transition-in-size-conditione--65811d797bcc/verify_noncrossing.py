#!/usr/bin/env python3
"""Exact checks for singleton/size-frequency covariance in noncrossing partitions."""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations
from math import comb

def all_set_partitions(n):
    def gen(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from gen(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from gen(i + 1, blocks)
        blocks.pop()
    yield from gen(0, [])

def noncrossing(parts):
    for index, a in enumerate(parts):
        for b in parts[index + 1:]:
            for x, y in combinations(a, 2):
                for z, w in combinations(b, 2):
                    if (x < z < y < w) or (z < x < w < y):
                        return False
    return True

def formula(n, k, s):
    assert n >= k + 2 and k >= 3 and 2 <= s <= n - k + 1
    p_s = Fraction(comb(n - s - 1, k - 2), comb(n - 1, k - 1))
    return k * (k - 1) * p_s * Fraction(k * s - 2 * (n - 1), (n - 1) * (n - s - 1))

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(1, n - k + 2):
            for rest in compositions(n - a, k - 1):
                yield (a,) + rest

ncs_checked = 0
cases = 0
for n in range(5, 10):
    by_k = defaultdict(list)
    for partition in all_set_partitions(n):
        if noncrossing(partition):
            by_k[len(partition)].append(tuple(Counter(map(len, partition)).items()))
    ncs_checked += sum(map(len, by_k.values()))
    assert ncs_checked > 0
    for k in range(3, n - 1):
        observed = Counter()
        for profile in by_k[k]:
            observed[tuple(sorted(profile))] += 1
        expected_comps = Counter()
        for comp in compositions(n, k):
            expected_comps[tuple(sorted(Counter(comp).items()))] += 1
        # All profiles have the same conditional probabilities as positive compositions.
        assert all(observed[t] * sum(expected_comps.values()) == expected_comps[t] * len(by_k[k])
                   for t in (set(observed) | set(expected_comps)))
        N = len(by_k[k])
        for s in range(2, n - k + 2):
            vals = [dict(t) for t in by_k[k]]
            a = sum(t.get(1, 0) for t in vals)
            b = sum(t.get(s, 0) for t in vals)
            ab = sum(t.get(1, 0) * t.get(s, 0) for t in vals)
            cov = Fraction(ab * N - a * b, N * N)
            target = formula(n, k, s)
            assert cov == target, (n, k, s, cov, target)
            assert (cov > 0) - (cov < 0) == ((k * s - 2 * (n - 1)) > 0) - ((k * s - 2 * (n - 1)) < 0)
            cases += 1
    print('NC_EXHAUSTIVE_PASS', n, sum(map(len, by_k.values())))

for n in range(5, 201):
    for k in range(3, n - 1):
        for s in range(2, n - k + 2):
            # Test the exact difference between the size-biased and unconditional means.
            p = Fraction(comb(n - s - 1, k - 2), comb(n - 1, k - 1))
            difference = Fraction((k - 1) * (k - 2), n - s - 1) - Fraction(k * (k - 1), n - 1)
            assert k * p * difference == formula(n, k, s)
assert formula(10, 3, 6) == 0
print('EXACT_ALGEBRA_PASS n=5..200')
print('VERIFY_OK', ncs_checked, 'noncrossing partitions;', cases, 'conditional covariance cases')
