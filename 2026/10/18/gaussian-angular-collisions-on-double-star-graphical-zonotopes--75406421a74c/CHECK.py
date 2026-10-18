#!/usr/bin/env python3
"""Independent exact checks of double-star normal-cone collision formulas."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def beta_triangle(p, q, i, j):
    total = Fraction(0)
    for h in range(p - i + 1):
        numerator = (-1) ** h * comb(p - i, h) * factorial(i + j + h + 1) * factorial(q - j)
        denominator = (i + h + 1) * factorial(i + q + h + 2)
        total += Fraction(numerator, denominator)
    return total


def collision_formula(p, q):
    if min(p, q) < 1:
        raise ValueError('Both hub leaf counts must be positive.')
    return 2 * sum(
        (comb(p, i) * comb(q, j) * beta_triangle(p, q, i, j) ** 2
         for i in range(p + 1) for j in range(q + 1)),
        Fraction(0),
    )


def collision_by_permutations(p, q):
    n = p + q + 2
    edges = [(0, k) for k in range(2, p + 2)]
    edges += [(0, 1)]
    edges += [(1, k) for k in range(p + 2, n)]
    classes = Counter()
    for vertex_ranks in permutations(range(n)):
        signature = tuple(vertex_ranks[u] > vertex_ranks[v] for u, v in edges)
        classes[signature] += 1
    return Fraction(sum(z * z for z in classes.values()), factorial(n) ** 2)


def star_formula(s):
    return sum((Fraction(1, comb(s, i)) for i in range(s + 1)), Fraction(0)) / (s + 1) ** 2


def star_by_permutations(s):
    n = s + 1
    classes = Counter()
    for vertex_ranks in permutations(range(n)):
        signature = tuple(vertex_ranks[0] > vertex_ranks[v] for v in range(1, n))
        classes[signature] += 1
    return Fraction(sum(z * z for z in classes.values()), factorial(n) ** 2)


def main():
    expected = {(1, 1): Fraction(11, 72),
                (1, 2): Fraction(163, 1800),
                (2, 2): Fraction(859, 16200),
                (1, 3): Fraction(103, 1800),
                (2, 3): Fraction(4381, 132300),
                (3, 3): Fraction(451, 22050),
                (2, 4): Fraction(2899, 132300)}
    for (p, q), value in expected.items():
        formula = collision_formula(p, q)
        exhaustive = collision_by_permutations(p, q)
        assert formula == value == exhaustive, (p, q, formula, exhaustive)
        assert formula == collision_formula(q, p)
        print('double-star', p, q, 'exact collision:', formula)
    for s in range(1, 7):
        assert star_formula(s) == star_by_permutations(s)
    for p, q in [(4, 4), (6, 6), (8, 16), (12, 12)]:
        prob = collision_formula(p, q)
        assert 0 < prob < star_formula(p) * star_formula(q)
        print('two-hub', p, q, 'scaled collision:', float((p * q) ** 2 * prob))
    print('All independent exact finite checks passed.')


if __name__ == '__main__':
    main()
