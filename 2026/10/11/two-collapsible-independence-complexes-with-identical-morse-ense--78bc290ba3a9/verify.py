#!/usr/bin/env python3
"""Exact arithmetic certificate for two discrete-Morse ensemble counterexamples."""
N = 11
TREE_A = ((0, 1), (0, 6), (1, 2), (2, 3), (3, 4), (3, 5),
          (6, 7), (6, 9), (7, 8), (9, 10))
TREE_B = ((0, 1), (0, 6), (1, 2), (2, 3), (2, 5), (3, 4),
          (6, 7), (6, 10), (7, 8), (8, 9))
LAPLACIAN_COEFFICIENTS = (1, -20, 169, -788, 2223, -3916,
                          4295, -2838, 1051, -188, 11, 0)
MATCHING_A = (1, 10, 34, 46, 23, 2)
MATCHING_B = (1, 10, 34, 46, 23, 3)


def laplacian(edges):
    assert len(edges) == N - 1 and len(set(edges)) == N - 1
    A = [[0 for _ in range(N)] for _ in range(N)]
    for u, v in edges:
        assert 0 <= u < v < N
        A[u][u] += 1
        A[v][v] += 1
        A[u][v] -= 1
        A[v][u] -= 1
    visited, pending = {0}, [0]
    while pending:
        u = pending.pop()
        for v in range(N):
            if v not in visited and A[u][v] == -1:
                visited.add(v)
                pending.append(v)
    assert len(visited) == N, "must be a tree"
    return A


def characteristic_coefficients(A):
    """Compute det(x I - A) by exact trace/Newton identities."""
    n = len(A)
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    traces, coefficients = [0], [1]
    for k in range(1, n + 1):
        P = [[sum(P[i][h] * A[h][j] for h in range(n))
              for j in range(n)] for i in range(n)]
        traces.append(sum(P[i][i] for i in range(n)))
        numerator = -sum(coefficients[k - r] * traces[r]
                         for r in range(1, k + 1))
        assert numerator % k == 0
        coefficients.append(numerator // k)
    return tuple(coefficients)


def matching_counts(edges):
    counts = [0] * (len(edges) // 2 + 1)
    for mask in range(1 << len(edges)):
        used, size, valid = 0, 0, True
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                bitset = (1 << u) | (1 << v)
                if bitset & used:
                    valid = False
                    break
                used |= bitset
                size += 1
        if valid:
            counts[size] += 1
    return tuple(counts)


def rooted_forest_coefficients(edges):
    """Independent weighted-forest expansion of det(t I + Laplacian)."""
    result = [0] * (N + 1)
    for mask in range(1 << len(edges)):
        parent = list(range(N))
        size = [1] * N
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                a, b = root(u), root(v)
                assert a != b  # each selected subset of a tree is a forest
                parent[a] = b
                size[b] += size[a]
        roots = [v for v in range(N) if parent[v] == v]
        weighted = 1
        for v in roots:
            weighted *= size[v]
        result[len(roots)] += weighted
    return tuple(result)


def count_colorings_of_complement(edges, colors=6):
    """Enumerate proper labelled colorings of the complement directly."""
    edges_set = {tuple(sorted(edge)) for edge in edges}
    neighbours = [set() for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            if (u, v) not in edges_set:
                neighbours[u].add(v)
                neighbours[v].add(u)
    order = sorted(range(N), key=lambda v: (-len(neighbours[v]), v))
    chosen = [-1] * N
    def rec(k):
        if k == N:
            return 1
        v = order[k]
        forbidden = {chosen[w] for w in neighbours[v] if chosen[w] >= 0}
        total = 0
        for color in range(colors):
            if color not in forbidden:
                chosen[v] = color
                total += rec(k + 1)
        chosen[v] = -1
        return total
    return rec(0)


def verify():
    poly_a = characteristic_coefficients(laplacian(TREE_A))
    poly_b = characteristic_coefficients(laplacian(TREE_B))
    assert poly_a == poly_b == LAPLACIAN_COEFFICIENTS
    matches_a = matching_counts(TREE_A)
    matches_b = matching_counts(TREE_B)
    assert matches_a == MATCHING_A and matches_b == MATCHING_B
    assert matches_a[:-1] == matches_b[:-1]
    assert matches_b[-1] - matches_a[-1] == 1
    for edges in (TREE_A, TREE_B):
        forest = rooted_forest_coefficients(edges)
        det_positive = tuple((-1)**(N-k) * LAPLACIAN_COEFFICIENTS[N-k]
                             for k in range(N+1))
        assert forest == det_positive, (forest, det_positive)
    assert count_colorings_of_complement(TREE_A) == 1440
    assert count_colorings_of_complement(TREE_B) == 2160
    print('Laplacian charpoly coefficients:', poly_a)
    print('Tree matching counts:', matches_a, matches_b)
    print('Six-colorings of the complement graphs:', 1440, 2160)
    print('Exact chromatic polynomial difference: q(q-1)(q-2)(q-3)(q-4)(q-5)')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
