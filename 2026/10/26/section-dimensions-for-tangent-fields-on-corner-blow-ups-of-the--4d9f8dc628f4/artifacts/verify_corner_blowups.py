#!/usr/bin/env python3
"""Exact linear-algebra check for the corner-blow-up tangent-section census.

This verifies the 6-variable constraint matrices over Q, F_2, F_3 and F_5
for every subset of the four corners. The geometric identification of these
constraints with H^0(S, T_S(-E)) is proved in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations

CORNERS = ((0, 0), (0, 1), (1, 0), (1, 1))  # 0 means coordinate 0; 1 means infinity


def rank_q(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0]) if a else 6
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    m, n = len(a), len(a[0]) if a else 6
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] % p:
                z = a[i][c] % p
                a[i] = [(x - z*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def constraint_matrix(points):
    # Variables are (a0,a1,a2,b0,b1,b2) for f(x)d/dx + g(y)d/dy.
    rows = []
    for x, y in points:
        if x == 0:
            rows.append([1, 0, 0, 0, 0, 0])  # f(0)=0
        else:
            rows.append([0, 0, 1, 0, 0, 0])  # f(infinity)=0
        if y == 0:
            rows.append([0, 0, 0, 1, 0, 0])  # g(0)=0
        else:
            rows.append([0, 0, 0, 0, 0, 1])  # g(infinity)=0
        eps_x = 1 if x == 0 else -1
        eps_y = 1 if y == 0 else -1
        # Equality of the two local linear eigenvalues at the blown-up point.
        rows.append([0, eps_x, 0, 0, -eps_y, 0])
    return rows


def expected_dimension(points, characteristic):
    if not points:
        return 6
    xs = {x for x, _ in points}
    ys = {y for _, y in points}
    signs = {1 if x == y else -1 for x, y in points}
    relation_rank = 1 if characteristic == 2 or len(signs) == 1 else 2
    return 6 - len(xs) - len(ys) - relation_rank


def main():
    checked = 0
    for size in range(5):
        for points in combinations(CORNERS, size):
            matrix = constraint_matrix(points)
            ranks = {"Q": rank_q(matrix), "F2": rank_mod(matrix, 2),
                     "F3": rank_mod(matrix, 3), "F5": rank_mod(matrix, 5)}
            dims = {field: 6-rank for field, rank in ranks.items()}
            expected = {"Q": expected_dimension(points, 0),
                        "F2": expected_dimension(points, 2),
                        "F3": expected_dimension(points, 3),
                        "F5": expected_dimension(points, 5)}
            assert dims == expected, (points, dims, expected)
            checked += 1
    assert checked == 16
    print("CHECK_OK: all 16 corner subsets over Q, F2, F3 and F5")


if __name__ == "__main__":
    main()
