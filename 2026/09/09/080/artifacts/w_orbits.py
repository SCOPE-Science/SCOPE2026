#!/usr/bin/env python3
"""Restrict to W = {w : w(Z(Q),Q)=0} for S0; orbit-partition W; extension invariants.
Also same for S1. Stdlib only."""
import json, os
P = 5
BASE = os.path.dirname(os.path.abspath(__file__))

def mat_inv(M):
    n = len(M)
    def inv(a): return pow(a % P, -1, P)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] % P != 0), None)
        assert piv is not None
        A[col], A[piv] = A[piv], A[col]
        s = inv(A[col][col]); A[col] = [x*s % P for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] % P != 0:
                f = A[r][col]
                A[r] = [(A[r][c]-f*A[col][c]) % P for c in range(2*n)]
    return [row[n:] for row in A]
def null_rows(M, ncols):
    A = [r[:] for r in M]; m = len(A); where = [-1]*ncols; r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        s = pow(A[r][c], -1, P); A[r] = [x*s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j]-f*A[r][j]) % P for j in range(len(A[i]))]
        where[c] = r; r += 1
    B = []
    for f in range(ncols):
        if where[f] == -1:
            v = [0]*ncols; v[f] = 1
            for c in range(ncols):
                if where[c] != -1: v[c] = (-A[where[c]][f]) % P
            B.append(v)
    return B
def rank_rows(M):
    A = [r[:] for r in M]
    if not A: return 0
    m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] % P != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        s = pow(A[r][c], -1, P); A[r] = [x*s % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P != 0:
                f = A[i][c]
                A[i] = [(A[i][j]-f*A[r][j]) % P for j in range(n)]
        r += 1
    return r

PAIRS = [(i, j) for i in range(5) for j in range(i+1, 5)]

def process(tag, C):
    log = json.load(open(os.path.join(BASE, "committed_log%s.json" % tag)))
    d = log["dimH2"]; H2 = log["H2basis10"]; AUT = log["Aut_order"]; ACT = log["act_matrices" if "act_matrices" in log else "act"]
    # W conditions: w(3,j)=0, w(4,j)=0 for all j -> on 10-vec: pair idx of (min(3,j),max(3,j)) etc.
    conds = []
    for z in (3, 4):
        for j in range(5):
            if j == z: continue
            i, jj = (z, j) if z < j else (j, z)
            t = PAIRS.index((i, jj))
            conds.append(t)
    conds = sorted(set(conds))
    print(tag or "S0", "W conditions on 10-comps:", conds)
    # condition rows on coords: sum_b x_b H2[b][t] == 0 for t in conds
    Mrows = [[H2[b][t] % P for b in range(d)] for t in conds]
    Wc = null_rows(Mrows, d)
    dw = len(Wc)
    print("dim W =", dw, "basis:", Wc)
    # verify Aut-stability: each ACT row-map sends Wc span into itself
    def apply(Mm, v): return [sum(v[b]*Mm[b][c] for b in range(d)) % P for c in range(d)]
    # project: check rank([Wc..., M v]) == dw for each generator and each basis elt... simpler: image of each Wc basis elt lies in span(Wc)
    for Mm in ACT:
        for wv in Wc:
            im = apply(Mm, wv)
            assert rank_rows(Wc + [im]) == dw, ("W not stable", tag)
    print("W Aut-stable: OK")
    # enumerate W classes
    Wcls = []
    for coeff in range(P**dw):
        c = []; s = coeff
        for i in range(dw-1, -1, -1): c = [s % P] + c; s //= P
        v = [sum(c[k]*Wc[k][b] for k in range(dw)) % P for b in range(d)]
        Wcls.append(tuple(v))
    Wset = set(Wcls)
    print("|W| =", len(Wset))
    # induced action matrices on W coords: solve images
    # build solve: for w-im y (d-vec in W), find coeffs: use Wc pseudo-inverse via gaussian
    def to_wcoords(y):
        A = [[Wc[k][b] for k in range(dw)] for b in range(d)]  # d x dw
        rhs = list(y)
        M = [A[j][:] + [rhs[j]] for j in range(d)]
        where = [-1]*dw; r = 0
        for cc in range(dw):
            piv = next((i for i in range(r, d) if M[i][cc] % P != 0), None)
            if piv is None: continue
            M[r], M[piv] = M[piv], M[r]
            s = pow(M[r][cc], -1, P); M[r] = [x*s % P for x in M[r]]
            for i in range(d):
                if i != r and M[i][cc] % P != 0:
                    f = M[i][cc]
                    M[i] = [(M[i][j]-f*M[r][j]) % P for j in range(dw+1)]
            where[cc] = r; r += 1
        x = [0]*dw
        for cc in range(dw):
            if where[cc] != -1: x[cc] = M[where[cc]][dw]
        chk = [sum(x[k]*Wc[k][b] for k in range(dw)) % P for b in range(d)]
        assert chk == [v % P for v in y]
        return x
    A_W = []
    for Mm in ACT:
        cols = [to_wcoords(apply(Mm, wv)) for wv in Wc]
        # matrix dw x dw rows=images of basis
        A_W.append([row[:] for row in cols])
    # BFS orbits on W
    def enc(v):
        s = 0
        for x in v: s = s*P+x
        return s
    ALPH = A_W + [mat_inv(Mm) for Mm in A_W]
    seen = {}; orbits = []
    allc = []
    for coeff in range(P**dw):
        c = []; s = coeff
        for i in range(dw-1, -1, -1): c = [s % P] + c; s //= P
        allc.append(c)
    for c in allc:
        e = enc(c)
        if e in seen: continue
        o = len(orbits); cur = [c]; seen[e] = o
        bag = [c]; k = 0
        while k < len(bag):
            v = bag[k]; k += 1
            for Mm in ALPH:
                wv = [sum(v[b]*Mm[b][cc] for b in range(dw)) % P for cc in range(dw)]
                ee = enc(wv)
                if ee not in seen: seen[ee] = o; cur.append(wv); bag.append(wv)
        orbits.append(cur)
    print("num W orbits =", len(orbits))
    # per-orbit extension invariants
    for oi, o in enumerate(orbits):
        r = min(enc(c) for c in o)
        # decode r to w-coords then d-coords then 10-vec
        cc = []; s = r
        for i in range(dw-1, -1, -1): cc = [s % P] + cc; s //= P
        v = [sum(cc[k]*Wc[k][b] for k in range(dw)) % P for b in range(d)]
        w10 = [sum(v[b]*H2[b][t] for b in range(d)) % P for t in range(10)]
        # extension
        L = [[[0]*6 for _ in range(6)] for _ in range(6)]
        for kk in range(5):
            for i in range(5):
                for j in range(5): L[kk][i][j] = C[kk][i][j]
        for t,(i,j) in enumerate(PAIRS):
            L[5][i][j] = (L[5][i][j]+w10[t]) % P; L[5][j][i] = (L[5][j][i]-w10[t]) % P
        rows = []
        for j in range(6):
            for k in range(6): rows.append([L[k][i][j] % P for i in range(6)])
        Z = null_rows(rows, 6)
        Dr = [[L[k][i][j] % P for i in range(6) for j in range(6)] for k in range(6)]
        cl2 = True
        for a in range(6):
            for b in range(6):
                br = [L[k][a][b] for k in range(6)]
                for c_ in range(6):
                    for m in range(6):
                        if sum(br[k]*L[m][k][c_] for k in range(6)) % P != 0: cl2 = False
        print("  W-orbit", oi, "size", len(o), "stab", AUT//len(o),
              "wcoords", cc, "dcoords", v, "rep10", w10,
              "dimZ", len(Z), "dimD", rank_rows(Dr), "class<=2", cl2)
        assert AUT % len(o) == 0
    return orbits

C0 = [[[0]*5 for _ in range(5)] for _ in range(5)]
C0[3][0][1] = 1; C0[3][1][0] = 4; C0[4][0][2] = 1; C0[4][2][0] = 4
print("=== S0 ===")
process("", C0)
C1 = [[[0]*5 for _ in range(5)] for _ in range(5)]
for (i,j,k) in ((0,1,3),(0,2,4),(1,2,3)):
    C1[k][i][j] = 1; C1[k][j][i] = 4
print("=== S1 ===")
process("_S1", C1)
