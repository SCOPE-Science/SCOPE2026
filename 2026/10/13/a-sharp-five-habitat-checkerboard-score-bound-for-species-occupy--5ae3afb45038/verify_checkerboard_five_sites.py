#!/usr/bin/env python3
"""Exact standard-library certificate for two-site occupancy C-score extremizers.

The input model is binary species-by-habitat incidence with each species
occupying exactly two of m habitats. Species of the same occupancy type may
repeat, and each distinct unordered pair of species contributes
(2-intersection_size)^2 checkerboard units.

This program enumerates the supports of the resulting finite quadratic form
on a real simplex, solves exact stationarity equations on negative-definite
faces, and checks first small integer censuses independently.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import comb


def det_bareiss(M):
    """Exact determinant of an integer matrix; row swaps are tracked."""
    n = len(M)
    if n == 0:
        return 1
    A = [list(map(int, row)) for row in M]
    sign = 1
    d = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if A[r][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numer = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numer % d == 0
                A[i][j] = numer // d
            A[i][k] = 0
        d = pivot
    return sign * A[n - 1][n - 1]


def solve(A, b):
    """Exact Gauss-Jordan solver for nonsingular square systems."""
    n = len(A)
    M = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col]), None)
        if pivot is None:
            return None
        M[col], M[pivot] = M[pivot], M[col]
        t = M[col][col]
        M[col] = [v / t for v in M[col]]
        for r in range(n):
            if r != col and M[r][col]:
                c = M[r][col]
                M[r] = [u - c * v for u, v in zip(M[r], M[col])]
    return [row[-1] for row in M]


def site_pairs(m):
    return tuple(combinations(range(m), 2))


def weighted_form(m):
    E = site_pairs(m)
    W = [[0] * len(E) for _ in E]
    for i, a in enumerate(E):
        for j, b in enumerate(E):
            if i != j:
                W[i][j] = 4 if set(a).isdisjoint(b) else 1
    return E, W


def score(W, x):
    return sum(F(W[i][j]) * x[i] * x[j]
               for i in range(len(x)) for j in range(i + 1, len(x)))


def stationary_faces(m):
    """Enumerate every face with strictly negative tangent Hessian."""
    E, W = weighted_form(m)
    all_candidates = []
    checked = 0
    negative_faces = 0
    for mask in range(1, 1 << len(E)):
        checked += 1
        ids = [i for i in range(len(E)) if mask & (1 << i)]
        n = len(ids)
        B = [[W[i][j] for j in ids] for i in ids]
        H = [[B[i][j] - B[i][-1] - B[-1][j] + B[-1][-1]
              for j in range(n - 1)] for i in range(n - 1)]
        if any((-1) ** k * det_bareiss([row[:k] for row in H[:k]]) <= 0
               for k in range(1, n)):
            continue
        negative_faces += 1
        # Gradient components on this face are all equal.
        # Solve (B_i-B_last)*x=0, sum(x)=1 exactly.
        if n == 1:
            x = [F(1)]
        else:
            A = [[B[i][j] - B[-1][j] for j in range(n)]
                 for i in range(n - 1)] + [[1] * n]
            x = solve(A, [0] * (n - 1) + [1])
            assert x is not None
        if not all(t > 0 for t in x):
            continue
        full = [F(0)] * len(E)
        for i, weight in zip(ids, x):
            full[i] = weight
        val = score(W, full)
        all_candidates.append((tuple(ids), tuple(x), val, tuple(full)))
    return E, W, checked, negative_faces, all_candidates


def exhaustive_integer_check():
    E, W = weighted_form(5)
    expected_max = {2: 4, 3: 9, 4: 17, 5: 27, 6: 39,
                    7: 53, 8: 69, 9: 88, 10: 108, 11: 132}
    all_count = 0
    for n in range(2, 12):
        maximum = -1
        winners = 0
        for seq in combinations_with_replacement(range(10), n):
            all_count += 1
            mult = [0] * 10
            for i in seq:
                mult[i] += 1
            # Direct pairwise checkerboard score from the occupancy-type weights.
            value = sum(W[i][j] * mult[i] * mult[j]
                        for i in range(10) for j in range(i + 1, 10))
            assert value * 11 <= 12 * n * n
            if value > maximum:
                maximum = value
                winners = 1
            elif value == maximum:
                winners += 1
            if n <= 6:
                # Independent formula using the five habitat occupancy totals.
                site_totals = [sum(mult[i] for i, edge in enumerate(E)
                                   if site in edge) for site in range(5)]
                alternative = (4 * n * n + 2 * sum(t * t for t in mult)
                               - 3 * sum(d * d for d in site_totals)) // 2
                assert alternative == value
        assert maximum == expected_max[n], (n, maximum)
        if n == 11:
            assert winners == 10, winners
    return all_count, expected_max


def main():
    expected = {
        3: { (1, F(0)): 3, (2, F(1, 4)): 3, (3, F(1, 3)): 1 },
        4: None,
        5: {
            (1, F(0)): 10,
            (2, F(1, 4)): 30,
            (2, F(1)): 15,
            (3, F(1, 3)): 30,
            (3, F(16, 15)): 30,
            (4, F(3, 8)): 5,
            (4, F(12, 11)): 10,
        },
    }
    expected_maxima = {3: F(1, 3), 4: F(1), 5: F(12, 11)}
    for m in (3, 4, 5):
        E, W, checked, negative_faces, candidates = stationary_faces(m)
        assert checked == 2 ** comb(m, 2) - 1
        histogram = Counter((len(ids), value) for ids, x, value, full in candidates)
        if expected[m] is not None:
            assert dict(histogram) == expected[m], (m, histogram)
        vmax = max(val for ids, x, val, full in candidates)
        assert vmax == expected_maxima[m]
        winners = [(ids, x, full) for ids, x, val, full in candidates if val == vmax]
        assert len(winners) == {3: 1, 4: 3, 5: 10}[m]
        for ids, x, full in winners:
            lam = 2 * vmax
            # Strict slack outside the winning support eliminates all
            # additional flat-face equality configurations.
            grad = [sum(W[i][j] * full[j] for j in range(len(E)))
                    for i in range(len(E))]
            for i in range(len(E)):
                if i in ids:
                    assert grad[i] == lam
                else:
                    assert grad[i] < lam
            if m == 5:
                # One large occupancy type, with three equal types forming
                # a triangle on the complementary three sites.
                assert sorted(x) == [F(2, 11)] * 3 + [F(5, 11)]
                big = ids[x.index(F(5, 11))]
                small = [ids[j] for j, weight in enumerate(x) if weight == F(2, 11)]
                other_sites = set(range(5)) - set(E[big])
                assert {E[j] for j in small} == set(combinations(sorted(other_sites), 2))
        if m == 5:
            assert negative_faces == 130
            assert len(candidates) == 130
        print('sites', m, 'faces_checked', checked,
              'strict_tangent_faces', negative_faces,
              'stationary_positive', len(candidates),
              'continuous_max', vmax, 'maximizer_types', len(winners))
        if m == 5:
            for key, count in sorted(histogram.items()):
                print('face_histogram', key[0], str(key[1]), count)

    checked, maxima = exhaustive_integer_check()
    print('integer_multisets_checked', checked)
    print('integer_maxima', ' '.join(f'{k}:{v}' for k, v in maxima.items()))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
