"""Independent finite checks of exact annulus-shift commutator identities.

These calculations support, but do not replace, the analytic infinite-dimensional proof.
Uses only the Python standard library.
"""
import math
from fractions import Fraction

checks = 0
for q in (Fraction(1, 7), Fraction(1, 2), Fraction(7, 8)):
    for k in range(0, 18):
        def squared_weight(n):
            return (1 + q ** (n + 1)) / (1 + q ** n)
        d1 = squared_weight(1 + k) - squared_weight(k)
        d2 = squared_weight(-k) - squared_weight(-k - 1)
        exact = (1 - q) ** 2 * q ** k / ((1 + q ** k) * (1 + q ** (k + 1)))
        assert d1 == d2 == exact
        checks += 1
        if k:
            old = (1 - q) ** 2 * q ** (k - 1) / ((1 + q ** (k - 1)) * (1 + q ** k))
            assert old > exact
            checks += 1

# Exact telescoping on each finite symmetric interval.
for q in (Fraction(1, 3), Fraction(4, 5)):
    for N in (1, 3, 7, 17):
        eigs = [((1 - q) ** 2 * q ** (n - 1) /
                 ((1 + q ** (n - 1)) * (1 + q ** n)))
                for n in range(-N, N + 1)]
        boundary = ((1 + q ** (N + 1)) / (1 + q ** N)
                    - (1 + q ** (-N)) / (1 + q ** (-N - 1)))
        assert sum(eigs) == boundary
        checks += 1

for q in (0.8, 0.96, 0.995):
    h = -math.log(q)
    K = math.ceil(38.0 / h)
    spectral_factors = [q ** k / ((1 + q ** k) * (1 + q ** (k + 1)))
                        for k in range(K)]
    trace = 2 * (1 - q) ** 2 * sum(spectral_factors)
    assert abs(trace - (1 - q)) < 1e-11
    checks += 1
    for p in (0.5, 1.0, 2.0, 3.0):
        predicted = math.gamma(p) ** 2 / math.gamma(2 * p)
        observed = (1 - q) * 2 * sum(z ** p for z in spectral_factors)
        # Only the finest mesh is used for quantitative convergence assertions.
        if q == 0.995:
            assert abs(observed - predicted) < 0.012, (p, observed, predicted)
        checks += 1
    for t in (0.4, 2.0, 5.0):
        observed = (1 - q) * 2 * sum(math.log1p(t * z) for z in spectral_factors)
        predicted = math.acosh(1 + t / 2) ** 2
        if q == 0.995:
            assert abs(observed - predicted) < 0.008, (t, observed, predicted)
        checks += 1

print(f"PASS: {checks} exact-rational and finite-asymptotic checks")
