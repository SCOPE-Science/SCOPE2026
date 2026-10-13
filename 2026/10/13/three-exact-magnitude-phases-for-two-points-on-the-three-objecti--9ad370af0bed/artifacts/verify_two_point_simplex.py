#!/usr/bin/env python3
"""Exact-rational consistency checks for a two-point simplex magnitude formula."""
from fractions import Fraction as F
from random import Random


def mag(points):
    x, y = points
    meet = tuple(min(a, b) for a, b in zip(x, y))
    def volume_product(v):
        p = F(1)
        for t in v:
            p *= 2 + t
        return p
    return (volume_product(x) + volume_product(y) - volume_product(meet)) / 8


def optimizer(L):
    L = F(L)
    if L <= 2:
        a = (L, F(0), F(0))
        b = (F(0), L / 2, L / 2)
        optimum = (L * L + 16 * L + 16) / 16
    elif L <= F(16, 5):
        a = ((L + 4) / 3, (L - 2) / 3, (L - 2) / 3)
        b = (F(0), L / 2, L / 2)
        optimum = (L + 4) ** 2 * (2 * L + 35) / 432
    else:
        a = ((11 * L + 20) / 23, (6 * L - 10) / 23, (6 * L - 10) / 23)
        b = ((5 * L - 16) / 23, (9 * L + 8) / 23, (9 * L + 8) / 23)
        optimum = F(27, 4232) * (L + 6) ** 3
    return (a, b), optimum


def parametrized(B, C, E, u, v):
    return ((B + u + v, C, E), (B, C + u, E + v))


def analytic_j(B, W, L):
    q = B + 2
    r = 2 + (L - B - W) / 2
    return (q + W) * r ** 2 + q * W * r + q * W ** 2 / 4


def main():
    scales = [F(k, 7) for k in range(1, 210)] + [F(2), F(16,5), F(31,10), F(33,10), F(100)]
    rng = Random(29174)
    tests = 0
    for L in scales:
        points, limit = optimizer(L)
        assert all(min(p) >= 0 and sum(p) == L for p in points)
        assert points[0] != points[1]
        assert mag(points) == limit, (L, points, mag(points), limit)
        for _ in range(75):
            a, b, c, d, e = [F(rng.randrange(101), 100) for j in range(5)]
            S = a + b + c + d + e
            if not S: continue
            B, C, E, u, v = [L * z / S for z in (a,b,c,d,e)]
            pair = parametrized(B, C, E, u, v)
            observed = mag(pair)
            assert observed <= limit, (L, pair, observed, limit)
            W = u + v
            center = (C + E) / 2
            cd = (C - E) / 2
            wd = (u - v) / 2
            penalty = (B + 2 + W) * cd ** 2 + 2 * (B + 2) * cd * wd + (B + 2) * wd ** 2
            assert 8 * observed == analytic_j(B, W, L) - penalty
            assert penalty >= 0
            tests += 1
    for L in [F(1,3), F(2), F(10,3), F(16,5), F(30)]:
        for B in [F(0),L/3,L/2,2*L/3,L]:
            Wstar = min(L-B, (L-B+4)/3)
            assert analytic_j(B,Wstar,L) >= analytic_j(B,F(0),L)
            assert analytic_j(B,Wstar,L) >= analytic_j(B,L-B,L)
    print('VERIFY_OK', 'rational_sample_comparisons', tests, 'scales', len(scales))

if __name__ == '__main__':
    main()
