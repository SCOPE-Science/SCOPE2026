#!/usr/bin/env python3
"""Exact small-instance checks for finite-product interaction projections."""
from itertools import product
from math import comb, prod, exp, pi, sqrt
from fractions import Fraction


def coeff(z, d):
    e = [1] + [0] * d
    for t in z:
        for j in range(d, 0, -1):
            e[j] += t * e[j - 1]
    return sum(e)


def formula(ns, d):
    M = prod(ns)
    total = 0
    for matching in product((False, True), repeat=len(ns)):
        z = [n - 1 if match else -1 for n, match in zip(ns, matching)]
        multiplicity = prod(n - 1 for n, match in zip(ns, matching) if not match)
        total += multiplicity * abs(coeff(z, d))
    return Fraction(total, M)


def check(ns, d):
    coords = list(product(*(range(n) for n in ns)))
    M = len(coords)
    mat = [[coeff([n - 1 if a == b else -1 for n, a, b in zip(ns, x, y)], d)
            for y in coords] for x in coords]
    assert len({sum(abs(v) for v in row) for row in mat}) == 1
    assert Fraction(sum(abs(v) for v in mat[0]), M) == formula(ns, d)
    assert all(mat[i][j] == mat[j][i] for i in range(M) for j in range(M))
    for i in range(M):
        for j in range(M):
            assert sum(mat[i][k] * mat[k][j] for k in range(M)) == M * mat[i][j]
    dim = sum(prod(ns[i] - 1 for i in S) for j in range(d + 1)
              for S in __import__('itertools').combinations(range(len(ns)), j))
    assert sum(mat[i][i] for i in range(M)) == M * dim
    return M * M + M * M * M


def uniform_formula(q, r, d):
    M = q ** r
    s = 0
    for h in range(r + 1):
        s += comb(r, h) * (q - 1) ** (r - h) * abs(coeff([q - 1] * h + [-1] * (r - h), d))
    return Fraction(s, M)


def main():
    cases = [((2, 2, 2, 2), 2), ((2, 2, 2, 3), 2),
             ((2, 2, 3, 3), 2), ((2, 3, 3, 3), 2),
             ((3, 3, 3, 3), 2), ((2, 2, 2, 2, 2), 2),
             ((2, 2, 2, 2, 2), 3), ((2, 2, 2, 2, 2, 2), 2)]
    cells = 0
    for ns, d in cases:
        cells += check(ns, d)
    assert formula((2, 2, 2, 2), 2) == Fraction(9, 4)
    assert formula((3, 3, 3, 3), 2) == Fraction(91, 27)
    for q in (2, 3, 4):
        for r in range(4, 9):
            for d in range(2, r-1):
                assert uniform_formula(q, r, d) == formula((q,)*r, d)
    for q in (2, 3):
        approx = float(uniform_formula(q, 180, 2)) / 180
        target = (q - 1) * sqrt(2 / pi) * exp(-0.5)
        assert abs(approx - target) < 0.035
    print('VERIFY_OK', len(cases), 'exact matrix cases;', cells, 'matrix operations; closed-form and limit sanity checks')

if __name__ == '__main__':
    main()
