#!/usr/bin/env python3
"""Independent finite checks of the weight-two shorthand universal-cycle formula.

Run with Python 3 standard library: python3 verify.py
The manuscript supplies the proof for all n; this file checks finite cases.
"""
from itertools import product
from math import comb


def determinant(matrix):
    """Fraction-free Bareiss determinant over exact integers."""
    a = [list(row) for row in matrix]
    size = len(a)
    if size == 0:
        return 1
    denominator = 1
    sign = 1
    for k in range(size - 1):
        if a[k][k] == 0:
            row = next((i for i in range(k + 1, size) if a[i][k]), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % denominator == 0
                a[i][j] = numerator // denominator
        for i in range(k + 1, size):
            a[i][k] = 0
        denominator = pivot
    return sign * a[-1][-1]


def original_graph(n):
    m = n - 2
    vertices = ["".join(b) for b in product("01", repeat=m)
                if "".join(b).count("1") <= 2]
    edges = []
    for src in vertices:
        for bit in "01":
            label = src + bit
            if label.count("1") in (1, 2):
                edges.append((src, label[1:], label))
    assert len(edges) == comb(n, 2)
    return vertices, edges


def euler_tours(n):
    vertices, edges = original_graph(n)
    outgoing = {u: [] for u in vertices}
    for j, (src, _, _) in enumerate(edges):
        outgoing[src].append(j)
    canonical = "0" * (n - 2) + "1"
    anchor = next(i for i, (_, _, label) in enumerate(edges)
                  if label == canonical)
    first = edges[anchor]
    tours = set()
    expected = {edge[2] for edge in edges}

    def visit(vertex, used, path):
        if len(path) == len(edges):
            if vertex != first[0]:
                return
            circular = "".join(edges[i][2][-1] for i in path)
            factors = {("".join(circular[(j+k) % len(circular)]
                                for k in range(n - 1)))
                       for j in range(len(circular))}
            assert factors == expected
            assert circular not in tours
            tours.add(circular)
            return
        for nxt in outgoing[vertex]:
            if not (used & (1 << nxt)):
                visit(edges[nxt][1], used | (1 << nxt), path + (nxt,))

    visit(first[1], 1 << anchor, (anchor,))
    return len(tours)


def graph_cofactor(n):
    vertices, edges = original_graph(n)
    index = {w: i for i, w in enumerate(vertices)}
    size = len(vertices)
    lap = [[0] * size for _ in range(size)]
    for src, target, _ in edges:
        i, j = index[src], index[target]
        lap[i][i] += 1
        lap[i][j] -= 1
    return determinant([row[:-1] for row in lap[:-1]])


def contracted_cofactor(n):
    m = n - 2
    lap = [[0] * m for _ in range(m)]
    for i in range(m):
        lap[i][i] += 2
        lap[i][(i - 1) % m] -= 1
        lap[i][m - 1 - i] -= 1
    return determinant([row[:-1] for row in lap[:-1]])


def direct_binary_enumeration(n):
    length = comb(n, 2)
    allowed = {i for i in range(1 << (n - 1))
               if i.bit_count() in (1, 2)}
    circles = set()
    for value in range(1 << length):
        w = format(value, f"0{length}b")
        cyclic = w + w[:n - 2]
        observed = {int(cyclic[j:j + n - 1], 2) for j in range(length)}
        if observed == allowed and len(observed) == length:
            circles.add(min(w[k:] + w[:k] for k in range(length)))
    return len(circles)


def main():
    for n in range(3, 13):
        expected = 1 << ((n - 2) // 2)
        euler = euler_tours(n)
        compressed = contracted_cofactor(n)
        assert euler == compressed == expected, (n, euler, compressed, expected)
        if n <= 10:
            original = graph_cofactor(n)
            assert original == expected, (n, original, expected)
        if n <= 6:
            raw = direct_binary_enumeration(n)
            assert raw == expected, (n, raw, expected)
        print(f"n={n}: {expected} cycles; independent checks agree")
    print("VERIFY_OK n=3..12; full graph cofactors n=3..10; direct binary enumeration n=3..6")


if __name__ == "__main__":
    main()
