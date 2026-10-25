#!/usr/bin/env python3
"""Independent standard-library survivor inversion checks for the fixed-parameter Holling-II assay theorem."""
import math
import random


def survivor(n0, t, c, h):
    # Invert t = c log(n0/n) + h(n0-n). All parameters strictly positive.
    lo, hi = n0 * math.exp(-min(t/c, 700.0)), n0
    # Exact solution is at least n0*exp(-t/c).
    for _ in range(110):
        mid = (lo + hi) / 2.0
        reach_time = c * math.log(n0 / mid) + h * (n0 - mid)
        if reach_time > t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def threshold(c1, c2, h1, h2, t):
    nc = (c1-c2)/(h2-h1)
    q = c1+h1*nc
    s = t/q
    return nc*s/(-math.expm1(-s))


def run():
    rng = random.Random(451972)
    for j in range(700):
        c2 = rng.uniform(0.2, 2.0)
        c1 = c2+rng.uniform(0.05, 1.2)
        h1 = rng.uniform(0.04, 0.6)
        h2 = h1+rng.uniform(0.05, 1.0)
        nc = (c1-c2)/(h2-h1)
        q = c1+h1*nc
        t = q*rng.uniform(0.04, 5.0)
        crit = threshold(c1, c2, h1, h2, t)
        common = crit*math.exp(-t/q)
        n1 = survivor(crit, t, c1, h1)
        n2 = survivor(crit, t, c2, h2)
        assert math.isclose(n1, common, rel_tol=4e-12, abs_tol=5e-14), (j,n1,common)
        assert math.isclose(n2, common, rel_tol=4e-12, abs_tol=5e-14), (j,n2,common)
        for ratio, expected in [(0.75, -1), (1.35, 1)]:
            n0 = crit*ratio
            capture_diff = survivor(n0, t, c2, h2) - survivor(n0, t, c1, h1)
            assert expected*capture_diff > 0, (j, ratio, capture_diff)
    c1, c2, h1, h2, t = 1.0, 0.5, 0.2, 0.6, 2.0
    exact_thr = 2.0 / (1-math.exp(-1.6))
    assert abs(threshold(c1,c2,h1,h2,t)-exact_thr)<1e-12
    assert abs(exact_thr-2.5059407020437066)<1e-12
    def b(s):return s/(-math.expm1(-s))
    for s in [1e-3, 2e-3, 5e-3]:
        approx = 1+s/2+s*s/12
        assert abs(b(s)-approx)<s**4/600
    print('PASS: 700 random tradeoffs, 1400 strict comparisons, 1400 equality inversions, exact example, small-duration series')


if __name__=='__main__':
    run()
