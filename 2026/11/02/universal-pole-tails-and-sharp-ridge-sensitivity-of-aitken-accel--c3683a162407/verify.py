#!/usr/bin/env python3
"""Exact rational checks and finite sampling for a Gaussian trace Aitken pole law."""
from fractions import Fraction
from math import comb, factorial, pi, isclose
from random import Random


def polynomial_integral(p):
    # Exact integral_0^3 (1-u)^p (3-u) du, for nonnegative integer p.
    return sum((Fraction((-1)**k * comb(p, k) * 3**(k+2),
                         (k+1)*(k+2)) for k in range(p+1)), Fraction(0))


def exact_J(p, lam=Fraction(1,2)):
    # Gamma integral_0^infty y^(p+2) exp(-4 lam y) dy.
    return lam**4 * polynomial_integral(p) * factorial(p+2) / (4*lam)**(p+3)


def aitken(x,y,z,w):
    m1=x
    m2=(x+y)/2
    m4=(x+y+z+w)/4
    return m1-(m2-m1)**2/(m4-2*m2+m1)


def main():
    assert polynomial_integral(2) == Fraction(9,4)
    assert polynomial_integral(4) == Fraction(27,10)
    assert exact_J(2) == Fraction(27,256)
    assert exact_J(4) == Fraction(243,256)
    assert 2*exact_J(2) == Fraction(27,128)
    assert isclose(pi*float(exact_J(4))/2,243*pi/512,rel_tol=1.e-14)
    for a in ((1.,2.,3.,4.),(.5,2.,.75,5.),(8.,3.,1.,9.)):
        x,y,z,w=a
        assert isclose(aitken(*a), x-(y-x)**2/(x-3*y+z+w),rel_tol=1e-13)
    rng=Random(251023)
    n=350000
    t=30.
    tail_count=0
    ridge_sq=0.
    delta=.08
    for j in range(n):
        x,y,z,w=(rng.expovariate(.5) for _ in range(4))
        H=x-3*y+z+w
        B=(y-x)**2
        raw=x-B/H
        if abs(raw-2.)>t:
            tail_count+=1
        softened=x-B*H/(H*H+delta*delta)
        ridge_sq+=(softened-2.)**2
    tail=t*tail_count/n
    ridge=delta*ridge_sq/n
    assert abs(tail-27/128)<.05, (tail,27/128)
    assert abs(ridge-243*pi/512)<.6, (ridge,243*pi/512)
    print('VERIFY_OK exact_J2=27/256 exact_J4=243/256',
          'tail_tP=%.6f'%tail,'ridge_delta_MSE=%.6f'%ridge,
          'draws=%d'%n)

if __name__ == '__main__':
    main()
