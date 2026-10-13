"""Exact rational crosschecks for three-term centred exponential moment comparison.

Run: python3 verification/check_moments.py
Uses only the Python standard library. These tests support, but do not replace,
the proof for arbitrary real coefficients and real moment orders.
"""
from fractions import Fraction as F
from math import factorial, gamma, log, pi, sqrt


def absolute_moment_factor(a, b, k):
    """E|a E1+b E2-(a+b) E3|^k / k!, k nonnegative integer."""
    c = a + b
    if not c:
        raise ValueError('At least one coefficient must be nonzero')
    atom = c ** (k + 2) / ((a + c) * (b + c))
    if a != b:
        plus = ((a ** (k + 2) / (a + c)) - (b ** (k + 2) / (b + c))) / (a - b)
    else:
        plus = a ** (k + 1) * ((k + 1) * a + (k + 2) * c) / (a + c) ** 2
    return plus + atom


def mgf_coefficient(xs, degree):
    out = [F(0)] * (degree + 1)
    out[0] = F(1)
    for x in xs:
        nxt = [F(0)] * (degree + 1)
        for n in range(degree + 1):
            nxt[n] = sum(out[j] * x ** (n - j) for j in range(n + 1))
        out = nxt
    return out[degree]


def gaussian_even_moment(k):
    return factorial(2 * k) // (2 ** k * factorial(k))


def norm_ratio_log(a, b, p):
    af, bf = float(a), float(b)
    c = af + bf
    if a != b:
        A = ((af ** (p + 2) / (af + c)) - (bf ** (p + 2) / (bf + c))) / (af - bf)
    else:
        A = af ** (p + 1) * ((p + 1) * af + (p + 2) * c) / (af + c) ** 2
    A += c ** (p + 2) / ((af + c) * (bf + c))
    return log(A) + .5 * p * log(2) + log(gamma(1 + p / 2))


def main():
    count = 0
    values = [F(0), F(1, 7), F(1, 3), F(1, 2), F(1), F(2), F(5), F(11)]
    for a in values:
        for b in values:
            if a == 0 and b == 0:
                continue
            c = a + b
            assert absolute_moment_factor(a, b, 0) == 1
            count += 1
            assert 2 * absolute_moment_factor(a, b, 2) == a*a + b*b + c*c
            count += 1
            for k in range(1, 11):
                p = 2*k
                lhs = absolute_moment_factor(a, b, p)
                rhs = mgf_coefficient([a, b, -c], p)
                assert lhs == rhs, (a, b, p, lhs, rhs)
                # A further check against the published variance--Gaussian bound.
                variance = a*a + b*b + c*c
                assert factorial(p) * lhs >= gaussian_even_moment(k) * variance**k
                count += 2
    for u in [F(1, 10), F(1), F(3), F(11)]:
        for c in [F(1, 5), F(2), F(13)]:
            for t in [F(1, 7), F(1), F(6)]:
                # Derivative of (u/(u+c))exp(-t/u) divided by exp(-t/u).
                lhs = c/(u+c)**2 + t/(u*(u+c))
                rhs = ((u+c)-u)/(u+c)**2 + t/(u*(u+c))
                assert lhs == rhs
                count += 1
    for j in range(1, 1201):
        p = F(2) + F(j, 17)
        # Elementary sufficient bound for strict curvature of
        # log[(p+1) 2^(p/2) Gamma(1+p/2) s^p].
        assert F(1, 2)*(p+2)**(-1) > (p+1)**(-2)
        count += 1
    for a, b in [(1., 0.), (1., 1.), (1., 2.), (1., 7.), (3., 5.)]:
        for p in [2.4, 3., 4.5, 7.5, 11.]:
            h = .0001
            curvature = (norm_ratio_log(a, b, p+h) + norm_ratio_log(a, b, p-h) - 2*norm_ratio_log(a, b, p)) / h**2
            assert curvature > 1e-3, (a, b, p, curvature)
            count += 1
    print(f'PASS: {count} exact and numerical assertions, no exceptions')


if __name__ == '__main__':
    main()
