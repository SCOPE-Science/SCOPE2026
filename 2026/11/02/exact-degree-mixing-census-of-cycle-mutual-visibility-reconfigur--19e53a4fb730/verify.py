"""Standalone exact-integer checks of the cycle triple-layer degree census.
Requires only Python 3 standard library. Run: python verify.py
"""
from collections import Counter, deque
from itertools import combinations


def expected(n):
    assert n >= 3
    if n == 3:
        return {0: 1}, {}
    if n == 4:
        return {2: 4}, {(2, 2): 4}
    if n == 5:
        return {2: 5}, {(2, 2): 5}
    if n == 6:
        return {3: 12, 6: 2}, {(3, 3): 12, (3, 6): 12}
    h = n // 2
    if n % 2:
        deg = {2: n, 4: n * (h - 2), 6: n * (h - 2) * (h - 3) // 6}
        edges = {(2, 4): 2 * n, (4, 4): n * (h - 2),
                 (4, 6): 2 * n * (h - 3),
                 (6, 6): n * (h - 3) * (h - 4) // 2}
    else:
        deg = {3: 2 * n, 4: n * (h - 3),
               6: n * (h - 1) * (h - 2) // 6}
        edges = {(3, 3): n, (3, 4): 2 * n, (3, 6): 2 * n,
                 (4, 4): n * (h - 4), (4, 6): 2 * n * (h - 3),
                 (6, 6): n * (h - 3) * (h - 2) // 2}
    return {k: v for k, v in deg.items() if v}, {k: v for k, v in edges.items() if v}


def gap_degree(a, b, c, h):
    g = (a, b, c)
    return sum(int(g[i] >= 2 and g[(i + 1) % 3] < h) +
               int(g[(i + 1) % 3] >= 2 and g[i] < h)
               for i in range(3))


def symbolic_comp_check(n):
    h = n // 2
    deg = Counter()
    edge = Counter()
    for a in range(1, h + 1):
        for b in range(1, h + 1):
            c = n - a - b
            if not 1 <= c <= h:
                continue
            deg[gap_degree(a, b, c, h)] += 1
            # Every undirected slide has exactly one clockwise direction.
            # The clockwise slide at the marked vertex turns (a,b,c)
            # into (a-1,b,c+1), provided a>=2 and c<h.
            if a >= 2 and c < h:
                u = gap_degree(a, b, c, h)
                v = gap_degree(a - 1, b, c + 1, h)
                edge[tuple(sorted((u, v)))] += 1
    assert all(v * n % 3 == 0 for v in deg.values())
    # A triple has three choices of marked vertex; an edge has a unique
    # clockwise slide and hence a unique marked source vertex.
    got_deg = {k: v * n // 3 for k, v in deg.items() if v}
    got_edge = {k: v * n for k, v in edge.items() if v}
    assert (got_deg, got_edge) == expected(n), (n, got_deg, got_edge, expected(n))
    assert sum(k * v for k, v in got_deg.items()) == 2 * sum(got_edge.values())
    h = n // 2
    formula_edges = (n * (h * h + h - 4) // 2 if n % 2 == 0
                     else n * h * (h - 1) // 2)
    assert sum(got_edge.values()) == formula_edges


def shortest_avoiding(n, start, stop, forbidden):
    # Independently test visibility from the original graph by BFS,
    # comparing to graph distance without forbidding the third token.
    q = deque([(start, 0)]); seen = {start}
    while q:
        x, d = q.popleft()
        if x == stop:
            return d
        for y in ((x + 1) % n, (x - 1) % n):
            if y not in forbidden and y not in seen:
                seen.add(y); q.append((y, d + 1))
    return n + 1


def direct_check(n):
    allowed = []
    for t in combinations(range(n), 3):
        ok = True
        for i, j in combinations(range(3), 2):
            u, v = t[i], t[j]
            k = t[3-i-j]
            graph_d = min((u-v) % n, (v-u) % n)
            if shortest_avoiding(n, u, v, {k}) != graph_d:
                ok = False; break
        if ok:
            allowed.append(t)
    ix = {t: i for i, t in enumerate(allowed)}
    adj = [set() for _ in allowed]
    for i, t in enumerate(allowed):
        ts = set(t)
        for x in t:
            for y in ((x-1)%n, (x+1)%n):
                if y not in ts:
                    s = tuple(sorted((ts-{x})|{y}))
                    if s in ix:
                        adj[i].add(ix[s])
    degrees = dict(Counter(len(a) for a in adj))
    edge_counts = dict(Counter(tuple(sorted((len(adj[i]), len(adj[j]))))
                               for i in range(len(allowed)) for j in adj[i] if i < j))
    assert (degrees,edge_counts)==expected(n), (n,degrees,edge_counts,expected(n))
    assert all(i in adj[j] for i,a in enumerate(adj) for j in a)


def main():
    for n in range(3, 181):
        symbolic_comp_check(n)
    print('EXACT_GAP_COMPOSITION_AND_HANDSHAKE_OK n=3..180')
    for n in range(3, 28):
        direct_check(n)
    print('INDEPENDENT_ORIGINAL_GRAPH_BFS_AND_SLIDES_OK n=3..27')
    print('PARITY_AND_SMALL_BOUNDARIES_OK')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
