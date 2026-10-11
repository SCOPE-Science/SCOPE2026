"""Exact rational Fourier checks for randomly selected integer circle maps.

These finite calculations supplement, rather than prove, the all-observable theorem.
"""
from fractions import Fraction as F


def transfer(poly, a, b, eps):
    out = {}
    for frequency, coeff in poly.items():
        for m, prob in ((a, 1 - eps), (b, eps)):
            if frequency % m == 0:
                key = frequency // m
                out[key] = out.get(key, F(0)) + prob * coeff
    return {k: v for k, v in out.items() if v}


def norm2(poly):
    return sum((v * v / 2 for v in poly.values()), F(0))


def asymptotic_variance(poly, a, b, eps):
    h = dict(poly)
    term = dict(poly)
    while term:
        term = transfer(term, a, b, eps)
        for k, v in term.items():
            h[k] = h.get(k, F(0)) + v
        h = {k: v for k, v in h.items() if v}
    qh = transfer(h, a, b, eps)
    return norm2(h) - norm2(qh)


def compose(poly, m):
    return {m * k: v for k, v in poly.items()}


def subtract(p, q):
    d = dict(p)
    for k, v in q.items():
        d[k] = d.get(k, F(0)) - v
    return {k: v for k, v in d.items() if v}


for a, b in ((2, 3), (3, 2), (2, 4), (6, 10), (4, 8)):
    f = {1: F(1), a: F(-1)}
    for eps in (F(0), F(1, 100), F(1, 5), F(3, 7), F(1)):
        assert asymptotic_variance(f, a, b, eps) == eps, (a, b, eps)


for base, power in ((2, 2), (2, 3), (3, 2)):
    a, b = base ** power, base
    phi = {1: F(1), a: F(-1)}
    for eps in (F(0), F(1, 10), F(2, 5), F(3, 4), F(1)):
        expected = eps - eps ** power
        assert asymptotic_variance(phi, a, b, eps) == expected, (a, b, eps)

for a, b in ((2, 3), (2, 4), (3, 6)):
    psi = {1: F(1), 2: F(1, 2)}
    phi = subtract(psi, compose(psi, a))
    expected = norm2(subtract(compose(psi, a), compose(psi, b)))
    assert expected > 0
    for denominator in (100, 1000, 10000):
        eps = F(1, denominator)
        quotient = asymptotic_variance(phi, a, b, eps) / eps
        assert abs(quotient - expected) <= F(10, denominator), (a, b, eps, quotient, expected)
    print(f"a={a}, b={b}, exact linear coefficient={expected}")
print('CHECK_OK')
