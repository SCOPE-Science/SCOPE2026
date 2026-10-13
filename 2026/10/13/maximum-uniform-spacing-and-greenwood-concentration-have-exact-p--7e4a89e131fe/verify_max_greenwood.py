#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial


def H(m, r=1):
    return sum((Fraction(1, k**r) for k in range(1, m+1)), Fraction(0))


def beta_int(a, b):
    # Integral_0^1 y^(a-1)(1-y)^(b-1) dy for positive integers a,b.
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def intersection_integral(m, k):
    # Integral of E[G 1{D_1>x,...,D_k>x}] over x in [0,1/k],
    # evaluated term-by-term after y=kx.
    t1 = Fraction(1, k*k) * beta_int(3, m)
    t2 = Fraction(2, m*k) * beta_int(2, m+1)
    t3 = Fraction(2, (m+1)*k) * beta_int(1, m+2)
    return t1 + t2 + t3


def closed_intersection_integral(m, k):
    return Fraction(2, k*m*(m+2)) + Fraction(2, k*k*m*(m+1)*(m+2))


def mixed_from_inclusion(m):
    return sum(((-1)**(k+1) * comb(m,k) * intersection_integral(m,k)
                for k in range(1,m+1)), Fraction(0))


def mixed_closed(m):
    h=H(m); h2=H(m,2)
    return Fraction(2, m*(m+2))*h + Fraction(1, m*(m+1)*(m+2))*(h*h+h2)


def cov_closed(m):
    h=H(m); h2=H(m,2)
    return (h*h+h2-2*h) / (m*(m+1)*(m+2))


def var_largest_closed(m):
    h=H(m); h2=H(m,2)
    return (m*h2-h*h) / (m*m*(m+1))


def var_greenwood_closed(m):
    return Fraction(4*(m-1), (m+1)*(m+1)*(m+2)*(m+3))


def run():
    intersection_checks=0
    mixed_checks=0
    covariance_checks=0
    variance_checks=0
    positivity_checks=0
    increment_checks=0

    for m in range(2, 101):
        for k in range(1,m+1):
            assert intersection_integral(m,k) == closed_intersection_integral(m,k)
            intersection_checks += 1
        mix=mixed_from_inclusion(m)
        assert mix == mixed_closed(m)
        mixed_checks += 1
        h=H(m); eg=Fraction(2,m+1); el=h/Fraction(m,1)
        assert mix-el*eg == cov_closed(m)
        covariance_checks += 1

        # Independent moment reconstruction of both marginal variances.
        e_l2=(h*h+H(m,2))/Fraction(m*(m+1),1)
        assert e_l2-el*el == var_largest_closed(m)
        e_g2=Fraction(4*(m+5),(m+1)*(m+2)*(m+3))
        assert e_g2-eg*eg == var_greenwood_closed(m)
        variance_checks += 2

    h=Fraction(1); h2=Fraction(1); prev=Fraction(0)
    for m in range(2, 1001):
        h += Fraction(1,m); h2 += Fraction(1,m*m)
        f=h*h+h2-2*h
        assert f>0
        positivity_checks += 1
        if m>2:
            # F_m-F_{m-1}=2(H_m-1)/m.
            assert f-prev == Fraction(2,m)*(h-1)
            increment_checks += 1
        prev=f

    print(
        'VERIFY_OK '
        f'intersection_checks={intersection_checks} '
        f'mixed_checks={mixed_checks} '
        f'covariance_checks={covariance_checks} '
        f'variance_checks={variance_checks} '
        f'positivity_checks={positivity_checks} '
        f'increment_checks={increment_checks}'
    )

if __name__=='__main__':
    run()
