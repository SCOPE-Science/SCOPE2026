#!/usr/bin/env python3
"""Exact standalone checks for hyperplane cuts of 4-dimensional cyclic polytopes.

Only standard-library Python is required. No numerical geometry or floating-point
arithmetic is used; finite tests complement the general counting proof.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction
import random


def gale_facets(n):
    """Facets from Gale evenness (not from the disjoint-cycle-edge rule)."""
    out = []
    for f in combinations(range(n), 4):
        outside = [j for j in range(n) if j not in f]
        if all(sum(a < k < b for k in f) % 2 == 0
               for a, b in combinations(outside, 2)):
            out.append(f)
    return out


def cycle_facets(n):
    edges = [(i, (i + 1) % n) for i in range(n)]
    return sorted({tuple(sorted(set(a + b))) for a, b in combinations(edges, 2)
                   if len(set(a + b)) == 4})


def counts(word, facets):
    facet_size_hist = [0, 0, 0, 0, 0]
    for face in facets:
        k = sum(word[i] for i in face)
        if k in (1, 2, 3):
            facet_size_hist[k] += 1
    p = sum(word)
    return (p * (len(word) - p), sum(facet_size_hist),
            facet_size_hist[1] + facet_size_hist[3], facet_size_hist[2])


def runs_stats(word):
    n = len(word)
    trans = sum(word[i] != word[(i + 1) % n] for i in range(n))
    r = trans // 2
    singleton = sum(word[(i - 1) % n] != word[i] != word[(i + 1) % n]
                    for i in range(n))
    return trans, r, singleton


def integer_det(matrix):
    """Integer determinant by fraction-free Gaussian elimination."""
    a = [row[:] for row in matrix]
    m = len(a)
    sgn, denom = 1, 1
    for k in range(m - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, m) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sgn = -sgn
        pivot = a[k][k]
        for i in range(k + 1, m):
            for j in range(k + 1, m):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % denom == 0
                a[i][j] = num // denom
        for i in range(k + 1, m):
            a[i][k] = 0
        denom = pivot
    return sgn * a[-1][-1]


def geometric_facets(n):
    """Facet test directly on rational moment-curve vertices."""
    v = [[1, t, t**2, t**3, t**4] for t in range(n)]
    out = []
    for fs in combinations(range(n), 4):
        remaining = (j for j in range(n) if j not in fs)
        signs = set()
        for j in remaining:
            d = integer_det([v[i] for i in fs] + [v[j]])
            assert d != 0
            signs.add(d > 0)
            if len(signs) > 1:
                break
        if len(signs) == 1:
            out.append(fs)
    return out


def realize(word):
    """Realize a word with an affine hyperplane polynomial of degree <=4."""
    n = len(word)
    flips = [Fraction(2 * i + 1, 2) for i in range(n - 1)
             if word[i] != word[i + 1]]
    assert len(flips) <= 4
    def q(t):
        v = Fraction(1)
        for root in flips:
            v *= Fraction(t) - root
        return v
    global_sign = (1 if (q(0) > 0) == bool(word[0]) else -1)
    assert all((global_sign * q(i) > 0) == bool(word[i])
               for i in range(n))


def check():
    word_checks = 0
    orientation_checks = 0
    for n in range(5, 15):
        gf = gale_facets(n)
        cf = cycle_facets(n)
        assert gf == cf, (n, 'Gale != cyclic disjoint-edge facets')
        assert len(gf) == n * (n - 3) // 2
        if n <= 10:
            assert gf == geometric_facets(n)
            orientation_checks += comb(n, 4) * (n - 4)
        best = -1
        maxima = []
        for word in product((0, 1), repeat=n):
            trans, r, singleton = runs_stats(word)
            if trans > 4 or r == 0:
                continue
            p = sum(word)
            sec_v, faces, tri, quad = counts(word, gf)
            assert faces == p * (n - p) + r * n - r * r - 5 * r + singleton
            assert (3 * tri + 4 * quad) % 2 == 0
            if n <= 10:
                realize(word)
            if faces > best:
                best, maxima = faces, [(word, sec_v, tri, quad, r, singleton)]
            elif faces == best:
                maxima.append((word, sec_v, tri, quad, r, singleton))
            word_checks += 1
        expected = 5 if n == 5 else n * n // 4 + 2 * n - 12
        assert best == expected, (n, best, expected)
        if n >= 7:
            p = n // 2
            q = n - p
            for word, sec_v, tri, quad, r, singleton in maxima:
                assert r == 2 and singleton == 2
                assert sum(word) in (p, q)
                assert (sec_v, tri, quad) == (p * q, 4 * n - 20,
                                                  p * q - 2 * n + 8)
            # Explicit sign pattern attains the bound.
            w = (0,) * (p - 1) + (1, 0) + (1,) * (q - 1)
            assert len(w) == n and counts(w, gf)[1] == expected
            realize(w)
    # Additional reproducible larger-parameter direct counting tests.
    rand = random.Random(20261016)
    random_checks = 0
    for n in (16, 19, 23, 28):
        facets = cycle_facets(n)
        for _ in range(220):
            a = rand.randint(1, n - 1)
            b = rand.randint(1, n - a)
            c = rand.randint(1, n - a - b) if n - a - b > 0 else 0
            d = n - a - b - c
            if min(a, b, c, d) <= 0:
                continue
            word = (0,) * a + (1,) * b + (0,) * c + (1,) * d
            _, r, singleton = runs_stats(word)
            p = sum(word)
            assert r == 2
            assert counts(word, facets)[1] == p * (n - p) + r * n - r * r - 5 * r + singleton
            random_checks += 1
    print('CYCLIC4_SECTION_FACETS_OK',
          f'exact_Gale_vs_cycle_n=5..14',
          f'exhaustive_admissible_words={word_checks}',
          f'moment_curve_determinants={orientation_checks}',
          f'larger_direct_counts={random_checks}')


if __name__ == '__main__':
    check()
