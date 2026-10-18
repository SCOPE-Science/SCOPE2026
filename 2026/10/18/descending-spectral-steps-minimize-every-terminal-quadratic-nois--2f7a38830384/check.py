"""Reproduce step-permutation covariance comparisons on positive-definite quadratics.

Run: python check.py
Needs numpy; all comparisons use deterministic random seeds.
The finite checks test formulas, not the proof over arbitrary dimensions.
"""
import itertools
import math
import numpy as np


def final_covariance(H, Q, steps):
    d = H.shape[0]
    ident = np.eye(d)
    C = np.zeros((d, d))
    T = ident.copy()
    for a in reversed(steps):
        C += a * a * (T @ Q @ T.T)
        T = T @ (ident - a * H)
    return C


def spectral_weight(H, exponents):
    eigvals, basis = np.linalg.eigh(H)
    return (basis * (eigvals ** exponents)) @ basis.T


def verify():
    rng = np.random.default_rng(903746)
    assertions = 0
    strict_count = 0
    for d in range(2, 7):
        for trial in range(60):
            X = rng.standard_normal((d, d))
            H = X.T @ X + np.eye(d) * 0.3
            Y = rng.standard_normal((d, d))
            Q = Y.T @ Y + np.eye(d) * 0.2
            W = spectral_weight(H, trial % 4 - 1)
            steps = list(rng.uniform(0.03, 1.65, size=4))
            descending = sorted(steps, reverse=True)
            risk_opt = float(np.trace(W @ final_covariance(H, Q, descending)))
            for p in itertools.permutations(steps):
                risk = float(np.trace(W @ final_covariance(H, Q, p)))
                assert risk >= risk_opt - 2e-8 * (1 + abs(risk_opt))
                assertions += 1
                if tuple(p) != tuple(descending):
                    assert risk > risk_opt + 1e-11 * (1 + abs(risk_opt))
                    strict_count += 1
            a, b = steps[:2]
            suffix = steps[2:]
            Ts = np.eye(d)
            for s in suffix:
                Ts = Ts @ (np.eye(d) - s * H)
            cab = final_covariance(H, Q, [a, b] + suffix)
            cba = final_covariance(H, Q, [b, a] + suffix)
            rhs = a * b * (b - a) * (Ts @ (H @ Q + Q @ H) @ Ts.T)
            np.testing.assert_allclose(cab - cba, rhs, rtol=4e-9, atol=5e-9)
            assertions += 1
            trdifference = float(np.trace(W @ (cab - cba)))
            trrhs = 2 * a * b * (b - a) * float(np.trace(W @ H @ (Ts @ Ts.T) @ Q))
            assert math.isclose(trdifference, trrhs, abs_tol=1e-8, rel_tol=1e-8)
            assertions += 1
    for kappa in [2, 3, 10, 100, 2000]:
        H = np.diag([1.0, float(kappa)])
        Q = np.eye(2)
        cup = final_covariance(H, Q, [1.0, 1.0 / kappa])
        cdown = final_covariance(H, Q, [1.0 / kappa, 1.0])
        np.testing.assert_allclose(cup, np.diag([(1-1/kappa)**2 + 1/kappa**2, 1/kappa**2]), rtol=0, atol=2e-15)
        np.testing.assert_allclose(cdown, np.diag([1, 1+(kappa-1)**2/kappa**2]), rtol=0, atol=2e-15)
        assert math.isclose(np.trace(H @ cup), 1-1/kappa+2/kappa**2, abs_tol=5e-13)
        assert math.isclose(np.trace(H @ cdown), 2*kappa-1+1/kappa, abs_tol=5e-13)
        assertions += 4
    H = np.diag([1., 9.])
    Q = np.array([[1., .8], [.8, 1.]])
    J = H @ Q + Q @ H
    assert np.linalg.eigvalsh(Q)[0] > 0 and np.linalg.eigvalsh(J)[0] < 0
    Csorted = final_covariance(H, Q, [1., 1/9])
    Creverse = final_covariance(H, Q, [1/9, 1.])
    assert np.linalg.eigvalsh(Creverse-Csorted)[0] < 0
    assert np.trace(Csorted) < np.trace(Creverse)
    assert np.trace(H @ Csorted) < np.trace(H @ Creverse)
    assertions += 5
    print(f'PASS: {assertions} formula/risk checks; {strict_count} strict alternative-permutation inequalities')
    print('2D correlated-noise covariance difference eigenvalues:', np.linalg.eigvalsh(Creverse-Csorted))
    print('kappa=10 Euclidean noise risks:',
          float(np.trace(final_covariance(np.diag([1.,10.]), np.eye(2), [1.,.1]))),
          float(np.trace(final_covariance(np.diag([1.,10.]), np.eye(2), [.1,1.]))))


if __name__ == '__main__':
    verify()
