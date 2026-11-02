"""Self-contained finite checks for the stated scalar smoothed-gradient map.

Requires Python 3.9+ standard library only; numerical probes support, but do not
replace, the analytic classification of all positive parameters.
"""
from fractions import Fraction
from math import isclose
import random


def T(x, p, eps, eta):
    if x == 0:
        return 0.0
    gradient = (abs(x) ** (p - 2)) * x
    return x - eta * gradient / (abs(gradient) + eps)


def crit(p, eps):
    r = ((p - 2) * eps) ** (1.0 / (p - 1))
    return r, 2 * (p - 1) * r / (p - 2)


def h(r, p, eps):
    return r + eps / (r ** (p - 2))


def derivative_at_cycle(r, p, eps):
    return 1.0 - 2.0 * (p - 1) * eps / (r ** (p - 1) + eps)


def bisect(f, lo, hi, num=100):
    f_lo = f(lo)
    f_hi = f(hi)
    assert f_lo * f_hi < 0
    for _ in range(num):
        mid = (lo + hi) / 2
        if f_lo * f(mid) > 0:
            lo = mid
            f_lo = f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


# Exact rational instance p=3, eps=1, eta=5.
# At r=1/2, the map reverses sign and has derivative -11/5;
# at r=2, the map reverses sign and has derivative +1/5.
for r in (Fraction(1, 2), Fraction(2, 1)):
    g = r * r
    x_next = r - 5 * g / (g + 1)
    assert x_next == -r
assert Fraction(1) - 4 / (Fraction(1, 4) + 1) == -Fraction(11, 5)
assert Fraction(1) - 4 / (Fraction(4) + 1) == Fraction(1, 5)
assert (-Fraction(11, 5)) ** 2 == Fraction(121, 25)
assert Fraction(1, 5) ** 2 == Fraction(1, 25)

rng = random.Random(20261031)
checks = 5

# Direct evaluation and analytic minimizer checks.
for _ in range(350):
    p = 2.03 + 7.0 * rng.random()
    eps = 10.0 ** rng.uniform(-3, 2)
    rstar, etac = crit(p, eps)
    assert isclose(h(rstar, p, eps), etac / 2, rel_tol=5e-12)
    assert h(rstar * 0.71, p, eps) > h(rstar, p, eps)
    assert h(rstar * 1.41, p, eps) > h(rstar, p, eps)
    checks += 3

# At exact threshold the coalesced nonzero symmetric orbit has multiplier +1.
for p, eps in ((2.25, 0.1), (3.0, 1.0), (4.5, 9.0), (8.0, 3.0)):
    rstar, etac = crit(p, eps)
    assert isclose(T(rstar, p, eps, etac), -rstar, rel_tol=1e-12)
    assert isclose(derivative_at_cycle(rstar, p, eps), -1.0, abs_tol=1e-12)
    checks += 2

# Strict-subcritical global radius contraction sampled independently on
# logarithmic scales; monotonicity for all radii is proved in RESULT.md.
for _ in range(800):
    p = 2.05 + 5.0 * rng.random()
    eps = 10.0 ** rng.uniform(-4, 3)
    rstar, etac = crit(p, eps)
    eta = etac * (0.01 + 0.989 * rng.random())
    x = rstar * (10.0 ** rng.uniform(-2, 2)) * (-1 if rng.random() < 0.5 else 1)
    xn = T(x, p, eps, eta)
    assert abs(xn) < abs(x)
    checks += 1

# For eta>eta_c, find both roots on opposite sides of unique minimizer,
# verify both symmetric cycles and their exact stability types.
for _ in range(300):
    p = 2.2 + 4.0 * rng.random()
    eps = 10.0 ** rng.uniform(-2, 2)
    rstar, etac = crit(p, eps)
    eta = etac * (1.03 + 2.0 * rng.random())
    f = lambda r: h(r, p, eps) - eta / 2
    low = rstar
    while f(low) <= 0:
        low /= 2
    high = rstar
    while f(high) <= 0:
        high *= 2
    rminus = bisect(f, low, rstar)
    rplus = bisect(f, rstar, high)
    assert 0 < rminus < rstar < rplus
    for r in (rminus, rplus):
        assert isclose(T(r, p, eps, eta), -r, rel_tol=1e-10, abs_tol=1e-10)
        assert isclose(T(-r, p, eps, eta), r, rel_tol=1e-10, abs_tol=1e-10)
        checks += 2
    assert derivative_at_cycle(rminus, p, eps) < -1
    assert -1 < derivative_at_cycle(rplus, p, eps) < 1
    checks += 3

# The saddle-node radius splitting has the predicted square-root slope.
for p, eps in ((3., 1.), (4., 0.5), (2.5, 1.5), (5.25, 0.2)):
    rstar, etac = crit(p, eps)
    delta = etac * 1e-6
    eta = etac + delta
    f = lambda r: h(r, p, eps) - eta / 2
    left = bisect(f, rstar * 0.5, rstar)
    right = bisect(f, rstar, rstar * 2.0)
    predicted = ((rstar / (p - 1)) * delta) ** 0.5
    assert isclose((right - left) / 2, predicted, rel_tol=0.004)
    checks += 1

# Near-minimum asymptotic constant for a trajectory that never hits zero.
# Choose small starts, far from potential finite-zero exceptional inputs.
for p, eps, eta, x0 in ((3., 1., 3., 0.1), (4., 1., 5., 0.1), (2.5, 1., 3., 0.01)):
    x = x0
    for k in range(1, 70001):
        x = T(x, p, eps, eta)
    target = eps / ((p - 2) * eta)
    value = 70000 * abs(x) ** (p - 2)
    assert abs(value / target - 1) < 0.06, (p, value, target)
    checks += 1

print(f'PASS: {checks} finite exact-rational and numerical assertions')
