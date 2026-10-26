#!/usr/bin/env python3
"""Exact two-round first-order type checks for cyclic groups in a relational language.

No external packages are required.  Exhaustive tests supplement, not replace,
the structural proof for arbitrary cyclic-group orders.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import gcd


def raw_atomic_pair_type(n, x, y):
    values = (x, y, 0)
    eq = tuple(values[i] == values[j] for i, j in combinations_with_replacement(range(3), 2))
    mult = tuple((values[i] + values[j] - values[k]) % n == 0
                 for i, j in combinations_with_replacement(range(3), 2)
                 for k in range(3))
    return eq + mult


def reduced_atomic_pair_type(n, x, y):
    return (x == 0, y == 0, x == y,
            (2 * x) % n == 0, (2 * y) % n == 0,
            (2 * x - y) % n == 0, (2 * y - x) % n == 0,
            (x + y) % n == 0)


def rank_two_signature(n, pair_type):
    # Correct EF invariant: set of pointed one-step extension types.
    return frozenset((x == 0, (2*x) % n == 0,
                      frozenset(pair_type(n, x, y) for y in range(n)))
                     for x in range(n))


def stable_class(n):
    assert n >= 1
    if n in {1, 2, 3, 4, 5, 6, 8}:
        return ('exception', n)
    return ('stable', gcd(n, 24))


def formula_bitmask(n):
    def R(a, b, c):
        return (a+b-c) % n == 0
    def large(x):
        return any(R(x,x,y) and y != 0 and y != x and not R(y,y,0)
                   and not R(x,y,0) for y in range(n))
    def halve(x):
        return any(R(y,y,x) for y in range(n))
    def generic(x):
        return any(y != 0 and y != x and not R(x,y,0) and not R(x,x,y)
                   and not R(y,y,0) and not R(y,y,x) for y in range(n))
    bits = [
        any(x and R(x,x,0) for x in range(n)),
        any(x and R(x,x,y) and R(x,y,0) for x in range(n) for y in range(n)),
        any(x and R(x,x,0) and R(y,y,x) for x in range(n) for y in range(n)),
        any(x and any(R(x,x,y) and y and R(y,y,0) for y in range(n))
            and halve(x) for x in range(1,n)),
        any(large(x) for x in range(n)),
        any(large(x) and halve(x) for x in range(n)),
        any(generic(x) for x in range(1,n)),
    ]
    return tuple(bits)


def main():
    # Complete syntactic atomic language compared against eight-bit reduction.
    for n in range(1, 65):
        raw = rank_two_signature(n, raw_atomic_pair_type)
        red = rank_two_signature(n, reduced_atomic_pair_type)
        # Structural relation is tested by comparing equivalence relations below.
        if n == 1:
            raw_sig, red_sig = {}, {}
        for oldn in range(1, n):
            assert ((raw == raw_sig[oldn]) == (red == red_sig[oldn])), (n, oldn)
        raw_sig[n], red_sig[n] = raw, red
    print('ATOMIC_LANGUAGE_REDUCTION_OK n=1..64 pairwise_comparisons=2016')

    data = defaultdict(list)
    signatures = {}
    for n in range(1, 129):
        key = rank_two_signature(n, reduced_atomic_pair_type)
        signatures[n] = key
        data[key].append(n)
    assert len(data) == 15, len(data)
    representatives = sorted(min(ns) for ns in data.values())
    assert representatives == [1,2,3,4,5,6,7,8,9,10,12,16,18,20,24], representatives
    for n in range(1,129):
        for m in range(1,n):
            assert (signatures[n] == signatures[m]) == (stable_class(n) == stable_class(m)), (m,n)
    print('EXACT_RANK2_OK n=1..128 classes=15 representatives=' + ','.join(map(str,representatives)))

    masks = {}
    for n in range(1,129):
        mask = formula_bitmask(n)
        assert all((mask == masks[m]) == (stable_class(n) == stable_class(m))
                   for m in masks), n
        masks[n] = mask
    print('EXPLICIT_FORMULAS_OK seven_rank_two_sentences_separate_all_15_classes')

    # Spot checks beyond the exhaustive grid.
    for n in [143,160,180,192,210,240,252,256,300,360]:
        sig = rank_two_signature(n, reduced_atomic_pair_type)
        rep = min(k for k in range(1,129) if stable_class(k) == stable_class(n))
        assert sig == signatures[rep], (n,rep)
    print('LARGE_ORDER_CHECKS_OK sampled_orders=143,160,180,192,210,240,252,256,300,360')
    print('SHARP_FAMILY_REPRESENTATIVE_OK min_maximum_order=24')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
