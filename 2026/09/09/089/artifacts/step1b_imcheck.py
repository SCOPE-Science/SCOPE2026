"""Step 1b: independent recheck of induced matching + matching stats."""
import itertools

n = 14
nbr = {i: set() for i in range(n)}
for i in range(n):
    for d in (1, 3):
        nbr[i].add((i + d) % n)
        nbr[i].add((i - d) % n)
edges = sorted((a, b) for a in range(n) for b in nbr[a] if a < b)
assert len(edges) == 28 and all(len(nbr[i]) == 4 for i in range(n))

def dist_ok(e, f):
    # induced matching condition: no edge with one end in e and other in f
    return not any(w in nbr[u] for u in e for w in f)

# brute force max induced matching via backtracking
best = [0]; wit = [None]
E = edges
def bt(i, chosen):
    if i == len(E):
        if len(chosen) > best[0]:
            best[0] = len(chosen); wit[0] = list(chosen)
        return
    # bound prune
    if len(chosen) + (len(E) - i) <= best[0]:
        return
    bt(i + 1, chosen)
    e = E[i]
    if all(dist_ok(e, f) for f in chosen) and not any(v in f for f in chosen for v in e):
        # also need disjointness (implied by dist_ok? sharing a vertex means... check separately)
        chosen.append(e); bt(i + 1, chosen); chosen.pop()

bt(0, [])
print("im(G) =", best[0], "witness:", wit[0])

# ordinary matching number (blossom-less: bipartite -> Hopcroft-Karp)
from collections import deque
part0 = [i for i in range(n) if i % 2 == 0]
mate = {}
def hk():
    from collections import deque
    INF = 10**9
    pairU = {u: None for u in part0}
    pairV = {}
    dist = {}
    def bfs():
        q = deque()
        for u in part0:
            if pairU[u] is None:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for w in nbr[u]:
                    v = w
                    if v not in pairV or pairV[v] is None:
                        d = dist[u] + 1
                    else:
                        uu = pairV[v]
                        if dist[uu] == INF:
                            dist[uu] = dist[u] + 1; q.append(uu)
        return d != INF
    def dfs(u):
        for w in nbr[u]:
            v = w
            if v not in pairV or pairV[v] is None or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                pairU[u] = v; pairV[v] = u
                return True
        dist[u] = INF
        return False
    m = 0
    while bfs():
        for u in part0:
            if pairU[u] is None and dfs(u):
                m += 1
    return m
print("matching number =", hk())
# girth
def girth():
    import collections
    best = 10**9
    for s in range(n):
        dist = {s: 0}; par = {s: -1}
        q = collections.deque([s])
        while q:
            u = q.popleft()
            for w in nbr[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1; par[w] = u; q.append(w)
                elif par[u] != w and par.get(w, -2) != u:
                    best = min(best, dist[u] + dist[w] + 1)
    return best
print("girth =", girth())
# co-chordal / gap-free? check for induced 2K2 (= induced matching size 2 exists -> not gap-free)
print("gap-free (im<=1):", best[0] <= 1)
