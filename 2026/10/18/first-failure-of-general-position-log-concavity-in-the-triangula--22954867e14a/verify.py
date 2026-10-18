"""Exact checks for triangular-graph general-position coefficient shapes.

Uses integer component recurrences, a separate rational binomial expansion,
and direct shortest-path triple obstruction enumeration in small graphs.
Python >=3.9; standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

LIMIT = 30


def via_components(limit):
    polys = [[1]]
    for n in range(1, limit + 1):
        row = [0] * (n + 1)
        for size in range(1, n + 1):
            choices = comb(n - 1, size - 1)
            if size == 1:
                forms = ((0, 1),)
            elif size == 2:
                forms = ((1, 1),)
            elif size == 3:
                forms = ((2, 3), (3, 1))
            else:
                forms = ((size - 1, size),)
            for edges, ways in forms:
                for degree, count in enumerate(polys[n - size]):
                    row[degree + edges] += choices * ways * count
        polys.append(row)
    return polys


def via_exponential_formula(n):
    # [z^k] z^n n![u^n]exp(u^3/6 + (u exp(u)-u^2/2)/z).
    row = [0] * (n + 1)
    fn = factorial(n)
    for k in range(n + 1):
        j = n - k
        total = Fraction()
        for tri in range(k // 3 + 1):
            rem = k - 3 * tri
            for h in range(min(j, rem) + 1):
                power = rem - h
                base = j - h
                factor = ((-1) ** h * comb(j, h) * base ** power)
                total += Fraction(factor, 6 ** tri * factorial(tri) * 2 ** h * factorial(power))
        value = fn * total / factorial(j)
        assert value.denominator == 1, (n, k, value)
        row[k] = value.numerator
    return row


def via_graph_definition(n):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    adjacency = [sum(1 << j for j, other in enumerate(edges)
                     if i != j and bool(set(edge) & set(other)))
                 for i, edge in enumerate(edges)]
    # Since the triangular graph has diameter two (n>=4), a
    # selected triple is forbidden precisely when its endpoints
    # are nonadjacent and its middle vertex is adjacent to both.
    forbidden = []
    for triple in combinations(range(m), 3):
        if any(not (adjacency[a] >> b & 1) and
               (adjacency[c] >> a & 1) and (adjacency[c] >> b & 1)
               for a, b, c in ((triple[0], triple[1], triple[2]),
                               (triple[0], triple[2], triple[1]),
                               (triple[1], triple[2], triple[0]))):
            forbidden.append(sum(1 << i for i in triple))
    # Every subset avoiding the forbidden triples is in general position.
    coeff = [0] * (m + 1)
    for subset in range(1 << m):
        if all(subset & bad != bad for bad in forbidden):
            coeff[subset.bit_count()] += 1
    return coeff, len(forbidden), 1 << m


def main():
    a = via_components(LIMIT)
    for n in range(0, LIMIT + 1):
        assert a[n] == via_exponential_formula(n), (n, 'formula disagreement')
    graph_masks = 0
    forbidden_counts = {}
    for n in range(3, 7):
        direct, forbidden, masks = via_graph_definition(n)
        assert direct[:len(a[n])] == a[n]
        assert not any(direct[len(a[n]):])
        forbidden_counts[n] = forbidden
        graph_masks += masks
    for n in range(3, LIMIT):
        row = a[n]
        degree = max(i for i, x in enumerate(row) if x)
        assert all(x > 0 for x in row[:degree + 1])
        assert all(row[k] ** 2 >= row[k - 1] * row[k + 1]
                   for k in range(1, degree))
    row = a[30]
    A, B, C = row[28], row[29], row[30]
    determinant = B * B - A * C
    assert determinant < 0
    assert (A, B, C, determinant) == (
        4575989857607826108600,
        73770312933671827650,
        1208883745669600000,
        -89780688879179441682809722027255477500,
    )
    print('VERIFICATION_OK exact_formula_orders=0..30 direct_graph_orders=3..6 '
          f'direct_masks={graph_masks} forbidden_triples={forbidden_counts}')
    print(f'first_non_log_concave_order=30 a_28={A} a_29={B} a_30={C}')
    print(f'a_29_squared_minus_a_28_times_a_30={determinant}')


if __name__ == '__main__':
    main()
