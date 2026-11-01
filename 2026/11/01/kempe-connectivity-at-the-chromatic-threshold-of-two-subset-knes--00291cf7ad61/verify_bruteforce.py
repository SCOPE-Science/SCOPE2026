"""Independent exhaustive enumeration of optimal Kneser colorings for 4 <= n <= 7.

Only proper coloring constraints are used in the search.  The theorem's component
parameters are recovered afterward by inspecting the enumerated color classes.
Run: python3 verify_bruteforce.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def direct_enumeration(n):
    edges = tuple(combinations(range(n), 2))
    palette = n - 2
    assignment = [-1] * len(edges)
    classes = [[] for _ in range(palette)]
    solutions = []

    def search(i, used):
        if i == len(edges):
            if used == palette:
                solutions.append(tuple(assignment))
            return
        x, y = edges[i]
        for color in range(min(used + 1, palette)):
            if all(x in pair or y in pair for pair in classes[color]):
                assignment[i] = color
                classes[color].append((x, y))
                search(i + 1, max(used, color + 1))
                classes[color].pop()

    search(0, 0)
    expect = comb(n, 3) * (1 << comb(n - 3, 2))
    assert len(solutions) == expect, (n, len(solutions), expect)
    degree_counts = Counter()
    triangle_data = Counter()
    for coloring in solutions:
        buckets = [set() for _ in range(palette)]
        for i, c in enumerate(coloring):
            buckets[c].add(edges[i])
        triangles = []
        for color, b in enumerate(buckets):
            if len(b) == 3:
                endpoints = set(z for e in b for z in e)
                if len(endpoints) == 3:
                    triangles.append((color, tuple(sorted(endpoints))))
        assert len(triangles) == 1
        triangle_color, Q = triangles[0]
        S = tuple(x for x in range(n) if x not in Q)
        center_color = {}
        for center in S:
            spoke_colors = [coloring[edges.index(tuple(sorted((center, q))))] for q in Q]
            assert len(set(spoke_colors)) == 1
            assert spoke_colors[0] != triangle_color
            center_color[center] = spoke_colors[0]
        assert len(set(center_color.values())) == len(S)
        assert set(center_color.values()) | {triangle_color} == set(range(palette))
        triangle_data[(Q, triangle_color, tuple(sorted(center_color.items()))) ] += 1
        legal_changes = []
        for i, e in enumerate(edges):
            for newcolor in range(palette):
                if newcolor != coloring[i] and all(not (newcolor == coloring[j] and set(e).isdisjoint(other))
                                                     for j, other in enumerate(edges) if j != i):
                    legal_changes.append((e, newcolor))
        assert len(legal_changes) == comb(n - 3, 2)
        predicted = {(tuple(sorted((s, t))), center_color[s]) for s, t in combinations(S, 2)
                     if coloring[edges.index(tuple(sorted((s, t))))] == center_color[t]}
        predicted |= {(tuple(sorted((s, t))), center_color[t]) for s, t in combinations(S, 2)
                      if coloring[edges.index(tuple(sorted((s, t))))] == center_color[s]}
        assert set(legal_changes) == predicted
        degree_counts[len(legal_changes)] += 1
    print(f'DIRECT_PASS n={n} canonical={len(solutions)} predicted={expect} '
          f'degree={dict(degree_counts)} triangle_label_sectors={len(triangle_data)}')


for n in range(4, 8):
    direct_enumeration(n)
print('ALL_DIRECT_PASS')
