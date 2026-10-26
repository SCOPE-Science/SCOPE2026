"""Exact token-swapping distances on the eight-vertex Wagner graph.

Run: python3 verify_cube.py
No dependencies outside Python standard library.
"""
from collections import Counter, deque
from itertools import permutations
from math import factorial

EDGES = sorted({tuple(sorted((i, (i + 1) % 8))) for i in range(8)} | {(i, i + 4) for i in range(4)})
assert len(EDGES) == 12 and len(set(EDGES)) == 12


def rank(p):
    # Lehmer factorial code, independent of permutation enumerator order.
    pool = list(range(8))
    code = 0
    for i, x in enumerate(p):
        j = pool.index(x)
        code += j * factorial(7 - i)
        pool.pop(j)
    return code


def unrank(k):
    pool = list(range(8))
    p = []
    for i in range(8):
        step = factorial(7 - i)
        j, k = divmod(k, step)
        p.append(pool.pop(j))
    assert k == 0
    return tuple(p)


def check():
    start = tuple(range(8))
    # Method A: tuple hashing BFS, without factorial numbering.
    distance = {start: 0}
    todo = deque([start])
    while todo:
        p = todo.popleft()
        d = distance[p]
        for u, v in EDGES:
            q = list(p)
            q[u], q[v] = q[v], q[u]
            q = tuple(q)
            if q not in distance:
                distance[q] = d + 1
                todo.append(q)
    assert len(distance) == factorial(8)
    a = Counter(distance.values())
    expected = [1, 12, 90, 500, 2059, 5960, 11124, 11986, 6748, 1702, 138]
    assert [a.get(i, 0) for i in range(len(expected))] == expected, a
    assert max(distance.values()) == 10
    far = [p for p, d in distance.items() if d == 10]
    assert len(far) == 138
    # Method B: full, independent array BFS indexed by Lehmer code.
    array = [-1] * factorial(8)
    array[rank(start)] = 0
    queue = deque([0])
    while queue:
        r = queue.popleft()
        p = list(unrank(r))
        for u, v in EDGES:
            p[u], p[v] = p[v], p[u]
            nr = rank(p)
            if array[nr] == -1:
                array[nr] = array[r] + 1
                queue.append(nr)
            p[u], p[v] = p[v], p[u]
    assert sorted(distance.values()) == sorted(array)
    for p, d in distance.items():
        assert array[rank(p)] == d
    # Exact graph-metric transport bound and slack census.
    adj = [set() for _ in range(8)]
    for u, v in EDGES:
        adj[u].add(v)
        adj[v].add(u)
    hop = [[100] * 8 for _ in range(8)]
    for root in range(8):
        hop[root][root] = 0
        walk = deque([root])
        while walk:
            u = walk.popleft()
            for v in adj[u]:
                if hop[root][v] == 100:
                    hop[root][v] = hop[root][u] + 1
                    walk.append(v)
    slack = Counter()
    extreme_transport = Counter()
    for p, d in distance.items():
        moved = sum(hop[i][p[i]] for i in range(8))
        lower = (moved + 1) // 2
        assert lower <= d
        slack[d - lower] += 1
        if d == 10:
            extreme_transport[moved] += 1
    assert slack == Counter({0: 16350, 1: 18574, 2: 5322, 3: 74}), slack
    assert extreme_transport == Counter({16: 90, 15: 48}), extreme_transport
    print('states', len(distance))
    print('distance_shells', expected)
    print('diameter', 10, 'diametral_states', 138)
    print('diametral_transport', sorted(extreme_transport.items()))
    print('transport_bound_slack', sorted(slack.items()))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
