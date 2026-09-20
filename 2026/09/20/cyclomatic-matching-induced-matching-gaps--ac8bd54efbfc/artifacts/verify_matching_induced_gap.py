#!/usr/bin/env python3
"""Exact finite checks for matching versus induced-matching bounds.

Requires NetworkX 3.x.  The script:
  * checks the cyclomatic lower bound on every connected Graph Atlas graph;
  * checks the sharp fixed-order tree bound on all nonisomorphic trees
    through order 14;
  * generates all nonisomorphic connected unicyclic graphs through order 11
    and checks the sharp fixed-order unicyclic bound.
"""

import itertools
import math
import warnings
import networkx as nx

warnings.filterwarnings("ignore", message="The hashes produced for graphs without node or edge attributes changed.*")


def matching_number(G):
    return len(nx.max_weight_matching(G, maxcardinality=True))


def conflict_graph(G):
    edges = list(G.edges())
    C = nx.Graph()
    C.add_nodes_from(range(len(edges)))
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                C.add_edge(i, j)
                continue
            if (G.has_edge(a, c) or G.has_edge(a, d)
                    or G.has_edge(b, c) or G.has_edge(b, d)):
                C.add_edge(i, j)
    return C


def induced_matching_number(G):
    if G.number_of_edges() == 0:
        return 0
    C = conflict_graph(G)
    return max(len(K) for K in nx.find_cliques(nx.complement(C)))


def cycle_rank(G):
    return G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G)


def unicyclic_graphs(n):
    """One representative of each connected unlabeled unicyclic graph."""
    buckets = {}
    reps = []
    for T in nx.nonisomorphic_trees(n):
        nodes = list(T.nodes())
        for u, v in itertools.combinations(nodes, 2):
            if T.has_edge(u, v):
                continue
            G = T.copy()
            G.add_edge(u, v)
            h = nx.weisfeiler_lehman_graph_hash(G)
            bucket = buckets.setdefault(h, [])
            if not any(nx.is_isomorphic(G, H) for H in bucket):
                bucket.append(G)
                reps.append(G)
    return reps


def main():
    atlas = [G for G in nx.graph_atlas_g()
             if G.number_of_nodes() > 0 and nx.is_connected(G)]
    for G in atlas:
        nu = matching_number(G)
        nus = induced_matching_number(G)
        c = cycle_rank(G)
        assert nus >= math.ceil((nu - c) / 2)
    print(f"connected Graph Atlas graphs checked: {len(atlas)}")

    print("trees: n count max_gap theorem_bound")
    for n in range(2, 15):
        count = 0
        max_gap = -1
        for T in nx.nonisomorphic_trees(n):
            count += 1
            nu = matching_number(T)
            nus = induced_matching_number(T)
            assert nus >= math.ceil(nu / 2)
            max_gap = max(max_gap, nu - nus)
        bound = n // 4
        assert max_gap == bound
        print(n, count, max_gap, bound)

    print("unicyclic: n count max_gap theorem_bound")
    for n in range(3, 12):
        graphs = unicyclic_graphs(n)
        max_gap = -1
        for G in graphs:
            nu = matching_number(G)
            nus = induced_matching_number(G)
            assert nus >= math.floor(nu / 2)
            max_gap = max(max_gap, nu - nus)
        bound = 0 if n == 3 else (n + 2) // 4
        assert max_gap == bound
        print(n, len(graphs), max_gap, bound)

    print("PASS")


if __name__ == "__main__":
    main()
