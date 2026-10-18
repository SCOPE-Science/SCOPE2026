"""Independent numerical checks for a curvature-weighted geometric minimax theorem.

Requires Python 3, NumPy and SciPy. Numerical checks are not a proof.
Run: python verify_minimax.py
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import roots_jacobi, gamma
from scipy.optimize import minimize


def check_exact(d):
    assert d >= 3
    beta = Fraction(d - 1, d + 1)
    r = [Fraction(d - j + 1, d - 1) for j in range(1, d + 1)]
    assert r[0] - r[-1] == 1
    lam = [Fraction(1, 2)] + [Fraction(0)] * (d - 2) + [Fraction(1, 2)]
    mean = sum(lam[j] * r[j] for j in range(d))
    var = sum(lam[j] * (r[j] - mean) ** 2 for j in range(d))
    assert var == Fraction(1, 4)
    spherical_var_h = Fraction(2 * (d + 1) ** 2 * (d - 1), d * d * (d + 2))
    pred = (1 - beta) * var * spherical_var_h / 2
    assert pred == Fraction(d * d - 1, 2 * d * d * (d + 2))
    return float(pred)


def quadrature_dual(d, t, nodes=220):
    eta = (d - 3) / 2
    z, w = roots_jacobi(nodes, eta, eta)
    sphere_factor = 2 * math.pi ** ((d - 1) / 2) / gamma((d - 1) / 2)
    a = 1 + t
    q = np.sqrt(1 - z * z + z * z / (a * a))
    ds = sphere_factor * w * a * q
    meridional = 1 / (a * a * q**3)
    azimuthal = 1 / q
    kappa = meridional * azimuthal ** (d - 2)
    beta = (d - 1) / (d + 1)
    values = []
    for j in range(1, d + 1):
        k = d - j
        H = (math.comb(d - 2, k) * azimuthal**k
             if k <= d - 2 else np.zeros_like(z))
        if k >= 1:
            H += math.comb(d - 2, k - 1) * meridional * azimuthal**(k - 1)
        H /= math.comb(d - 1, k)
        weight = kappa ** (1 / (d - 1)) * H
        M = (np.sum(ds * weight**beta)) ** (1 / beta)
        values.append(weight / M)
    V = np.asarray(values)

    def objective(lam):
        return float((np.sum(ds * (lam @ V)**beta)) ** (1 / beta))

    result = minimize(lambda lam: -objective(lam), np.full(d, 1 / d),
                      method="SLSQP", bounds=[(0, 1)] * d,
                      constraints=[{"type": "eq", "fun": lambda lam: sum(lam) - 1}],
                      options={"maxiter": 1000, "ftol": 5e-15})
    assert abs(sum(result.x) - 1) < 1e-8
    assert np.min(result.x) > -1e-8
    score = objective(result.x)
    endpoint = np.zeros(d)
    endpoint[0] = endpoint[-1] = .5
    assert score >= objective(endpoint) - 1e-8
    assert score >= 1 - 1e-8
    return score, result.x


def main():
    for d in (3, 4, 6):
        predicted = check_exact(d)
        ratios = []
        for t in (0.08, 0.04, 0.02):
            q, lam = quadrature_dual(d, t)
            ratio = (q - 1) / t**2
            ratios.append(ratio)
            print("d", d, "t", t, "regret", q, "ratio", ratio,
                  "predicted", predicted, "dual", np.round(lam, 5))
        assert abs(ratios[-1] - predicted) < 0.003
        assert abs(ratios[-1] - predicted) < abs(ratios[0] - predicted)
    print("PASS: exact moment identities and ellipsoid dual quadrature checks")


if __name__ == "__main__":
    main()
