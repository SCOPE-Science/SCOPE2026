"""Independent exact and floating-point checks for a Lindblad boundary sink on a finite path.

Requires Python 3, sympy, numpy and scipy. Run: python verify_path_absorption.py
"""
from fractions import Fraction
import sympy as sp
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def predicted(n, hop, loss):
    """Integrated survival Gramian in zero-based site indices."""
    out = sp.zeros(n)
    for r in range(n):
        for s in range(n):
            a, b = min(r, s), max(r, s)
            if (r - s) % 2 == 0:
                out[r, s] = (n - b) * ((a + 1) / loss + loss * a / (4 * hop**2))
            else:
                out[r, s] = sp.I * (1 if s > r else -1) * (n - b) / (2 * hop)
    return out


def generator(n, hop, loss):
    h = sp.zeros(n)
    for i in range(n-1):
        h[i, i+1] = h[i+1, i] = hop
    p = sp.zeros(n)
    p[0, 0] = 1
    return -sp.I*h - loss*p/2


def exact_checks():
    count = 0
    for n in range(2, 15):
        for J, gamma in [(sp.Integer(1), sp.Integer(1)),
                         (sp.Rational(3, 2), sp.Rational(7, 3)),
                         (sp.Rational(5, 3), sp.Rational(2, 5))]:
            X = predicted(n, J, gamma)
            K = generator(n, J, gamma)
            residual = K.conjugate().T * X + X * K + sp.eye(n)
            assert residual == sp.zeros(n), (n, J, gamma, residual)
            assert X.conjugate().T == X
            for j in range(n):
                expected = (n - j) * ((j + 1) / gamma + gamma * j / (4 * J**2))
                assert sp.simplify(X[j, j]-expected) == 0
            count += 1
    return count


def independent_numeric_checks():
    count = 0
    for n in range(2, 13):
        for J, gamma in [(0.71, 0.38), (1.3, 3.25), (2.4, 7.1)]:
            H = np.diag(np.full(n - 1, J), 1) + np.diag(np.full(n - 1, J), -1)
            P = np.diag([1] + [0] * (n - 1))
            K = -1j * H - gamma * P / 2
            numerical = solve_continuous_lyapunov(K.conj().T, -np.eye(n))
            exact = np.array(predicted(n, sp.Float(J), sp.Float(gamma)), dtype=complex)
            assert np.allclose(numerical, exact, rtol=1e-9, atol=1e-9), (n, J, gamma)
            assert np.max(np.real(np.linalg.eigvals(K))) < -1e-10
            count += 1
    return count


if __name__ == '__main__':
    print('exact Lyapunov residuals', exact_checks())
    print('independent numerical Lyapunov solves', independent_numeric_checks())
    print('PASS')
