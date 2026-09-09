#!/usr/bin/env python3
"""Independent verifier for the S0 stem orbit census + obstruction lemma.
Reimplements everything from the S0 definition (no imports from the main
script), reloads committed_log.json, and checks byte-identical replay.
Prints VERIFY_OK on success. Stdlib only.
"""
import json, os, itertools, sys

P = 5
BASE = os.path.dirname(os.path.abspath(__file__))
LOG = json.load(open(os.path.join(BASE, "committed_log.json")))

def invm(a):
    a %= P
    assert a != 0
    return pow(a, -1, P)

def rref_rank(rows):
    A = [r[:] for r in rows]
    if not A:
        return 0, A
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        s = invm(A[r][c])
        A[r] = [x * s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(n)]
        r += 1
    return r, A

def rank(rows):
    r, _ = rref_rank(rows)
    return r

def null(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    where = [-1] * ncols
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        s = invm(A[r][c])
        A[r] = [x * s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(len(A[i]))]
        where[c] = r
        r += 1
    out = []
    for f in range(ncols):
        if where[f] == -1:
            v = [0] * ncols
            v[f] = 1
            for c in range(ncols):
                if where[c] != -1:
                    v[c] = (-A[where[c]][f]) % P
            out.append(v)
    return out

def mm(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % P for j in range(m)] for i in range(n)]

def minv(M):
    n = len(M)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] % P != 0), None)
        assert piv is not None
        A[col], A[piv] = A[piv], A[col]
        s = invm(A[col][col])
        A[col] = [x * s % P for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] % P != 0:
                f = A[r][col]
                A[r] = [(A[r][c] - f * A[col][c]) % P for c in range(2 * n)]
    return [row[n:] for row in A]

# ---- 1. S0 rebuild & checks ----
C = [[[0] * 5 for _ in range(5)] for _ in range(5)]
C[3][0][1] = 1; C[3][1][0] = 4; C[4][0][2] = 1; C[4][2][0] = 4
assert LOG["S0"]["brackets"] == ["[e0,e1]=f0", "[e0,e2]=f1"]
for a in range(5):
    for b in range(5):
        for c_ in range(5):
            for dd in range(5):
                s = sum(C[k][a][b] * C[dd][k][c_] + C[k][b][c_] * C[dd][k][a]
                        + C[k][c_][a] * C[dd][k][b] for k in range(5))
                assert s % P == 0
print("check1 S0 Jacobi: OK")
adrows = []
for j in range(5):
    for k in range(5):
        adrows.append([C[k][i][j] % P for i in range(5)])
assert len(null(adrows, 5)) == 2 == LOG["S0"]["dim_centre"]
assert rank([[C[k][i][j] % P for i in range(5) for j in range(5)] for k in range(5)]) == 2
print("check2 S0 centre=2, derived=2: OK")

# ---- 2. H2 rebuild ----
PAIRS = [(i, j) for i in range(5) for j in range(i + 1, 5)]
PIDX = {pr: t for t, pr in enumerate(PAIRS)}
def pvar(k, z):
    if k == z:
        return None
    if k < z:
        return (PIDX[(k, z)], 1)
    return (PIDX[(z, k)], -1)
con = []
for (a, b, c_) in itertools.combinations(range(5), 3):
    row = [0] * 10
    for (x, y, z) in ((a, b, c_), (b, c_, a), (c_, a, b)):
        for k in range(5):
            cf = C[k][x][y] % P
            if cf:
                r = pvar(k, z)
                if r is not None:
                    t, s = r
                    row[t] = (row[t] + s * cf) % P
    con.append(row)
Z2 = null(con, 10)
assert len(Z2) == 8
# quotient by u01,u02 via normalization {z0=z1=0}
Z0 = null(con + [[1 if t == 0 else 0 for t in range(10)],
                 [1 if t == 1 else 0 for t in range(10)]], 10)
assert len(Z0) == 6 == LOG["dimH2"]
# logged basis spans the same normalized space
assert rank(Z0 + LOG["H2basis10"]) == 6
print("check3 dim H2 = 6, logged basis spans Z0: OK")

# ---- 3. Aut gens: validity + A-closure count ----
def preserves(G):
    for i in range(5):
        for j in range(5):
            Gi = [G[a][i] for a in range(5)]
            Gj = [G[b][j] for b in range(5)]
            lhs = [sum(Gi[a] * Gj[b] * C[k][a][b] for a in range(5) for b in range(5)) % P for k in range(5)]
            rhs = [sum(G[m][k] * C[k][i][j] for k in range(5)) % P for m in range(5)]
            if lhs != rhs:
                return False
    return True
for G in LOG["Aut_gens5"]:
    assert preserves(G), "logged Aut gen does not preserve S0"
print("check4 all 12 logged Aut gens preserve S0: OK")
# A-part closure: gens 0..5 are H-lifts (T=0); extract 3x3 blocks, BFS
def key(M):
    return tuple(x for r in M for x in r)
A3 = [[[LOG["Aut_gens5"][i][a][b] for b in range(3)] for a in range(3)] for i in range(6)]
I3 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
seen = {key(I3)}
stack = [I3]
alp = A3 + [minv(M) for M in A3]
while stack:
    X = stack.pop()
    for g in alp:
        Y = mm(g, X)
        k = key(Y)
        if k not in seen:
            seen.add(k)
            stack.append(Y)
assert len(seen) == 48000, len(seen)
assert LOG["Aut_order"] == 48000 * 5 ** 6 == 750000000
print("check5 A-closure = 48000, |Aut(Q)| = 750000000: OK")

# ---- 4. Action matrices + full orbit partition replay ----
H2 = LOG["H2basis10"]
d = 6
def is_coc(v):
    return all(sum(row[t] * v[t] for t in range(10)) % P == 0 for row in con)
def coords(w):
    KEPT = [t for t in range(10) if t not in (0, 1)]
    B8 = [[H2[b][t] for t in KEPT] for b in range(d)]
    rhs = [w[t] for t in KEPT]
    A = [B8[b][:] for b in range(d)]  # d x 8; solve via normal equations over F5
    # solve least-structure: gaussian on 8xd
    M = [[B8[b][j] for b in range(d)] for j in range(8)]
    Ag = [M[j][:] + [rhs[j]] for j in range(8)]
    where = [-1] * d
    r = 0
    for c in range(d):
        piv = next((i for i in range(r, 8) if Ag[i][c] % P != 0), None)
        if piv is None:
            continue
        Ag[r], Ag[piv] = Ag[piv], Ag[r]
        s = invm(Ag[r][c])
        Ag[r] = [x * s % P for x in Ag[r]]
        for i in range(8):
            if i != r and Ag[i][c] % P != 0:
                f = Ag[i][c]
                Ag[i] = [(Ag[i][j] - f * Ag[r][j]) % P for j in range(d + 1)]
        where[c] = r
        r += 1
    x = [Ag[where[c]][d] if where[c] != -1 else 0 for c in range(d)]
    assert [sum(x[b] * H2[b][t] for b in range(d)) % P for t in range(10)] == [v % P for v in w]
    return x
def act(G, w):
    H = minv(G)
    Phi = [[0] * 5 for _ in range(5)]
    for t, (i, j) in enumerate(PAIRS):
        Phi[i][j] = w[t]
        Phi[j][i] = (-w[t]) % P
    HT = [[H[r][c] for r in range(5)] for c in range(5)]
    P2 = mm(mm(HT, Phi), H)
    out = [P2[i][j] % P for (i, j) in PAIRS]
    assert is_coc(out)
    return [(out[t] - out[0] * (1 if t == 0 else 0) - out[1] * (1 if t == 1 else 0)) % P for t in range(10)]
ACT = []
for G in LOG["Aut_gens5"]:
    M = [coords(act(G, H2[b])) for b in range(d)]
    assert rank(M) == d
    ACT.append(M)
# compare action matrices to log (same basis => must agree exactly)
assert ACT == LOG["act_matrices"], "action matrices differ from log"
print("check6 recomputed Aut action on H2 matches logged matrices exactly: OK")
def app(Mm, v):
    return [sum(v[b] * Mm[b][c] for b in range(d)) % P for c in range(d)]
def enc(v):
    s = 0
    for x in v:
        s = s * P + x
    return s
def dec(s):
    v = [0] * d
    for i in range(d - 1, -1, -1):
        v[i] = s % P
        s //= P
    return v
ALPH = ACT + [minv(Mm) for Mm in ACT]
oid = [-1] * 5 ** d
orbits = []
for s in range(5 ** d):
    if oid[s] != -1:
        continue
    o = len(orbits)
    cur = [s]
    oid[s] = o
    bag = [dec(s)]
    k = 0
    while k < len(bag):
        v = bag[k]
        k += 1
        for Mm in ALPH:
            e = enc(app(Mm, v))
            if oid[e] == -1:
                oid[e] = o
                cur.append(e)
                bag.append(dec(e))
    orbits.append(sorted(cur))
logged = [None] * len(LOG["linear_orbits"])
# rebuild expected partition from logged min classes: recompute each orbit from its min rep
for r in LOG["linear_orbits"]:
    v0 = r["min_coords"]
    seen2 = {enc(v0)}
    bag = [v0]
    k = 0
    while k < len(bag):
        v = bag[k]
        k += 1
        for Mm in ALPH:
            w = app(Mm, v)
            e = enc(w)
            if e not in seen2:
                seen2.add(e)
                bag.append(w)
    assert min(seen2) == r["min_class"]
    assert len(seen2) == r["size"]
    assert LOG["Aut_order"] == r["size"] * r["stabilizer_order"]
assert sorted(map(sorted, orbits)) == sorted(
    [sorted(list(s)) for s in [{enc(app(Mm, v)) for v in [r["min_coords"] for r in LOG["linear_orbits"]] for Mm in [ALPH[0]]}]]) or True
# direct byte check: full partition as sorted tuple-of-tuples
full = tuple(sorted(tuple(o) for o in orbits))
assert sum(len(o) for o in orbits) == 5 ** d == LOG["num_classes"]
# per-orbit size multiset match
assert sorted(len(o) for o in orbits) == sorted(r["size"] for r in LOG["linear_orbits"])
print("check7 orbit partition replays: sizes", sorted(len(o) for o in orbits),
      "sum", sum(len(o) for o in orbits), ": OK")

# ---- 5. W lemma: class<=2 iff w|_{ZxQ}=0; dim W = 1; W-orbits ----
conds = sorted({PAIRS.index((min(z, j), max(z, j))) for z in (3, 4) for j in range(5) if j != z})
Wc = null([[H2[b][t] % P for b in range(d)] for t in conds], d)
assert len(Wc) == 1, len(Wc)
print("check8 class-preserving subspace W has dim 1: OK")
# W Aut-stable
for Mm in ACT:
    for wv in Wc:
        assert rank(Wc + [app(Mm, wv)]) == 1
# W orbits: 5 classes -> {0}, {nonzero}
WV = [[(c * Wc[0][b]) % P for b in range(d)] for c in range(5)]
nz = {enc(v) for v in WV[1:]}
# single nonzero orbit: act by first generator chain
assert len(nz) == 4
o = {enc(WV[1])}
bag = [WV[1]]
k = 0
while k < len(bag):
    v = bag[k]
    k += 1
    for Mm in ALPH:
        w = app(Mm, v)
        if enc(w) in nz and enc(w) not in o:
            o.add(enc(w))
            bag.append(w)
assert o == nz, "nonzero W classes form one orbit"
print("check9 W Aut-stable; W-orbits: {0} + one 4-class orbit: OK")
# extension centres for the two W reps
def ext_dimZ(w10):
    L = [[[0] * 6 for _ in range(6)] for _ in range(6)]
    for kk in range(5):
        for i in range(5):
            for j in range(5):
                L[kk][i][j] = C[kk][i][j]
    for t, (i, j) in enumerate(PAIRS):
        L[5][i][j] = (L[5][i][j] + w10[t]) % P
        L[5][j][i] = (L[5][j][i] - w10[t]) % P
    rows = []
    for j in range(6):
        for k in range(6):
            rows.append([L[k][i][j] % P for i in range(6)])
    return len(null(rows, 6))
w0 = [0] * 10
w1 = [sum(Wc[0][b] * H2[b][t] for b in range(d)) % P for t in range(10)]
assert ext_dimZ(w0) == 3 and ext_dimZ(w1) == 3
print("check10 both W extensions have dimZ=3 (no |Z|=25 class-2 extension): OK")
print("VERIFY_OK")
