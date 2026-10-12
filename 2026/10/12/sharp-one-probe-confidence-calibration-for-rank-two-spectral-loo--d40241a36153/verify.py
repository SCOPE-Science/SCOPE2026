#!/usr/bin/env python3
"""Reproduce rank-two Gaussian look-ahead projection identities and numerical checks.

The analytic proof in RESULT.md, not the finite tests here, establishes the theorem.
Uses only Python standard library; run: python verify.py
"""
import math
import random
from fractions import Fraction


def ratio_sq(r, h1, h2):
    return (h1*h1 + r**4*h2*h2)/(h1*h1 + r*r*h2*h2)


def exact_probability(t, r):
    if r >= t:
        return 0.0
    return (2.0/math.pi)*math.atan(r*math.sqrt((t*t-r*r)/(1.0-t*t)))


def envelope(t):
    return (2.0/math.pi)*math.atan(t*t/(2.0*math.sqrt(1.0-t*t)))


def inverse_envelope(delta):
    c = math.tan(math.pi*delta/2.0)
    return math.sqrt(2.0*c*(math.sqrt(1+c*c)-c))


def run():
    exact_matrix_cases = 0
    algebraic_max_cases = 0
    for ii in range(1, 17):
        r = Fraction(ii, 20)
        for j in range(-7, 8):
            for k in range(-7, 8):
                if j == 0 and k == 0:
                    continue
                h1, h2 = Fraction(j, 5), Fraction(k, 7)
                # Independently reconstruct a non-diagonal 2-by-3 matrix
                # E=U diag(1,r) V^T, and compute ||q^T E||^2 directly.
                u1 = (Fraction(5, 13), Fraction(12, 13))
                u2 = (Fraction(-12, 13), Fraction(5, 13))
                v1 = (Fraction(3, 5), Fraction(4, 5), Fraction(0))
                v2 = (Fraction(-4, 5), Fraction(3, 5), Fraction(0))
                E = [[u1[i]*v1[c]+r*u2[i]*v2[c] for c in range(3)]
                     for i in range(2)]
                g3 = Fraction(j+2*k, 11)
                g = [h1*v1[c]+h2*v2[c]+g3*(1 if c==2 else 0)
                     for c in range(3)]
                y = [sum(E[i][c]*g[c] for c in range(3)) for i in range(2)]
                den_sq = sum(v*v for v in y)
                numer_sq = sum(sum(y[i]*E[i][c] for i in range(2))**2 for c in range(3))
                projection_sq = numer_sq/den_sq
                assert projection_sq == ratio_sq(r, h1, h2)
                assert r*r <= projection_sq <= 1
                exact_matrix_cases += 1
    for t_num in range(1, 20):
        t = Fraction(t_num, 20)
        for r_num in range(1, t_num):
            r = Fraction(r_num, 20)
            # Sharp maximizing identity; its difference is a square.
            left = (t**4)/4-r*r*(t*t-r*r)
            assert left == (r*r-(t*t)/2)**2
            assert left >= 0
            assert exact_probability(float(t), float(r)) <= envelope(float(t))+1.e-14
            algebraic_max_cases += 1
    for delta in (0.001, 0.005, 0.01, 0.05, 0.1, 0.25, 0.5, 0.9):
        t = inverse_envelope(delta)
        assert 0 < t < 1
        assert abs(envelope(t)-delta) <= 5.e-14
        assert abs(exact_probability(t, t/math.sqrt(2))-delta) <= 5.e-14
    assert abs(envelope(.5)-.09125789668597989) < 1.e-14
    rng = random.Random(20261010)
    trials = 170000
    results=[]
    for t in (0.25, 0.5, 0.75):
        r=t/math.sqrt(2)
        empirical=sum(ratio_sq(r,rng.gauss(0,1),rng.gauss(0,1))<t*t for _ in range(trials))/trials
        target=envelope(t)
        assert abs(empirical-target)<0.012
        results.append((t,round(empirical,6),round(target,6)))
    print('VERIFY_OK exact_rational_matrix_identities=',exact_matrix_cases,
          'exact_rational_sharpness_identities=',algebraic_max_cases,
          'calibration_cases=8 monte_carlo_trials=',3*trials,
          'frequency_pairs=',results)


if __name__=='__main__':
    run()
