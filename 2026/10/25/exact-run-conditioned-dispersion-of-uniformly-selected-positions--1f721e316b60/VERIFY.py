#!/usr/bin/env python3
"""Exact finite reproducibility checks for a run-count/position-variance identity.

Standard library only. Finite checks complement, but do not replace, the proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def predicted_conditional(n, k, r):
    return F(k * (k + 1), 12) + F((k + 1) * (n - k + 2) * (n + k + 1) * (r - 1), 12 * (k - 1) * (r + 1))


def predicted_covariance(n, k):
    return F((n - k) * (n + k + 1), 6 * n)


def falling(a, t):
    out = 1
    for j in range(t):
        out *= a - j
    return out


def pair_overlap_expectation(n, k):
    # Aggregate exact mixed moments by union size of an edge and point pair.
    assert n >= 4
    all_pair_weight = F(n * n * (n * n - 1), 12)
    one_shared = F((n - 2) * (n - 1) * (n * n + n + 3), 3)
    two_shared = n - 1
    disjoint = (n - 1) * all_pair_weight - one_shared - two_shared
    p2 = F(falling(k, 2), falling(n, 2))
    sums = {2: two_shared, 3: one_shared, 4: disjoint}
    out = F(0)
    for union_size, weight in sums.items():
        if k < union_size:
            joint = F(0)
        else:
            joint = F(falling(k, union_size), falling(n, union_size))
        out += weight * (joint - p2 * p2)
    return -out / (k * (k - 1))  # run count = k - adjacency count


def gap_moment_regression(n, k, r):
    # This is an independent route through exchangeable weak compositions.
    # Formula checked independently against enumerated samples below.
    if k == 2:
        # Conditional on one run the two marks are adjacent. Otherwise,
        # the uniform nonadjacent pair has a position-difference distribution
        # proportional to n-d for d >= 2.
        if r == 1:
            return F(1, 2)
        assert r == 2
        numerator = sum((n - d) * d * d for d in range(2, n))
        denominator = sum(n - d for d in range(2, n))
        return F(numerator, 2 * denominator)
    q = r - 1
    b = r + 1
    m = n - k
    leftover = m - q
    m1 = F(q, k - 1) * (1 + F(leftover, b))
    m2 = F(q, k - 1) * (1 + F(3 * leftover, b) + F(2 * leftover * (leftover - 1), b * (b + 1)))
    cross = F(q * (q - 1), (k - 1) * (k - 2)) * (
        1 + F(2 * leftover, b) + F(leftover * (leftover - 1), b * (b + 1)))
    # Pair distances are sums of d unit steps plus d internal vacant gaps.
    out = F(0)
    for d in range(1, k):
        distance2 = d*d*(1 + 2*m1 + cross) + d*(m2 - cross)
        out += (k - d) * distance2
    return out / (k*(k-1))


def main():
    stats = defaultdict(int)
    for n in range(2, 14):
        for k in range(2, n+1):
            groups = defaultdict(lambda: [F(0), 0])
            count, total_r, total_v, total_rv = 0, F(0), F(0), F(0)
            for positions in combinations(range(1, n+1), k):
                r = 1 + sum(positions[j+1] > positions[j]+1 for j in range(k-1))
                v = F(sum((positions[j]-positions[i])**2 for i in range(k) for j in range(i+1,k)), k*(k-1))
                groups[r][0] += v
                groups[r][1] += 1
                count += 1
                total_r += r
                total_v += v
                total_rv += r*v
                stats['samples_enumerated'] += 1
            assert count == comb(n,k)
            assert total_v/count == F(n*(n+1),12)
            stats['marginal_checks'] += 1
            for r,(vsum,howmany) in groups.items():
                assert howmany == comb(k-1,r-1)*comb(n-k+1,r)
                assert vsum/howmany == predicted_conditional(n,k,r)
                assert vsum/howmany == gap_moment_regression(n,k,r)
                stats['conditional_groups_checked'] += 1
            cv = total_rv/count-(total_r/count)*(total_v/count)
            assert cv == predicted_covariance(n,k)
            stats['exhaustive_covariance_checks'] += 1
    # A broad independent exact overlap-count calculation, no enumeration.
    for n in range(4, 121):
        for k in range(2, n+1):
            assert pair_overlap_expectation(n,k) == predicted_covariance(n,k)
            stats['pair_overlap_checks'] += 1
    # Broad tests of the weak-composition moment computation, no enumeration.
    for n in range(2, 81):
        for k in range(2, n+1):
            for r in range(1, min(k,n-k+1)+1):
                assert gap_moment_regression(n,k,r) == predicted_conditional(n,k,r)
                stats['gap_moment_checks'] += 1
                if r < min(k,n-k+1):
                    assert predicted_conditional(n,k,r+1) > predicted_conditional(n,k,r)
                    stats['strict_monotonicity_checks'] += 1
    print(json.dumps(dict(sorted(stats.items())),sort_keys=True))

if __name__ == '__main__':
    main()
