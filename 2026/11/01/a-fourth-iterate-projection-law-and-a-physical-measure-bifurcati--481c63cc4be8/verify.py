#!/usr/bin/env python3
"""Exact rational checks for a resonant piecewise-affine planar map.

All computations use Python's standard-library Fraction. The universal
claims are established in the accompanying proof, not by these grids.
"""
from fractions import Fraction as Q
from itertools import product


def f(mu, z):
    x, y = z
    return (mu + y, -max(x, 0))


def iterate(mu, z, n):
    for _ in range(n):
        z = f(mu, z)
    return z


def clip(t, a, b):
    return min(max(t, a), b)


def projected(mu, z):
    x, y = z
    if mu <= 0:
        return (mu, Q(0))
    return (clip(x, Q(0), mu), clip(y, -mu, Q(0)))


def main():
    checks = 0
    for mu in map(Q, (-4, -1, 0, 1, 2, 5)):
        for den in (1, 2, 3, 5):
            for ix, iy in product(range(-17, 18, 2), repeat=2):
                z = (Q(ix, den), Q(iy, den))
                w = projected(mu, z)
                assert iterate(mu, z, 4) == w
                assert iterate(mu, z, 8) == w
                assert iterate(mu, z, 12) == w
                assert iterate(mu, w, 4) == w
                checks += 4
        if mu > 0:
            center = (mu / 2, -mu / 2)
            assert f(mu, center) == center
            corners = ((Q(0), Q(0)), (mu, Q(0)),
                       (mu, -mu), (Q(0), -mu))
            for j in range(4):
                assert f(mu, corners[j]) == corners[(j + 1) % 4]
                checks += 1
            z = (mu / 2, mu)
            assert iterate(mu, z, 3) not in ((Q(0), Q(0)),)
            assert not (Q(0) <= iterate(mu, z, 3)[0] <= mu and
                        -mu <= iterate(mu, z, 3)[1] <= Q(0))
            checks += 1
        else:
            z = (Q(0), Q(10))
            assert iterate(mu, z, 3) != (mu, Q(0))
            checks += 1
    print(f'PASS: {checks} exact rational identities and boundary witnesses')


if __name__ == '__main__':
    main()
