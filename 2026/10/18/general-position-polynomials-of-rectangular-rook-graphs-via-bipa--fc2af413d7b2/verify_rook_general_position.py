"""Independent finite checks for the general-position polynomial of rook graphs.

Run: python verify_rook_general_position.py
No external packages or files are required.
"""

from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial


def heavy_column_formula(m, n):
    """Closed sum: columns of degree >= 2 have disjoint row neighborhoods."""
    result = [0] * (m * n + 1)
    for q in range(min(n, m // 2) + 1):
        for sizes in product(range(2, m + 1), repeat=q):
            k = sum(sizes)
            if k > m:
                continue
            denom = factorial(m - k)
            for s in sizes:
                denom *= factorial(s)
            coefficient = comb(n, q) * factorial(m) // denom
            for j in range(n - q + 1):
                result[k + j] += coefficient * comb(n - q, j) * (m - k) ** j
    return tuple(result)


@lru_cache(None)
def root_component_recurrence(m, n):
    """Decompose a spanning star forest at its smallest indexed row vertex."""
    if m == 0 or n == 0:
        return (1,)
    result = [0] * (m * n + 1)

    def append_poly(poly, factor, offset):
        for j, c in enumerate(poly):
            result[j + offset] += factor * c

    append_poly(root_component_recurrence(m - 1, n), 1, 0)
    for k in range(1, n + 1):
        append_poly(root_component_recurrence(m - 1, n - k), comb(n, k), k)
    for other_rows in range(1, m):
        append_poly(root_component_recurrence(m - 1 - other_rows, n - 1),
                    n * comb(m - 1, other_rows), other_rows + 1)
    return tuple(result)


def direct_geodesic_enumeration(m, n):
    """Literal vertex-subset enumeration using shortest-path distances."""
    vertices = [(i, j) for i in range(m) for j in range(n)]
    def distance(a, b):
        return int(a[0] != b[0]) + int(a[1] != b[1])
    forbidden = []
    for i, j, k in combinations(range(m * n), 3):
        a, b, c = vertices[i], vertices[j], vertices[k]
        dab, dac, dbc = distance(a, b), distance(a, c), distance(b, c)
        if max(dab, dac, dbc) == 2 and sorted((dab, dac, dbc)) == [1, 1, 2]:
            forbidden.append((1 << i) | (1 << j) | (1 << k))
    result = [0] * (m * n + 1)
    for mask in range(1 << (m * n)):
        if not any((mask & b) == b for b in forbidden):
            result[mask.bit_count()] += 1
    return tuple(result)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def assert_top_coefficient(m, n, poly):
    if min(m,n) == 1:
        want_degree, want_coefficient = max(m,n), 1
    elif m == n == 2:
        want_degree, want_coefficient = 2, 6
    elif min(m,n) == 2:
        want_degree, want_coefficient = max(m,n), 2**max(m,n)
    else:
        want_degree, want_coefficient = m+n-2, m*n
    assert len(poly)-1 == want_degree, (m,n,poly)
    assert poly[-1] == want_coefficient, (m,n,poly)


def run():
    checks = 0
    subsets = 0
    for m, n in [(1,1),(1,5),(2,2),(2,3),(2,4),(2,5),
                 (3,3),(3,4),(3,5),(4,4)]:
        first = trim(heavy_column_formula(m,n))
        second = trim(root_component_recurrence(m,n))
        third = trim(direct_geodesic_enumeration(m,n))
        assert first == second == third, (m,n,first,second,third)
        assert_top_coefficient(m,n,first)
        checks += 1
        subsets += 1 << (m*n)
    # Formula-vs-recurrence comparisons beyond brute-force ranges.
    for m,n in [(2,12),(3,12),(4,8),(5,7),(6,6),(7,8),(8,8)]:
        first = trim(heavy_column_formula(m,n))
        assert first == trim(root_component_recurrence(m,n)), (m,n)
        assert_top_coefficient(m,n,first)
        checks += 1
    print('PASS:',checks,'parameter pairs;',subsets,
          'literal vertex subsets enumerated in 10 small-board cases')
    print('Examples: R(3,3)=',trim(heavy_column_formula(3,3)),
          '; R(4,4)=',trim(heavy_column_formula(4,4)))

if __name__ == '__main__':
    run()
