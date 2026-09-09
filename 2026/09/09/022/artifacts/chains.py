"""Build explicit Dilworth chain partitions for T5 and M6 via consecutive-layer
bipartite matchings (Hopcroft-Karp, stdlib only). Writes *_chains.csv and prints
certificate lines. Asserts #chains == width == middle-layer size.
"""
import csv
from collections import deque

def subsets(n, k):
    out = []
    def rec(i, k, m):
        if k == 0:
            out.append(m); return
        for j in range(i, n - k + 1):
            rec(j + 1, k - 1, m | (1 << j))
    rec(0, k, 0)
    return out

def hopcroft_karp(adj, left, right):
    matchL = {u: None for u in left}
    matchR = {v: None for v in right}
    INF = float('inf')
    def bfs():
        dist = {}
        q = deque()
        for u in left:
            if matchL[u] is None:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = matchR[v]
                if w is None:
                    found = True
                elif dist.get(w, INF) == INF:
                    dist[w] = dist[u] + 1; q.append(w)
        return found, dist
    def dfs(u, dist):
        for v in adj[u]:
            w = matchR[v]
            if w is None or (dist.get(w, INF) == dist[u] + 1 and dfs(w, dist)):
                matchL[u] = v; matchR[v] = u
                return True
        dist[u] = INF
        return False
    while True:
        found, dist = bfs()
        if not found:
            break
        for u in left:
            if matchL[u] is None:
                dfs(u, dist)
    return matchL, matchR

def build(n, rmin, rmax, tag):
    layers = {r: subsets(n, r) for r in range(rmin, rmax + 1)}
    match_down = {}  # (r, x) -> y in layer r-1 matched below x
    match_up = {}    # (r, x) -> y in layer r+1 matched above x
    for r in range(rmin, rmax):
        A, B = layers[r], layers[r + 1]
        adj = {a: [b for b in B if a & b == a] for a in A}
        mL, mR = hopcroft_karp(adj, A, B)
        size = sum(1 for a in A if mL[a] is not None)
        print(f"[{tag}] matching rank {r}->{r+1}: size {size} (|A|={len(A)}, |B|={len(B)})")
        for a in A:
            if mL[a] is not None:
                match_up[(r, a)] = mL[a]
                match_down[(r + 1, mL[a])] = a
    # assemble chains: start at elements with no match below, follow match_up
    chains = []
    for r in range(rmin, rmax + 1):
        for x in layers[r]:
            if (r, x) not in match_down:
                ch = [(r, x)]
                while (ch[-1][0], ch[-1][1]) in match_up or (ch[-1] in ch and False):
                    break
                while (ch[-1][0], ch[-1][1]) in [(k[0], k[1]) for k in [ch[-1]] ] and (ch[-1][0], ch[-1][1]) in match_up:
                    rr, xx = ch[-1]
                    ch.append((rr + 1, match_up[(rr, xx)]))
                chains.append([m for (_, m) in ch])
    # verify coverage exactly once
    Flat = [m for L in layers.values() for m in L]
    seen = [m for c in chains for m in c]
    assert sorted(seen) == sorted(Flat), f"[{tag}] coverage failed"
    assert len(seen) == len(set(seen)), f"[{tag}] duplicate coverage"
    for c in chains:
        cs = sorted(c, key=lambda m: bin(m).count('1'))
        assert cs == c or all(bin(c[i]).count('1') <= bin(c[i+1]).count('1') for i in range(len(c)-1))
        for i in range(len(cs) - 1):
            assert cs[i] & cs[i+1] == cs[i], f"[{tag}] chain not totally ordered"
    width_layer = max(len(L) for L in layers.values())
    print(f"[{tag}] NE={len(Flat)} nchains={len(chains)} maxlayer={width_layer}")
    assert len(chains) == width_layer, f"[{tag}] chains != width layer"
    with open(f"{tag}_chains.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chain_id", "length", "members"])
        for i, c in enumerate(chains):
            cs = sorted(c, key=lambda m: bin(m).count('1'))
            w.writerow([i, len(cs), " ".join(map(str, cs))])
    # width witness = largest layer
    W = max(layers.values(), key=len)
    print(f"[{tag}] width witness layer size {len(W)}: {' '.join(map(str, sorted(W)[:8]))} ...")
    return chains, sorted(W)

if __name__ == "__main__":
    build(5, 1, 4, "t5")
    build(6, 2, 4, "m6")
