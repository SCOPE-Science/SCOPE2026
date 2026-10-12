#!/usr/bin/env python3
from collections import deque
from itertools import combinations


def graph(n):
    N = 2*n
    adj = [[] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                u, v = i, n+j
                adj[u].append(v)
                adj[v].append(u)
    return adj


def distances(adj):
    N = len(adj)
    D = [[None]*N for _ in range(N)]
    for s in range(N):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s][v] is None:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D


def pairmask(n, i, j):
    return (1 << i) | (1 << (n+i)) | (1 << j) | (1 << (n+j))


def expected_profile(n, k, mask):
    c = [((mask >> i) & 1) + ((mask >> (n+i)) & 1) for i in range(n)]
    if k == 1:
        return c.count(0) == 1 and c.count(1) == n-1
    if k == 2:
        return c.count(1) == n
    if k == 3:
        return c.count(1) == 1 and c.count(2) == n-1
    if k == 4:
        return c.count(2) == n
    raise ValueError(k)


def main():
    subset_checks = 0
    basis_checks = 0
    distance_pair_checks = 0
    expected_dims = {1: lambda n:n-1, 2:lambda n:n, 3:lambda n:2*n-1, 4:lambda n:2*n}
    expected_counts = {1:lambda n:n*(2**(n-1)), 2:lambda n:2**n, 3:lambda n:2*n, 4:lambda n:1}

    for n in range(3, 10):
        adj = graph(n)
        D = distances(adj)
        N = 2*n
        dsets = []
        for x, y in combinations(range(N), 2):
            dm = 0
            for z in range(N):
                if D[x][z] != D[y][z]:
                    dm |= 1 << z
            sx, ix = (0, x) if x < n else (1, x-n)
            sy, iy = (0, y) if y < n else (1, y-n)
            if sx == sy:
                assert ix != iy
                assert dm == pairmask(n, ix, iy)
            else:
                assert dm == (1 << N) - 1
            dsets.append(dm)
            distance_pair_checks += 1
        assert min(m.bit_count() for m in dsets) == 4

        same_masks = [pairmask(n, i, j) for i, j in combinations(range(n), 2)]
        for k in range(1, 5):
            best = N+1
            count = 0
            bases = []
            for mask in range(1 << N):
                subset_checks += 1
                size = mask.bit_count()
                if size > best:
                    continue
                ok = all((mask & dm).bit_count() >= k for dm in same_masks)
                if not ok:
                    continue
                # Opposite-side pairs have full distinctive set, and size >= k follows
                # from the same-side constraints for n >= 3.
                if size < best:
                    best = size
                    count = 0
                    bases = []
                if size == best:
                    count += 1
                    bases.append(mask)
            assert best == expected_dims[k](n), (n, k, best)
            assert count == expected_counts[k](n), (n, k, count)
            for mask in bases:
                basis_checks += 1
                assert expected_profile(n, k, mask), (n, k, mask)

    print(f"VERIFY_OK n_range=3..9 subset_checks={subset_checks} basis_checks={basis_checks} distance_pair_checks={distance_pair_checks} max_order=18")

if __name__ == '__main__':
    main()
