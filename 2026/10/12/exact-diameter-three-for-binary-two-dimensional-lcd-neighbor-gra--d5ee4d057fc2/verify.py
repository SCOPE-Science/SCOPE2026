#!/usr/bin/env python3
from itertools import combinations
from collections import deque


def dot(x, y):
    return (x & y).bit_count() & 1


def rank(vectors, n):
    piv = [0] * n
    for x in vectors:
        y = x
        while y:
            i = y.bit_length() - 1
            if piv[i]:
                y ^= piv[i]
            else:
                piv[i] = y
                break
    return sum(bool(x) for x in piv)


def planes(n):
    seen = set()
    out = []
    for a, b in combinations(range(1, 1 << n), 2):
        if rank([a, b], n) != 2:
            continue
        s = frozenset((0, a, b, a ^ b))
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def lcd_plane(s):
    nz = list(s - {0})
    a, b = nz[0], nz[1]
    return (dot(a, a) * dot(b, b) ^ dot(a, b)) == 1


def graph(n):
    v = [s for s in planes(n) if lcd_plane(s)]
    adj = [[] for _ in v]
    for i in range(len(v)):
        for j in range(i):
            if len(v[i] & v[j]) == 2:
                adj[i].append(j)
                adj[j].append(i)
    return v, adj


def diameter(adj):
    ans = 0
    for s in range(len(adj)):
        dist = [-1] * len(adj)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert min(dist) >= 0
        ans = max(ans, max(dist))
    return ans


def witness(n):
    e1, e2, e3, e4 = 1, 2, 4, 8
    c = frozenset((0, e1, e2, e1 ^ e2))
    d1 = e1 ^ e2 ^ e3
    d2 = e3 ^ e4
    d = frozenset((0, d1, d2, d1 ^ d2))
    assert lcd_plane(c) and lcd_plane(d)
    assert c & d == {0}
    for x in c - {0}:
        for y in d - {0}:
            det = dot(x, x) * dot(y, y) ^ dot(x, y)
            assert det == 0
    return c, d


def check_gram_identity(n):
    w = (1 << n) - 1
    for c in range(1, 1 << n):
        qc = dot(c, c)
        for z in range(1 << n):
            qz = dot(z, z)
            tz = z ^ (w if qz else 0)
            lhs = qc * qz ^ dot(c, z)
            rhs = dot(c, tz)
            assert lhs == rhs


def main():
    for n in (4, 5, 6):
        check_gram_identity(n)
        c, d = witness(n)
        v, adj = graph(n)
        diam = diameter(adj)
        assert diam == 3
        index = {s: i for i, s in enumerate(v)}
        s, t = index[c], index[d]
        dist = [-1] * len(v)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for x in adj[u]:
                if dist[x] < 0:
                    dist[x] = dist[u] + 1
                    q.append(x)
        assert dist[t] == 3
        print(f'n={n} lcd_planes={len(v)} diameter={diam} witness_distance={dist[t]}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
