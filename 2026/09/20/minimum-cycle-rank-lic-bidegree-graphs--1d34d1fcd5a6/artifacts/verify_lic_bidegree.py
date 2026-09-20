import networkx as nx


def is_lic(G):
    deg = dict(G.degree())
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    H.add_edges_from((u, v) for u, v in G.edges() if deg[u] != deg[v])
    return len(H) > 0 and nx.is_connected(H)


def min_size_formula(a, b):
    if a % 2 == 1 or b % 2 == 0:
        return b * (a + 1) // 2
    return (a * b + 2 * b - a) // 2


def min_cycle_rank_formula(a, b):
    if a % 2 == 1 or b % 2 == 0:
        return b * (a - 1) // 2
    return a * (b - 1) // 2


def regular_graph(n, r):
    """Deterministic r-regular simple graph on n labeled vertices when nr is even."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if r == 0:
        return G
    half = r // 2
    for v in range(n):
        for d in range(1, half + 1):
            G.add_edge(v, (v + d) % n)
    if r % 2 == 1:
        assert n % 2 == 0
        for v in range(n // 2):
            G.add_edge(v, v + n // 2)
    assert all(d == r for _, d in G.degree())
    return G


def extremal_graph(a, b):
    if a % 2 == 1 or b % 2 == 0:
        H = regular_graph(b, a - 1)
        G = nx.Graph()
        G.add_nodes_from(range(b + 1))
        G.add_edges_from((0, v + 1) for v in H.nodes())
        G.add_edges_from((u + 1, v + 1) for u, v in H.edges())
    else:
        H = regular_graph(b - 1, a - 2)
        G = nx.Graph()
        G.add_nodes_from(range(b + 1))
        G.add_edge(0, 1)
        for h in (0, 1):
            G.add_edges_from((h, v + 2) for v in H.nodes())
        G.add_edges_from((u + 2, v + 2) for u, v in H.edges())
    return G


def matches_cycle_extremal_structure(G):
    deg = dict(G.degree())
    vals = sorted(set(deg.values()))
    if len(vals) != 2 or vals[0] < 1:
        return False
    a, b = vals
    X = [v for v in G if deg[v] == b]
    Y = [v for v in G if deg[v] == a]

    if a == 1:
        return len(X) == 1 and len(Y) == b

    normal = (a % 2 == 1 or b % 2 == 0)
    if normal:
        if len(X) != 1 or len(Y) != b:
            return False
        x = X[0]
        if any(not G.has_edge(x, y) for y in Y):
            return False
        return all(G.subgraph(Y).degree(y) == a - 1 for y in Y)

    if a >= 4:
        if len(X) != 2 or len(Y) != b - 1 or not G.has_edge(*X):
            return False
        if any(not G.has_edge(x, y) for x in X for y in Y):
            return False
        return all(G.subgraph(Y).degree(y) == a - 2 for y in Y)

    # Exceptional case a=2, b odd.  Minimum cycle rank is equivalent to
    # exactly two b-vertices.  The low vertices split into common neighbors
    # and private neighbors; common neighbors have no low-low edge and the
    # private vertices form a perfect matching.
    if len(X) != 2:
        return False
    u, v = X
    common = [y for y in Y if G.has_edge(u, y) and G.has_edge(v, y)]
    if not common:
        return False
    private = [y for y in Y if y not in common]
    if any(G.subgraph(Y).degree(y) != 0 for y in common):
        return False
    if any(sum(G.has_edge(x, y) for x in X) != 1 for y in private):
        return False
    return all(G.subgraph(Y).degree(y) == 1 for y in private)


# Exhaustive check on every graph in the NetworkX Graph Atlas.
atlas_min_size = {}
atlas_min_cycle = {}
atlas_graph_count = 0
for G in nx.graph_atlas_g():
    if G.number_of_nodes() < 2:
        continue
    degrees = sorted(set(dict(G.degree()).values()))
    if len(degrees) != 2 or degrees[0] < 1 or not is_lic(G):
        continue
    a, b = degrees
    atlas_graph_count += 1
    q = G.number_of_edges()
    c = q - G.number_of_nodes() + 1
    atlas_min_size[(a, b)] = min(atlas_min_size.get((a, b), q), q)
    atlas_min_cycle[(a, b)] = min(atlas_min_cycle.get((a, b), c), c)

for (a, b), q in atlas_min_size.items():
    assert q == min_size_formula(a, b), (a, b, q, min_size_formula(a, b))
    assert atlas_min_cycle[(a, b)] == min_cycle_rank_formula(a, b)

for G in nx.graph_atlas_g():
    if G.number_of_nodes() < 2:
        continue
    degrees = sorted(set(dict(G.degree()).values()))
    if len(degrees) != 2 or degrees[0] < 1 or not is_lic(G):
        continue
    a, b = degrees
    c = G.number_of_edges() - G.number_of_nodes() + 1
    if c == min_cycle_rank_formula(a, b):
        assert matches_cycle_extremal_structure(G), (a, b, G.number_of_nodes())

# Construct and check the claimed extremal family over a broad parameter range.
constructed = 0
for a in range(1, 41):
    for b in range(a + 1, 61):
        G = extremal_graph(a, b)
        assert G.number_of_nodes() == b + 1
        assert sorted(set(dict(G.degree()).values())) == [a, b]
        assert is_lic(G)
        assert G.number_of_edges() == min_size_formula(a, b)
        assert G.number_of_edges() - G.number_of_nodes() + 1 == min_cycle_rank_formula(a, b)
        constructed += 1

print(f"atlas LIC bidegree graphs checked: {atlas_graph_count}")
print(f"atlas degree pairs checked: {len(atlas_min_size)}")
print(f"constructed parameter pairs checked: {constructed}")
print("all checks passed")
