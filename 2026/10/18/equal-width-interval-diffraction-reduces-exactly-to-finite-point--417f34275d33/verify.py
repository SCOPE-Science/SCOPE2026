#!/usr/bin/env python3
"""Exact integer-endpoint corroboration for a finite-interval Fourier phase-retrieval theorem.

This checks finite enumerations and an explicit known homometric counterexample;
the accompanying analytic proof establishes the unrestricted real theorem.
"""
from collections import Counter
from itertools import combinations


def endpoint_measure(intervals):
    e = Counter()
    for a, b in intervals:
        assert a < b
        e[a] += 1
        e[b] -= 1
    return {x: c for x, c in e.items() if c}


def endpoint_corr(intervals):
    e = endpoint_measure(intervals)
    c = Counter()
    for x, ux in e.items():
        for y, uy in e.items():
            c[x - y] += ux * uy
    return tuple(sorted((d, v) for d, v in c.items() if v))


def normal_form(intervals):
    a = intervals[0][0]
    return tuple((u - a, v - a) for u, v in intervals)


def reflection_form(intervals):
    maxv = intervals[-1][1]
    return normal_form(tuple((maxv - v, maxv - u) for u, v in reversed(intervals)))


def interval_candidates(max_right, total_length):
    # One to three strictly separated positive-integer-length intervals.
    for n in range(1, total_length + 1):
        for ends in combinations(range(1, max_right + 1), 2 * n - 1):
            coords = (0,) + ends
            intervals = tuple((coords[2*j], coords[2*j+1]) for j in range(n))
            if not all(intervals[j][1] < intervals[j+1][0] for j in range(n-1)):
                continue
            if sum(v-u for u,v in intervals) != total_length:
                continue
            yield intervals


def differences(A):
    return Counter(x-y for x in A for y in A)


def main():
    maxright = 28
    population = list(interval_candidates(maxright, 3))
    by_corr = {}
    for g in population:
        by_corr.setdefault(endpoint_corr(g), []).append(g)
    target = [g for g in population if len(g) == 3 and all(v-u == 1 for u,v in g)]
    comparisons = 0
    for f in target:
        c = endpoint_corr(f)
        options = by_corr[c]
        for g in options:
            comparisons += 1
            assert normal_form(g) in {normal_form(f), reflection_form(f)}, (f,g)
            assert len(g) == 3 and all(v-u == 1 for u,v in g), (f,g)
    assert comparisons > 0
    A = (0,1,4,10,12,17)
    B = (0,1,8,11,13,17)
    assert differences(A) == differences(B)
    assert tuple(B) != tuple(A)
    assert tuple(B) != tuple(A[-1]-a for a in reversed(A))
    width4_A = tuple((4*a,4*a+1) for a in A)
    width4_B = tuple((4*b,4*b+1) for b in B)
    assert endpoint_corr(width4_A) == endpoint_corr(width4_B)
    print('VERIFY_OK finite exact comparisons:', comparisons,
          '; candidate interval unions:',len(population),
          '; three-window targets:',len(target),
          '; six-window homometric witness: verified')

if __name__ == '__main__':
    main()
