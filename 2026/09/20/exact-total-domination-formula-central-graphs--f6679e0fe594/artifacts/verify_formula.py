"""Finite verification of the central-graph total-domination formula.

Requires NetworkX and SciPy.  For each connected graph in the NetworkX Graph
Atlas having at least two vertices, the script compares:

  (1) the vertex-cover/partial-edge-cover formula from RESULT.md; and
  (2) a direct binary MILP for total domination in the central graph.

The theorem itself is proved symbolically in RESULT.md; this computation is only
an independent finite sanity check.
"""

import networkx as nx
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def central_graph(G):
    C = nx.Graph()
    vertices = list(G.nodes())
    C.add_nodes_from(("v", v) for v in vertices)
    for i, u in enumerate(vertices):
        for v in vertices[i + 1 :]:
            if not G.has_edge(u, v):
                C.add_edge(("v", u), ("v", v))
    for j, (u, v) in enumerate(G.edges()):
        c = ("e", j)
        C.add_edge(c, ("v", u))
        C.add_edge(c, ("v", v))
    return C


def exact_total_domination_milp(H):
    vertices = list(H.nodes())
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    adjacency = np.zeros((n, n), dtype=float)
    for i, v in enumerate(vertices):
        for w in H.neighbors(v):
            adjacency[i, index[w]] = 1.0
    constraints = LinearConstraint(
        adjacency, np.ones(n), np.full(n, np.inf)
    )
    result = milp(
        np.ones(n),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=constraints,
        options={"time_limit": 30.0},
    )
    if not result.success:
        raise ValueError(result.message)
    return int(round(result.fun))


def formula_value(G):
    vertices = list(G.nodes())
    n = len(vertices)
    best = n + G.number_of_edges() + 1
    for mask in range(1 << n):
        A = {vertices[i] for i in range(n) if (mask >> i) & 1}
        if any(u not in A and v not in A for u, v in G.edges()):
            continue
        R = {
            v
            for v in vertices
            if A.issubset(set(G.neighbors(v)) | {v})
        }
        matching = nx.max_weight_matching(G.subgraph(R), maxcardinality=True)
        candidate = len(A) + len(R) - len(matching)
        best = min(best, candidate)
    return best


def main():
    checked = 0
    by_order = {}
    for G in nx.graph_atlas_g():
        if len(G) < 2 or not nx.is_connected(G):
            continue
        if min(dict(G.degree()).values()) == 0:
            continue
        predicted = formula_value(G)
        direct = exact_total_domination_milp(central_graph(G))
        if predicted != direct:
            raise AssertionError(
                f"mismatch n={len(G)} m={G.number_of_edges()}: "
                f"formula={predicted}, direct={direct}"
            )
        checked += 1
        by_order[len(G)] = by_order.get(len(G), 0) + 1

    print("orders:", " ".join(f"{n}:{by_order[n]}" for n in sorted(by_order)))
    print("checked:", checked)
    print("status: all formula values agree with direct total-domination MILPs")


if __name__ == "__main__":
    main()
