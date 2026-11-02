#!/usr/bin/env python3
"""Direct shortest-path census of minimum distance-equalizer sets.

All graph distances are recomputed by breadth-first search on the original
Johnson and Kneser adjacency predicates. The predicted orbit list is tested
against every two- and three-element candidate subset, without using the
intersection-signature proof.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def distances(vertices, are_adjacent):
    k = len(vertices)
    adj = [[j for j in range(k) if i != j and are_adjacent(vertices[i], vertices[j])]
           for i in range(k)]
    answer = []
    for i in range(k):
        ds = [-1] * k
        ds[i] = 0
        todo = deque([i])
        while todo:
            v = todo.popleft()
            for u in adj[v]:
                if ds[u] == -1:
                    ds[u] = ds[v] + 1
                    todo.append(u)
        assert all(x >= 0 for x in ds), 'Disconnected graph'
        answer.append(ds)
    return answer


def is_equalizer(ds, selected):
    remaining = [i for i in range(len(ds)) if i not in selected]
    for a, b in combinations(remaining, 2):
        if not any(ds[a][w] == ds[b][w] for w in selected):
            return False
    return True


def orbit_type(vertices, selected):
    degree = Counter(u for k in selected for u in vertices[k])
    return tuple(sorted(degree.values(), reverse=True))


def expected(n):
    if n == 4:
        return {(1, 1, 1, 1): 3}
    if n == 5:
        return {(2, 2, 2): comb(n, 3), (2, 1, 1, 1, 1): 30}
    if n == 6:
        return {(2, 2, 2): comb(n, 3), (1, 1, 1, 1, 1, 1): 15}
    return {(2, 2, 2): comb(n, 3)}


def check_one(n, flavor):
    vs = list(combinations(range(n), 2))
    if flavor == 'Johnson':
        ds = distances(vs, lambda x, y: bool(set(x).intersection(y)))
    else:
        ds = distances(vs, lambda x, y: set(x).isdisjoint(y))
    assert len(vs) == comb(n, 2)
    dimension = 2 if n == 4 else 3
    if n >= 5:
        assert not any(is_equalizer(ds, selected)
                       for selected in combinations(range(len(vs)), 2))
    counts = Counter()
    for selected in combinations(range(len(vs)), dimension):
        if is_equalizer(ds, selected):
            counts[orbit_type(vs, selected)] += 1
    assert dict(counts) == expected(n), (n, flavor, counts, expected(n))
    print(f'{flavor} n={n}: eqdim={dimension}, bases={sum(counts.values())}, types={dict(counts)}')


def main():
    for n in range(4, 11):
        check_one(n, 'Johnson')
        if n >= 5:
            check_one(n, 'Kneser')
    print('All direct BFS census checks passed.')

if __name__ == '__main__':
    main()
