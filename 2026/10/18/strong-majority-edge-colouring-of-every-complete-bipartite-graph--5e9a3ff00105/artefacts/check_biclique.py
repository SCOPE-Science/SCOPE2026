#!/usr/bin/env python3
"""Standalone exact checks for strong-majority edge colourings of bicliques.

All tests use only the Python standard library. No external record, file or
solver is required. The bit-mask census is exhaustive for its stated finite
sizes; general parameter bounds are proved separately in RESULT.md.
"""
from collections import Counter
from math import comb

SPECIAL_44 = (
    (0, 2, 2, 0),
    (1, 2, 0, 1),
    (1, 0, 1, 2),
    (0, 1, 2, 0),
)
SPECIAL_47 = (
    (0, 2, 1, 0, 1, 2, 0),
    (1, 2, 0, 2, 2, 0, 1),
    (1, 0, 1, 2, 0, 1, 2),
    (0, 1, 2, 0, 2, 1, 0),
)


def is_strong_majority(matrix):
    a = len(matrix)
    b = len(matrix[0])
    colors = set(sum((list(row) for row in matrix), []))
    bound = (a + b - 2) // 2
    for i in range(a):
        for j in range(b):
            neighbors = [matrix[i][k] for k in range(b) if k != j]
            neighbors += [matrix[k][j] for k in range(a) if k != i]
            if any(neighbors.count(color) > bound for color in colors):
                return False
    return True


def examples(a, b):
    if a == 2:
        return tuple(tuple(j % 3 for j in range(b)) for _ in range(2))
    if (a, b) == (4, 4):
        return SPECIAL_44
    if (a, b) == (4, 7):
        return SPECIAL_47
    if (a, b) in ((3, 4), (4, 5)):
        return tuple(tuple((i + j) % 4 for j in range(b)) for i in range(a))
    return tuple(tuple((i + j) % 3 for j in range(b)) for i in range(a))


def exhaustive_one_color(a, b):
    """All 2^(ab) subsets, independently enforcing all ambient edge tests."""
    edges = [(i, j) for i in range(a) for j in range(b)]
    neighbor_masks = []
    for x, (i, j) in enumerate(edges):
        mask = 0
        for y, (u, v) in enumerate(edges):
            if y != x and (i == u or j == v):
                mask |= 1 << y
        neighbor_masks.append(mask)
    cap = (a + b - 2) // 2
    distribution = Counter()
    maximal = []
    for subset in range(1 << (a * b)):
        if all((subset & mask).bit_count() <= cap for mask in neighbor_masks):
            s = subset.bit_count()
            distribution[s] += 1
            if s >= (4 if (a, b) == (3, 4) else 6):
                maximal.append(subset)
    return distribution, maximal


def check_two_colors():
    for b in (2, 4, 6, 8):
        got = 0
        for mask in range(1 << (2 * b)):
            c = tuple(tuple((mask >> (i * b + j)) & 1 for j in range(b)) for i in range(2))
            if is_strong_majority(c):
                got += 1
        target = 4 if b == 2 else comb(b, b // 2)
        assert got == target, (b, got, target)
    for a, b in ((2, 3), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4)):
        found = any(is_strong_majority(tuple(tuple((m >> (i * b + j)) & 1
                                            for j in range(b)) for i in range(a)))
                    for m in range(1 << (a * b)))
        assert not found, (a, b)


def main():
    for a in range(2, 21):
        for b in range(a, 31):
            assert is_strong_majority(examples(a, b)), (a, b)
            used = len(set(sum((list(row) for row in examples(a, b)), [])))
            expected = 4 if (a, b) in ((3, 4), (4, 5)) else 3
            assert used <= expected, (a, b, used)
    assert is_strong_majority(SPECIAL_44)
    assert is_strong_majority(SPECIAL_47)
    check_two_colors()
    distribution34, top34 = exhaustive_one_color(3, 4)
    assert sorted(distribution34.items()) == [(0, 1), (1, 12), (2, 66), (3, 100), (4, 18)]
    for mask in top34:
        assert mask.bit_count() == 4
        rowdeg = sorted(sum((mask >> (i*4+j)) & 1 for j in range(4)) for i in range(3))
        coldeg = sorted(sum((mask >> (i*4+j)) & 1 for i in range(3)) for j in range(4))
        assert rowdeg == [0, 2, 2] and coldeg == [0, 0, 2, 2]
    distribution45, top45 = exhaustive_one_color(4, 5)
    assert sorted(distribution45.items()) == [(0, 1), (1, 20), (2, 190), (3, 1140),
        (4, 4145), (5, 6600), (6, 1900)]
    assert all(mask.bit_count() == 6 for mask in top45)
    print('PASS: modular and exceptional constructions for 2 <= a <= 20, a <= b <= 30')
    print('PASS: two-colour full labelled enumeration at K_(2,b) b=2,4,6,8 and six obstructions')
    print('PASS: 2^12=4096 one-class subsets of K_(3,4), max 4, exactly 18 rectangles')
    print('PASS: 2^20=1048576 one-class subsets of K_(4,5), max 6, exactly 1900 maximizers')
    print('PASS: complete finite certificate; infinite cases rely on the accompanying proof')


if __name__ == '__main__':
    main()
