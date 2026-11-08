#!/usr/bin/env python3
"""Standalone exact verification of the first order-9 KC-shift obstruction.

Python 3.10+, standard library only. Expected output: VERIFY_OK.
Pruefer-code enumeration is exhaustive on labelled trees through order eight;
canonical rooted encodings retain one representative per isomorphism type.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product

T_EDGES = ((0, 1), (0, 5), (1, 2), (2, 3), (2, 4),
           (5, 6), (6, 7), (6, 8))
U_EDGES = ((0, 1), (0, 5), (1, 2), (1, 6), (2, 3),
           (2, 4), (6, 7), (6, 8))


def neighbours(n, edges):
    adj = [set() for _ in range(n)]
    for x, y in edges:
        assert x != y and 0 <= x < n and 0 <= y < n
        adj[x].add(y)
        adj[y].add(x)
    return adj


def prufer_edges(n, code):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    leaves = [i for i in range(n) if deg[i] == 1]
    assert len(leaves) == 2
    edges.append(tuple(leaves))
    return tuple(edges)


def tree_code(n, edges):
    adj = neighbours(n, edges)
    def rooted(v, parent):
        sub = sorted(rooted(w, v) for w in adj[v] if w != parent)
        return '(' + ''.join(sub) + ')'
    return min(rooted(v, -1) for v in range(n))


def one_from_each_tree(n):
    representatives = {}
    codes = product(range(n), repeat=max(n-2, 0))
    for code in codes:
        E = prufer_edges(n, code) if n >= 2 else ()
        canon = tree_code(n, E)
        if canon not in representatives:
            representatives[canon] = E
    return list(representatives.values())


def expected_greedy(n, edges):
    adj = neighbours(n, edges)
    closed = [(1 << v) | sum(1 << u for u in adj[v]) for v in range(n)]
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return Fraction(0)
        summand = Fraction(0)
        for v in range(n):
            if mask & (1 << v):
                summand += 1 + rec(mask & ~closed[v])
        return summand / mask.bit_count()
    return rec((1 << n) - 1)


def path_between(adj, x, y):
    parents = {x: -1}
    queue = [x]
    for v in queue:
        if v == y:
            break
        for w in adj[v]:
            if w not in parents:
                parents[w] = v
                queue.append(w)
    if y not in parents:
        raise AssertionError('Disconnected input')
    path = [y]
    while path[-1] != x:
        path.append(parents[path[-1]])
    return path[::-1]


def proper_kc_transforms(n, edges):
    adj = neighbours(n, edges)
    S = {tuple(sorted(edge)) for edge in edges}
    for x in range(n):
        for y in range(x+1, n):
            if len(adj[x]) <= 1 or len(adj[y]) <= 1:
                continue
            path = path_between(adj, x, y)
            if any(len(adj[v]) != 2 for v in path[1:-1]):
                continue
            z = path[-2]
            moved = [(y, w) for w in adj[y] if w != z]
            assert moved
            updated = set(S)
            for v, w in moved:
                updated.remove(tuple(sorted((v, w))))
                updated.add(tuple(sorted((x, w))))
            result = tuple(sorted(updated))
            assert len(result) == n-1
            assert sum(len(s)==1 for s in neighbours(n, result)) == sum(len(s)==1 for s in adj)+1
            yield (x, y, result)


def brute_permutation_counts(n, edges):
    adj = neighbours(n, edges)
    hist = Counter()
    for order in permutations(range(n)):
        chosen = set()
        for v in order:
            if chosen.isdisjoint(adj[v]):
                chosen.add(v)
        hist[len(chosen)] += 1
    return dict(sorted(hist.items()))


def main():
    types = (1, 1, 1, 2, 3, 6, 11, 23)
    total = 0
    by_order = []
    for n in range(1, 9):
        reps = one_from_each_tree(n)
        assert len(reps) == types[n-1], (n, len(reps))
        checked = 0
        minimum_gap = None
        for E in reps:
            before = expected_greedy(n, E)
            for x, y, F in proper_kc_transforms(n, E):
                after = expected_greedy(n, F)
                gap = after-before
                assert gap > 0, (n, E, x, y, gap)
                checked += 1
                minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
        total += checked
        by_order.append((n, len(reps), checked, str(minimum_gap)))

    assert set(T_EDGES) != set(U_EDGES)
    moves = list(proper_kc_transforms(9, T_EDGES))
    assert any(set(E) == set(U_EDGES) for _,_,E in moves)
    assert expected_greedy(9, T_EDGES) == Fraction(73, 15)
    assert expected_greedy(9, U_EDGES) == Fraction(34, 7)
    assert Fraction(73,15)-Fraction(34,7) == Fraction(1,105)
    hist_T = brute_permutation_counts(9, T_EDGES)
    hist_U = brute_permutation_counts(9, U_EDGES)
    assert hist_T == {3:25984, 4:139776, 5:53760, 6:143360}, hist_T
    assert hist_U == {3:35200, 4:127680, 5:53760, 6:146240}, hist_U
    assert sum(k*v for k,v in hist_T.items()) == 9*8*7*6*5*4*3*2*1*Fraction(73,15)
    assert sum(k*v for k,v in hist_U.items()) == 9*8*7*6*5*4*3*2*1*Fraction(34,7)
    print('ORDERS n, unlabeled trees, proper shifts, smallest positive shift:')
    for line in by_order:
        print(*line)
    print('BRUTE_T', hist_T)
    print('BRUTE_U', hist_U)
    print('WITNESS', '73/15 > 34/7', 'gap=1/105')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
