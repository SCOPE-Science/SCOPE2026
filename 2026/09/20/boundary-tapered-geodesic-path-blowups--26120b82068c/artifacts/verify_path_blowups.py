#!/usr/bin/env python3
"""Finite checks for the path-blow-up geodesic-subpath formulas."""

from collections import deque


def blowup_graph(parts):
    layers = []
    adjacency = {}
    nxt = 0
    for size in parts:
        layer = list(range(nxt, nxt + size))
        nxt += size
        layers.append(layer)
        for v in layer:
            adjacency[v] = set()
    for left, right in zip(layers, layers[1:]):
        for u in left:
            for v in right:
                adjacency[u].add(v)
                adjacency[v].add(u)
    return adjacency


def gpn_by_bfs(adjacency):
    vertices = sorted(adjacency)
    total = len(vertices)  # zero-length geodesics
    for pos, source in enumerate(vertices):
        distance = {source: 0}
        sigma = {source: 1}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if v not in distance:
                    distance[v] = distance[u] + 1
                    sigma[v] = sigma[u]
                    queue.append(v)
                elif distance[v] == distance[u] + 1:
                    sigma[v] += sigma[u]
        for target in vertices[pos + 1:]:
            total += sigma[target]
    return total


def gpn_layer_formula(parts):
    n = sum(parts)
    distinct_layers = 0
    for i in range(len(parts)):
        product = 1
        for j in range(i, len(parts)):
            product *= parts[j]
            if j > i:
                distinct_layers += product
    same_layer = 0
    for i, size in enumerate(parts):
        left = parts[i - 1] if i else 0
        right = parts[i + 1] if i + 1 < len(parts) else 0
        same_layer += size * (size - 1) // 2 * (left + right)
    return n + distinct_layers + same_layer


def h_parts(q):
    return [1, 2] + [3] * (q - 2) + [2, 1]


def h_closed(q):
    numerator = 121 * (3 ** q) + 594 * q - 1269
    assert numerator % 36 == 0
    return numerator // 36


def g3_closed(q):
    numerator = 9 * (3 ** q) + 66 * q - 81
    assert numerator % 4 == 0
    return numerator // 4


def compositions(n):
    for mask in range(1 << (n - 1)):
        parts = []
        current = 1
        for i in range(n - 1):
            if (mask >> i) & 1:
                parts.append(current)
                current = 1
            else:
                current += 1
        parts.append(current)
        if len(parts) >= 2:
            yield parts


print("q n gpn(H_q) gpn(G_{3,q}) difference")
for q in range(3, 9):
    H = h_parts(q)
    G3 = [3] * q
    h_bfs = gpn_by_bfs(blowup_graph(H))
    g_bfs = gpn_by_bfs(blowup_graph(G3))
    assert h_bfs == gpn_layer_formula(H) == h_closed(q)
    assert g_bfs == gpn_layer_formula(G3) == g3_closed(q)
    difference = h_bfs - g_bfs
    assert difference == 10 * (3 ** (q - 2)) - 15
    assert difference > 0
    print(q, 3 * q, h_bfs, g_bfs, difference)

print("path-blow-up maxima for n divisible by 3 through 18")
for n in (9, 12, 15, 18):
    best = -1
    maximizers = []
    for parts in compositions(n):
        value = gpn_layer_formula(parts)
        if value > best:
            best = value
            maximizers = [parts]
        elif value == best:
            maximizers.append(parts)
    q = n // 3
    H = h_parts(q)
    assert best == gpn_layer_formula(H)
    # H is symmetric, so it is the unique composition here, not merely unique up to reversal.
    assert maximizers == [H]
    print(n, best, H)
