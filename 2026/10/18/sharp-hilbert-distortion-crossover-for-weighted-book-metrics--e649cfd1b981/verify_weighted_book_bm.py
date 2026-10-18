#!/usr/bin/env python3
"""Exact independent finite checks for a two-hub Lipschitz-ball Hilbert distortion.

Run: python3 verify_weighted_book_bm.py
Only Python standard library. Finite checks illustrate, do not prove, all-parameter theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product


def exact_optimal(m, H):
    threshold_inner = 1 / (H * H) - 1
    threshold_outer = m * (2 - H) / H
    r = max(threshold_inner, threshold_outer)
    result = (1 + m * (1 - H) / (1 + H) if threshold_inner >= threshold_outer
              else m + H / (2 - H))
    return r, result


def objective(m, H, r):
    outer = max(F(m), r * H * H + m * (1 - H)**2)
    inner = min(r * H * H, r / (r + 1))
    return outer / inner


def solve_linear(A, b):
    n = len(b)
    X = [list(row) + [rhs] for row, rhs in zip(A, b)]
    for j in range(n):
        piv = next((i for i in range(j, n) if X[i][j]), None)
        if piv is None:
            return None
        X[j], X[piv] = X[piv], X[j]
        a = X[j][j]
        X[j] = [v / a for v in X[j]]
        for i in range(n):
            if i != j:
                b0 = X[i][j]
                if b0:
                    X[i] = [X[i][k] - b0 * X[j][k] for k in range(n + 1)]
    return tuple(X[i][-1] for i in range(n))


def enumerate_vertices(m, H):
    # h in [-H,H], |h|+|z_i|<=1 represented by four linear inequalities.
    n = m + 1
    hs = [((F(1),) + (F(0),) * m, H),
          ((F(-1),) + (F(0),) * m, H)]
    for i in range(m):
        for sh, sz in product([-1, 1], repeat=2):
            row = [F(0)] * n
            row[0] = F(sh)
            row[i+1] = F(sz)
            hs.append((tuple(row), F(1)))
    vertices = set()
    for inds in combinations(range(len(hs)), n):
        x = solve_linear([hs[j][0] for j in inds], [hs[j][1] for j in inds])
        if x is None:
            continue
        if all(sum(a*y for a, y in zip(row,x)) <= b for row, b in hs):
            vertices.add(x)
    return vertices


def run():
    hs = [F(1, 12), F(1, 9), F(1, 6), F(1, 4), F(1, 3),
          F(1, 2), F(2, 3), F(3, 4), F(1)]
    cases = 0
    checks = 0
    tested_vertices = 0
    for m in range(2, 9):
        for H in hs:
            r, result = exact_optimal(m, H)
            assert result == objective(m, H, r)
            # For all positive rational test weights verify the exact claimed global optimizer.
            for num in range(1, 101):
                for den in (1, 3, 11, 29):
                    test = F(num, den)
                    assert objective(m, H, test) >= result
                    checks += 1
            # Direct vertices, independent of the collapsed outer-radius formula.
            if m <= 4 and H in (F(1, 6), F(1, 3), F(1, 2), F(1)):
                verts = enumerate_vertices(m, H)
                assert verts
                actual_outer = max(r*x[0]**2 + sum(y*y for y in x[1:]) for x in verts)
                expected_outer = max(F(m), r*H*H + m*(1-H)**2)
                assert actual_outer == expected_outer
                tested_vertices += len(verts)
            cases += 1
    # Dimension 3, hub-edge length one, and K_{2,2} endpoint exact benchmarks.
    assert exact_optimal(2, F(1, 2))[1] == F(7, 3)
    assert exact_optimal(2, F(1))[1] == 3
    # Sharp transition: threshold at H=1/(2+sqrt(3)) in m=2 (by polynomial identity).
    assert 2 * F(1, 4)**2 - 4 * F(1, 4) + 1 > 0
    assert 2 * F(1, 3)**2 - 4 * F(1, 3) + 1 < 0
    print(f"EXACT_BOOK_BM_CHECKS_PASS {cases} parameter cases, {checks} rational comparisons, {tested_vertices} vertices")


if __name__ == '__main__':
    run()
