"""Supplementary finite checks of beta-sampling OLS moment boundaries.

Runs on Python 3.10+ standard library; the analytic theorem is in RESULT.md.
"""
import math


def gamma(n, a, b):
    return min(n - 1, n * a, n * b)


def arcsine_range(n, r, panels=160000):
    # Integrate after x = sin(theta)^2 to remove beta endpoint density.
    h = math.pi / (2 * panels)
    s = 0.0
    for j in range(panels):
        theta = (j + 0.5) * h
        x = math.sin(theta) ** 2
        delta = (2 / math.pi) * (math.asin(math.sqrt(min(1., x + r))) - theta)
        s += delta ** (n - 1)
    return n * (2 / math.pi) * s * h


def uniform_range(n, r):
    return n * r ** (n - 1) - (n - 1) * r ** n


def midpoint_uniform_integral(n, r, panels=100000):
    h = 1 / panels
    z = 0.0
    for j in range(panels):
        x = (j + 0.5) * h
        z += min(r, 1 - x) ** (n - 1)
    return n * z * h


def main():
    for n in range(2, 10):
        for r in (0.03, 0.12, 0.6):
            a = uniform_range(n, r)
            b = midpoint_uniform_integral(n, r)
            assert abs(a - b) < 2e-6, (n, r, a, b)
    assert gamma(4, 1., 1.) == 3
    assert gamma(4, 0.5, 0.5) == 2
    assert gamma(5, 0.5, 0.5) == 2.5
    for n in range(4, 21):
        for a in (0.15, 0.5, 0.9, 1., 3.):
            for b in (0.18, 0.5, 1., 2.):
                g = gamma(n, a, b)
                assert (2 < g) == (n > 3 and n * a > 2 and n * b > 2)
    target = 48 / math.pi ** 4
    radii = (0.01, 0.002, 0.0005)
    ratios = [arcsine_range(4, r) / (r * r) for r in radii]
    assert all(ratios[i] > ratios[i + 1] > target for i in range(len(ratios) - 1))
    assert abs(ratios[-1] / target - 1) < 0.004
    print('VERIFY_OK uniform_identity=24 grid_thresholds=340 arcsine_ratios=',
          [round(t, 8) for t in ratios], 'limit=', round(target, 8))


if __name__ == '__main__':
    main()
