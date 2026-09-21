import itertools
import numpy as np
import networkx as nx
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix


def locating_domination_number(G):
    vertices = list(G)
    for r in range(len(vertices) + 1):
        for choice in itertools.combinations(vertices, r):
            D = set(choice)
            seen = set()
            ok = True
            for v in vertices:
                if v in D:
                    continue
                signature = frozenset(set(G[v]) & D)
                if not signature or signature in seen:
                    ok = False
                    break
                seen.add(signature)
            if ok:
                return r
    raise AssertionError("unreachable")


def rooted_cycle_product(H, m):
    G = nx.Graph()
    for v in H:
        root = ("r", v)
        cycle = [root] + [("c", v, i) for i in range(1, m)]
        G.add_edges_from((cycle[i], cycle[(i + 1) % m]) for i in range(m))
    for u, v in H.edges():
        G.add_edge(("r", u), ("r", v))
    return G


def locating_total_number(G):
    vertices = list(G)
    pos = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    neighborhoods = {v: set(G[v]) for v in vertices}
    rows = []
    lower = []

    # Total domination.
    for v in vertices:
        row = np.zeros(n)
        for w in neighborhoods[v]:
            row[pos[w]] = 1
        rows.append(row)
        lower.append(1)

    # If u and v are both outside S, some vertex in N(u) symmetric-difference N(v)
    # must be selected.
    for i, u in enumerate(vertices):
        for j in range(i + 1, n):
            v = vertices[j]
            row = np.zeros(n)
            row[i] = 1
            row[j] = 1
            for w in neighborhoods[u] ^ neighborhoods[v]:
                row[pos[w]] += 1
            rows.append(row)
            lower.append(1)

    A = csr_matrix(np.vstack(rows))
    constraints = LinearConstraint(A, np.array(lower), np.full(len(lower), np.inf))
    result = milp(
        c=np.ones(n),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=constraints,
    )
    if not result.success:
        raise RuntimeError(result.message)
    return int(round(result.fun))


def main():
    atlas = nx.graph_atlas_g()
    bases = [
        G.copy()
        for G in atlas
        if 1 <= G.number_of_nodes() <= 5
        and (G.number_of_nodes() == 1 or nx.is_connected(G))
    ]

    checked = 0
    for H in bases:
        ld = locating_domination_number(H)
        for m in (5, 9):
            k = (m - 1) // 4
            product = rooted_cycle_product(H, m)
            exact = locating_total_number(product)
            predicted = 2 * k * H.number_of_nodes() + ld
            assert exact == predicted, (H.number_of_nodes(), H.number_of_edges(), m, exact, predicted)
            checked += 1

    H = nx.path_graph(10)
    exact = locating_total_number(rooted_cycle_product(H, 5))
    assert locating_domination_number(H) == 4
    assert exact == 24

    print(f"checked rooted products: {checked}")
    print("P10 rooted with C5: 24")
    print("all checks passed")


if __name__ == "__main__":
    main()
