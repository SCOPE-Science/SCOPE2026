"""Finite numerical diagnostics for exact isotonic stability constants.
The theorem uses an analytic proof; this script is not an exhaustive certificate.
Only Python standard library is required.
"""
import math


def graph_gradient(n, edges, coefficients):
    g = [0.0] * n
    for (u, v), a in zip(edges, coefficients):
        assert a > 0.0
        g[u] += a
        g[v] -= a
    return g


def pooled_data_and_ratio(n, edges, coefficients, p):
    g = graph_gradient(n, edges, coefficients)
    assert max(abs(t) for t in g) > 0.0
    assert all(t != 0.0 for t in g)
    x = [math.copysign(abs(t) ** (1.0 / (p - 1.0)), t) for t in g]
    reconstructed = [math.copysign(abs(t) ** (p - 1.0), t) for t in x]
    assert max(abs(a - b) for a, b in zip(reconstructed, g)) < 1e-10
    assert abs(sum(reconstructed)) < 1e-10  # the p-mean is zero
    weights = [abs(t) ** (p - 2.0) for t in x]
    W = sum(weights)
    q = p / (p - 1.0)
    ratio = n ** (1.0 / p) * (sum((w / W) ** q for w in weights)) ** (1.0 / q)
    return ratio


def noncut_vertex(n, edges):
    for j in range(n):
        pool = {next(i for i in range(n) if i != j)}
        while True:
            old = len(pool)
            for u, v in edges:
                if u != j and v != j and (u in pool or v in pool):
                    pool.update([u, v])
            if len(pool) == old:
                break
        if len(pool) == n - 1:
            return j
    raise ValueError('no non-cut vertex in a connected graph')


def coefficients_below_2(n, edges, eps):
    j = noncut_vertex(n, edges)
    eligible = [i for i, (u, v) in enumerate(edges) if u != j and v != j]
    e0 = eligible[0]
    return [(1.0 if i == e0 else eps * (i + 1))
            if u != j and v != j else eps * eps * (i + 1)
            for i, (u, v) in enumerate(edges)]


def main():
    graphs = {
        'path3': (3, [(0, 1), (1, 2)]),
        'star4': (4, [(0, 1), (0, 2), (0, 3)]),
        'diamond4': (4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
        'path5': (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
    }
    for graph, (n, edges) in graphs.items():
        for p in (1.5, 3.0, 4.0):
            bounds = []
            for eps in (1e-2, 1e-4, 1e-6):
                if p < 2.0:
                    coefs = coefficients_below_2(n, edges, eps)
                    target = n ** (1.0 / p)
                else:
                    coefs = [1.0 if i == 0 else eps * (i + 1)
                             for i in range(len(edges))]
                    target = (n / 2.0) ** (1.0 / p)
                try:
                    ratio = pooled_data_and_ratio(n, edges, coefs, p)
                except AssertionError:
                    # For some bipartite graphs a symmetric choice cancels;
                    # nonzero perturbations are required for differentiability.
                    coefs = [a * (1.0 + 0.001 * (i + 1)) for i, a in enumerate(coefs)]
                    ratio = pooled_data_and_ratio(n, edges, coefs, p)
                bounds.append(ratio)
                assert ratio <= target + 1e-9, (graph, p, ratio, target)
            assert bounds[-1] >= bounds[0] - 1e-4, (graph, p, bounds)
            print(graph, 'p=', p, 'upper=', round(target, 8),
                  'local_at_eps_1e-6=', round(bounds[-1], 8))
    print('FINITE_DIAGNOSTICS_OK')


if __name__ == '__main__':
    main()
