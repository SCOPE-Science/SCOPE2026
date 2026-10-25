"""Independent block-partition generator and swap graph check for T(n)."""
from collections import Counter, deque
from itertools import combinations
from math import factorial


def configurations(n):
    k, r = divmod(n, 3)
    options = ([(k, 0, 0)] if r == 0 else
               [(k, 0, 1), (k - 1, 2, 0)] if r == 1 else
               [(k, 1, 0)])
    result = set()
    for threes, pairs, singles in options:
        if threes < 0:
            continue
        def extend(unused, a, b, c, chosen):
            if not unused:
                assert a == b == c == 0
                result.add(frozenset(chosen))
                return
            v = min(unused)
            leftover = unused - {v}
            if a:
                for x, y in combinations(sorted(leftover), 2):
                    for center, leaf1, leaf2 in ((v, x, y), (x, v, y), (y, v, x)):
                        edge1 = tuple(sorted((center, leaf1)))
                        edge2 = tuple(sorted((center, leaf2)))
                        extend(leftover - {x, y}, a - 1, b, c, chosen | {edge1, edge2})
            if b:
                for x in sorted(leftover):
                    extend(leftover - {x}, a, b - 1, c, chosen | {tuple(sorted((v, x)))})
            if c:
                extend(leftover, a, b, c - 1, chosen)
        extend(set(range(n)), threes, pairs, singles, frozenset())
    return result


def verify(n):
    nodes = configurations(n)
    lookup = {s: i for i, s in enumerate(nodes)}
    all_edges = set(combinations(range(n), 2))
    graph = []
    for s in nodes:
        succ = set()
        for removed in s:
            for inserted in all_edges - s:
                key = (s - {removed}) | {inserted}
                if key in lookup:
                    succ.add(lookup[key])
        graph.append(succ)
    found = set(); comps = []
    for start in range(len(graph)):
        if start in found:
            continue
        found.add(start); todo = deque([start]); size = 0
        while todo:
            vertex = todo.popleft(); size += 1
            for u in graph[vertex]:
                if u not in found:
                    found.add(u); todo.append(u)
        comps.append(size)
    k, r = divmod(n, 3)
    if r == 0:
        expected_components = factorial(n) // (6 ** k * factorial(k))
        expected_component_size = 3 ** k
        assert len(comps) == expected_components
        assert all(x == expected_component_size for x in comps)
    else:
        assert len(comps) == 1
    return dict(n=n, configurations=len(nodes), components=len(comps), component_sizes=dict(sorted(Counter(comps).items())), degrees=dict(sorted(Counter(map(len, graph)).items())))

if __name__ == '__main__':
    for n in range(3, 10):
        print(verify(n))
    print('STRUCTURAL_PASS')
