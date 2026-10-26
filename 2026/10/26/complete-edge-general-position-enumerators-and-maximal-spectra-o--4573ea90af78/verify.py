#!/usr/bin/env python3
"""Exact finite checks for edge general position sets of simple cycles.

Uses original geodesic definition, independently of cyclic-gap counting proof.
Python 3 standard library only; no external inputs.
"""
from collections import Counter
from itertools import combinations
from math import comb


def formula(n):
    if n <= 5:
        return [comb(n, k) for k in range(n + 1)]
    m = n // 2
    c3 = n * (comb(n-1, 2) - 3 * comb(m-1, 2)) // 3
    c4 = comb(m, 2) if n % 2 == 0 else n * (m-1)
    return [1, n, comb(n, 2), c3, c4]


def maximal_formula(n):
    m = n // 2
    if n % 2 == 0:
        t3 = m * (m-1) * (m-2) // 3
        t4 = comb(m, 2)
    else:
        t3 = n * (m-2) * (m-3) // 6
        t4 = n * (m-1)
    return {3: t3, 4: t4}


def shortest_path_masks(n):
    """Enumerate all directed shortest paths of a cycle as edge masks.

    Clockwise paths suffice as every undirected geodesic admits
    a clockwise orientation of length <= floor(n/2).
    """
    masks = set()
    for initial_vertex in range(n):
        for length in range(1, n//2 + 1):
            mask = 0
            for step in range(length):
                mask |= 1 << ((initial_vertex + step) % n)
            masks.add(mask)
    return tuple(sorted(masks))


def exact_counts(n):
    paths = shortest_path_masks(n)
    counts = Counter()
    maximal = Counter()
    allmask = (1 << n) - 1
    allowed = bytearray(1 << n)
    for mask in range(1 << n):
        allowed[mask] = int(all((mask & path).bit_count() < 3 for path in paths))
        if allowed[mask]:
            counts[mask.bit_count()] += 1
    for mask in range(1 << n):
        if not allowed[mask]:
            continue
        missing = allmask ^ mask
        max_flag = True
        while missing:
            bit = missing & -missing
            missing ^= bit
            if allowed[mask | bit]:
                max_flag = False
                break
        if max_flag:
            maximal[mask.bit_count()] += 1
    return counts, maximal, allowed


def gap_condition(n, selected):
    if len(selected) <= 2:
        return True
    if len(selected) > 4:
        return False
    b = (n+1)//2
    gaps = [((selected[(i+1) % len(selected)] - selected[i]) % n)
            for i in range(len(selected))]
    if len(selected) == 3:
        return max(gaps) <= b
    return all(gaps[i] + gaps[(i+1) % 4] <= b for i in range(4))


def gap_maximal(n, selected):
    if len(selected) == 4:
        return True
    if len(selected) <= 2:
        return False
    m = n // 2
    gaps = [((selected[(i+1) % 3] - selected[i]) % n) for i in range(3)]
    return max(gaps) < m


def run():
    total_subsets = 0
    for n in range(3, 17):
        counts, maximal, allowed = exact_counts(n)
        prediction = formula(n)
        actual = [counts[k] for k in range(n+1)]
        assert actual == prediction + [0] * (n+1-len(prediction)), (n, actual, prediction)
        if n >= 6:
            for mask in range(1<<n):
                if mask.bit_count() <= 2 or mask.bit_count() > 4:
                    continue
                selected = tuple(i for i in range(n) if mask>>i&1)
                assert bool(allowed[mask]) == gap_condition(n, selected), (n, selected)
                if allowed[mask]:
                    assert (maximal.get(mask.bit_count(),0) >= 0)
                    if mask.bit_count() == 3:
                        truly_maximal = all(not allowed[mask | (1<<i)] for i in range(n) if not mask >> i & 1)
                        assert truly_maximal == gap_maximal(n, selected), (n,selected)
            expected_max = maximal_formula(n)
            assert dict(maximal) == {k:v for k,v in expected_max.items() if v}, (n,maximal,expected_max)
        total_subsets += 1 << n
        print(f'n={n:2d}  coefficients={actual[:max(actual.__len__(),5)] if n<6 else actual[:5]}  maximal={dict(sorted(maximal.items()))}')
    print(f'ALL PASS: exact independent geodesic checks for {total_subsets} subsets, n=3..16')

if __name__ == '__main__':
    run()
