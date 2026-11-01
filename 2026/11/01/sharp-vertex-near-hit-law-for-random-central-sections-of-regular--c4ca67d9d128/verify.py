#!/usr/bin/env python3
"""Deterministic finite diagnostics of the regular-simplex section-radius theorem."""
import math, random


def planar_cdf(eps):
    assert 0 <= eps <= 2/3
    root = math.sqrt(max(0.0, 1 - 4*eps/3))
    k = (1-root)/(1+root)
    s = (math.sqrt(3)*k/2)/math.sqrt(1-k+k*k)
    return 6/math.pi*math.asin(max(-1,min(1,s)))


def deficit(heights, d):
    best = 0.0
    c = 2*(d+1)/d
    for i in range(d+1):
        for j in range(i+1,d+1):
            if heights[i]*heights[j] < 0:
                t = abs(heights[i])/(abs(heights[i])+abs(heights[j]))
                r2 = 1-c*t*(1-t)
                best = max(best, r2)
    assert best >= 0.0
    return 1-best


def gaussian_sample(d, rng):
    h = [rng.gauss(0,1) for _ in range(d+1)]
    avg = sum(h)/(d+1)
    return [x-avg for x in h]


def run():
    rng = random.Random(82043)
    assert planar_cdf(0.0) == 0.0
    assert abs(planar_cdf(2/3)-1) < 5e-15
    assert abs(planar_cdf(0.5)-0.5)<5e-14
    for eps in [0.001,0.01,0.1]:
        k = (1-math.sqrt(1-4*eps/3))/(1+math.sqrt(1-4*eps/3))
        assert abs(eps-3*k/(1+k)**2)<1e-12
    for e in [0.05,0.2,0.5,0.65]:
        observed = 0
        total = 80000
        for j in range(total):
            observed += (deficit(gaussian_sample(2,rng),2) <= e)
        exact = planar_cdf(e)
        assert abs(observed/total-exact)<0.012,(e,observed/total,exact)
    c3 = 3*math.sqrt(6)/(2*math.pi)
    for eps in [0.01,0.02]:
        observed = 0
        total = 140000
        for j in range(total):
            observed += (deficit(gaussian_sample(3,rng),3) <= eps)
        expected = c3*eps
        assert abs(observed/total-expected)<0.0035,(eps,observed/total,expected)
    print('PASS: planar exact endpoint/half-mass/algebra, Monte Carlo in dimensions 2 and 3, sharp first-order coefficient.')

if __name__ == '__main__':
    run()
