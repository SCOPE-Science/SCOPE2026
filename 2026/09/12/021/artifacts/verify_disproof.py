"""Independent verification (stdlib only, no sympy) that the K2P
single-triangle quarnet variety does NOT have dimension 7.

Rebuilds the Fourier mixture map from scratch, evaluates its exact QQ
Jacobian at an explicit rational point, and certifies rank >= 13 via a
nonzero 13x13 minor (Bareiss determinant), plus rank >= 10 for the
displayed tree. Prints VERIFY_OK.
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
    return [("bh", g1), ("h1", g1), ("b2", g2), ("c3", g3), ("r4", g4),
            ("ab", s), ("ca", s), ("rc", s)]

def L2(p):
    g1, g2, g3, g4 = p
    s = add(g1, g2)
    return [("ah", g1), ("h1", g1), ("ab", g2), ("b2", g2), ("c3", g3),
            ("r4", g4), ("ca", s), ("rc", s)]

EN = ["rc", "r4", "ca", "c3", "ab", "b2", "ah", "bh", "h1"]
VCOLS = [(e, k) for e in EN for k in (1, 2)] + ["d"]

def mon(L, t, s):
    m = Fraction(1)
    for (e, x) in L:
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
        d = Fraction(0)
        n1 = sum(1 for (f, x) in A if f == e and cls(x) == k)
        n2 = sum(1 for (f, x) in B if f == e and cls(x) == k)
        v = t[e] if k == 1 else s[e]
        if n1:
            d += dl * m1 * n1 / v
        if n2:
            d += (Fraction(1) - dl) * m2 * n2 / v
        row.append(d)
    return row

def bareiss_det(M):
    n = len(M)
    A = [[Fraction(x) for x in r] for r in M]
    prev = Fraction(1)
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            assert piv is not None, "zero pivot: minor singular"
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) / prev
            A[i][k] = Fraction(0)
        prev = A[k][k]
        assert prev != 0, "zero pivot: minor singular"
    return A[n - 1][n - 1]

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

t0 = {e: Fraction(2 + i, 3) for i, e in enumerate(EN)}
s0 = {e: Fraction(1 + i, 4) for i, e in enumerate(EN)}
dl = Fraction(1, 5)
J = [jrow(p, t0, s0, dl) for p in PATS]
rk = rank_of(J)
print("network Jacobian rank:", rk)
assert rk >= 13

# greedy independent rows / cols -> 13x13 minor
sel = []
for i in range(64):
    if rank_of([J[i] for i in sel + [i]]) == len(sel) + 1:
        sel.append(i)
assert len(sel) >= 13
sel = sel[:13]
sub = [[J[i][j] for j in range(19)] for i in sel]
csel = []
for j in range(19):
    if rank_of([[r[k] for k in csel + [j]] for r in sub]) == len(csel) + 1:
        csel.append(j)
assert len(csel) >= 13
csel = csel[:13]
det = bareiss_det([[J[sel[i]][csel[j]] for j in range(13)] for i in range(13)])
print("rows:", sel)
print("cols:", [VCOLS[j] for j in csel])
print("det13 =", det)
assert det != 0

# displayed-tree rank >= 10
def trow(p, t, s):
    A = L1(p)
    m = mon(A, t, s)
    edges = sorted(set(f for (f, _) in A))
    row = []
    for e in edges:
        for k in (1, 2):
            n = sum(1 for (f, x) in A if f == e and cls(x) == k)
            row.append(m * n / (t[e] if k == 1 else s[e]) if n else Fraction(0))
    return row
Jt = [trow(p, t0, s0) for p in PATS]
print("tree Jacobian rank:", rank_of(Jt))
assert rank_of(Jt) >= 10
print("VERIFY_OK")
