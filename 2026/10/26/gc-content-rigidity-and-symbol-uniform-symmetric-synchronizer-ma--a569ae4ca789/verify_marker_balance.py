#!/usr/bin/env python3
"""Exact finite verification of complementary marker lookup-table distributions.

Symbols 0,1 form one complementary pair and 2,3 form the other.
The proof's orbit factors and an independent enumeration are checked separately.
No external libraries are required.
"""
from collections import Counter
from itertools import product

Q = range(4)
bar = lambda s: s ^ 1


def poly_product(a, b):
    result = Counter()
    for ex, ca in a.items():
        for ey, cb in b.items():
            result[tuple(x + y for x, y in zip(ex, ey))] += ca * cb
    return result


def monomial(j, k):
    v = [0] * 4
    v[j] += 1
    v[k] += 1
    return tuple(v)


def choices(a, b):
    u, v = bar(a), bar(b)
    return [(c, d) for c, d in product(Q, repeat=2)
            if c not in (a, b) and d not in (u, v) and d != bar(c)]


def pair_orbits():
    seen = set()
    orbit_list = []
    for a, b in product(Q, repeat=2):
        if (a, b) in seen:
            continue
        pair = ((a, b), (bar(a), bar(b)))
        assert pair[0] != pair[1]
        seen.update(pair)
        orbit_list.append(pair)
    assert len(orbit_list) == 8 and len(seen) == 16
    return orbit_list


def count_by_polynomial(only_symmetric=False):
    # Eight factors are written independently of the programmatic constraints.
    hardcoded = [
        [(1, 2), (1, 3), (2, 0), (2, 2), (3, 0), (3, 3)],
        [(2, 2), (3, 3)],
        [(1, 2), (3, 0)],
        [(1, 3), (2, 0)],
        [(1, 2), (3, 0)],
        [(0, 2), (3, 1)],
        [(0, 0), (0, 2), (1, 1), (1, 2), (3, 0), (3, 1)],
        [(0, 0), (1, 1)],
    ]
    generating = {(0, 0, 0, 0): 1}
    # Coefficient DP of the explicitly listed eight orbit polynomials.
    if only_symmetric:
        # Transpose interchanges orbit 2 with 4, and 3 with 5 (zero based).
        representatives = [0, 1, 2, 3, 6, 7]
        multiples = {0: 1, 1: 1, 2: 2, 3: 2, 6: 1, 7: 1}
    else:
        representatives = list(range(8))
        multiples = {i: 1 for i in representatives}
    for i in representatives:
        factor = Counter()
        for c, d in hardcoded[i]:
            e = monomial(c, d)
            e = tuple(x * multiples[i] for x in e)
            factor[e] += 1
        generating = poly_product(generating, factor)
    assert sum(generating.values()) == (576 if only_symmetric else 2304)
    # Complete output symbol balance means each symbol appears four times.
    return generating.get((4, 4, 4, 4), 0), generating


def count_by_direct_enumeration():
    orbit_list = pair_orbits()
    options = [choices(*p[0]) for p in orbit_list]
    assert [len(opts) for opts in options] == [6, 2, 2, 2, 2, 2, 6, 2]
    gc_counts = Counter()
    balanced = symmetric = both = 0
    example = None
    for opt_tuple in product(*options):
        lookup = {}
        for pair, outputs in zip(orbit_list, opt_tuple):
            for (a, b), c in zip(pair, outputs):
                lookup[a, b] = c
        assert len(lookup) == 16
        for a, b in product(Q, repeat=2):
            c = lookup[a, b]
            assert c != a and c != b
            assert lookup[bar(a), bar(b)] != bar(c)
        hist = tuple(sum(lookup[a, b] == c for a, b in product(Q, repeat=2)) for c in Q)
        gc_counts[hist[2] + hist[3]] += 1
        sym = all(lookup[a, b] == lookup[b, a] for a, b in product(Q, repeat=2))
        bal = hist == (4, 4, 4, 4)
        balanced += int(bal)
        symmetric += int(sym)
        both += int(bal and sym)
        if bal and sym and example is None:
            example = [[lookup[a, b] for b in Q] for a in Q]
    return gc_counts, balanced, symmetric, both, example


def main():
    bal_poly, p_all = count_by_polynomial()
    both_poly, p_sym = count_by_polynomial(True)
    gc_count, bal, sym, both, example = count_by_direct_enumeration()
    poly_gc = Counter()
    for ex, ct in p_all.items():
        poly_gc[ex[2] + ex[3]] += ct
    assert gc_count == poly_gc == {7: 512, 8: 1280, 9: 512}
    assert bal_poly == bal == 80
    assert both_poly == both == 16
    assert sym == 576
    assert sum(gc_count.values()) == 2304
    assert example == [[1, 2, 3, 1], [2, 2, 3, 0], [3, 3, 1, 0], [1, 0, 0, 2]]
    print('Admissible tables: 2304')
    print('GC input-pair profile:', sorted(gc_count.items()))
    print('Fully symbol-balanced tables: 80')
    print('Transpose-symmetric admissible tables: 576')
    print('Fully balanced and transpose-symmetric tables: 16')
    print('Balanced symmetric sample, rows a=0..3, columns b=0..3:')
    for row in example:
        print(' ', ' '.join(map(str, row)))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
