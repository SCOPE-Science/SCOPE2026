from itertools import combinations, product
from functools import lru_cache

def graph_from_mask(n, mask):
    edges = list(combinations(range(n), 2))
    adj = [0] * n
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj

def all_distances(adj):
    n = len(adj)
    inf = 99
    d = [[inf] * n for _ in range(n)]
    for u in range(n):
        d[u][u] = 0
        for v in range(n):
            if (adj[u] >> v) & 1:
                d[u][v] = 1
    for w in range(n):
        for u in range(n):
            for v in range(n):
                z = d[u][w] + d[w][v]
                if z < d[u][v]:
                    d[u][v] = z
    return d

def diameter(adj):
    d = all_distances(adj)
    return max(max(row) for row in d), d

def maximal_independent_sizes(adj):
    n = len(adj)
    full = (1 << n) - 1
    sizes = set()
    for s in range(1, 1 << n):
        independent = True
        for v in range(n):
            if ((s >> v) & 1) and (adj[v] & s):
                independent = False
                break
        if not independent:
            continue
        covered = s
        for v in range(n):
            if (s >> v) & 1:
                covered |= adj[v]
        if covered == full:
            sizes.add(s.bit_count())
    return sizes

def packing_ok(f, d):
    n = len(f)
    for u in range(n):
        for v in range(u + 1, n):
            if f[u] == f[v]:
                color = f[u]
                separation = color
                if d[u][v] <= separation:
                    return False
    return True

def maximum_broadcast_partition(f, d):
    n = len(f)
    full = (1 << n) - 1
    dominates = [False] * (1 << n)
    for block in range(1, 1 << n):
        ok = True
        for x in range(n):
            if not any(((block >> w) & 1) and d[x][w] <= f[w] for w in range(n)):
                ok = False
                break
        dominates[block] = ok

    @lru_cache(None)
    def best(mask):
        if mask == 0:
            return 0
        first = mask & -mask
        ans = -100
        sub = mask
        while sub:
            if (sub & first) and dominates[sub]:
                ans = max(ans, 1 + best(mask ^ sub))
            sub = (sub - 1) & mask
        return ans

    return best(full)

def brute_profile(adj, d):
    n = len(adj)
    best = [10**9] * (n + 1)
    examined = 0
    packing_colorings = 0
    for f in product(range(1, n + 2), repeat=n):
        examined += 1
        if not packing_ok(f, d):
            continue
        packing_colorings += 1
        blocks = maximum_broadcast_partition(f, d)
        t = max(f)
        for k in range(1, blocks + 1):
            if t < best[k]:
                best[k] = t
    return best[1:], examined, packing_colorings

def theorem_profile(adj):
    n = len(adj)
    sizes = maximal_independent_sizes(adj)
    alpha = max(sizes)
    c = n - alpha + 1
    out = []
    for k in range(1, n + 1):
        if k <= c:
            out.append(c)
        elif n - k + 1 in sizes:
            out.append(k)
        else:
            out.append(k + 1)
    return out

graphs = 0
colorings = 0
packing_colorings = 0
by_order = {}

for n in range(3, 6):
    local = 0
    edge_count = n * (n - 1) // 2
    for mask in range(1 << edge_count):
        adj = graph_from_mask(n, mask)
        diam, d = diameter(adj)
        if diam != 2:
            continue
        graphs += 1
        local += 1
        expected = theorem_profile(adj)
        observed, checked, packed = brute_profile(adj, d)
        colorings += checked
        packing_colorings += packed
        if observed != expected:
            raise AssertionError(
                ("profile mismatch", n, mask, expected, observed, maximal_independent_sizes(adj))
            )
    by_order[n] = local

print(
    "ALL CHECKS PASSED; "
    f"graphs={graphs}; "
    f"graphs_by_order=3:{by_order[3]},4:{by_order[4]},5:{by_order[5]}; "
    f"colorings_examined={colorings}; "
    f"packing_colorings={packing_colorings}; "
    "orders=3..5"
)
