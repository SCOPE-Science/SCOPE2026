#!/usr/bin/env python3
"""Finite checks for the pair-incidence constructions in the accompanying result."""
from math import ceil, floor


def pair_cover(n, edges, u, v):
    return sum(1 for a, b in edges if a == u or b == u or a == v or b == v)


def check_graph(n, edges, q, expected_m):
    assert len(edges) == expected_m
    for a, b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
    for u in range(n):
        for v in range(u + 1, n):
            assert pair_cover(n, edges, u, v) >= q


def havel_hakimi(degrees):
    rem = [[d, i] for i, d in enumerate(degrees)]
    edges = []
    while True:
        rem.sort(reverse=True)
        d, v = rem[0]
        if d == 0:
            break
        rem = rem[1:]
        assert d <= len(rem)
        for j in range(d):
            assert rem[j][0] > 0
            edges.append((v, rem[j][1]))
            rem[j][0] -= 1
        rem.append([0, v])
    return edges


def odd_q_graph(n, q):
    assert q >= 3 and q % 2 == 1 and q <= 2 * n - 3
    d = (q + 1) // 2
    m = ceil(d * n / 2)
    total = 2 * m
    degrees = [d] * n
    for i in range(total - d * n):
        degrees[i] += 1
    edges = havel_hakimi(degrees)
    check_graph(n, edges, q, m)
    return edges


def q1_graph(n):
    edges = [(2*i, 2*i+1) for i in range(n // 2)]
    check_graph(n, edges, 1, floor(n / 2))
    return edges


def q2_graph(n):
    edges = []
    offset = 0
    if n % 3 == 1:
        block = 4
    elif n % 3 == 2:
        block = 5
    else:
        block = 0
    if block:
        edges += [(offset+i, offset+i+1) for i in range(block-1)]
        offset += block
    while offset < n:
        edges += [(offset, offset+1), (offset+1, offset+2)]
        offset += 3
    check_graph(n, edges, 2, ceil(2*n/3))
    return edges


def shift_edges(edges, s):
    return [(a+s, b+s) for a, b in edges]


def q4_block(size):
    if size == 3:
        return [(0,1),(0,1),(0,2),(1,2)]
    if size == 4:
        return [(0,2),(0,3),(1,2),(1,3),(2,3)]
    if size == 5:
        return [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
    if size == 6:
        return [(i,j) for i in (0,1) for j in (2,3,4,5)]
    if size == 7:
        return [
            (3,4),(4,5),(5,6),
            (0,3),(0,6),(1,3),(1,4),(2,5),(2,6)
        ]
    raise ValueError(size)


def q4_graph(n):
    edges = []
    offset = 0
    if n in (3,4):
        sizes = [n]
    else:
        r = n % 5
        if r == 0:
            sizes = [5] * (n // 5)
        elif r == 1:
            sizes = [6] + [5] * ((n - 6) // 5)
        elif r == 2:
            sizes = [7] + [5] * ((n - 7) // 5)
        elif r == 3:
            sizes = [3] + [5] * ((n - 3) // 5)
        else:
            sizes = [4] + [5] * ((n - 4) // 5)
    for s in sizes:
        edges += shift_edges(q4_block(s), offset)
        offset += s
    check_graph(n, edges, 4, ceil(6*n/5))
    return edges


def verify_lrc_family():
    for N in range(5, 51):
        n = N*N + N - 1
        k = N*(N-2)
        r = N + 1
        k1 = ceil(k/r)
        k2 = k1*r - k
        n1 = ceil(n/(r+1))
        n2 = n1*(r+1) - n
        dstar = n-k-k1+2
        assert (n1, k1, n2, k2) == (N, N-2, N+1, N-2)
        assert n2-k2 == 3
        assert n2 >= ceil((3+1)*n1/4)
        assert dstar == 2*N + 3


def main():
    for n in range(3, 41):
        q1_graph(n)
        q2_graph(n)
        q4_graph(n)
        for q in range(3, 2*n-2, 2):
            odd_q_graph(n, q)
    verify_lrc_family()
    print("verified pair-incidence constructions for 3 <= N <= 40")
    print("verified odd q with 3 <= q <= 2N-3")
    print("verified q=1,2,4 sharp construction sizes")
    print("verified LRC infinite-family identities for 5 <= N <= 50")


if __name__ == "__main__":
    main()
