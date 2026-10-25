#!/usr/bin/env python3
"""Reproduce a sharp two-direction phi_1-splitting bound.

Uses Python standard library only. Analytic proof of the universal theorem and
uniqueness is supplied in RESULT.md; numerical grids are supplementary.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from math import exp

CHECKS = 0


def check(test, what):
    global CHECKS
    if not test:
        raise AssertionError(what)
    CHECKS += 1


def exp_positive_bounds(x, terms=105):
    """Strict rational interval for exp(x), x>=0, from the Taylor tail."""
    check(x >= 0, 'positive input')
    term = Q(1)
    total = term
    for k in range(1, terms + 1):
        term *= x / k
        total += term
    nxt = term * x / (terms + 1)
    ratio = x / (terms + 2)
    check(0 <= ratio < 1, 'Taylor geometric remainder')
    return total, total + nxt / (1 - ratio)


def sum_intervals(*pairs):
    return (sum(z[0] for z in pairs), sum(z[1] for z in pairs))


def times_scalar(t, ab):
    l, u = ab
    return (t * l, t * u) if t >= 0 else (t * u, t * l)


def H_bounds(x):
    ex = exp_positive_bounds(x)
    ex2 = exp_positive_bounds(2*x)
    return sum_intervals(times_scalar(4-x, ex2),
                         times_scalar(-4*x-8, ex),
                         (2*x*x+5*x+4, 2*x*x+5*x+4))


def phi1_minus_bounds(x):
    ex_l, ex_u = exp_positive_bounds(x)
    return ((1 - 1/ex_l)/x, (1 - 1/ex_u)/x)


def cov(a, b):
    if a == 0 or b == 0:
        return 0.0
    phi = lambda x: -__import__('math').expm1(-x)/x
    return phi(a+b)-phi(a)*phi(b)


def var(a):
    return cov(a, a)


def main():
    left = Q('3.245304481708')
    right = Q('3.245304481710')
    L = H_bounds(left)
    R = H_bounds(right)
    check(L[0] > 0, 'H left positive by exact rational enclosure')
    check(R[1] < 0, 'H right negative by exact rational enclosure')

    # V(t)=phi1(-2t)-phi1(-t)^2. Two independent monotone
    # enclosures, valid for every t in the certified root interval.
    two_left = phi1_minus_bounds(2*left)
    two_right = phi1_minus_bounds(2*right)
    one_left = phi1_minus_bounds(left)
    one_right = phi1_minus_bounds(right)
    V_low = two_right[0] - one_left[1]**2
    V_high = two_left[1] - one_right[0]**2
    check(V_low > Q('0.066139893974'), 'constant certified lower bound')
    check(V_high < Q('0.066139893977'), 'constant certified upper bound')
    check(V_low < V_high, 'consistent exact enclosure')

    # Checks on a rational parameter mesh are consistency tests only;
    # the universal inequality is established by Cauchy--Schwarz.
    grid = [k/16 for k in range(1,161)]
    for a in grid:
        v = var(a)
        check(v > 0, 'strict positive variance')
        check(v < float(V_high) + 2e-15, 'universal candidate bound on mesh')
        for b in grid:
            c = cov(a,b)
            check(c > -2e-15, 'positive covariance mesh')
            check(c <= (var(a)*var(b))**0.5 + 2e-15,
                  'covariance Cauchy-Schwarz mesh')

    check(abs(var(3.2453044817087544)-0.06613989397537867)<2e-15,
          'attaining scalar example')
    for x in [3.0, 10.0, 20.0]:
        p1 = -__import__('math').expm1(-x)/x
        p2 = -__import__('math').expm1(-2*x)/(2*x)
        check(p1*p1/p2 < 2/x, 'vanishing relative captured fraction')

    with localcontext() as ctx:
        ctx.prec = 50
        print('Certified unique maximizer interval:',
              Decimal(left.numerator)/Decimal(left.denominator),
              Decimal(right.numerator)/Decimal(right.denominator))
        print('Certified sharp constant interval:',
              Decimal(V_low.numerator)/Decimal(V_low.denominator),
              Decimal(V_high.numerator)/Decimal(V_high.denominator))
    print('PASSED', CHECKS, 'checks')


if __name__ == '__main__':
    main()
