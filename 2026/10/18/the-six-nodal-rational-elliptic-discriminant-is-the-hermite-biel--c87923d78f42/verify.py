"""Exact finite consistency checks for a six-point determinantal equation.

The universal identification, its degree, and moduli claims use the
geometric proof in RESULT.md, not these finite calculations.
"""
from itertools import permutations
from math import prod


def matchings(ids):
    ids = tuple(ids)
    if not ids:
        yield ()
        return
    first = ids[0]
    for j in range(1, len(ids)):
        for tail in matchings(ids[1:j] + ids[j + 1:]):
            yield ((first, ids[j]),) + tail


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def deltas(roots):
    return [det3([(1, -(roots[i] + roots[j]), roots[i] * roots[j])
                  for i, j in matching])
            for matching in matchings(range(6))]


M = tuple(matchings(range(6)))
assert len(M) == 15 and len(set(M)) == 15
ordinary = (0, 1, 2, 4, 7, 13)
ordinary_value = prod(deltas(ordinary))
assert ordinary_value == 5492176600112938778274260582400
assert all(prod(deltas(tuple(ordinary[i] for i in p))) == ordinary_value
           for p in permutations(range(6)))
collision = (0, 0, 1, 2, 4, 7)
assert prod(deltas(collision)) == -417070016364124569600

symmetric = (1, -1, 2, -2, 3, -3)
values = deltas(symmetric)
assert values.count(0) == 1
assert M[values.index(0)] == ((0, 1), (2, 3), (4, 5))

# The dependence 5(s^2-t^2)-8(s^2-4t^2)+3(s^2-9t^2)=0
Q1, Q2, Q3 = (2, 22), (-13, 37), (11, -59)
assert tuple(Q1[i] + Q2[i] + Q3[i] for i in range(2)) == (0, 0)
A = tuple(Q1[i] - Q2[i] for i in range(2))
B = tuple(Q2[i] - Q3[i] for i in range(2))
C = tuple(Q3[i] - Q1[i] for i in range(2))
assert (A, B, C) == ((15, -15), (-24, 96), (9, -81))
assert all(sum(c * r ** (2-2*j) for j, c in enumerate(poly)) == 0
           for poly, roots in [(A, (-1, 1)), (B, (-2, 2)), (C, (-3, 3))]
           for r in roots)
assert len({-1, 1, -2, 2, -3, 3}) == 6
print('VERIFY_OK matchings=15 symmetric_permutations=720 special_zeros=1')
