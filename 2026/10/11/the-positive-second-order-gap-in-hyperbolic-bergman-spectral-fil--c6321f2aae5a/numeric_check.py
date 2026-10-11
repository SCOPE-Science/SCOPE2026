"""Finite-N consistency checks for the hyperbolic Bergman filling gap.

Requires numpy and scipy. These quadrature computations are not an
infinite-N proof; the accompanying text provides the analytic argument.
"""
from math import comb, exp, log
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma, gammaln, roots_jacobi


def run(d: int, alpha: float, p: float, N: int, nodes: int = 120) -> None:
    A = exp(gammaln(alpha + d + 1) - gammaln(alpha + 1) - gammaln(d + 1))
    filling, _ = quad(
        lambda s: np.arcsinh((s / A) ** (1 / (2 * d))) ** p,
        0.0, float(N), epsabs=1e-8, limit=400,
    )
    spectral = 0.0
    remaining, degree = N, 0
    while remaining:
        shell = min(remaining, comb(degree + d - 1, d - 1))
        # Gauss--Jacobi quadrature for the Beta(degree+d, alpha+1) law.
        x, weights = roots_jacobi(nodes, alpha, degree + d - 1)
        t = (x + 1) / 2
        cost = np.arctanh(np.sqrt(t)) ** p
        spectral += shell * np.dot(weights, cost) / np.sum(weights)
        remaining -= shell
        degree += 1
    predicted = p / (2 * d) ** p * (
        gammaln(alpha + d + 1) - gammaln(alpha + 1) - d * digamma(alpha + 1)
    )
    observed = (spectral - filling) / (N * log(N) ** (p - 1))
    print(
        f"d={d}, alpha={alpha:g}, p={p:g}, N={N}: "
        f"scaled finite-N gap={observed:.7f}; predicted limit={predicted:.7f}"
    )


if __name__ == "__main__":
    run(2, 0.0, 1.0, 2016)
    run(2, 1.5, 2.0, 2016)
