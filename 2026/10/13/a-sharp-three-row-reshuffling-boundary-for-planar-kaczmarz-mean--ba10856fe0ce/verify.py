"""Exact rational checks for planar Kaczmarz reshuffling and iid sampling.

Run with Python 3 standard library: python verify.py
The general-angle result is proved algebraically in RESULT.md; finite examples
here are independent exact-arithmetic corroboration, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import permutations, product

I = ((F(1), F(0)), (F(0), F(1)))
Z = ((F(0), F(0)), (F(0), F(0)))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def sub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(2)) for i in range(2))


def scale(a, c):
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def tr(a):
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def projector(row):
    x, y = row
    assert x*x + y*y == 1
    return ((1 - x*x, -x*y), (-x*y, 1 - y*y))


def moment(rows, replace):
    ps = tuple(map(projector, rows))
    m = len(rows)
    sequences = list(product(range(m), repeat=m)) if replace else list(permutations(range(m)))
    ans = Z
    for seq in sequences:
        b = I
        for i in seq:
            b = mm(ps[i], b)
        ans = add(ans, mm(tr(b), b))
    return scale(ans, F(1, len(sequences)))


def norm_value(mat, v):
    return sum(v[i] * mat[i][j] * v[j] for i in range(2) for j in range(2))


# Check the symbolic closed form at five distinct rational projectors.
for c, s in [(F(0), F(1)), (F(3, 5), F(4, 5)),
             (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)),
             (F(12, 13), F(5, 13))]:
    rows = [(F(1), F(0)), (F(1), F(0)), (c, s)]
    p, q = projector(rows[0]), projector(rows[2])
    u = c*c
    sr = moment(rows, False)
    ti = moment(rows, True)
    expected_s = add(scale(p, u*(1+u)/3), scale(q, u/3))
    expected_t = add(scale(p, (8+6*u+4*u*u)/27),
                     scale(q, (1+6*u+2*u*u)/27))
    expected_d = scale(add(scale(p, 8+5*u), scale(q, 1-2*u)), (1-u)/27)
    assert sr == expected_s
    assert ti == expected_t
    assert sub(ti, sr) == expected_d
    det = expected_d[0][0]*expected_d[1][1] - expected_d[0][1]**2
    assert det == (1-u)**3 * (1-2*u) * (8+5*u)/729

# Exact three-row counterexample with repeated first two rows.
a = [(F(1), F(0)), (F(1), F(0)), (F(4, 5), F(3, 5))]
v = (F(1), F(0))
rr = norm_value(moment(a, False), v)
iid = norm_value(moment(a, True), v)
assert rr == F(48, 625)
assert iid == F(1179, 15625)
assert rr - iid == F(21, 15625) > 0
assert rr / iid == F(400, 393)

# Non-identical rational rows retain the reversal.
b = [(F(1), F(0)), (F(399, 401), F(40, 401)),
     (F(4, 5), F(3, 5))]
assert norm_value(moment(b, False), v) > norm_value(moment(b, True), v)
assert len({row for row in b}) == 3

# Two-row planar Kaczmarz has the opposite exact universal ordering.
for c, s in [(F(0), F(1)), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5))]:
    pair = [(F(1), F(0)), (c, s)]
    p, q = map(projector, pair)
    u = c*c
    assert sub(moment(pair, True), moment(pair, False)) == scale(add(p, q), (1-u)/4)

print('VERIFY_OK: exact row identities, phase determinant, 27 iid and 6 permutation paths, minimality, distinct-row witness')
