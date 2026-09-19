import itertools
import json
import networkx as nx


def girth_at_least_five(G):
    if nx.is_tree(G):
        return True
    return nx.girth(G) >= 5


def is_connected_mutual_visibility(G, S):
    S = frozenset(S)
    if not S:
        return False
    if len(S) > 1 and not nx.is_connected(G.subgraph(S)):
        return False
    for u, v in itertools.combinations(S, 2):
        d = nx.shortest_path_length(G, u, v)
        H = G.copy()
        H.remove_nodes_from(S - {u, v})
        try:
            if nx.shortest_path_length(H, u, v) != d:
                return False
        except nx.NetworkXNoPath:
            return False
    return True


def factor_graphs():
    out = []
    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if 2 <= n <= 5 and nx.is_connected(G) and girth_at_least_five(G):
            out.append(nx.convert_node_labels_to_integers(G))
    return out


def verify_product(G, H):
    P = nx.cartesian_product(G, H)
    nodes = list(P.nodes())

    # Every factor-edge pair gives a three-vertex Cartesian corner.
    corner_count = 0
    for g, gp in G.edges():
        for h, hp in H.edges():
            for center in [(g, h), (gp, h), (g, hp), (gp, hp)]:
                cg, ch = center
                ng = gp if cg == g else g
                nh = hp if ch == h else h
                S = {(cg, ch), (ng, ch), (cg, nh)}
                assert is_connected_mutual_visibility(P, S)
                corner_count += 1
    assert corner_count == 4 * G.number_of_edges() * H.number_of_edges()

    connected_mv_triples = 0
    for S in itertools.combinations(nodes, 3):
        if is_connected_mutual_visibility(P, S):
            connected_mv_triples += 1
    expected = 4 * G.number_of_edges() * H.number_of_edges()
    assert connected_mv_triples == expected

    # Mutual visibility is hereditary under passing to subsets. Every connected
    # vertex set of order at least four contains a connected four-vertex subset,
    # so it is enough to exclude connected mutual-visibility sets of order four.
    for S in itertools.combinations(nodes, 4):
        assert not is_connected_mutual_visibility(P, S)

    return {
        "factor_orders": [G.number_of_nodes(), H.number_of_nodes()],
        "product_order": P.number_of_nodes(),
        "maximum_connected_mv_size": 3,
        "connected_mv_triples": connected_mv_triples,
        "expected_cartesian_corners": expected,
    }


def main():
    factors = factor_graphs()
    results = []
    for i, G in enumerate(factors):
        for H in factors[i:]:
            results.append(verify_product(G, H))

    summary = {
        "networkx_version": nx.__version__,
        "factor_types": len(factors),
        "factor_type_counts_by_order": {
            str(n): sum(G.number_of_nodes() == n for G in factors)
            for n in range(2, 6)
        },
        "unordered_product_pairs": len(results),
        "maximum_product_order": max(r["product_order"] for r in results),
        "all_products_have_mu_c_3": all(
            r["maximum_connected_mv_size"] == 3 for r in results
        ),
        "all_maximum_set_counts_match": all(
            r["connected_mv_triples"] == r["expected_cartesian_corners"]
            for r in results
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
