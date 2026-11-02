#!/usr/bin/env python3
"""Exact finite checks for a symmetric slab-truncated cross-polytope.

The theorem is analytical; this script checks representative rational cases.
Run with Python 3, with no third-party dependencies.
"""
from fractions import Fraction as F
from itertools import product


def theoretical(n, tau):
    assert n >= 2 and tau >= 1
    p = tau * tau
    t = F(n) * (p - 1) / (n*n - (n % 2))
    if n % 2 == 0:
        target = F(n+2, 2) + F(n-2, 2) / p
    else:
        target = F(n) * (n*n*p + n*n + 2*n*p - 2*n - p - 1) / (2*(n*n*p - 1))
    return t, target


def raw_objective(n, tau, t):
    """Exact product of the two squared radial extrema for I+t*11^T."""
    assert t > F(-1, n)
    q = F(1, tau)
    vertices = []
    if tau == 1:
        for i in range(n):
            for sgn in (-1, 1):
                x = [F(0)] * n
                x[i] = F(sgn)
                vertices.append(tuple(x))
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for h in (-1, 1):
                    x = [F(0)] * n
                    x[i] = (1+h*q)/2
                    x[j] = -(1-h*q)/2
                    vertices.append(tuple(x))
    above = max(sum(xi*xi for xi in x) + t*sum(x)**2 for x in vertices)
    signs = product((-1, 1), repeat=n)
    inv_one = max(F(n) - t*sum(s)**2/(1+n*t) for s in signs)
    inv_mean = tau*tau*n/(1+n*t)
    below = max(inv_one, inv_mean)
    return above*below, above, below


def run():
    count = 0
    for n in range(2, 12):
        for tau in (F(1), F(11, 10), F(3, 2), F(2), F(3), F(7)):
            t, target = theoretical(n, tau)
            observed, above, below = raw_objective(n, tau, t)
            assert observed == target, (n, tau, observed, target)
            assert observed <= F(n), (n, tau)
            assert observed == F(n) if tau == 1 or n == 2 else observed < F(n)
            count += 1
            # Rational probe of all symmetric quadratic pullbacks within range.
            for t0 in (F(-1, 2*n), F(0), t/3, 2*t/3, t, 3*t/2, 2*t, t+1, t+20):
                if t0 > F(-1, n):
                    val, _, _ = raw_objective(n, tau, t0)
                    assert val >= target, (n,tau,t0,val,target)
                    count += 1
    print('CHECK_OK exact_slab_cases=', 60, 'exact_parameter_comparisons=', count)


if __name__ == '__main__':
    run()
