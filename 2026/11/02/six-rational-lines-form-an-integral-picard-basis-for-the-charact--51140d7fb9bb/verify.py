"""Exact arithmetic certificate for the characteristic-two Clebsch cubic.

No third-party dependencies. GF(4)=GF(2)[t]/(t*t+t+1). Coordinates for
P^3 are the first four of five coordinates constrained by their sum zero.
"""
from itertools import combinations, product


def mul(a, b):
    out = 0
    for i in range(2):
        if (b >> i) & 1:
            out ^= a << i
    if out & 8:
        out ^= 0b1100
    if out & 4:
        out ^= 0b0111
    return out


def power(a, n):
    b = 1
    while n:
        if n & 1:
            b = mul(b, a)
        a = mul(a, a)
        n //= 2
    return b


def inv(a):
    assert a
    return power(a, 2)


def normalize(v):
    if not any(v):
        return None
    x = next(t for t in v if t)
    return tuple(mul(inv(x), t) for t in v)


def addvec(v, w):
    return tuple(x ^ y for x, y in zip(v, w))


def scale(c, v):
    return tuple(mul(c, x) for x in v)


def on_cubic(v):
    fifth = 0
    for x in v:
        fifth ^= x
    return (sum(power(x, 3) for x in v) + power(fifth, 3)) % 2 == 0


def det_bareiss(rows):
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    denom = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % denom == 0
                a[i][j] = numerator // denom
        for i in range(k + 1, n):
            a[i][k] = 0
        denom = pivot
    return sign * a[-1][-1]


# Surface rational points over F4 in the restricted four-dimensional space.
P = sorted({normalize(v) for v in product(range(4), repeat=4)} - {None})
assert len(P) == 85
S = {v for v in P if on_cubic(v)}
assert len(S) == 45

# Enumerate ALL projective lines over F4; each has five points.
lines = set()
for v, w in combinations(P, 2):
    points = {normalize(addvec(v, scale(c, w))) for c in range(4)}
    points.add(w)
    assert len(points) == 5
    lines.add(frozenset(points))
assert len(lines) == 357
S_lines = {ell for ell in lines if ell <= S}
assert len(S_lines) == 27

def frob(v):
    return normalize(tuple(power(x, 2) for x in v))

def frob_line(ell):
    return frozenset(frob(v) for v in ell)

assert all(frob_line(ell) in S_lines for ell in S_lines)
fixed = {ell for ell in S_lines if frob_line(ell) == ell}
assert len(fixed) == 15
assert all(frob_line(frob_line(ell)) == ell for ell in S_lines)

# The field F2 points of the original five-coordinate hyperplane are
# the nonzero even-weight binary vectors.
even = sorted(x for x in range(1, 32) if x.bit_count() % 2 == 0)
assert len(even) == 15
F2_lines = sorted({tuple(sorted((a, b, a ^ b)))
                   for a, b in combinations(even, 2)
                   if (a & b).bit_count() % 2 == 0})
assert len(F2_lines) == 15

def f2_point_to_f4(v):
    x = tuple((v >> i) & 1 for i in range(4))
    assert ((v >> 4) & 1) == (x[0] ^ x[1] ^ x[2] ^ x[3])
    return normalize(x)

F2_line_sets = set()
for triple in F2_lines:
    a, b, _ = triple
    u, v = f2_point_to_f4(a), f2_point_to_f4(b)
    ell = frozenset({normalize(addvec(u, scale(c, v))) for c in range(4)} | {v})
    assert ell in S_lines
    F2_line_sets.add(ell)
assert F2_line_sets == fixed

# The six listed F2-lines are spanned by coordinate indicator pairs.
# Bits encode e_0, e_1, ..., e_4.
chosen = [(3, 12, 15), (3, 20, 23), (3, 24, 27),
          (5, 10, 15), (5, 18, 23), (9, 18, 27)]
assert all(tr in F2_lines for tr in chosen)
G = [[(-1 if i == j else (1 if set(chosen[i]) & set(chosen[j]) else 0))
      for j in range(6)] for i in range(6)]
assert G == [
    [-1, 1, 1, 1, 0, 0],
    [1, -1, 1, 0, 1, 0],
    [1, 1, -1, 0, 0, 1],
    [1, 0, 0, -1, 1, 0],
    [0, 1, 0, 1, -1, 1],
    [0, 0, 1, 0, 1, -1],
]
assert det_bareiss(G) == -2

print('CLEBSCH_SURFACE_F2_POINTS=15')
print('F4_PROJECTIVE_LINES=357; F4_SURFACE_POINTS=45')
print('GEOMETRIC_CUBIC_LINES_F4=27; F2_LINES=15; FROBENIUS_2_CYCLES=6')
print('SELECTED_SIX_LINE_INTERSECTION_DETERMINANT=-2')
print('VERIFICATION_OK')
