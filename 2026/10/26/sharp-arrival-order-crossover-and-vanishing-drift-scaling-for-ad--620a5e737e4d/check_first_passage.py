"""Reproducible checks for first-passage breakthrough distribution comparisons.

Run: python check_first_passage.py  (Python 3 standard library only).
Checks supplement, but do not replace, the analytic proof in RESULT.md.
"""
import math
import random

SQRT2 = math.sqrt(2.0)


def cdf(t, L, v, D):
    if t <= 0:
        return 0.0
    z1 = (v * t - L) / math.sqrt(4.0 * D * t)
    z2 = (-v * t - L) / math.sqrt(4.0 * D * t)
    return 0.5 * math.erfc(-z1) + 0.5 * math.exp(v * L / D) * math.erfc(-z2)


def pdf(t, L, v, D):
    return L / math.sqrt(4.0 * math.pi * D * t ** 3) * math.exp(-(L - v * t) ** 2 / (4.0 * D * t))


def log_density_ratio(t, L, v1, D1, v2, D2):
    A = L * L / 4.0 * (1.0 / D2 - 1.0 / D1)
    B = (v2 * v2 / D2 - v1 * v1 / D1) / 4.0
    C = 0.5 * math.log(D2 / D1) + L / 2.0 * (v1 / D1 - v2 / D2)
    return A / t + B * t + C


def cross_root(fun, lo, hi):
    flo, fhi = fun(lo), fun(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(95):
        mid = (lo + hi) / 2.0
        if (fun(mid) > 0) == (flo > 0):
            lo, flo = mid, fun(mid)
        else:
            hi = mid
    return (lo + hi) / 2.0


def G(y, D, L=1.0):
    z = math.sqrt(y / (2.0 * D))
    phi = math.exp(-z * z / 2.0) / math.sqrt(2 * math.pi)
    tail = 0.5 * math.erfc(z / SQRT2)
    return L / D * (phi / z - tail)


def run():
    L, D1, D2 = 1.0, 4.0, 1.0
    v = 1.0
    t_cross = cross_root(lambda t: cdf(t, L, v, D1) - cdf(t, L, v, D2), 2.0, 4.0)
    assert abs(t_cross - 2.5581690175836225) < 1e-10
    assert L / v < t_cross
    assert cdf(0.5, L, v, D1) > cdf(0.5, L, v, D2)
    assert cdf(6.0, L, v, D1) < cdf(6.0, L, v, D2)
    print('fixed-drift CDF crossover:', format(t_cross, '.13f'))

    y_p = 2 * math.log(D1 / D2) / (1 / D2 - 1 / D1)
    y_star = cross_root(lambda y: G(y, D1) - G(y, D2), 0.5, 3.0)
    assert 0 < y_star < y_p
    print('singular scaling constant:', format(y_star, '.13f'))
    for speed, eps in [(0.2, 0.28), (0.1, 0.13), (0.05, 0.07), (0.02, 0.03)]:
        f = lambda y: cdf(y / speed ** 2, L, speed, D1) - cdf(y / speed ** 2, L, speed, D2)
        scaled = cross_root(f, 0.5, y_p)
        assert abs(scaled - y_star) < eps
        print('v, v^2*t_cross:', speed, format(scaled, '.11f'))

    # Comparison with the derivative of the exact CDF; 300 bounded cases.
    rng = random.Random(91311)
    for _ in range(300):
        L = rng.uniform(0.7, 1.8)
        v = rng.uniform(0.2, 2.4)
        D = rng.uniform(0.6, 3.0)
        t = rng.uniform(0.1, 3.0)
        h = 1e-5
        numerical = (cdf(t + h, L, v, D) - cdf(t - h, L, v, D)) / (2 * h)
        assert abs(numerical - pdf(t, L, v, D)) < 1e-7

    # Compare the exact ratio formula at 300 independent parameter settings.
    for _ in range(300):
        L = rng.uniform(0.6, 2.0)
        v1 = rng.uniform(0.1, 2.5)
        v2 = rng.uniform(0.1, 2.5)
        D1 = rng.uniform(0.4, 3.0)
        D2 = rng.uniform(0.4, 3.0)
        t = rng.uniform(0.1, 5.0)
        lhs = math.log(pdf(t, L, v1, D1) / pdf(t, L, v2, D2))
        rhs = log_density_ratio(t, L, v1, D1, v2, D2)
        assert abs(lhs - rhs) < 1e-12

    # A fixed pair with greater drift AND dispersion, yet one strict CDF crossover.
    L, D1, D2, v1, v2 = 1.0, 4.0, 1.0, 1.5, 1.0
    assert v1 > v2 and v1 * v1 / D1 < v2 * v2 / D2
    assert cdf(.05, L, v1, D1) > cdf(.05, L, v2, D2)
    assert cdf(10., L, v1, D1) < cdf(10., L, v2, D2)

    print('PASS: 300 CDF derivative, 300 density-ratio, 4 singular-limit, and illustrative crossover checks')


if __name__ == '__main__':
    run()
