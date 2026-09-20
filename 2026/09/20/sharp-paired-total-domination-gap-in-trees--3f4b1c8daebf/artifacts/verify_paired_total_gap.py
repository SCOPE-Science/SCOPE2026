import itertools
from functools import lru_cache
import networkx as nx


def parameters(T):
    nodes = list(T.nodes())
    n = len(nodes)
    index = {v: i for i, v in enumerate(nodes)}
    adj = [0] * n
    for v in nodes:
        i = index[v]
        for u in T.neighbors(v):
            adj[i] |= 1 << index[u]
    full = (1 << n) - 1

    gamma_t = None
    for r in range(2, n + 1):
        for S in itertools.combinations(range(n), r):
            mask = sum(1 << i for i in S)
            if all(adj[i] & mask for i in range(n)):
                gamma_t = r
                break
        if gamma_t is not None:
            break

    @lru_cache(maxsize=None)
    def has_perfect_matching(mask):
        if mask == 0:
            return True
        if mask.bit_count() % 2:
            return False
        i = (mask & -mask).bit_length() - 1
        nbrs = adj[i] & mask & ~(1 << i)
        while nbrs:
            bit = nbrs & -nbrs
            j = bit.bit_length() - 1
            if has_perfect_matching(mask ^ (1 << i) ^ (1 << j)):
                return True
            nbrs ^= bit
        return False

    gamma_pr = None
    for r in range(2, n + 1, 2):
        for S in itertools.combinations(range(n), r):
            mask = sum(1 << i for i in S)
            dominated = mask
            for i in S:
                dominated |= adj[i]
            if dominated != full:
                continue
            if has_perfect_matching(mask):
                gamma_pr = r
                break
        if gamma_pr is not None:
            break

    return gamma_t, gamma_pr


def subdivided_star(r):
    G = nx.Graph()
    center = 0
    nxt = 1
    for _ in range(r):
        support, leaf = nxt, nxt + 1
        nxt += 2
        G.add_edge(center, support)
        G.add_edge(support, leaf)
    return G


def even_family_a(m):
    # K_{1,m-1} corona K_1.
    H = nx.star_graph(m - 1)
    G = H.copy()
    nxt = m
    for v in range(m):
        G.add_edge(v, nxt)
        nxt += 1
    return G


def even_family_b(m):
    # S(K_{1,m-1}) with one extra leaf at a support vertex.
    G = subdivided_star(m - 1)
    G.add_edge(1, max(G.nodes()) + 1)
    return G


def predicted(n):
    return max(0, (n - 3) // 2)


print(f"networkx={nx.__version__}")
for n in range(2, 13):
    best = -1
    extremals = []
    count = 0
    for T in nx.generators.nonisomorphic_trees(n):
        gt, gp = parameters(T)
        gap = gp - gt
        count += 1
        if gap > best:
            best = gap
            extremals = [T.copy()]
        elif gap == best:
            extremals.append(T.copy())

    assert best == predicted(n)
    if n == 2:
        assert len(extremals) == 1
    elif n == 3:
        assert len(extremals) == 1 and nx.is_isomorphic(extremals[0], nx.path_graph(3))
    elif n == 4:
        assert len(extremals) == 2
    elif n % 2 == 1:
        m = (n - 1) // 2
        assert len(extremals) == 1
        assert nx.is_isomorphic(extremals[0], subdivided_star(m))
    else:
        m = n // 2
        targets = [even_family_a(m), even_family_b(m)]
        assert len(extremals) == 2
        assert all(any(nx.is_isomorphic(T, F) for F in targets) for T in extremals)

    print(f"n={n:2d} trees={count:4d} max_gap={best} extremal_classes={len(extremals)}")

print("all checks passed")
