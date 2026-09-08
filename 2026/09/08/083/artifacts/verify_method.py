"""Exact graded Betti numbers of edge ideals via Hochster's formula (stdlib only).
Over QQ: beta_{i,j}(S/I(G)) = sum_{|W|=j} dim Htilde_{j-i-1}(Ind(G[W])).
Exact rational homology ranks + Hilbert/Euler cross-check + induced matchings.
"""
from fractions import Fraction
import itertools, json

def rank_qq(mat):
    # mat: list of rows, each list of ints/Fractions; returns rank over QQ
    if not mat or not mat[0]:
        return 0
    M = [[Fraction(x) for x in row] for row in mat]
    r = len(M); c = len(M[0])
    piv = 0
    for col in range(c):
        f = None
        for i in range(piv, r):
            if M[i][col] != 0:
                f = i; break
        if f is None:
            continue
        M[piv], M[f] = M[f], M[piv]
        inv = 1 / M[piv][col]
        M[piv] = [v * inv for v in M[piv]]
        for i in range(r):
            if i != piv and M[i][col] != 0:
                s = M[i][col]
                M[i] = [a - s * b for a, b in zip(M[i], M[piv])]
        piv += 1
        if piv == r:
            break
    return piv

def betti_hochster(n, edges):
    adj = [[False]*n for _ in range(n)]
    for a, b in edges:
        adj[a][b] = adj[b][a] = True
    nbr = [0]*n
    for i in range(n):
        m = 0
        for j in range(n):
            if adj[i][j]:
                m |= (1 << j)
        nbr[i] = m
    betti = {}
    # precompute independent[q] for all masks q
    N = 1 << n
    is_indep = [True]*N
    for q in range(N):
        ok = True
        m = q
        while m:
            lsb = m & (-m)
            i = lsb.bit_length()-1
            if (q & nbr[i]) != 0:
                # need to ensure neighbor strictly inside q and avoid self; nbr has no self
                ok = False; break
            m ^= lsb
        is_indep[q] = ok
    for W in range(1, N):
        j = bin(W).count('1')
        # collect faces (independent submasks of W) by size
        faces = {}  # size -> list of masks
        F = W
        # iterate submasks
        s = W
        while True:
            if is_indep[s]:
                k = bin(s).count('1')
                faces.setdefault(k, []).append(s)
            if s == 0:
                break
            s = (s - 1) & W
        # index maps
        idx = {sz: {f: t for t, f in enumerate(fl)} for sz, fl in faces.items()}
        maxk = max(faces)
        # boundary ranks d_k : C_k -> C_{k-1}, k>=0, C_{-1} dim 1
        ranks = {}
        for k in range(0, maxk+1):
            dom = faces.get(k, [])
            if k == 0:
                # rows=1 (empty face), cols = #verts
                mat = [[1]*len(dom)] if dom else []
                ranks[k] = rank_qq(mat) if dom else 0
            else:
                cod = faces.get(k-1, [])
                if not dom or not cod:
                    ranks[k] = 0
                    continue
                # rows=cod, cols=dom
                mat = [[0]*len(dom) for _ in range(len(cod))]
                for ci, f in enumerate(dom):
                    # vertices of f sorted
                    vs = [v for v in range(n) if (f >> v) & 1]
                    for t, v in enumerate(vs):
                        g = f ^ (1 << v)
                        r = idx[k-1][g]
                        mat[r][ci] = 1 if (t % 2 == 0) else -1
                ranks[k] = rank_qq(mat)
        # homology dims: Htilde_{k-1} corresponds chain C_k? careful:
        # reduced homology Htilde_t, t>= -1. dim ker(d_t) - rank(d_{t+1}), C_t = span t+1-sets... our faces[size k] = C_{k-1}.
        # d_k computed above maps C_{k-1}... let me re-index: D_s: C_s -> C_{s-1}, C_s <-> faces[size s+1].
        # ranks keyed by size k = s+1. So rank(D_s) = ranks[s+1].
        def rankD(s):
            if s <= -1:
                return 0
            return ranks.get(s+1, 0)
        for t in range(-1, maxk):
            dimC = len(faces.get(t+1, []))  # C_t dim (C_{-1}: faces size0 = [0] if indep (always) -> 1)
            kd = dimC - rankD(t)
            hd = kd - rankD(t+1)
            if hd < 0:
                raise AssertionError("negative homology")
            if hd > 0 and t >= 0 - 0:
                # Hochster: k=j-i-1=t, j=|W| -> i=j-t-1
                if t == -1:
                    continue  # disconnected check below? include: t=-1 contributes beta_{j,j}? j-i-1=-1 -> i=j: beta_{j,j}= #components-1
                i = j - t - 1
                betti[(i, j)] = betti.get((i, j), 0) + hd
            elif hd > 0 and t == -1:
                i = j
                betti[(i, j)] = betti.get((i, j), 0) + hd
    return betti

def reg_pdim(betti):
    reg = 0; pd = 0
    for (i, j), v in betti.items():
        if v:
            reg = max(reg, j - i); pd = max(pd, i)
    return reg, pd

def hilbert_check(n, edges, betti):
    # K(t) = sum_{F indep} t^|F| (1-t)^{n-|F|}; E(t)=sum (-1)^i b t^j; check equal (degree<=n)
    N = 1 << n
    nbr = [0]*n
    for a, b in edges:
        nbr[a] |= (1 << b); nbr[b] |= (1 << a)
    from math import comb
    K = [Fraction(0)]*(n+1)
    for q in range(N):
        ok = True; m = q
        while m:
            lsb = m & (-m); i = lsb.bit_length()-1
            if q & nbr[i]:
                ok = False; break
            m ^= lsb
        if not ok:
            continue
        k = bin(q).count('1')
        # t^k (1-t)^{n-k}
        for s in range(n-k+1):
            K[k+s] += Fraction(comb(n-k, s)) * (Fraction(-1)**s)
    E = [Fraction(0)]*(n+1)
    E[0] += Fraction(1)  # beta_{0,0} = 1
    for (i, j), v in betti.items():
        E[j] += Fraction((-1)**i * v)
    return K == E, [str(x) for x in K], [str(x) for x in E]

def induced_matching(n, edges):
    adj = [[False]*n for _ in range(n)]
    for a, b in edges:
        adj[a][b] = adj[b][a] = True
    m = len(edges)
    best = []
    # order edges; branch and bound: state (idx, chosen list, used-set, banned-edge-set)
    # banned[e] = True if e shares a vertex with chosen or has an endpoint adjacent to chosen endpoint
    order = list(range(m))
    best_set = []
    def bound(idx, cur):
        return cur + (m - idx)
    import sys
    sys.setrecursionlimit(10000)
    # precompute conflict: e2 conflicts with e1 (e1 chosen) if they share a vertex
    # or any endpoint of e2 is adjacent to any endpoint of e1 (then e2 cannot join an induced matching containing e1)
    conf = [[False]*m for _ in range(m)]
    for i in range(m):
        a, b = edges[i]
        for j in range(m):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                conf[i][j] = True
            elif adj[a][c] or adj[a][d] or adj[b][c] or adj[b][d]:
                conf[i][j] = True
    chosen = []
    alive = [True]*m
    def dfs(idx, cur):
        nonlocal best_set
        # upper bound: cur + number of alive edges from idx on
        rem = sum(1 for k in range(idx, m) if alive[k])
        if cur + rem <= len(best_set):
            return
        if idx == m:
            if cur > len(best_set):
                best_set = list(chosen)
            return
        if not alive[idx]:
            dfs(idx+1, cur)
            return
        # branch: take idx
        killed = [k for k in range(idx+1, m) if alive[k] and conf[idx][k]]
        for k in killed:
            alive[k] = False
        chosen.append(idx)
        dfs(idx+1, cur+1)
        chosen.pop()
        for k in killed:
            alive[k] = True
        # branch: skip idx
        alive[idx] = False
        dfs(idx+1, cur)
        alive[idx] = True
    dfs(0, 0)
    wit = [edges[t] for t in best_set]
    return len(best_set), wit

def show(n, edges, name):
    b = betti_hochster(n, edges)
    r, p = reg_pdim(b)
    ok, K, E = hilbert_check(n, edges, b)
    im, wit = induced_matching(n, edges)
    print(f"== {name}: n={n} m={len(edges)} reg(S/I)={r} reg(I)={r+1} pdim={p} im={im} euler_ok={ok}")
    print("   betti(i,j)=v:", sorted(b.items()))
    print("   im witness:", wit)
    print("   K:", K)
    return {"name": name, "n": n, "edges": edges, "betti": [[i, j, v] for (i, j), v in sorted(b.items())],
            "reg_SI": r, "reg_I": r+1, "pdim": p, "im": im, "im_witness": wit, "euler_ok": ok, "K": K, "E": E}

if __name__ == "__main__":
    # G1: C5 blow-up, parts {2i,2i+1}
    e1 = []
    for i in range(5):
        A = [2*i, 2*i+1]; B = [2*((i+1) % 5), 2*((i+1) % 5)+1]
        for a in A:
            for b in B:
                e1.append([a, b])
    # G2: K5 on 0..4 + 5->{0,1}, 6->{1,2}, 7->{2,3}
    e2 = [[a, b] for a in range(5) for b in range(a+1, 5)] + [[5, 0], [5, 1], [6, 1], [6, 2], [7, 2], [7, 3]]
    # G3: C5 on 0..4 + pendants 5@0,6@1,7@2
    e3 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 0], [6, 1], [7, 2]]
    # G4: C5 + chordal attachments (9v): 5->{0,1},6->{2,3},7->{0,3},8->{1,4}
    e4 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 0], [5, 1], [6, 2], [6, 3], [7, 0], [7, 3], [8, 1], [8, 4]]
    # G5: partial blow-up sizes (2,2,2,2,1): parts P0={0,1},P1={2,3},P2={4,5},P3={6,7},P4={8}
    P = [[0, 1], [2, 3], [4, 5], [6, 7], [8]]
    e5 = []
    for i in range(5):
        for a in P[i]:
            for b in P[(i+1) % 5]:
                e5.append([a, b])
    res = {}
    res["G1"] = show(10, e1, "G1")
    res["G2"] = show(8, e2, "G2")
    res["G3"] = show(8, e3, "G3")
    res["G4"] = show(9, e4, "G4")
    res["G5"] = show(9, e5, "G5")
    with open("tables.json", "w") as f:
        json.dump(res, f, indent=1)
