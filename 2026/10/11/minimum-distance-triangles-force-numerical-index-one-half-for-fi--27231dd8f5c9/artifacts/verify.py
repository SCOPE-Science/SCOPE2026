"""Exact finite-graph checks supporting a triangular-metric numerical-index theorem.

All arithmetic is integer or Fraction. Finite enumeration is illustrative, not
an exhaustive proof of the unbounded-order theorem in RESULT.md.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations


def is_connected(n, edges):
    if not edges:
        return False
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    queue = deque([0])
    while queue:
        for j in adj[queue.popleft()]:
            if j not in seen:
                seen.add(j)
                queue.append(j)
    return len(seen) == n


def triangle(n, edges):
    eset = set(edges)
    for a, b, c in combinations(range(n), 3):
        if (a, b) in eset and (a, c) in eset and (b, c) in eset:
            return a, b, c
    return None


def enumerate_potentials(n, edges, anchor):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    # BFS order ensures every new vertex has an already-assigned parent.
    order = [anchor]
    parents = {anchor: None}
    for u in order:
        for v in sorted(adj[u]):
            if v not in parents:
                parents[v] = u
                order.append(v)
    assert len(order) == n
    vals = {anchor: 0}
    def rec(k):
        if k == n:
            yield tuple(vals[i] for i in range(n))
            return
        v = order[k]
        p = parents[v]
        for d in (-1, 0, 1):
            vals[v] = vals[p] + d
            if all(abs(vals[v] - vals[z]) <= 1 for z in adj[v] if z in vals and z != v):
                yield from rec(k + 1)
        vals.pop(v, None)
    yield from rec(1)


def tight_connected(n, edges, f):
    return is_connected(n, [(u, v) for u, v in edges if abs(f[u] - f[v]) == 1])


def weighted_distance(n, edges, f, start):
    d = [10 ** 9] * n
    d[start] = 0
    for _ in range(n - 1):
        change = False
        for u, v in edges:
            w = 2 - abs(f[u] - f[v])
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                change = True
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                change = True
        if not change:
            break
    return d


def verify(n, edges, tri, tally):
    a, b, c = tri
    extreme = [f for f in enumerate_potentials(n, edges, a) if tight_connected(n, edges, f)]
    assert extreme, 'no dual vertices'
    tally['dual_extremes'] += len(extreme)
    # Every extreme potential has integer values; the converse follows
    # from a connected tight-edge spanning subgraph (proved in RESULT.md).
    # Exact lower-bound split on every flat edge and every extreme potential.
    for f in extreme:
        for u, v in edges:
            if f[u] == f[v]:
                h = weighted_distance(n, edges, f, u)
                assert h[v] == 2
                for i, j in edges:
                    fp = Fraction(f[i]-f[j], 2)
                    hp = Fraction(h[i]-h[j], 2)
                    assert abs(fp + hp) <= 1 and abs(fp - hp) <= 1
                assert abs(Fraction(f[u]-f[v]+h[u]-h[v], 2)) == 1
                assert abs(Fraction(f[u]-f[v]-h[u]+h[v], 2)) == 1
                tally['splittings'] += 1
    # Direct computation of the explicit rank-two operator, using the
    # extreme Lipschitz potentials to norm edge molecules.
    def image_eval(f, vertex):
        if vertex == a:
            return Fraction(0)
        if vertex == b:
            return Fraction(f[c]) - Fraction(f[b], 2)
        return Fraction(f[c], 2)

    op_norm = Fraction(0)
    radius = Fraction(0)
    for u, v in edges:
        for f in extreme:
            magnitude = abs(image_eval(f, u) - image_eval(f, v))
            op_norm = max(op_norm, magnitude)
            if abs(f[u] - f[v]) == 1:
                radius = max(radius, magnitude)
                assert magnitude <= Fraction(1, 2), (n, edges, tri, f, u, v)
                tally['norming_tests'] += 1
    assert op_norm == 1, (op_norm, n, edges)
    assert radius == Fraction(1, 2), (radius, n, edges)
    tally['triangle_graphs'] += 1


def main():
    tally = {'connected_graphs': 0, 'triangle_graphs': 0,
             'dual_extremes': 0, 'norming_tests': 0, 'splittings': 0}
    for n in range(3, 6):
        candidate_edges = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(candidate_edges)):
            edges = [e for bit, e in enumerate(candidate_edges) if mask >> bit & 1]
            if not is_connected(n, edges):
                continue
            tally['connected_graphs'] += 1
            tri = triangle(n, edges)
            if tri is not None:
                verify(n, edges, tri, tally)
    print('VERIFY_OK', ' '.join(k+'='+str(v) for k, v in tally.items()), 'n=3..5 exact=True')


if __name__ == '__main__':
    main()
