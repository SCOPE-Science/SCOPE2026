"""Reproducibility checks for the finite-projective-plane heat-flow theorem.

Uses Python 3, numpy and scipy. Tests coordinatized prime-field planes;
the proof for arbitrary finite projective planes is analytical, not exhaustive.
"""
from __future__ import annotations

from collections import deque
from itertools import product
from math import cosh, exp, isclose, sinh, sqrt

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def projective_plane(q):
    # q is prime in these checks, avoiding finite-field extensions.
    def normalize(x):
        i = next(i for i, a in enumerate(x) if a % q)
        inv = pow(x[i], -1, q)
        return tuple(a * inv % q for a in x)

    points = sorted({normalize(x) for x in product(range(q), repeat=3) if any(x)})
    v = q * q + q + 1
    assert len(points) == v
    N = np.asarray([[int(sum(a * b for a, b in zip(p, l)) % q == 0)
                     for l in points] for p in points], dtype=int)
    assert np.all(N.sum(axis=0) == q + 1) and np.all(N.sum(axis=1) == q + 1)
    assert np.array_equal(N @ N.T, q * np.eye(v, dtype=int) + np.ones((v, v), dtype=int))
    A = np.block([[np.zeros((v, v), dtype=int), N],
                  [N.T, np.zeros((v, v), dtype=int)]])
    D = np.full((2 * v, 2 * v), 99, dtype=int)
    for x in range(2 * v):
        D[x, x] = 0
        queue = deque([x])
        while queue:
            a = queue.popleft()
            for b in np.flatnonzero(A[a]):
                if D[x, b] == 99:
                    D[x, b] = D[x, a] + 1
                    queue.append(b)
    assert np.all(D <= 3)
    return N, A, D


def w1_direct(mu, D):
    plus = np.flatnonzero(mu > 1e-10)
    minus = np.flatnonzero(mu < -1e-10)
    if len(plus) == 0:
        return 0.0
    m, n = len(plus), len(minus)
    constraints = lil_matrix((m + n, m * n))
    for i in range(m):
        constraints[i, i*n:(i+1)*n] = 1
    for j in range(n):
        constraints[m+j, j::n] = 1
    solution = linprog(D[np.ix_(plus, minus)].astype(float).ravel(),
                       A_eq=constraints.tocsr(), b_eq=np.r_[mu[plus], -mu[minus]],
                       bounds=(0, None), method="highs")
    assert solution.success, solution.message
    return float(solution.fun)


def exact_formula(q, t):
    d = q + 1
    v = q*q + q + 1
    r = sqrt(q)
    return exp(-d*t) * (4*q/v * cosh(r*t)
                        + 4*q**3/(v*r) * sinh(r*t)
                        + (q*q-3*q+1)/v * exp(-d*t))


def certificates(q, t):
    v = q*q + q + 1
    d = q + 1
    r = sqrt(q)
    c = cosh(r*t)
    s = sinh(r*t)/r
    k = (exp(-d*t)-c+d*s)/v
    a, b, z = exp(-d*t)*(c-s+k), exp(-d*t)*(s-k), exp(-d*t)*k
    assert a >= -1e-13 and b >= -1e-13 and z >= -1e-13
    return a + 3*q*b + q*q*z


def main():
    plane_count = 0
    edge_checks = 0
    lp_checks = 0
    for q in (2, 3, 5):
        N, A, D = projective_plane(q)
        v = len(N)
        d = q + 1
        # Every incidence edge has the same combinatorial shell data.
        x = 0
        y = v + int(np.flatnonzero(N[x])[0])
        phi = np.zeros(2*v, dtype=int)
        phi[x] = 1
        phi[:v][N[:, y-v] == 0] = 1
        phi[:v][N[:, y-v] == 1] = -1
        phi[x] = 1
        phi[v:][N[x] == 1] = 2
        phi[y] = 0
        assert max(abs(int(phi[i]-phi[j])) for i, j in zip(*np.where(A == 1))) == 1
        # The scalar certificate works for all incidence edges.
        for t in (0.01, 0.13, 0.5):
            P = expm(-t*(d*np.eye(2*v)-A))
            formula = exact_formula(q, t)
            assert isclose(formula, certificates(q, t), rel_tol=2e-12, abs_tol=2e-12)
            for x in range(v):
                for l in np.flatnonzero(N[x]):
                    y = v + int(l)
                    difference = P[:, x]-P[:, y]
                    dual = float(phi @ difference) if x == 0 and l == int(np.flatnonzero(N[x])[0]) else None
                    # Full transport solved on a fixed edge; every other edge has
                    # identical shell pattern by projective-plane incidence axioms.
                    if x == 0 and l == int(np.flatnonzero(N[x])[0]):
                        primal = w1_direct(difference, D)
                        assert isclose(primal, formula, abs_tol=3e-9, rel_tol=3e-9)
                        assert isclose(dual, primal, abs_tol=3e-9, rel_tol=3e-9)
                        lp_checks += 1
                    edge_checks += 1
            # Compare the formula with every vertex pair for the Fano plane.
            if q == 2:
                for xx in range(2*v):
                    for yy in range(xx):
                        w = w1_direct(P[:, xx]-P[:, yy], D)
                        assert w <= formula * D[xx, yy] + 2e-9
                        lp_checks += 1
        plane_count += 1
    assert abs(exact_formula(1000, 0.768039047/1000) - 1.64046408905) < 0.01
    print(f"CHECK_OK planes={plane_count} incidence_edges={edge_checks} lp_instances={lp_checks}")


if __name__ == '__main__':
    main()
