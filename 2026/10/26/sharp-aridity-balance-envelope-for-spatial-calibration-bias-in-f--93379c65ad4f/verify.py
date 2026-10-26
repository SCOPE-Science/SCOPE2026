#!/usr/bin/env python3
"""Reproducible checks for a two-input hydrological water-balance identity.

Finite tests complement, but do not replace, the analytic proof.
"""
import math
import random


def norm(exp, p, d):
    return (p ** exp + d ** exp) ** (1.0 / exp)


def fitted(exp, precip, demand):
    p, d = sum(precip), sum(demand)
    target = sum(norm(exp, x, y) for x, y in zip(precip, demand))
    low, high = 1.0, exp
    assert norm(low, p, d) + 2e-12 >= target
    assert norm(high, p, d) - 2e-12 <= target
    for _ in range(84):
        mid = (low + high) / 2.0
        if norm(mid, p, d) > target:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def bias_coefficient(exp, p, d, a, u, v):
    z = p ** exp / (p ** exp + d ** exp)
    entropy = -z * math.log(z) - (1.0 - z) * math.log1p(-z)
    mismatch = sum((ui - vi) ** 2 / ai for ai, ui, vi in zip(a, u, v))
    return exp * exp * (exp - 1.0) * z * (1.0 - z) * mismatch / (2.0 * entropy)


def main():
    rng = random.Random(20261024)
    for case in range(6000):
        exp = rng.uniform(1.15, 4.5)
        p = math.exp(rng.uniform(-0.6, 0.6))
        d = math.exp(rng.uniform(-0.6, 0.6))
        n = rng.randrange(2, 7)
        a = [rng.uniform(0.25, 1.5) for _ in range(n)]
        b = [rng.uniform(0.25, 1.5) for _ in range(n)]
        aa, bb = sum(a), sum(b)
        a = [x / aa for x in a]
        b = [x / bb for x in b]
        wh = fitted(exp, [p*x for x in a], [d*x for x in b])
        assert 1.0 - 1e-11 < wh <= exp + 1e-11, (case, wh, exp)
        z = p ** exp / (p ** exp + d ** exp)
        entropy = -z * math.log(z) - (1-z) * math.log(1-z)
        assert z*(1-z)/entropy <= 1.0/(4.0*math.log(2)) + 2e-14

    for exp in (1.3, 2.0, 3.7):
        for share in (0.14, 0.38, 0.75):
            for ratio in (0.3, 1.0, 2.6):
                assert abs(fitted(exp, [share, 1-share],
                                  [ratio*share, ratio*(1-share)]) - exp) < 2e-12

    n_local = 0
    a = [0.20, 0.35, 0.45]
    u = [0.20, -0.10, -0.10]
    v = [-0.10, 0.05, 0.05]
    for exp in (1.25, 1.8, 2.0, 3.5):
        for ratio in (0.25, 1.0, 4.0):
            p, d = 1.0, ratio
            coefficient = bias_coefficient(exp, p, d, a, u, v)
            for eps in (0.006, 0.003):
                pp = [p*(ai+eps*ui) for ai, ui in zip(a,u)]
                dd = [d*(ai+eps*vi) for ai, vi in zip(a,v)]
                measured = (exp-fitted(exp, pp, dd))/(eps*eps)
                assert abs(measured/coefficient-1) < 0.04, (exp, ratio, eps, measured, coefficient)
                n_local += 1

    for exp in (1.4, 2.2, 4.0):
        for b in (0.20, 0.45, 0.73):
            grid = [b*t for t in (0.1, 0.4, 0.7, 1.0)] + [b+(1-b)*t for t in (0.3,0.6,0.9)]
            fitted_grid = [fitted(exp, [1.2*a,1.2*(1-a)], [0.8*b,0.8*(1-b)]) for a in grid]
            assert all(fitted_grid[j] < fitted_grid[j+1] - 1e-12 for j in range(3))
            assert all(fitted_grid[j] > fitted_grid[j+1] + 1e-12 for j in range(3,6))
            assert abs(fitted_grid[3]-exp) < 2e-12

    aggregate = (math.sqrt(61.0)+math.sqrt(41.0))/10.0
    exact = math.log(2.0)/math.log(aggregate)
    obtained = fitted(2.0, [0.6,0.4], [0.5,0.5])
    assert abs(exact-obtained) < 2e-12
    assert abs(exact-1.971418157337623) < 3e-12
    assert abs(bias_coefficient(2.0, 1.0, 1.0, [0.5,0.5], [1,-1], [0,0])
               -2.0/math.log(2.0)) < 1e-12
    print('PASS: 6000 pooled-fit configurations; 27 proportional-equality cases;')
    print(f'      {n_local} second-order asymptotic checks; 9 strict two-region monotonicity grids;')
    print('      6000 entropy inequalities; exact radical benchmark and sharp coefficient.')
    print(f'exact example fitted exponent: {exact:.15f}')


if __name__ == '__main__':
    main()
