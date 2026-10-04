#!/usr/bin/env python3
from collections import defaultdict
import json

V = tuple(range(8))
E = tuple((x, x ^ b) for x in V for b in (1,2,4) if x < (x ^ b))
assert len(E) == 12

by_size = defaultdict(list)
used_tail = [False] * 8
adj = [[] for _ in V]

def path_exists(start, target):
    stack = [start]
    seen = set()
    while stack:
        x = stack.pop()
        if x == target:
            return True
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj[x])
    return False

def rec(i, mask, size):
    if i == len(E):
        by_size[size].append(mask)
        return
    u, v = E[i]
    rec(i + 1, mask, size)
    # Pair vertex u with edge {u,v}; this directs u -> v in the V-path model.
    if not used_tail[u] and not path_exists(v, u):
        used_tail[u] = True
        adj[u].append(v)
        rec(i + 1, mask | (1 << (2*i)), size + 1)
        adj[u].pop()
        used_tail[u] = False
    # Pair vertex v with edge {u,v}; this directs v -> u.
    if not used_tail[v] and not path_exists(u, v):
        used_tail[v] = True
        adj[v].append(u)
        rec(i + 1, mask | (1 << (2*i + 1)), size + 1)
        adj[v].pop()
        used_tail[v] = False

rec(0, 0, 0)
counts = [len(by_size[k]) for k in range(1, 8)]
expected_counts = [24, 240, 1296, 4080, 7488, 7424, 3072]
assert counts == expected_counts, (counts, expected_counts)

# Independent brute-force enumeration of all 3^12 edge states.
# State 0 = absent; 1 = orientation from smaller endpoint to larger; 2 = reverse.
# Legality is checked from scratch, not through the recursive pruning above.
from itertools import product
brute_counts = [0] * 8
for state in product((0,1,2), repeat=len(E)):
    tails = set()
    dadj = [[] for _ in V]
    chosen = 0
    legal = True
    for j, st in enumerate(state):
        if st == 0:
            continue
        u, v = E[j]
        a, b = (u, v) if st == 1 else (v, u)
        if a in tails:
            legal = False
            break
        tails.add(a)
        dadj[a].append(b)
        chosen += 1
    if not legal:
        continue
    color = [0] * len(V)
    def dfs(x):
        color[x] = 1
        for y in dadj[x]:
            if color[y] == 1:
                return False
            if color[y] == 0 and not dfs(y):
                return False
        color[x] = 2
        return True
    if all(color[x] or dfs(x) for x in V):
        brute_counts[chosen] += 1
assert brute_counts == [1] + expected_counts, brute_counts

# Independent f-vector cross-check from the cube Laplacian spectrum
# 0^1, 2^3, 4^3, 6^1: det(L + t I)=t(t+2)^3(t+4)^3(t+6).
def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c
poly = [1]
for root, mult in [(0,1),(2,3),(4,3),(6,1)]:
    for _ in range(mult):
        poly = mul(poly, [root,1])
# coefficients t^1,...,t^7 are the face counts in reverse critical-edge indexing.
assert poly == [0,3072,7424,7488,4080,1296,240,24,1], poly
assert list(reversed(poly[1:-1])) == expected_counts

# Every codimension-one subset of an acyclic matching remains acyclic.
for k in range(2,8):
    lower = set(by_size[k-1])
    for mask in by_size[k]:
        x = mask
        while x:
            b = x & -x
            assert (mask ^ b) in lower
            x ^= b

# Full simplicial identity d^2=0 over F_2 by explicit cancellation on every face.
for k in range(3,8):
    for mask in by_size[k]:
        accum = set()
        x = mask
        while x:
            b = x & -x
            sub = mask ^ b
            y = sub
            while y:
                c = y & -y
                codim2 = sub ^ c
                if codim2 in accum:
                    accum.remove(codim2)
                else:
                    accum.add(codim2)
                y ^= c
            x ^= b
        assert not accum

def rank_bits_high(vectors):
    piv = {}
    for z in vectors:
        x = z
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)

def rank_bits_low(vectors):
    piv = {}
    for z in vectors:
        x = z
        while x:
            low = x & -x
            p = low.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)

ranks = {1: 1}  # augmented d_0 to C_{-1}
for k in range(2,8):
    lower_index = {m:i for i,m in enumerate(by_size[k-1])}
    columns = []
    rows = [0] * len(by_size[k-1])
    for j, mask in enumerate(by_size[k]):
        col = 0
        x = mask
        while x:
            b = x & -x
            i = lower_index[mask ^ b]
            col ^= (1 << i)
            rows[i] ^= (1 << j)
            x ^= b
        columns.append(col)
    r1 = rank_bits_high(columns)
    r2 = rank_bits_low(columns)
    r3 = rank_bits_high(rows)  # rank of transpose
    assert r1 == r2 == r3, (k, r1, r2, r3)
    ranks[k] = r1

expected_ranks = {1:1, 2:23, 3:217, 4:1079, 5:3001, 6:4487, 7:2933}
assert ranks == expected_ranks, ranks

betti = {}
for k in range(1,8):
    b = len(by_size[k]) - ranks[k] - ranks.get(k+1, 0)
    if b:
        betti[k-1] = b
assert betti == {5:4, 6:139}, betti

chi = sum(((-1)**i) * counts[i] for i in range(7))
reduced_chi = chi - 1
assert reduced_chi == 135
assert (-4 + 139) == reduced_chi

print(json.dumps({
    "graph":"Q3",
    "edges":len(E),
    "nonempty_face_vector":counts,
    "augmented_boundary_ranks_by_face_size":ranks,
    "reduced_mod2_betti":betti,
    "reduced_euler_characteristic":reduced_chi
}, sort_keys=True))
print("VERIFY_OK")
