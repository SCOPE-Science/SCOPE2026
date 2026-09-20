from math import floor, sqrt


def add_edge(adj, u, v):
    adj[u].add(v)
    adj[v].add(u)


def complete(adj, U, V):
    for u in U:
        for v in V:
            add_edge(adj, u, v)


def bipartite_gadget(t, p, X, Y):
    """Return the minimum-edge gadget used in the construction."""
    L = p + t
    edges = set()
    for j, y in enumerate(Y):
        for z in range(j * t, j * t + t):
            edges.add((X[z % L], y))

    target = 2 * t - p
    deg = {x: 0 for x in X}
    for x, _ in edges:
        deg[x] += 1

    for x in X:
        need = target - deg[x]
        if need <= 0:
            continue
        used = {y for xx, y in edges if xx == x}
        for y in Y:
            if y not in used and need:
                edges.add((x, y))
                need -= 1
        assert need == 0
    return edges


def build_graph(t, p, q, n):
    assert t <= p <= 2 * t
    assert t <= q <= 2 * t
    assert n >= p + q + 3 * t

    A1 = [("A1", i) for i in range(p)]
    A2 = [("A2", i) for i in range(n - p - q)]
    A3 = [("A3", i) for i in range(q)]
    B1 = [("B1", i) for i in range(p + t)]
    B2 = [("B2", i) for i in range(t)]
    B3 = [("B3", i) for i in range(n - p - 2 * t)]
    C1 = [("C1", i) for i in range(q + t)]
    C2 = [("C2", i) for i in range(t)]
    C3 = [("C3", i) for i in range(n - q - 2 * t)]

    A = A1 + A2 + A3
    B = B1 + B2 + B3
    C = C1 + C2 + C3
    vertices = A + B + C
    adj = {v: set() for v in vertices}

    complete(adj, A1, B)
    complete(adj, A1, C2)
    complete(adj, A2, B2 + B3)
    complete(adj, A2, C2 + C3)
    complete(adj, A3, C)
    complete(adj, A3, B2)
    complete(adj, B1, C1 + C3)
    complete(adj, B3, C1)

    E1 = bipartite_gadget(t, p, B1, C2)
    E2 = bipartite_gadget(t, q, C1, B2)
    for u, v in E1 | E2:
        add_edge(adj, u, v)

    return adj, (A, B, C), len(E1), len(E2)


def triangle_count(adj, parts):
    A, B, C = (set(P) for P in parts)
    total = 0
    for a in A:
        nbB = adj[a] & B
        nbC = adj[a] & C
        for b in nbB:
            total += len(adj[b] & nbC)
    return total


def F(t, p):
    return p * max(t * t, (p + t) * (2 * t - p))


def check_instance(t, p, q, n):
    adj, parts, e1, e2 = build_graph(t, p, q, n)
    assert [len(P) for P in parts] == [n, n, n]
    assert min(len(adj[v]) for v in adj) >= n + t
    expected_e1 = max(t * t, (p + t) * (2 * t - p))
    expected_e2 = max(t * t, (q + t) * (2 * t - q))
    assert e1 == expected_e1
    assert e2 == expected_e2
    observed = triangle_count(adj, parts)
    expected = F(t, p) + F(t, q)
    assert observed == expected


def main():
    graph_checks = 0
    for t in range(1, 13):
        for p in range(t, 2 * t + 1):
            for q in range(t, 2 * t + 1):
                n0 = p + q + 3 * t
                for n in (n0, n0 + 3):
                    check_instance(t, p, q, n)
                    graph_checks += 1

    threshold_checks = 0
    for t in range(2, 5001):
        p0 = floor(sqrt(2) * t) + 1
        assert t <= p0 <= 2 * t
        assert F(t, p0) < 2 * t ** 3
        assert F(t, t) == 2 * t ** 3
        for p in range(t, p0):
            assert F(t, p) >= 2 * t ** 3
        # Thus p+q < t+p0 cannot beat 4t^3 inside this two-parameter family.
        threshold_checks += 1

    print(f"graph construction checks: {graph_checks}")
    print(f"threshold arithmetic checks: {threshold_checks}")
    print("all checks passed")


if __name__ == "__main__":
    main()
