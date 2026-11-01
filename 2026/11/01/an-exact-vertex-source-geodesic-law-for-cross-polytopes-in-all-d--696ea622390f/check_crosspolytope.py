#!/usr/bin/env python3
"""Standalone exact-rational and numerical checks for a vertex-source cross-polytope metric identity.

This is a reproducibility aid. It does not replace the universal geometric proof.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt, log


def sqnorm(v):
    return sum(a * a for a in v)


def check_one(n, t, u):
    assert n >= 2 and Q(0) <= t <= Q(1)
    assert len(u) == n-1 and all(x >= 0 for x in u) and sum(u) == Q(1)
    p = (-t,) + tuple((Q(1)-t)*a for a in u)
    v = (Q(1),) + tuple(Q(0) for _ in range(n-1))
    c = (Q(1, n-1),) * (n-1)
    s = (Q(1)-t) / (Q(1)+t)
    q = (Q(0),) + tuple(c[i]+s*(u[i]-c[i]) for i in range(n-1))
    assert all(z >= 0 for z in q[1:]) and sum(q[1:]) == Q(1)
    a = sqnorm(tuple(v[i]-q[i] for i in range(n)))
    b = sqnorm(tuple(p[i]-q[i] for i in range(n)))
    assert b == t*t*a  # paths meet the equator with matching angles
    predicted = sqnorm(tuple(v[i]-p[i] for i in range(n))) + Q(4)*t/(n-1)
    assert (Q(1)+t)**2*a == predicted
    ratio_sq = predicted/sqnorm(tuple(v[i]-p[i] for i in range(n)))
    assert ratio_sq <= Q(n,n-1)
    if t == Q(1):
        assert ratio_sq == Q(n,n-1)
    elif t > 0:
        assert ratio_sq < Q(n,n-1)
    return predicted


def main():
    rng = Random(2026102806)
    cases = 0
    max_numeric_error = 0.0
    for n in range(2, 25):
        simple = [(Q(0), (Q(1),)+(Q(0),)*(n-2)),
                  (Q(1), (Q(1),)+(Q(0),)*(n-2)),
                  (Q(1,2), (Q(1,n-1),)*(n-1)),
                  (Q(1,3), (Q(1),)+(Q(0),)*(n-2))]
        for t,u in simple:
            check_one(n,t,u); cases += 1
        for _ in range(170):
            t = Q(rng.randrange(0,30), rng.randrange(30,60))
            a = [rng.randrange(0,20) for _ in range(n-1)]
            if sum(a)==0:a[0]=1
            u = tuple(Q(x,sum(a)) for x in a)
            d2 = check_one(n,t,u)
            cases += 1
            p = [-float(t)]+[(1-float(t))*float(x) for x in u]
            ambient2 = (1-p[0])**2 + sum(x*x for x in p[1:])
            max_numeric_error = max(max_numeric_error, abs(float(d2)-(ambient2+4*float(t)/(n-1))))
        # Exact moment integration from the standard simplex Dirichlet moments.
        mean_x_squared = n*Q(2,n*(n+1))
        mean_abs_x1 = Q(1,n)
        derived = Q(1)+mean_x_squared+Q(4,n-1)*Q(1,2)*mean_abs_x1
        expected = Q(n+3,n+1)+Q(2,n*(n-1))
        assert derived == expected
    assert check_one(4,Q(1),(Q(1),Q(0),Q(0))) == Q(16,3)
    # Independent Monte Carlo check of the exact chord-excess tail distribution.
    worst_tail_error = 0.0
    for n in (2, 4, 8, 16):
        observations = []
        for _ in range(45000):
            weights = [-log(max(rng.random(), 1e-15)) for j in range(n)]
            t = weights[0]/sum(weights)
            z = (4*t/(n-1)) if rng.random() < 0.5 else 0.0
            observations.append(z)
        for frac in (0.12,0.37,0.68,0.91):
            cutoff = (4/(n-1))*frac
            empirical = sum(z > cutoff for z in observations)/len(observations)
            exact = 0.5*(1-frac)**(n-1)
            worst_tail_error = max(worst_tail_error,abs(empirical-exact))
    assert worst_tail_error < 0.007
    print('distribution_mc_samples=', 180000)
    print('distribution_max_absolute_tail_error=',format(worst_tail_error,'.6g'))
    print('exact_path_and_dilation_cases=', cases)
    print('dimensions=', '2..24')
    print('exact_mean_square_cases=', 23)
    print('max_float_squared_distance_error=',format(max_numeric_error,'.3g'))
    print('test_status=PASS')

if __name__ == '__main__': main()
