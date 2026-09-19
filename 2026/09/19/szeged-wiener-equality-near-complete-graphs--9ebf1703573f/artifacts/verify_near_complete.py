from collections import deque


def build_graph(a, b, c, d, xy):
    q = a + b + c + d
    x, y = q, q + 1
    adj = [set() for _ in range(q + 2)]
    for u in range(q):
        for v in range(u + 1, q):
            adj[u].add(v)
            adj[v].add(u)
    a_only = range(0, a)
    b_only = range(a, a + b)
    both = range(a + b, a + b + c)
    A = set(a_only) | set(both)
    B = set(b_only) | set(both)
    for u in A:
        adj[x].add(u)
        adj[u].add(x)
    for u in B:
        adj[y].add(u)
        adj[u].add(y)
    if xy:
        adj[x].add(y)
        adj[y].add(x)
    return adj


def distances(adj):
    n = len(adj)
    out = []
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        out.append(dist)
    return out


def eta_direct(adj):
    D = distances(adj)
    if any(-1 in row for row in D):
        return None
    n = len(adj)
    W = sum(D[u][v] for u in range(n) for v in range(u + 1, n))
    Sz = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                nu = sum(D[z][u] < D[z][v] for z in range(n))
                nv = sum(D[z][v] < D[z][u] for z in range(n))
                Sz += nu * nv
    return Sz - W


def eta_formula(a, b, c, d, xy):
    if xy:
        return (
            8 * a * b + 2 * a * c + 3 * a * d
            + 2 * b * c + 3 * b * d + 4 * c * d - 4 * d
        )
    if c > 0:
        return (
            5 * a * b + 2 * a * c + 2 * a * d - 2 * a
            + 2 * b * c + 2 * b * d - 2 * b
            + 4 * c * d + 2 * c - 4 * d - 2
        )
    return 5 * a * b + 2 * a * d - a + 2 * b * d - b - 4 * d - 3


def connected(adj, omitted=None):
    vertices = [v for v in range(len(adj)) if v != omitted]
    if not vertices:
        return True
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v != omitted and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(vertices)


def two_connected(adj):
    return len(adj) >= 3 and connected(adj) and all(
        connected(adj, v) for v in range(len(adj))
    )


def two_connected_criterion(a, b, c, xy):
    if xy:
        return a + c >= 1 and b + c >= 1 and a + b + c >= 2
    return a + c >= 2 and b + c >= 2


formula_cases = 0
connectivity_cases = 0
for q in range(2, 11):
    for a in range(q + 1):
        for b in range(q - a + 1):
            for c in range(q - a - b + 1):
                d = q - a - b - c
                if a + c == 0 or b + c == 0:
                    continue
                for xy in (False, True):
                    adj = build_graph(a, b, c, d, xy)
                    direct = eta_direct(adj)
                    formula = eta_formula(a, b, c, d, xy)
                    assert direct == formula, (q, a, b, c, d, xy, direct, formula)
                    formula_cases += 1
                    assert two_connected(adj) == two_connected_criterion(a, b, c, xy)
                    connectivity_cases += 1

classification_cases = 0
for q in range(8, 41):
    found = set()
    for a in range(q + 1):
        for b in range(q - a + 1):
            for c in range(q - a - b + 1):
                d = q - a - b - c
                for xy in (False, True):
                    if not two_connected_criterion(a, b, c, xy):
                        continue
                    if eta_formula(a, b, c, d, xy) == 2 * (q + 2):
                        found.add((a, b, c, d, xy))
                    classification_cases += 1
    expected = {(1, 1, 0, q - 2, True)}
    if q == 8:
        expected |= {
            (0, 1, 1, 6, True),
            (1, 0, 1, 6, True),
        }
    assert found == expected, (q, found, expected)

print(f"direct_formula_cases={formula_cases}")
print(f"two_connectivity_cases={connectivity_cases}")
print(f"classification_parameter_cases={classification_cases}")
print("all_checks=PASS")
