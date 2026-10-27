#!/usr/bin/env python3
"""Exact finite-state validation for the coupon-cover singleton calculations."""
from fractions import Fraction
from functools import lru_cache
from math import log, sqrt, exp, pi


def harmonic(n, p=1):
    return sum((Fraction(1, j**p) for j in range(1, n+1)), Fraction(0))


def state_moments(n):
    @lru_cache(None)
    def moments(unseen, once):
        if unseen == 0:
            raise ValueError('terminal state must be handled at transition')
        den = unseen + once
        if unseen == 1:
            a, a2, at = (Fraction(once+1), Fraction((once+1)**2), Fraction(0))
        else:
            a, a2, at = moments(unseen - 1, once + 1)
        if once:
            b, b2, bt = moments(unseen, once - 1)
        else:
            b = b2 = bt = Fraction(0)
        es = (unseen*a + once*b)/den
        es2 = (unseen*a2 + once*b2)/den
        ets = (n*es + unseen*at + once*bt)/den
        return es, es2, ets
    return moments(n, 0)


def check_exact():
    for n in range(2, 15):
        mean_s, second_s, mixed = state_moments(n)
        h, h2 = harmonic(n), harmonic(n, 2)
        assert mean_s == h, (n,'mean', mean_s,h)
        assert mixed - n*h*h == n*(h2-h), (n,'mixed', mixed-n*h*h)
        if n >= 3:
            fm2 = 2*((h-Fraction(3,2))**2 + h2-Fraction(5,4))
            proposed_second_s = 1+3*(h-1)+fm2  # S=1+B, S^2=1+3B+B(B-1)
            assert second_s == proposed_second_s, (n,'second',second_s,proposed_second_s)
        print('EXACT_STATE_PASS',n,str(mean_s),str(mixed))


def check_asymptotic():
    for n in (100,1000,10000,100000):
        h = sum(1.0/j for j in range(1,n+1))
        h2 = sum(1.0/(j*j) for j in range(1,n+1))
        fm2 = 2*((h-1.5)**2 + h2-1.25)
        var_s = 1 + 3*(h-1)+fm2-h*h
        var_t = n*n*h2 -n*h
        cov = n*(h2-h)
        rho = cov/sqrt(var_s*var_t)
        assert var_s > 0 and var_t>0 and cov < 0
        assert abs(var_s/log(n)**2-1)<0.35
        assert abs(rho + sqrt(6)/pi)<0.13
        print('ASYMPTOTIC_DIAGNOSTIC',n,round(var_s/log(n)**2,6),round(rho,6))

if __name__=='__main__':
    check_exact()
    check_asymptotic()
    print('VERIFY_OK')
