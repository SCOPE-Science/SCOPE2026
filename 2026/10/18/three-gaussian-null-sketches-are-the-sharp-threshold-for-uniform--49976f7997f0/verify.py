#!/usr/bin/env python3
"""Reproduce exact checks for undersketched Gaussian null-vector residuals.

Requires Python >=3.9 standard library only. The analytical theorem, not
these finite checks, establishes the universal claims.
"""
from fractions import Fraction
import math
import random


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def normsq(z):
    return sum(v*v for v in z)


def exact_witness():
    a = 5
    g1 = (1, 2, 3)
    g2 = (2, -1, 4)
    u = cross(g1, g2)
    ga1 = (a*g1[0], a*g1[1], g1[2])
    ga2 = (a*g2[0], a*g2[1], g2[2])
    v = cross(ga1, ga2)
    av = (a*v[0], a*v[1], v[2])
    r = Fraction(normsq(av), normsq(v))
    t = Fraction(u[2]*u[2], normsq(u))
    assert r == Fraction(a*a, 1+(a*a-1)*t) == Fraction(5,1)
    return r


def numerical_integral(f, num=120000):
    # Composite midpoint integration, avoiding singular endpoints.
    return sum(f((i+.5)/num) for i in range(num))/num


def finite_expectation(n, k, kap):
    # n=3: sqrt(T) is uniform on [0,1], and its maximum has density k*u^(k-1).
    d = kap*kap-1
    return numerical_integral(lambda u:k*u**(k-1)*kap*kap/(1+d*u*u))


def exact_n3(k, kap):
    d = kap*kap-1
    if d == 0:
        return 1.
    if k == 1:
        return kap*kap*math.atan(math.sqrt(d))/math.sqrt(d)
    if k == 2:
        return kap*kap*math.log(1+d)/d
    if k == 3:
        return 3*kap*kap/d*(1-math.atan(math.sqrt(d))/math.sqrt(d))
    raise ValueError('exact expressions provided only for k=1,2,3')


def randomized_matrix_check():
    rng = random.Random(47271)
    kappa = 4.
    runs = 35000
    vals = []
    for _ in range(runs):
        chosen = float('inf')
        for j in range(3):
            g1 = [rng.gauss(0, 1) for _ in range(3)]
            g2 = [rng.gauss(0, 1) for _ in range(3)]
            u = cross(g1, g2)
            v = cross((kappa*g1[0], kappa*g1[1], g1[2]),
                      (kappa*g2[0], kappa*g2[1], g2[2]))
            direct = normsq((kappa*v[0], kappa*v[1], v[2]))/normsq(v)
            t = u[2]*u[2]/normsq(u)
            predicted = kappa*kappa/(1+(kappa*kappa-1)*t)
            assert abs(direct-predicted) < 3e-11
            chosen = min(chosen, direct)
        vals.append(chosen)
    empirical = sum(vals)/runs
    exact = exact_n3(3, kappa)
    assert abs(empirical-exact) < 0.055, (empirical, exact)
    return empirical, exact


def main():
    exact_witness()
    comparisons=0
    for k in (1,2,3):
        for kap in (1., 1.5, 2., 4., 10.):
            a=finite_expectation(3, k, kap)
            b=exact_n3(k, kap)
            assert abs(a-b) < 0.00011, (k, kap, a, b)
            comparisons+=1
    for kap in (10., 100., 1000.):
        assert exact_n3(3,kap)<3
        assert exact_n3(1,kap)>1
    for k in (3,4,5,8):
        # n=3 limiting formula E M^{-2}=k/(k-2), M=max k uniforms.
        assert abs(numerical_integral(lambda u:k*u**(k-3))-k/(k-2))<0.0002
    empirical, theory=randomized_matrix_check()
    print('VERIFY_OK exact_fraction_witness=1 exact_n3_formula_quadratures=',comparisons,
          'limit_checks=3 threshold_integrals=4 random_matrix_sketches=105000',
          'mc_mean=',round(empirical,7),'theory=',round(theory,7))

if __name__=='__main__':
    main()
