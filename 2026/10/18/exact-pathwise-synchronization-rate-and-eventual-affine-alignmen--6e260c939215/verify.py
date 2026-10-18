#!/usr/bin/env python3
"""Reproduce finite exact-arithmetic checks for a random interval iteration."""
from fractions import Fraction
from math import log, isclose
from random import Random


def parameters(c):
    a = Fraction(1, 2) / (1 - c)
    b = Fraction(1, 2) / c
    assert Fraction(1, 2) / a + Fraction(1, 2) / b == 1
    assert a * (1-c) == b * c == Fraction(1, 2)
    return a, b


def apply(t, z, c, a, b):
    if t == 0:
        return (a*z, a) if z <= 1-c else (1-b*(1-z), b)
    return (b*z, b) if z <= c else (1-a*(1-z), a)


def finite_check(c, seed, count):
    a, b = parameters(c)
    for t in (0, 1):
        assert apply(t, Fraction(0), c, a, b)[0] == 0
        assert apply(t, Fraction(1), c, a, b)[0] == 1
    h = -float(c)*log(float(c))-(1-float(c))*log(1-float(c))
    lam=(1-float(c))*log(float(a))+float(c)*log(float(b))
    assert isclose(lam, h-log(2), rel_tol=1e-14, abs_tol=1e-14)
    assert lam < 0
    x, y = Fraction(1, 5), Fraction(4, 5)
    last_different = -1
    gaps = []
    slopes = []
    for n in range(count):
        choice = Random(seed+n*7919).randrange(2)
        xn, sx = apply(choice, x, c, a, b)
        yn, sy = apply(choice, y, c, a, b)
        assert 0 < xn < yn < 1
        if sx != sy:
            last_different=n
        gaps.append(y-x)
        slopes.append(sx)
        x, y = xn, yn
    assert last_different+15 < count, (c, last_different)
    for k in range(last_different+1, count-1):
        assert gaps[k+1] == gaps[k]*slopes[k]
    # Exponent and almost-sure claims are ANALYTIC; a finite word is not evidence
    # of their universal/infinite-time validity.
    return last_different


def main():
    for c, seed in ((Fraction(1, 4), 23147), (Fraction(1, 3), 4461)):
        last=finite_check(c, seed, 400)
        print('finite_branch_example', str(c), 'last_crossing', last)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
