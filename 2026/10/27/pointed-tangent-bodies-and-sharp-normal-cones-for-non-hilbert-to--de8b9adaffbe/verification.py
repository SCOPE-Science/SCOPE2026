"""Bounded, standard-library checks for the transversely normalized Toeplitz range.

The analytic proof establishes the cone threshold, uniqueness, and Hausdorff
rate. This program only checks numerical consequences at selected parameters.
"""

from math import cosh, exp, hypot, isclose, sinh, sqrt, tanh


def axes(delta, v):
    return (2 * cosh(delta * v) / cosh(v),
            (sinh(delta * v) / delta if delta else v) / cosh(v))


def from_weights(p, v):
    # Directly choose r^p/s^p = exp(2v) and normalize r^p+s^p to one.
    t = exp(-2 * v)
    r, s = (1 / (1 + t)) ** (1 / p), (t / (1 + t)) ** (1 / p)
    left, right = r * s ** (p - 1), s * r ** (p - 1)
    # The source range is twice the hull of the two-term expressions;
    # the normalization divides the imaginary coordinate by 2*delta.
    return 2 * (left + right), abs(left - right) / abs(1 - 2 / p)


def support_at(delta, a, b, v):
    x, y = axes(delta, v)
    return hypot(a * x, b * y)


def root(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    # Rescaling from the original r,s ellipses; verify both conjugate sides.
    for p in (1.2, 1.5, 1.9, 1.99, 1.999):
        q = p / (p - 1)
        delta = abs(1 - 2 / p)
        for v in (0., .05, .5, 1.2, 3., 8.):
            predicted = axes(delta, v)
            for exponent in (p, q):
                assert all(isclose(x, y, abs_tol=5e-12, rel_tol=5e-12)
                           for x, y in zip(predicted, from_weights(exponent, v)))

    # Test the exact boundary at fixed v, and a witness above the boundary.
    for delta in (0., .01, .2, .5, .8, .95):
        boundary = 2 * sqrt(1 - delta * delta)
        for v in (.02, .1, .3, .7, 1.2, 2., 6., 12.):
            assert support_at(delta, 1, boundary, v) < 2
        assert support_at(delta, 1, 1.03 * boundary, .05) > 2

    # Characterization of the nonzero maximizing v for several normals.
    for a, b in ((0., 1.), (.15, 1.), (.9, 2.), (1., 2.01), (2., 5.)):
        r2 = (2 * a / b) ** 2
        v = root(lambda z: r2 + z * z - z / tanh(z), 1e-6, 3.)
        h = support_at(0., a, b, v)
        assert h > 2 * abs(a)
        assert h > support_at(0., a, b, .98 * v)
        assert h > support_at(0., a, b, 1.02 * v)

    # The positive vertical excess has the predicted second-order coefficient.
    v = root(lambda z: z * tanh(z) - 1, .1, 3.)
    height = v / cosh(v)
    assert isclose(height, .6627434193491816, abs_tol=2e-14, rel_tol=0.)
    coefficient = v ** 3 / (6 * cosh(v))
    for delta in (.04, .02, .01, .005):
        assert isclose((axes(delta, v)[1] - height) / delta ** 2,
                       coefficient, rel_tol=3e-4)
    print(f'Finite normalized-ellipse, cone, and support checks passed; height={height:.15f}')


if __name__ == '__main__':
    main()
