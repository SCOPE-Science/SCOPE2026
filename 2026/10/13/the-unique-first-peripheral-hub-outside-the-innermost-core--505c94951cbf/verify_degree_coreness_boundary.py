#!/usr/bin/env python3
from itertools import permutations
from collections import Counter

EXPECTED_CONNECTED = {2:1, 3:4, 4:38, 5:728, 6:26704, 7:1866256}
EXPECTED_FAILURES = {2:0, 3:0, 4:0, 5:0, 6:0, 7:420}

def edge_pairs(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def adjacency_from_mask(n, pairs, mask):
    adj = [0]*n
    mm = mask
    while mm:
        bit = mm & -mm
        e = bit.bit_length()-1
        i,j = pairs[e]
        adj[i] |= 1 << j
        adj[j] |= 1 << i
        mm -= bit
    return adj

def connected_bfs(adj, n):
    seen = 1
    frontier = 1
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length()-1
        new = adj[v] & ~seen
        seen |= new
        frontier |= new
    return seen == (1 << n) - 1

def connected_closure(adj, n):
    reach = [adj[i] | (1 << i) for i in range(n)]
    for k in range(n):
        kb = 1 << k
        rk = reach[k]
        for i in range(n):
            if reach[i] & kb:
                reach[i] |= rk
    full = (1 << n) - 1
    return all(x == full for x in reach)

def core_numbers_peeling(adj, n):
    rem = (1 << n) - 1
    deg = [a.bit_count() for a in adj]
    core = [None]*n
    level = 0
    while rem:
        best_v = None
        best_d = n+1
        rr = rem
        while rr:
            bit = rr & -rr
            rr -= bit
            v = bit.bit_length()-1
            if deg[v] < best_d:
                best_d = deg[v]
                best_v = v
        if best_d > level:
            level = best_d
        core[best_v] = level
        rem &= ~(1 << best_v)
        rr = adj[best_v] & rem
        while rr:
            bit = rr & -rr
            rr -= bit
            u = bit.bit_length()-1
            deg[u] -= 1
    return core

def kcore_mask_pruning(adj, n, k):
    rem = (1 << n) - 1
    changed = True
    while changed:
        changed = False
        rr = rem
        kill = 0
        while rr:
            bit = rr & -rr
            rr -= bit
            v = bit.bit_length()-1
            if (adj[v] & rem).bit_count() < k:
                kill |= bit
        if kill:
            rem &= ~kill
            changed = True
    return rem

def core_numbers_pruning(adj, n):
    out = [0]*n
    for k in range(1, n):
        rem = kcore_mask_pruning(adj, n, k)
        for v in range(n):
            if rem & (1 << v):
                out[v] = k
    return out

def failure(adj, n, core=None):
    deg = [a.bit_count() for a in adj]
    top = max(deg)
    leaders = [v for v,d in enumerate(deg) if d == top]
    if len(leaders) != 1:
        return False
    if core is None:
        core = core_numbers_peeling(adj, n)
    k = max(core)
    return core[leaders[0]] < k

def permute_mask(mask, maps):
    out = 0
    mm = mask
    while mm:
        bit = mm & -mm
        e = bit.bit_length()-1
        out |= 1 << maps[e]
        mm -= bit
    return out

def canonical_mask(n, mask):
    pairs = edge_pairs(n)
    idx = {e:i for i,e in enumerate(pairs)}
    best = None
    for p in permutations(range(n)):
        mp = []
        for i,j in pairs:
            a,b = sorted((p[i], p[j]))
            mp.append(idx[(a,b)])
        pm = permute_mask(mask, mp)
        if best is None or pm < best:
            best = pm
    return best

connected_counts = {}
failure_counts = {}
failure_masks_7 = []

for n in range(2, 8):
    pairs = edge_pairs(n)
    conn = 0
    bad = 0
    for mask in range(1 << len(pairs)):
        adj = adjacency_from_mask(n, pairs, mask)
        if not connected_bfs(adj, n):
            continue
        conn += 1
        core = core_numbers_peeling(adj, n)
        if failure(adj, n, core):
            bad += 1
            if n == 7:
                failure_masks_7.append(mask)
    connected_counts[n] = conn
    failure_counts[n] = bad

assert connected_counts == EXPECTED_CONNECTED, connected_counts
assert failure_counts == EXPECTED_FAILURES, failure_counts

# Independent validation on every order-7 failure.
pairs7 = edge_pairs(7)
for mask in failure_masks_7:
    adj = adjacency_from_mask(7, pairs7, mask)
    assert connected_closure(adj, 7)
    c1 = core_numbers_peeling(adj, 7)
    c2 = core_numbers_pruning(adj, 7)
    assert c1 == c2
    assert failure(adj, 7, c2)
    deg = sorted((a.bit_count() for a in adj), reverse=True)
    cores = sorted(c2, reverse=True)
    assert deg == [4,3,2,2,1,1,1]
    assert cores == [2,2,2,1,1,1,1]

# Canonicalize the complete first-failure set.
classes = Counter(canonical_mask(7, m) for m in failure_masks_7)
assert len(classes) == 1
rep, multiplicity = next(iter(classes.items()))
assert multiplicity == 420

rep_adj = adjacency_from_mask(7, pairs7, rep)
rep_edges = [pairs7[i] for i in range(len(pairs7)) if rep & (1 << i)]
assert rep_edges == [(0,1),(0,4),(0,5),(0,6),(1,2),(1,3),(2,3)]
assert [a.bit_count() for a in rep_adj] == [4,3,2,2,1,1,1]
assert core_numbers_peeling(rep_adj, 7) == [1,2,2,2,1,1,1]

# Orbit and automorphism checks.
orbit = set()
aut = 0
idx7 = {e:i for i,e in enumerate(pairs7)}
for p in permutations(range(7)):
    mp = []
    for i,j in pairs7:
        a,b = sorted((p[i],p[j]))
        mp.append(idx7[(a,b)])
    pm = permute_mask(rep, mp)
    orbit.add(pm)
    if pm == rep:
        aut += 1
assert len(orbit) == 420
assert aut == 12
assert orbit == set(failure_masks_7)

print("VERIFY_OK")
print("connected", connected_counts)
print("failures", failure_counts)
print("representative_edges", rep_edges)
print("orbit_size", len(orbit))
print("automorphism_group_order", aut)
