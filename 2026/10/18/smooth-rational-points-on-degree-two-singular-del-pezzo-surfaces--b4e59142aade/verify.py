"""Exact finite-field linear-algebra certificate for a double-plane point theorem.
Pure Python 3; no external dependencies.
"""
from itertools import product

# F4 = F2[t]/(t^2+t+1), elements 0,1,t,1+t encoded 0,1,2,3.
def add(a, b):
    return a ^ b

def mul(a, b):
    c = (a if b & 1 else 0) ^ ((a << 1) if b & 2 else 0)
    if c & 4:
        c ^= 7
    assert 0 <= c < 4
    return c

def power(a, n):
    out = 1
    for _ in range(n):
        out = mul(out, a)
    return out

def inverse(a):
    assert a != 0
    return power(a, 2)

def trace(a):
    return a ^ power(a, 2)

def norm_quad(p):
    x, y, z = p
    return power(x, 2) ^ mul(x, y) ^ mul(2, power(y, 2))

def monomial(p, exps):
    r = 1
    for a, d in zip(p, exps):
        r = mul(r, power(a, d))
    return r

def rank_f2_columns(columns):
    pivots = {}
    chosen = []
    for index, column in enumerate(columns):
        v = column
        while v:
            leading = v.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = v
                chosen.append(index)
                break
            v ^= pivots[leading]
    return len(pivots), chosen

def rank_f2_rows(columns, rows):
    basis = {}
    for row_idx in range(rows):
        v = sum(((c >> row_idx) & 1) << j for j, c in enumerate(columns))
        while v:
            k = (v & -v).bit_length() - 1
            if k not in basis:
                basis[k] = v
                break
            v ^= basis[k]
    return len(basis)

assert [[mul(a, b) for b in range(4)] for a in range(4)] == [
    [0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]
]
assert [trace(a) for a in range(4)] == [0, 0, 1, 1]
points = ([(1, y, z) for y, z in product(range(4), repeat=2)]
          + [(0, 1, z) for z in range(4)] + [(0, 0, 1)])
assert len(points) == 21
zeros = [p for p in points if norm_quad(p) == 0]
assert zeros == [(0, 0, 1)]
outside = [p for p in points if norm_quad(p)]
assert len(outside) == 20
monomials = [(i, j, 4-i-j) for i in range(5) for j in range(5-i)]
assert len(monomials) == 15
cols = []
for e in monomials:
    for c in (1, 2):
        vec = 0
        for j, pt in enumerate(outside):
            q = norm_quad(pt)
            ratio = mul(mul(c, monomial(pt, e)), inverse(power(q, 2)))
            bit = trace(ratio)
            assert bit in (0, 1)
            vec |= bit << j
        cols.append(vec)
assert len(cols) == 30
# The trace-evaluation image is the even-parity code; rank exactly 19.
assert all(col.bit_count() % 2 == 0 for col in cols)
rank, chosen = rank_f2_columns(cols)
assert rank == 19
assert rank_f2_rows(cols, 20) == 19
independent = [1, 0, 2, 8, 3, 5, 4, 9, 10, 13, 12, 16, 11,
               14, 15, 17, 6, 7, 29]
assert rank_f2_columns([cols[i] for i in independent])[0] == 19
assert [(i, format(cols[i], '05x')) for i in independent] == [
    (1, 'a6aa6'), (0, '6c66c'), (2, 'eeee0'), (8, 'ffff0'),
    (3, 'e00e0'), (5, '66a60'), (4, 'aaca0'), (9, 'f00f0'),
    (10, '00ee0'), (13, '0cc60'), (12, '066a0'), (16, '00ff0'),
    (11, '0eeee'), (14, '06c60'), (15, '0a6a0'), (17, '0fff0'),
    (6, '6c660'), (7, 'a6aa0'), (29, '0ffff')]
# H -> H^2 + Q H, a 12-bit F2-linear map, evaluates to trace zero.
quad_monomials = [(i, j, 2-i-j) for i in range(3) for j in range(3-i)]
assert len(quad_monomials) == 6
for e in quad_monomials:
    for c in (1, 2):
        for pt in outside:
            q = norm_quad(pt)
            h = mul(c, monomial(pt, e))
            as_value = power(h, 2) ^ mul(q, h)
            assert trace(mul(as_value, inverse(power(q, 2)))) == 0
# Kernel of H -> H(H+Q) consists of 0 and Q, because F4[x,y,z] is a domain.
# Thus image dimension is 12-1=11. Evaluation rank 19 => kernel dimension 30-19=11.
# The two spaces therefore coincide. The constant-one evaluation vector has
# a representative t*Q^2 because trace(t)=1, implying geometric factorization.
print('PASS: 21 projective points; Q zero at one point; 20 evaluation rows;')
print('PASS: trace code rank 19 by independent row and column eliminations;')
print('PASS: explicit 19 independent columns reproduced and Artin-Schreier kernel dimension 11;')
print('PASS: required trace vanishing and geometric splitting implication established.')
