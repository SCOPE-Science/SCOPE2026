from itertools import combinations, product
from collections import Counter, deque
from math import comb

def crown_graph(n):
    # A = 0,...,n-1; B = n,...,2n-1.
    # The nonedges across the bipartition are the matched pairs a_i b_i.
    N = 2*n
    adj = [set() for _ in range(N)]
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            u, v = i, n+j
            adj[u].add(v)
            adj[v].add(u)
            edges.append((u, v))
    return adj, edges

def all_distances(adj):
    D = []
    for s in range(len(adj)):
        d = [10**9]*len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D

def elem_distance(D, landmark, elem):
    typ, data = elem
    if typ == "v":
        return D[landmark][data]
    u, v = data
    return min(D[landmark][u], D[landmark][v])

def distinguisher_masks(D, edges):
    elems = [("v", v) for v in range(len(D))] + [("e", e) for e in edges]
    masks = []
    for x, y in combinations(elems, 2):
        mask = 0
        for s in range(len(D)):
            if elem_distance(D, s, x) != elem_distance(D, s, y):
                mask |= 1 << s
        masks.append(mask)
    return masks

def is_mixed_fault_tolerant(masks, S_mask):
    return all((S_mask & m).bit_count() >= 2 for m in masks)

def is_mixed_resolving(masks, S_mask):
    return all((S_mask & m) != 0 for m in masks)

def predicted_basis(n, S_mask):
    if S_mask.bit_count() != n:
        return False
    p = 0
    q = 0
    for i in range(n):
        ai = (S_mask >> i) & 1
        bi = (S_mask >> (n+i)) & 1
        if ai + bi != 1:
            return False
        p += ai
        q += bi
    return p == 0 or q == 0 or (p >= 4 and q >= 4)

def predicted_one_hole_mixed(n, S_mask):
    if S_mask.bit_count() != n-1:
        return False
    omitted = 0
    p = q = 0
    for i in range(n):
        ai = (S_mask >> i) & 1
        bi = (S_mask >> (n+i)) & 1
        if ai + bi == 0:
            omitted += 1
        elif ai + bi == 1:
            p += ai
            q += bi
        else:
            return False
    return omitted == 1 and (p == 0 or q == 0 or (p >= 3 and q >= 3))

subset_trials = 0
mft_bases_checked = 0
one_hole_trials = 0

for n in range(4, 10):
    adj, edges = crown_graph(n)
    D = all_distances(adj)
    masks = distinguisher_masks(D, edges)
    N = 2*n

    # Exhaustively reject every set smaller than n.
    for k in range(n):
        for S in combinations(range(N), k):
            subset_trials += 1
            mask = sum(1 << v for v in S)
            assert not is_mixed_fault_tolerant(masks, mask), (n, k, S)

    # Exhaustively classify every size-n candidate.
    actual = set()
    for S in combinations(range(N), n):
        subset_trials += 1
        mask = sum(1 << v for v in S)
        good = is_mixed_fault_tolerant(masks, mask)
        pred = predicted_basis(n, mask)
        assert good == pred, (n, S, good, pred)
        if good:
            actual.add(mask)

    if n <= 7:
        expected_count = 2
    else:
        expected_count = 2 + sum(comb(n, p) for p in range(4, n-3))
    assert len(actual) == expected_count, (n, len(actual), expected_count)
    mft_bases_checked += len(actual)

    # Independently verify the one-hole mixed-resolving lemma on every
    # omitted pair and every orientation of the remaining pairs.
    for h in range(n):
        remaining = [i for i in range(n) if i != h]
        for bits in product((0, 1), repeat=n-1):
            mask = 0
            for i, b in zip(remaining, bits):
                mask |= 1 << (i if b == 0 else n+i)
            one_hole_trials += 1
            good = is_mixed_resolving(masks, mask)
            pred = predicted_one_hole_mixed(n, mask)
            assert good == pred, (n, h, bits, good, pred)

print("VERIFY_OK")
print("crown_parameters_checked =", list(range(4, 10)))
print("subset_trials_size_at_most_n =", subset_trials)
print("minimum_mft_bases_checked =", mft_bases_checked)
print("one_hole_transversal_trials =", one_hole_trials)
print("all sets smaller than n failed mixed fault tolerance")
print("all size-n MFT bases matched the transversal/orientation theorem")
print("all one-hole transversals matched the mixed-resolving lemma")
