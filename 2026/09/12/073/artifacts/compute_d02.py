"""Compute ker(d^{0,2}: E2^{0,2} -> E2^{2,1}) for F_n(T*) over Fp.
E02 = Lambda^2(G)/Arnold. E21 = (H^2 x G)/sliding-relations.
d(G_e G_f) = Delta_e G_f - Delta_f G_e.
Steps: build Q21 quotient per edge, project, check Arnold maps to 0, compute rank.
"""
import itertools
import numpy as np
from explore_dims import build_H, cup, pairs_list, rank_mod, nullspace_mod

P = 1000003

def edge_key(n, e):
    return e

for n in range(2, 8):
    mons, index_of, N = build_H(n)
    H1 = mons.get(1, []); H2 = mons.get(2, []); H3 = mons.get(3, [])
    d1, d2 = len(H1), len(H2)
    h1idx = {m: k for k, m in enumerate(H1)}
    h2idx = {m: k for k, m in enumerate(H2)}
    pairs = pairs_list(n)
    ng = len(pairs)
    gindex = {p: k for k, p in enumerate(pairs)}
    Delta = np.zeros((ng, d2), dtype=np.int64)
    for k, (i, j) in enumerate(pairs):
        m_a = tuple(sorted([2*i, 2*j+1]))
        m_b = tuple(sorted([2*i+1, 2*j]))
        Delta[k, h2idx[m_a]] += 1
        Delta[k, h2idx[m_b]] -= 1
    Delta %= P
    # F21 coords: (c in H2, k edge) index c*ng+k
    F = d2*ng
    def f21(c, k):
        return c*ng + k
    # relations: for each edge k=(i,j), each h in H1, each mu in H1:
    # ((h_i - h_j) cup mu) \otimes G_k
    Rrows = []
    for k, (i, j) in enumerate(pairs):
        for h in H1:
            hg = h[0]
            # point index of generator: hg//2, type hg%2
            for mu in H1:
                # (h_i cup mu) - (h_j cup mu)
                vec = np.zeros(F, dtype=np.int64)
                for (pt, sgn) in [(i, 1), (j, -1)]:
                    # generator h at point pt: same type, point pt
                    g = 2*pt + (hg % 2)
                    r = cup((g,), mu, None, n)
                    if r is None:
                        continue
                    _, m2v, s = r
                    vec[f21(h2idx[m2v], k)] += sgn*s
                if np.any(vec):
                    Rrows.append(vec % P)
    R = np.array(Rrows, dtype=np.int64) % P if Rrows else np.zeros((0, F), dtype=np.int64)
    rR = rank_mod(R, P)
    dimQ21 = F - rR
    # projection: nullspace of R gives quotient dual; instead compute maps into F mod R:
    # map Phi: free pairs -> F, then compose with projection. rank of induced = rank([Phi; R])-rR trick:
    # Build lifted matrix L: rows = free-pair basis images in F.
    from math import comb
    gpair_list = [(u, v) for u in range(ng) for v in range(u+1, ng)]
    gpidx = {p: k for k, p in enumerate(gpair_list)}
    Nfree = len(gpair_list)
    L = np.zeros((Nfree, F), dtype=np.int64)
    for q, (u, v) in enumerate(gpair_list):
        # G_u G_v -> Delta_u G_v - Delta_v G_u
        for c in range(d2):
            L[q, f21(c, v)] += Delta[u, c]
            L[q, f21(c, u)] -= Delta[v, c]
    L %= P
    # well-definedness: Arnold rows map into row-space of R
    arn_rows = []
    for (i, j, k_) in itertools.combinations(range(n), 3):
        e1 = gindex[tuple(sorted([i, j]))]
        e2 = gindex[tuple(sorted([j, k_]))]
        e3 = gindex[tuple(sorted([i, k_]))]
        row = np.zeros(Nfree, dtype=np.int64)
        for (u, v, s) in [(e1, e2, 1), (e2, e3, 1), (e3, e1, 1)]:
            if u < v:
                row[gpidx[(u, v)]] += s
            else:
                row[gpidx[(v, u)]] -= s
        arn_rows.append(row)
    if arn_rows:
        Arn = np.array(arn_rows, dtype=np.int64) % P
        # image of Arnold in F
        Aimg = (Arn @ L) % P
        # check each row in row-space of R: rank([R;row])==rR
        ok = True
        for t in range(Aimg.shape[0]):
            if np.all(Aimg[t] == 0):
                continue
            S = np.vstack([R, Aimg[t]]) % P
            if rank_mod(S, P) != rR:
                ok = False
                break
        rA = rank_mod(Arn, P)
    else:
        ok = True; rA = 0
        Aimg = np.zeros((0, F))
    dimE02 = Nfree - rA
    # rank of induced map E02 -> Q21: rank of L restricted mod R and mod Arnold:
    # induced rank = rank( vstack[L, R, ArnoldLifted?] ) ... simpler:
    # rank_induced = rank([L; R]) - rR - (correction if Arnold not in ker... but Arnold maps into R so fine)
    stacked = np.vstack([L, R]) % P if R.shape[0] else L % P
    rstack = rank_mod(stacked, P)
    rind = rstack - rR
    dimker = dimE02 - rind
    print(f"n={n} F21={F} nRrel={R.shape[0]} rankR={rR} dimQ21={dimQ21} ArnOK={ok} "
          f"dimE02={dimE02} rank_ind={rind} dimker(d02)={dimker}")
    # also total H^2 dim under collapse
    from math import comb as C
    pred = 2*C(n, 3) + 5*C(n, 2) if n >= 3 else (3 if n == 2 else 0)
    print(f"   predicted dim={pred}")
