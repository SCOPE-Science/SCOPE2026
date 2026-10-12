from math import exp, gamma


def density(x, a, d, p):
    return p * x ** (d - 1) * exp(-(x / a) ** p) / (a ** d * gamma(d / p))


def w0(z):
    lo, hi = -1.0, 0.0
    for _ in range(120):
        mid = (lo + hi) / 2
        if mid * exp(mid) < z:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def wm1(z):
    lo, hi = -2.0, -1.0
    while lo * exp(lo) <= z:
        lo *= 2
    for _ in range(180):
        mid = (lo + hi) / 2
        if mid * exp(mid) > z:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def level_points(a, d, p, y):
    assert a > 0 and d > 1 and p > 0 and 0 < y < 1
    m = a * ((d - 1) / p) ** (1 / p)
    z = -exp(-1) * y ** (p / (d - 1))
    lo = m * (-w0(z)) ** (1 / p)
    hi = m * (-wm1(z)) ** (1 / p)
    return lo, m, hi


cases = [
    (2.0, 3.0, 1.5, 0.5),
    (1.2, 5.0, 0.7, 0.3),
    (3.0, 2.0, 4.0, 0.8),
    (1.0, 1.5, 2.0, 0.5),
]

for a, d, p, y in cases:
    lo, m, hi = level_points(a, d, p, y)
    fm = density(m, a, d, p)
    assert lo < m < hi
    assert abs(density(lo, a, d, p) / fm - y) < 1e-12
    assert abs(density(hi, a, d, p) / fm - y) < 1e-12

print("verification passed")
