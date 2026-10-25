"""Reproducible exact checks for the Paley-11 tournament out-neighborhood complex.
Python 3.10+; standard library only. Run: python PALEY11_VERIFY.py
"""
import collections
import random

P = 11
RESIDUES = {x*x % P for x in range(1, P)}
assert RESIDUES == {1, 3, 4, 5, 9}
FACETS = [sum(1 << ((v+r) % P) for r in RESIDUES) for v in range(P)]
FACES = set()
for facet in FACETS:
    mask = facet
    while mask:
        FACES.add(mask)
        mask = (mask-1) & facet
assert len(FACES) == 242
assert len(FACETS) == 11 and len(set(FACETS)) == 11
fvector = collections.Counter(mask.bit_count()-1 for mask in FACES)
assert [fvector[j] for j in range(5)] == [11, 55, 110, 55, 11]

# Find a complete acyclic matching on the nonempty-face poset.
# Each coface is an immediate (codimension-one) coface.
rng = random.Random(0)
alive = set(FACES)
critical, matched = [], []
while alive:
    upper = collections.defaultdict(list)
    for big in alive:
        x = big
        while x:
            bit = x & -x
            x -= bit
            small = big ^ bit
            if small in alive:
                upper[small].append(big)
    free_pairs = [(s, bigger[0]) for s, bigger in upper.items()
                  if len(bigger) == 1]
    if free_pairs:
        small, big = rng.choice(free_pairs)
        assert big.bit_count() == small.bit_count()+1
        matched.append((small, big))
        alive.remove(small)
        alive.remove(big)
    else:
        maximal = [mask for mask in alive if mask not in upper]
        max_size = max(mask.bit_count() for mask in maximal)
        top = [mask for mask in maximal if mask.bit_count() == max_size]
        mask = rng.choice(top)
        critical.append(mask)
        alive.remove(mask)
assert len(matched) == 110
assert collections.Counter(m.bit_count()-1 for m in critical) == {0: 1, 2: 21}
assert set(critical).isdisjoint({x for pair in matched for x in pair})
assert set(critical) | {x for pair in matched for x in pair} == FACES

# Acyclicity certificate: topologically sort the FULL directed Hasse graph.
paired = set(matched)
adjacency = {x: [] for x in FACES}
indegree = {x: 0 for x in FACES}
edge_count = 0
for big in FACES:
    bits = big
    while bits:
        bit = bits & -bits
        bits -= bit
        small = big ^ bit
        if small not in FACES:
            continue
        source, target = ((big, small) if (small, big) in paired
                          else (small, big))
        adjacency[source].append(target)
        indegree[target] += 1
        edge_count += 1
assert edge_count == 715
queue = collections.deque(x for x in FACES if indegree[x] == 0)
seen = 0
while queue:
    u = queue.popleft()
    seen += 1
    for v in adjacency[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert seen == len(FACES), 'A cycle exists in the reversed-matching Hasse graph'

# Signed fixed-face Lefschetz characters. Empty simplex contributes -1.
FACES_WITH_EMPTY = FACES | {0}
def signed_trace(permutation):
    total = 0
    for simplex in FACES_WITH_EMPTY:
        image = 0
        sequence = []
        bits = simplex
        while bits:
            bit = bits & -bits
            bits -= bit
            old_index = bit.bit_length()-1
            target = permutation[old_index]
            image |= 1 << target
            sequence.append(target)
        if image != simplex:
            continue
        inversions = sum(sequence[i] > sequence[j]
                         for i in range(len(sequence))
                         for j in range(i+1, len(sequence)))
        exponent = simplex.bit_count()-1 + inversions
        total += -1 if exponent % 2 else 1
    return total

by_type = collections.defaultdict(list)
for multiplier in sorted(RESIDUES):
    for offset in range(P):
        perm = [(multiplier*x+offset) % P for x in range(P)]
        mapped_facets = {sum(1 << perm[i] for i in range(P) if f & (1 << i))
                         for f in FACETS}
        assert mapped_facets == set(FACETS)
        assert {perm[(x+r) % P] for r in RESIDUES} == {
            (perm[x]+multiplier*r) % P for r in RESIDUES}
        kind = ('identity' if multiplier == 1 and offset == 0
                else 'translation' if multiplier == 1
                else 'affine_nontranslation')
        by_type[kind].append(signed_trace(perm))
assert [(len(by_type[k]), set(by_type[k])) for k in
        ('identity','translation','affine_nontranslation')] == [
            (1,{21}), (10,{-1}), (44,{1})]
assert (21+10*(-1)+44*1)//55 == 1
assert 21+10*(-1)+44*1 == 55
print('PALEY11_CERTIFICATE_PASSED: 242 faces; 715 covers; 110 pairs; '
      'critical (1 vertex,21 triangles); 55 affine signed traces (21,-1,1)')
