"""Numerical corroboration of spectral flip and critical decay in weighted phase networks.

Requires NumPy and SciPy. Analytic arguments, not numerical trials, establish
all-size theorems; this script checks concrete weighted bipartite examples.
"""
import numpy as np
from scipy.optimize import root


def graph_data(n, edges):
    B = np.zeros((len(edges), n), dtype=float)
    w = np.array([weight for _, _, weight in edges], dtype=float)
    for k, (i, j, _) in enumerate(edges):
        B[k, i], B[k, j] = 1.0, -1.0
    L = B.T @ np.diag(w) @ B
    vals, vecs = np.linalg.eigh(L)
    lam, v = float(vals[-1]), vecs[:, -1]
    S4 = float(np.dot(w, (B @ v) ** 4))
    return B, w, L, lam, v, S4


def verify_graph(name, n, edges, delta):
    B, w, L, lam, v, S4 = graph_data(n, edges)
    hcrit = 2.0 / lam
    h = hcrit + delta
    a = lam * np.sqrt(3.0 * delta / S4)

    def antipodal_equation(u):
        return 2.0 * u - h * B.T @ (w * np.sin(B @ u))

    solution = root(antipodal_equation, a * v, tol=1e-11)
    u = solution.x
    residual = np.linalg.norm(antipodal_equation(u))
    assert residual < 1e-8, (name, residual)
    assert 0.85 < np.linalg.norm(u) / a < 1.15, name
    assert abs(np.sum(u)) < 1e-9

    J = np.eye(n) - h * B.T @ np.diag(w * np.cos(B @ u)) @ B
    multipliers = np.linalg.eigvalsh(J)
    transverse = multipliers[np.abs(multipliers - 1) > 1e-8]
    assert len(transverse) == n - 1
    assert np.max(np.abs(transverse)) < 1, name
    assert abs(min(transverse) - (-1.0 + 2 * lam * delta)) < 0.01

    x = 0.15 * v
    for _ in range(30000):
        x = x - hcrit * B.T @ (w * np.sin(B @ x))
    observed = 30000 * float((v @ x) ** 2)
    predicted = 3.0 * lam / (2 * S4)
    assert abs(observed / predicted - 1) < 0.015, (name, observed, predicted)
    print(f"{name}: lambda={lam:.10f}, hcrit={hcrit:.10f}, "
          f"amplitude_ratio={np.linalg.norm(u)/a:.6f}, "
          f"max_transverse_multiplier={np.max(np.abs(transverse)):.8f}, "
          f"critical_decay_ratio={observed/predicted:.6f}")


def main():
    verify_graph("one edge", 2, [(0, 1, 1.0)], 0.001)
    verify_graph("unequal weighted path", 3, [(0, 1, 1.0), (1, 2, 2.0)], 0.0005)
    verify_graph("weighted three-leaf star", 4,
                 [(0, 1, 1.0), (0, 2, 0.7), (0, 3, 1.4)], 0.0002)
    verify_graph("unequal weighted tree", 5,
                 [(0, 2, 1.0), (0, 3, 1.5), (1, 2, 0.6), (1, 4, 2.2)], 0.0002)
    verify_graph("weighted K2,3", 5,
                 [(0, 2, 1.0), (0, 3, 0.7), (0, 4, 1.1),
                  (1, 2, 1.6), (1, 3, 0.9), (1, 4, 1.3)], 0.0001)
    K23 = [(i, j, 1.0) for i in range(2) for j in range(2, 5)]
    _, _, _, lam, _, S4 = graph_data(5, K23)
    assert abs(lam - 5) < 1e-12
    assert abs(S4 - 25 / 6) < 1e-12
    assert abs(3 * lam * lam / S4 - 18) < 1e-12
    assert abs(3 * lam / (2 * S4) - 9 / 5) < 1e-12
    verify_graph("unweighted K2,3", 5, K23, 0.0001)
    print("All finite checks passed; general validity rests on the analytical proof.")


if __name__ == "__main__":
    main()
