"""Finite sanity check for the one-step empty-join theorem.

Requires NetworkX 3.6.1.  The symbolic proof in RESULT.md is the primary proof.
"""
import networkx as nx


def edge_imbalances(G):
    deg = dict(G.degree())
    return [abs(deg[u] - deg[v]) for u, v in G.edges()]


def join_with_empty(G, m):
    old = {v: ("g", v) for v in G.nodes()}
    H = nx.relabel_nodes(G, old, copy=True)
    for j in range(m):
        a = ("a", j)
        H.add_node(a)
        for v in old.values():
            H.add_edge(a, v)
    return H


def boundary_m(G):
    n = G.number_of_nodes()
    delta = min(dict(G.degree()).values())
    return n - max(1, delta) - 1


def check_order(n):
    graphs = [G for G in nx.graph_atlas_g() if G.number_of_nodes() == n]
    failures = []
    min_slack = None
    for G in graphs:
        m = boundary_m(G)
        H = join_with_empty(G, m)
        positive = [x for x in edge_imbalances(H) if x > 0]
        if positive:
            D = max(positive)
            S = sum(positive)
            slack = S - D * (D + 1)
            min_slack = slack if min_slack is None else min(min_slack, slack)
        if not nx.is_graphical(positive, method="eg"):
            failures.append(
                {
                    "graph6": nx.to_graph6_bytes(G, header=False).decode().strip(),
                    "degrees": sorted(dict(G.degree()).values()),
                    "m": m,
                    "positive_imbalances": sorted(positive, reverse=True),
                }
            )
    return len(graphs), failures, min_slack


def main():
    expected_counts = {4: 11, 5: 34, 6: 156, 7: 1044}
    results = {}
    for n in range(4, 8):
        count, failures, min_slack = check_order(n)
        assert count == expected_counts[n]
        results[n] = (count, failures, min_slack)

    # The theorem range.
    for n in (5, 6, 7):
        assert results[n][1] == []
        assert results[n][2] >= 0

    # The known order-four obstruction is unique in the atlas.
    failures4 = results[4][1]
    assert len(failures4) == 1
    assert failures4[0]["degrees"] == [0, 2, 2, 2]
    assert failures4[0]["m"] == 2
    assert failures4[0]["positive_imbalances"] == [2, 2]

    for n in range(4, 8):
        count, failures, min_slack = results[n]
        print(
            f"n={n}: graphs={count}, failures={len(failures)}, "
            f"min_nonzero_slack={min_slack}"
        )
        for failure in failures:
            print("  failure:", failure)


if __name__ == "__main__":
    main()
