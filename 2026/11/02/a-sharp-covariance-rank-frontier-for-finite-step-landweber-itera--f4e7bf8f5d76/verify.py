#!/usr/bin/env python3
"""Standalone checks of the Landweber finite-iteration covariance-rank theorem.

Uses only the Python standard library; finite checks supplement the written proof.
"""
import math
from fractions import Fraction


def f(k, t):
    return (1.0 - (1.0-t)**k)**2 / t


def stationary_equation(k, t):
    a = math.exp((k - 1) * math.log1p(-t))
    g = -math.expm1(k * math.log1p(-t))
    return 2 * k * t * a - g


def crossing(k):
    lo, hi = 1e-12 / k, 1.0 - 1e-12
    assert stationary_equation(k, lo) > 0
    assert stationary_equation(k, hi) < 0
    for _ in range(85):
        md = (lo + hi) * 0.5
        if stationary_equation(k, md) > 0:
            lo = md
        else:
            hi = md
    return (lo + hi) * 0.5


def madd(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def mmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mscale(s, a):
    return tuple(tuple(s*a[i][j] for j in range(2)) for i in range(2))


def flat_diff(a, b):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))


def check():
    checks = 0
    t2 = crossing(2)
    assert abs(t2 - 2/3) < 2e-14
    checks += 1
    t3 = crossing(3)
    assert abs(t3 - (9-math.sqrt(21))/10) < 2e-14
    checks += 1
    for k in range(2, 51):
        crit = crossing(k)
        assert 0 < crit < 1
        for j in range(1, 101):
            t = j / 101.0
            val = stationary_equation(k, t)
            assert ((val > 0) == (t < crit))
            checks += 1
    s_star = 1.2564312086261697
    for k in [100, 1000, 10000]:
        assert abs(k*crossing(k)-s_star) < 2.0/k
        checks += 1
    # Check spectral covariance against the literal Landweber noise recurrence.
    eye = ((1.0, 0.0), (0.0, 1.0))
    zero = ((0.0, 0.0), (0.0, 0.0))
    for k in range(2, 21):
        t = crossing(k)
        for eps in [0.01, 0.05, 0.2, 0.5]:
            hi, low = 2-eps, t
            # Orthogonal basis columns v_high=(1,1)/sqrt(2), v_low=(1,-1)/sqrt(2).
            B = ((.5*(hi+low), .5*(hi-low)), (.5*(hi-low), .5*(hi+low)))
            S = zero
            power = eye
            T = madd(eye, mscale(-1.0, B))
            for _ in range(k):
                S = madd(S, power)
                power = mmul(power, T)
            direct_cov = mmul(B, mmul(S, S))
            gamma_hi, gamma_lo = f(k, hi), f(k, low)
            spectral_cov = ((.5*(gamma_hi+gamma_lo), .5*(gamma_hi-gamma_lo)),
                            (.5*(gamma_hi-gamma_lo), .5*(gamma_hi+gamma_lo)))
            assert flat_diff(direct_cov, spectral_cov) < 2e-11 * (1 + max(gamma_hi, gamma_lo))
            checks += 1
    # Exact K=2 ratio and limiting asymptotic scale using rational arithmetic.
    for denominator in [10, 100, 1000, 10000]:
        eps = Fraction(1, denominator)
        u = 2-eps
        f_high = u*(2-u)**2
        f_low = Fraction(2,3)*(2-Fraction(2,3))**2
        ratio = f_low/f_high
        assert ratio == Fraction(32, 27)/(u*eps**2)
        assert ratio > 1
        checks += 2
    # Exact four-outcome Rademacher diagonal probe variance for each rank-one residual.
    for gamma in [Fraction(1, 2), Fraction(3, 7), Fraction(32, 27), Fraction(100, 1)]:
        for sign in [-1, 1]:
            obs = [gamma*Fraction(1+sign*z1*z2, 2)
                   for z1 in [-1, 1] for z2 in [-1, 1]]
            mean = sum(obs)/4
            var = sum((v-mean)**2 for v in obs)/4
            assert mean == gamma/2 and var == gamma**2/4
            checks += 1
    print('All supplementary checks passed:', checks)
    print('t_2 =', t2)
    print('t_3 =', t3)
    print('10000 t_10000 =', 10000*crossing(10000))
    print('The analytic manuscript, not the finite tests, proves universal statements.')


if __name__ == '__main__':
    check()
