"""Independent bitset verification of connected-dominating-set exchanges in prisms.

Usage: python verify_direct.py
Exhaustively checks all subsets of size at most n for 6 <= n <= 11.
"""
from collections import Counter, deque
from itertools import combinations


def verify(n):
    nvertices = 2 * n
    adj = [0] * nvertices
    for i in range(nvertices):
        row, col = divmod(i, n)
        for j in (((col - 1) % n) + row * n,
                  ((col + 1) % n) + row * n,
                  col + (1 - row) * n):
            adj[i] |= 1 << j
    closed = [adj[i] | (1 << i) for i in range(nvertices)]
    full = (1 << nvertices) - 1

    def feasible(mask):
        cover = 0
        v = mask
        while v:
            b = v & -v
            cover |= closed[b.bit_length() - 1]
            v -= b
        if cover != full:
            return False
        reached = mask & -mask
        while True:
            extension = reached
            v = reached
            while v:
                b = v & -v
                extension |= adj[b.bit_length() - 1] & mask
                v -= b
            if extension == reached:
                return reached == mask
            reached = extension

    def masks_of_size(k):
        for verts in combinations(range(nvertices), k):
            mask = 0
            for v in verts:
                mask |= 1 << v
            yield mask

    assert not any(feasible(mask) for mask in masks_of_size(n - 1)), n
    all_sets = {mask for mask in masks_of_size(n) if feasible(mask)}
    assert len(all_sets) == 2*n*n + 2, (n, len(all_sets))
    edges = 0
    degrees = Counter()
    connected_seen = set()
    root = next(iter(all_sets))
    bfs = deque([root]); connected_seen.add(root)
    while bfs:
        state = bfs.popleft()
        selected = [v for v in range(nvertices) if (state >> v) & 1]
        missing = [v for v in range(nvertices) if not ((state >> v) & 1)]
        neighbors = set()
        for u in selected:
            base = state ^ (1 << u)
            for v in missing:
                alt = base | (1 << v)
                if alt in all_sets:
                    neighbors.add(alt)
        edges += len(neighbors)
        degrees[len(neighbors)] += 1
        for alt in neighbors:
            if alt not in connected_seen:
                connected_seen.add(alt)
                bfs.append(alt)
    assert len(connected_seen) == len(all_sets), (n, len(connected_seen))
    assert degrees == Counter({2*n:2, 6:4*n, 5:4*n, 4:2*n*(n-4)}), (n, degrees)
    assert edges//2 == 4*n*(n+2), (n, edges//2)
    print(f"n={n}: optimum={n}, configurations={len(all_sets)}, "
          f"exchange_edges={edges//2}, connected=yes")


if __name__ == '__main__':
    for n in range(6, 12):
        verify(n)
    print('DIRECT_ALL_SUBSETS_AND_EXCHANGES_PASS')
