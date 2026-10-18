"""Optional numerical cross-check of unrestricted projection minima.

Requires numpy and scipy. Run: python verify_lp.py
This checks only the finite cases n=4,5,6; it is not the proof of the theorem.
"""
from itertools import combinations
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def graph(n):
    V = list(combinations(range(n), 2))
    E = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V))
         if len(set(V[i]) & set(V[j])) == 1]
    D = np.zeros((len(V), len(E)), dtype=int)
    for t, (u, v) in enumerate(E):
        D[u, t], D[v, t] = -1, 1
    return D


def min_norm(n, cycle=False):
    D = graph(n)
    v, e = D.shape
    m = v * e
    num = m + e * e + 1
    eq_rows, eq_rhs = [], []
    for a in range(v):
        for b in range(v):
            eq_rows.append({a * e + j: int(D[b, j])
                            for j in range(e) if D[b, j]})
            eq_rhs.append((1 if a == b else 0) - 1 / v)
    for j in range(e):
        eq_rows.append({a * e + j: 1 for a in range(v)})
        eq_rhs.append(0)
    ub_rows, ub_rhs = [], []
    for f in range(e):
        u = int(np.where(D[:, f] == -1)[0][0])
        w = int(np.where(D[:, f] == 1)[0][0])
        for j in range(e):
            z = m + f * e + j
            diag = int(cycle and f == j)
            # The operator being bounded is Q=D^T M or I-Q.
            ub_rows.append({z: -1, u * e + j: 1, w * e + j: -1})
            ub_rhs.append(-diag)
            ub_rows.append({z: -1, u * e + j: -1, w * e + j: 1})
            ub_rhs.append(diag)
    for j in range(e):
        row = {m + f * e + j: 1 for f in range(e)}
        row[num - 1] = -1
        ub_rows.append(row)
        ub_rhs.append(0)

    def sparse(rows):
        A = lil_matrix((len(rows), num))
        for i, row in enumerate(rows):
            for j, val in row.items():
                A[i, j] = val
        return A.tocsr()

    objective = np.zeros(num)
    objective[-1] = 1
    bounds = [(None, None)] * m + [(0, None)] * (e * e + 1)
    result = linprog(objective, A_ub=sparse(ub_rows), b_ub=ub_rhs,
                     A_eq=sparse(eq_rows), b_eq=eq_rhs,
                     bounds=bounds, method='highs',
                     options={'time_limit': 90})
    assert result.success, result.message
    expected = (Fraction(2 * (2 * n - 5), n - 1) if cycle else
                Fraction((n - 2) * (3 * n - 1), n * (n - 1)))
    assert abs(result.fun - float(expected)) < 1e-7, (n, cycle, result.fun)
    return result.fun


if __name__ == '__main__':
    for n in (4, 5, 6):
        a, b = min_norm(n, False), min_norm(n, True)
        print(f'n={n}: unrestricted LP cut={a:.10f}, cycle={b:.10f}, OK')
    print('FINITE_LP_OK')
