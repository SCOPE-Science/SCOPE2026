from itertools import combinations
from collections import deque


def partitions(n, min_part=1):
    if n == 0:
        yield []
        return
    for first in range(min_part, n + 1):
        for rest in partitions(n - first, first):
            yield [first] + rest


def build_graph(parts):
    part_of = []
    for i, size in enumerate(parts):
        part_of += [i] * size
    n = len(part_of)
    adj = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if part_of[u] != part_of[v]:
                adj[u].append(v)
                adj[v].append(u)
    return part_of, adj


def distance_matrix(adj):
    n = len(adj)
    out = []
    for source in range(n):
        dist = [-1] * n
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        out.append(dist)
    return out


def direct_local_outer(mask, adj, dist):
    n = len(adj)
    chosen = [v for v in range(n) if (mask >> v) & 1]
    outside = [v for v in range(n) if not ((mask >> v) & 1)]
    rep = {v: tuple(sorted(dist[v][w] for w in chosen)) for v in outside}
    for u in outside:
        for v in adj[u]:
            if u < v and not ((mask >> v) & 1) and rep[u] == rep[v]:
                return False
    return True


def structural_local_outer(mask, parts, part_of):
    occupancy = [0] * len(parts)
    for v, p in enumerate(part_of):
        if (mask >> v) & 1:
            occupancy[p] += 1
    active = [occupancy[i] for i, size in enumerate(parts) if occupancy[i] < size]
    return len(active) == len(set(active))


def closed_formula(parts):
    sizes = sorted(parts)
    n = sum(sizes)
    r = len(sizes)
    best = None
    for k in range(1, r + 1):
        top = sizes[r - k:]
        if all(top[j - 1] >= j for j in range(1, k + 1)):
            value = n - sum(top) + k * (k - 1) // 2
            best = value if best is None else min(best, value)
    return best


graph_types = 0
subsets = 0
for n in range(2, 12):
    for parts in partitions(n):
        if len(parts) < 2:
            continue
        graph_types += 1
        part_of, adj = build_graph(parts)
        dist = distance_matrix(adj)
        direct_minimum = n + 1
        for mask in range(1 << n):
            subsets += 1
            direct = direct_local_outer(mask, adj, dist)
            structural = structural_local_outer(mask, parts, part_of)
            if direct != structural:
                raise SystemExit(
                    f"STRUCTURE FAIL parts={parts} mask={mask} direct={direct} structural={structural}"
                )
            if direct:
                direct_minimum = min(direct_minimum, mask.bit_count())
        formula = closed_formula(parts)
        if direct_minimum != formula:
            raise SystemExit(
                f"FORMULA FAIL parts={parts} direct={direct_minimum} formula={formula}"
            )

print(
    f"ALL CHECKS PASSED; multipartite_types={graph_types}; "
    f"subsets={subsets}; max_order=11"
)
