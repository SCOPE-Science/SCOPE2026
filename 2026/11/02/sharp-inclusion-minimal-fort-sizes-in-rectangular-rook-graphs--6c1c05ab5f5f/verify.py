#!/usr/bin/env python3
"""Independent finite verification of the minimal-fort rank for rook graphs.

Tests all proper subsets, not merely one-cell deletions. This is crucial:
being a fort is not a hereditary or upward-closed property.
"""
from collections import Counter


def predicted_rank(m, n):
    return m + n - 2 + (abs(m - n) == 1)


def calculate(m, n):
    N = m*n
    neighbors = []
    for i in range(m):
        for j in range(n):
            neighbors.append(sum(1 << (a*n+b) for a in range(m) for b in range(n)
                                 if (a, b) != (i, j) and (a == i or b == j)))
    full = (1 << N)-1
    # has_fort_submask[mask] means mask contains SOME nonempty fort.
    # Recurrence is exact even though the fort predicate is not monotone.
    has_fort_submask = bytearray(1 << N)
    min_distribution = Counter()
    all_forts = 0
    for mask in range(1, 1 << N):
        is_fort = True
        unused = full ^ mask
        while unused:
            bit = unused & -unused
            v = bit.bit_length()-1
            if (mask & neighbors[v]).bit_count() == 1:
                is_fort = False
                break
            unused ^= bit
        if is_fort:
            all_forts += 1
            # A fort is inclusion-minimal iff no proper subset contains a fort.
            proper_has = False
            bits = mask
            while bits:
                bit = bits & -bits
                if has_fort_submask[mask ^ bit]:
                    proper_has = True
                    break
                bits ^= bit
            if not proper_has:
                min_distribution[mask.bit_count()] += 1
            has_fort_submask[mask] = 1
        else:
            bits = mask
            while bits:
                bit = bits & -bits
                if has_fort_submask[mask ^ bit]:
                    has_fort_submask[mask] = 1
                    break
                bits ^= bit
    got = max(min_distribution)
    expected = predicted_rank(m,n)
    assert got == expected, (m,n,got,expected)
    return N,all_forts,dict(sorted(min_distribution.items()))


if __name__ == '__main__':
    trials = [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
    checked = 0
    for m,n in trials:
        N,all_count,dist = calculate(m,n)
        checked += (1 << N)
        print(f'{m}x{n}: all_forts={all_count}, minimal_histogram={dist}, '
              f'rank={max(dist)}, predicted={predicted_rank(m,n)}', flush=True)
    print(f'PASS: {len(trials)} boards; {checked} subset masks including empty tested.')
