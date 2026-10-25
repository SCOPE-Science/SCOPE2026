"""Standalone numerical consistency checks for monomial-circle Hilbert-space formulas.

Runs with Python 3 standard library only. All assertions are finite diagnostics;
proof of the infinite-parameter statements is in RESULT.md.
"""
import cmath
import math


def log_m(n, p, a, b, beta):
    d = a + b
    return (n * (d * math.log(d) - a * math.log(a) - b * math.log(b)) / p
            + math.lgamma(1 + a * n / p)
            + math.lgamma(1 + b * n / p)
            - math.lgamma(2 + d * n / p)
            + beta * math.log(d * n + 2))


def kappa(p, a, b, beta):
    return math.sqrt(2 * math.pi * p * a * b) * (a + b) ** (beta - 1.5)


def check_asymptotics():
    for p, a, b, beta in ((2, 1, 1, 1.5), (2, 1, 2, 1),
                          (1.5, 2, 3, 1.1), (5, 3, 4, 1.7)):
        n = 10000
        log_ratio = (log_m(n, p, a, b, beta)
                     - (beta - .5) * math.log(n)
                     - math.log(kappa(p, a, b, beta)))
        assert abs(math.expm1(log_ratio)) < .001, (p, a, b, beta, log_ratio)


def check_optimality():
    p, a, b, beta = 2, 1, 2, 1
    N = 7
    M = [math.exp(log_m(n, p, a, b, beta)) for n in range(N + 2)]
    S = sum(1 / t for t in M)
    e = [(1 / t) / S for t in M]
    coeff = [sum(e[j + 1:]) for j in range(N + 1)]
    residual = [1 - coeff[0]] + [coeff[j - 1] - coeff[j]
                                 for j in range(1, N + 1)] + [coeff[-1]]
    assert max(abs(u - v) for u, v in zip(residual, e)) < 1e-12
    assert abs(sum(residual) - 1) < 1e-12
    assert abs(sum(M[j] * abs(residual[j])**2 for j in range(N+2))
               - 1 / S) < 1e-12


def check_boundary():
    for p, a, b in ((2, 1, 1), (1.5, 2, 3), (5, 3, 4)):
        d = a + b
        lam = (d**d / (a**a * b**b))**(1/(2*p))
        r1, r2 = (a/d)**(1/(2*p)), (b/d)**(1/(2*p))
        assert abs(r1**(2*p) + r2**(2*p) - 1) < 1e-12
        assert abs(lam*r1**a*r2**b - 1) < 1e-12
        th = .257
        eta1 = cmath.exp(1j*b*th)
        eta2 = cmath.exp(-1j*a*th)
        assert abs(eta1**a * eta2**b - 1) < 1e-12


if __name__ == '__main__':
    check_asymptotics()
    check_optimality()
    check_boundary()
    print('CHECK_OK')
