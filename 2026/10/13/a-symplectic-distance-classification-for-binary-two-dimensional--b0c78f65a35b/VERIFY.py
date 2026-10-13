"""Self-contained finite verification of the rank-two binary LCD neighbor graph.

Enumerates all two-dimensional subspaces from integer bit masks, uses the
original dot-product Gram determinant for LCD (not the symplectic criterion),
and independently reconstructs graph distances by breadth-first search.
"""
from collections import deque


def dot(a, b):
    return ((a & b).bit_count() & 1)


def is_lcd(a, b):
    return dot(a, a) * dot(b, b) != dot(a, b)


def omega(a, b):
    return dot(a, b) ^ (a.bit_count() & 1) * (b.bit_count() & 1)


def predicted(n):
    t = n & 1
    size = ((1 << n) - (1 << t)) * (1 << (n - 1)) // 6
    s1 = 3 * ((1 << (n - 2)) - 1)
    s3 = ((1 << (n - 2)) - (1 << t)) * (1 << (n - 3)) // 6
    return (1, s1, size - 1 - s1 - s3, s3)


def verify(n):
    seen = set()
    planes = []
    for a in range(1, 1 << n):
        for b in range(a + 1, 1 << n):
            if b == a:
                continue
            s = frozenset((a, b, a ^ b))
            if s in seen:
                continue
            seen.add(s)
            if is_lcd(a, b):
                assert len(s) == 3
                assert omega(a, b) == 1
                planes.append(s)
            else:
                assert omega(a, b) == 0

    index = {s: j for j, s in enumerate(planes)}
    owners = {}
    for i, s in enumerate(planes):
        for x in s:
            owners.setdefault(x, []).append(i)
    graph = []
    for i, s in enumerate(planes):
        v = set()
        for x in s:
            v.update(owners[x])
        v.discard(i)
        graph.append(v)
    pred = predicted(n)
    assert len(planes) == sum(pred), (n, len(planes), pred)
    for i, u in enumerate(planes):
        assert len(graph[i]) == pred[1]
        dist = [-1] * len(planes)
        dist[i] = 0
        todo = deque([i])
        while todo:
            j = todo.popleft()
            for k in graph[j]:
                if dist[k] < 0:
                    dist[k] = dist[j] + 1
                    todo.append(k)
        shells = tuple(dist.count(j) for j in range(4))
        assert shells == pred, (n, i, shells, pred)
        assert all(0 <= d <= 3 for d in dist)
        for j, w in enumerate(planes):
            pairing_zero = all(omega(a, b) == 0 for a in u for b in w)
            if i == j:
                assert dist[j] == 0
            elif not u.isdisjoint(w):
                assert dist[j] == 1
            elif pairing_zero:
                assert dist[j] == 3
            else:
                assert dist[j] == 2
    print(f'n={n}; planes={len(planes)}; spheres={pred}; check=PASS')


if __name__ == '__main__':
    for n in (4, 5, 6):
        verify(n)
    print('VERIFY_OK')
