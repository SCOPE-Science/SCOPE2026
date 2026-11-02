"""Reproducibility checks for theta-graph Lipschitz projection constants.

Run: python check_theta_projection.py
Requires Python 3 and scipy for the small unrestricted linear programs.
The unrestricted theorem requires the argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def prescription(p, a, b):
    assert all(isinstance(z, int) and z >= 2 for z in (p, a, b))
    r = F(b, a)
    C = 2 - F(2, a) + r
    h = p - 2 + F(2, a) - p * r
    B = p * (1 + F(a - 2, b))
    H = 3 - F(2, p) - F(2 * (p - 1), a * p)
    J = 2 + F(a - 2, b)
    if h >= 0:
        return C, F(0), "short"
    if H >= J:
        return H, F(1, p), "saturated"
    x = (C - 1) / (B - h)
    return 1 + B * x, x, "balanced"


def column_max(p, a, b, x):
    sizes = [a] * p + [b]
    gamma = [x] * p + [1 - p * x]
    values = []
    for j, length in enumerate(sizes):
        same = abs(1 - (1 - gamma[j]) / length)
        same += (length - 1) * abs((1 - gamma[j]) / length)
        different = sum(sizes[i] * abs(gamma[i]) / length
                        for i in range(p + 1) if i != j)
        values.append(same + different)
    return max(values)


def exact_cases():
    branches = {"short": 0, "balanced": 0, "saturated": 0}
    columns = 0
    for p, a, b in product(range(2, 13), range(2, 26), range(2, 26)):
        value, x, branch = prescription(p, a, b)
        branches[branch] += 1
        assert 0 <= x <= F(1, p)
        assert column_max(p, a, b, x) == value
        # Independent exact evaluation at a full rational mesh in the
        # mathematically sufficient interval, plus endpoints and kink.
        for k in range(13):
            z = F(k, 12 * p)
            assert column_max(p, a, b, z) >= value
            columns += 1
        assert column_max(p, a, b, F(0)) >= value
        assert column_max(p, a, b, F(1, p)) >= value
    return branches, columns


def unrestricted_linear_program(p, a, b):
    """Do not assume any group symmetry in the variables of the LP."""
    import numpy as np
    from scipy.optimize import linprog
    lengths = [a] * p + [b]
    path_of_edge = [i for i, length in enumerate(lengths) for _ in range(length)]
    N = len(path_of_edge)
    W = np.zeros((N, p))
    for i, path in enumerate(path_of_edge):
        if path < p:
            W[i, path] = 1
        else:
            W[i, :] = -1
    # P=W @ U with U @ W=I, and Q=I-P.  Minimize max column 1-norm of Q.
    nb = p * N
    na = N * N
    nv = nb + na + 1
    eq, eqrhs = [], []
    for i in range(p):
        for j in range(p):
            row = np.zeros(nv)
            for e in range(N):
                row[i * N + e] = W[e, j]
            eq.append(row)
            eqrhs.append(float(i == j))
    ub, ubrhs = [], []
    for e in range(N):
        row = np.zeros(nv)
        for s in range(N):
            row[nb + s * N + e] = 1
        row[-1] = -1
        ub.append(row)
        ubrhs.append(0)
        for s in range(N):
            row = np.zeros(nv)
            for i in range(p):
                row[i * N + e] = -W[s, i]
            row[nb + s * N + e] = -1
            ub.append(row)
            ubrhs.append(-float(s == e))
            row = np.zeros(nv)
            for i in range(p):
                row[i * N + e] = W[s, i]
            row[nb + s * N + e] = -1
            ub.append(row)
            ubrhs.append(float(s == e))
    c = np.zeros(nv)
    c[-1] = 1
    bounds = [(None, None)] * nb + [(0, None)] * na + [(0, None)]
    res = linprog(c, A_ub=ub, b_ub=ubrhs, A_eq=eq,
                  b_eq=eqrhs, bounds=bounds, method="highs")
    assert res.success, res.message
    predicted, _, _ = prescription(p, a, b)
    assert abs(res.fun - float(predicted)) < 1e-8, (p, a, b, res.fun, predicted)
    return N


if __name__ == "__main__":
    regimes, mesh_checks = exact_cases()
    examples = [(2, 2, 2), (2, 2, 3), (2, 3, 5), (3, 2, 2),
                (3, 2, 6), (3, 4, 2), (4, 3, 3), (4, 5, 2)]
    n_edges = [unrestricted_linear_program(*case) for case in examples]
    print("CHECK_OK rational_parameter_cases=6336", "mesh_checks=", mesh_checks,
          "regimes=", regimes, "unrestricted_LP_cases=", len(examples),
          "LP_edge_counts=", n_edges)
