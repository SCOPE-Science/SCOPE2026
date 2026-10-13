from itertools import combinations, permutations
from collections import Counter, deque
from math import ceil


def edge_pairs(n):
    return list(combinations(range(n), 2))


def adjacency(n, mask):
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(edge_pairs(n)):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj


def connected_bfs(adj):
    n = len(adj)
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == n


def connected_floyd(adj):
    n = len(adj)
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
        for j in adj[i]:
            reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return all(reach[0])


def threshold(adj, v):
    # ceil((deg(v)+1)/2) = floor(deg(v)/2)+1
    return (len(adj[v]) // 2) + 1


def closure_rounds(adj, seeds):
    active = set(seeds)
    while True:
        add = {
            v for v in range(len(adj)) if v not in active
            and len(adj[v] & active) >= threshold(adj, v)
        }
        if not add:
            return frozenset(active)
        active |= add


def closure_queue(adj, seeds):
    n = len(adj)
    active = [False] * n
    count = [0] * n
    q = deque()
    for s in seeds:
        active[s] = True
    for v in range(n):
        if not active[v]:
            count[v] = sum(active[u] for u in adj[v])
            if count[v] >= threshold(adj, v):
                q.append(v)
    queued = set(q)
    while q:
        v = q.popleft()
        queued.discard(v)
        if active[v] or count[v] < threshold(adj, v):
            continue
        active[v] = True
        for w in adj[v]:
            if not active[w]:
                count[w] += 1
                if count[w] >= threshold(adj, w) and w not in queued:
                    q.append(w)
                    queued.add(w)
    return frozenset(i for i, x in enumerate(active) if x)


def high_degree_pairs_by_score(adj):
    pairs = list(combinations(range(len(adj)), 2))
    scores = [len(adj[u]) + len(adj[v]) for u, v in pairs]
    best = max(scores)
    return [p for p, s in zip(pairs, scores) if s == best]


def unique_high_degree_pair_by_order(adj):
    n = len(adj)
    if n == 2:
        return (0, 1)
    deg = [len(a) for a in adj]
    order = sorted(range(n), key=lambda v: (-deg[v], v))
    if deg[order[1]] > deg[order[2]]:
        return tuple(sorted(order[:2]))
    return None


def permute_mask(n, mask, p):
    index = {e: i for i, e in enumerate(edge_pairs(n))}
    out = 0
    for bit, (u, v) in enumerate(edge_pairs(n)):
        if (mask >> bit) & 1:
            a, b = sorted((p[u], p[v]))
            out |= 1 << index[(a, b)]
    return out


def canonical_mask(n, mask):
    return min(permute_mask(n, mask, p) for p in permutations(range(n)))


def orbit(n, mask):
    return {permute_mask(n, mask, p) for p in permutations(range(n))}


def edge_list(n, mask):
    return [e for bit, e in enumerate(edge_pairs(n)) if (mask >> bit) & 1]


connected_counts = {}
unique_hd_counts = {}
failure_counts = {}
failure_masks_5 = []
unique_hd_classes_5 = Counter()
failure_classes_5 = Counter()
spread_pairs_5 = Counter()

for n in range(2, 6):
    m = n * (n - 1) // 2
    conn = unique_hd = failures = 0
    for mask in range(1 << m):
        adj = adjacency(n, mask)
        c1 = connected_bfs(adj)
        c2 = connected_floyd(adj)
        assert c1 == c2
        if not c1:
            continue
        conn += 1

        score_pairs = high_degree_pairs_by_score(adj)
        ordered_pair = unique_high_degree_pair_by_order(adj)
        if len(score_pairs) == 1:
            assert ordered_pair == score_pairs[0]
        else:
            assert ordered_pair is None
        if ordered_pair is None:
            continue

        unique_hd += 1
        pairs = list(combinations(range(n), 2))
        spreads = {}
        for pair in pairs:
            a = closure_rounds(adj, pair)
            b = closure_queue(adj, pair)
            assert a == b
            spreads[pair] = len(a)
        heuristic_spread = spreads[ordered_pair]
        optimum = max(spreads.values())

        if n == 5:
            c = canonical_mask(n, mask)
            unique_hd_classes_5[c] += 1
            spread_pairs_5[(heuristic_spread, optimum)] += 1

        if heuristic_spread < optimum:
            failures += 1
            if n == 5:
                failure_masks_5.append(mask)
                failure_classes_5[canonical_mask(n, mask)] += 1
        if n <= 4:
            assert heuristic_spread == optimum == n

    connected_counts[n] = conn
    unique_hd_counts[n] = unique_hd
    failure_counts[n] = failures

assert connected_counts == {2: 1, 3: 4, 4: 38, 5: 728}
assert unique_hd_counts == {2: 1, 3: 0, 4: 18, 5: 290}
assert failure_counts == {2: 0, 3: 0, 4: 0, 5: 60}
assert spread_pairs_5 == Counter({(5, 5): 230, (3, 5): 60})
assert len(unique_hd_classes_5) == 7
assert len(failure_classes_5) == 1

HOUSE_MASK = 221
HOUSE_EDGES = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3)]
assert canonical_mask(5, HOUSE_MASK) == HOUSE_MASK
assert edge_list(5, HOUSE_MASK) == HOUSE_EDGES
assert failure_classes_5 == Counter({HOUSE_MASK: 60})
assert len(orbit(5, HOUSE_MASK)) == 60
assert sum(1 for p in permutations(range(5)) if permute_mask(5, HOUSE_MASK, p) == HOUSE_MASK) == 2
assert set(failure_masks_5) == orbit(5, HOUSE_MASK)

house = adjacency(5, HOUSE_MASK)
deg = tuple(len(a) for a in house)
tau = tuple(threshold(house, v) for v in range(5))
assert deg == (3, 3, 2, 2, 2)
assert tau == (2, 2, 2, 2, 2)
assert high_degree_pairs_by_score(house) == [(0, 1)]

house_spreads = {p: len(closure_rounds(house, p)) for p in combinations(range(5), 2)}
assert house_spreads[(0, 1)] == 3
assert max(house_spreads.values()) == 5
optimal_pairs = {p for p, s in house_spreads.items() if s == 5}
assert optimal_pairs == {(0, 2), (1, 3), (2, 4), (3, 4)}
assert closure_rounds(house, (0, 1)) == frozenset({0, 1, 4})
assert closure_rounds(house, (0, 2)) == frozenset(range(5))

# Direct lower-bound structure at n=4: the only connected isomorphism classes
# with an unambiguous two-highest-degree pair are P4 and K4 minus one edge.
classes4 = Counter()
unique_classes4 = {}
for mask in range(1 << 6):
    adj = adjacency(4, mask)
    if not connected_bfs(adj):
        continue
    c = canonical_mask(4, mask)
    classes4[c] += 1
for c, count in classes4.items():
    adj = adjacency(4, c)
    pair = unique_high_degree_pair_by_order(adj)
    if pair is not None:
        unique_classes4[c] = (count, edge_list(4, c), tuple(len(a) for a in adj), len(closure_rounds(adj, pair)))
assert len(classes4) == 6
assert set(unique_classes4) == {13, 31}
assert unique_classes4[13][3] == 4
assert unique_classes4[31][3] == 4

print('VERIFY_OK')
print('connected_counts', connected_counts)
print('unique_high_degree_pair_counts', unique_hd_counts)
print('suboptimal_high_degree_pair_counts', failure_counts)
print('n5_unique_hd_spread_vs_optimum', dict(sorted(spread_pairs_5.items())))
print('n5_unique_hd_isomorphism_classes', len(unique_hd_classes_5))
print('n5_failure_isomorphism_classes', dict(failure_classes_5))
print('house_edges', HOUSE_EDGES)
print('house_degrees', deg)
print('house_thresholds', tau)
print('house_high_degree_pair_spread', house_spreads[(0, 1)])
print('house_optimal_spread', max(house_spreads.values()))
print('house_optimal_pairs', sorted(optimal_pairs))
print('house_orbit_size', len(orbit(5, HOUSE_MASK)))
print('house_automorphism_order', 2)
