#!/usr/bin/env python3
"""Finite standard-library sanity checks for the displayed mathematical theorem.

No randomness from external sources, external packages, internet, or source files.
These checks corroborate but do not certify the analytic proof.
"""
import math
import random


def S(n, x):
    return sum((1.0 - x) ** j for j in range(n))


def choose(n, c, r, delta, alpha, beta, u):
    k = c * (1.0 - r / n)
    h = u / (1.0 + u)
    aa = lambda x: k / (delta * S(n, x))
    d0 = k / (n * beta)
    d1 = k / (beta * S(n, h))
    d2 = k / (alpha * S(n, h))
    d3 = k / alpha
    assert 0 < d0 < d1 < d2 < d3
    if delta <= d0:
        return 0.0, beta, (d0, d1, d2, d3)
    if delta < d1:
        target, lo, hi = beta, 0.0, h
    elif delta <= d2:
        return h, aa(h), (d0, d1, d2, d3)
    elif delta < d3:
        target, lo, hi = alpha, h, 1.0
    else:
        return 1.0, alpha, (d0, d1, d2, d3)
    for _ in range(110):
        mid = 0.5 * (lo + hi)
        if aa(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), target, (d0, d1, d2, d3)


def test_case(n, c, r, delta, alpha, beta, u, epsilon, gen):
    xe, ae, thresholds = choose(n, c, r, delta, alpha, beta, u)
    h = u / (1.0 + u)
    k = c * (1.0 - r / n)
    for _ in range(20):
        x = gen.uniform(0.00001, 0.99999)
        a = alpha + (beta - alpha) * gen.uniform(0.00001, 0.99999)
        p = (delta / epsilon) * x * (1 - x) * S(n, x)
        q = (a - alpha) * (beta - a)
        ad = lambda y: k / (delta * S(n, y))
        original_dx = x * (1 - x) * (-k + a * delta * S(n, x)) / epsilon
        factored_dx = p * (a - ad(x))
        original_da = q * (u * (1 - x) - x)
        factored_da = (1 + u) * q * (h - x)
        tol = 2e-10 * max(1.0, abs(original_dx), abs(original_da))
        assert abs(original_dx - factored_dx) < tol
        assert abs(original_da - factored_da) < tol
        vd_1 = (1 + u) * ((x - xe) * (a - ad(x)) + (a - ae) * (h - x))
        vd_2 = (1 + u) * ((x - xe) * (ae - ad(x)) + (a - ae) * (h - xe))
        vd_3 = (1 + u) * (-(x - xe) * (ad(x) - ad(xe))
                            + (x - xe) * (ae - ad(xe)) + (a - ae) * (h - xe))
        assert abs(vd_1 - vd_2) < tol * 20
        assert abs(vd_2 - vd_3) < tol * 20
        assert vd_1 < tol * 20, (vd_1, n, delta, x, a)
    assert abs(xe * (1-xe) * (-k + ae * delta * S(n, xe))) < 1e-9
    assert abs((ae - alpha) * (beta - ae) * (h - xe)) < 1e-9
    return thresholds


def main():
    g = random.Random(137)
    count = 0
    for n in (2, 3, 5, 8, 13):
        for _ in range(120):
            c = g.uniform(.2, 3.0)
            r = g.uniform(1.0001, n - .0001)
            alpha = g.uniform(.03, 1.0)
            beta = alpha + g.uniform(.02, 6.0)
            u = math.exp(g.uniform(-3, 3))
            epsilon = math.exp(g.uniform(-4, 4))
            k = c * (1 - r/n)
            h = u/(1+u)
            thresholds = (k/(n*beta), k/(beta*S(n,h)),
                          k/(alpha*S(n,h)), k/alpha)
            probes = [g.uniform(thresholds[0]/10, thresholds[3]*10),
                      *thresholds,
                      .5*(thresholds[0]+thresholds[1]),
                      .5*(thresholds[1]+thresholds[2]),
                      .5*(thresholds[2]+thresholds[3])]
            for delta in probes:
                test_case(n,c,r,delta,alpha,beta,u,epsilon,g)
                count += 1
            ordered = sorted([thresholds[0]/10, *thresholds,
                              thresholds[3]*10])
            out = [choose(n,c,r,d,alpha,beta,u)[:2] for d in ordered]
            for (x0,a0),(x1,a1) in zip(out,out[1:]):
                assert x0 <= x1+1e-10 and a0 >= a1-1e-10
    print('PASS: %d regimes including threshold equality; symbolic identities and monotone predictions checked numerically' % count)


if __name__ == '__main__':
    main()
