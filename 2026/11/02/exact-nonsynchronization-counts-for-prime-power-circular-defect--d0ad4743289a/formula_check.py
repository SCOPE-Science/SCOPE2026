#!/usr/bin/env python3
"""Exact arithmetic for defect-one circular automata with prime-power state counts."""
from math import factorial, comb
from itertools import combinations, permutations


def exceptional_count(p, k):
    assert p >= 2 and k >= 2
    n = p ** k
    total = 0
    for t in range(1, k):
        for levels in combinations(range(1, k), t):
            top = levels[-1]
            block_count = p ** top
            block_size = p ** (k - top)
            group_size = 1
            previous = 0
            for level in levels:
                group_size *= factorial(p ** (level - previous)) ** (p ** previous)
                previous = level
            count = (group_size * block_count *
                     factorial(block_size) ** block_count *
                     comb(block_size, 2))
            total += (-1 if t % 2 == 0 else 1) * count
    return total


def preserves(perm, r):
    image = {}
    for x, y in enumerate(perm):
        src = x % r
        dst = y % r
        if src in image and image[src] != dst:
            return False
        image[src] = dst
    return len(set(image.values())) == r


def verify_groups():
    # Direct finite symmetric-group enumeration, independent of factorial formula.
    expected = {(2, (1,)): 2, (4, (2,)): 24,
                (4, (1, 2)): 8, (8, (1, 2, 3)): 128}
    for (L, levels), size in expected.items():
        count = sum(all(preserves(sigma, 2 ** j) for j in levels)
                    for sigma in permutations(range(L)))
        assert count == size, (L, levels, count, size)


def main():
    known = {(2, 2): 16, (2, 3): 14848, (3, 2): 11664,
             (2, 4): 182285762560, (3, 3): 30964600730445078528,
             (2, 5): 210126310372982592935494156288}
    for (p, k), wanted in known.items():
        observed = exceptional_count(p, k)
        assert observed == wanted, (p, k, observed, wanted)
        n = p ** k
        assert 0 < observed < factorial(n) * comb(n, 2)
        assert observed % n == 0
        print('p', p, 'k', k, 'n', n, 'exceptional', observed,
              'rotation_classes', observed // n)
    verify_groups()
    print('FORMULA_VERIFY_OK')


if __name__ == '__main__':
    main()
