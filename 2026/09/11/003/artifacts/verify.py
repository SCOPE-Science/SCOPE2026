"""verify.py — INDEPENDENT exact replay of the P1 4-fold certificate.
Reads output/artifacts/complexes.json (adj1) + certificate.json; reimplements
Koszul calculus from scratch (no imports from 06_exact); checks over Q:
 [V1] flag/sphere/C4-free nerve data sanity (counts from adj1)
 [V2] d^2=0 on every used multidegree
 [V3] the four 2-set classes are nonzero (dim H^3(J)=1, rep outside im d)
 [V4] six ORDERED cup equations d(x)+P=0 with P recomputed by graded product
 [V5] triple reps recomputed (t_abc=x_ab c-a x_bc etc.) and killings d(y)+t=0
 [V6] w recomputed from (x,y) data, equals recorded W, d(w)=0
 [V7] [w] Gibbs-free: w not in im(d) in Jw
 [V8] full indeterminacy (cup-choice + killing-choice + aH+Hd + z_ab*z_cd),
      exact rref: w NOT in span => 4-fold value does not contain 0
Prints VERIFY_OK iff all pass.
"""
import json, itertools
from fractions import Fraction

C = json.load(open("output/artifacts/complexes.json"))
CERT = json.load(open("output/artifacts/certificate.json"))
adj = C["adj1"]; n = len(adj)

def in_K(S):
    S = list(S)
    return all(adj[a][b] for a, b in itertools.combinations(S, 2))

# ---- V1 ----
ne = sum(adj[i][j] for i in range(n) for j in range(i + 1, n))
ntr = sum(1 for t in itertools.combinations(range(n), 3) if in_K(t))
nk4 = sum(1 for t in itertools.combinations(range(n), 4) if in_K(t))
chi = n - ne + ntr - nk4
c4 = sum(1 for q in itertools.combinations(range(n), 4)
         if sum(1 for a, b in itertools.combinations(q, 2) if adj[a][b]) == 4
         and sorted(sum(1 for w in q if w != v and adj[v][w]) for v in q) == [2] * 4)
print(f"[V1] n={n} edges={ne} tris={ntr} K4={nk4} chi={chi} inducedC4={c4}")
assert (n, ne, chi, c4) == (13, 36, 2, 0), "nerve data mismatch"

def basis(J):
    J = tuple(sorted(J)); out = []
    for r in range(len(J) + 1):
        for L in itertools.combinations(J, r):
            if in_K(set(J) - set(L)): out.append(tuple(sorted(L)))
    return out

def dmat(J):
    B = basis(J); idx = {L: k for k, L in enumerate(B)}
    m = len(B)
    M = [[Fraction(0)] * m for _ in range(m)]
    for j, L in enumerate(B):
        for t, l in enumerate(L):
            L2 = tuple(sorted(set(L) - {l}))
            if L2 in idx: M[idx[L2]][j] += Fraction((-1) ** t)
    return B, idx, M

def rref_solve(M, b):
    R = len(M); Cc = len(M[0]) if R else 0
    A = [list(map(Fraction, row)) + [Fraction(b[i])] for i, row in enumerate(M)]
    piv = []; r = 0
    for c in range(Cc):
        p = next((i for i in range(r, R) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(R):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * q for a, q in zip(A[i], A[r])]
        piv.append(c); r += 1
    for i in range(r, R):
        if A[i][Cc] != 0: return False, None, None
    xp = [Fraction(0)] * Cc
    for k, c in enumerate(piv): xp[c] = A[k][Cc]
    free = [c for c in range(Cc) if c not in piv]
    N = []
    for f in free:
        v = [Fraction(0)] * Cc; v[f] = Fraction(1)
        for k, c in enumerate(piv): v[c] = -A[k][f]
        N.append(v)
    return True, xp, N

def F(c):
    return c if isinstance(c, Fraction) else Fraction(c)

def vec(B, idx, X):
    v = [Fraction(0)] * len(B)
    for L, c in X.items(): v[idx[tuple(sorted(L))]] += F(c)
    return v

def mul(X, JX, Y, JY):
    J = tuple(sorted(set(JX) | set(JY))); out = {}
    for LX, cx in X.items():
        for LY, cy in Y.items():
            LX = set(LX); LY = set(LY)
            if LX & LY: continue
            VX = set(JX) - LX; VY = set(JY) - LY
            if (set(JX) & LY) - LX: continue
            if (set(JY) & LX) - LY: continue
            L = tuple(sorted(LX | LY))
            s = Fraction((-1) ** (len(LY) * len(VX)))
            m = sorted(LX) + sorted(LY)
            inv = sum(1 for i in range(len(m)) for j in range(i + 1, len(m)) if m[i] > m[j])
            s *= Fraction((-1) ** inv)
            if not in_K(set(J) - set(L)): continue
            out[L] = out.get(L, Fraction(0)) + s * F(cx) * F(cy)
    return {L: c for L, c in out.items() if c != 0}, J

def add(*Xs):
    out = {}
    for X in Xs:
        for L, c in X.items(): out[L] = out.get(L, Fraction(0)) + F(c)
    return {L: c for L, c in out.items() if c != 0}

def neg(X): return {L: -c for L, c in X.items()}
def coc(e):
    return {(e[0],): Fraction(1)}, tuple(sorted(e))
def rd(X):  # read recorded {[[L],str]} -> {tuple: Fraction}
    return {tuple(L): Fraction(v) for L, v in X}

perm = [tuple(e) for e in CERT["quad"]]
a, b, c, d = perm
A, JA = coc(a); Bc, JB = coc(b); Cc, JC = coc(c); Dc, JD = coc(d)
S = set(v for e in perm for v in e)
assert not (S & {0, 1}), "support must avoid doubling locus"
assert len(S) == 8 and len(set(tuple(sorted(e)) for e in perm)) == 4
print(f"[V0] quad={perm} support={sorted(S)} disjoint-from-D OK")

Jall = []
# ---- V2/V4: cups ----
X = {}
for key, rec in CERT["cups"].items():
    J = tuple(rec["J"]); Jall.append(J)
    B, idx, M = dmat(J)
    # d^2 = 0
    m = len(B)
    assert all(sum(M[i][k] * M[k][j] for k in range(m)) == 0
               for i in range(m) for j in range(m)), f"d^2!=0 on {J}"
    e1, e2 = key.split("x")
    e1 = tuple(int(v) for v in e1.strip("() ").split(","))
    e2 = tuple(int(v) for v in e2.strip("() ").split(","))
    P, Jp = mul(*coc(e1), *coc(e2))
    assert tuple(sorted(Jp)) == J, "cup multidegree mismatch"
    assert P == rd(rec["P"]), f"cup product mismatch {key}: {P} vs {rd(rec['P'])}"
    x = rd(rec["x"])
    res = [sum(M[i][j] * x.get(B[j], Fraction(0)) for j in range(m)) - vec(B, idx, neg(P))[i]
           for i in range(m)]
    assert all(v == 0 for v in res), f"cup equation fails {key}"
    X[(e1, e2)] = (x, J)
print("[V2+V4] d^2=0 everywhere; 6 ordered cup products recomputed; d(x)+P=0 exact")

# ---- V3: classes nonzero ----
for e in perm:
    J = tuple(sorted(e))
    B, idx, M = dmat(J)
    rep = vec(B, idx, {(e[0],): Fraction(1)})
    ok, _, _ = rref_solve(M, rep)
    assert not ok, f"class {e} is exact"
print("[V3] all four H^3 classes nonzero (rep outside im d)")

# ---- V5: triples ----
xab, Jab = X[(a, b)]; xbc, Jbc = X[(b, c)]; xcd, Jcd = X[(c, d)]
P1, Jp1 = mul(xab, Jab, Cc, JC); P2, Jp2 = mul(A, JA, xbc, Jbc)
Jt1 = tuple(sorted(set(Jp1) | set(Jp2))); T1 = add(P1, neg(P2))
Q1, Jq1 = mul(xbc, Jbc, Dc, JD); Q2, Jq2 = mul(Bc, JB, xcd, Jcd)
Jt2 = tuple(sorted(set(Jq1) | set(Jq2))); T2 = add(Q1, neg(Q2))
r1 = CERT["triple_abc"]; r2 = CERT["triple_bcd"]
assert tuple(r1["J"]) == Jt1 and rd(r1["T"]) == T1, "T_abc mismatch"
assert tuple(r2["J"]) == Jt2 and rd(r2["T"]) == T2, "T_bcd mismatch"
y1 = rd(r1["y"]); y2 = rd(r2["y"])
for (y, Jt, T, nm) in [(y1, Jt1, T1, "abc"), (y2, Jt2, T2, "bcd")]:
    B, idx, M = dmat(Jt)
    m = len(B)
    assert all(sum(M[i][k] * M[k][j] for k in range(m)) == 0
               for i in range(m) for j in range(m)), f"d^2!=0 on {Jt}"
    res = [sum(M[i][j] * y.get(B[j], Fraction(0)) for j in range(m)) - vec(B, idx, neg(T))[i]
           for i in range(m)]
    assert all(v == 0 for v in res), f"triple killing fails {nm}"
print(f"[V5] triple reps recomputed; both inner triples strictly vanish (T_abc={len(T1)} terms, T_bcd={len(T2)} terms)")

# ---- V6: w ----
W1, Jw1 = mul(y1, Jt1, Dc, JD); X1, Jx1 = mul(xab, Jab, xcd, Jcd); W2, Jw2 = mul(A, JA, y2, Jt2)
Jw = tuple(sorted(set(Jw1) | set(Jx1) | set(Jw2)))
def emb(Xx):
    o = {}
    for L, cc in Xx.items():
        if in_K(set(Jw) - set(L)): o[tuple(sorted(L))] = o.get(tuple(sorted(L)), Fraction(0)) + F(cc)
    return o
W = add(emb(W1), neg(emb(X1)), emb(W2))
assert W == rd(CERT["w"]["terms"]), "w recomputation mismatch"
assert tuple(CERT["w"]["J"]) == Jw
Bw, iw, Mw = dmat(Jw); bw = vec(Bw, iw, W)
m = len(Bw)
assert all(sum(Mw[i][k] * Mw[k][j] for k in range(m)) == 0
           for i in range(m) for j in range(m)), "d^2!=0 on Jw"
assert all(sum(Mw[i][j] * bw[j] for j in range(m)) == 0 for i in range(m)), "d(w)!=0"
print(f"[V6] w recomputed from (x,y) data, matches record, d-closed; Jw={Jw} terms={len(W)} deg=10")

# ---- V7: non-exact ----
ok, _, _ = rref_solve(Mw, bw)
assert not ok, "w is exact"
print("[V7] [w] != 0 in H(Jw): non-exact")

# ---- V8: full indeterminacy ----
cols = []
for (Xx, JXx, nm) in [(xab, Jab, "ab"), (xbc, Jbc, "bc"), (xcd, Jcd, "cd")]:
    B, idx, M = dmat(JXx)
    _, _, N0 = rref_solve(M, [Fraction(0)] * len(B))
    for nv in N0:
        z = {L: nv[idx[L]] for L in B if nv[idx[L]] != 0}
        if nm == "ab":
            R1, _ = mul(add(Xx, z), JXx, Cc, JC); R2, _ = mul(A, JA, xbc, Jbc)
            Jt = tuple(sorted(set(JXx) | set(JC)))
            T = add(R1, neg(R2))
            B3, i3, M3 = dmat(Jt)
            okk, yv, _ = rref_solve(M3, vec(B3, i3, neg(T)))
            if not okk: continue
            yv = {L: yv[i3[L]] for L in B3 if yv[i3[L]] != 0}
            S1, _ = mul(yv, Jt, Dc, JD); D1, _ = mul(add(Xx, z), JXx, xcd, Jcd); S2, _ = mul(A, JA, y2, Jt2)
        elif nm == "bc":
            R1, _ = mul(xab, Jab, Cc, JC); R2, _ = mul(A, JA, add(Xx, z), JXx)
            Jt = tuple(sorted(set(Jab) | set(JC)))
            T = add(R1, neg(R2))
            B3, i3, M3 = dmat(Jt)
            okk, yv, _ = rref_solve(M3, vec(B3, i3, neg(T)))
            if not okk: continue
            yv = {L: yv[i3[L]] for L in B3 if yv[i3[L]] != 0}
            S1, _ = mul(yv, Jt, Dc, JD); D1, _ = mul(xab, Jab, xcd, Jcd); S2, _ = mul(A, JA, y2, Jt2)
        else:
            R1, _ = mul(xbc, Jbc, Dc, JD); R2, _ = mul(Bc, JB, add(Xx, z), JXx)
            Jt = tuple(sorted(set(Jbc) | set(JD)))
            T = add(R1, neg(R2))
            B3, i3, M3 = dmat(Jt)
            okk, yv, _ = rref_solve(M3, vec(B3, i3, neg(T)))
            if not okk: continue
            yv = {L: yv[i3[L]] for L in B3 if yv[i3[L]] != 0}
            S1, _ = mul(y1, Jt1, Dc, JD); D1, _ = mul(xab, Jab, add(Xx, z), JXx); S2, _ = mul(A, JA, yv, Jt)
        Wn = add(emb(S1), neg(emb(D1)), emb(S2))
        cols.append([x - y for x, y in zip(vec(Bw, iw, Wn), bw)])
for yJ, Jt, other, side in [(y1, Jt1, (Dc, JD), "R"), (y2, Jt2, (A, JA), "L")]:
    B, idx, M = dmat(Jt)
    _, _, N0 = rref_solve(M, [Fraction(0)] * len(B))
    for nv in N0:
        z = {L: nv[idx[L]] for L in B if nv[idx[L]] != 0}
        E, JE = other
        P, Jp = (mul(add(yJ, z), Jt, E, JE) if side == "R" else mul(E, JE, add(yJ, z), Jt))
        cols.append(vec(Bw, iw, {L: c for L, c in P.items() if in_K(set(Jw) - set(L))}))
for E, JE in [(a, JA), (d, JD)]:
    Jc = tuple(sorted(set(Jw) - set(JE)))
    B, idx, M = dmat(Jc)
    _, _, N0 = rref_solve(M, [Fraction(0)] * len(B))
    Ee, _ = coc(E)
    for nv in N0:
        h = {L: nv[idx[L]] for L in B if nv[idx[L]] != 0}
        P, Jp = mul(Ee, JE, h, Jc) if E == a else mul(h, Jc, Ee, JE)
        cols.append(vec(Bw, iw, {L: c for L, c in P.items() if in_K(set(Jw) - set(L))}))
Bab, iab, Mab = dmat(Jab); _, _, Nab = rref_solve(Mab, [Fraction(0)] * len(Bab))
Bcd, icd, Mcd = dmat(Jcd); _, _, Ncd = rref_solve(Mcd, [Fraction(0)] * len(Bcd))
n2 = 0
for va in Nab:
    za = {L: va[iab[L]] for L in Bab if va[iab[L]] != 0}
    for vc in Ncd:
        zc = {L: vc[icd[L]] for L in Bcd if vc[icd[L]] != 0}
        P, Jp = mul(za, Jab, zc, Jcd)
        assert tuple(sorted(Jp)) == Jw
        cols.append(vec(Bw, iw, {L: c for L, c in P.items() if in_K(set(Jw) - set(L))}))
        n2 += 1
k = len(cols)
G = [[cols[j][i] for j in range(k)] for i in range(m)]
okk, _, _ = rref_solve(G, bw)
assert not okk, "4-fold value contains 0"
print(f"[V8] indeterminacy: {k} exact columns ({n2} second-order); w NOT in span => <a,b,c,d> != 0 mod indet")
print("VERIFY_OK")
