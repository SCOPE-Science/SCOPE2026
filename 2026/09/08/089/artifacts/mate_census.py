"""Exact mate-stratum census for the fixed Egan-Wanless pair (A,B) (stdlib only).

For X in (A,B): enumerate all transversals of X, all 1-partitions (mates),
and the deficit distribution of the OTHER pair's overlay.
Deterministic; prints exact census. Replay in seconds.
"""
import json
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sq = json.load(open(HERE / "squares.json"))


def grid(rows):
    return [[int(c) for c in r] for r in rows]


A, B = grid(sq["A"]), grid(sq["B"])


def census(X, Y, label):
    n = 10
    cellY = [Y[i][j] for i in range(n) for j in range(n)]
    trans = []

    def bt(r, cm, sm, cur):
        if r == n:
            trans.append(tuple(cur))
            return
        gr = X[r]
        for c in range(n):
            if (cm >> c) & 1:
                continue
            s = gr[c]
            if (sm >> s) & 1:
                continue
            cur.append(r * 10 + c)
            bt(r + 1, cm | (1 << c), sm | (1 << s), cur)
            cur.pop()

    t0 = time.time()
    bt(0, 0, 0, [])
    masks, dup = [], []
    for t in trans:
        m = 0
        bs = 0
        for c in t:
            m |= (1 << c)
            bs |= (1 << cellY[c])
        masks.append(m)
        dup.append(10 - bin(bs).count("1"))
    bycell = [[] for _ in range(100)]
    for i, t in enumerate(trans):
        for c in t:
            bycell[c].append(i)
    FULL = (1 << 100) - 1
    dist = Counter()
    nodes = [0]

    def dfs(used, s):
        nodes[0] += 1
        if used == FULL:
            dist[s] += 1
            return
        u = (~used) & FULL
        cell = (u & (-u)).bit_length() - 1
        for i in bycell[cell]:
            if masks[i] & used:
                continue
            dfs(used | masks[i], s + dup[i])

    dfs(0, 0)
    dt = time.time() - t0
    total = sum(dist.values())
    print(f"mates-of-{label}: n_trans={len(trans)} n_partitions={total} "
          f"min_deficit={min(dist)} n_opt={dist[min(dist)]} time={dt:.1f}s",
          flush=True)
    print(f"  deficit distribution: {dict(sorted(dist.items()))}", flush=True)
    return len(trans), total, min(dist), dist[min(dist)]


na, pa, mina, nopta = census(A, B, "A (BC-deficit)")
nb, pb, minb, noptb = census(B, A, "B (AC-deficit)")
print(f"CENSUS_OK A:({na},{pa},{mina},{nopta}) B:({nb},{pb},{minb},{noptb})")
