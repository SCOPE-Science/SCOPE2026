#!/usr/bin/env python3
"""S0 stem Lie algebra over F5: Lie H^2, Aut(Q) generators, orbit table.
Stdlib only. Writes committed_log.json. Target: Phi_7 cell, p=5.
Convention: matrices act on COLUMN vectors. Basis Q = [e0,e1,e2,f0,f1].
Brackets: [e0,e1]=f0, [e0,e2]=f1 (indices [0,1]->3, [0,2]->4).
"""
import json, itertools, os

P = 5
BASE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(BASE, "committed_log.json")

def add(a, b): return (a + b) % P
def mul(a, b): return (a * b) % P
def neg(a): return (-a) % P
def inv(a):
    a %= P
    assert a != 0
    return pow(a, -1, P)

def mat_mul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % P for j in range(m)] for i in range(n)]

def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) % P for i in range(len(A))]

def mat_inv(M):
    n = len(M)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] % P != 0), None)
        assert piv is not None, "singular"
        A[col], A[piv] = A[piv], A[col]
        s = inv(A[col][col])
        A[col] = [x * s % P for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] % P != 0:
                f = A[r][col]
                A[r] = [(A[r][c] - f * A[col][c]) % P for c in range(2 * n)]
    return [row[n:] for row in A]

def nullspace_rows(M, ncols):
    """Nullspace of matrix given as list of rows. Returns basis list."""
    A = [r[:] for r in M]
    m = len(A)
    where = [-1] * ncols
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        s = inv(A[r][c])
        A[r] = [x * s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(len(A[i]))]
        where[c] = r
        r += 1
    basis = []
    for f in range(ncols):
        if where[f] == -1:
            v = [0] * ncols
            v[f] = 1
            for c in range(ncols):
                if where[c] != -1:
                    v[c] = (-A[where[c]][f]) % P
            basis.append(v)
    return basis

def rank_rows(M):
    A = [r[:] for r in M]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        s = inv(A[r][c])
        A[r] = [x * s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(n)]
        r += 1
    return r

# ---------------- S0 ----------------
# c[k][i][j]
C = [[[0]*5 for _ in range(5)] for _ in range(5)]
def set_br(i, j, k, v=1):
    C[k][i][j] = v % P
    C[k][j][i] = (-v) % P
set_br(0, 1, 3, 1)
set_br(0, 2, 4, 1)

# Jacobi check
for a in range(5):
    for b in range(5):
        for c_ in range(5):
            for d in range(5):
                s = 0
                for k in range(5):
                    s += C[k][a][b]*C[d][k][c_] + C[k][b][c_]*C[d][k][a] + C[k][c_][a]*C[d][k][b]
                assert s % P == 0, ("jacobi fail", a, b, c_, d)
print("S0 Jacobi OK")

# centre: rows = ad_{e_j} matrices (k,i) = C[k][i][j]
rows = []
for j in range(5):
    for k in range(5):
        rows.append([C[k][i][j] % P for i in range(5)])
Zb = nullspace_rows(rows, 5)
print("dim centre =", len(Zb), Zb)
assert len(Zb) == 2
# derived rank
Drows = [[C[k][i][j] % P for i in range(5) for j in range(5)] for k in range(5)]
print("derived rank =", rank_rows(Drows))
assert rank_rows(Drows) == 2

# ---------------- Lie H^2(Q, F5) ----------------
PAIRS = [(i, j) for i in range(5) for j in range(i+1, 5)]
PAIRIDX = {pr: t for t, pr in enumerate(PAIRS)}
def phi_var(k, z):
    if k == z: return None
    if k < z: return (PAIRIDX[(k, z)], 1)
    return (PAIRIDX[(z, k)], -1)

con = []
for (a, b, c_) in itertools.combinations(range(5), 3):
    row = [0]*10
    for (x, y, z) in ((a, b, c_), (b, c_, a), (c_, a, b)):
        for k in range(5):
            coef = C[k][x][y] % P
            if coef:
                r = phi_var(k, z)
                if r is not None:
                    t, s = r
                    row[t] = (row[t] + s*coef) % P
    con.append(row)
rz = rank_rows(con)
print("Jacobi-constraint rank =", rz, "-> dim Z2 =", 10 - rz)
Z2 = nullspace_rows(con, 10)
print("dim Z2 =", len(Z2))
# B2 supported on pair idx 0 (01) and 1 (02); both are cocycles (checked below)
u01 = [1 if t == 0 else 0 for t in range(10)]
u02 = [1 if t == 1 else 0 for t in range(10)]
def is_cocycle(v):
    for row in con:
        if sum(row[t]*v[t] for t in range(10)) % P != 0:
            return False
    return True
assert is_cocycle(u01) and is_cocycle(u02)
# H2 = Z2 / span(u01,u02): normalized subspace Z0 = {z: z0=z1=0}
con0 = con + [[1 if t == 0 else 0 for t in range(10)],
              [1 if t == 1 else 0 for t in range(10)]]
Z0 = nullspace_rows(con0, 10)
d = len(Z0)
print("dim H2 =", d)
DIMH2 = d
H2basis = Z0  # list of 10-vecs, normalized (comps 0,1 are 0)
# coordinate map: 8-comps (drop idx 0,1)
KEPT = [t for t in range(10) if t not in (0, 1)]
assert len(KEPT) == 8
B8 = [[v[t] for t in KEPT] for v in H2basis]  # d x 8
assert rank_rows(B8) == d
# solve coords: for normalized cocycle w (10-vec), find coords x with sum x_b * H2basis[b] = w.
# Build solve matrix: transpose approach via small Gaussian on augmented system.
def h2_coords(w):
    # unknowns x (d), equations: full 10 rows of H2basis^T x = w; use kept 8 rows then verify.
    # Solve 8 x d system.
    M = [[B8[b][j] for b in range(d)] for j in range(8)]  # 8 x d
    rhs = [w[t] for t in KEPT]
    # gaussian solve (possibly underdetermined if d>8? d<=8 expected; handle generally: least-structure via rref)
    A = [M[j][:] + [rhs[j]] for j in range(8)]
    where = [-1]*d
    r = 0
    for c in range(d):
        piv = next((i for i in range(r, 8) if A[i][c] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        s = inv(A[r][c])
        A[r] = [x*s % P for x in A[r]]
        for i in range(8):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j]-f*A[r][j]) % P for j in range(d+1)]
        where[c] = r
        r += 1
    x = [0]*d
    for c in range(d):
        if where[c] != -1:
            x[c] = A[where[c]][d]
    # verify
    chk = [sum(x[b]*H2basis[b][t] for b in range(d)) % P for t in range(10)]
    assert chk == [v % P for v in w], ("coord fail", chk, w)
    return x

def normalize(w):
    return [(w[t] - w[0]*u01[t] - w[1]*u02[t]) % P for t in range(10)]

# ---------------- Aut(Q) ----------------
# B: w01->(1,0), w02->(0,1), w12->(0,0)
def wedge2_cols(A):
    """A 3x3 (column convention). Return images of w01,w02,w12 as coeff triples on (w01,w02,w12)."""
    def col(j): return [A[i][j] for i in range(3)]
    out = []
    for (i, j) in ((0,1),(0,2),(1,2)):
        ci, cj = col(i), col(j)
        m01 = (ci[0]*cj[1]-ci[1]*cj[0]) % P
        m02 = (ci[0]*cj[2]-ci[2]*cj[0]) % P
        m12 = (ci[1]*cj[2]-ci[2]*cj[1]) % P
        out.append((m01, m02, m12))
    return out
def D_of_A(A):
    w = wedge2_cols(A)
    # B(w) for each: (m01, m02)
    col01 = (w[0][0] % P, w[0][1] % P)
    col02 = (w[1][0] % P, w[1][1] % P)
    col12 = (w[2][0] % P, w[2][1] % P)
    if col12 != (0, 0):
        return None
    det = (col01[0]*col02[1]-col01[1]*col02[0]) % P
    if det == 0:
        return None
    return [[col01[0], col02[0]], [col01[1], col02[1]]]

def lift(A3, T):
    D = D_of_A(A3)
    assert D is not None
    G = [[0]*5 for _ in range(5)]
    for i in range(3):
        for j in range(3):
            G[i][j] = A3[i][j]
    for a in range(2):
        for j in range(3):
            G[3+a][j] = T[a][j]
    for a in range(2):
        for b in range(2):
            G[3+a][3+b] = D[a][b]
    return G

def preserves(G):
    # check on basis pairs: G[x,y]_new == [Gx,Gy]: compare structure constants pullback
    # ([Gx,Gy])_k = sum_{p,q} G[k?] ... direct: for pairs (i,j): compute [G e_i, G e_j] and G[e_i,e_j].
    for i in range(5):
        for j in range(5):
            lhs = [0]*5  # [G e_i, G e_j]
            Gi = [G[a][i] for a in range(5)]
            Gj = [G[b][j] for b in range(5)]
            for a in range(5):
                for b in range(5):
                    for k in range(5):
                        lhs[k] = (lhs[k] + Gi[a]*Gj[b]*C[k][a][b]) % P
            rhs = [0]*5  # G[e_i,e_j]
            for k in range(5):
                for m in range(5):
                    rhs[m] = (rhs[m] + G[m][k]*C[k][i][j]) % P
            if lhs != rhs:
                return False
    return True

I3 = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
Z23 = [[0]*3 for _ in range(2)]
# H generators (plane P=span{e1,e2} stabilizer)
h1 = [[2,0,0],[0,1,0],[0,0,1]]
g1 = [[1,1],[0,1]]; g2 = [[1,0],[1,1]]; g3 = [[2,0],[0,1]]
def blk(M2):
    return [[1,0,0],[0,M2[0][0],M2[0][1]],[0,M2[1][0],M2[1][1]]]
h2, h3, h3b = blk(g1), blk(g2), blk(g3)
h4 = [[1,0,0],[1,1,0],[0,0,1]]  # e0 -> e0+e1
h5 = [[1,0,0],[0,1,0],[1,0,1]]  # e0 -> e0+e2
Hgens3 = [h1, h2, h3, h3b, h4, h5]
# verify H generation: BFS 3x3 matrices, expect 48000
def mkey(M): return tuple(x for r in M for x in r)
seen = {mkey(I3)}
stack = [I3]
prods = []
Hinv = []
for h in Hgens3:
    Hinv.append(mat_inv(h))
alphabet = Hgens3 + Hinv
while stack:
    X = stack.pop()
    for g in alphabet:
        Y = mat_mul(g, X)
        k = mkey(Y)
        if k not in seen:
            seen.add(k)
            stack.append(Y)
print("|<Hgens>| =", len(seen))
assert len(seen) == 48000, len(seen)
# GL(2,5) check
seen2 = {(1,0,0,1)}
st = [[[1,0],[0,1]]]
inv2 = [mat_inv(g) for g in (g1,g2,g3)]
alp2 = [g1,g2,g3]+inv2
while st:
    X = st.pop()
    for g in alp2:
        Y = mat_mul(g,X)
        k = (Y[0][0],Y[0][1],Y[1][0],Y[1][1])
        if k not in seen2:
            seen2.add(k); st.append(Y)
print("|<g1,g2,g3>| =", len(seen2))
assert len(seen2) == 480

AUTGENS = []
for h in Hgens3:
    G = lift(h, Z23)
    assert preserves(G)
    AUTGENS.append(("H", h, G))
for a in range(2):
    for i in range(3):
        T = [[0]*3 for _ in range(2)]
        T[a][i] = 1
        G = lift(I3, T)
        assert preserves(G)
        AUTGENS.append(("T%d%d" % (a, i), None, G))
print("num Aut gens =", len(AUTGENS))
AUT_ORDER = 48000 * (P**6)
print("|Aut(Q)| =", AUT_ORDER)
assert AUT_ORDER == 750000000

# ---------------- action on H^2 ----------------
def act_on_cocycle(G, w):
    """(g.w)(x,y) = w(g^-1 x, g^-1 y). w as 10-vec -> 10-vec."""
    H = mat_inv(G)
    Phi = [[0]*5 for _ in range(5)]
    for t,(i,j) in enumerate(PAIRS):
        Phi[i][j] = w[t]; Phi[j][i] = (-w[t]) % P
    # Phi' = H^T Phi H
    HT = [[H[r][c] for r in range(5)] for c in range(5)]
    T1 = mat_mul(HT, Phi)
    P2 = mat_mul(T1, H)
    out = []
    for (i,j) in PAIRS:
        out.append(P2[i][j] % P)
    assert is_cocycle(out)
    return normalize(out)

ACT = []  # d x d matrices, row-vector convention: x -> x M
for name, h, G in AUTGENS:
    cols = []
    for b in range(d):
        im = act_on_cocycle(G, H2basis[b])
        cols.append(h2_coords(im))
    # M with rows = images of basis vecs: M[b][c]
    M = [row[:] for row in cols]
    # verify invertible
    assert rank_rows(M) == d
    ACT.append(M)
print("action matrices ok, d =", d)

def apply_act(M, v):
    return [sum(v[b]*M[b][c] for b in range(d)) % P for c in range(d)]

def enc(v):
    s = 0
    for x in v:
        s = s*P + x
    return s
def dec(s):
    v = [0]*d
    for i in range(d-1, -1, -1):
        v[i] = s % P; s //= P
    return v

NCL = P**d
print("num H2 classes =", NCL)
# orbit BFS over all classes
ALPHACT = ACT + [mat_inv(M) for M in ACT]
orbit_id = [-1]*NCL
orbits = []
for s in range(NCL):
    if orbit_id[s] != -1:
        continue
    oid = len(orbits)
    cur = [s]
    orbit_id[s] = oid
    bag = [dec(s)]
    k = 0
    while k < len(bag):
        v = bag[k]; k += 1
        for M in ALPHACT:
            w = apply_act(M, v)
            e = enc(w)
            if orbit_id[e] == -1:
                orbit_id[e] = oid
                cur.append(e)
                bag.append(w)
    orbits.append(cur)
print("num linear orbits =", len(orbits))
tot = sum(len(o) for o in orbits)
assert tot == NCL, (tot, NCL)
for o in orbits:
    assert AUT_ORDER % len(o) == 0, ("orbit size does not divide |Aut|", len(o))

# projective orbits: identify v ~ λv
proj_rep = [-1]*NCL
plabel = {}
for s in range(1, NCL):
    v = dec(s)
    cyc = tuple(sorted(enc([(t*v[i]) % P for i in range(d)]) for t in range(1, P)))
    if cyc not in plabel:
        plabel[cyc] = len(plabel)
    proj_rep[s] = plabel[cyc]
print("num projective orbits (incl zero sep) =", len(plabel))

def min_rep(o):
    return min(o)

# ---------------- extensions ----------------
def extension_invariants(w10):
    """6-dim Lie L = Q + span{c}: brackets + w. Returns dict."""
    # L[k][i][j], k,i,j in 0..5
    L = [[[0]*6 for _ in range(6)] for _ in range(6)]
    for k in range(5):
        for i in range(5):
            for j in range(5):
                L[k][i][j] = C[k][i][j]
    for t,(i,j) in enumerate(PAIRS):
        L[5][i][j] = (L[5][i][j] + w10[t]) % P
        L[5][j][i] = (L[5][j][i] - w10[t]) % P
    # centre
    rows = []
    for j in range(6):
        for k in range(6):
            rows.append([L[k][i][j] % P for i in range(6)])
    Z = nullspace_rows(rows, 6)
    # derived
    Dr = [[L[k][i][j] % P for i in range(6) for j in range(6)] for k in range(6)]
    dd = rank_rows(Dr)
    # class: check [[L,L],L]==0
    cl2 = True
    for a in range(6):
        for b in range(6):
            br = [L[k][a][b] for k in range(6)]  # bracket vector [ea,eb]
            for c_ in range(6):
                for m in range(6):
                    s = sum(br[k]*L[m][k][c_] for k in range(6)) % P
                    if s != 0:
                        cl2 = False
    return {"dimZ": len(Z), "dimD": dd, "class_le_2": cl2}

results = []
for oid, o in enumerate(orbits):
    r = min_rep(o)
    v = dec(r)
    w10 = [sum(v[b]*H2basis[b][t] for b in range(d)) % P for t in range(10)]
    invs = extension_invariants(w10)
    # projective size of this linear orbit
    ps = set()
    for s in o:
        ps.add(proj_rep[s])
    results.append({
        "linear_orbit": oid, "size": len(o),
        "stabilizer_order": AUT_ORDER // len(o),
        "min_class": r, "min_coords": v,
        "proj_orbits_touched": sorted(ps),
        "rep10": w10, "inv": invs,
    })

# relevance: dimZ==2 (order 25), class<=2
for res in results:
    res["relevant"] = (res["inv"]["dimZ"] == 2 and res["inv"]["class_le_2"])
nrel = sum(1 for res in results if res["relevant"])
print("relevant linear orbits =", nrel)

# group projective view: one row per projective orbit
proj_rows = {}
for s in range(1, NCL):
    pl = proj_rep[s]
    if pl not in proj_rows:
        proj_rows[pl] = {"members": []}
    proj_rows[pl]["members"].append(s)
print("num nonzero projective orbits =", len(proj_rows))

log = {
    "p": P,
    "S0": {"basis": "e0,e1,e2,f0,f1", "brackets": ["[e0,e1]=f0", "[e0,e2]=f1"],
            "dim_centre": 2, "dim_derived": 2},
    "dimH2": d,
    "H2basis10": H2basis,
    "Aut_order": AUT_ORDER,
    "Aut_gens5": [G for _, _, G in AUTGENS],
    "Aut_gen_names": [n if isinstance(n, str) else "H" for n, _, _ in AUTGENS],
    "act_matrices": ACT,
    "num_classes": NCL,
    "linear_orbits": [
        {"id": r["linear_orbit"], "size": r["size"],
         "stabilizer_order": r["stabilizer_order"], "min_class": r["min_class"],
         "min_coords": r["min_coords"], "rep10": r["rep10"], "inv": r["inv"],
         "relevant": r["relevant"]} for r in results],
    "num_projective_nonzero": len(proj_rows),
}
with open(LOG, "w") as f:
    json.dump(log, f, indent=1)
print("wrote", LOG)
