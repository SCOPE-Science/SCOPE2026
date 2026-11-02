"""Reproduce exact finite checks for weighted tree neighborhood-max dilation.

This file checks the stated finite formula on deterministic tree samples.  The
unbounded theorem follows from the mathematical proof, not these tests.
"""
from collections import deque
from fractions import Fraction
from random import Random


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for j, (u, v, wt) in enumerate(edges):
        assert 0 <= u < n and 0 <= v < n and u != v and wt > 0
        adj[u].append((v, j))
        adj[v].append((u, j))
    return adj


def wave(n, edges, adj, edge_index, source, radius):
    """Edge weight of the radius wave into the far component, never crossing e."""
    u, v, _ = edges[edge_index]
    assert source in (u, v)
    far = v if source == u else u
    depth = {far: 0}
    todo = deque([far])
    while todo:
        a = todo.popleft()
        for b, j in adj[a]:
            if j == edge_index or b in depth:
                continue
            depth[b] = depth[a] + 1
            todo.append(b)
    return sum(wt for a, b, wt in edges if a in depth and b in depth
               and sorted((depth[a], depth[b])) == [radius - 1, radius])


def formula(n, edges, radius):
    if radius == 0:
        return Fraction(1)
    adj = adjacency(n, edges)
    return max(Fraction(wave(n, edges, adj, j, source, radius), wt)
               for j, (u, v, wt) in enumerate(edges) for source in (u, v))


def variation(edges, values):
    return sum(wt * abs(values[u] - values[v]) for u, v, wt in edges)


def dilate(n, adj, values, radius):
    curr = list(values)
    for _ in range(radius):
        curr = [max([curr[v]] + [curr[u] for u, _ in adj[v]]) for v in range(n)]
    return curr


def direct_cut_max(n, edges, radius):
    adj = adjacency(n, edges)
    best = Fraction(0)
    for mask in range(1, (1 << n) - 1):
        sig = [(mask >> i) & 1 for i in range(n)]
        ini = variation(edges, sig)
        out = variation(edges, dilate(n, adj, sig, radius))
        best = max(best, Fraction(out, ini))
    return best


def run():
    rng = Random(813704)
    profiles = cut_tests = signal_tests = equalities = 0
    for n in range(2, 11):
        for _ in range(40 if n <= 8 else 12):
            edges = [(v, rng.randrange(v), rng.randrange(1, 7)) for v in range(1, n)]
            adj = adjacency(n, edges)
            profiles += 1
            for radius in range(1, n + 1):
                predicted = formula(n, edges, radius)
                observed = direct_cut_max(n, edges, radius)
                assert observed == predicted, (n, edges, radius, observed, predicted)
                equalities += 1
                if radius == n:
                    assert predicted == 0
                for _ in range(7):
                    sig = [rng.randrange(-3, 5) for _ in range(n)]
                    vi = variation(edges, sig)
                    if vi:
                        vo = variation(edges, dilate(n, adj, sig, radius))
                        assert Fraction(vo, vi) <= predicted
                        signal_tests += 1
            cut_tests += ((1 << n) - 2) * n
    # Exact branching growth and instantaneous exhaustion after diameter.
    for b in range(1, 4):
        for height in range(1, 5):
            edges = []
            layers = [[0]]
            nxt = 1
            for _ in range(height):
                layer = []
                for u in layers[-1]:
                    for j in range(b):
                        edges.append((u, nxt, 1))
                        layer.append(nxt)
                        nxt += 1
                layers.append(layer)
            edges.append((0, nxt, 1))
            nxt += 1
            for radius in range(1, height + 1):
                assert formula(nxt, edges, radius) == b ** radius
            assert formula(nxt, edges, 2 * height) == 0
    print("PASS", profiles, "weighted trees;", equalities,
          "exact cut/formula comparisons;", cut_tests,
          "indicator cut instances;", signal_tests,
          "integer-signal inequalities; 12 branching families")


if __name__ == '__main__':
    run()
