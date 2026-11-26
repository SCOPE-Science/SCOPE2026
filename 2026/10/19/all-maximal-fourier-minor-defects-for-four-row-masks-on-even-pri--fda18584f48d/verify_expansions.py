"""Exact determinant coefficients for z = sign * exp(exponent * tau)."""

from itertools import permutations, product
from math import factorial

import sympy as s


A, B, C, D, d = s.symbols("A B C D d", integer=True)
Z = (A, B, C, D)
ROWS = (0, 1, 2, d)
# The symbolic fourth row is even. Only row one carries column signs.
PERMS = [
    (perm, (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4)))
    for perm in permutations(range(4))
]


def coefficient(signs, n):
    """Extract the degree-n coefficient from the Leibniz expansion."""
    terms = []
    for perm, parity in PERMS:
        for powers in product(range(n + 1), repeat=4):
            if sum(powers) != n:
                continue
            term = s.Integer(parity * signs[perm[1]])
            for row, column, k in zip(ROWS, perm, powers):
                term *= (row * Z[column]) ** k / factorial(k)
            terms.append(term)
    return s.expand(sum(terms))


def verify():
    three = (1, 1, 1, -1)
    two = (1, 1, -1, -1)
    for signs in (three, two):
        for n in range(3):
            assert coefficient(signs, n) == 0
    expected_three = 2 * d * (d - 2) * (A - B) * (A - C) * (B - C)
    expected_two = -2 * d * (d - 2) * (A - B) * (C - D) * (A + B - C - D)
    assert s.expand(coefficient(three, 3) - expected_three) == 0
    assert s.expand(coefficient(two, 3) - expected_two) == 0
    expected_four = s.Rational(2, 3) * d * (d - 2) * (d - 1) * (A - B) * (C - D) * (A - C) * (B - C)
    assert s.expand((coefficient(two, 4) - expected_four).subs(D, A + B - C)) == 0
    print("PASS: determinant coefficients through degree two vanish;")
    print("both degree-three and the equal-sum degree-four identities hold.")


if __name__ == "__main__":
    verify()
