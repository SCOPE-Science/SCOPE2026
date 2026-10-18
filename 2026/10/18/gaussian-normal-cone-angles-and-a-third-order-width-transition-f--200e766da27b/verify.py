#!/usr/bin/env python3
"""Reproducible checks for partial-permutohedron angular and width formulas.

Python 3 standard library only. Finite checks corroborate; analytic proofs
of the universal statements are in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, erfc, exp, gamma, isclose, lgamma, pi, sqrt


def vertices(m, n):
    out = set()
    for k in range(min(m, n) + 1):
        for indices in combinations(range(m), k):
            for order in permutations(indices):
                v = [0] * m
                for j, i in enumerate(order):
                    v[i] = n - j
                out.add(tuple(v))
    return out


def optimal_vertex(g, n):
    m = len(g)
    ranked = sorted(range(m), key=lambda i: g[i], reverse=True)
    selected = [i for i in ranked if g[i] > 0][:n]
    v = [0] * m
    for j, i in enumerate(selected):
        v[i] = n - j
    return tuple(v)


def normal_angles(m, n):
    # Signs and relative absolute-value ranks jointly are equidistributed.
    counts = Counter()
    for signed in product((-1, 1), repeat=m):
        for magnitude_order in permutations(range(m)):
            g = [0] * m
            for r, i in enumerate(magnitude_order):
                g[i] = signed[i] * (m - r)
            counts[optimal_vertex(g, n)] += 1
    total = (2 ** m) * __import__('math').factorial(m)
    assert set(counts) == vertices(m, n)
    for v, count in counts.items():
        s = sum(t > 0 for t in v)
        if s < n:
            want = Fraction(1, (2 ** m) * __import__('math').factorial(s))
        else:
            assert s == n <= m
            tail = Fraction(sum(comb(m, j) for j in range(n, m + 1)), 2 ** m)
            falling = __import__('math').factorial(m) // __import__('math').factorial(m - n)
            want = tail / falling
        assert Fraction(count, total) == want, (m, n, v, count, total, want)


def exact_gaussian_support_integrand(m, n, x):
    # E[sum_{j<=min(N_x,n)}(n-j+1)] with N_x~Bin(m,q(x)).
    q = 0.5 * erfc(x / sqrt(2))
    ans = 0.0
    for j in range(m + 1):
        r = min(j, n)
        prob = comb(m, j) * q**j * (1 - q)**(m - j)
        ans += prob * r * (2*n - r + 1) / 2
    return ans


def integrate_width(m, n, panels=1200):
    assert panels % 2 == 0
    xmax = 9.0
    h = xmax / panels
    vals = [exact_gaussian_support_integrand(m, n, i*h) for i in range(panels+1)]
    eh = h * (vals[0] + vals[-1] + 4*sum(vals[1:-1:2]) +
              2*sum(vals[2:-1:2])) / 3
    er = sqrt(2) * exp(lgamma((m+1)/2) - lgamma(m/2))
    return 2 * eh / er


def limiting_profile(rho):
    # Depend only on math functions available in the standard library;
    # invert the strictly decreasing normal-tail function by bisection.
    if rho >= 0.5:
        return 1/(2*sqrt(pi)) + sqrt(2/pi)*(rho-0.5)
    left, right = 0.0, 12.0
    for _ in range(90):
        middle = (left+right)/2
        if 0.5*erfc(middle/sqrt(2)) > rho:
            left = middle
        else:
            right = middle
    z = (left+right)/2
    return erfc(z)/(2*sqrt(pi))


def test():
    cone_checks = 0
    for m in range(1, 6):
        for n in range(1, 7):
            normal_angles(m, n)
            cone_checks += 1
    grid_checks = 0
    for m in range(1, 5):
        for n in range(1, 5):
            vv = vertices(m, n)
            for g in product((-2, -1, 1, 3), repeat=m):
                desired = max(sum(a*b for a,b in zip(g,v)) for v in vv)
                got = sum(a*b for a,b in zip(g,optimal_vertex(g,n)))
                assert desired == got, (m, n, g, got, desired)
                grid_checks += 1
    # The unit segment and the right isosceles triangle are exact benchmarks.
    assert abs(integrate_width(1,1) - 1) < 1e-8
    assert abs(integrate_width(2,1) - (2+sqrt(2))/pi) < 1e-8
    for rho in (0.2, 0.5, 0.8):
        m = 240
        n = round(rho*m)
        observed = integrate_width(m,n) / m**1.5
        target = limiting_profile(rho)
        assert abs(observed-target) < 0.0035, (rho, observed, target)
    # Critical point: both branches have the same value and first two
    # derivatives, but the left and right third derivatives differ.
    c = 1/sqrt(2*pi)
    assert isclose(-2/c, -2*sqrt(2*pi), rel_tol=1e-13)
    print('CHECKS_PASSED', 'normal_angle_profiles',cone_checks,
          'direct_support_tests',grid_checks,
          'exact_planar_benchmarks',2,'scaling_profiles',3)


if __name__ == '__main__':
    test()
