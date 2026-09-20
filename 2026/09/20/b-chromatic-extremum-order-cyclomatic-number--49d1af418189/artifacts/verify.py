"""Finite checks for the fixed-order/fixed-cycle-rank b-chromatic extremum."""
import networkx as nx
from collections import defaultdict
from math import isqrt


def partitions_rgs(n):
    a = [0] * n
    if n == 0:
        yield ()
        return
    a[0] = 0
    def rec(i, mx):
        if i == n:
            yield tuple(a)
            return
        for x in range(mx + 2):
            a[i] = x
            yield from rec(i + 1, max(mx, x))
    yield from rec(1, 0)


def b_number(G):
    nodes = list(G.nodes())
    n = len(nodes)
    pos = {v: i for i, v in enumerate(nodes)}
    edges = [(pos[u], pos[v]) for u, v in G.edges()]
    nbr = [set(pos[w] for w in G.neighbors(v)) for v in nodes]
    best = 1 if n else 0
    for c in partitions_rgs(n):
        k = 1 + max(c, default=-1)
        if k <= best or any(c[u] == c[v] for u, v in edges):
            continue
        good = True
        for color in range(k):
            target = set(range(k)) - {color}
            if not any(c[v] == color and target <= {c[w] for w in nbr[v]}
                       for v in range(n)):
                good = False
                break
        if good:
            best = k
    return best


def predicted(n, r):
    return min(n, 1 + isqrt(n + 2 * r - 1))


def make_witness(n, r):
    k = predicted(n, r)
    Rk = (k - 1) * (k - 2) // 2
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if r <= Rk:
        # Connected k-vertex core with k-1+r edges.
        core = nx.path_graph(k)
        for u in range(k):
            for v in range(u + 1, k):
                if core.number_of_edges() >= k - 1 + r:
                    break
                if not core.has_edge(u, v):
                    core.add_edge(u, v)
            if core.number_of_edges() >= k - 1 + r:
                break
        G.add_edges_from(core.edges())
        colors = {v: v for v in range(k)}
        nextv = k
        for v in range(k):
            missing = [j for j in range(k) if j != v and not core.has_edge(v, j)]
            for col in missing:
                G.add_edge(v, nextv)
                colors[nextv] = col
                nextv += 1
        # Remaining vertices are harmless extra leaves.
        while nextv < n:
            G.add_edge(0, nextv)
            colors[nextv] = 1 if k > 1 else 0
            nextv += 1
        # Verify the displayed coloring is a b-coloring with k colors.
        assert all(colors[u] != colors[v] for u, v in G.edges())
        for col in range(k):
            target = set(range(k)) - {col}
            assert any(colors[v] == col and target <= {colors[w] for w in G.neighbors(v)}
                       for v in G.nodes())
    else:
        # K_k plus tree attachments has cycle rank Rk; add arbitrary missing edges.
        for u in range(k):
            for v in range(u + 1, k):
                G.add_edge(u, v)
        for v in range(k, n):
            G.add_edge(0, v)
        need = r - Rk
        for u in range(n):
            for v in range(u + 1, n):
                if need == 0:
                    break
                if not G.has_edge(u, v):
                    G.add_edge(u, v)
                    need -= 1
            if need == 0:
                break
        assert need == 0
        # K_k is present, hence chi(G) >= k and therefore b(G) >= k.
        assert all(G.has_edge(u, v) for u in range(k) for v in range(u + 1, k))
    assert nx.is_connected(G)
    assert G.number_of_edges() - n + 1 == r
    return G

# Exhaustive unlabeled connected graphs through order 7 (NetworkX Graph Atlas).
maxima = defaultdict(int)
checked = 0
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if n < 1 or n > 7 or not nx.is_connected(G):
        continue
    r = G.number_of_edges() - n + 1
    b = b_number(G)
    assert b <= predicted(n, r)
    maxima[n, r] = max(maxima[n, r], b)
    checked += 1

pairs = 0
for n in range(1, 8):
    for r in range((n - 1) * (n - 2) // 2 + 1):
        pairs += 1
        assert maxima[n, r] == predicted(n, r)

# Directly verify a theorem witness for every feasible pair through order 30.
witness_pairs = 0
for n in range(2, 31):
    for r in range((n - 1) * (n - 2) // 2 + 1):
        make_witness(n, r)
        witness_pairs += 1

print(f"connected_atlas_graphs_checked={checked}")
print(f"atlas_parameter_pairs_checked={pairs}")
print(f"constructed_parameter_pairs_checked={witness_pairs}")
print("all_checks_passed=True")
