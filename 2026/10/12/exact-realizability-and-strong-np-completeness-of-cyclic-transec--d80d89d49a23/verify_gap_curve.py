#!/usr/bin/env python3
"""Exact finite checks for cyclic spatial species-richness realizability."""
from fractions import Fraction
from itertools import combinations, product
from functools import lru_cache


def observed_curve(n, masks):
    """Direct average over all n translates of k consecutive positions."""
    out = []
    for k in range(1, n + 1):
        total = 0
        for t in range(n):
            window = sum(1 << ((t + j) % n) for j in range(k))
            total += sum(bool(mask & window) for mask in masks)
        out.append(Fraction(total, n))
    return tuple(out)


def gaps(n, mask):
    """Lengths of all maximal cyclic zero runs, for nonempty binary mask."""
    assert 0 < mask < 1 << n
    if mask == (1 << n) - 1:
        return []
    starts = [j for j in range(n) if not mask & (1 << j) and mask & (1 << ((j - 1) % n))]
    lengths = []
    for j in starts:
        z = 0
        while not mask & (1 << ((j + z) % n)):
            z += 1
        lengths.append(z)
    return lengths


def curve_from_gaps(n, s, all_gaps):
    return tuple(Fraction(s, 1) - Fraction(sum(max(g - k + 1, 0) for g in all_gaps), n)
                 for k in range(1, n + 1))


def invert_curve(n, s, curve):
    assert len(curve) == n
    if curve[-1] != s:
        return None
    tails = [n * (curve[k] - curve[k - 1]) for k in range(1, n)]
    # tails[k-1] = number of runs with length >= k (1 <= k <= n-1).
    h = [tails[k] - tails[k + 1] for k in range(n - 2)] + [tails[-1]]
    if any(c.denominator != 1 or c < 0 for c in h):
        return None
    return tuple(sum(([g] * int(h[g - 1]) for g in range(1, n)), []))


def packable(n, s, lengths):
    """True iff run lengths plus their mandatory separators fit in s cycles."""
    items = sorted((g + 1 for g in lengths), reverse=True)
    if any(a > n for a in items):
        return False

    @lru_cache(None)
    def rec(i, space):
        if i == len(items):
            return True
        previous = -1
        for j, c in enumerate(space):
            if c != previous and c >= items[i]:
                newer = list(space)
                newer[j] -= items[i]
                if rec(i + 1, tuple(sorted(newer, reverse=True))):
                    return True
                previous = c
        return False

    return rec(0, (n,) * s)


def realizable(n, s, curve):
    gg = invert_curve(n, s, curve)
    return gg is not None and packable(n, s, gg)


def test_small():
    cases, matrices, signatures = 0, 0, 0
    # Enumerate all nonempty species incidence masks. Includes identical species.
    for n, s in [(2, 1), (3, 2), (4, 2), (4, 3), (5, 2), (5, 3), (6, 2)]:
        words = list(range(1, 1 << n))
        empirical = set()
        for masks in product(words, repeat=s):
            curve = observed_curve(n, masks)
            gg = [g for mask in masks for g in gaps(n, mask)]
            assert curve == curve_from_gaps(n, s, gg)
            assert tuple(sorted(gg)) == invert_curve(n, s, curve)
            empirical.add(curve)
            matrices += 1
        assert all(realizable(n, s, curve) for curve in empirical)
        # Enumerate every integer gap histogram with <=s*n items by bounded recursion via all multisets
        # of sizes <=n and aggregate mandatory-size <=n*s.
        from collections import Counter
        seen = set()
        def histograms(g, capacity, current):
            if g == n:
                cc = curve_from_gaps(n, s, current)
                poss = packable(n, s, tuple(current))
                if poss:
                    assert cc in empirical, (n, s, current, cc)
                seen.add(cc)
                return
            for k in range(capacity // (g + 1) + 1):
                histograms(g + 1, capacity - k * (g + 1), current + [g] * k)
        if n <= 5:
            histograms(1, n*s, [])
        cases += 1
        signatures += len(empirical)
        print('CASE', n, s, 'matrices', len(words)**s, 'curves', len(empirical), 'hist_curves',len(seen))
    no = (Fraction(3,5), Fraction(6,5), Fraction(9,5), Fraction(2), Fraction(2))
    assert invert_curve(5, 2, no) == (2, 2, 3)
    assert not realizable(5, 2, no)
    # 3-partition yes: 12,12,12 and 12,12,12 in bins of 36; no: 3,3,4 in bins of 5.
    B, m, aa = 36, 2, (12,)*6
    yc = tuple(Fraction(m) - Fraction(sum(max(a-k, 0) for a in aa), B) for k in range(1,B+1))
    assert realizable(B, m, yc)
    assert not packable(5, 2, (2,2,3))
    print('VERIFY_OK matrices',matrices,'distinct_curves', signatures,'cases',cases,'infeasible_concave=1','partition_bridge=1')

if __name__ == '__main__':
    test_small()
