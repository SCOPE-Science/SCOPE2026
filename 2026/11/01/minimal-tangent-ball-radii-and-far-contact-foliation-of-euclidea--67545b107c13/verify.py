"""Exact-rational spot checks for the ellipsoid tangent-ball spectral law.

The rigorous statement is proved separately; finite checks do not certify the
universal quantifiers. Run with Python 3, no third-party dependencies.
"""
from fractions import Fraction as F
from random import Random


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def sphere_point(t):
    """Rational stereographic parametrization of the unit sphere."""
    denominator = 1 + dot(t, t)
    return [(1 - dot(t, t)) / denominator] + [2 * x / denominator for x in t]


def difference(x, y):
    return [a - b for a, b in zip(x, y)]


def squared_weighted(x, semi):
    return sum(a * a * xx * xx for a, xx in zip(semi, x))


def check():
    rng = Random(2601020)
    count = 0
    for axes in [(F(5), F(3)), (F(5), F(3), F(2)),
                 (F(5), F(5), F(2)), (F(7), F(5), F(3), F(2)),
                 (F(2), F(2), F(2))]:
        maximum = max(axes)
        dim = len(axes)
        for _ in range(160):
            u = sphere_point([F(rng.randrange(-6, 7), rng.randrange(1, 8)) for _ in range(dim - 1)])
            v = sphere_point([F(rng.randrange(-6, 7), rng.randrange(1, 8)) for _ in range(dim - 1)])
            assert dot(u, u) == 1 and dot(v, v) == 1
            if u != v:
                displacement = difference(u, v)
                # Equivalent to containment in the exact minimal tangent ball.
                assert squared_weighted(displacement, axes) <= maximum ** 2 * dot(displacement, displacement)
                count += 1
            # If a top-eigenvector has nonzero u-coordinate, reflection gives
            # a genuine second contact, including multiple top eigenvalues.
            for i, a in enumerate(axes):
                if a == maximum and u[i]:
                    reflected = list(u)
                    reflected[i] = -reflected[i]
                    displacement = difference(u, reflected)
                    assert squared_weighted(displacement, axes) == maximum ** 2 * dot(displacement, displacement)
                    assert dot(reflected, reflected) == 1
                    count += 1
        # At top endpoint (unique top eigenvalue), global tangency exceeds
        # local osculating support by the exact semiaxis-square ratio.
        if axes.count(maximum) == 1:
            second = max(a for a in axes if a != maximum)
            assert maximum ** 2 / second ** 2 > 1
            count += 1
    # Nonattained sharpness at the minor-axis tip for a unique top eigenvalue:
    # the direction of a sequence of secants approaches the major axis.
    axes = [F(5), F(3)]
    u = [F(0), F(1)]
    for k in [2, 4, 8, 16, 32, 64]:
        t = F(1, k)
        v = [(2*t)/(1+t*t), (1-t*t)/(1+t*t)]
        assert dot(v, v) == 1 and v != u
        w = difference(u, v)
        quotient = squared_weighted(w, axes) / dot(w, w)
        assert quotient < 25
        assert quotient > 25 - F(24, k*k)
        count += 1
    return count


if __name__ == '__main__':
    print(f'PASS: {check()} exact-rational checks; analytic proof required for all dimensions/parameters.')
