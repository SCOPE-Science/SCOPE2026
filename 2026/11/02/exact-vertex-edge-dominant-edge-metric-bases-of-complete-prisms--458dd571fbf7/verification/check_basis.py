#!/usr/bin/env python3
"""Independent exhaustive graph-distance check for complete-prism edge landmarks.

Runs on standard Python 3.8+; no third-party packages are required.
The graph is constructed from its adjacency lists and all distances use BFS.
"""
from collections import deque
from itertools import combinations
from math import comb


def predicted_basis(n, sel):
    # Vertices indexed 0..n-1 in the first clique, n..2n-1 in the second.
    top = {i for i in range(n) if (sel >> i) & 1}
    bottom = {i for i in range(n) if (sel >> (i + n)) & 1}
    holes = set(range(n)) - (top | bottom)
    doubled = top & bottom
    if n >= 7:
        return (len(holes) == 1 and not doubled and
                len(top) >= 3 and len(bottom) >= 3)
    if len(holes) == 1 and len(doubled) == 1:
        return True
    if holes or doubled:
        return False
    a, b = len(top), len(bottom)
    return min(a, b) == 0 or (n >= 5 and min(a, b) >= 2)


def predicted_count(n):
    if n >= 7:
        return n * (2 ** (n - 1) - 2 * (1 + (n - 1) + comb(n - 1, 2)))
    t = 2 if n <= 4 else 2 ** n - 2 * n
    return n * (n - 1) * 2 ** (n - 2) + t


def check_one(n):
    N = 2 * n
    adjacency = [[] for _ in range(N)]
    edges = []
    for layer in range(2):
        for i in range(n):
            for j in range(i + 1, n):
                u, v = layer * n + i, layer * n + j
                edges.append((u, v))
                adjacency[u].append(v)
                adjacency[v].append(u)
    for i in range(n):
        u, v = i, i + n
        edges.append((u, v))
        adjacency[u].append(v)
        adjacency[v].append(u)
    distances = []
    for u in range(N):
        d = [-1] * N
        d[u] = 0
        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    queue.append(y)
        assert all(value >= 0 for value in d)
        distances.append(d)
    codes = [tuple(min(distances[z][u], distances[z][v])
                   for z in range(N)) for (u, v) in edges]
    difference_masks = set()
    for i, one in enumerate(codes):
        for other in codes[:i]:
            mask = sum(1 << z for z in range(N) if one[z] != other[z])
            difference_masks.add(mask)
    dom_masks = set(sum(1 << z for z, d in enumerate(code) if d <= 1)
                    for code in codes)
    # Only inclusion-minimal hitting constraints are needed; computed independently.
    def remove_redundant(masks):
        minimal = []
        for mask in sorted(masks, key=int.bit_count):
            if not any(small & mask == small for small in minimal):
                minimal.append(mask)
        return minimal
    requirements = remove_redundant(difference_masks | dom_masks)
    target = n - 1 if n >= 7 else n
    found = 0
    for chosen in combinations(range(N), target):
        mask = sum(1 << v for v in chosen)
        actual = all(mask & required for required in requirements)
        proposed = predicted_basis(n, mask)
        assert actual == proposed, (n, chosen, actual, proposed)
        found += actual
    assert found == predicted_count(n), (n, found, predicted_count(n))
    print(f"n={n}: minimum={target}, bases={found}, checked={comb(N,target)}")


def main():
    for n in range(2, 12):
        check_one(n)
    print("VERIFY_OK: full candidate-space verification at minimum sizes n=2..11; "
          "graph-theoretic BFS and independent edge comparisons")


if __name__ == "__main__":
    main()
