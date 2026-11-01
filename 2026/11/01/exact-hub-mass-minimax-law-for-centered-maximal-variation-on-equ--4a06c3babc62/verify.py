#!/usr/bin/env python3
"""Exact-rational finite checks for the centered mass-weighted star maximal operator.

The theorem for all real inputs and all positive masses is proved analytically;
these tests are independent evaluations of the original graph-ball definition.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt


def maximal_on_star(f, q):
    """Vertex 0 has mass q; vertices 1,...,m have mass 1."""
    m = len(f) - 1
    h = q
    v = [abs(a) for a in f]
    global_average = (h * v[0] + sum(v[1:])) / (h + m)
    ans = [max(v[0], global_average)]
    for leaf in v[1:]:
        pair_average = (h * v[0] + leaf) / (h + 1)
        ans.append(max(leaf, pair_average, global_average))
    return ans


def variation(f):
    return sum(abs(z - f[0]) for z in f[1:])


def bound(m, q):
    return max(1 - 1 / (q + m), 1 / (q + 1))


def check_all():
    comparisons = 0
    for m in [3, 4, 5, 6]:
        for q in [Q(1, 10), Q(1, 3), Q(1, 2), Q(1), Q(2), Q(7)]:
            b = bound(m, q)
            for coords in product(range(3), repeat=m + 1):
                f = list(map(Q, coords))
                var = variation(f)
                if not var:
                    continue
                z = maximal_on_star(f, q)
                assert variation(z) <= b * var, (m, q, coords, z)
                comparisons += 1
            leaf = [Q(0), Q(1)] + [Q(0)] * (m - 1)
            center = [Q(1)] + [Q(0)] * m
            assert variation(maximal_on_star(leaf, q)) / variation(leaf) == 1 - 1 / (q + m)
            assert variation(maximal_on_star(center, q)) / variation(center) == 1 / (q + 1)
            comparisons += 2
    for m in range(3, 41):
        q_star = (sqrt((m - 1)**2 + 4) - (m - 1)) / 2
        assert abs((1 - 1/(m + q_star)) - 1/(1 + q_star)) < 5e-14
        for ratio in [0.99, 1.01, 0.1, 3.0]:
            if ratio == 0.99 or ratio == 1.01:
                x = q_star * ratio
            else:
                x = q_star * ratio
            assert max(1 - 1/(m + x), 1/(1 + x)) > 1/(1 + q_star) - 1e-13
            comparisons += 1
    return comparisons

if __name__ == '__main__':
    n = check_all()
    print('PASS:', n, 'independent graph-ball and optimal-parameter checks')
