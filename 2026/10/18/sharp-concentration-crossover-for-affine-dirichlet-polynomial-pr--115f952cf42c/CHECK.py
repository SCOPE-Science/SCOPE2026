#!/usr/bin/env python3
"""Independent numerical consistency checks for affine Dirichlet projection identities."""
import math
from scipy.integrate import quad
from scipy.special import betainc, betaln, gammaln


def exact(n, a):
    total = n * a
    b = (n - 1) * a
    threshold = a / (total + 1)
    return 1 + 2 * (total * betainc(a, b, threshold)
                    - (total + 1) * betainc(a + 1, b, threshold))


def integrated_by_parts(n, a):
    total = n * a
    b = (n - 1) * a
    threshold = a / (total + 1)
    boundary = math.exp(a * math.log(threshold)
                        + b * math.log1p(-threshold)
                        - math.log(a) - betaln(a, b))
    return 1 - 2 * betainc(a, b, threshold) + 2 * (total + 1) * boundary


def quadrature(n, a):
    total = n * a
    b = (n - 1) * a
    threshold = a / (total + 1)
    normalizer = betaln(a, b)
    def integrand(y):
        density = math.exp((a - 1) * math.log(y)
                           + (b - 1) * math.log1p(-y) - normalizer)
        return (total - n * (total + 1) * y) * density
    return 1 + 2 * quad(integrand, 0, threshold, limit=300,
                        epsabs=1e-11, epsrel=1e-11)[0]


def gamma_deviation(a):
    return 2 * math.exp(a * math.log(a) - a - gammaln(a))


checks = 0
for n in [2, 3, 5, 12, 50, 100]:
    for a in [0.25, 0.5, 1, 2, 5, 12]:
        first = exact(n, a)
        second = integrated_by_parts(n, a)
        assert abs(first - second) < 5e-8, (n, a, first, second)
        checks += 1
        assert 1 < first < 1 + 2 * n * a
        checks += 1
        assert abs(first / n - gamma_deviation(a)) <= math.sqrt(n*a+1)/n+1e-10
        checks += 1
        if a == 1:
            uniform = 2 * n * (n / (n + 1)) ** (n - 1) - 1
            assert abs(first - uniform) < 1e-9
            checks += 1
for n in [2, 4, 10, 30]:
    for a in [0.5, 1, 2.5]:
        assert abs(exact(n, a) - quadrature(n, a)) < 1e-8
        checks += 1
for c in [0.1, 0.5, 1, 3, 8]:
    early = exact(100, c / 100)
    late = exact(10000, c / 10000)
    expected = 1 + 2*c
    assert abs(late - expected) < abs(early - expected)
    checks += 1
for a in [0.001, 0.1, 0.5, 1, 10, 100]:
    early = exact(500, a) / (500 * gamma_deviation(a))
    late = exact(5000, a) / (5000 * gamma_deviation(a))
    assert abs(late - 1) < abs(early - 1)
    checks += 1
print(f"PASS: {checks} independent finite consistency assertions")
