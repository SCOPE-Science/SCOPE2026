#!/usr/bin/env python3
"""Finite checks for abelian subalgebras and ideals of an explicit nilpotent Lie algebra.

All operations use only the Python standard library. Exhaustive base-field
subspace checks are for extension-degree one; the general theorem is proved
separately by the commutator-minor argument.
"""
from itertools import combinations, product
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def bracket(u, v, q):
    a, b, c = u[:3]
    x, y, z = v[:3]
    h = (a*y-b*x) % q
    return (0, 0, h, (h+2*c*x-2*a*z) % q, (h+2*b*z-2*c*y) % q)


def rref_subspaces(n, k, q):
    for pivots in combinations(range(n), k):
        pivot_set = set(pivots)
        slots = [(i, j) for i, p in enumerate(pivots)
                 for j in range(p+1, n) if j not in pivot_set]
        basis = [[int(j == p) for j in range(n)] for p in pivots]
        for values in product(range(q), repeat=len(slots)):
            rows = [row.copy() for row in basis]
            for (i, j), value in zip(slots, values):
                rows[i][j] = value
            yield rows


def is_abelian(rows, q):
    return all(bracket(rows[i], rows[j], q) == (0,)*5
               for i in range(len(rows)) for j in range(i+1, len(rows)))


def lies_in_row_span(vector, rows, q):
    remainder = list(vector)
    for row in rows:
        pivot = next(i for i, v in enumerate(row) if v)
        coefficient = remainder[pivot]
        for j in range(pivot, len(row)):
            remainder[j] = (remainder[j] - coefficient*row[j]) % q
    return not any(remainder)


def check_subspace_counts(q):
    unit = [[int(i == j) for i in range(5)] for j in range(5)]
    observed_ab = []
    observed_ideals = []
    nmax = q*q + q + 1
    for d in range(6):
        num_ab = num_ideal = 0
        for rows in rref_subspaces(5, d, q):
            if not is_abelian(rows, q):
                continue
            num_ab += 1
            if all(lies_in_row_span(bracket(v, w, q), rows, q)
                   for v in unit for w in rows):
                num_ideal += 1
        predicted_ab = gaussian(2, d, q) + nmax*(gaussian(3, d, q)-gaussian(2, d, q))
        predicted_ideal = gaussian(2, d, q) + gaussian(1, d-2, q) - int(d == 2)
        assert num_ab == predicted_ab, (q, d, num_ab, predicted_ab)
        assert num_ideal == predicted_ideal, (q, d, num_ideal, predicted_ideal)
        observed_ab.append(num_ab)
        observed_ideals.append(num_ideal)
    print('base field', q, 'abelian subalgebras', observed_ab, 'abelian ideals', observed_ideals)


def check_centralizers(q):
    vecs = list(product(range(q), repeat=5))
    for u in vecs:
        if u[:3] == (0, 0, 0):
            continue
        count = 0
        for v in vecs:
            if bracket(u, v, q) == (0,)*5:
                count += 1
                a, b, c = u[:3]
                x, y, z = v[:3]
                assert (a*y-b*x) % q == 0
                assert (a*z-c*x) % q == 0
                assert (b*z-c*y) % q == 0
        assert count == q**3, (q, u, count)
    print('centralizers checked over F_'+str(q)+':', len(vecs), 'elements')


def f9_add(x, y):
    return ((x % 3+y % 3) % 3) + 3*((x//3+y//3) % 3)


def f9_neg(x):
    return (-x % 3) + 3*((-(x//3)) % 3)


def f9_mul(x, y):
    # F_9 = F_3[t] / (t^2+1), with t^2 = 2.
    a, b = x % 3, x // 3
    c, d = y % 3, y // 3
    return ((a*c+2*b*d) % 3) + 3*((a*d+b*c) % 3)


def check_extension_field():
    vectors = list(product(range(9), repeat=3))
    nonzero = [v for v in vectors if any(v)]
    slopes = set()
    for u in nonzero:
        slopes.add(min(tuple(f9_mul(t, k) for t in u) for k in range(1, 9)))
        count = 0
        a, b, c = u
        for x, y, z in vectors:
            h = f9_add(f9_mul(a, y), f9_neg(f9_mul(b, x)))
            cross2 = f9_add(f9_mul(c, x), f9_neg(f9_mul(a, z)))
            cross3 = f9_add(f9_mul(b, z), f9_neg(f9_mul(c, y)))
            if h == cross2 == cross3 == 0:
                count += 1
                assert any((x, y, z) == tuple(f9_mul(k, t) for t in u)
                           for k in range(9))
        assert count == 9, (u, count)
    assert len(slopes) == 91, len(slopes)
    print('F_9 triple commutation checked; K-lines =', len(slopes))


if __name__ == '__main__':
    for size in (3, 5):
        check_subspace_counts(size)
    check_centralizers(3)
    check_extension_field()
    print('VERIFY_OK')
