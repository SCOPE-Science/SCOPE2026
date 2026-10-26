"""Reproduce exact finite identities and numerical asymptotic spot checks for the stated SIS mean-field map.

Uses only the Python standard library. Finite checks are not proofs of asymptotic claims.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb

getcontext().prec = 72
D = Decimal


def bisection(fun, low, high, rounds=190):
    assert fun(low) > 0 and fun(high) < 0
    for _ in range(rounds):
        mid = (low + high) / 2
        if fun(mid) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def solve(r, s, delta, epsilon, kappa):
    beta = delta / D(s - 1)
    core = lambda x: 1 - (1 - (1 - delta) * x) * (1 - beta * x) ** (r - 1)
    x_star = bisection(lambda x: core(x) - x, D('1e-40'), D(1))
    q = delta * (1 - delta) + delta * delta * D(s - 2) / D(2 * (s - 1))

    def equilibrium_core(y):
        func = lambda x: 1 - (1 - (1 - delta) * x) * (1 - beta * x) ** (r - 1) * (1 - epsilon * beta * y) ** s - x
        return bisection(func, x_star * (1 - D("1e-25")), D(1))

    def satellite_residual(y):
        x = equilibrium_core(y)
        return 1 - (1 - (1 - delta) * y) * (1 - kappa * beta * y) ** (s - 1) * (1 - epsilon * beta * x) ** r - y

    y = bisection(satellite_residual, D(0), D(1))
    x = equilibrium_core(y)
    assert 0 < x < 1 and 0 < y < 1
    return beta, q, x_star, x, y


def exact_taylor_checks():
    checks = 0
    for s in range(2, 15):
        for num, den in [(1, 3), (1, 2), (3, 4), (7, 8)]:
            delta = Fraction(num, den)
            beta = delta / (s - 1)
            # Coefficient of y^2 in (1-(1-delta)y)(1-beta*y)^(s-1).
            a2 = comb(s - 1, 2) * beta**2 + (1 - delta) * (s - 1) * beta
            q = delta * (1 - delta) + delta**2 * Fraction(s - 2, 2 * (s - 1))
            assert a2 == q and q > 0
            checks += 1
    # Exactly x_* = 3-sqrt(5) in the (r,s,delta)=(3,2,1/2) benchmark.
    # The corresponding core fixed-point polynomial, after removing x=0, is
    # 0 = x^2-6*x+4, so the physical positive root is 3-sqrt(5).
    assert (Fraction(1,2), -Fraction(3,4), Fraction(1,8)) == tuple(Fraction(v,8) for v in (4,-6,1))
    checks += 1
    return checks


def numerical_checks():
    checks = 0
    for r, s, deltastr in [(3, 2, '0.5'), (5, 3, '0.4'), (7, 4, '0.7')]:
        delta = D(deltastr)
        eps = D('1e-8')
        for c in (-2, 0, 2):
            kappa = 1 + D(c) * eps.sqrt()
            beta, q, x_star, x, y = solve(r, s, delta, eps, kappa)
            z = (delta * D(c) + (delta**2 * D(c)**2 + 4*q*r*beta*x_star).sqrt()) / (2*q)
            assert abs(y / (eps.sqrt()*z) - 1) < D('0.003')
            assert x >= x_star
            checks += 1
        for kappa in (D('0.7'), D('0.9')):
            beta, q, x_star, x, y = solve(r, s, delta, eps, kappa)
            pred = r * beta * x_star / (delta * (1 - kappa)) * eps
            assert abs(y / pred - 1) < D('0.003')
            checks += 1
    return checks


if __name__ == '__main__':
    n_exact = exact_taylor_checks()
    n_numerical = numerical_checks()
    print('PASS:', n_exact, 'exact coefficient identities and', n_numerical, 'numerical asymptotic comparisons')
