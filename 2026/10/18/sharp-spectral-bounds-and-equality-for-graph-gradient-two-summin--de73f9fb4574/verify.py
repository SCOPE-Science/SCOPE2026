"""Numerical cross-checks for graph-gradient 2-summing spectral bounds.

Run: python3 verify.py   (requires NumPy)
The analytic proof, not these floating-point checks, establishes the theorem.
"""
from itertools import combinations
from math import comb, pi, sqrt
import numpy as np


def analyze(n, edges):
    E = np.asarray(edges, dtype=int)
    if len(E) == 0:
        raise ValueError("Graph has no edges")
    B = np.zeros((n, len(E)))
    for j, (u, v) in enumerate(E):
        B[u, j] = 1.0
        B[v, j] = -1.0
    L = B @ B.T
    eig, U = np.linalg.eigh(L)
    positive = eig > 1.e-8
    assert positive.sum() == n - 1, "Graph must be connected"
    s = np.zeros(n)
    s[positive] = eig[positive] ** (-0.5)
    inv_sqrt = (U * s) @ U.T
    X = inv_sqrt @ B
    P = np.eye(n) - np.ones((n, n)) / n
    assert np.linalg.norm(X @ X.T - P, ord='fro') < 3e-8
    r = np.sum(B * X, axis=0)
    tr_sqrt = float(np.sqrt(eig[positive]).sum())
    assert abs(r.sum() - tr_sqrt) < 3e-8
    m = len(E)
    lower = float(np.linalg.norm(r))
    baseline = tr_sqrt / sqrt(m)
    upper = sqrt(tr_sqrt * r.max())
    assert lower + 1e-8 >= baseline and upper + 1e-8 >= lower
    return baseline, lower, upper, r, L, X, B


def check_uniform(n, edges, expected=None):
    baseline, lower, upper, rho, L, X, B = analyze(n, edges)
    assert rho.max() - rho.min() < 1e-8
    assert abs(baseline - lower) < 1e-8
    assert abs(baseline - upper) < 1e-8
    actual_outputs = np.max(np.abs(B.T @ X), axis=0)
    assert np.max(np.abs(actual_outputs - rho)) < 2e-8
    if expected is not None:
        assert abs(baseline - expected) < 2e-8, (baseline, expected)
    return 1


def cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def complete(n):
    return list(combinations(range(n), 2))


def complete_bipartite(a, b):
    return [(i, a + j) for i in range(a) for j in range(b)]


def hypercube(d):
    return [(u, u ^ (1 << k)) for u in range(1 << d) for k in range(d) if not u & (1 << k)]


def chang_graph():
    vertices = list(combinations(range(8), 2))
    switched = {(0, 1), (2, 3), (4, 5), (6, 7)}
    is_inside = [pair in switched for pair in vertices]
    edges = []
    adjacency = np.zeros((28, 28), dtype=np.int8)
    for i, j in combinations(range(28), 2):
        adjacent = bool(set(vertices[i]) & set(vertices[j]))
        if is_inside[i] != is_inside[j]:
            adjacent = not adjacent
        if adjacent:
            edges.append((i, j))
            adjacency[i, j] = adjacency[j, i] = 1
    assert len(edges) == 168
    assert np.array_equal(adjacency.sum(axis=1), np.full(28, 12))
    AA = adjacency @ adjacency
    for i, j in combinations(range(28), 2):
        assert AA[i, j] == (6 if adjacency[i, j] else 4)
    return edges


def main():
    total = 0
    for n in range(3, 23):
        # sum_{k=1}^{n-1} 2 sin(pi*k/n) = 2 cot(pi/(2*n))
        expected = 2.0 / np.tan(pi / (2*n)) / sqrt(n)
        total += check_uniform(n, cycle(n), expected)
    for n in range(2, 13):
        total += check_uniform(n, complete(n), sqrt(2 * (n - 1)))
    for a in range(1, 8):
        for b in range(1, 8):
            expected = (a - 1)/sqrt(a) + (b - 1)/sqrt(b) + sqrt(1/a + 1/b)
            total += check_uniform(a + b, complete_bipartite(a,b), expected)
    for d in range(1, 7):
        expected = sum(comb(d,k) * sqrt(2*k) for k in range(1,d+1))/sqrt(d*2**(d-1))
        total += check_uniform(2**d, hypercube(d), expected)
    # Chang strongly regular graph has 28 vertices, degree 12, eigenvalues
    # 12 (one), 4 (seven), -2 (twenty), and is not edge-transitive.
    expected = (7*sqrt(8) + 20*sqrt(14)) / sqrt(168)
    total += check_uniform(28, chang_graph(), expected)
    # A nonuniform connected graph has a strict gap above spectral baseline.
    b, lo, up, rho, *_ = analyze(4, [(0,1),(1,2),(2,3)])
    assert rho.max()-rho.min() > 0.01 and lo > b + 1e-4
    print(f"PASS: {total} uniform-edge spectral identities; "
          "one strict nonuniform boundary; frame and dual bounds checked")

if __name__ == '__main__':
    main()
