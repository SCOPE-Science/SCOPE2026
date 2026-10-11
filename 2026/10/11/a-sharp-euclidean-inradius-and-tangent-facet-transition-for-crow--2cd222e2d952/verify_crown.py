"""Exact finite checks for the Euclidean crown symmetric-edge-polytope theorem.

Use: python3 verify_crown.py. Finite tests supplement the symbolic proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def expected(n):
    binary = Fraction(n, 1) - Fraction(n % 2, 2 * n)
    exceptional = Fraction(n + 8, 2)
    balanced_count = (2 if n % 2 == 0 else 4) * comb(n, n // 2)
    count = (2 * n if exceptional >= binary else 0)
    count += balanced_count if binary >= exceptional else 0
    return max(binary, exceptional), count


def compressed_enumeration(n):
    """Enumerate all feasible integer potentials modulo translation and index permutation."""
    types = list(product(range(4), repeat=2))
    compatible = [[abs(a - d) <= 1 and abs(c - b) <= 1
                   for c, d in types] for a, b in types]
    best = -1
    count = 0
    tested = 0

    def visit(k, start, chosen, total, squares, minimum):
        nonlocal best, count, tested
        if k == n:
            if minimum != 0:
                return
            tested += 1
            numerator = 2 * n * squares - total * total
            multiplicity = factorial(n)
            for v in Counter(chosen).values():
                multiplicity //= factorial(v)
            if numerator > best:
                best, count = numerator, multiplicity
            elif numerator == best:
                count += multiplicity
            return
        for i in range(start, 16):
            a, b = types[i]
            if not all(compatible[i][j] for j in chosen):
                continue
            visit(k + 1, i, chosen + (i,), total + a + b,
                  squares + a * a + b * b, min(minimum, a, b))

    visit(0, 0, (), 0, 0, 3)
    return Fraction(best, 2 * n), count, tested


def independent_small(n):
    """Direct coordinate enumeration, no permutation-profile compression."""
    best, count = Fraction(-1), 0
    for a in product(range(4), repeat=n):
        for b in product(range(4), repeat=n):
            vals = a + b
            if min(vals) != 0:
                continue
            if any(abs(a[i] - b[j]) > 1
                   for i in range(n) for j in range(n) if i != j):
                continue
            radius_sq = Fraction(2 * n * sum(v * v for v in vals)
                                 - sum(vals) ** 2, 2 * n)
            if radius_sq > best:
                best, count = radius_sq, 1
            elif radius_sq == best:
                count += 1
    return best, count


for n in range(3, 15):
    got, count, profiles = compressed_enumeration(n)
    want, want_count = expected(n)
    assert (got, count) == (want, want_count), (n, got, count, want, want_count)
    print(f'n={n}: squared polar radius={got}; tangent facets={count}; profiles={profiles}: PASS')
for n in (3, 4):
    got, count = independent_small(n)
    assert (got, count) == expected(n), (n, got, count)
    print(f'n={n}: independent direct-coordinate check: PASS')
print('ALL EXACT FINITE CHECKS PASS')
