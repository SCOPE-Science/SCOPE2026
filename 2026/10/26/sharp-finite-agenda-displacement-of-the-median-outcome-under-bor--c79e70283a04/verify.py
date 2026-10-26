#!/usr/bin/env python3
"""Exact finite checks for median-peak / Borda-axis displacement on single-peaked profiles."""
import json
from itertools import combinations_with_replacement
from math import comb


def single_peaked_orders(m):
    # Build each ranking from worst to best by deleting one of the two axis endpoints.
    def delete_ends(lo, hi):
        if lo == hi:
            yield (lo,)
            return
        for rem in delete_ends(lo + 1, hi):
            yield (lo,) + rem
        for rem in delete_ends(lo, hi - 1):
            yield (hi,) + rem
    return tuple(p[::-1] for p in delete_ends(0, m - 1))


def is_sp(p):
    # Independent direct check of within-side monotonicity.
    peak = p[0]
    loc = {x: i for i, x in enumerate(p)}
    return all(loc[x] < loc[x - 1] for x in range(1, peak + 1)) and all(
        loc[x] < loc[x + 1] for x in range(peak, len(p) - 1)
    )


def score(profile, m):
    s = [0] * m
    for p in profile:
        for j, a in enumerate(p):
            s[a] += m - 1 - j
    return s


def witness(m, r):
    w = (m - 1) // (r + 1) + 1
    high = tuple(range(m - 1, -1, -1))
    low = tuple(range(w, -1, -1)) + tuple(range(w + 1, m))
    return w, (high,) * (r + 1) + (low,) * r


def sharp_distance(m, r):
    return (r * (m - 1) - 1) // (r + 1)


def check():
    constructed = 0
    for m in range(2, 51):
        for r in range(1, 41):
            d = sharp_distance(m, r)
            w, p = witness(m, r)
            assert all(is_sp(order) for order in p)
            assert sorted(q[0] for q in p)[r] == m - 1
            s = score(p, m)
            assert s.index(max(s)) == w and s.count(max(s)) == 1
            assert m - 1 - w == d
            assert d == m - 2 - (m - 1) // (r + 1)
            constructed += 1
    exhaustive = []
    for m in range(2, 7):
        orders = single_peaked_orders(m)
        assert len(orders) == 2 ** (m - 1)
        assert all(is_sp(p) for p in orders)
        for r in (1, 2, 3):
            n = 2 * r + 1
            count = comb(len(orders) + n - 1, n)
            if count > 200000:
                continue
            ranks = tuple(tuple(m - 1 - p.index(i) for i in range(m)) for p in orders)
            peaks = tuple(p[0] for p in orders)
            observed_max = 0
            for choice in combinations_with_replacement(range(len(orders)), n):
                median = sorted(peaks[j] for j in choice)[r]
                s = [sum(ranks[j][i] for j in choice) for i in range(m)]
                if s.count(max(s)) != 1:
                    continue
                winner = s.index(max(s))
                d = abs(winner - median)
                assert d <= sharp_distance(m, r), (m, n, choice, median, winner)
                observed_max = max(observed_max, d)
            assert observed_max == sharp_distance(m, r)
            exhaustive.append({'alternatives':m,'voters':n,'anonymous_profiles':count,'max_distance':observed_max})
    return {'schema_version':1,'constructed_cases':constructed,'exhaustive':exhaustive,
            'constructed_scope':{'min_alternatives':2,'max_alternatives':50,'min_half_electorate':1,'max_half_electorate':40},
            'result':'PASS','proof_dependency':'The arbitrary-parameter theorem is proved algebraically; finite enumerations corroborate it.'}


if __name__ == '__main__':
    print(json.dumps(check(),sort_keys=True,indent=2))
