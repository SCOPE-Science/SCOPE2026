#!/usr/bin/env python3
"""Supplementary numerical tests for two convolution-quadrature weight arrays.

Requires Python 3 standard library. All asymptotic assertions in the result
are established analytically; this script checks finite cases only.
"""
import math


def integrate(f, panels=1200):
    assert panels % 2 == 0
    h = 1.0 / panels
    total = f(0.0) + f(1.0)
    for j in range(1, panels):
        total += (4 if j % 2 else 2) * f(j * h)
    return total * h / 3


def be_beta(n, beta):
    if n == 0:
        return 1.0
    if beta == 0:
        return 0.0
    return math.exp(math.lgamma(n + beta) - math.lgamma(n + 1) - math.lgamma(beta))


def bdf_beta(n, beta):
    # Recurrence from the logarithmic derivative of the BDF2 symbol.
    if beta == 0:
        return 1.0 if n == 0 else 0.0
    coeff = [(2.0 / 3.0) ** beta]
    for j in range(1, n + 1):
        coeff.append(beta * sum((1 + 3 ** (-k)) * coeff[j-k]
                                for k in range(1, j+1)) / j)
    return coeff[-1]


def bdf_minus_be_at_large_n(n, beta, cutoff=70):
    if beta == 0 or beta == 1:
        return 0.0
    # For n>=1000, the uniform first Stirling correction in the Gamma ratio
    # avoids subtracting two large log-Gamma values.
    a = (n ** (beta - 1.0)) / math.gamma(beta)
    a *= 1.0 + beta * (beta - 1.0) / (2 * n)
    pk = (2.0 / 3.0) ** beta
    logratio = 0.0
    diff_factor = 0.0
    for k in range(1, min(n, cutoff) + 1):
        pk *= (beta + k - 1.0) / (3 * k)
        logratio += math.log1p((1.0-beta) / (n-k+beta))
        diff_factor += pk * math.expm1(logratio)
    return a * diff_factor


def main():
    z0 = integrate(lambda beta: (2/3)**beta - 1)
    exact0 = 1/(3 * math.log(1.5)) - 1
    assert abs(z0 - exact0) < 5e-13, (z0, exact0)
    assert exact0 < 0

    # Factorized BDF2 generating function: the beta=1 coefficients equal
    # 1-3**(-n-1), while beta=0 coefficients vanish except at index zero.
    for n in range(12):
        assert abs(bdf_beta(n, 1.0) - (1.0 - 3.0 ** (-n-1))) < 1e-13
        assert abs(bdf_beta(n, 0.0) - (1.0 if n == 0 else 0.0)) < 1e-13

    # Direct recurrence independently checked against finite convolution of
    # generalized-binomial and negative-binomial coefficients.
    for beta in [0.1, 0.25, 0.5, 0.75, 0.9]:
        for n in range(15):
            p = (2 / 3) ** beta
            conv = p * be_beta(n, beta)
            for k in range(1, n+1):
                p *= (beta+k-1)/(3*k)
                conv += p * be_beta(n-k,beta)
            assert abs(conv-bdf_beta(n,beta)) < 1e-12

    observed = []
    for n in [1, 2, 5, 10, 25, 50, 100]:
        d = integrate(lambda beta: bdf_beta(n,beta)-be_beta(n,beta), 160)
        observed.append((n,d))
        assert d > 0, (n,d)

    high = []
    for n in [10_000, 1_000_000, 1_000_000_000]:
        d = integrate(lambda beta: bdf_minus_be_at_large_n(n,beta), 1200)
        scale = d * n * math.log(n)**2
        high.append((n, d, scale))
        assert 0 < scale < 0.51
    assert high[0][2] < high[1][2] < high[2][2]
    assert abs(high[-1][2] - 0.5) < 0.1
    # Endpoint-density families w(beta)=(1-beta)**alpha: finite large-index
    # observations are compatible with the different logarithmic powers.
    for exponent in [1, 2]:
        ratios = []
        for n in [10_000, 1_000_000, 1_000_000_000]:
            d = integrate(lambda beta: (1-beta)**exponent *
                          bdf_minus_be_at_large_n(n,beta), 1200)
            ratios.append(d * n * math.log(n)**(exponent+2))
        assert ratios[0] < ratios[1] < ratios[2] < math.gamma(exponent+2)/2
    print('density endpoint power tests: alpha=1,2; finite indices only')
    print('VERIFY_OK: zero-index coefficient, endpoint orders, recurrence convolution,')
    print('seven finite positive differences, three long-index tail ratios')
    for entry in observed:
        print('n=%d difference=%.12g' % entry)
    for n,d,s in high:
        print('n=%d difference=%.12g scaled=%.9f' % (n,d,s))


if __name__ == '__main__':
    main()
