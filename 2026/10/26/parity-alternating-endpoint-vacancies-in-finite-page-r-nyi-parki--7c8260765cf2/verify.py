#!/usr/bin/env python3
"""Exact finite checks for endpoint vacancies of greedy dimers on a path."""
from fractions import Fraction
from itertools import permutations
from math import factorial

a = [Fraction(0), Fraction(1)]
b = [Fraction(0), Fraction(1)]
checks = 0
for n in range(2, 80):
    a.append(sum(a[:n - 1], Fraction(0)) / (n - 1))
    b.append(sum((a[j] * a[n - 2 - j] for j in range(n - 1)), Fraction(0)) / (n - 1))
    exact_a = sum((Fraction((-1) ** j, factorial(j)) for j in range(n)), Fraction(0))
    assert a[n] == exact_a
    checks += 1
    if n >= 4:
        exact_b = sum((Fraction((n - 3 - j) * (-2) ** j, factorial(j)) for j in range(n - 3)), Fraction(0)) / (n - 1)
        assert b[n] == exact_b
        checks += 1
    if n >= 3:
        assert (-1) ** n * (b[n] - a[n] * a[n]) > 0
        checks += 1
assert b[2] == a[2] == 0
checks += 1
for n in range(2, 10):
    left = both = 0
    for order in permutations(range(n - 1)):
        occupied = [False] * n
        for i in order:
            if not occupied[i] and not occupied[i + 1]:
                occupied[i] = occupied[i + 1] = True
        is_left_vacant = not occupied[0]
        is_right_vacant = not occupied[-1]
        left += is_left_vacant
        both += is_left_vacant and is_right_vacant
    total = factorial(n - 1)
    assert a[n] == Fraction(left, total)
    assert b[n] == Fraction(both, total)
    checks += 2
print(f"PASS: {checks} exact tests, independent enumeration through nine sites")
