"""Deterministic corroboration of the Lamperti--reset occupation SCGF.

Uses only the Python standard library. Finite checks support, but do not
replace, the analytic all-parameter and large-deviation arguments.
"""
import math


def stieltjes(mu, a, b):
    assert 0 < mu <= 0.5 and min(a, b) > 0
    return (a ** (mu - 1) + b ** (mu - 1)) / (a ** mu + b ** mu)


def scgf(mu, r, k):
    lo = max(k, 0.0) - r
    # Continuity at the boundary with a divergent endpoint Stieltjes transform.
    lo = math.nextafter(lo, math.inf)
    hi = max(k, 0.0) + r + abs(k) + 1

    def f(s):
        a = r + s
        b = a - k
        if min(a, b) <= 0:
            return float('inf')
        return r * stieltjes(mu, a, b) - 1.0

    assert f(hi) < 0
    for _ in range(95):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def rho_and_fraction(mu, t):
    p = 1 / mu
    left = t ** p
    right = (1 - t) ** p
    u = left / (left + right)
    den = t * t + (1 - t) ** 2 + 2 * t * (1 - t) * math.cos(math.pi * mu)
    density = math.sin(math.pi * mu) / (math.pi * mu * den)
    return density, u


def simpson(f, n=2000):
    assert n % 2 == 0
    h = 1 / n
    total = f(0) + f(1)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(j * h)
    return total * h / 3


def near(x, y, tol=2e-7):
    assert abs(x - y) < tol * max(1, abs(x), abs(y)), (x, y)


count = 0
for mu in (0.25, 1 / 3, 0.4, 0.5):
    near(simpson(lambda t: rho_and_fraction(mu, t)[0]), 1, 1e-9)
    count += 1
    near(simpson(lambda t: math.prod(rho_and_fraction(mu, t))), 0.5, 1e-9)
    count += 1
    for r in (0.6, 1.0, 2.3):
        for k in (-3., -1., -0.2, 0.2, 1., 3.):
            v = scgf(mu, r, k)
            a, b = r + v, r + v - k
            near(r * stieltjes(mu, a, b), 1, 1e-10)
            count += 1
            integral = simpson(lambda t: (
                rho_and_fraction(mu, t)[0] /
                (a - k * rho_and_fraction(mu, t)[1])))
            near(integral, stieltjes(mu, a, b), 1e-7)
            count += 1
            near(scgf(mu, r, -k) + k, v, 1e-9)
            count += 1
            if mu == 0.5:
                closed = (k + math.sqrt(k*k + 4*r*r)) / 2 - r
                near(v, closed, 1e-10)
                count += 1
        step = 0.0006
        curvature = (scgf(mu, r, step) + scgf(mu, r, -step)) / step**2
        near(curvature, (1 - mu) / (2 * r), 4e-6)
        count += 1
        for k in (0.0, 0.3, 0.7):
            step = 0.01
            second = scgf(mu, r, k + step) - 2 * scgf(mu, r, k) + scgf(mu, r, k-step)
            assert second > 0
            count += 1
    # Endpoint exponent from an independently parameterized pole branch.
    for r in (0.6, 2.3):
        q = 1e-16
        qm = q ** (mu - 1)
        b = r * q * (1 + qm) / (1 + q ** mu)
        k = r * (1-q) * (1 + qm) / (1 + q ** mu)
        predicted = r ** (1 / (1-mu)) * k ** (-mu/(1-mu))
        assert abs(b / predicted - 1) < 0.002, (mu, b/predicted)
        count += 1
print(f'PASS: {count} independent deterministic quadrature/algebra checks')
