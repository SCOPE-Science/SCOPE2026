"""Deterministic exact-identity and floating-point checks for the VBP shift theorem.

Requires numpy >= 1.24 and scipy >= 1.10. The mathematical proof is analytic;
these finite tests verify implementation and illustrative examples only.
"""
import math
import numpy as np
from numpy.linalg import eigvals, norm
from scipy.linalg import eigh
from scipy.optimize import brentq


def generalized_spectrum(T, W, a):
    B = W @ np.linalg.solve(T, W)
    return eigh(a * np.eye(len(T)) - B, T + a * np.eye(len(T)), eigvals_only=True)


def opt_shift(T, W):
    def f(a):
        eig = generalized_spectrum(T, W, a)
        return float(eig[0] + eig[-1])
    high = 1.0
    while f(high) <= 0:
        high *= 2
        assert high < 1e12
    return brentq(f, 0.0, high, xtol=1e-13)


def full_iteration_spectrum(T, W, a, gamma):
    n = len(T)
    I = np.eye(n)
    A = np.block([[T, -W], [W, T]])
    P = np.block([[T + a * I - gamma * W @ W, -gamma * W @ T], [W, T]])
    return eigvals(np.linalg.solve(P, P - A))


def assert_close(a, b, tol=3e-9):
    assert np.max(np.abs(np.array(a) - np.array(b))) < tol, (a, b)


def check():
    T = np.diag([1.0, 4.0])
    W = np.array([[-2.0, 1.0], [1.0, 3.0]])
    B = W @ np.linalg.solve(T, W)
    assert_close(B, [[4.25, -1.25], [-1.25, 3.25]])
    assert norm(T @ B - B @ T) > 1
    exact_shift = (5 + math.sqrt(673)) / 8
    a = opt_shift(T, W)
    assert_close(a, exact_shift)
    eig = generalized_spectrum(T, W, a)
    assert_close(eig[0] + eig[-1], 0)
    qstar = float(max(abs(eig)))
    assert_close(qstar, math.sqrt((47602 - 1825 * math.sqrt(673)) / 5481))
    print(f'noncommuting alpha*: {a:.12f}; optimal rho: {qstar:.12f}')
    for gamma in [1e-6, .3, 2.0]:
        all_eig = sorted(full_iteration_spectrum(T, W, a, gamma).real)
        assert_close(all_eig, [eig[0], 0, 0, eig[-1]], 3e-8)
        print(f'  gamma={gamma:g}: full 4x4 eigenvalues verified')
    ac = .5 * max(np.linalg.eigvalsh(B - T))
    assert_close(ac, 1.8042476415070754)
    assert max(abs(generalized_spectrum(T, W, ac))) > 1 - 1e-10
    assert max(abs(generalized_spectrum(T, W, a * .7))) > qstar
    assert max(abs(generalized_spectrum(T, W, a * 1.3))) > qstar

    T = np.eye(2)
    W = np.diag([-4., 4.])
    a = opt_shift(T, W)
    assert_close(a, 16.0)
    assert_close(generalized_spectrum(T, W, a), [0., 0.])
    gamma = 1e-6
    a_fro = gamma * np.sum(W * W) / 2
    growth = max(abs(generalized_spectrum(T, W, a_fro)))
    assert growth > 15.9
    print(f'commuting exact shift={a:g}, rho=0; Frobenius shift={a_fro:g}, rho={growth:.8f}')
    for gamma in [1e-6, .25, 1.]:
        n = 2
        A = np.block([[T, -W], [W, T]])
        P = np.block([[T + a * np.eye(n) - gamma * W @ W, -gamma * W @ T], [W, T]])
        L = np.linalg.solve(P, P - A)
        assert norm(L @ L) < 1e-9

    rng = np.random.default_rng(19023)
    for n in [2, 3, 4, 6]:
        for trial in range(20):
            X = rng.normal(size=(n, n))
            T = X @ X.T + np.eye(n) * .5
            Y = rng.normal(size=(n, n))
            Z = (Y + Y.T) / 2
            mu = np.linalg.eigvalsh(Z)
            # Force one eigenvalue of each sign; indefinite W is essential.
            W = Z - (mu[0] + mu[-1]) / 2 * np.eye(n)
            a = opt_shift(T, W)
            e = generalized_spectrum(T, W, a)
            assert abs(e[0] + e[-1]) < 5e-10
            q = max(abs(e))
            assert q < 1
            for factor in [.3, .8, 1.2, 3.]:
                e2 = generalized_spectrum(T, W, a * factor)
                assert max(abs(e2)) > q - 5e-9
            gamma = .2
            full = full_iteration_spectrum(T, W, a, gamma)
            assert_close(sorted(full.real), sorted(list(e) + [0.] * n), 2e-7)
            assert max(abs(full.imag)) < 2e-7
    print('80 random definite/indefinite tests: exact spectral reduction and strict optimum OK')
    print('ALL CHECKS PASSED (finite tests are not a proof).')

if __name__ == '__main__':
    check()
