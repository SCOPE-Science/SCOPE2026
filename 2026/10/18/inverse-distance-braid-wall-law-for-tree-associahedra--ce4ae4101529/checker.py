#!/usr/bin/env python3
"""Independent finite checks of exact labelled braid-wall survival formulas.

Requires only the Python standard library; complete proof is mathematical,
not inferred from this finite enumeration.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial


def tree_from_prufer(n, code):
    if n == 2:
        return ((0, 1),)
    degrees = [1] * n
    for x in code:
        degrees[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append(tuple(sorted((leaf, x))))
        degrees[leaf] -= 1
        degrees[x] -= 1
    a, b = (i for i in range(n) if degrees[i] == 1)
    edges.append((a, b))
    return tuple(sorted(edges))


def adjacent(n, edges):
    graph = [set() for _ in range(n)]
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph


def distance(n, edges, source):
    graph = adjacent(n, edges)
    q = deque([source]); dist = {source: 0}
    while q:
        x = q.popleft()
        for y in graph[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    assert len(dist) == n
    return dist


def connected_subsets(n, edges):
    graph = adjacent(n, edges)
    out = []
    for mask in range(1, 1 << n):
        members = [i for i in range(n) if mask & (1 << i)]
        seen = {members[0]}
        q = [members[0]]
        for x in q:
            for y in graph[x]:
                if mask & (1 << y) and y not in seen:
                    seen.add(y); q.append(y)
        if len(seen) == len(members):
            out.append(tuple(members))
    return out


def exposed_vertex(order, tubes, n):
    rank = {x: i for i, x in enumerate(order)}
    answer = [0] * n
    for s in tubes:
        answer[min(s, key=rank.__getitem__)] += 1
    return tuple(answer)


def test_tree(n, edges):
    tubes = connected_subsets(n, edges)
    permlist = list(permutations(range(n)))
    vertices = {p: exposed_vertex(p, tubes, n) for p in permlist}
    counts = defaultdict(int)
    changes = 0
    for p in permlist:
        for j in range(n - 1):
            q = list(p); q[j], q[j+1] = q[j+1], q[j]
            q = tuple(q)
            if p > q:
                continue  # Every permutohedron edge counted exactly once.
            u, v = sorted((p[j], p[j+1]))
            x, y = vertices[p], vertices[q]
            if x != y:
                assert all(x[t] == y[t] for t in range(n) if t not in (u, v))
                assert x[u] - y[u] == -(x[v] - y[v])
                counts[(u, v)] += 1
                changes += 1
    H = Fraction(0, 1)
    for u, v in combinations(range(n), 2):
        d = distance(n, edges, u)[v]
        H += Fraction(1, d)
        predicted = Fraction(factorial(n-1), d)
        assert predicted.denominator == 1, (n, d)
        assert counts[(u, v)] == predicted, (n, edges, u, v, counts[(u,v)], predicted)
    assert changes == factorial(n - 1) * H
    return changes


def main():
    checked = 0
    for n in range(2, 6):
        count = 0
        for code in product(range(n), repeat=max(n-2, 0)):
            test_tree(n, tree_from_prufer(n, code))
            checked += 1
            count += 1
        assert count == n**(n-2)
        print('all labelled trees', n, ':', count, 'PASS')
    for n in (6, 7):
        code_list = [tuple([0] * (n-2)), tuple(range(n-2)), tuple([i % 2 for i in range(n-2)])]
        for code in dict.fromkeys(code_list):
            test_tree(n, tree_from_prufer(n, code))
            checked += 1
        print('selected labelled trees', n, ':', len(dict.fromkeys(code_list)), 'PASS')
    print('TOTAL', checked, 'exact tests PASS')

if __name__ == '__main__':
    main()
