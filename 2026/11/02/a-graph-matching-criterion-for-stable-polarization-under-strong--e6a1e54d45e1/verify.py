"""Standalone reproducibility checks for the homophily network sign-criterion theorem.

Python 3.10+; standard library only. The analytic proof, not enumeration,
justifies the all-graph and all-parameter statements.
"""
import itertools
import math


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n, adj


def compatible(adj, signs):
    return all(any(signs[j] == signs[i] for j in adj[i])
               for i in range(len(adj)))


def two_disjoint_edges(edges):
    return any(len({*p, *q}) == 4
               for p, q in itertools.combinations(edges, 2))


def finite_graph_check(max_order=6):
    checked = [0] * (max_order + 1)
    polarized = [0] * (max_order + 1)
    for n in range(2, max_order + 1):
        pairs = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [e for k, e in enumerate(pairs) if mask & (1 << k)]
            is_connected, adj = connected(n, edges)
            if not is_connected:
                continue
            checked[n] += 1
            allowed = any(compatible(adj, s)
                          for s in itertools.product((-1, 1), repeat=n)
                          if len(set(s)) == 2)
            expected = two_disjoint_edges(edges)
            assert allowed == expected, (n, edges)
            polarized[n] += int(allowed)
    return [(n, checked[n], polarized[n]) for n in range(2, max_order + 1)]


def weighted_map(x, adj, kappa, eps, beta):
    out = []
    for i, ne in enumerate(adj):
        w = [(eps + abs(x[i] - x[j])) ** (-beta) for j in ne]
        z = sum(w)
        out.append(kappa * sum(wj * math.tanh(x[j])
                               for wj, j in zip(w, ne)) / z)
    return tuple(out)


def four_path_example():
    kappa, eps, beta = 2.0, 1/250, 4
    adj = [[1], [0, 2], [1, 3], [2]]
    lo, hi = 1.9, 2.0
    assert kappa * math.tanh(lo) > lo
    assert kappa * math.tanh(hi) < hi
    for _ in range(90):
        mid = (lo + hi) / 2
        if kappa * math.tanh(mid) > mid:
            lo = mid
        else:
            hi = mid
    r = (lo + hi) / 2
    radius = 1e-4
    m = 1 / math.cosh(1.9 - radius)**2
    q = eps/(eps + 3.8)
    alpha_bound = ((eps + 2*radius)/(eps + 3.8 - 2*radius))**beta
    contraction = kappa*m + 4*kappa*beta/eps*(m*radius + 2*alpha_bound)
    offset = 4 * q**beta
    assert contraction < 0.25
    assert offset < (1-contraction)*radius
    x = [r, r, -r, -r]
    for _ in range(100):
        z = weighted_map(x, adj, kappa, eps, beta)
        if max(abs(a-b) for a,b in zip(x,z)) < 1e-14:
            x = z
            break
        x = z
    residual = max(abs(a-b) for a,b in zip(x,weighted_map(x,adj,kappa,eps,beta)))
    assert residual < 1e-12
    assert max(abs(a - s*r) for a, s in zip(x, [1,1,-1,-1])) < radius
    assert x[0] > x[1] > 0 > x[2] > x[3]
    return dict(r=r, fixed_point=x, residual=residual,
                computed_contraction_bound=contraction,
                checked_radius=radius, computed_center_offset_bound=offset)


if __name__ == '__main__':
    print('Connected labeled graph census (n, total, supports mixed compatible coloring):')
    for line in finite_graph_check(6):
        print(*line)
    print('Four-path quantitative contraction check:')
    for k, v in four_path_example().items():
        print(k, v)
    print('ALL CHECKS PASSED')
