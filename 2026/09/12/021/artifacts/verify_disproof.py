"""Independent exact verifier for the K2P single-triangle quarnet lower bound.

This version uses the phylogenetically correct root-edge Fourier exponent
rc = g1+g2+g3 = g4 (for G = Z2 x Z2 and consistent leaf patterns).
It rebuilds the Fourier mixture map, evaluates its exact rational Jacobian
at an explicit torus point, certifies rank >= 13 by a nonzero 13x13 minor,
and verifies that the displayed-tree monomial exponent matrix has rank 10.
"""
from fractions import Fraction

Z = (0, 0); T = (0, 1); V1 = (1, 0); V2 = (1, 1)
G = [Z, T, V1, V2]

def add(a, b):
    return ((a[0] + b[0]) & 1, (a[1] + b[1]) & 1)

def cls(g):
    if g == Z:
        return 0
    if g == T:
        return 1
    return 2

PATS = [(a, b, c, d) for a in G for b in G for c in G for d in G
        if add(add(add(a, b), c), d) == Z]
assert len(PATS) == 64

def L1(p):
    g1, g2, g3, g4 = p
    s = add(g1, g2)
    # Correct Fourier exponent on the root edge:
    # g1+g2+g3 = -g4 = g4 in Z2 x Z2.
    return [("bh", g1), ("h1", g1), ("b2", g2), ("c3", g3), ("r4", g4),
            ("ab", s), ("ca", s), ("rc", g4)]

def L2(p):
    g1, g2, g3, g4 = p
    s = add(g1, g2)
    return [("ah", g1), ("h1", g1), ("ab", g2), ("b2", g2), ("c3", g3),
            ("r4", g4), ("ca", s), ("rc", g4)]

EN = ["rc", "r4", "ca", "c3", "ab", "b2", "ah", "bh", "h1"]
VCOLS = [(e, k) for e in EN for k in (1, 2)] + ["d"]

def mon(L, t, s):
    m = Fraction(1)
    for e, x in L:
        c = cls(x)
        if c == 1:
            m *= t[e]
        elif c == 2:
            m *= s[e]
    return m

def jrow(p, t, s, dl):
    A, B = L1(p), L2(p)
    m1, m2 = mon(A, t, s), mon(B, t, s)
    row = []
    for c in VCOLS:
        if c == "d":
            row.append(m1 - m2)
            continue
        e, k = c
        v = t[e] if k == 1 else s[e]
        n1 = sum(1 for f, x in A if f == e and cls(x) == k)
        n2 = sum(1 for f, x in B if f == e and cls(x) == k)
        d = Fraction(0)
        if n1:
            d += dl * m1 * n1 / v
        if n2:
            d += (Fraction(1) - dl) * m2 * n2 / v
        row.append(d)
    return row

def rank_of(rows):
    R = [list(r) for r in rows]
    nr, nc = len(R), len(R[0])
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if R[i][c] != 0), None)
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        for i in range(nr):
            if i != r and R[i][c] != 0:
                f = R[i][c] / R[r][c]
                for j in range(c, nc):
                    R[i][j] -= f * R[r][j]
        r += 1
        if r == nr:
            break
    return r

def bareiss_det(M):
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    prev = Fraction(1)
    sign = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            assert piv is not None, "singular minor"
            A[k], A[piv] = A[piv], A[k]
            sign *= -1
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) / prev
            A[i][k] = Fraction(0)
        prev = A[k][k]
        assert prev != 0
    return sign * A[n - 1][n - 1]

t0 = {e: Fraction(2 + i, 3) for i, e in enumerate(EN)}
s0 = {e: Fraction(1 + i, 4) for i, e in enumerate(EN)}
dl = Fraction(1, 5)

J = [jrow(p, t0, s0, dl) for p in PATS]
rk = rank_of(J)
print("corrected network Jacobian rank:", rk)
assert rk >= 13

rows = [1, 2, 4, 5, 8, 10, 16, 20, 24, 32, 36, 40, 44]
cols = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
det = bareiss_det([[J[i][j] for j in cols] for i in rows])
print("rows:", rows)
print("cols:", [VCOLS[j] for j in cols])
print("corrected det13 =", det)
assert det == Fraction(160576479, 4194304)

# Displayed-tree monomial map: exact exponent-matrix rank gives its image dimension.
TREE_COLS = [(e, k) for e in sorted({f for p in PATS for f, _ in L1(p)})
             for k in (1, 2)]

def exponent_row(p):
    A = L1(p)
    return [sum(1 for f, x in A if f == e and cls(x) == k)
            for e, k in TREE_COLS]

E = [exponent_row(p) for p in PATS]
tree_rank = rank_of(E)
print("displayed-tree exponent rank:", tree_rank)
assert tree_rank == 10

# Independent torus-Jacobian cross-check for the displayed tree.
def tree_jrow(p):
    A = L1(p)
    m = mon(A, t0, s0)
    out = []
    for e, k in TREE_COLS:
        n = sum(1 for f, x in A if f == e and cls(x) == k)
        v = t0[e] if k == 1 else s0[e]
        out.append(m * n / v if n else Fraction(0))
    return out

assert rank_of([tree_jrow(p) for p in PATS]) == 10
print("VERIFY_OK")
