#!/usr/bin/env python3
"""Exact perfect-matching and elementary-square-flip enumeration for a 2x2xn box.
No external libraries. Run: python3 verify_direct.py
"""
from collections import Counter
from functools import lru_cache
import json


def enumerate_degrees(n):
    cells = [(x, y, z) for z in range(n) for x in range(2) for y in range(2)]
    index = {c: i for i, c in enumerate(cells)}
    edges = []
    for c in cells:
        a = index[c]
        for axis in range(3):
            nxt = list(c)
            nxt[axis] += 1
            nxt = tuple(nxt)
            if nxt in index:
                edges.append((a, index[nxt]))
    edge_id = {e: i for i, e in enumerate(edges)}
    adjacency = [[] for _ in cells]
    for k, (a, b) in enumerate(edges):
        adjacency[a].append((b, k))
        adjacency[b].append((a, k))

    # The four-cell faces are exactly the elementary 2x2x1 slabs.
    faces = []
    for c in cells:
        for axis1 in range(3):
            for axis2 in range(axis1 + 1, 3):
                d = list(c)
                d[axis1] += 1
                e = list(c)
                e[axis2] += 1
                f = list(d)
                f[axis2] += 1
                d, e, f = tuple(d), tuple(e), tuple(f)
                if not all(v in index for v in (d, e, f)):
                    continue
                q = (c, d, f, e)
                ids = [edge_id[tuple(sorted((index[q[i]], index[q[(i+1)%4]])))] for i in range(4)]
                faces.append(((1 << ids[0]) | (1 << ids[2]),
                              (1 << ids[1]) | (1 << ids[3])))
    assert len(faces) == 5 * n - 4

    @lru_cache(None)
    def all_matchings(remaining):
        if remaining == 0:
            return (0,)
        a = (remaining & -remaining).bit_length() - 1
        choices = []
        for b, k in adjacency[a]:
            if (remaining >> b) & 1:
                submask = remaining ^ (1 << a) ^ (1 << b)
                for smaller in all_matchings(submask):
                    choices.append(smaller | (1 << k))
        return tuple(choices)

    hist = Counter()
    for matching in all_matchings((1 << len(cells)) - 1):
        degree = sum((matching & u) == u or (matching & v) == v for u, v in faces)
        hist[degree] += 1
    return dict(sorted(hist.items()))


def main():
    output = {}
    for n in range(1, 9):
        h = enumerate_degrees(n)
        assert min(h) == (2*n+2)//3
        assert max(h) == 3*n - 2
        assert h[max(h)] == (3 if n == 2 else 2)
        if n % 3 == 0:
            assert h[min(h)] == 4 * 3**(n//3 - 1)
        output[str(n)] = {str(d): count for d, count in h.items()}
    assert [sum(x.values()) for x in output.values()] == [2, 9, 32, 121, 450, 1681, 6272, 23409]
    print(json.dumps(output, sort_keys=True, separators=(',', ':')))
    print('DIRECT_VERIFY_OK')


if __name__ == '__main__':
    main()
