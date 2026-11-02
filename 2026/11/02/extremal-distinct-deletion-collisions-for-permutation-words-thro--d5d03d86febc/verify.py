#!/usr/bin/env python3
"""Exhaustive reproducibility check for finite permutation pattern-shadow intersections.

Uses two separately defined enumerations: forward deletion and inverse insertion.
All integer pair IDs encode unordered pairs of lexicographically ranked permutations.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial
import json


def normalize(sequence):
    lookup = {v: i for i, v in enumerate(sorted(sequence))}
    return tuple(lookup[v] for v in sequence)


def all_pairs_from_children(n, index):
    children = defaultdict(set)
    for perm in permutations(range(n)):
        k = index[perm]
        for deleted in range(n):
            child = normalize(perm[:deleted] + perm[deleted + 1:])
            children[child].add(k)
    assert len(children) == factorial(n - 1)
    return count_pair_common(children.values(), factorial(n))


def all_pairs_from_parents(n, index):
    parent_sets = []
    for child in permutations(range(n - 1)):
        possible = set()
        for missing in range(n):
            shifted = tuple(x + (x >= missing) for x in child)
            for pos in range(n):
                perm = shifted[:pos] + (missing,) + shifted[pos:]
                possible.add(index[perm])
        parent_sets.append(possible)
    return count_pair_common(parent_sets, factorial(n))


def count_pair_common(families, m):
    # Every common child contributes once to each unordered distinct parent pair.
    packed = []
    for fam in families:
        parents = sorted(fam)
        for i, left in enumerate(parents):
            packed.extend(left * m + right for right in parents[i + 1:])
    packed.sort()
    hist = Counter()
    extrema = set()
    maximum = 0
    i = 0
    while i < len(packed):
        j = i + 1
        while j < len(packed) and packed[j] == packed[i]:
            j += 1
        count = j - i
        hist[count] += 1
        if count > maximum:
            maximum, extrema = count, {packed[i]}
        elif count == maximum:
            extrema.add(packed[i])
        i = j
    return maximum, extrema, dict(sorted(hist.items()))


def construction(n, index):
    expected = set()
    for base in range(n - 3):
        # Four consecutive values form one indivisible block; all other
        # symbols are individually ordered.  The block is labeled by base.
        other = tuple(i for i in range(n) if i < base or i >= base + 4)
        for atoms in permutations(other + (base,)):
            j = atoms.index(base)
            left = atoms[:j] + (base + 1, base + 3, base, base + 2) + atoms[j + 1:]
            right = atoms[:j] + (base + 2, base, base + 3, base + 1) + atoms[j + 1:]
            a, b = sorted((index[left], index[right]))
            expected.add(a * factorial(n) + b)
    return expected


def main():
    for n in range(3, 9):
        idx = {p: i for i, p in enumerate(permutations(range(n)))}
        a = all_pairs_from_children(n, idx)
        b = all_pairs_from_parents(n, idx)
        assert a == b, (n, 'forward and inverse enumerations disagree')
        mx, extremizers, distribution = a
        if n == 3:
            assert mx == 2 and len(extremizers) == 6
        else:
            expected = construction(n, idx)
            assert mx == 4 and extremizers == expected
            assert len(expected) == (n - 3) * factorial(n - 3)
        print(json.dumps({'n': n, 'max_common_distinct': mx,
                          'number_extremal_pairs': len(extremizers),
                          'pair_intersection_histogram_positive': distribution},
                         separators=(',', ':'), sort_keys=True), flush=True)
    print('PASS: two complete enumerations agree; all extremizers classified')


if __name__ == '__main__':
    main()
