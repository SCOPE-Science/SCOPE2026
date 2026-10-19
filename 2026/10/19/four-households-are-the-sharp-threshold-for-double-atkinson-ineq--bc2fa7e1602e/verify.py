#!/usr/bin/env python3
"""Reproduce exact certificates for the four-income Atkinson crossing theorem.

Requires only the Python 3 standard library. Root decimal output is illustrative;
the analytic proof uses the exponential-polynomial zero bound.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from math import prod

X = (4, 9, 9, 22)
Y = (5, 5, 16, 18)
TERMS = ((4, 1), (5, -2), (9, 2), (16, -1), (18, -1), (22, 1))


def exact_F(integer_exponent):
    return sum((Fraction(z) ** integer_exponent for z in X), Fraction(0)) - sum(
        (Fraction(z) ** integer_exponent for z in Y), Fraction(0)
    )


def F(r):
    return sum(Decimal(coefficient) * (Decimal(base).ln() * r).exp()
               for base, coefficient in TERMS)


def root(a, b):
    left, right = Decimal(a), Decimal(b)
    left_sign = F(left) > 0
    assert left_sign != (F(right) > 0)
    for _ in range(160):
        mid = (left + right) / 2
        if (F(mid) > 0) == left_sign:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def main():
    assert len(X) == len(Y) == 4
    assert sum(X) == sum(Y) == 44
    assert tuple(sorted(TERMS)) == TERMS
    assert tuple(c for _, c in TERMS) == (1, -2, 2, -1, -1, 1)
    assert sum(TERMS[i][1] * TERMS[i + 1][1] < 0
               for i in range(len(TERMS) - 1)) == 4
    assert exact_F(0) == 0 and exact_F(1) == 0
    assert exact_F(-1) == Fraction(-1, 2640)
    assert exact_F(-2) == Fraction(142063, 62726400)
    assert Fraction(prod(X), prod(Y)) == Fraction(99, 100)
    # In a six-term, three-plus-three alternating pattern, both sorted
    # populations would have termwise strict ordering, violating equal sums.
    alternating = []
    for plus_positions in combinations(range(6), 3):
        signs = [1 if i in plus_positions else -1 for i in range(6)]
        if sum(signs[i] != signs[i+1] for i in range(5)) == 5:
            alternating.append(tuple(plus_positions))
    assert alternating == [(0, 2, 4), (1, 3, 5)]
    with localcontext() as ctx:
        ctx.prec = 60
        assert F(Decimal(-2)) > 0 > F(Decimal(-1))
        assert F(Decimal(-1)) < 0 < F(Decimal('-0.1'))
        assert F(Decimal('0.1')) < 0
        smaller_r = root('-2', '-1')
        larger_r = root('-1', '-0.1')
        assert Decimal('-1.141') < smaller_r < Decimal('-1.140')
        assert Decimal('-0.422') < larger_r < Decimal('-0.420')
        print('VERIFY_OK sizes=4 common_total=44 log_product_ratio=log(99/100)')
        print('VERIFY_OK F(-2)=142063/62726400 F(-1)=-1/2640 zero_bound=4')
        print('VERIFY_OK alternating_three_household_signs=2')
        print('VERIFY_OK first_epsilon=', str(1-larger_r))
        print('VERIFY_OK second_epsilon=', str(1-smaller_r))

if __name__ == '__main__':
    main()
