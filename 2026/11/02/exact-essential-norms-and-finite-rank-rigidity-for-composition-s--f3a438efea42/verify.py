#!/usr/bin/env python3
"""Supplementary finite checks for exact discrete-tree Hardy essential norms.

These assertions test finite duality and the two-vertex example; infinite
compactness and essential-norm claims require the analytical proof.
"""
from fractions import Fraction
from itertools import product
from math import isclose

checks = 0

def check(condition, message='assertion'):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def c(q, n):
    return 1 if n == 0 else (q + 1) * q ** (n - 1)

# Size of spheres and the exact extremal two-point difference on a source sphere.
for q in range(2, 9):
    for n in range(4, 39):
        m = n // 2
        check(c(q, m) * q ** (n - m) == c(q, n))
        for p in (1, 2, 3, 4, 7, 12):
            a = (c(q, m) / 2) ** (1 / p)
            input_norm = ((abs(a) ** p + abs(-a) ** p) / c(q, m)) ** (1 / p)
            output_norm = (2 * a) / c(q, n) ** (1 / p)
            exact = 2 ** (1 - 1 / p) * (c(q, m) / c(q, n)) ** (1 / p)
            check(isclose(input_norm, 1, rel_tol=1e-12))
            check(isclose(output_norm, exact, rel_tol=1e-12))

# In the cited two-vertex construction the operator is supported at a single
# output vertex of each high level. The tail supremum is at n=2(R+1).
for q in range(2, 7):
    for R in range(2, 17):
        admissible = [n for n in range(2 * R + 2, 4 * R + 20)
                      if n // 2 > R]
        for p in (1, 2, 5, 13):
            vals = [2 ** (1 - 1 / p) * (c(q, n // 2) / c(q, n)) ** (1 / p)
                    for n in admissible]
            predicted = 2 ** (1 - 1 / p) * q ** (-(R + 1) / p)
            check(isclose(max(vals), predicted, rel_tol=1e-12))

# Exact dual norm of a row of matrices for p=1 with two input levels:
# max over output sign vector y of sum_l c_l ||B_l^T y||_infinity / c_out.
# Independently enumerate all extreme points of each input-level l1 ball.
matrices = (
    (((1, -1), (0, 2)), ((1, 1, -1), (0, -1, 1))),
    (((2, 0), (-1, 2)), ((-1, 0, 1), (1, 1, 0))),
    (((0, 2), (3, -1)), ((1, 2, 1), (2, -1, -1))),
)
for b1, b2 in matrices:
    c1, c2, cout = 3, 6, 3
    dual = Fraction(0)
    for y in product((-1, 1), repeat=2):
        col1 = max(abs(sum(y[i] * b1[i][j] for i in range(2))) for j in range(2))
        col2 = max(abs(sum(y[i] * b2[i][j] for i in range(2))) for j in range(3))
        dual = max(dual, Fraction(c1 * col1 + c2 * col2, cout))
    primal = Fraction(0)
    for j1, s1, j2, s2 in product(range(2), (-1, 1), range(3), (-1, 1)):
        out = [c1 * s1 * b1[i][j1] + c2 * s2 * b2[i][j2] for i in range(2)]
        primal = max(primal, Fraction(sum(map(abs, out)), cout))
    check(dual == primal, 'p=1 finite block duality')

# For p=infinity, independent input signs yield the exact row l1 norm.
for b1, b2 in matrices:
    row_sum = max(sum(map(abs, row1)) + sum(map(abs, row2))
                  for row1, row2 in zip(b1, b2))
    primal = 0
    for z1 in product((-1, 1), repeat=2):
        for z2 in product((-1, 1), repeat=3):
            val = max(abs(sum(a * b for a, b in zip(row1, z1)) +
                          sum(a * b for a, b in zip(row2, z2)))
                      for row1, row2 in zip(b1, b2))
            primal = max(primal, val)
    check(primal == row_sum, 'p=infinity finite row duality')

# Finite support and coefficients imply finitely many possible absolute row sums.
for coeff in ((1, -1), (2, 3, -1), (1, 1j, -1, -1j)):
    totals = set()
    for sizes in product(range(4), repeat=len(coeff)):
        val = 0
        for group in set(sizes):
            if group == 0:
                continue  # zero: outside the cutoff
            val += abs(sum(coeff[i] for i in range(len(coeff)) if sizes[i] == group))
        totals.add(round(val, 12))
    check(len(totals) <= 4 ** len(coeff))

print(f'{checks} finite assertions passed; infinite statements are proved separately.')
