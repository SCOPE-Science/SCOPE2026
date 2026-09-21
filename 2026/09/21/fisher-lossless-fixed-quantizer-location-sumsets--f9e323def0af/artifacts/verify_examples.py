"""Numerical checks for the fixed-quantizer Fisher-lossless location theorem.

This script verifies two scientifically relevant examples:
1. For an asymmetric Laplace location family, a fixed interval quantizer has
   full Fisher information exactly when the location aligns the density knot
   with a finite quantizer threshold (tested at representative points).
2. Arithmetic-progression knot and threshold sets attain the sharp
   |Lambda| = m-kappa cardinality bound.
"""

from math import exp, isclose


def ald_cdf(z, a, b):
    c = a * b / (a + b)
    if z < 0.0:
        return (c / a) * exp(a * z)
    return 1.0 - (c / b) * exp(-b * z)


def ald_pdf(z, a, b):
    c = a * b / (a + b)
    if z < 0.0:
        return c * exp(a * z)
    return c * exp(-b * z)


def quantized_fi(theta, thresholds, a, b):
    ends = [float("-inf"), *thresholds, float("inf")]
    out = 0.0
    for lo, hi in zip(ends[:-1], ends[1:]):
        Flo = 0.0 if lo == float("-inf") else ald_cdf(lo - theta, a, b)
        Fhi = 1.0 if hi == float("inf") else ald_cdf(hi - theta, a, b)
        p = Fhi - Flo
        flo = 0.0 if lo == float("-inf") else ald_pdf(lo - theta, a, b)
        fhi = 0.0 if hi == float("inf") else ald_pdf(hi - theta, a, b)
        dp = flo - fhi
        out += dp * dp / p
    return out


def lossless_shifts(knots, thresholds):
    T = set(thresholds)
    candidates = {t - knots[0] for t in thresholds}
    return sorted(theta for theta in candidates if all(k + theta in T for k in knots))


def main():
    a, b = 1.7, 0.8
    thresholds = [-2.0, 0.5, 3.0]
    full = a * b
    for theta in thresholds:
        got = quantized_fi(theta, thresholds, a, b)
        assert isclose(got, full, rel_tol=2e-12, abs_tol=2e-12), (theta, got, full)
    for theta in [-1.0, 0.0, 1.25, 4.0]:
        if theta not in thresholds:
            got = quantized_fi(theta, thresholds, a, b)
            assert got < full - 1e-10, (theta, got, full)

    for m in range(2, 12):
        for kappa in range(1, m):
            knots = list(range(kappa))
            thresholds_ap = list(range(m - 1))
            shifts = lossless_shifts(knots, thresholds_ap)
            assert shifts == list(range(m - kappa)), (m, kappa, shifts)

    print("asymmetric-Laplace threshold-alignment checks: passed")
    print("arithmetic-progression sharpness checks: passed")


if __name__ == "__main__":
    main()
