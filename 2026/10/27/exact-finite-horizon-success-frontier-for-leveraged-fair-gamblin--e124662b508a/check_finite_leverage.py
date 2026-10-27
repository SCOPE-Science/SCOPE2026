"""Independent finite-horizon Bellman-envelope checks for a leverage-constrained fair game.

Dependencies: Python 3 standard library, sympy (symbolic identities).
This verifies algebra and finite numerical inequalities, not the theorem for all real parameters.
"""
from fractions import Fraction
from math import exp, log, isclose
from random import Random
from sympy import symbols, simplify, diff, exp as sexp, log as slog, series


def value(n, leverage, target, wealth):
    if wealth <= 0:
        return 0.0
    if wealth >= target:
        return 1.0
    if n == 0:
        return 0.0
    q = exp(log(target / wealth) / n)
    return (leverage / (leverage + q - 1)) ** n


def optimal_next(n, leverage, target, wealth):
    assert n >= 1 and 0 < wealth < target and leverage >= 1
    up = target if n == 1 else wealth * exp(log(target / wealth) / n)
    down = -(leverage - 1) * wealth
    prob = leverage * wealth / (up - down)
    return up, down, prob


def run_checks():
    # Exact rational success probabilities in special cases.
    assert Fraction(2, 3) ** 4 == Fraction(16, 81)
    assert Fraction(2, 5) ** 2 == Fraction(4, 25)
    assert isclose(value(4, 2, 16, 1), float(Fraction(16, 81)), abs_tol=1e-14)
    assert isclose(value(2, 2, 16, 1), float(Fraction(4, 25)), abs_tol=1e-14)
    assert isclose(value(1, 2, 16, 1), float(Fraction(2, 17)), abs_tol=1e-14)
    rng = Random(817)
    count = 0
    for L in [1.0, 1.2, 2.0, 3.5, 10.0]:
        for ratio in [1.01, 1.2, 2.0, 16.0, 1000.0]:
            for n in range(1, 17):
                x, m = 1.0, ratio
                up, down, p = optimal_next(n, L, m, x)
                assert down <= 0 and x <= up <= m * (1 + 1e-12)
                assert 0 < p <= 1
                assert isclose(p * up + (1-p) * down, x, rel_tol=3e-12, abs_tol=3e-12)
                rhs = p * value(n-1, L, m, up)
                assert isclose(value(n, L, m, x), rhs, rel_tol=2e-12, abs_tol=2e-12)
                if n > 1 and L > 1:
                    assert value(n, L, m, x) > value(n-1, L, m, x)
                assert value(n, L, m, x) <= ratio ** (-1/L) + 1e-11
                # Verify the full affine Bellman majorant on interior and endpoint samples.
                if n > 1:
                    slope = value(n-1, L, m, up) / (up - down)
                    for y in [down, 0, 1e-12, x, up, m] + [rng.random() * m for _ in range(35)]:
                        assert value(n-1, L, m, y) <= slope * (y - down) + 1e-10
                        count += 1
    # Symbolic critical stationarity at the candidate and first-order loss.
    L, x, u, q = symbols('L x u q', positive=True)
    a = (L-1)*x
    expr = simplify(q/(u*(L+q-1)) - 1/(u+a))
    assert simplify(expr - (L-1)*(x*q-u)/(u*(L+q-1)*(u+a))) == 0
    h, z = symbols('h z', positive=True)
    series_log = series(-slog(1+(sexp(h*z)-1)/L)/z, z, 0, 2).removeO()
    assert simplify(series_log + h/L + (L-1)*h**2*z/(2*L**2)) == 0
    print('PASS: rational special cases, dynamic recursions, affine majorants, and asymptotic coefficient; finite inequality checks:',count)

if __name__ == '__main__':
    run_checks()
