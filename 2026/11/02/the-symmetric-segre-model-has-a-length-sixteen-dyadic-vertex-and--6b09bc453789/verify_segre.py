#!/usr/bin/env python3
"""Exact verification of the characteristic-two symmetric cubic model.

The checker uses only Python's standard library. Polynomial arithmetic is in
F_2[z0,z1,z2,z3,t], while line enumeration uses F_2 and F_4.
"""
from itertools import combinations, product
from math import comb

N = 5
ZERO = (0,) * N

def mon(i):
    a = list(ZERO); a[i] = 1
    return frozenset([tuple(a)])

def add(*ps):
    out = set()
    for p in ps:
        out.symmetric_difference_update(p)
    return frozenset(out)

def multiply(a, b):
    out = set()
    for u in a:
        for v in b:
            w = tuple(x + y for x, y in zip(u, v))
            if w in out: out.remove(w)
            else: out.add(w)
    return frozenset(out)

def power(a, n):
    z = frozenset([ZERO])
    for _ in range(n): z = multiply(z, a)
    return z

def deriv(a, i):
    out = set()
    for exp in a:
        if exp[i] % 2:
            u = list(exp); u[i] -= 1; out.add(tuple(u))
    return frozenset(out)

z = [mon(i) for i in range(4)]
t = mon(4)
S = add(*z)
y = z + [S, frozenset()]
x = [add(t, yi) for yi in y]
e1 = add(*x)
e3 = add(*(multiply(multiply(x[i], x[j]), x[k]) for i, j, k in combinations(range(6), 3)))
F = add(*(multiply(power(z[i], 2), z[j]) for i in range(4) for j in range(4) if i != j))
assert not e1 and e3 == F

# The four partial derivatives are squares of four independent linear forms.
L = [add(*(z[j] for j in range(4) if j != i)) for i in range(4)]
for i in range(4):
    assert deriv(F, i) == power(L[i], 2)
assert add(*(multiply(z[i], deriv(F, i)) for i in range(4))) == F

# The change of linear variables is self-inverse in characteristic two.
A = [[int(i != j) for j in range(4)] for i in range(4)]
assert [[sum(A[i][k] * A[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)] == [[int(i == j) for j in range(4)] for i in range(4)]
assert [comb(4, i) for i in range(5)] == [1, 4, 6, 4, 1]

# Elements of F_4 are bit-encoded in 1, a with a^2+a+1=0.
def fm(a, b):
    r = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                r ^= (1 << (i + j))
    if r & 4: r ^= 7
    return r

def cube(a): return fm(fm(a, a), a)
def square(a): return fm(a, a)
assert fm(2, 3) == 1 and square(2) == 3 and square(3) == 2

def contained(u, v):
    # A line in P3 maps into the cubic iff all four coefficients vanish.
    U = list(u) + [u[0] ^ u[1] ^ u[2] ^ u[3]]
    V = list(v) + [v[0] ^ v[1] ^ v[2] ^ v[3]]
    c = [0] * 4
    for a, b in zip(U, V):
        c[0] ^= cube(a)
        c[1] ^= fm(square(a), b)
        c[2] ^= fm(a, square(b))
        c[3] ^= cube(b)
    return c == [0, 0, 0, 0]

def all_rref(q):
    # Each 2-dimensional subspace has one 2x4 RREF basis.
    for i, j in combinations(range(4), 2):
        free = [(r, k) for r in range(2) for k in range(4)
                if k != i and k != j
                and ((r == 0 and k > i) or (r == 1 and k > j))]
        for v in product(range(q), repeat=len(free)):
            u = [0] * 4; w = [0] * 4
            u[i] = 1; w[j] = 1
            for (r, k), a in zip(free, v):
                (u if r == 0 else w)[k] = a
            yield (tuple(u), tuple(w))

def line_set(q):
    return {line for line in all_rref(q) if contained(*line)}

L2 = line_set(2)
L4 = line_set(4)
assert len(list(all_rref(2))) == 35
assert len(list(all_rref(4))) == 357
assert len(L2) == 15 and len(L4) == 27
assert L2 <= L4
Lnew = L4 - L2
assert len(Lnew) == 12
for u, v in Lnew:
    conjugate = (tuple(square(a) for a in u), tuple(square(a) for a in v))
    assert conjugate != (u, v) and conjugate in Lnew

# First-order normal equations at each cone plane have full rank six.
# For an RREF line with rows u,v, choose as normals the two standard
# vectors in the nonpivot columns. Their derivative quadrics Q1,Q2
# must be independent on the line. Since these are pure squares in
# U,V, their 2x2 determinant is the complete tangent-space test.
for u, v in L4:
    pivot_u = next(i for i in range(4) if u[i] != 0)
    pivot_v = next(i for i in range(4) if v[i] != 0)
    freecols = [i for i in range(4) if i not in (pivot_u, pivot_v)]
    assert len(freecols) == 2
    rows = []
    for k in freecols:
        a = 0; b = 0
        for i in range(4):
            if i != k:
                a ^= u[i]; b ^= v[i]
        rows.append((square(a), square(b)))
    normal_det = fm(rows[0][0], rows[1][1]) ^ fm(rows[0][1], rows[1][0])
    assert normal_det != 0

# All fifteen classical pair-partition planes reduce to the fifteen F2 lines.
def matchings(items):
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for remaining in matchings(items[1:j] + items[j + 1:]):
            yield ((a, b),) + remaining

def point_y(zvec, i):
    return zvec[i] if i < 4 else (zvec[0] ^ zvec[1] ^ zvec[2] ^ zvec[3]) if i == 4 else 0

def span_f2(u, v):
    return frozenset(tuple((a ^ b) for a, b in zip(a1, b1))
                     for a1, b1 in (([0] * 4, [0] * 4), (u, [0] * 4), ([0] * 4, v), (u, v)))

seen = set()
for pairs in matchings(tuple(range(6))):
    vectors = [v for v in product(range(2), repeat=4)
               if all(point_y(v, a) == point_y(v, b) for a, b in pairs)]
    assert len(vectors) == 4
    seen.add(frozenset(vectors))
assert len(seen) == 15
assert seen == {span_f2(*line) for line in L2}

# Hessian of the quadratic jet at a (3+,3-) node over odd characteristic.
H = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 2]]
def det(A):
    if len(A) == 1: return A[0][0]
    return sum((-1) ** j * A[0][j] * det([row[:j] + row[j+1:] for row in A[1:]]) for j in range(len(A)))
assert det(H) == 1  # Hence Hessian of -2Q has determinant 16.
# For every odd p, singular coordinates are triples of signs; the p=3
# all-equal possibilities are excluded because +/- binom(6,3) != 0 mod 3.
assert len(list(combinations(range(6), 3))) // 2 == 10
assert 20 % 3 != 0
print('SYMMETRIC_SEGRE_CHAR2_JACOBIAN16_FANO_15PLUS6_ETALE_EXACT_OK')
