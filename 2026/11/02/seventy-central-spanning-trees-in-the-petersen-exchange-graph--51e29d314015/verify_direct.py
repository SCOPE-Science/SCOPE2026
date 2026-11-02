"""Independent enumeration of Petersen spanning-tree exchange distances."""
from itertools import combinations
from collections import Counter

V = list(combinations(range(5), 2))
E = [(i, j) for i in range(10) for j in range(i + 1, 10)
     if not set(V[i]) & set(V[j])]
assert len(V) == 10 and len(E) == 15

def rank(mask):
    parent = list(range(10)); ncomp = 10
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for i, (a,b) in enumerate(E):
        if mask & (1 << i):
            a, b = root(a), root(b)
            if a != b:
                parent[a] = b
                ncomp -= 1
    return 10-ncomp

TREE = [mask for mask in range(1 << 15)
        if mask.bit_count() == 9 and rank(mask) == 9]
assert len(TREE) == 2000

pair = Counter()
for i, a in enumerate(TREE):
    for b in TREE[i+1:]:
        pair[9 - (a & b).bit_count()] += 1
assert [pair[d] for d in range(1,7)] == [28140,222360,651080,748200,314220,35000]
assert sum(pair.values()) == 1999000
assert sum(d * pair[d] for d in pair) == 7200000

central = Counter()
for t in TREE:
    co = ((1 << 15) - 1) ^ t
    r = rank(co)
    assert r in (5,6)
    central[r] += 1
assert central == {5:70, 6:1930}

# Count every distinct 5- or 6-cycle by its edge set.
cyc = {5: [], 6: []}
for size in (5,6):
    for I in combinations(range(15),size):
        mask = sum(1 << i for i in I)
        degree = [0]*10
        for i in I:
            a,b = E[i]; degree[a] += 1; degree[b] += 1
        if all(d in (0,2) for d in degree) and sum(d==2 for d in degree)==size and rank(mask)==size-1:
            cyc[size].append(mask)
assert len(cyc[5]) == 12 and len(cyc[6]) == 10
center_types = Counter()
for t in TREE:
    co = ((1 << 15) - 1) ^ t
    if rank(co)==5:
        cycles = [k for k in (5,6) for c in cyc[k] if (c & co) == c]
        assert len(cycles) == 1
        center_types[cycles[0]] += 1
assert center_types == {5:60, 6:10}
print('DIRECT_ENUMERATION_PASS trees=2000 pairdist=', [pair[d] for d in range(1,7)],
      'radius=5 diameter=6 centers=70 (60 pentagon/10 hexagon)')
