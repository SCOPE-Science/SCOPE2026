#!/usr/bin/env python3
"""Exact finite census of primitive length-two substitutions on {0,1,2}.

All calculations use Python integers; no nonstandard dependencies.  The
mathematical connection of the matrix spectra to amorphic complexity is
Theorems A and B of Groeger--Krawczyk (arXiv:2602.23267).
"""
from collections import Counter
from itertools import permutations, product

PAIR = ((0, 1), (0, 2), (1, 2))
P_INDEX = {ab: j for j, ab in enumerate(PAIR)}


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def primitive(words):
    m = tuple(tuple(sum(v == i for v in words[j]) for j in range(3))
              for i in range(3))
    cur = m
    for exponent in range(1, 6):
        if all(cur[i][j] > 0 for i in range(3) for j in range(3)):
            return True
        cur = mul(cur, m)
    return False


def discrepancy(words):
    matrix = [[0] * 3 for _ in range(3)]
    for j, (a, b) in enumerate(PAIR):
        for site in (0, 1):
            u, v = words[a][site], words[b][site]
            if u != v:
                matrix[P_INDEX[tuple(sorted((u, v)))]][j] += 1
    return tuple(map(tuple, matrix))


def det(m):
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def polynomial(m):
    trace = sum(m[i][i] for i in range(3))
    b = sum(m[i][i] * m[j][j] - m[i][j] * m[j][i]
            for i in range(3) for j in range(i + 1, 3))
    return (1, -trace, b, -det(m))


def alternate_polynomial(m):
    # Independent characteristic-polynomial implementation: determinants.
    def val(z):
        return det(tuple(tuple((z if i == j else 0) - m[i][j]
                               for j in range(3)) for i in range(3)))
    v0, v1, vm1 = val(0), val(1), val(-1)
    c = v0
    a = (v1 + vm1 - 2 * c) // 2
    b = (v1 - vm1 - 2) // 2
    assert (v1 + vm1 - 2 * c) % 2 == 0
    assert (v1 - vm1 - 2) % 2 == 0
    assert val(3) == 27 + a * 9 + b * 3 + c
    return (1, a, b, c)


POLY_CLASS = {
    (1, 0, 0, 0): 'zero',
    (1, 0, 0, -1): 'one',
    (1, -1, 0, 0): 'one',
    (1, 0, -1, 0): 'one',
    (1, -2, 1, 0): 'one',
    (1, -1, -2, 2): 'square_root_two',
    (1, 0, -1, -2): 'cubic_one',
    (1, -1, -1, 0): 'golden_ratio',
    (1, -2, 0, 1): 'golden_ratio',
    (1, -1, 0, -2): 'cubic_two',
    (1, -1, -1, -1): 'tribonacci',
    (1, -2, 0, 0): 'two',
    (1, -2, -1, 2): 'two',
    (1, -3, 3, -2): 'two',
    (1, -1, -2, 0): 'two',
    (1, 0, -3, -2): 'two',
}
EXPECTED = {
    'finite_nilpotent': 12,
    'finite_three_cycle': 6,
    'one': 96,
    'square_root_two': 12,
    'cubic_one': 24,
    'golden_ratio': 48,
    'cubic_two': 24,
    'tribonacci': 24,
    'infinite': 42,
}


def main():
    all_three_cycles = set()
    for abc in permutations(range(3)):
        # Periodic sequence ...abcabc...; substituted sequence must be identical
        # with each letter's start position multiplied by 2 mod 3.
        words = [None] * 3
        for j, a in enumerate(abc):
            words[a] = (abc[(2 * j) % 3], abc[(2 * j + 1) % 3])
        all_three_cycles.add(tuple(words))
    assert len(all_three_cycles) == 6
    result = Counter()
    chars = Counter()
    visited, primitive_count, nil_count = 0, 0, 0
    witnesses = {}
    for digits in product(range(3), repeat=6):
        visited += 1
        words = tuple(tuple(digits[2 * i:2 * i + 2]) for i in range(3))
        if not primitive(words):
            continue
        primitive_count += 1
        d = discrepancy(words)
        poly = polynomial(d)
        assert poly == alternate_polynomial(d), (words, poly)
        assert poly in POLY_CLASS, (words, poly)
        chars[poly] += 1
        cls = POLY_CLASS[poly]
        is_three_cycle = words in all_three_cycles
        if cls == 'zero':
            assert mul(mul(d, d), d) == ((0, 0, 0),) * 3
            cat = 'finite_nilpotent'
            nil_count += 1
        elif is_three_cycle:
            assert poly == (1, -2, -1, 2)
            cat = 'finite_three_cycle'
        elif cls == 'two':
            cat = 'infinite'
        else:
            cat = cls
        result[cat] += 1
        witnesses.setdefault(cat, words)
    assert visited == 729
    assert primitive_count == 288
    assert nil_count == 12
    assert sum(result.values()) == 288
    assert result == EXPECTED, (result, EXPECTED)
    assert sum(result[c] for c in ('finite_nilpotent', 'finite_three_cycle', 'one')) == 114
    assert len(chars) == 16
    # Two independent ways to tally the total, via primitive and charpolys.
    assert sum(chars.values()) == primitive_count
    print('EXHAUSTIVE EXACT CENSUS PASSED')
    print('Visited:', visited, 'primitive:', primitive_count)
    for k in EXPECTED:
        print(k, result[k], 'witness=', witnesses[k])
    print('Exact characteristic-polynomial distribution:')
    for poly, count in sorted(chars.items()):
        print(' ', poly, count)
    print('Each primitive substitution tested through full 3x3 integer matrices;')
    print('independent determinant interpolation agreed at every instance.')


if __name__ == '__main__':
    main()
