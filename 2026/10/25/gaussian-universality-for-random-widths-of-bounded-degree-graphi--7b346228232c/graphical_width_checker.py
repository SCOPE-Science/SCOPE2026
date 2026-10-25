"""Reproducible numerical diagnostics for Euclidean widths of graph zonotopes.

Requires numpy. The exact identities are checked by exhaustive small zonotope
vertex generation; Monte Carlo diagnostics are not a proof of asymptotic laws.
"""
import itertools
import math
import numpy as np

SEED = 20261020
MU = 2 / math.sqrt(math.pi)
V = 2 - 4 / math.pi
KAPPA = 1 / 3 + (2 * math.sqrt(3) - 4) / math.pi


def graph_width(g, edges):
    projected = g - np.mean(g, axis=-1, keepdims=True)
    norm = np.linalg.norm(projected, axis=-1)
    total = np.zeros(g.shape[:-1], dtype=float)
    for i, j in edges:
        total += np.abs(g[..., i] - g[..., j])
    return total / norm


def degree_invariants(n, edges):
    deg = np.zeros(n, dtype=int)
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    alpha = len(edges) / n
    tau = float(np.sum(deg * (deg - 1) // 2)) / n
    variance = alpha * V + 2 * tau * KAPPA - 2 * alpha ** 2 / math.pi
    return alpha, tau, variance


def exact_support_test():
    rng = np.random.default_rng(SEED)
    tested = 0
    graphs = [
        (4, [(0, 1), (1, 2), (2, 3)]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),
        (5, [(0, 1), (0, 2), (0, 3), (0, 4)]),
        (6, [(i, (i + 1) % 6) for i in range(6)]),
    ]
    for n, edges in graphs:
        directions = rng.standard_normal((40, n))
        directions -= directions.mean(axis=1, keepdims=True)
        directions /= np.linalg.norm(directions, axis=1, keepdims=True)
        gen = np.array([np.eye(n)[i] - np.eye(n)[j] for i, j in edges])
        for u in directions:
            vertices = np.array([
                (np.array(signs) @ gen) / 2
                for signs in itertools.product([-1, 1], repeat=len(edges))
            ])
            by_vertices = np.max(vertices @ u) - np.min(vertices @ u)
            by_generators = sum(abs(u[i] - u[j]) for i, j in edges)
            assert abs(by_vertices - by_generators) < 1e-12
            tested += 1
    return tested


def asymptotic_diagnostics():
    rng = np.random.default_rng(SEED + 1)
    n = 360
    graphs = {
        "path": [(i, i + 1) for i in range(n - 1)],
        "cycle": [(i, (i + 1) % n) for i in range(n)],
        "four_regular_circulant": [(i, (i + step) % n) for i in range(n) for step in (1, 2)],
    }
    output = []
    for name, edges in graphs.items():
        alpha, tau, theoretical = degree_invariants(n, edges)
        sample = []
        for _ in range(12):
            g = rng.standard_normal((1000, n))
            w = graph_width(g, edges)
            exact_mean = len(edges) * math.sqrt(2 / math.pi) * math.exp(
                math.lgamma((n - 1) / 2) - math.lgamma(n / 2)
            )
            sample.append(w - exact_mean)
        values = np.concatenate(sample)
        obs = float(np.var(values, ddof=1))
        empirical_mean = float(np.mean(values))
        # Monte Carlo check with generous but non-vacuous tolerance.
        assert abs(obs - theoretical) < 0.11, (name, obs, theoretical)
        assert abs(empirical_mean) < 0.07, (name, empirical_mean)
        output.append((name, alpha, tau, theoretical, obs, empirical_mean))
    return output


if __name__ == "__main__":
    print("exact support/width comparisons", exact_support_test())
    print("mu", MU, "v", V, "kappa", KAPPA)
    for row in asymptotic_diagnostics():
        print("graph, m/n, wedges/n, asymptotic_variance, empirical_variance, empirical_center:", row)
    print("All reproducibility checks passed. No infinite theorem inferred from sampling.")
