"""Canonical enumeration of connected graphs (stdlib + numpy only).

Canonical augmentation (McKay-style): every connected (n+1)-graph H has a
non-cut vertex v with H-v connected, so H ~= G + new vertex (neighborhood S
nonempty) for some canonical connected n-graph G. Canonicalizing all such
extensions yields exactly the canonical connected (n+1)-graphs.

Canonical form: lex-min upper-triangle bitstring (edge 0 most significant)
over all n! vertex permutations; stored as LSB-first integer of the winning
labeling so extensions interpret bits consistently.
"""
import itertools
import json
import numpy as np


def edges_of(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def perm_maps(n):
    E = edges_of(n)
    pos = {e: k for k, e in enumerate(E)}
    M = []
    for p in itertools.permutations(range(n)):
        row = []
        for (i, j) in E:
            a, b = p[i], p[j]
            if a > b:
                a, b = b, a
            row.append(pos[(a, b)])
        M.append(row)
    return np.array(M, dtype=np.int32)


def bits_of(vals, m):
    B = np.zeros((len(vals), m), dtype=np.uint8)
    for b, v in enumerate(vals):
        for k in range(m):
            B[b, k] = (v >> k) & 1
    return B


def canonical_reps(vals, m, P):
    """Return LSB-first integer of lex-min labeling for each input."""
    Bm = bits_of(vals, m).astype(np.float64)
    W = 2.0 ** np.arange(m - 1, -1, -1)  # edge0 = MSB
    PW2 = 2.0 ** np.arange(m)            # LSB-first rep weights
    reps = np.zeros(len(vals), dtype=np.int64)
    C = 256
    bestV = np.full(len(vals), np.inf)
    bestQ = np.zeros(len(vals), dtype=np.int32)
    for s in range(0, len(P), C):
        Pc = P[s:s + C]
        T = Bm[:, Pc]                       # (B,C,m) permuted bitstrings
        V = np.einsum('bcm,m->bc', T, W)
        j = V.argmin(axis=1)
        Vb = V[np.arange(len(vals)), j]
        upd = Vb < bestV
        bestV[upd] = Vb[upd]
        bestQ[upd] = (s + j)[upd]
    for b in range(len(vals)):
        reps[b] = int((Bm[b, P[bestQ[b]]] * PW2).sum())
    return reps


def extend_bits(gbits, n, S):
    Enew = edges_of(n + 1)
    newpos = {e: k for k, e in enumerate(Enew)}
    Eold = edges_of(n)
    v = 0
    for k in range(len(Eold)):
        if (gbits >> k) & 1:
            v |= 1 << newpos[Eold[k]]
    for i in range(n):
        if (S >> i) & 1:
            v |= 1 << newpos[(min(i, n), max(i, n))]
    return v


def census_up_to(N):
    levels = {1: [0]}
    for n in range(1, N):
        m = (n + 1) * n // 2
        P = perm_maps(n + 1)
        exts = []
        for g in levels[n]:
            for S in range(1, 1 << n):
                exts.append(extend_bits(g, n, S))
        reps = canonical_reps(exts, m, P)
        levels[n + 1] = sorted(set(reps.tolist()))
    return levels


def bits_to_edges(v, n):
    E = edges_of(n)
    return [[i, j] for k, (i, j) in enumerate(E) if (v >> k) & 1]


def is_connected(v, n):
    E = edges_of(n)
    adj = [[] for _ in range(n)]
    for k, (i, j) in enumerate(E):
        if (v >> k) & 1:
            adj[i].append(j)
            adj[j].append(i)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


if __name__ == '__main__':
    levels = census_up_to(7)
    for n in sorted(levels):
        print(f'n={n}: {len(levels[n])} canonical graphs')
        assert all(is_connected(v, n) for v in levels[n]), f'disconnected at {n}'
    assert len(levels[5]) == 21, len(levels[5])
    assert len(levels[6]) == 112, len(levels[6])
    assert len(levels[7]) == 853, len(levels[7])
    print('COUNTS OK: 21 / 112 / 853 (OEIS A001349); all connected')
    out = {}
    for n in (5, 6, 7):
        out[str(n)] = [
            {'id': i, 'canon': int(v), 'edges': bits_to_edges(int(v), n)}
            for i, v in enumerate(levels[n])
        ]
    with open('graphs567.json', 'w') as f:
        json.dump(out, f)
    print('wrote graphs567.json')
