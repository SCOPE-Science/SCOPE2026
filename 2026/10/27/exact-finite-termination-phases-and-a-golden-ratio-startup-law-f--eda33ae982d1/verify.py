#!/usr/bin/env python3
"""Reproducibility checks for the exact-arithmetic AdaBB scalar-mode theorem.

The calculations below are finite consistency tests. The all-parameter and
asymptotic statements are justified by the accompanying analytic proof.
"""
from decimal import Decimal, localcontext
from random import Random


def d(s):
    return Decimal(str(s))


def normalized_termination(a, theta, max_steps=4000):
    """Return the first state index K at which the exact step is a=1.

    Decimal arithmetic avoids catastrophic cancellation in the high-startup
    examples; away from switching boundaries this agrees with exact algebra.
    """
    one = Decimal(1)
    two = Decimal(2)
    for k in range(max_steps):
        if a == one:
            return k + 1
        old = a
        if a < one:
            theta_next = (one + theta).sqrt()
            a = old * theta_next
            theta = theta_next
        elif a < two:
            a = one
            theta = two / old - one
        else:
            a = one / two.sqrt()
            theta = a / old
    raise AssertionError("precision, scope, or termination failure")


def informed_initialization(a):
    two = Decimal(2)
    if a <= 1 / two.sqrt():
        return 1 / (two * a * a) - 1
    return Decimal(0)


def predicted_class(a):
    one = Decimal(1)
    two = Decimal(2)
    b = 1 / (Decimal(7) * two.sqrt())
    c = 1 / two.sqrt()
    if a <= b:
        return 7
    if a < c:
        return 4
    if a == c:
        return 3
    if a < one:
        return 4
    if a == one:
        return 1
    if a < two:
        return 2
    return 5


def product_hitting_time(a, cap=4000):
    t = Decimal(0)
    value = a
    for j in range(1, cap + 1):
        t = (1 + t).sqrt()
        value *= t
        if value >= 1:
            return j + (1 if value == 1 else 2)
    raise AssertionError("unexpected non-crossing")


def main():
    with localcontext() as ctx:
        ctx.prec = 260
        rng = Random(20261024)
        checks = 0
        for _ in range(10000):
            # log-uniform and high-startup samples, deliberately not exactly
            # on the algebraic switching boundaries.
            p = rng.randint(-160, 5)
            coeff = d(rng.randint(1001, 9999)) / 1000
            a = coeff * (d(10) ** p)
            k = normalized_termination(a, informed_initialization(a))
            assert k == predicted_class(a), (a, k, predicted_class(a))
            checks += 1
        for s in ['1e-90', '1e-140', '1e-180', '0.1', '0.2', '0.5',
                  '0.8', '0.999', '1.0', '1.1', '1.9', '2.0', '9.0']:
            a = d(s)
            assert normalized_termination(a, informed_initialization(a)) == predicted_class(a)
            checks += 1
        for n in range(2, 201):
            a = (-d(n)).exp()
            observed = normalized_termination(a, Decimal(0))
            predicted = product_hitting_time(a)
            assert observed == predicted, (n, observed, predicted)
            checks += 1
        # The boundary itself is an exact symbolic identity:
        # a0=1/(7 sqrt 2) implies a1=1/sqrt 2, theta1=7, a2=2.
        # The exact a0=1/sqrt 2 implies a2=1. These identities are
        # proved algebraically in RESULT.md; Decimal cannot certify exact
        # equality to an irrational threshold.
        t = d('0.01')
        u = (1 + t).sqrt()
        a5 = u * (1 + u).sqrt() / d(2).sqrt()
        assert d(1) < a5 < d(2)
        print('VERIFY_OK: informed phases', checks,
              '; uninformed hitting law 199; strict post-reset crossing; '
              'irrational thresholds established analytically')


if __name__ == '__main__':
    main()
