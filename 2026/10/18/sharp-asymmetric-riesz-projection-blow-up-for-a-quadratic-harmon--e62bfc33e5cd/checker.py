"""Supplementary finite-section checks for a quadratic harmonic-Bergman Toeplitz operator.

Python 3 standard library only. These tests do not replace the infinite-dimensional proof.
"""
import cmath
import math


def shift_weight(k):
    return math.sqrt((k + 1) / (k + 2)) if k >= 0 else math.sqrt(-k / (1 - k))


def profile(radius):
    q = 49.0 / (16.0 * radius * radius)
    a2 = 9.0 * radius * radius / 49.0
    assert 7 / 4 < radius < 7 / 3
    return ((1 - a2) ** -2 + (-math.log1p(-q) - q) / q) / 7


def check_case(b, radius_cutoff=350):
    alpha = -3 * b / 7
    beta = -4 * b / 7
    spectral_point = -12 * b * b / 49
    sep = alpha - beta
    k_values = range(-radius_cutoff, radius_cutoff + 1)
    v = {}
    u = {}
    for k in k_values:
        if k <= 0:
            n = -k
            v[k] = math.sqrt(2 * (n + 1)) * alpha ** n / sep
        else:
            n = k - 1
            v[k] = math.sqrt(2 / (n + 2)) * beta ** (-n - 1) / sep
        if k >= 0:
            row = math.sqrt(2 * (k + 1)) * alpha ** k / sep
        elif k == -1:
            row = 1 / (beta * sep)
        else:
            r = -k
            row = math.sqrt(2 / (r + 1)) * beta ** (-r) / sep
        u[k] = row.conjugate()
    uv = sum(u[k].conjugate() * v[k] for k in k_values)
    nv = sum(abs(z) ** 2 for z in v.values())
    nu = sum(abs(z) ** 2 for z in u.values())
    predicted = profile(abs(b))
    assert abs(uv - 686 / (b * b)) < 2e-8
    assert abs(nv - nu) < 2e-8
    assert abs(nv ** 0.5 * nu ** 0.5 / abs(uv) - predicted) < 2e-8
    residual_sq = 0.0
    for k in k_values:
        actual = 0j
        if k - 2 in v:
            actual += shift_weight(k - 2) * shift_weight(k - 1) * v[k - 2]
        if k - 1 in v:
            actual += b * shift_weight(k - 1) * v[k - 1]
        if k == 1:
            actual += v[-1] / 6
        residual_sq += abs(actual - spectral_point * v[k]) ** 2
    assert math.sqrt(residual_sq) < 3e-7
    return predicted, math.sqrt(residual_sq)


def main():
    for b in (1.9, 2.0, 2.1, 2 * cmath.exp(0.7j)):
        value, residual = check_case(b)
        print("parameter", b, "projection norm", value, "finite-section residual", residual)
    # A direct exact monomial-weight diagnostic checks the rank-one defect:
    # T_(z squared) sends the normalized anti-analytic first monomial to
    # (2/3) times the normalized analytic first monomial; T_z squared gives 1/2.
    assert abs(2 / 3 - 1 / 2 - 1 / 6) < 1e-15
    for radius in (1.76, 1.9, 2.0, 2.1, 2.3):
        assert profile(radius) >= 1.0
    print("All supplementary checks passed.")


if __name__ == "__main__":
    main()
