from itertools import combinations
from collections import deque

def broom(handle, brush):
    # Path p_0 ... p_handle, and brush leaves w_1,...,w_brush adjacent to p_0.
    n = handle + brush + 1
    adj = [set() for _ in range(n)]
    for i in range(handle):
        adj[i].add(i+1)
        adj[i+1].add(i)
    leaves = list(range(handle+1, n))
    for w in leaves:
        adj[0].add(w)
        adj[w].add(0)
    return adj, leaves

def all_distances(adj):
    n = len(adj)
    D = []
    for s in range(n):
        d = [10**9]*n
        d[s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if d[y] == 10**9:
                    d[y] = d[x] + 1
                    q.append(y)
        D.append(d)
    return D

def outer_multiset_resolving(D, mask):
    seen = {}
    n = len(D)
    S = [s for s in range(n) if (mask >> s) & 1]
    for v in range(n):
        if (mask >> v) & 1:
            continue
        rep = tuple(sorted(D[v][s] for s in S))
        if rep in seen:
            return False
        seen[rep] = v
    return True

graphs = subsets = bases_checked = 0

for brush in range(3, 8):
    for handle in range(2, 9):
        adj, leaves = broom(handle, brush)
        D = all_distances(adj)
        n = len(adj)
        resolving_by_size = [[] for _ in range(n+1)]
        for mask in range(1 << n):
            subsets += 1
            if outer_multiset_resolving(D, mask):
                resolving_by_size[mask.bit_count()].append(mask)

        dim = next(k for k, arr in enumerate(resolving_by_size) if arr)
        assert dim == brush, (handle, brush, dim)

        bases = resolving_by_size[brush]
        expected = set()

        # All brush leaves.
        mask_all = sum(1 << w for w in leaves)
        expected.add(mask_all)

        # Omit one brush leaf and add one non-root path vertex p_j, 1 <= j <= handle.
        for omitted in leaves:
            leaf_mask = mask_all ^ (1 << omitted)
            for j in range(1, handle + 1):
                expected.add(leaf_mask | (1 << j))

        assert set(bases) == expected, (handle, brush, len(bases), len(expected))
        assert len(bases) == 1 + brush*handle
        bases_checked += len(bases)
        graphs += 1

print("VERIFY_OK")
print("broom_parameter_pairs_checked =", graphs)
print("vertex_subsets_checked =", subsets)
print("minimum_bases_checked =", bases_checked)
print("parameters brush = 3..7, handle = 2..8")
print("all outer multiset dimensions equal the brush size")
print("all minimum bases match the complete classification")
print("all basis counts equal 1 + brush*handle")
