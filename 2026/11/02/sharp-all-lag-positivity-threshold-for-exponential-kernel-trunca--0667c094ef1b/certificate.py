#!/usr/bin/env python3
"""Exact rational certificate for positivity of exponential-kernel TTR2 CQ weights.

This script uses only the Python standard library. It checks the finite
Bernstein-coefficient and interval assertions needed by the analytic proof;
it does not replace the infinite-tail Chebyshev and Pringsheim arguments.
"""
from fractions import Fraction as F
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        out[i] += v
    for i, v in enumerate(q):
        out[i] += v
    return trim(out)


def scale(p, c):
    return trim([c * v for v in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def evaluate(p, x):
    y = F(0)
    for a in reversed(p):
        y = y*x + a
    return y


def derivative(p):
    return [p[i]*i for i in range(1, len(p))] or [F(0)]


def bernstein(p, left, right):
    """Convert the power polynomial p(r) to degree-d Bernstein on [left,right]."""
    d = len(p) - 1
    width = right - left
    q = [sum((p[j] * comb(j, k) * left**(j-k) * width**k for j in range(k, d+1)), F(0)) for k in range(d+1)]
    return [sum((q[k] * F(comb(i, k), comb(d, k)) for k in range(i+1)), F(0)) for i in range(d+1)]


def test():
    a = [F(5,3), F(1)]
    b = F(5,2)
    p = [[F(1)], [b], add([b*b], scale(a, -1))]
    for n in range(3, 31):
        p.append(add(add(scale(p[-1], b), scale(mul(a, p[-2]), -1)), scale(mul(mul(a,a),p[-3]), F(1,6))))

    g = [F(1667125), F(-2997300), F(1440720), F(-154656), F(1296)]
    assert p[6] == scale(g, F(1,46656)), 'sixth coefficient polynomial'
    checks = 1
    for n, poly in enumerate(p):
        if n == 6:
            continue
        coefficients = bernstein(poly, F(4,5), F(9333,10000))
        assert all(v > 0 for v in coefficients), ('Bernstein coefficient failure', n)
        checks += len(coefficients)

    deriv = bernstein(derivative(g), F(4,5), F(15,16))
    assert all(v < 0 for v in deriv)
    checks += len(deriv)
    assert evaluate(g, F(9332,10000)) > 0
    assert evaluate(g, F(9333,10000)) < 0
    checks += 2
    s = F(24933,10000)
    rr = s*s-6*s+15
    assert s*s/rr < F(997,1000)**2
    assert s**3-6*s*s+15*s-10-6*F(9333,10000) > 0
    assert F(997,1000)**32 * F(11,10) < 1
    assert F(885,1000)**4 * F(14,10) < 1
    assert F(67,100) / F(36,100) < F(14,10)**2
    checks += 5
    # The r<=4/5 part has 0.3<=rho<=0.885, .7<=c<=.8,
    # as shown analytically in RESULT.md. The root s(4/5) is bounded
    # by a rational point for exact rho upper control.
    root_bound = F(2263,1000)
    f_at_bound = root_bound**3-6*root_bound**2+15*root_bound-10-6*F(4,5)
    assert f_at_bound > 0
    assert root_bound**2/(root_bound**2-6*root_bound+15) < F(885,1000)**2
    checks += 2
    print('PASS: %s exact-rational positivity and boundary checks' % checks)
    print('Certified: P_n positive for n<=30 (except n=6) on [4/5,9333/10000]')
    print('Certified: P_6=g/46656, g decreasing on [4/5,15/16]')
    print('Certified: threshold interval (0.9332,0.9333), tail rational bounds')
    return checks


if __name__ == '__main__':
    test()
