#!/usr/bin/env python3
from collections import Counter
from math import ceil


def target_degrees(n):
    if n % 6 in (1, 4):
        return list(range(1, n - 1)) + [n, n + 1]
    return list(range(1, n + 1))


def matching(vertices):
    vertices = list(vertices)
    assert len(vertices) % 2 == 0
    return [(vertices[i], vertices[i + 1]) for i in range(0, len(vertices), 2)]


def build(n):
    if n < 6:
        raise ValueError("n must be at least 6")
    edges = {
        frozenset((1, 5, 6)),
        frozenset((2, 4, 6)),
        frozenset((2, 5, 6)),
        frozenset((3, 4, 5)),
        frozenset((3, 4, 6)),
        frozenset((3, 5, 6)),
        frozenset((4, 5, 6)),
    }
    for order in range(7, n + 1):
        deg = Counter(v for e in edges for v in e)
        by_degree = {d: v for v, d in deg.items()}
        m_now = ceil(order * (order + 1) / 6)
        m_prev = len(edges)
        k = m_now - m_prev
        link_edges = []

        if order % 6 in (0, 3):
            vertices = [by_degree[d] for d in range(k, order)]
            link_edges = matching(vertices)

        elif order % 6 in (2, 5):
            vertices = [by_degree[d] for d in range(k, order - 2)]
            link_edges = matching(vertices)

        else:  # order % 6 in (1, 4)
            A = [by_degree[d] for d in range(k, order - 2)]
            u = by_degree[order - 2]
            w = by_degree[order - 1]
            a, b = A[0], A[1]
            link_edges = [(a, u), (u, w), (w, b)]
            link_edges += matching(A[2:])

        assert len(link_edges) == k
        x = order
        for u, v in link_edges:
            edge = frozenset((x, u, v))
            assert len(edge) == 3
            assert edge not in edges
            edges.add(edge)

    return edges


def verify(n):
    edges = build(n)
    assert len(edges) == ceil(n * (n + 1) / 6)
    assert all(len(e) == 3 for e in edges)
    assert all(e <= set(range(1, n + 1)) for e in edges)
    deg = Counter(v for e in edges for v in e)
    assert len(deg) == n
    values = sorted(deg.values())
    assert values == target_degrees(n)
    assert len(set(values)) == n
    assert min(values) >= 1
    assert sum(values) == 3 * len(edges)
    return len(edges), values[0], values[-1]


if __name__ == "__main__":
    for n in range(6, 201):
        verify(n)
    sample = [6, 7, 8, 9, 10, 11, 12, 25, 50, 100, 200]
    for n in sample:
        m, dmin, dmax = verify(n)
        print(f"n={n}: edges={m}, min_degree={dmin}, max_degree={dmax}")
    print("verified n=6..200")
