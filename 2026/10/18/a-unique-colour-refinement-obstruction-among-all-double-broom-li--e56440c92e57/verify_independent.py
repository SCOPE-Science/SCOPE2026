"""Small-parameter independent check using exact rooted graph isomorphism.

Requires networkx; unlike verify_structure.py, orbit classes are computed from
actual graph automorphisms rather than a proposed formula.
"""
from collections import defaultdict, Counter
import networkx as nx


def make_line_graph(a, b, ell):
    tree = nx.path_graph(ell + 1)
    for j in range(a):
        tree.add_edge(0, ell + 1 + j)
    for j in range(b):
        tree.add_edge(ell, ell + 1 + a + j)
    return nx.convert_node_labels_to_integers(nx.line_graph(tree))


def stable_colors(G):
    colors = {v: 0 for v in G}
    while True:
        sig = {v: (colors[v], tuple(sorted(colors[u] for u in G[v]))) for v in G}
        numbered = {z: i for i, z in enumerate(sorted(set(sig.values())))}
        new = {v: numbered[sig[v]] for v in G}
        if new == colors:
            return colors
        colors = new


def automorphic(G, u, v):
    G1 = G.copy()
    G2 = G.copy()
    nx.set_node_attributes(G1, {x: int(x == u) for x in G}, 'fixed')
    nx.set_node_attributes(G2, {x: int(x == v) for x in G}, 'fixed')
    return nx.is_isomorphic(G1, G2, node_match=nx.algorithms.isomorphism.categorical_node_match('fixed', 0))


def main():
    checked = 0
    failure_cases = []
    for a in range(2, 5):
        for b in range(a, 6):
            for ell in range(1, 8):
                G = make_line_graph(a, b, ell)
                colors = stable_colors(G)
                classes = defaultdict(list)
                for v, c in colors.items():
                    classes[c].append(v)
                nonorbit = False
                for cls in classes.values():
                    for ix, u in enumerate(cls):
                        for v in cls[:ix]:
                            if not automorphic(G, u, v):
                                nonorbit = True
                                break
                        if nonorbit:
                            break
                    if nonorbit:
                        break
                if nonorbit:
                    failure_cases.append((a, b, ell, sorted(Counter(colors.values()).values())))
                checked += 1
    assert failure_cases == [(2, 2, 4, [2, 6])], failure_cases
    special = make_line_graph(2, 2, 4)
    remaining = set(special)
    orbit_sizes = []
    while remaining:
        root = min(remaining)
        orbit = {v for v in remaining if automorphic(special, root, v)}
        orbit_sizes.append(len(orbit))
        remaining -= orbit
    assert sorted(orbit_sizes) == [2, 2, 4], orbit_sizes
    print('independently checked rooted-isomorphism instances:', checked)
    print('non-orbit-exact instances:', failure_cases)
    print('exceptional automorphism orbit sizes:', sorted(orbit_sizes))
    print('PASS')


if __name__ == '__main__':
    main()
