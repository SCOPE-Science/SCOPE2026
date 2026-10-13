"""Numerical cross-check of exact capture-time theorem for symmetric quantum cone networks.

Run: python verify.py
Requires numpy, scipy.  This is not a proof for arbitrary system size.
"""
import numpy as np
from scipy.linalg import solve, eigvals
from scipy.optimize import brentq


def analytic(n, g, h, eps, kappa, delta):
    detuning = eps - (n - 1) * h
    return ((n + 1) / kappa + (n - 1) / delta +
            (kappa + delta) / (4 * g * g) +
            detuning * detuning / (g * g * (kappa + delta)))


def numerical(n, g, h, eps, kappa, delta, leaf=1):
    d = n + 1
    H = np.zeros((d, d), dtype=complex)
    H[0, 0] = eps
    H[0, 1:] = g
    H[1:, 0] = g
    H[1:, 1:] = h * (np.ones((n, n)) - np.eye(n))
    p0 = np.zeros((d, d), dtype=complex)
    p0[0, 0] = 1
    pleaf = np.eye(d) - p0

    def lindblad(rho):
        diag_leaf = np.diag(np.r_[0, np.diag(rho)[1:]])
        return (-1j * (H @ rho - rho @ H)
                - kappa / 2 * (p0 @ rho + rho @ p0)
                + delta * (diag_leaf - (pleaf @ rho + rho @ pleaf) / 2))

    liouvillian = np.column_stack([
        lindblad(np.eye(d, dtype=complex)[:, [i]] @
                 np.eye(d, dtype=complex)[[j], :]).reshape(-1, order="F")
        for j in range(d) for i in range(d)
    ])
    rho0 = np.zeros((d, d), dtype=complex)
    rho0[leaf, leaf] = 1
    integrated = solve(-liouvillian, rho0.reshape(-1, order="F"))
    accumulated = integrated.reshape((d, d), order="F")
    return float(np.trace(accumulated).real), np.max(eigvals(liouvillian).real)


def main():
    rng = np.random.default_rng(73)
    cases = 0
    worst = 0.0
    max_spectral = -float("inf")
    for n in [2, 3, 4, 5, 7]:
        for trial in range(4):
            g = float(rng.choice([-1, 1]) * rng.uniform(0.45, 1.9))
            h = float(rng.uniform(-1.2, 1.1))
            eps = float(rng.uniform(-2.4, 2.1))
            kappa = float(rng.uniform(0.55, 2.6))
            delta = float(rng.uniform(0.3, 2.2))
            for leaf in sorted(set([1, n])):
                numerical_value, spectral_abscissa = numerical(
                    n, g, h, eps, kappa, delta, leaf
                )
                predicted_value = analytic(n, g, h, eps, kappa, delta)
                error = abs(numerical_value - predicted_value)
                assert error < 8e-9, (n, trial, leaf, error)
                assert spectral_abscissa < -1e-7, (n, trial, spectral_abscissa)
                worst = max(worst, error)
                max_spectral = max(max_spectral, spectral_abscissa)
                cases += 1

    optimizations = 0
    for n in [2, 3, 6, 11]:
        for g, h, kappa in [(0.7, 0.0, 0.9), (-1.2, 0.4, 2.2)]:
            eps = (n - 1) * h
            delta_star = 2 * abs(g) * np.sqrt(n - 1)
            assert abs(analytic(n, g, h, eps, kappa, delta_star) -
                       ((n + 1) / kappa + kappa / (4 * g * g) +
                        np.sqrt(n - 1) / abs(g))) < 1e-10
            for multiplier in [0.65, 0.85, 1.1, 1.4]:
                assert analytic(n, g, h, eps, kappa, delta_star * multiplier) > analytic(
                    n, g, h, eps, kappa, delta_star
                )
            eps_detuned = eps + 0.4
            delta_root = brentq(
                lambda D: 1 / (4 * g * g) - (n - 1) / (D * D) -
                (eps_detuned - (n - 1) * h) ** 2 /
                (g * g * (kappa + D) ** 2),
                0.2 * delta_star, 7 * delta_star,
            )
            assert delta_root > delta_star
            optimizations += 1

    for n in [2, 3, 6, 11]:
        g, h = 0.8, -0.2
        eps = (n - 1) * h
        K = 2 * abs(g) * np.sqrt(n + 1)
        D = 2 * abs(g) * np.sqrt(n - 1)
        expected = (np.sqrt(n + 1) + np.sqrt(n - 1)) / abs(g)
        assert abs(analytic(n, g, h, eps, K, D) - expected) < 1e-10

    print('VERIFY_OK lindblad_inverse_cases=%d optimization_checks=%d max_abs_error=%.3g max_real_eigenvalue=%.3g' %
          (cases, optimizations, worst, max_spectral))


if __name__ == '__main__':
    main()
