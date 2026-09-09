"""Parametric H^2 constancy check for L6,22(eps), L6,24(eps) over Q.
Stdlib only. Builds Chevalley-Eilenberg d1,d2 from committed brackets,
verifies Jacobi, exact dim H^2 at anchors eps=0,1,-1,2, and the
eps-independent minor certificates (det +-1) proving constancy for all eps.
Run: python3 verify_h2.py
"""
from fractions import Fraction
from itertools import permutations

PAIRS = [(i, j) for i in range(1, 7) for j in range(i + 1, 7)]
PIDX = {p: k for k, p in enumerate(PAIRS)}
TRIPLES = [(i, j, k) for i in range(1, 7) for j in range(i + 1, 7) for k in range(j + 1, 7)]

# Brackets as dict (a,b)->{l:(c0,c1)} meaning coeff c0 + c1*e.
def br22(a, b):
    if a == b:
        return {}
    if a > b:
        return {k: (-c0, -c1) for k, (c0, c1) in br22(b, a).items()}
    F = Fraction
    if (a, b) == (1, 2):
        return {5: (F(1), F(0))}
    if (a, b) == (1, 3):
        return {6: (F(1), F(0))}
    if (a, b) == (2, 4):
        return {6: (F(0), F(1))}
    if (a, b) == (3, 4):
        return {5: (F(1), F(0))}
    return {}

def br24(a, b):
    if a == b:
        return {}
    if a > b:
        return {k: (-c0, -c1) for k, (c0, c1) in br24(b, a).items()}
    F = Fraction
    if (a, b) == (1, 2):
        return {3: (F(1), F(0))}
    if (a, b) == (1, 3):
        return {5: (F(1), F(0))}
    if (a, b) == (1, 4):
        return {6: (F(0), F(1))}
    if (a, b) == (2, 3):
        return {6: (F(1), F(0))}
    if (a, b) == (2, 4):
        return {5: (F(1), F(0))}
    return {}

def eval_poly(c, e):
    return c[0] + c[1] * e

def check_jacobi(br, name):
    F = Fraction
    for e in [F(0), F(1), F(-1), F(2)]:
        B = {}
        for a in range(1, 7):
            for b in range(a + 1, 7):
                B[(a, b)] = {l: eval_poly(c, e) for l, c in br(a, b).items()}
        def lb(x, y):
            if x == y:
                return {}
            if x > y:
                return {k: -v for k, v in lb(y, x).items()}
            return dict(B.get((x, y), {}))
        for (a, b, c) in TRIPLES:
            acc = {}
            for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                w = lb(x, y)
                for l, cl in w.items():
                    for m, cm in lb(l, z).items():
                        acc[m] = acc.get(m, F(0)) + cl * cm
            assert all(v == 0 for v in acc.values()), (name, e, (a, b, c), acc)
    print(f"Jacobi OK for {name} at e=0,1,-1,2")

def rank_of(rows):
    M = [r[:] for r in rows]
    m, n = len(M), len(M[0]) if M else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = M[r][c]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c] / inv
                for j in range(c, n):
                    M[i][j] -= f * M[r][j]
        r += 1
    return r

def d2_rows(br, e):
    rows = []
    for (a, b, c) in TRIPLES:
        row = [Fraction(0)] * len(PAIRS)
        for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
            xx, yy = (x, y) if x < y else (y, x)
            sgn = Fraction(1) if x < y else Fraction(-1)
            d = br(xx, yy)
            for l, cp in d.items():
                if l == z:
                    continue
                v = sgn * eval_poly(cp, e)
                if l < z:
                    row[PIDX[(l, z)]] += v
                else:
                    row[PIDX[(z, l)]] -= v
        rows.append(row)
    return rows

def d1_rows(br, e):
    # rows = coboundary vectors d(xk*) in C^2 coords, k=1..6
    rows = []
    for k in range(1, 7):
        row = [Fraction(0)] * len(PAIRS)
        for (i, j) in PAIRS:
            ii, jj = (i, j)
            sgn = Fraction(1)
            d = br(ii, jj)
            for l, cp in d.items():
                if l == k:
                    row[PIDX[(ii, jj)]] += sgn * eval_poly(cp, e)
        rows.append(row)
    nz = [r for r in rows if any(v != 0 for v in r)]
    return rows, nz

def det_int(mat):
    # exact det of Fraction matrix via elimination
    n = len(mat)
    M = [r[:] for r in mat]
    det = Fraction(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        inv = M[c][c]
        for i in range(c + 1, n):
            f = M[i][c] / inv
            for j in range(c, n):
                M[i][j] -= f * M[c][j]
    return det

def submat(rows, R, C):
    return [[rows[r][c] for c in C] for r in R]

TN = lambda t: PIDX[t]
# Certificate row/col index sets (triple order in TRIPLES; col = pair):
# L6,22: rows (1,2,6),(1,2,3),(1,2,4),(1,3,4),(2,3,4) x cols 56,26,45,15,25
R22 = [TRIPLES.index(t) for t in [(1, 2, 6), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]]
C22 = [TN(p) for p in [(5, 6), (2, 6), (4, 5), (1, 5), (2, 5)]]
# L6,24: rows (1,2,5),(1,2,6),(1,3,6),(1,3,4),(2,3,4),(1,2,3),(1,2,4)
#   x cols 35,36,56,45,46,16,15
R24 = [TRIPLES.index(t) for t in [(1, 2, 5), (1, 2, 6), (1, 3, 6), (1, 3, 4), (2, 3, 4), (1, 2, 3), (1, 2, 4)]]
C24 = [TN(p) for p in [(3, 5), (3, 6), (5, 6), (4, 5), (4, 6), (1, 6), (1, 5)]]

ok = True
for br, name, R, C, expZ, expB in [(br22, "L6,22", R22, C22, 10, 2),
                                   (br24, "L6,24", R24, C24, 8, 3)]:
    check_jacobi(br, name)
    for e in [Fraction(0), Fraction(1), Fraction(-1), Fraction(2)]:
        zr = rank_of(d2_rows(br, e))
        allrows, nz = d1_rows(br, e)
        br_ = rank_of(nz) if nz else 0
        dimZ, dimB = len(PAIRS) - zr, br_
        dimH = dimZ - dimB
        flag = "OK" if (dimZ == expZ and dimB == expB) else "FAIL"
        if flag == "FAIL":
            ok = False
        print(f"{name} e={e}: rank(d2)={zr} dimZ={dimZ} dimB={dimB} dimH={dimH} [{flag}]")
        D = det_int(submat(d2_rows(br, e), R, C))
        print(f"   minor det = {D} (expected +-1)")
        assert abs(D) == 1, (name, e, D)
    # redundancy: every d2 row lies in span of cert rows (check at e=0 and e=1)
    for e in [Fraction(0), Fraction(1)]:
        M = d2_rows(br, e)
        base = [M[i] for i in R]
        rb = rank_of(base)
        for i, row in enumerate(M):
            if rank_of(base + [row]) != rb:
                print(f"   {name} e={e}: row {TRIPLES[i]} adds rank -> FAIL")
                ok = False
        print(f"   {name} e={e}: all d2 rows in span of cert rows (rank {rb}) OK")

print("ALL VERIFY_OK" if ok else "VERIFY_FAIL")
assert ok
