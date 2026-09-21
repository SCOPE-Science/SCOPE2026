"""Numerically check the sharp fixed-(perimeter, side-deficit) area profiles.

The script uses only the Python standard library. It parameterizes the circle of
triangle-inequality slacks having prescribed first and second moments and checks
that the sampled spherical and hyperbolic areas lie in the claimed interval.
"""
import math


def tau(kind, t):
    if kind == "hyperbolic":
        return math.tanh(t / 2.0)
    if kind == "spherical":
        return math.tan(t / 2.0)
    raise ValueError(kind)


def area_from_slacks(kind, s, x, y, z):
    q = tau(kind, s) * tau(kind, x) * tau(kind, y) * tau(kind, z)
    return 4.0 * math.atan(math.sqrt(max(q, 0.0)))


def predicted(kind, p, X):
    """Return (lower_or_None, upper) for X=Q/p^2."""
    s = p / 2.0
    m = p / 6.0
    u = math.sqrt(2.0 * X)
    upper_product = tau(kind, m * (1.0 + 2.0 * u)) * tau(kind, m * (1.0 - u)) ** 2
    upper = 4.0 * math.atan(math.sqrt(tau(kind, s) * upper_product))
    lower = None
    if u < 0.5:
        lower_product = tau(kind, m * (1.0 - 2.0 * u)) * tau(kind, m * (1.0 + u)) ** 2
        lower = 4.0 * math.atan(math.sqrt(tau(kind, s) * lower_product))
    return lower, upper


def sampled_areas(kind, p, X, n=24000):
    s = p / 2.0
    m = s / 3.0
    Q = X * p * p
    V = Q / 3.0
    radius = math.sqrt(V)
    e1 = (1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0), 0.0)
    e2 = (1.0 / math.sqrt(6.0), 1.0 / math.sqrt(6.0), -2.0 / math.sqrt(6.0))
    vals = []
    for j in range(n):
        t = 2.0 * math.pi * j / n
        c, q = math.cos(t), math.sin(t)
        d = [radius * (c * e1[i] + q * e2[i]) for i in range(3)]
        xyz = [m + di for di in d]
        if min(xyz) > 0.0:
            vals.append(area_from_slacks(kind, s, *xyz))
    return vals


def main():
    cases = [
        ("hyperbolic", 4.2, 0.02),
        ("hyperbolic", 4.2, 0.10),
        ("hyperbolic", 4.2, 0.13),
        ("hyperbolic", 4.2, 0.30),
        ("spherical", 4.2, 0.02),
        ("spherical", 4.2, 0.10),
        ("spherical", 4.2, 0.13),
        ("spherical", 4.2, 0.30),
    ]
    # p=4.2<2*pi in spherical cases.
    tolerance = 2e-7
    for kind, p, X in cases:
        lower, upper = predicted(kind, p, X)
        vals = sampled_areas(kind, p, X)
        observed_min, observed_max = min(vals), max(vals)
        if observed_max > upper + tolerance:
            raise AssertionError((kind, X, observed_max, upper))
        if lower is not None and observed_min < lower - tolerance:
            raise AssertionError((kind, X, observed_min, lower))
        # The symmetric extremizer occurs on the parameter circle and the grid is
        # chosen fine enough that the sampled maximum is very close to the formula.
        if abs(observed_max - upper) > 2e-6:
            raise AssertionError((kind, X, observed_max, upper))
        if lower is not None and abs(observed_min - lower) > 2e-6:
            raise AssertionError((kind, X, observed_min, lower))
    print("PASS: sampled spherical and hyperbolic profiles agree with the formulas.")


if __name__ == "__main__":
    main()
