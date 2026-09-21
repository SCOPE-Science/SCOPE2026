"""Finite verification for the identifying-open-code skeleton lift.

Requires Python 3, NetworkX, NumPy, and SciPy.  For every connected Graph Atlas
skeleton on 2--5 vertices and Delta in {3,4,5} with Delta(H)<=Delta, the script
constructs the lifted graph, checks its structural properties and the explicit
code, and independently solves the minimum identifying-open-code 0-1 formulation.
"""
import itertools
import math
import networkx as nx
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def lift(H, Delta):
    if len(H) < 2 or not nx.is_connected(H) or max(dict(H.degree()).values()) > Delta:
        raise ValueError("invalid skeleton")
    G = nx.Graph()
    centers = {v: ("c", v) for v in H}
    G.add_nodes_from(centers.values())
    for eid, (u, v) in enumerate(H.edges()):
        xu, xv = ("x", eid, u), ("x", eid, v)
        G.add_edges_from([(centers[u], xu), (xu, xv), (xv, centers[v])])
    for v in H:
        for j in range(Delta - H.degree(v)):
            s, l = ("s", v, j), ("l", v, j)
            G.add_edges_from([(centers[v], s), (s, l)])
    return G, set(centers.values())


def is_ioc(G, S):
    S = set(S)
    signatures = []
    for v in G:
        sig = frozenset(set(G.neighbors(v)) & S)
        if not sig:
            return False
        signatures.append(sig)
    return len(signatures) == len(set(signatures))


def gamma_ioc(G):
    V = list(G)
    pos = {v: i for i, v in enumerate(V)}
    N = {v: set(G.neighbors(v)) for v in V}
    rows = []
    for v in V:
        rows.append([pos[w] for w in N[v]])
    for i, u in enumerate(V):
        for v in V[i + 1:]:
            diff = N[u] ^ N[v]
            if not diff:
                return math.inf
            rows.append([pos[w] for w in diff])
    rr, cc, data = [], [], []
    for i, row in enumerate(rows):
        for j in row:
            rr.append(i)
            cc.append(j)
            data.append(1.0)
    A = coo_matrix((data, (rr, cc)), shape=(len(rows), len(V))).tocsr()
    constraints = LinearConstraint(A, np.ones(len(rows)), np.full(len(rows), np.inf))
    result = milp(
        c=np.ones(len(V)),
        integrality=np.ones(len(V)),
        bounds=Bounds(0, 1),
        constraints=constraints,
    )
    if not result.success:
        raise AssertionError(result.message)
    return int(round(result.fun))


def has_4cycle(G):
    V = list(G)
    for a, b, c, d in itertools.combinations(V, 4):
        for cyc in ((a, b, c, d), (a, c, b, d), (a, b, d, c)):
            if all(G.has_edge(cyc[i], cyc[(i + 1) % 4]) for i in range(4)):
                return True
    return False


def open_twin_free(G):
    neighborhoods = [frozenset(G.neighbors(v)) for v in G]
    return len(neighborhoods) == len(set(neighborhoods))


def main():
    checked = 0
    for H in nx.graph_atlas_g():
        p = len(H)
        if p < 2 or p > 5 or not nx.is_connected(H):
            continue
        for Delta in (3, 4, 5):
            if max(dict(H.degree()).values()) > Delta:
                continue
            G, centers = lift(H, Delta)
            m = H.number_of_edges()
            n_expected = (2 * Delta + 1) * p - 2 * m
            gamma_expected = n_expected - p
            assert len(G) == n_expected
            assert max(dict(G.degree()).values()) == Delta
            assert open_twin_free(G)
            assert not has_4cycle(G)
            assert is_ioc(G, set(G) - centers)
            assert gamma_ioc(G) == gamma_expected
            checked += 1
    print(f"verified_instances={checked}")
    print("all_formula_property_checks=PASS")


if __name__ == "__main__":
    main()
