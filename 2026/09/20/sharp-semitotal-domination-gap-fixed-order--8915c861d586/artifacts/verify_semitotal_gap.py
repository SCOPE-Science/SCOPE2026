#!/usr/bin/env python3
"""Finite checks for the sharp semitotal-domination gap theorem."""
import itertools
import networkx as nx


def parameters(G):
    V = list(G.nodes())
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}
    full = (1 << n) - 1
    closed = []
    witness = []
    for v in V:
        cm = 1 << idx[v]
        for u in G.neighbors(v):
            cm |= 1 << idx[u]
        closed.append(cm)
        wm = 0
        for u, dist in nx.single_source_shortest_path_length(G, v, cutoff=2).items():
            if u != v:
                wm |= 1 << idx[u]
        witness.append(wm)

    gamma = None
    gamma_t2 = None
    for k in range(1, n + 1):
        for C in itertools.combinations(range(n), k):
            sm = sum(1 << i for i in C)
            dominated = 0
            for i in C:
                dominated |= closed[i]
            if dominated != full:
                continue
            if gamma is None:
                gamma = k
            if k >= 2 and all(witness[i] & (sm ^ (1 << i)) for i in C):
                gamma_t2 = k
                return gamma, gamma_t2
    raise AssertionError("connected nontrivial graph must have a semitotal dominating set")


def extremal_tree(n):
    d = (n - 2) // 4
    s = n - (4 * d + 2)
    G = nx.Graph()
    G.add_node("x")
    for i in range(d):
        a, b, c, z = (f"a{i}", f"b{i}", f"c{i}", f"d{i}")
        G.add_edges_from([("x", a), (a, b), (b, c), (c, z)])
    for j in range(s + 1):
        G.add_edge("x", f"l{j}")
    return G


atlas = [G for G in nx.graph_atlas_g() if len(G) >= 2 and nx.is_connected(G)]
print("connected graph atlas")
for n in range(2, 8):
    vals = [parameters(G)[1] - parameters(G)[0] for G in atlas if len(G) == n]
    target = max(1, (n - 2) // 4)
    assert max(vals) == target
    print(n, max(vals), sum(v == target for v in vals), "formula", target)

print("nonisomorphic trees")
for n in range(2, 11):
    vals = []
    for T in nx.generators.nonisomorphic_trees(n):
        g, st = parameters(T)
        vals.append(st - g)
    target = max(1, (n - 2) // 4)
    assert max(vals) == target
    print(n, max(vals), sum(v == target for v in vals), "formula", target)

print("explicit extremal family")
for n in range(6, 21):
    G = extremal_tree(n)
    g, st = parameters(G)
    d = (n - 2) // 4
    assert g == d + 1
    assert st == 2 * d + 1
    assert st - g == d
print("n=6..20: OK")
