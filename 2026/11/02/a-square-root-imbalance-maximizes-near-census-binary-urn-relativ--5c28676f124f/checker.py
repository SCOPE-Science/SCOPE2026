#!/usr/bin/env python3
"""Independent finite-distribution checks of the near-census binary-urn divergence identity.

This program verifies finite examples only. The all-size asymptotics require the
Stirling expansion and localization argument supplied in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb, sqrt


def fraction_as_decimal(value):
    return Decimal(value.numerator) / Decimal(value.denominator)


def log_factorials(n):
    a = [Decimal(0)] * (n + 1)
    for j in range(2, n + 1):
        a[j] = a[j - 1] + Decimal(j).ln()
    return a


def formula(n, j, lf):
    p = Decimal(j) / Decimal(n)
    q = 1 - p
    log_binomial_mass = lf[n] - lf[j] - lf[n-j] + j*p.ln() + (n-j)*q.ln()
    return -log_binomial_mass + p*p.ln() + q*q.ln()


def direct(n, j):
    p = Fraction(j, n)
    q = 1 - p
    k = n - 1
    ans = Decimal(0)
    for x in (j-1, j):
        h = p if x == j-1 else q
        b = Fraction(comb(k,x)) * p**x * q**(k-x)
        ans += fraction_as_decimal(h) * (fraction_as_decimal(h) / fraction_as_decimal(b)).ln()
    return ans


def run():
    with localcontext() as ctx:
        ctx.prec = 75
        exact_checks = 0
        for n in range(3, 17):
            lf = log_factorials(n)
            for j in range(1, n):
                p = Fraction(j,n)
                q = 1-p
                k = n-1
                left = Fraction(comb(k,j))*p**j*q**(k-j)
                right = Fraction(comb(k,j-1))*p**(j-1)*q**(k-j+1)
                mode = Fraction(comb(n,j))*p**j*q**(n-j)
                assert left == right == mode, (n,j)
                exact_checks += 1
                delta = abs(direct(n,j)-formula(n,j,lf))
                assert delta < Decimal('1e-65'), (n,j,delta)
                exact_checks += 1
                assert abs(formula(n,j,lf) - formula(n,n-j,lf)) < Decimal('1e-65')
                exact_checks += 1
        print('Exact rational probability identities and high-precision KL equalities:', exact_checks)
        print('n, maximizing small color class, standardized imbalance, n^2 gain over most balanced class')
        for n in (50, 51, 100, 101, 200, 400, 401, 800, 801):
            lf = log_factorials(n)
            values = [formula(n,j,lf) for j in range(1,n//2+1)]
            jstar = 1 + max(range(len(values)), key=lambda idx: values[idx])
            standardized = (Decimal(n)/2 - Decimal(jstar)) / Decimal(n).sqrt()
            gain = (values[jstar-1] - values[-1]) * n * n
            assert Decimal('.35') < standardized < Decimal('.7')
            assert Decimal('.13') < gain < Decimal('.19')
            print(n, jstar, str(standardized)[:18], str(gain)[:18])
        print('Finite checks passed; no numerical experiment is used as proof of the limit.')

if __name__ == '__main__':
    run()
