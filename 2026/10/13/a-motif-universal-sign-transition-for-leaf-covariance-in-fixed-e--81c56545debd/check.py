#!/usr/bin/env python3
"""Reproducible exact checks for fixed-edge random-graph leaf/motif covariances.

Pure Python 3 standard library. Exhaustive enumeration is a finite verification;
all-size claims rely on the analytic conditional-counting argument.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def falling(x, k):
    z = 1
    for i in range(k):
        z *= x - i
    return z


def aut_count(h, motif_edges):
    edges = {tuple(sorted(e)) for e in motif_edges}
    return sum({tuple(sorted((p[u], p[v]))) for u, v in edges} == edges
               for p in permutations(range(h)))


def masks_of_copies(n, h, motif_edges):
    ambient = list(combinations(range(n), 2))
    indexes = {edge: i for i, edge in enumerate(ambient)}
    masks = set()
    for image in permutations(range(n), h):
        mask = 0
        for u, v in motif_edges:
            mask |= 1 << indexes[tuple(sorted((image[u], image[v])))]
        masks.add(mask)
    assert len(masks) == falling(n, h) // aut_count(h, motif_edges)
    return tuple(masks)


def covariance_formula(n, m, h, e, aut):
    N = comb(n, 2)
    B = comb(n - 1, 2)
    if m < e or m > B + 1:
        return Fraction(0)
    mean_leaves = Fraction(n * (n - 1) * comb(B, m - 1), comb(N, m))
    mean_motif = Fraction(falling(n, h), aut) * Fraction(falling(m, e), falling(N, e))
    mean_cond = Fraction(falling(n - 1, h), aut) * Fraction(falling(m - 1, e), falling(B, e))
    return mean_leaves * (mean_cond - mean_motif)


def ratio(n, h, e):
    return Fraction(n - h, n) * Fraction(falling(comb(n, 2), e), falling(comb(n - 1, 2), e))


# All motifs have minimum degree >= 2; vertices are numbered 0,...,h-1.
MOTIFS = {
    'triangle': (3, ((0, 1), (0, 2), (1, 2))),
    '4-cycle': (4, ((0, 1), (1, 2), (2, 3), (3, 0))),
    'diamond': (4, ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3))),
    '4-clique': (4, tuple(combinations(range(4), 2))),
    '5-cycle': (5, ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0))),
    'house': (5, ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4))),
    'bowtie': (5, ((0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)))
}


def enumerate_covariances(n):
    ambient = list(combinations(range(n), 2))
    N = len(ambient)
    incidence = [sum(1 << i for i, (u, v) in enumerate(ambient) if u == w or v == w)
                 for w in range(n)]
    motifs = []
    for title, (h, motif_edges) in MOTIFS.items():
        if h < n:
            e = len(motif_edges)
            aut = aut_count(h, motif_edges)
            masks = masks_of_copies(n, h, motif_edges)
            motifs.append((title, h, e, aut, masks))
    sums = {(title, m): [0, 0, 0, 0] for title, *_ in motifs for m in range(N + 1)}
    for graph in range(1 << N):
        m = graph.bit_count()
        leaves = sum((graph & inc).bit_count() == 1 for inc in incidence)
        for title, h, e, aut, masks in motifs:
            copies = sum((graph & mask) == mask for mask in masks)
            s = sums[(title, m)]
            s[0] += 1
            s[1] += leaves
            s[2] += copies
            s[3] += leaves * copies
    checks = 0
    for title, h, e, aut, masks in motifs:
        for m in range(N + 1):
            count, leaf_sum, copy_sum, product_sum = sums[(title, m)]
            observed = Fraction(product_sum, count) - Fraction(leaf_sum * copy_sum, count ** 2)
            expected = covariance_formula(n, m, h, e, aut)
            assert observed == expected, (title, n, m, observed, expected)
            checks += 1
    return checks


def validate():
    cells = sum(enumerate_covariances(n) for n in (4, 5, 6))
    assert cells >= 100
    grid = 0
    positive_R = 0
    nonpositive_R = 0
    for n in range(4, 201):
        for h in range(3, min(18, n)):
            for e in range(h, min(comb(h, 2), comb(n-1, 2)) + 1):
                R = ratio(n, h, e)
                if R > 1:
                    threshold = e * R / (R - 1)
                    positive_R += 1
                else:
                    threshold = None
                    nonpositive_R += 1
                for m in {e, e + 1, e + 3, comb(n - 1, 2), comb(n - 1, 2) + 1,
                          *(() if threshold is None else (int(threshold), int(threshold) + 1))}:
                    if e <= m <= comb(n - 1, 2) + 1:
                        cov = covariance_formula(n, m, h, e, 1)
                        if threshold is None:
                            assert cov < 0, (n, h, e, m, R, cov)
                        else:
                            assert (cov > 0) == (m > threshold)
                            assert (cov < 0) == (m < threshold)
                            assert (cov == 0) == (m == threshold)
                        grid += 1
    for n in range(5, 1001):
        t = 3 * ratio(n, 3, 3) / (ratio(n, 3, 3) - 1)
        assert n < t < n + 1
        assert covariance_formula(n, n, 3, 3, 6) < 0
        assert covariance_formula(n, n + 1, 3, 3, 6) > 0
    assert ratio(10, 9, 9) < 1
    print('PASS exact complete graph enumeration cells:', cells)
    print('PASS exact sign grid cells:', grid)
    print('PASS R>1 classes and R<=1 classes:', positive_R, nonpositive_R)
    print('PASS triangle threshold: every n=5,...,1000 and n=4 special case')
    print('PASS general motif architecture: triangle, cycles, diamond, clique, house, bowtie')


if __name__ == '__main__':
    validate()
