#!/usr/bin/env python3
"""Exact rational consistency test for periodic-point counts with open holes."""
from fractions import Fraction
from itertools import product

HALF = Fraction(1, 2)
PARAMETERS = (Fraction(1, 4), Fraction(1, 3), Fraction(7, 20), Fraction(2, 5))


def point_for_word(word):
    """Solve the affine periodicity equation for one branch word, if valid."""
    intercept = 0
    for branch in word:
        intercept = -2 * intercept + branch
    point = Fraction(intercept, 1 - (-2) ** len(word))
    if not Fraction(0) <= point <= Fraction(1):
        return None
    x = point
    for branch in word:
        if branch == 1:
            if x >= HALF:
                return None
            x = 1 - 2 * x
        else:
            if x <= HALF:
                return None
            x = 2 - 2 * x
    assert x == point
    return point


def periodic_points(n):
    return {x for word in product((1, 2), repeat=n)
            if (x := point_for_word(word)) is not None}


def avoids_hole(x, a, n):
    for _ in range(n):
        if a < x < 1 - a:
            return False
        if x < HALF:
            x = 1 - 2 * x
        elif x > HALF:
            x = 2 - 2 * x
        else:
            return False
    return True


def expected(n, a):
    return 2 * (n % 2 == 0) + 2 * (a >= Fraction(1, 3)) + 4 * (a == Fraction(2, 5) and n % 4 == 0)


def main():
    checks = 0
    for n in range(1, 14):
        candidates = periodic_points(n)
        for a in PARAMETERS:
            actual = sum(avoids_hole(x, a, n) for x in candidates)
            target = expected(n, a)
            assert actual == target, (n, a, actual, target)
            checks += 1
    print(f"PASS: {checks} exact parameter/period checks (n<=13)")


if __name__ == "__main__":
    main()
