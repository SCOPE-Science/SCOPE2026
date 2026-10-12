from collections import deque
from math import comb


def crown_graph(n):
    # Vertices 0..n-1 are a_i and n..2n-1 are b_i.
    N = 2 * n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                u, v = i, n + j
                adj[u].add(v)
                adj[v].add(u)
    return adj


def distances(adj):
    N = len(adj)
    out = []
    for s in range(N):
        d = [-1] * N
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        out.append(d)
    return out


def is_dtd(mask, adj, dist):
    N = len(adj)
    for v in range(N):
        if any(mask >> u & 1 for u in adj[v]):
            continue
        d2 = sum(1 for u in range(N) if (mask >> u) & 1 and dist[v][u] == 2)
        if d2 < 2:
            return False
    return True


def predicted(mask, n):
    I = {i for i in range(n) if (mask >> i) & 1}
    J = {j for j in range(n) if (mask >> (n + j)) & 1}
    k = len(I) + len(J)
    if k >= 4:
        return True
    if k <= 2:
        return False
    # k == 3
    if len(I) in (0, 3):
        return True
    if len(I) == 2:
        (j,) = tuple(J)
        return j not in I
    # len(I) == 1 and len(J) == 2
    (i,) = tuple(I)
    return i not in J


def expected_coeff(n, k):
    if k < 3:
        return 0
    if k == 3:
        return 4 * n * (n - 1) * (n - 2) // 3
    return comb(2 * n, k)


def main():
    subset_checks = 0
    dtd_sets = 0
    criterion_checks = 0
    coefficient_checks = 0
    distance_checks = 0
    minimum_checks = 0
    for n in range(3, 10):
        adj = crown_graph(n)
        dist = distances(adj)
        # Check the exact crown distance table independently.
        for i in range(n):
            for j in range(n):
                assert dist[i][n + j] == (3 if i == j else 1)
                assert dist[i][j] == (0 if i == j else 2)
                assert dist[n + i][n + j] == (0 if i == j else 2)
                distance_checks += 3
        hist = [0] * (2 * n + 1)
        for mask in range(1 << (2 * n)):
            subset_checks += 1
            actual = is_dtd(mask, adj, dist)
            pred = predicted(mask, n)
            assert actual == pred, (n, mask, actual, pred)
            criterion_checks += 1
            if actual:
                k = mask.bit_count()
                hist[k] += 1
                dtd_sets += 1
        for k, count in enumerate(hist):
            assert count == expected_coeff(n, k), (n, k, count, expected_coeff(n, k))
            coefficient_checks += 1
        assert next(k for k, c in enumerate(hist) if c) == 3
        assert hist[3] == 4 * n * (n - 1) * (n - 2) // 3
        minimum_checks += 2
    print(
        'VERIFY_OK '
        f'n_range=3..9 subset_checks={subset_checks} '
        f'dtd_sets={dtd_sets} criterion_checks={criterion_checks} '
        f'distance_checks={distance_checks} coefficient_checks={coefficient_checks} '
        f'minimum_checks={minimum_checks} max_order=18'
    )


if __name__ == '__main__':
    main()
