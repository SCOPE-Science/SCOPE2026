"""Finite numerical cross-checks of the circle quadrature formulas.

Requires Python 3.10+, NumPy and SciPy. Run `python verify.py`.
These checks are not substitutes for the limiting-probability proof.
"""
from math import cos, sin, pi, sqrt
import numpy as np
from scipy.optimize import linprog


def chord_formula(z):
    """Exact finite direction formula evaluated in floating-point arithmetic."""
    z = np.asarray(z, dtype=float)
    m = len(z)
    if m < 3 or np.linalg.matrix_rank(z[1:] - z[0]) < 2:
        raise ValueError('At least three noncollinear nodes are required')
    s = z.sum(axis=0)
    best = 0.0
    for i in range(m):
        for j in range(i):
            direction = z[i] - z[j]
            direction = np.array([-direction[1], direction[0]])
            norm = np.linalg.norm(direction)
            if norm < 1e-12:
                continue
            direction /= norm
            p = z @ direction
            h = np.abs(p - np.median(p)).sum()
            best = max(best, abs(s @ direction) / h)
    return best


def primal_lp(z):
    """Independently minimize the largest deviation in the primal box LP."""
    z = np.asarray(z, dtype=float)
    m = len(z)
    objective = np.r_[np.zeros(m), 1.0]
    eq = np.column_stack((np.vstack((np.ones(m), z.T)), np.zeros(3)))
    rhs = np.r_[0.0, -z.sum(axis=0)]
    upper = np.vstack((np.column_stack((np.eye(m), -np.ones(m))),
                       np.column_stack((-np.eye(m), -np.ones(m)))))
    ans = linprog(objective, A_ub=upper, b_ub=np.zeros(2 * m),
                  A_eq=eq, b_eq=rhs,
                  bounds=[(None, None)] * m + [(0, None)],
                  method='highs')
    assert ans.success, ans.message
    return ans.fun


def test():
    rng = np.random.default_rng(20261026)
    count = 0
    for m in range(3, 20):
        for rep in range(12):
            angles = rng.uniform(0, 2 * pi, size=m)
            z = np.column_stack((np.cos(angles), np.sin(angles)))
            dual = chord_formula(z)
            primal = primal_lp(z)
            assert abs(dual - primal) <= 2e-7 * max(1, dual, primal), (
                m, rep, dual, primal)
            count += 1
    # A regular triangle needs no reweighting.
    tri = np.array([(cos(2 * pi * j / 3), sin(2 * pi * j / 3))
                    for j in range(3)])
    assert chord_formula(tri) < 2e-15
    count += 1
    # Empirical projection L1 normalizers approach 2/pi uniformly on an angular net.
    angles = rng.uniform(0, 2 * pi, size=20000)
    z = np.column_stack((np.cos(angles), np.sin(angles)))
    for angle in np.linspace(0, 2 * pi, 37)[:-1]:
        p = z @ np.array([cos(angle), sin(angle)])
        value = np.abs(p - np.median(p)).mean()
        assert abs(value - 2 / pi) < 0.02
        count += 1
    print(f'PASS: {count} deterministic/seeded finite numerical tests')
    print('Limit theorem is proved analytically; no finite check certifies it.')


if __name__ == '__main__':
    test()
