from itertools import combinations, permutations
from collections import defaultdict
from fractions import Fraction

verts = [tuple((i >> j) & 1 for j in range(4)) for i in range(16)]

def det_int(M):
    # Bareiss exact determinant.
    A = [list(map(int, row)) for row in M]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]

def cls(v):
    w = sum(v)
    return 0 if w in (0,4) else (1 if w in (1,3) else 2)

P = defaultdict(int)
for I in combinations(range(16), 5):
    M = [list(verts[i]) + [1] for i in I]
    vol = abs(det_int(M))
    if vol == 0:
        continue
    e = [0,0,0]
    for i in I:
        e[cls(verts[i])] += 1
    P[tuple(e)] += vol

expected_P = {
    (2,3,0):32, (2,2,1):96, (2,1,2):96, (2,0,3):16,
    (1,4,0):132, (1,3,1):480, (1,2,2):624, (1,1,3):336, (1,0,4):48,
    (0,5,0):64, (0,4,1):396, (0,3,2):576, (0,2,3):368, (0,1,4):96,
}
assert dict(P) == expected_P

def add(p, q):
    r = defaultdict(int)
    for m,c in p.items(): r[m] += c
    for m,c in q.items(): r[m] += c
    return {m:c for m,c in r.items() if c}

def scale(p, s):
    return {m:c*s for m,c in p.items() if c*s}

def mul(p, q):
    r = defaultdict(int)
    for m,c in p.items():
        for n,d in q.items():
            r[tuple(m[i]+n[i] for i in range(3))] += c*d
    return {m:c for m,c in r.items() if c}

def power(p, n):
    r = {(0,0,0):1}
    for _ in range(n):
        r = mul(r,p)
    return r

a = {(1,0,0):1}
b = {(0,1,0):1}
c = {(0,0,1):1}
S = add(add(a, scale(b,4)), scale(c,3))
Ppoly = dict(P)

A = {
    (0,2,1):58295, (0,3,0):37269, (1,1,1):179836,
    (1,2,0):69930, (2,0,1):10710, (2,1,0):12600,
}
B = {
    (0,0,3):133209, (0,1,2):292940, (0,2,1):357151,
    (0,3,0):214635, (2,0,1):51915, (3,0,0):56070,
}
C = {
    (0,0,3):19881, (0,1,2):404254, (0,2,1):556128,
    (0,3,0):296583, (1,1,1):104924, (3,0,0):630,
}

ab2 = power(add(a, scale(b,-1)), 2)
bc2 = power(add(b, scale(c,-1)), 2)
ac2 = power(add(a, scale(c,-1)), 2)

lhs = scale(add(scale(power(S,5),105), scale(Ppoly,-1024)), 6)
rhs = add(add(mul(ab2,A), mul(bc2,B)), mul(ac2,C))
assert lhs == rhs

# Facet count check for the three classes.
for coord in range(4):
    for bit in (0,1):
        counts = [0,0,0]
        for v in verts:
            if v[coord] == bit:
                counts[cls(v)] += 1
        assert counts == [1,4,3]

# Equality value at uniform weights.
P1 = sum(P.values())
S1 = 8
assert P1 == 3360
assert Fraction(8*P1, S1**5) == Fraction(105,128)

# Every coefficient of the certificate multipliers is strictly positive,
# and B,C contain positive pure cubes in all three variables.
assert all(v > 0 for v in A.values())
assert all(v > 0 for v in B.values())
assert all(v > 0 for v in C.values())
for E in ((3,0,0),(0,3,0),(0,0,3)):
    assert B[E] > 0
    assert C[E] > 0

print("VERIFY_OK")
print("five_vertex_subsets=4368")
print("nonzero_specialized_monomials=14")
print("uniform_ratio=105/128")
print("certificate_identity=true")
