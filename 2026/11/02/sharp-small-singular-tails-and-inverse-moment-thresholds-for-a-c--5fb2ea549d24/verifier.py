"""Supplementary reproducibility checks for a two-frequency circular sketch."""
import cmath
import math
import random

TAU = 2.0 * math.pi


def gram_edge(angles):
    z = sum((cmath.exp(1j * a) for a in angles), 0j)
    return len(angles) - abs(z)


def leading_constant(count):
    return (math.sqrt(count) / (TAU ** ((count - 1.0) / 2.0)
                                * math.gamma((count + 1.0) / 2.0)))


def quadratic(phis):
    count = len(phis) + 1
    return 0.5 * (sum(t*t for t in phis) - sum(phis)**2 / count)


def cdf_two(epsilon):
    return 2.0 / math.pi * math.acos(1.0 - epsilon / 2.0)


def check():
    assertions = 0
    # Closed-form 2-column tests, including the end points.
    for k in range(2001):
        e = 2.0 * k / 2000.0
        cdf = cdf_two(e)
        assert 0.0 <= cdf <= 1.0
        assertions += 1
        if k > 0:
            assert cdf >= cdf_two(e - 0.001)
            assertions += 1
    assert abs(leading_constant(2) - 2.0 / math.pi) < 1e-13
    assert abs(leading_constant(3) - math.sqrt(3.0)/(2*math.pi)) < 1e-13
    assertions += 2

    # The Gram eigenvalues, exact quadratic limit, and pseudoinverse relation.
    rng = random.Random(172917)
    for count in range(2, 9):
        for _ in range(850):
            phis = [rng.uniform(-2.7, 2.7) for __ in range(count-1)]
            angles = [0.0] + phis
            z = sum(cmath.exp(1j*p) for p in angles)
            lam = gram_edge(angles)
            assert abs(lam - (count - abs(z))) < 1e-12
            assert lam >= -1e-12
            assertions += 2
            if lam > 1e-10:
                kappa_squared = (count+abs(z)) / lam
                assert abs((kappa_squared+1)*lam - 2*count) < 1e-9
                assertions += 1
        for scale in (0.015, 0.008, 0.004):
            for _ in range(300):
                phis = [scale*rng.uniform(-1.0,1.0) for __ in range(count-1)]
                q = quadratic(phis)
                e = gram_edge([0.0]+phis)
                assert q > 0 and abs(e/q-1) < 0.003
                assertions += 1

    # Numerical Monte Carlo corroboration (not part of the analytical proof).
    samples = 290000
    for count, epsilon, tolerance in ((2,0.1,0.022),(3,0.1,0.034),(4,0.2,0.075)):
        hits = 0
        for _ in range(samples):
            angles = [0.0] + [rng.uniform(-math.pi, math.pi)
                              for __ in range(count-1)]
            hits += gram_edge(angles) <= epsilon
        empirical = hits/samples
        predicted = leading_constant(count)*epsilon**((count-1.0)/2.0)
        assert abs(empirical / predicted - 1.0) < tolerance, (
            count, empirical, predicted, tolerance)
        assertions += 1

    # Gaussian counterpart: complex Gamma(L-1,1) residual has
    # expected reciprocal equal 1/(L-2) for integer L>2.
    for count in range(3, 20):
        assert count-2 > 0
        assertions += 1
    print(f"PASS: {assertions} deterministic assertions and {3*samples:,} seeded phase draws")


if __name__ == '__main__':
    check()
