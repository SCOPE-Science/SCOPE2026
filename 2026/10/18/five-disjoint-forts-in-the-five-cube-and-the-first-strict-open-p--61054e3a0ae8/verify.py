#!/usr/bin/env python3
"""Standalone exhaustive finite verification of fort packing in the 5-cube.
No external dependencies. This independently checks all small-fort cases and a
five-fort witness, and checks the parity profile of six-vertex forts.
"""
from itertools import combinations
from collections import Counter

DIM = 5
ORDER = 1 << DIM
ALL = (1 << ORDER) - 1
NEIGHBOR_MASKS = tuple(sum(1 << (v ^ (1 << i)) for i in range(DIM))
                       for v in range(ORDER))


def mask(vertices):
    return sum(1 << x for x in vertices)


def is_fort(f):
    if not f:
        return False
    outside = ALL ^ f
    while outside:
        vbit = outside & -outside
        v = vbit.bit_length() - 1
        if (NEIGHBOR_MASKS[v] & f).bit_count() == 1:
            return False
        outside -= vbit
    return True


def main():
    minimum_forts = []
    tested = 0
    for k in range(1, 6):
        count = 0
        for comb in combinations(range(ORDER), k):
            tested += 1
            f = mask(comb)
            if is_fort(f):
                count += 1
                if k == 5:
                    minimum_forts.append(f)
        if k < 5:
            assert count == 0, (k, count)
        else:
            assert count == 32, count
        print('fort_size', k, 'count', count)
    assert set(minimum_forts) == set(NEIGHBOR_MASKS)
    print('small_subset_checks', tested)
    packed_centers = (0, 1, 30, 31)
    packed = [NEIGHBOR_MASKS[c] for c in packed_centers]
    extra = mask((6, 7, 10, 11, 20, 21, 24, 25))
    packed.append(extra)
    assert all(is_fort(f) for f in packed)
    assert sum(f.bit_count() for f in packed) == (
        sum(packed).bit_count()) == 28
    assert all((a & b) == 0 for i, a in enumerate(packed)
               for b in packed[i+1:])
    print('five_fort_sizes', [f.bit_count() for f in packed])
    print('five_fort_union', sum(packed).bit_count())
    # Exhaustively confirm maximum open packing is four.
    compatible = Counter()
    for c in range(ORDER):
        compatible[c] = sum((NEIGHBOR_MASKS[c] & NEIGHBOR_MASKS[d]) == 0
                            for d in range(ORDER) if d != c)
    max_open = 0
    for s in range(1, 6):
        found = False
        for centers in combinations(range(ORDER), s):
            if all((NEIGHBOR_MASKS[a] & NEIGHBOR_MASKS[b]) == 0
                   for a, b in combinations(centers, 2)):
                found = True
                max_open = s
        if not found:
            break
    assert max_open == 4, max_open
    print('maximum_open_packing', max_open)
    # Check every six-vertex fort, including every parity split.
    parity_counts = Counter()
    for comb in combinations(range(ORDER), 6):
        f = mask(comb)
        if is_fort(f):
            even_count = sum(v.bit_count() % 2 == 0 for v in comb)
            parity_counts[even_count] += 1
    assert set(parity_counts) <= {0, 1, 5, 6}, parity_counts
    print('six_fort_parity_counts', dict(sorted(parity_counts.items())))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
