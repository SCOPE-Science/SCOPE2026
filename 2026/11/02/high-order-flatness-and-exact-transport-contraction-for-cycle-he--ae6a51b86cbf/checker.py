"""Separate finite checks for exact transport contraction on cycle heat semigroups.

Requires numpy and scipy. This is numerical corroboration, not a proof for all sizes.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog


def laplacian(n):
    A = np.zeros((n, n), dtype=float)
    for j in range(n):
        A[j, j] = 2
        A[j, (j + 1) % n] -= 1
        A[j, (j - 1) % n] -= 1
    return A


def exact_formula(p):
    n = len(p)
    r = (n + 1) // 4
    return sum(abs(p[j] - p[r]) for j in range(n))


def dual_lp(sig):
    """Separate Kantorovich dual LP with one potential pinned to zero."""
    n = len(sig)
    A = []
    b = []
    for j in range(n):
        for a, b_end in ((j, (j + 1) % n), ((j + 1) % n, j)):
            row = np.zeros(n)
            row[a], row[b_end] = 1, -1
            A.append(row)
            b.append(1)
    fixed = np.zeros(n)
    fixed[0] = 1
    ans = linprog(-sig, A_ub=A, b_ub=b, A_eq=[fixed], b_eq=[0.0],
                  bounds=[(None, None)] * n, method="highs")
    assert ans.success, ans.message
    return -ans.fun


# Check dual optimization by an independent linear-program solver.
count = 0
for n in range(3, 31):
    L = laplacian(n)
    for t in (0.005, 0.035, 0.18, 0.65, 1.4):
        p = expm(-t * L)[0]
        assert min(p) >= -5e-12
        r = (n + 1) // 4
        val = exact_formula(p)
        sig = p - np.roll(p, 1)
        got = dual_lp(sig)
        assert abs(got - val) < 3e-6, (n, t, got, val)
        assert -1e-10 < val < 1+1e-10, (n, t, val)
        assert all(p[j - 1] > p[j] - 1e-10 for j in range(1, n // 2 + 1))
        count += 1
print("Separate cycle Kantorovich dual LP comparisons:", count)


# Compute exact Taylor derivatives using integer matrices, without float approximations.
count = 0
for n in range(3, 65):
    L = [[(2 if i == j else 0) - (1 if j == (i + 1) % n else 0)
          - (1 if j == (i - 1) % n else 0) for j in range(n)] for i in range(n)]
    Q = [[-a for a in row] for row in L]
    r, k = (n + 1) // 4, (n + 2) // 4
    eta = (2, 1, 4, 3)[n % 4]
    v = [1] + [0] * (n - 1)
    for order in range(k + 1):
        defect_derivative = (4 * r + 2 - n) * v[r]
        defect_derivative += sum(4 * v[j] for j in range(r + 1, (n - 1) // 2 + 1))
        if n % 2 == 0:
            defect_derivative += 2 * v[n // 2]
        if order < k:
            assert defect_derivative == 0, (n, order, defect_derivative)
        else:
            assert defect_derivative == eta, (n, k, defect_derivative, eta)
        v = [sum(Q[i][j] * v[j] for j in range(n)) for i in range(n)]
        count += 1
print("Exact-integer Taylor checks:", count)

for n in (4, 6, 8, 12, 20, 40):
    t = 4.0 / (2 - 2 * math.cos(2 * math.pi / n))
    # avoid underflow for gigantic t; at n=40 t is moderate but exp is tiny
    if n > 12:
        continue
    p = expm(-t * laplacian(n))[0]
    A = 2 / n * sum(abs(math.cos(2 * math.pi * j / n)
        - math.cos(2 * math.pi * ((n + 1) // 4) / n)) for j in range(n))
    assert abs(exact_formula(p) * math.exp((2-2*math.cos(2*math.pi/n))*t) - A) < 0.02
print("All finite checks passed")
