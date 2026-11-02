#!/usr/bin/env python3
"""Independent finite checks for cyclic triple hypergraph lean colorings.

Run: python3 verify.py
No dependencies outside the Python standard library.
"""
from itertools import product


def lean_valid(word):
    n = len(word)
    if len(set(word)) < 2:
        return False
    return all(len({word[i], word[(i + 1) % n], word[(i + 3) % n]}) in (1, 3)
               for i in range(n))


def coloring_valid(word, a, b):
    n = len(word)
    return len(set(word)) >= 2 and all(
        len({word[i], word[(i + a) % n], word[(i + b) % n]}) in (1, 3)
        for i in range(n))


def poly_strip(a):
    a = [v % 3 for v in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_mod(a, b):
    a = poly_strip(a)
    b = poly_strip(b)
    assert b
    inv = pow(b[-1], -1, 3)
    while a and len(a) >= len(b):
        x = a[-1] * inv % 3
        k = len(a) - len(b)
        for j, v in enumerate(b):
            a[k + j] = (a[k + j] - x * v) % 3
        a = poly_strip(a)
    return a


def poly_gcd_degree(n, a, b):
    first = [2] + [0] * (n - 1) + [1]  # t^n - 1
    second = [0] * (b + 1)
    second[0] = second[a] = second[b] = 1
    while second:
        first, second = second, poly_mod(first, second)
    return len(first) - 1


def gf3_rank(mat):
    a = [row[:] for row in mat]
    n = len(a)
    cols = len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, n) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        if a[r][c] == 2:
            a[r] = [(2 * v) % 3 for v in a[r]]
        for i in range(n):
            if i != r and a[i][c]:
                x = a[i][c]
                a[i] = [(u - x * v) % 3 for u, v in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def incidence_rank(n, a, b):
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for d in (0, a, b):
            M[i][(i + d) % n] = 1
    return gf3_rank(M)


def check_general_circulants():
    trials = 0
    for n in range(3, 17):
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                deg = poly_gcd_degree(n, a, b)
                rank = incidence_rank(n, a, b)
                assert deg == n - rank, (n, a, b, deg, rank)
                trials += 1
    print('GCD_RANK_MATCH', trials)
    checks = 0
    for n in range(3, 9):
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                expected = 3 ** poly_gcd_degree(n, a, b) - 3
                actual = sum(coloring_valid(w, a, b)
                             for w in product(range(3), repeat=n))
                assert actual == expected, (n, a, b, expected, actual)
                checks += 1
    print('DIRECT_GENERAL_COLORING_MATCH', checks)


def check_seven():
    n = 7
    edges = {frozenset((i, (i+1)%n, (i+3)%n)) for i in range(n)}
    assert len(edges) == 7
    for i in range(n):
        for j in range(i + 1, n):
            assert sum({i, j} <= e for e in edges) == 1
    counts = {}
    for q in (3, 4, 5):
        ct = 0
        for w in product(range(q), repeat=n):
            if lean_valid(w):
                ct += 1
        counts[q] = ct
    assert counts == {3: 0, 4: 0, 5: 840}, counts
    print('FANO_MINIMUM_COUNTS', counts)


def check_eight_pattern():
    counts = {}
    for n in (8, 9, 10, 16, 24, 40):
        if n <= 10:
            seqs = [w for w in product(range(3), repeat=n) if lean_valid(w)]
        else:
            seqs = []
            for a, b, c in product(range(3), repeat=3):
                w = [a, b, c]
                for i in range(n - 3):
                    w.append((-w[i] - w[i+1]) % 3)
                if lean_valid(w):
                    seqs.append(tuple(w))
        exp = 24 if n % 8 == 0 else 0
        assert len(seqs) == exp, (n, len(seqs), exp)
        for w in seqs:
            mono = sum(len({w[i], w[(i+1)%n], w[(i+3)%n]}) == 1
                       for i in range(n))
            assert mono == n // 4, (n, mono)
        counts[n] = len(seqs)
    print('EIGHT_PERIODIC_TERNARY', counts)


BLOCKS = {
    4: '0123',
    9: '012202311',
    10: '0122321003',
    11: '01220213323',
}


def construct(n):
    assert n >= 8
    base = {0: (8, (4, 4)), 1: (9, (9,)),
            2: (10, (10,)), 3: (11, (11,))}[n % 4]
    w = ''.join(BLOCKS[k] for k in base[1])
    return tuple(map(int, w + BLOCKS[4] * ((n - base[0]) // 4)))


def check_four_color_construction():
    for length, block in BLOCKS.items():
        assert len(block) == length
        assert lean_valid(tuple(map(int, block)))
        assert block[:3] == '012'
    for n in range(8, 301):
        word = construct(n)
        assert len(word) == n
        assert lean_valid(word), n
        assert max(word) < 4
        if n % 8:
            assert len(set(word)) == 4
    print('FOUR_COLOR_CONSTRUCTIONS', 293)


def main():
    check_general_circulants()
    check_seven()
    check_eight_pattern()
    check_four_color_construction()
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
