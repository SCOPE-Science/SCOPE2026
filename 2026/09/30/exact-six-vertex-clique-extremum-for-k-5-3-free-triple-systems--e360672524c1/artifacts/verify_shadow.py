#!/usr/bin/env python3
import itertools

V = range(6)
triples = list(itertools.combinations(V, 3))
pairs = list(itertools.combinations(V, 2))
pair_index = {p:i for i,p in enumerate(pairs)}

vertex_masks = []
shadow_masks = []
for G in triples:
    vm = sum(1 << v for v in G)
    sm = 0
    for p in itertools.combinations(G, 2):
        sm |= 1 << pair_index[p]
    vertex_masks.append(vm)
    shadow_masks.append(sm)

best = 10**9
witnesses = []
for fam in range(1, 1 << 20):
    union = 0
    shadow = 0
    x = fam
    while x:
        bit = x & -x
        i = bit.bit_length() - 1
        x -= bit
        union |= vertex_masks[i]
        shadow |= shadow_masks[i]
    if union != (1 << 6) - 1:
        continue
    score = fam.bit_count() + shadow.bit_count()
    if score < best:
        best = score
        witnesses = [fam]
    elif score == best:
        witnesses.append(fam)

assert best == 8
assert len(witnesses) == 10
for fam in witnesses:
    members = [triples[i] for i in range(20) if (fam >> i) & 1]
    assert len(members) == 2
    assert set(members[0]).isdisjoint(members[1])
assert 57 - best == 49
print('VERIFY_OK shadow: min_family_plus_shadow=8 maximum_cliques=49 witnesses=10')
