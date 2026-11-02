#!/usr/bin/env python3
"""Independent exact finite checks for prefix--sparse convex geometries.

Run: python3 verify_prefix_sparse.py
Python 3.9+, standard library only.
"""
from functools import lru_cache
from math import comb
from itertools import combinations


def from_definition(k, n):
    """Original cardinality/prefix-membership rule."""
    ans = []
    for mask in range(1 << n):
        need = max(0, mask.bit_count() - k)
        if mask & ((1 << need) - 1) == (1 << need) - 1:
            ans.append(mask)
    return ans


def from_first_zero(k, n):
    """Independent first-zero/sparse-tail construction."""
    out = {((1 << n) - 1)}
    for i in range(n):
        prefix = (1 << i) - 1
        rest = list(range(i + 1, n))
        for tail in range(1 << len(rest)):
            if tail.bit_count() <= k:
                out.add(prefix | sum(1 << rest[j] for j in range(len(rest)) if (tail >> j) & 1))
    return sorted(out)


def exact_depth(k, n, depth):
    """Exact Boolean tree recurrence with cardinality pruning; no approximation."""
    concepts = [(1 << n) - 1]
    for i in range(n):
        prefix = (1 << i) - 1
        for t in range(min(k, n-i-1) + 1):
            for tail in combinations(range(i+1, n), t):
                concepts.append(prefix | sum(1 << j for j in tail))
    assert len(set(concepts)) == len(concepts)
    tests = [sum(1 << j for j, c in enumerate(concepts) if (c >> x) & 1)
             for x in range(n)]
    @lru_cache(None)
    def yes(mask, d):
        if d == 0:
            return bool(mask)
        if mask.bit_count() < (1 << d):
            return False
        for t in tests:
            one, zero = mask & t, mask & ~t
            if (one.bit_count() >= (1 << (d - 1))
                    and zero.bit_count() >= (1 << (d - 1))
                    and yes(one, d-1) and yes(zero, d-1)):
                return True
        return False
    result = yes((1 << len(concepts)) - 1, depth)
    return result, yes.cache_info().currsize


def bound(k, n, d):
    return 1 + sum((n-j) * comb(d, j) for j in range(min(k, d) + 1))


def check_basic():
    samples = 0
    for k in range(1, 4):
        for n in range(k + 2, 10):
            a = from_definition(k, n)
            b = from_first_zero(k, n)
            assert a == b, (k, n, 'two independent constructions differ')
            assert len(a) == sum(comb(n, j) for j in range(k+2))
            for p in range(1 << n):
                sampled = [i for i in range(n) if (p >> i) & 1]
                if len(sampled) > k + 2: continue
                traces = set(sum(1 << j for j, s in enumerate(sampled)
                                 if (c >> s) & 1) for c in a)
                shattered = len(traces) == 1 << len(sampled)
                assert shattered == (len(sampled) <= k + 1), (k, n, sampled)
                samples += 1
    print('STRUCTURE_AND_MAXIMUM_VC_PASS checked_supports=', samples)


def check_thresholds():
    # Certified first occurrences of depth 3 through depth 8.
    thresholds = [(3,4), (4,7), (5,12), (6,21), (7,39), (8,69)]
    for d, first in thresholds:
        lo, s1 = exact_depth(1, first - 1, d)
        hi, s2 = exact_depth(1, first, d)
        assert not lo and hi, (d, first, lo, hi)
        print('ONLINE_THRESHOLD_PASS depth=', d, 'first_n=', first,
              'states_pre=', s1, 'states_at=', s2)
    top, states = exact_depth(1,69,9)
    assert not top
    print('NO_DEPTH_NINE_THROUGH_69_PASS states=', states)
    for k, n, d in [(1,12,5),(1,21,6),(2,9,5),(3,8,5)]:
        yes, _ = exact_depth(k, n, d)
        assert yes
        assert 2 ** d <= bound(k, n, d)
    print('FINITE_BOUND_CHECKS_PASS')


if __name__ == '__main__':
    check_basic()
    check_thresholds()
    print('ALL_PREFIX_SPARSE_ONLINE_CHECKS_PASS')
