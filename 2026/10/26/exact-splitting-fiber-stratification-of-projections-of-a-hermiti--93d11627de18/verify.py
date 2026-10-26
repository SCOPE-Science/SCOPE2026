#!/usr/bin/env python3
"""Exact split-pencil profile of Y^2 Z + Y Z^2 = X^3 over GF(64).

Python standard library only; two separately implemented enumerations.
Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import combinations

MOD = 0b1000011  # X^6+X+1

def gf2_mod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

# Monic degree-6 polynomial has no factor of degree <= 3.
assert all(gf2_mod(MOD, (1 << d) | tail)
           for d in (1, 2, 3) for tail in range(1 << d))

def multiply(a, b):
    out = 0
    while b:
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & 64: a ^= MOD
    return out

M = [[multiply(i, j) for j in range(64)] for i in range(64)]

def power(a, n):
    v = 1
    while n:
        if n & 1: v = M[v][a]
        a = M[a][a]
        n >>= 1
    return v

inv = [0] + [power(a, 62) for a in range(1, 64)]
assert all(M[a][inv[a]] == 1 for a in range(1, 64))

# Every projective point has exactly one representative in this list.
P = [(0, 1, 0)] + [(1, a, 0) for a in range(64)] + [
    (a, b, 1) for a in range(64) for b in range(64)]
assert len(P) == len(set(P)) == 4161

def norm(a):
    for z in a:
        if z:
            k = inv[z]
            # A leading-one chart is an alternative canonical normalization.
            out = tuple(M[x][k] for x in a)
            assert out[0] == 1 or (out[0] == 0 and out[1] == 1)
            return out
    raise AssertionError('zero vector')

def cross(a, b):
    return norm((M[a[1]][b[2]] ^ M[a[2]][b[1]],
                 M[a[2]][b[0]] ^ M[a[0]][b[2]],
                 M[a[0]][b[1]] ^ M[a[1]][b[0]]))

def dot(a, b):
    return M[a[0]][b[0]] ^ M[a[1]][b[1]] ^ M[a[2]][b[2]]

# The cubic is smooth because its homogeneous partials in char 2 are
# dF/dX=X^2, dF/dY=Z^2, dF/dZ=Y^2, with no common projective zero.
E = {(0, 1, 0)} | {
    (a, b, 1) for a in range(64) for b in range(64)
    if M[b][b] ^ b ^ M[M[a][a]][a] == 0
}
assert len(E) == 81

# Method A: form secant lines using unordered pairs of rational curve points.
contact = defaultdict(set)
for a, b in combinations(sorted(E), 2):
    contact[cross(a, b)].update((a, b))
assert Counter(map(len, contact.values())) == {3: 1056, 2: 72}
three_lines = {line for line, ps in contact.items() if len(ps) == 3}
N_a = {point: 0 for point in P}
for line in three_lines:
    for point in P:
        N_a[point] += int(dot(line, point) == 0)

# Method B: count the distinct roots of each nonvertical line's cubic.
# The affine line Y=mX+c cuts the curve in X^3+(mX+c)^2+(mX+c)=0.
# Requiring three *distinct* roots is essential (tangencies do not count).
root_count = {}
for m in range(64):
    for c in range(64):
        root_count[m, c] = sum(
            (M[M[x][x]][x] ^ M[M[m][x] ^ c][M[m][x] ^ c]
             ^ M[m][x] ^ c) == 0 for x in range(64))
assert Counter(root_count.values()) == {0: 1080, 1: 1928, 2: 72, 3: 1016}
# The 64 vertical projective lines X=aZ and the line at infinity have
# characters 1 or 3. Their contribution is computed separately.
vert_3 = {a for a in range(64) if sum(
    (M[y][y] ^ y ^ M[M[a][a]][a]) == 0 for y in range(64)) == 2}
assert len(vert_3) == 40
N_b = {}
for point in P:
    if point[2]:
        a, b, _ = point
        N_b[point] = sum(root_count[m, b ^ M[m][a]] == 3
                         for m in range(64)) + int(a in vert_3)
    else:
        if point == (0, 1, 0):
            N_b[point] = len(vert_3)
        else:
            # A point (1:m:0) is on the 64 affine lines of slope m;
            # the line Z=0 meets E only at infinity, with multiplicity 3.
            m = point[1]
            N_b[point] = sum(root_count[m, c] == 3 for c in range(64))
assert N_a == N_b

Nout = Counter(N_a[p] for p in P if p not in E)
Non = Counter(N_a[p] for p in E)
assert Nout == {11: 72, 14: 648, 16: 2052, 17: 864, 18: 432, 26: 12}
assert Non == {39: 72, 40: 9}
assert sum(Nout.values()) == 4161 - 81
assert sum(j * count for j, count in Nout.items()) == 1056 * (65 - 3)
assert sum(j * count for j, count in Non.items()) == 1056 * 3

# The extreme 26-split-fiber centers are exactly the 12 noncurve
# points of the embedded F4-subplane.
F4 = {p for p in P if all(power(z, 4) == z for z in p)}
assert len(F4) == 21 and len(F4 & E) == 9
assert {p for p in P if p not in E and N_a[p] == 26} == F4 - E

# Global hyperplane-section characters; determined *again* by lines.
line_char = Counter(sum(dot(l, p) == 0 for p in E) for l in P)
assert line_char == {0: 1080, 1: 1953, 2: 72, 3: 1056}
assert sum(t * n for t, n in line_char.items()) == len(E) * 65
assert sum(t * (t-1)//2 * n for t, n in line_char.items()) == 81*80//2
print('EXTERIOR_SPLIT_PROFILE', dict(sorted(Nout.items())))
print('ON_CURVE_SPLIT_PROFILE', dict(sorted(Non.items())))
print('LINE_SECTION_PROFILE', dict(sorted(line_char.items())))
print('F4_OUTSIDE_EXTREMALS', len(F4-E))
print('VERIFY_OK')
