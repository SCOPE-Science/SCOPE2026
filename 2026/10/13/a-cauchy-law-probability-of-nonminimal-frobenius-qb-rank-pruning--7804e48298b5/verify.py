#!/usr/bin/env python3
"""Reproduce exact algebraic identities and numerical checks of a QB rank-pruning law.

Uses the Python standard library only. Experiments supplement, not prove,
claims about continuous probability distributions and limiting behavior.
"""
from fractions import Fraction
import math
import random


def probability(epsilon, c):
    tau = c * epsilon
    u = (tau*tau - epsilon*epsilon) / (1 - epsilon*epsilon)
    assert 0 < u < 0.5
    lo = math.sqrt(u / (1-u)) / epsilon
    hi = math.sqrt((1-u) / u) / epsilon
    return (2/math.pi)*(math.atan(hi) - math.atan(lo))


def rational_check():
    cases = 0
    for j in range(1, 101):
        eps = Fraction(j, 400)
        for c2 in [Fraction(5, 4), Fraction(3, 2), Fraction(2), Fraction(3)]:
            tau2 = c2 * eps * eps
            assert tau2 < (1 + eps*eps) / 2
            u = (tau2-eps*eps)/(1-eps*eps)
            for x, y in [(1, 0), (0, 1), (1, 1), (2, 3), (-3, 4), (5, -7)]:
                x, y = Fraction(x), Fraction(y)
                den = x*x + eps*eps*y*y
                s = eps*eps*y*y / den
                w1 = (x*x + eps**4*y*y) / den
                w2 = eps*eps*(x*x+y*y) / den
                assert w1 == 1-(1-eps*eps)*s
                assert w2 == eps*eps+(1-eps*eps)*s
                assert w1+w2 == 1+eps*eps
                keep_two = min(w1, w2) >= tau2
                assert keep_two == (u <= s <= 1-u)
                # A rank-one spectral rotation has exact error eps < tau.
                assert eps*eps < tau2 < 1
                cases += 1
    return cases


def direct_cauchy_integral(eps, c):
    tau = c*eps
    u = (tau*tau-eps*eps)/(1-eps*eps)
    a = math.sqrt(u/(1-u))/eps
    b = math.sqrt((1-u)/u)/eps
    # Midpoint integration in the angular coordinate: dP = (2/pi) dtheta.
    N = 10000
    lo, hi = math.atan(a), math.atan(b)
    step = (hi-lo)/N
    return sum((2/math.pi)*step for _ in range(N))


def monte_carlo(eps, c, seed=673421, trials=180000):
    rng = random.Random(seed)
    tau2 = (c*eps)**2
    nr = ne = nj = 0
    for _ in range(trials):
        x1, x2 = rng.gauss(0,1), rng.gauss(0,1)
        y1, y2 = rng.gauss(0,1), rng.gauss(0,1)
        den = x1*x1+eps*eps*y1*y1
        w1 = (x1*x1+eps**4*y1*y1)/den
        w2 = eps*eps*(x1*x1+y1*y1)/den
        rank_two = min(w1,w2) >= tau2
        passes_first = (x1*x1+x2*x2+eps*eps*(y1*y1+y2*y2)) / 2 > tau2
        nr += rank_two
        ne += not passes_first
        nj += rank_two and passes_first
    return nr/trials, ne/trials, nj/trials


def main():
    n = rational_check()
    checks = 0
    for c in [1.01,1.1,math.sqrt(2),1.7,2.5]:
        for eps in [0.0005, 0.005, 0.03, 0.1]:
            if (2*c*c-1)*eps*eps >= 1:
                continue
            p = probability(eps,c)
            assert abs(p-direct_cauchy_integral(eps,c)) < 1e-10
            checks += 1
        e = 1e-7
        limiting = (2/math.pi)*math.atan(1/math.sqrt(c*c-1))
        assert abs(probability(e,c)-limiting) < 1e-5
    e = 0.03
    c = math.sqrt(2)
    pr, pf, pj = monte_carlo(e,c)
    p = probability(e,c)
    bound = 1-math.exp(-c*c*e*e)
    assert abs(pr-p) < 0.015
    assert abs(pj-p) < 0.015
    assert pj <= pr and 0 <= pr-pj <= bound + 0.006
    assert pf <= bound + 0.006
    assert abs(pj-0.5) < 0.018
    print('VERIFY_OK rational_row_identities=',n,
          'cauchy_integrals=', checks,
          'lookahead_simulations=',180000,
          'p_exact=',round(p,6),
          'p_joint_empirical=',round(pj,6))


if __name__ == '__main__':
    main()
