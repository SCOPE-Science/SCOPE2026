"""Independent constructive census of rooted orbit refinement in distance-hereditary graphs.
Run: python recursive_census.py. Requires NetworkX 3.x."""
import networkx as nx
from collections import defaultdict

def graph_key(G):
    return (tuple(sorted(d for _, d in G.degree())), nx.weisfeiler_lehman_graph_hash(G))

def unique_graphs(graphs):
    bins = defaultdict(list)
    for G in graphs:
        group = bins[graph_key(G)]
        if not any(nx.is_isomorphic(G, H) for H in group):
            group.append(G)
    return [G for group in bins.values() for G in group]

def extend(G):
    n = len(G)
    for u in G:
        for kind in ('pendant', 'true_twin', 'false_twin'):
            neighbors = set(G.neighbors(u))
            if kind in ('pendant', 'true_twin'):
                neighbors.add(u)
            if kind == 'pendant':
                neighbors = {u}
            H = G.copy()
            H.add_node(n)
            H.add_edges_from((n, v) for v in neighbors)
            if nx.is_connected(H):
                yield H

def refined(G, root):
    n = len(G)
    c = [int(u == root) for u in range(n)]
    while True:
        signatures = [(c[u], tuple(sorted(c[v] for v in G[u]))) for u in range(n)]
        catalog = {s: i for i, s in enumerate(sorted(set(signatures)))}
        nc = [catalog[x] for x in signatures]
        if all((c[u] == c[v]) == (nc[u] == nc[v]) for u in range(n) for v in range(n)):
            return nc
        c = nc

def rooted_orbits(G, root):
    H = G.copy()
    nx.set_node_attributes(H, {v: int(v == root) for v in G}, 'fixed')
    matcher = nx.algorithms.isomorphism.GraphMatcher(H, H,
                       node_match=nx.algorithms.isomorphism.categorical_node_match('fixed', 0))
    parent = list(range(len(G)))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for phi in matcher.isomorphisms_iter():
        for v in G:
            parent[find(v)] = find(phi[v])
    return [find(v) for v in G]

def failures(G):
    answer = []
    for root in G:
        col, orb = refined(G,root), rooted_orbits(G,root)
        if any((col[u] == col[v]) != (orb[u] == orb[v])
               for u in G for v in G):
            answer.append(root)
    return answer

def main():
    states = [nx.empty_graph(1)]
    for n in range(1, 9):
        bad = [(G, failures(G)) for G in states]
        bad = [(G, roots) for G, roots in bad if roots]
        print(f'n={n} graphs={len(states)} failing_unrooted_types={len(bad)} '
              f'failing_labelled_roots={sum(len(r) for G,r in bad)}', flush=True)
        if n == 8:
            for G, roots in bad:
                print('witness', 'root',roots, 'edges',sorted(tuple(sorted(e)) for e in G.edges()),flush=True)
            assert len(bad) == 2
            break
        states = unique_graphs(H for G in states for H in extend(G))
    assert len(states) == 1484
if __name__ == '__main__': main()
