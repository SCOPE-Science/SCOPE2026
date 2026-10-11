#!/usr/bin/env python3
"""Exact finite arithmetic stress tests for a parametric norm theorem.

The all-parameter proof is analytic. These rational examples check separate
polytope vertex and facet calculations without floating point operations.
"""
from fractions import Fraction as F
from itertools import product


def extreme_vertices(t):
    out = set()
    for u in product((-1, 1), repeat=3):
        if abs(sum(u)) <= t:
            out.add(tuple(map(F, u)))
    for fixed in range(3):
        for other in range(fixed + 1, 3):
            third = ({0, 1, 2} - {fixed, other}).pop()
            for a, b, sig in product((-1, 1), repeat=3):
                c = sig * t - a - b
                if abs(c) <= 1:
                    x = [F(0)] * 3
                    x[fixed], x[other], x[third] = F(a), F(b), c
                    out.add(tuple(x))
    return out


def Q(x, alpha):
    return sum(v * v for v in x) + alpha * sum(x) ** 2


def independent_maximum(t, alpha):
    return max(Q(v, alpha) for v in extreme_vertices(t))


def independent_minimum(t, alpha):
    # On a slab facet |sum x_i| = t, the constrained minimizer is (t/3)^3.
    slab = t * t * (alpha + F(1, 3))
    # On a cube facet x_1 = 1, averaging x_2,x_3 is optimal.
    lo = max(F(-1), (-t - 1) / 2)
    hi = min(F(1), (t - 1) / 2)
    unconstrained = -alpha / (1 + 2 * alpha)
    v = min(hi, max(lo, unconstrained))
    cube_facet = 1 + 2 * v * v + alpha * (1 + 2 * v) ** 2
    return min(slab, cube_facet)


def analytic_extrema(t, alpha):
    low = min(t * t * (alpha + F(1, 3)), (1 + 3 * alpha) / (1 + 2 * alpha))
    if t <= 1:
        high = 2 + (1 + alpha) * t * t
    else:
        high = max(3 + alpha, 2 + (t - 2) ** 2 + alpha * t * t)
    return high, low


def optimum(t):
    a1 = (3 - t * t) / (2 * t * t)
    if t <= 1 or 5 * t * t <= 9:
        return a1, 3 * (7 + t * t) / (9 - t * t) if t <= 1 else 3 * (5 * t * t + 3) / (t * t * (9 - t * t))
    if t <= 2:
        return F(1, 3), F(25, 9)
    return (3 - t) / (1 + t), (t + 3) * (7 - t) / ((t + 1) * (5 - t))


def main():
    ts = [F(1, 20), F(1, 4), F(1, 2), F(4, 5), F(1), F(6, 5), F(4, 3), F(7, 5), F(3, 2), F(7, 4), F(2), F(9, 4), F(5, 2), F(11, 4), F(3)]
    alphas = [F(-8, 25), F(-1, 4), F(-1, 8), F(0), F(1, 10), F(1, 3), F(1, 2), F(1), F(2), F(4), F(10), F(30)]
    checked = 0
    for t in ts:
        astar, want = optimum(t)
        assert astar > F(-1, 3)
        high, low = analytic_extrema(t, astar)
        assert high / low == want, (t, astar, high, low, want)
        for a in set(alphas + [astar]):
            if a <= F(-1, 3):
                continue
            M, L = analytic_extrema(t, a)
            independent_M, independent_L = independent_maximum(t, a), independent_minimum(t, a)
            assert M == independent_M, ('max', t, a, M, independent_M)
            assert L == independent_L, ('min', t, a, L, independent_L)
            assert M / L >= want, ('opt', t, a, M/L, want)
            checked += 1
    print('WEIGHTED_CYCLE_RATIONAL_CHECK_OK', checked)


if __name__ == '__main__':
    main()
