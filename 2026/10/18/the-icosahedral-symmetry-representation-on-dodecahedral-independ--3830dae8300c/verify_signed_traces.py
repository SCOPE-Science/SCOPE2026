#!/usr/bin/env python3
"""Independent brute-force oriented-chain check for the dodecahedral character.

Requires Python >=3.9 and networkx >=2.8. Automorphisms are independently
enumerated as graph isomorphisms rather than generated from listed permutations.
"""
from collections import Counter
import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(20))
for t in range(10):
    G.add_edge(t, (t + 1) % 10)
    G.add_edge(t, 10 + t)
    G.add_edge(10 + t, 10 + (t + 2) % 10)
assert G.number_of_edges() == 30
bad = [sum(1 << w for w in G[v]) for v in G.nodes]

# Bottom-up, exhaustive 2^20 subset test, independent of the recursive enumerator.
valid = bytearray(1 << 20)
valid[0] = 1
all_faces = [[] for _ in range(8)]
for mask in range(1, 1 << 20):
    low = mask & -mask
    v = low.bit_length() - 1
    rest = mask - low
    if valid[rest] and not (rest & bad[v]):
        valid[mask] = 1
        all_faces[mask.bit_count() - 1].append(mask)
assert tuple(map(len, all_faces)) == (20,160,660,1510,1912,1240,320,5)

# Independently compute F2 ranks using rows indexed by lower simplices;
# each row is a bit vector of upper-simplex incidences.
ranks = []
for k in range(1, 8):
    idx = {f:j for j, f in enumerate(all_faces[k])}
    rows = []
    for lower in all_faces[k-1]:
        row = 0
        remaining = ((1<<20)-1) ^ lower
        while remaining:
            bit = remaining & -remaining
            upper = lower | bit
            if valid[upper]:
                row |= 1 << idx[upper]
            remaining ^= bit
        rows.append(row)
    piv = {}
    for row in rows:
        while row:
            b = row.bit_length()-1
            if b not in piv:
                piv[b] = row
                break
            row ^= piv[b]
    ranks.append(len(piv))
assert ranks == [19, 141, 519, 991, 921, 315, 5], ranks

perms = [tuple(p[i] for i in range(20))
         for p in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()]
assert len(perms) == len(set(perms)) == 120
all_nonempty = [f for Fs in all_faces for f in Fs]

def perm_order(p):
    seen=set()
    lengths=[]
    for j in range(20):
        if j in seen: continue
        k=j;c=0
        while k not in seen:
            seen.add(k);c+=1;k=p[k]
        lengths.append(c)
    from math import lcm
    return lcm(*lengths)

def direct_signed_trace(p):
    # Coefficient of an oriented simplex is the sign of its restricted
    # vertex permutation. Include the reduced empty-face contribution.
    ans = 1
    for face in all_nonempty:
        support = [j for j in range(20) if face & (1<<j)]
        images = [p[j] for j in support]
        if sum(1<<j for j in images) != face:
            continue
        parity = sum(images[i] > images[j] for i in range(len(images))
                     for j in range(i+1, len(images))) & 1
        ans += (-1 if len(images) & 1 else 1) * (-1 if parity else 1)
    return ans

counts = Counter((perm_order(p), direct_signed_trace(p)) for p in perms)
assert counts == {(1,4):1,(2,-4):1,(2,0):30,(3,1):20,
                  (5,-1):24,(6,-1):20,(10,1):24}, counts
print('VERIFY_OK')
print('f_vector:', [len(a) for a in all_faces])
print('row_boundary_ranks_mod_2:',ranks)
print('independently_enumerated_automorphisms:',len(perms))
print('direct_oriented_chain_character:',sorted(counts.items()))
