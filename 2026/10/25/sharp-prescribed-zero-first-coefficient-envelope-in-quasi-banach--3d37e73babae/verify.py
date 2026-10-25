"""Standalone arithmetic checks for a first-coefficient Hardy-space envelope.

Run: python verify.py.  General validity is established analytically in RESULT.md;
finite tests here verify formulas and boundary conventions only.
"""
from fractions import Fraction
from cmath import exp
from math import sqrt, pi


def t_star(q, rho):
    if rho == 0:
        return 0.0
    # Stable positive quadratic-root evaluation.
    h = 1 - rho * rho
    return 2 * rho / (sqrt(h * h + 4 * (q - 1) * rho * rho) + h)


def bound(q, rho):
    t = t_star(q, rho)
    return (1 - rho * rho + q * rho * t) / (1 + t * t) ** (q / 2)


def derivative_stationarity(q, rho, t):
    return rho - (1 - rho * rho) * t - (q - 1) * rho * t * t


def finite_difference_first_coefficient(q, rho, phase=0.1):
    t = t_star(q, rho)
    u = exp(1j * phase)
    scale = (1 + t * t) ** (-q / 2)
    # B(z)=(rho+u*z)/(1+rho*u*z); H(z)=scale*(1+t*u*z)^q.
    # Product derivative at zero is explicit, independently from the envelope.
    a0 = rho * scale
    a1 = u * scale * (1 - rho * rho + q * rho * t)
    return a0, a1


def run():
    count = 0
    for q in (2.01, 2.1, 2.5, 3.0, 4.0, 7.0, 15.0, 100.0):
        for rho in (0.0, 0.00001, 0.01, 0.15, 0.33, 0.5, 0.75, 0.95, 0.999999, 1.0):
            t = t_star(q, rho)
            assert t >= 0 and t <= 1 / sqrt(q - 1) + 1e-12
            assert abs(derivative_stationarity(q, rho, t)) < 5e-12 * (q + 1)
            _, a1 = finite_difference_first_coefficient(q, rho)
            assert abs(abs(a1) - bound(q, rho)) < 1e-12 * max(1, bound(q, rho))
            assert bound(q, rho) >= 1 - 1e-13
            count += 1
        grid = [bound(q, k / 100.0) for k in range(101)]
        assert all(grid[i + 1] > grid[i] for i in range(100))
        assert abs(grid[-1] - sqrt(q) * ((q - 1) / q) ** ((q - 1) / 2)) < 1e-12
    # Algebraic monotonicity witness for each rational q, rho:
    # P(2*rho/q) = -rho*(q-2)*(q-2*rho**2)/q**2.
    exact = 0
    for q in (Fraction(5, 2), Fraction(3), Fraction(4), Fraction(9, 2), Fraction(7)):
        for rho in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
            t = 2 * rho / q
            P = (q - 1) * rho * t * t + (1 - rho * rho) * t - rho
            RHS = -rho * (q - 2) * (q - 2 * rho * rho) / (q * q)
            assert P == RHS and P < 0
            exact += 1
    # Exact rational example at p=1/2 and rho=1/2: 6 t^2+3t-2=0.
    r = .5
    t = t_star(4., r)
    assert abs(6 * t * t + 3 * t - 2) < 1e-14
    # Leading small-rho coefficient and near-one slope tested asymptotically.
    for q in (2.5, 3., 4., 7.):
        for rho in (1e-3, 3e-4):
            approx = (bound(q, rho) - 1) / (rho * rho)
            assert abs(approx - (q / 2 - 1)) < .002
        h = 1e-4
        M = bound(q, 1)
        slope = (q / sqrt(q - 1) - 2) * ((q - 1) / q) ** (q / 2)
        assert abs((M - bound(q, 1 - h)) / h - slope) < .002
    print(f'CHECK_OK: {count} analytic-parameter grids, {exact} exact rational monotonicity certificates, endpoint tests')


if __name__ == '__main__':
    run()
