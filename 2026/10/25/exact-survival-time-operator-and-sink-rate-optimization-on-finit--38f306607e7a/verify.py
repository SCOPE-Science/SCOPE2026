"""Independent finite-matrix checks for the boundary-sink finite-path theorem.
Run with Python 3, NumPy, and SciPy: python verify.py.
Numerical checks supplement the all-dimensional Lyapunov proof.
"""

import numpy as np
from scipy.linalg import solve_continuous_lyapunov, expm
from scipy.integrate import quad


def generator(n, hopping, loss):
    a = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    q = 1j * hopping * a
    q[0, 0] = -loss / 2
    return q


def witness(n, hopping, loss):
    q = np.empty((n, n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            if (j - i) % 2 == 0:
                z = (n - j) * ((i + 1) / loss + i * loss / (4 * hopping**2))
            else:
                z = -1j * (n - j) / (2 * hopping)
            q[i, j] = z
            q[j, i] = np.conj(z)
    return q


def time_formula(n, m, hopping, loss):
    return (n + 1 - m) * (m / loss + (m - 1) * loss / (4 * hopping**2))


def test():
    count = 0
    for n in range(2, 16):
        for hopping, loss in ((1.0, 0.35), (0.6, 1.6), (1.7, 3.4), (1.1, 11.0)):
            l = generator(n, hopping, loss)
            w = witness(n, hopping, loss)
            assert np.max(np.abs(l.conj().T @ w + w @ l + np.eye(n))) < 2e-11
            count += 1
            assert np.max(np.abs(w - w.conj().T)) < 1e-12
            count += 1
            eig = np.linalg.eigvals(l)
            assert np.max(np.real(eig)) < 1e-8
            count += 1
            independent = solve_continuous_lyapunov(l.conj().T, -np.eye(n))
            assert np.max(np.abs(w - independent)) < 2e-8
            count += 1
            for m in range(1, n + 1):
                assert abs(w[m - 1, m - 1] - time_formula(n, m, hopping, loss)) < 2e-11
                count += 1
    # Independent quadratures of survival from propagator in four instances.
    for n, m, hopping, loss in ((2, 1, 1., 1.), (3, 2, 1., 2.), (5, 3, 1.3, 1.6), (6, 5, 1.5, 1.1)):
        l = generator(n, hopping, loss)
        initial = np.eye(n)[:, m - 1]
        decay = -max(np.real(np.linalg.eigvals(l)))
        horizon = max(120., 28. / decay)
        # Integrate survivor norm; exponential matrix is evaluated independently of Lyapunov solve.
        def surv(t):
            w = expm(l * t) @ initial
            return np.vdot(w, w).real
        integral, error = quad(surv, 0., horizon, epsabs=5e-8, limit=200)
        assert abs(integral - time_formula(n, m, hopping, loss)) < 1.5e-5
        count += 1
    # At any fixed injection index, the unique minimum is independent of chain extension.
    for m in range(2, 13):
        for n in range(m, 18):
            hopping = 1.3
            critical = 2 * hopping * np.sqrt(m / (m - 1))
            expected = (n + 1 - m) * np.sqrt(m * (m - 1)) / hopping
            assert abs(time_formula(n, m, hopping, critical) - expected) < 2e-12
            count += 1
            for scale in (0.4, 0.9, 1.1, 2.1):
                assert time_formula(n, m, hopping, scale * critical) > expected
                count += 1
    print('PASS:', count, 'numerical assertions')


if __name__ == '__main__':
    test()
