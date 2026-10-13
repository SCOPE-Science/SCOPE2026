"""Reproducible checks for the Gaussian randomized-Ritz median theorem.

Requires Python 3.10+ and NumPy. The analytic proof, not this finite
simulation, establishes statements for all dimensions and angles.
"""

import math
import numpy as np


def complex_gaussian(rng, shape):
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / math.sqrt(2)


def nonspectator_root(rng, m, n, theta):
    assert n >= m + 1
    A = np.diag(np.arange(n))
    W = np.zeros((n, m), dtype=complex)
    W[0, 0] = math.cos(theta)
    W[1, 0] = math.sin(theta)
    for j in range(1, m):
        W[j + 1, j] = 1
    Omega = complex_gaussian(rng, (n, m))
    B = Omega.conj().T @ W
    D = Omega.conj().T @ A @ W
    # Linear-algebraic spectral extraction by the quotient of determinants.
    # For the chosen diagonal A, spectator generalized roots are 2,...,m.
    mu = np.linalg.det(np.column_stack((D[:, 0], B[:, 1:]))) / np.linalg.det(B)
    # Independent Cauchy-ratio derivation through the residual vector.
    rho = math.sin(theta)**2
    residual = A @ W[:, 0] - rho * W[:, 0]
    sigma = np.linalg.norm(residual)
    Q = np.linalg.qr(B[:, 1:], mode='complete')[0]
    u = Q[:, -1]
    z0 = np.vdot(u, Omega.conj().T @ W[:, 0])
    z1 = np.vdot(u, Omega.conj().T @ (residual/sigma))
    ratio = rho + sigma*z1/z0
    assert np.allclose(mu, ratio, atol=3e-9, rtol=1e-9)
    # Rank and eigenvalue factorization independent of the spectator roots:
    for lam in range(2, m+1):
        assert abs(np.linalg.det(D - lam*B)) < 1e-7
    return mu


def general_invariant_spectator_check(rng):
    """Arbitrary complex trial vector in a 3-eigenmode reducing complement."""
    for m in (2, 4, 6):
        n = m + 9
        A = np.diag(np.arange(n) * (np.arange(n) + 2) / 3)
        w = np.zeros(n, dtype=complex)
        w[:3] = [0.61, 0.42j, 0.44 * np.exp(0.9j)]
        w /= np.linalg.norm(w)
        W = np.zeros((n, m), dtype=complex)
        W[:, 0] = w
        for j in range(1, m):
            W[j + 2, j] = 1
        rho = np.vdot(w, A @ w).real
        r = A @ w - rho * w
        sigma = np.linalg.norm(r)
        assert abs(np.vdot(w, r)) < 1e-12
        for _ in range(35):
            Omega = complex_gaussian(rng, (n, m))
            B = Omega.conj().T @ W
            D = Omega.conj().T @ A @ W
            mu = np.linalg.det(np.column_stack((D[:, 0], B[:, 1:]))) / np.linalg.det(B)
            Q = np.linalg.qr(B[:, 1:], mode='complete')[0]
            u = Q[:, -1]
            z0 = np.vdot(u, Omega.conj().T @ w)
            z1 = np.vdot(u, Omega.conj().T @ (r / sigma))
            assert np.allclose(mu, rho + sigma*z1/z0, atol=5e-9, rtol=1e-9)
            for j in range(1, m):
                exact = A[j+2, j+2]
                assert abs(np.linalg.det(D - exact*B)) < 1e-6


def check():
    rng = np.random.default_rng(726101)
    for m in (2, 3, 4, 6):
        for theta in (0.12, 0.31, 0.64):
            for n in (m+1, m+7):
                for _ in range(20):
                    nonspectator_root(rng, m, n, theta)
    general_invariant_spectator_check(rng)
    # Independent denominator/numerator circular Gaussians have exact
    # complex-Cauchy tail P(|Z1/Z0| > t) = 1/(1+t*t).
    count = 170000
    z0 = complex_gaussian(rng, count)
    z1 = complex_gaussian(rng, count)
    R = z1 / z0
    tail = np.mean(np.abs(R) > 1)
    assert abs(tail - 0.5) < 0.012, tail
    # Median of 3 Re/Im values separately: the exact one-coordinate second
    # moment is 1/2. Total E|coordinatewise-median(R)|^2=1.
    R3 = (complex_gaussian(rng, (count, 3)) / complex_gaussian(rng, (count, 3)))
    med = np.median(R3.real, axis=1) + 1j * np.median(R3.imag, axis=1)
    squared = np.mean(np.abs(med)**2)
    assert abs(squared - 1) < 0.08, squared
    theta = 0.43
    rho = math.sin(theta)**2
    sigma = math.sin(theta)*math.cos(theta)
    err = np.mean(np.abs(rho + sigma * med)**2)
    truth = math.sin(theta)**2
    assert abs(err - truth) < 0.04, (err, truth)
    # Exact symbolic integration for the median density (Beta function):
    # 3/4 * integral_R x^2/(1+x^2)^(5/2) dx = 1/2.
    integral = (3/4)*math.gamma(1.5)*math.gamma(1.0)/math.gamma(2.5)
    assert abs(integral - 0.5) < 1e-14
    print('VERIFY_OK: 585 compressed-eigenvalue checks; Cauchy tail and 3-median Monte Carlo; beta integral')
    print(f'tail_at_sigma={tail:.5f}, median_squared={squared:.5f}, sample_mse={err:.5f}, exact_mse={truth:.5f}')


if __name__ == '__main__':
    check()
