"""Numerical diagnostics for random-direction widths of symmetric edge polytopes.

Run: python geometry_gumbel_checker.py --output geometry_gumbel_checks.json
Only finite checks are performed; asymptotic theorems require the analytic proof.
"""
import argparse
import itertools
import json
import math
import numpy as np
from scipy.special import ndtri


def edges_for(kind, n):
    if kind == "path":
        return np.array([(i, i + 1) for i in range(n - 1)], dtype=np.int64)
    if kind == "cycle":
        return np.array([(i, (i + 1) % n) for i in range(n)], dtype=np.int64)
    if kind == "star":
        return np.array([(0, i) for i in range(1, n)], dtype=np.int64)
    if kind == "cubic":
        if n % 2 or n < 6:
            raise ValueError("Cubic graph requires an even n>=6")
        links = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
        links |= {(i, i + n // 2) for i in range(n // 2)}
        return np.array(sorted(links), dtype=np.int64)
    raise ValueError(kind)


def test_support():
    rng = np.random.default_rng(42019)
    comparisons = 0
    discrepancies = []
    for kind, n in [("path", 7), ("cycle", 8), ("star", 9), ("cubic", 8)]:
        ee = edges_for(kind, n)
        vertices = np.zeros((2 * len(ee), n))
        for j, (a, b) in enumerate(ee):
            vertices[2 * j, a] = 1.0
            vertices[2 * j, b] = -1.0
            vertices[2 * j + 1] = -vertices[2 * j]
        for _ in range(127):
            x = rng.normal(size=n)
            x -= x.mean()
            x /= np.linalg.norm(x)
            vals = vertices @ x
            direct = vals.max() - vals.min()
            formula = 2.0 * np.max(np.abs(x[ee[:, 0]] - x[ee[:, 1]]))
            discrepancies.append(float(abs(direct - formula)))
            comparisons += 1
    assert max(discrepancies) < 2e-12
    return {"comparison_count": comparisons, "max_error": max(discrepancies)}


def sample_maxima(kind, n, draws, seed):
    rng = np.random.default_rng(seed)
    ee = edges_for(kind, n)
    m = len(ee)
    b = ndtri(1.0 - 1.0 / (2.0 * m)) if kind != "star" else ndtri(1.0 - 1.0 / m)
    ts = []
    winning = np.zeros(m, dtype=np.int64)
    for off in range(0, draws, 120):
        sz = min(120, draws - off)
        x = rng.normal(size=(sz, n))
        centered = x - x.mean(axis=1, keepdims=True)
        norms = np.linalg.norm(centered, axis=1)
        diffs = np.abs(x[:, ee[:, 0]] - x[:, ee[:, 1]])
        maxval = diffs.max(axis=1)
        if kind == "star":
            ts.extend((np.sqrt(n - 1) * maxval / norms - b).tolist())
        else:
            ts.extend((b * (np.sqrt(n - 1) * maxval / (np.sqrt(2) * norms) - b)).tolist())
        winning += np.bincount(diffs.argmax(axis=1), minlength=m)
    vals = np.asarray(ts)
    return {
        "graph": kind, "vertices": n, "edges": m, "draws": draws,
        "normalized_mean": float(vals.mean()),
        "empirical_F_at_0": float(np.mean(vals <= 0.0)),
        "predicted_F_at_0": 0.0 if kind == "star" else float(math.exp(-1.0)),
        "win_probability_min": float(winning.min() / draws),
        "win_probability_max": float(winning.max() / draws),
        "predicted_each_edge_win_probability": float(1.0 / m),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='geometry_gumbel_checks.json')
    args = parser.parse_args()
    records = {"support_function": test_support(),
               "finite_distribution_diagnostics": [
                   sample_maxima('path', 1400, 2800, 414),
                   sample_maxima('cycle', 1400, 2800, 415),
                   sample_maxima('cubic', 1400, 2800, 416),
                   sample_maxima('star', 1400, 2800, 417),
                   sample_maxima('path', 72, 130000, 418)],
               "limits": "Finite checks only; no numerical result is used to certify an infinite-dimensional limit."}
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
