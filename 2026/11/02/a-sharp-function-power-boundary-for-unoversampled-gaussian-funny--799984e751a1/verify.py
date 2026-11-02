"""Reproduce finite-dimensional Gaussian Nyström identities and quadrature checks.

The asymptotic theorem is proved analytically in RESULT.md; this program
checks finite cases and numerical approaches to its explicit constants.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as beta_fn, gamma


def exact_nonzero_eigenvalue(L, q, g):
    numerator = L ** (2 * q) * g[0] ** 2 + np.dot(g[1:], g[1:])
    denominator = L ** (2 * q - 1) * g[0] ** 2 + np.dot(g[1:], g[1:])
    return numerator / denominator


def analytic_constant(m, b):
    return 2 * gamma((m + 1) / 2) * gamma(b + 0.5) / (gamma(m / 2) * gamma(b))


def normalized_expected_excess(m, b, q, L):
    """Stable positive integral for (E[trace error] - m)/L**(b-q+1/2)."""
    a = L ** (q - 0.5)
    def integrand(y):
        # Avoid subtracting two nearly equal floating-point powers.
        missing_fraction = (1 - 1 / L) / (1 + y * y)
        gap = -math.expm1(b * math.log1p(-missing_fraction))
        return gap * (1 + (y / a) ** 2) ** (-(m + 1) / 2)
    piece1 = quad(integrand, 0, 1, epsabs=1e-11, limit=200)[0]
    piece2 = quad(integrand, 1, math.inf, epsabs=1e-11, limit=200)[0]
    return 2 * (piece1 + piece2) / beta_fn(0.5, m / 2)


def run():
    rng = np.random.default_rng(20261025)
    checks = 0
    for m in (1, 2, 3, 5, 8):
        for q in (1, 2, 3):
            for L in (1.1, 2.0, 5.0, 19.0):
                for _ in range(7):
                    g = rng.standard_normal(m + 1)
                    A = np.diag([L] + [1.] * m)
                    Aqg = np.linalg.matrix_power(A, q) @ g
                    den = g @ np.linalg.matrix_power(A, 2*q - 1) @ g
                    approx = np.outer(Aqg, Aqg) / den
                    spectrum = np.linalg.eigvalsh(approx)
                    mu = exact_nonzero_eigenvalue(L, q, g)
                    assert np.allclose(spectrum[-1], mu, atol=1e-10, rtol=1e-10)
                    assert np.max(np.abs(spectrum[:-1])) < 1e-9
                    assert 1.0 - 1e-10 <= mu <= L + 1e-10
                    checks += 1
    for m in (1, 3):
        for q in (1, 2, 3):
            for L in (2., 10., 100.):
                a = L ** (q - 0.5)
                ratio = normalized_expected_excess(m, 1.0, q, L)
                numer = ratio * L ** (1.5 - q)
                if m == 1:
                    exact = (L - 1) / (1 + a)
                else:
                    exact = (L - 1) * (2*a + 1) / (a + 1)**2
                assert abs(numer - exact) <= 3e-8 * max(1, exact), (m, q, L, numer, exact)
                checks += 1
    for m in (1, 3, 5):
        for b in (0.25, 0.5, 0.75, 1.0):
            for q in (1, 2):
                c = analytic_constant(m, b)
                approx = normalized_expected_excess(m, b, q, 1e4)
                assert 0 < approx < c + 1e-7, (m, b, q, approx, c)
                assert abs(approx / c - 1) < 0.065, (m, b, q, approx, c)
                checks += 1
    assert math.isclose(analytic_constant(1, 0.5), 2/math.pi)
    assert math.isclose(analytic_constant(1, 1.0), 1.0)
    assert math.isclose(analytic_constant(3, 0.5), 4/math.pi)
    print(f'VERIFY_OK {checks} independent matrix, exact-integral and asymptotic-constant checks')

if __name__ == '__main__':
    run()
