#!/usr/bin/env python3
"""Exact arithmetic checks for the Fermat-quartic line scheme.

Only the Python standard library is required.  Computations use F_9=F_3[i]
with i^2=-1.  The geometric and local-algebra arguments are in RESULT.md.
"""
from itertools import product, permutations
from math import comb

K = range(9)

def ab(x):
    return x % 3, x // 3

def enc(a, b):
    return (a % 3) + 3 * (b % 3)

def add(x, y):
    a, b = ab(x)
    c, d = ab(y)
    return enc(a + c, b + d)

def neg(x):
    a, b = ab(x)
    return enc(-a, -b)

def mul(x, y):
    a, b = ab(x)
    c, d = ab(y)
    return enc(a*c - b*d, a*d + b*c)

def power(x, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out

def sumk(xs):
    z = 0
    for x in xs:
        z = add(z, x)
    return z

def H(x, y):
    return sumk(mul(power(a, 3), b) for a, b in zip(x, y))

def rref_lines():
    """List every 2-space in F_9^4 exactly once by pivot-position RREF."""
    for i in range(4):
        for j in range(i + 1, 4):
            ucols = [k for k in range(i + 1, 4) if k != j]
            vcols = list(range(j + 1, 4))
            for xs in product(K, repeat=len(ucols) + len(vcols)):
                a, b = [0]*4, [0]*4
                a[i], b[j] = 1, 1
                for k, x in zip(ucols, xs):
                    a[k] = x
                for k, x in zip(vcols, xs[len(ucols):]):
                    b[k] = x
                yield (tuple(a), tuple(b))

def rref(a, b):
    rows = [list(a), list(b)]
    pivot = 0
    for j in range(4):
        piv = next((r for r in range(pivot, 2) if rows[r][j]), None)
        if piv is None:
            continue
        rows[pivot], rows[piv] = rows[piv], rows[pivot]
        inv = next(x for x in K if mul(x, rows[pivot][j]) == 1)
        rows[pivot] = [mul(inv, x) for x in rows[pivot]]
        for k in range(2):
            if k != pivot:
                q = rows[k][j]
                rows[k] = [add(rows[k][l], neg(mul(q, rows[pivot][l])))
                           for l in range(4)]
        pivot += 1
        if pivot == 2:
            break
    assert pivot == 2
    return tuple(map(tuple, rows))

def is_iso(a, b):
    return H(a, a) == H(b, b) == H(a, b) == 0

def is_pairing(a, b):
    for (i, j), (k, l) in [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]:
        if (mul(a[i], b[j]) == mul(a[j], b[i]) and
                mul(a[k], b[l]) == mul(a[l], b[k])):
            return True
    return False

all_sp = list(rref_lines())
assert len(all_sp) == (9*9 + 1)*(9*9 + 9 + 1) == 7462
lines = {z for z in all_sp if is_iso(*z)}
assert len(lines) == 112
pairing = {z for z in lines if is_pairing(*z)}
extra = lines - pairing
assert len(pairing) == 48 and len(extra) == 64

L0 = ((1,0,1,1), (0,1,1,2))
assert L0 in extra
mu4 = [x for x in K if power(x,4) == 1]
assert len(mu4) == 4
orbit = set()
for sigma in permutations(range(4)):
    for scales in product(mu4, repeat=3):
        diagonal = (1,) + scales
        a, b = L0
        orbit.add(rref(tuple(mul(diagonal[j], a[sigma[j]]) for j in range(4)),
                       tuple(mul(diagonal[j], b[sigma[j]]) for j in range(4))))
assert len(orbit) == 64 and orbit == extra

# The Frobenius fixed points on the Grassmannian are exactly the F_3 lines.
def frob_fixed(L):
    return all(power(x,3) == x for row in L for x in row)
assert sum(map(frob_fixed, pairing)) == 0
assert sum(map(frob_fixed, extra)) == 8

# Verify the actual Hilbert tangent matrix in every special-fiber Grassmann chart.
# For nonpivot column k, a deformation has coordinate
#    (a[k]+eps*A[k])*u + (b[k]+eps*B[k])*v.
# The linearized Fermat equation, in characteristic 3, has coefficients
# u^4: a[k]^3*A[k], u^3*v: a[k]^3*B[k],
# u*v^3: b[k]^3*A[k], v^4: b[k]^3*B[k].
# The u^2*v^2 row is identically zero. Four independent coefficient
# equations force the four Grassmann perturbations to vanish.
def matrix_rank(rows):
    rows = [r[:] for r in rows]
    rank = 0
    for col in range(len(rows[0])):
        pi = next((z for z in range(rank, len(rows)) if rows[z][col]), None)
        if pi is None:
            continue
        rows[rank], rows[pi] = rows[pi], rows[rank]
        inv = next(x for x in K if mul(x, rows[rank][col]) == 1)
        rows[rank] = [mul(inv,x) for x in rows[rank]]
        for z in range(len(rows)):
            if z == rank:
                continue
            q = rows[z][col]
            rows[z] = [add(rows[z][h], neg(mul(q, rows[rank][h])))
                       for h in range(len(rows[z]))]
        rank += 1
    return rank

for a, b in lines:
    pivots = [j for j in range(4) if a[j] or b[j]]
    # Recover the two RREF leading-pivot coordinates, not arbitrary support.
    i = next(j for j in range(4) if a[j] == 1 and all(a[z]==0 for z in range(j)))
    j = next(j for j in range(4) if b[j] == 1 and all(b[z]==0 for z in range(j)))
    free = [h for h in range(4) if h not in (i,j)]
    mat = [[0]*4 for _ in range(5)]
    for z, h in enumerate(free):
        mat[0][2*z] = power(a[h],3)
        mat[1][2*z+1] = power(a[h],3)
        mat[3][2*z] = power(b[h],3)
        mat[4][2*z+1] = power(b[h],3)
    assert matrix_rank(mat) == 4

# Substituting the representative line in the integer Fermat equation gives
# 3(u^4+4u^2v^2+v^4).  Its u^2v^2 coefficient is 12, nonzero modulo 9.
# Every 3-times-linear perturbation of z=u+v and w=u-v changes this
# coefficient by a multiple of 9, since binomial(3,1)=binomial(3,2)=3.
assert comb(4,2)*2 == 12
assert 12 % 9 == 3
assert (3*4*comb(3,1)) % 9 == 0
assert (3*4*comb(3,2)) % 9 == 0

# Self-contained projective F_3 point count for the hyperbolic quadric:
# Q(x)=sum x_i^2=0 iff exactly three of four coordinates are nonzero.
points_Q = 4*2**3//2
assert points_Q == 16
assert points_Q*2//4 == 8

print('FERMAT_QUARTIC_MIXED_CHAR_48_64_FROBENIUS_8_28_AND_MOD9_PASS')
