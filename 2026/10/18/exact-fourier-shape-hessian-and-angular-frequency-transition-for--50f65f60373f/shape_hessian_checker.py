"""Independent finite-matrix checks for the Gaussian concentration shape Hessian.

Requires Python 3, numpy and scipy.  These finite tests do not establish
statements about the full Bargmann--Fock space or asymptotic limits.
"""
import math
import numpy as np
from scipy.special import gammainc, gamma, gammaln, logsumexp


def phi(radius, mode):
    if mode < 2:
        return 0.0
    j = np.arange(1, mode + 1, dtype=float)
    logs = j * np.log(radius) - gammaln(j + 1)
    return float(1 - np.exp(logs[-1] - logsumexp(logs)))


def top_eigenvalue(radius, epsilon, components, dimension=13, angles=1024):
    """Polar quadrature, then a separate eigensolver; no Hessian formulas used."""
    theta = 2 * np.pi * np.arange(angles) / angles
    heights = radius + epsilon * sum(coef * np.cos(k * theta)
                                     for k, coef in components)
    assert np.min(heights) > 0
    orders = np.arange(dimension)
    phase = np.exp(1j * np.outer(theta, orders))
    result = np.zeros((dimension, dimension), dtype=complex)
    for j in orders:
        for k in orders:
            shape = 1 + (j + k) / 2
            radial = gamma(shape) * gammainc(shape, heights)
            result[j, k] = np.mean(radial * phase[:, k] * phase[:, j].conj()) / math.sqrt(
                math.factorial(int(j)) * math.factorial(int(k))
            )
    result = (result + result.conj().T) / 2
    return float(np.linalg.eigvalsh(result)[-1])


def check():
    pure_checks = 0
    for radius in (0.4, 1.0, 3.0):
        for k in (1, 2, 3, 5):
            # A single real cosine has two Fourier coefficients of size 1/2.
            theoretical = np.exp(-radius) * phi(radius, k) / 4
            epsilon = 0.016
            observed = (1 - np.exp(-radius)
                        - top_eigenvalue(radius, epsilon, [(k, 1)])) / epsilon**2
            if k == 1:
                assert abs(observed) < 8e-5, (radius, k, observed)
            else:
                assert abs(observed - theoretical) < 7e-5 + 0.005*theoretical, (radius, k, observed, theoretical)
            pure_checks += 1
    mixed_checks = 0
    for radius, components in [
        (0.8, [(1, 0.3), (2, 0.7), (4, -0.2)]),
        (2.5, [(2, 0.35), (3, -0.6), (5, 0.2)]),
    ]:
        # Spectrally separated cosines have no cross term in the quadratic form.
        theoretical = np.exp(-radius) * sum(phi(radius, k)*coef**2/4 for k,coef in components)
        eps = 0.012
        observed = (1-np.exp(-radius)-top_eigenvalue(radius, eps, components)) / eps**2
        assert abs(observed-theoretical) < 6e-5 + 0.007*theoretical, (radius,observed,theoretical)
        mixed_checks += 1
    asymptotic_checks = 0
    for radius in (50, 200, 500):
        for alpha in (0.2, 0.6, 1.0, 1.4):
            mode = max(2, int(round(radius*alpha)))
            actual = phi(radius, mode)
            expected = min(1.0, alpha)
            # Slow boundary convergence at alpha=1 is expected and measured.
            tolerance = 0.2 if alpha == 1.0 else (0.09 if alpha == 0.6 else 0.045)
            assert abs(actual-expected) < tolerance, (radius,alpha,actual,expected)
            asymptotic_checks += 1
    for radius in (0.05, 0.8, 3.0, 25.0):
        vals = [phi(radius, mode) for mode in range(1,31)]
        assert all(vals[k+1] > vals[k] for k in range(1,len(vals)-1)
                   if vals[k+1] < 1 - 1e-10)
    print(f'PASS: {pure_checks} pure-mode, {mixed_checks} mixed-mode, '
          f'{asymptotic_checks} crossover comparisons, four monotonicity checks.')
    print('At R=1, cos(2 theta): predicted deficit / epsilon^2 =',
          np.exp(-1)*phi(1,2)/4)


if __name__ == '__main__':
    check()
