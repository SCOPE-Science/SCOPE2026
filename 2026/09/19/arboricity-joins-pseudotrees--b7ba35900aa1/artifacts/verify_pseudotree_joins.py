"""Definition-level checks for the pseudotree-join density formulas.

Requires Python 3 and NetworkX 3.6.1.  The script uses NetworkX's graph atlas,
keeps all connected trees and unicyclic graphs on at most six vertices, forms
joins, and exhaustively maximizes e(S)/(|S|-1) over vertex subsets S.
"""
from fractions import Fraction
import networkx as nx


def is_pseudotree(G):
    return len(G) > 0 and nx.is_connected(G) and G.number_of_edges() in (len(G) - 1, len(G))


def graph_join(G, H):
    G = nx.convert_node_labels_to_integers(G, first_label=0)
    H = nx.convert_node_labels_to_integers(H, first_label=len(G))
    J = nx.Graph()
    J.add_nodes_from(G)
    J.add_nodes_from(H)
    J.add_edges_from(G.edges)
    J.add_edges_from(H.edges)
    for u in G:
        for v in H:
            J.add_edge(u, v)
    return J


def nash_williams_density(G):
    nodes = list(G)
    best = Fraction(0, 1)
    N = len(nodes)
    for mask in range(1, 1 << N):
        k = mask.bit_count()
        if k < 2:
            continue
        S = [nodes[i] for i in range(N) if (mask >> i) & 1]
        e = G.subgraph(S).number_of_edges()
        best = max(best, Fraction(e, k - 1))
    return best


atlas = [g.copy() for g in nx.graph_atlas_g() if 1 <= len(g) <= 6 and is_pseudotree(g)]
by_order = {n: sum(len(g) == n for g in atlas) for n in range(1, 7)}
print("pseudotrees", len(atlas), by_order)

pair_checks = 0
for i, G in enumerate(atlas):
    for H in atlas[i:]:
        if len(G) + len(H) > 11:
            continue
        m, n = len(G), len(H)
        eps_g = G.number_of_edges() - (m - 1)
        eps_h = H.number_of_edges() - (n - 1)
        J = graph_join(G, H)
        observed = nash_williams_density(J)
        predicted = Fraction(m * n + m + n - 2 + eps_g + eps_h, m + n - 1)
        assert observed == predicted, (m, n, eps_g, eps_h, observed, predicted)
        pair_checks += 1
print("pseudotree-pair checks", pair_checks)

independent_checks = 0
for G in atlas:
    m = len(G)
    eps_g = G.number_of_edges() - (m - 1)
    for n in range(1, 7):
        if m + n > 11:
            continue
        J = graph_join(G, nx.empty_graph(n))
        observed = nash_williams_density(J)
        predicted = Fraction(m * n + m - 1 + eps_g, m + n - 1)
        assert observed == predicted, (m, n, eps_g, observed, predicted)
        independent_checks += 1
print("pseudotree-independent checks", independent_checks)
print("PASS")
