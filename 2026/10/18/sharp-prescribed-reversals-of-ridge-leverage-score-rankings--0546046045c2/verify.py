"""Reproduce the ridge-leverage ranking crossover theorem's finite checks.

The algebraic proof for all dimensions appears in RESULT.md. These checks
exercise exact partial fractions and actual real orthonormal-column matrices.
Requires numpy and sympy; run with: python verify.py
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

z = sp.symbols('z')
checks = 0


def make_case(d, roots, eps_override=None):
    """Return exact residues and numeric full-rank matrix realizing roots."""
    global checks
    r = len(d)
    assert len(roots) == r - 1
    assert all(t > 0 for t in roots)
    assert all(d[j] < d[j + 1] for j in range(r - 1))
    P = sp.prod(z - t for t in roots)
    Q = sp.prod(z + a for a in d)
    R = []
    for j in range(r):
        v = sp.simplify(P.subs(z, -d[j]) /
                        sp.prod(d[k] - d[j] for k in range(r) if k != j))
        R.append(v)
    assert sp.factor(sum(R[j] / (z + d[j]) for j in range(r)) - P / Q) == 0
    checks += 1
    assert all(R[j] != 0 for j in range(r))
    assert all(sp.sign(R[j]) == -sp.sign(R[j + 1]) for j in range(r - 1))
    checks += 2
    weight = sum(abs(R[j] / d[j]) for j in range(r))
    eps = sp.Rational(1, 4) / weight if eps_override is None else eps_override
    assert eps > 0 and eps * weight < 1
    plus = [float(sp.sqrt(eps * max(R[j] / d[j], 0))) for j in range(r)]
    minus = [float(sp.sqrt(eps * max(-R[j] / d[j], 0))) for j in range(r)]
    x, y = np.array(plus), np.array(minus)
    assert abs(x @ y) < 1e-13
    M = np.eye(r) - np.outer(x, x) - np.outer(y, y)
    eig, eigvec = np.linalg.eigh(M)
    assert eig.min() > 0.5
    B = (eigvec * np.sqrt(eig)) @ eigvec.T
    U = np.vstack((x, y, B))
    assert np.allclose(U.T @ U, np.eye(r), atol=2e-13)
    checks += 3
    A = U @ np.diag(np.sqrt(np.asarray(d, float)))
    for lam in [0.0, .07, .3, .8, 1.0, 1.4, 2.3, 5.0, 11.0, 30.0, 1000.0] + [float(t) for t in roots]:
        F = A.T @ A + lam * np.eye(r)
        l0 = float(A[0] @ np.linalg.solve(F, A[0]))
        l1 = float(A[1] @ np.linalg.solve(F, A[1]))
        exact = float((eps * P / Q).subs(z, sp.Rational(str(lam))))
        assert abs(l0 - l1 - exact) < 2e-11 * max(1.0, abs(exact)), (d, roots, lam, l0, l1, exact)
        checks += 1
    return P, Q, R, eps, A


# Degree two example with crossings exactly 1 and 4.
P, Q, R, eps, A = make_case([sp.Integer(1), sp.Integer(2), sp.Integer(3)],
                            [sp.Integer(1), sp.Integer(4)],
                            eps_override=sp.Rational(1, 30))
assert P == (z - 4) * (z - 1) or sp.expand(P) == z * z - 5*z + 4
assert R == [5, -18, 14], R
assert eps == sp.Rational(1, 30)
assert abs(A[0] @ A[1]) < 1e-13  # first rows disjoint support
checks += 4

# Several dimensions; prescribed positive crossing parameters vary independently.
for r in range(2, 10):
    d = [sp.Integer(j + 1) for j in range(r)]
    sets = [[sp.Rational(2*j + 1, 3) for j in range(r - 1)],
            [sp.Rational(j + 1, 5) for j in range(r - 1)],
            [sp.Rational(4*j + 7, 2) for j in range(r - 1)]]
    for roots in sets:
        make_case(d, roots)

# Degenerate spectrum groups are just one partial-fraction pole each.
c1, c2, c3 = sp.symbols('c1 c2 c3')
F = c1 / (z + 1) + c2 / (z + 2) + c3 / (z + 2)
assert sp.factor(F - (c1 / (z + 1) + (c2 + c3) / (z + 2))) == 0
checks += 1
print(f'PASS: {checks} exact-algebraic and matrix-resolvent assertions; explicit crossings 1,4.')
