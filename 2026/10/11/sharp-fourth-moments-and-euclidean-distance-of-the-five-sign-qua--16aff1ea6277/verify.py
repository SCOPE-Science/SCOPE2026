"""Exact finite arithmetic for five-sign quadratic Walsh-chaos geometry.

Usage: python3 verify.py. No dependencies outside the standard library.
This finite calculation independently replays the polynomial identity;
the accompanying written proof establishes global nonnegativity.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial

n = 5
edges = list(combinations(range(n), 2))
assert len(edges) == 10

cycles = set()
for vs in combinations(range(n), 4):
    for q in permutations(vs[1:]):
        v = (vs[0],) + q
        cyc = frozenset(tuple(sorted((v[k], v[(k + 1) % 4]))) for k in range(4))
        cycles.add(cyc)
assert len(cycles) == 15
cycs = sorted(tuple(sorted(edges.index(e) for e in cyc)) for cyc in cycles)

incidence = Counter(pair for cyc in cycs for pair in combinations(cyc, 2))
assert len(incidence) == 45 and all(v == 2 for v in incidence.values())

poly = defaultdict(Fraction)

def add_square(first, second, weight):
    """Accumulate weight*(product(first)-product(second))**2."""
    poly[tuple(sorted(first + first))] += weight
    poly[tuple(sorted(second + second))] += weight
    poly[tuple(sorted(first + second))] -= 2 * weight

# Rational sum-of-squares identity, right side.
for i, j in combinations(range(10), 2):
    add_square((i, i), (j, j), Fraction(3, 5))
for a, b, c, d in cycs:
    for u, v in (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))):
        add_square(u, v, Fraction(4))

# Independent coefficient computation for left side = (32/5)*S^2 - E[Q^4].
lhs = defaultdict(Fraction)
for i in range(10):
    lhs[(i, i, i, i)] += Fraction(32, 5)
for i, j in combinations(range(10), 2):
    lhs[(i, i, j, j)] += Fraction(64, 5)
for inds in combinations_with_replacement(range(10), 4):
    counts = Counter(inds)
    coefficient = factorial(4)
    for multiplicity in counts.values():
        coefficient //= factorial(multiplicity)
    xor_mask = 0
    for e in inds:
        u, v = edges[e]
        xor_mask ^= (1 << u) | (1 << v)
    if xor_mask == 0:
        lhs[inds] -= coefficient

monomials = list(combinations_with_replacement(range(10), 4))
assert len(monomials) == 715
assert all(lhs[monom] == poly[monom] for monom in monomials)

# Equality data and complete classification of saturated sign patterns.
values = [sum(s[u] * s[v] for u, v in edges) for s in product((-1, 1), repeat=5)]
assert Fraction(sum(t*t for t in values), 32) == 10
assert Fraction(sum(t**4 for t in values), 32) == 640
assert Fraction(640, 100) == Fraction(32, 5)
valid = set()
for signs in product((-1, 1), repeat=10):
    if all(__import__('math').prod(signs[e] for e in cyc) == 1 for cyc in cycs):
        valid.add(signs)
cut = set(tuple(global_sign * s[u] * s[v] for u, v in edges)
          for global_sign in (-1, 1)
          for s in product((-1, 1), repeat=5))
assert valid == cut and len(valid) == 32
print('VERIFY_OK: 715 exact polynomial coefficients, 15 cycles, 45 twofold pair incidences, 32 cut-sign extremizers')
