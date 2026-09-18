from itertools import combinations


def chromatic_edge_decomposition(n, edges):
    edges = [tuple(sorted(e)) for e in edges]
    conflict = [[False] * len(edges) for _ in edges]
    for i, e in enumerate(edges):
        for j in range(i):
            if set(e) & set(edges[j]):
                conflict[i][j] = conflict[j][i] = True
    degrees = [sum(v in e for e in edges) for v in range(n)]
    delta = max(degrees, default=0)
    order = sorted(range(len(edges)), key=lambda i: -sum(conflict[i]))

    def color_with(q):
        color = [-1] * len(edges)
        def search(t):
            if t == len(order):
                return True
            i = order[t]
            forbidden = {color[j] for j in range(len(edges)) if conflict[i][j] and color[j] >= 0}
            for c in range(q):
                if c not in forbidden:
                    color[i] = c
                    if search(t + 1):
                        return True
                    color[i] = -1
            return False
        if not search(0):
            return None
        classes = [[] for _ in range(q)]
        for i, e in enumerate(edges):
            classes[color[i]].append(e)
        return classes

    if not edges:
        return []
    for q in (delta, delta + 1):
        classes = color_with(q)
        if classes is not None:
            return classes
    raise RuntimeError("Vizing bound was not attained")


def verify(n, edges, a, b):
    edges = {tuple(sorted(e)) for e in edges}
    if a > b:
        a, b = b, a
    classes = chromatic_edge_decomposition(n, edges)
    q = len(classes)
    assert a >= q

    parts = []
    for i in range(a):
        for r, matching in enumerate(classes):
            j = (i + r) % a
            for x, y in matching:
                parts.append((('A', i, x), ('A', i, y), ('B', j, x), ('B', j, y)))
    for j in range(a, b):
        for r, matching in enumerate(classes):
            anchor = ('A', r, 0)
            for x, y in matching:
                parts.append((anchor, ('B', j, x), ('B', j, y)))

    graph_edges = set()
    for side, count in (('A', a), ('B', b)):
        for i in range(count):
            for x, y in edges:
                graph_edges.add(tuple(sorted(((side, i, x), (side, i, y)))))
    for i in range(a):
        for j in range(b):
            for x in range(n):
                for y in range(n):
                    graph_edges.add(tuple(sorted((('A', i, x), ('B', j, y)))))

    covered = set()
    for clique in parts:
        for e in combinations(clique, 2):
            e = tuple(sorted(e))
            assert e in graph_edges
            assert e not in covered
            covered.add(e)
    for e in graph_edges - covered:
        parts.append(e)
        covered.add(e)

    m = len(edges)
    expected = a * b * n * n - (2 * a + b) * m
    assert covered == graph_edges
    assert len(parts) == expected
    return q, len(parts)


def edge_set_path(n):
    return {(i, i + 1) for i in range(n - 1)}


def edge_set_cycle(n):
    return edge_set_path(n) | {(0, n - 1)}


def edge_set_complete(n):
    return set(combinations(range(n), 2))


cases = [
    ("P4", 4, edge_set_path(4)),
    ("C5", 5, edge_set_cycle(5)),
    ("K3", 3, edge_set_complete(3)),
    ("K4", 4, edge_set_complete(4)),
    ("K5", 5, edge_set_complete(5)),
]
for name, n, edges in cases:
    q = len(chromatic_edge_decomposition(n, edges))
    a, b = max(1, q), max(1, q) + 2
    q2, count = verify(n, edges, a, b)
    print(f"{name}: chi'={q2}, a={a}, b={b}, partition_size={count}, verified")
