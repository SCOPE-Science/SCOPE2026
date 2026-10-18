"""Exact standard-library verification of a finite plant-pollinator variance theorem.

Run: python3 verify_coextinction_variance.py
All enumerated networks are finite simple bipartite incidence matrices with no zero row
or zero column. The analytic reductions used for smaller/degenerate sides are stated
in the accompanying mathematical proof.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def union_histogram(rows, n_pollinators):
    hist = [0] * (n_pollinators + 1)
    for i, j in combinations(range(len(rows)), 2):
        hist[(rows[i] | rows[j]).bit_count()] += 1
    return tuple(hist)


def degree_data(rows, n_pollinators):
    return (tuple(sorted(row.bit_count() for row in rows)),
            tuple(sorted(sum(row >> col & 1 for row in rows)
                         for col in range(n_pollinators))))


def grouped_histograms(n_plants, n_pollinators):
    groups = defaultdict(set)
    examined = 0
    for rows in product(range(1, 1 << n_pollinators), repeat=n_plants):
        margins = degree_data(rows, n_pollinators)
        if margins[1][0] == 0:
            continue
        examined += 1
        groups[margins].add(union_histogram(rows, n_pollinators))
    # Independent inclusion-exclusion count: all columns must be occupied.
    expected = sum((-1)**j * comb(n_pollinators, j)
                   * ((1 << (n_pollinators-j)) - 1)**n_plants
                   for j in range(n_pollinators + 1))
    assert examined == expected, (examined, expected)
    return groups, examined


def quotient_by_q_one_minus_q_squared(coefficients):
    """Return exact Q where sum c[k]q^k = q(1-q)^2 Q(q)."""
    n = len(coefficients) - 1
    assert coefficients[0] == 0
    assert sum(coefficients) == 0
    assert sum(k * c for k, c in enumerate(coefficients)) == 0
    qcoeff = []
    for j in range(n - 2):
        new = (coefficients[j + 1]
               + (2 * qcoeff[-1] if len(qcoeff) else 0)
               - (qcoeff[-2] if len(qcoeff) >= 2 else 0))
        qcoeff.append(new)
    reconstructed = [0] * (n + 1)
    for j, c in enumerate(qcoeff):
        for shift, weight in ((1, 1), (2, -2), (3, 1)):
            reconstructed[j + shift] += weight * c
    assert tuple(reconstructed) == tuple(coefficients)
    return tuple(qcoeff)


# These complete finite sets of nonzero difference quotients are compact
# certificates; lexicographic ordering of histograms fixes their signs.
EXPECTED_QUOTIENTS = {
    (3, 4): {(0, -1), (-1, -1)},
    (4, 4): {(0, -1), (0, -2), (-1, -1), (-1, 0),
             (-1, 1), (-2, -2), (-1, -2)},
    (3, 5): {(0, 0, -1), (0, -1, -1), (-1, -1, -1),
             (0, -1, 0), (0, -1, -2)},
}
EXPECTED_COUNTS = {
    (3, 4): (2161, 33, 5),
    (4, 4): (41503, 103, 48),
    (3, 5): (16081, 64, 17),
}


def finite_minimality():
    for shape, expected in EXPECTED_COUNTS.items():
        m, n = shape
        groups, number = grouped_histograms(m, n)
        quotient_set = set()
        comparison_count = 0
        for histograms in groups.values():
            for left, right in combinations(sorted(histograms), 2):
                comparison_count += 1
                difference = tuple(a - b for a, b in zip(left, right))
                quotient = quotient_by_q_one_minus_q_squared(difference)
                if any(quotient):
                    quotient_set.add(quotient)
        assert (number, len(groups), comparison_count) == expected
        assert quotient_set == EXPECTED_QUOTIENTS[shape]
        # Each possible Q is strictly negative on (0,1).
        # Only exceptional positive coefficient appears in Q=(-1,1).
        for coefficients in quotient_set:
            assert (all(c <= 0 for c in coefficients)
                    or coefficients == (-1, 1))
        print('Verified exhaustive shape:', shape, 'matrices:', number,
              'degree groups:', len(groups), 'histogram pairs:', comparison_count)


A = (0b00001, 0b00011, 0b01110, 0b10110)
B = (0b00001, 0b00110, 0b00111, 0b11001)


def connected(rows, n_pollinators):
    m = len(rows)
    visited = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        neighbors = ([m+j for j in range(n_pollinators) if rows[vertex] >> j & 1]
                     if vertex < m else
                     [i for i, row in enumerate(rows) if row >> (vertex-m) & 1])
        for v in neighbors:
            if v not in visited:
                visited.add(v)
                frontier.append(v)
    return len(visited) == m + n_pollinators


def moment_by_failure_subsets(rows, n_pollinators, q):
    mean = Fraction(0)
    second = Fraction(0)
    for dead in range(1 << n_pollinators):
        cardinality = dead.bit_count()
        probability = q**cardinality * (1-q)**(n_pollinators-cardinality)
        extinct = sum((row & ~dead) == 0 for row in rows)
        mean += probability * extinct
        second += probability * extinct**2
    return mean, second-mean*mean


def moment_by_union_identity(rows, n_pollinators, q):
    ds = [r.bit_count() for r in rows]
    mean = sum((q**d for d in ds), Fraction(0))
    variance = sum((q**d*(1-q**d) for d in ds), Fraction(0))
    variance += 2*sum((q**(rows[i] | rows[j]).bit_count()
                       -q**(ds[i]+ds[j])
                       for i,j in combinations(range(len(rows)),2)), Fraction(0))
    return mean, variance


def witness():
    assert degree_data(A,5) == degree_data(B,5)
    assert degree_data(A,5) == ((1,2,3,3), (1,1,2,2,3))
    assert connected(A,5) and connected(B,5)
    assert union_histogram(A,5) == (0,0,1,0,5,0)
    assert union_histogram(B,5) == (0,0,0,4,0,2)
    assert quotient_by_q_one_minus_q_squared(tuple(x-y for x,y in zip(
        union_histogram(A,5),union_histogram(B,5)))) == (0,1,-2)
    for q in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
        moments_a = moment_by_failure_subsets(A,5,q)
        moments_b = moment_by_failure_subsets(B,5,q)
        assert moments_a == moment_by_union_identity(A,5,q)
        assert moments_b == moment_by_union_identity(B,5,q)
        assert moments_a[0] == moments_b[0]
        difference = moments_a[1]-moments_b[1]
        assert difference == 2*q*q*(1-q)*(1-q)*(1-2*q)
        print('q =',q,'common expected extinct plants =',moments_a[0],
              'Var_A =',moments_a[1], 'Var_B =',moments_b[1],
              'difference =', difference)


if __name__ == '__main__':
    finite_minimality()
    witness()
    print('All exact checks passed.')
