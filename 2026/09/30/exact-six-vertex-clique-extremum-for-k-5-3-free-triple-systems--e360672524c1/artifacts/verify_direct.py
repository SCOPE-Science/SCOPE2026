#!/usr/bin/env python3
import itertools
from collections import Counter

V = range(6)
triples = list(itertools.combinations(V, 3))
index = {t:i for i,t in enumerate(triples)}

five_masks = []
for S in itertools.combinations(V, 5):
    m = 0
    for t in itertools.combinations(S, 3):
        m |= 1 << index[t]
    five_masks.append(m)

four_masks = []
for S in itertools.combinations(V, 4):
    m = 0
    for t in itertools.combinations(S, 3):
        m |= 1 << index[t]
    four_masks.append(m)

best = -1
extremal = []
for H in range(1 << 20):
    if any((H & m) == m for m in five_masks):
        continue
    edges = H.bit_count()
    k4 = sum((H & m) == m for m in four_masks)
    total_cliques = 22 + edges + k4
    if total_cliques > best:
        best = total_cliques
        extremal = [H]
    elif total_cliques == best:
        extremal.append(H)

perms = list(itertools.permutations(V))
maps = []
for p in perms:
    mp = []
    for t in triples:
        mp.append(index[tuple(sorted(p[x] for x in t))])
    maps.append(mp)

def permute_mask(mask, mp):
    out = 0
    for i in range(20):
        if (mask >> i) & 1:
            out |= 1 << mp[i]
    return out

def canonical(mask):
    return min(permute_mask(mask, mp) for mp in maps)

classes = Counter(canonical(H) for H in extremal)
assert best == 49
assert len(extremal) == 10
assert len(classes) == 1
rep = next(iter(classes))
missing = [triples[i] for i in range(20) if not ((rep >> i) & 1)]
assert len(missing) == 2
assert set(missing[0]).isdisjoint(missing[1])
print('VERIFY_OK direct: maximum=49 labeled_extremizers=10 isomorphism_types=1')
