"""Certificate for emergent finding (lane-720): intact-row disjoint-crossing theorem.
Proves, with exact integer arithmetic + node-split Dinic max-flow/min-cut:
 (a) level-k kept-cell graphs (k=1,2,3) have EXACT left-right Menger width 5^k,
     realized by the 5^k intact rows (base-7 y-digits in {0,1,2,5,6}), all of length 7^k;
 (b) hence combinatorial LR-modulus lower bounds M_k(p) >= g(p)^k, g(p)=5*7^{1-p},
     with g(p)>1 for p < 1+log5/log7 (certified integer witness 5^100000>=7^82708);
 (c) certified Hausdorff upper edge log46/log7 <= 1.96754 (witness 46^100000<=7^196754).
Maximality (upper side of the widths) is certified by max-flow/min-cut on the
node-split network (source->A cap 1, B->sink cap 1, vin->vout cap 1, undirected
edges as paired infinite-capacity arcs); achieved flows are asserted 5/25/125.
The level-1 LP-duality modulus enclosure is NOT part of this certificate
(kept only as an uncertified exploratory baseline elsewhere).
Stdlib + numpy only."""
import math
import sys
from collections import deque
import numpy as np

sys.setrecursionlimit(1000000)

P = 7
HOLE = {(2, 3), (3, 3), (3, 4)}
INTACT = {0, 1, 2, 5, 6}
INF = 10 ** 9


def occ_grid(level):
    n = P ** level
    occ = np.ones((n, n), dtype=bool)
    for x in range(n):
        for y in range(n):
            xx, yy = x, y
            keep = True
            for _ in range(level):
                if (xx % 7, yy % 7) in HOLE:
                    keep = False
                    break
                xx //= 7
                yy //= 7
            occ[x, y] = keep
    return occ


def build_graph(occ):
    n = occ.shape[0]
    idx = -np.ones((n, n), dtype=int)
    cells = np.argwhere(occ)
    for k, (x, y) in enumerate(cells):
        idx[x, y] = k
    N = len(cells)
    nbrs = [[] for _ in range(N)]
    for k, (x, y) in enumerate(cells):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if 0 <= xx < n and 0 <= yy < n and occ[xx, yy]:
                nbrs[k].append(int(idx[xx, yy]))
    A = [k for k, (x, y) in enumerate(cells) if x == 0]
    B = [k for k, (x, y) in enumerate(cells) if x == n - 1]
    return cells, nbrs, A, B


class Dinic:
    __slots__ = ("n", "g", "level", "it")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def bfs(self, s, t):
        level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        g = self.g
        while q:
            u = q.popleft()
            for e in g[u]:
                if e[1] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])
        self.level = level
        return level[t] >= 0

    def dfs(self, u, t, f):
        if u == t:
            return f
        g = self.g
        level = self.level
        it = self.it
        while it[u] < len(g[u]):
            e = g[u][it[u]]
            if e[1] > 0 and level[u] < level[e[0]]:
                ret = self.dfs(e[0], t, f if f < e[1] else e[1])
                if ret:
                    e[1] -= ret
                    g[e[0]][e[2]][1] += ret
                    return ret
            it[u] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow


def max_vertex_disjoint(nbrs, A, B):
    """Exact max number of vertex-disjoint A->B paths via node splitting."""
    N = len(nbrs)
    SRC = 2 * N
    SNK = 2 * N + 1
    d = Dinic(2 * N + 2)
    for v in range(N):
        d.add_edge(v, v + N, 1)  # vin -> vout, vertex capacity 1
    for u in range(N):
        for w in nbrs[u]:
            if w > u:
                d.add_edge(u + N, w, INF)  # u_out -> w_in
                d.add_edge(w + N, u, INF)  # w_out -> u_in
    for a in A:
        d.add_edge(SRC, a, 1)
    for b in B:
        d.add_edge(b + N, SNK, 1)
    return d.max_flow(SRC, SNK)


def intact_rows(level):
    n = P ** level
    rows = []
    for y in range(n):
        yy = y
        digs = []
        for _ in range(level):
            digs.append(yy % 7)
            yy //= 7
        if all(dd in INTACT for dd in digs):
            rows.append(y)
    return rows


print("=== (i) intact-row counts (achievability) ===")
for k in (1, 2, 3):
    r = intact_rows(k)
    assert len(r) == 5 ** k, (k, len(r))
    occ = occ_grid(k)
    n = P ** k
    assert all(bool(occ[x, y]) for y in r for x in range(n)), f"row kept fail k={k}"
    assert all(sum(1 for x in range(n) if occ[x, y]) == n for y in r), f"row length fail k={k}"
    print(f"level {k}: {len(r)} intact rows == 5^{k}, each fully kept of length {n}: OK")

print("=== (ii) exact Menger widths (node-split Dinic max-flow/min-cut) ===")
for k in (1, 2, 3):
    occ = occ_grid(k)
    cells, nbrs, A, B = build_graph(occ)
    print(f"level {k}: N={len(cells)} |A|={len(A)} |B|={len(B)}, running Dinic...", flush=True)
    flow = max_vertex_disjoint(nbrs, A, B)
    assert flow == 5 ** k, (k, flow)
    print(f"level {k}: max-flow/min-cut = {flow} == 5^{k}: OK", flush=True)

print("=== (iii) modulus lower bounds g(p)^k ===")
for p in (1.6, 1.7, 1.8, 1.82):
    g = 5 * 7 ** (1 - p)
    print(f"p={p}: g={g:.6f} M1>={g:.4f} M2>={g**2:.4f} M3>={g**3:.4f} growing={g > 1}")

print("=== (iv) certified integer witnesses ===")
assert 5 ** 100000 >= 7 ** 82708
print("5^100000 >= 7^82708: True  (=> log5/log7 >= 0.82708, so Q_LR >= 1.82708)")
assert not (5 ** 100000 >= 7 ** 82709)
print("5^100000 >= 7^82709: False (=> edge decimal 1.82708 is sharp at 5 digits)")
assert 46 ** 100000 <= 7 ** 196754
print("46^100000 <= 7^196754: True  (=> log46/log7 <= 1.96754)")
q = 1 + math.log(5) / math.log(7)
print(f"edge 1+log5/log7 = {q:.10f} (double-precision evaluation only)")
print("ALL CERTIFICATES OK")
