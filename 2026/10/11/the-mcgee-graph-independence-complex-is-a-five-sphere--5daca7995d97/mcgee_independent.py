"""Independent checks for the McGee graph independence-complex calculation.

Deletion/contraction recurrence for the independence polynomial; independent
fixed-cardinality face generation and exact mod-two chain ranks.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

n = 24
shifts = [12, 7, -7] * 8
neighbors = [set() for _ in range(n)]
for i in range(n):
    for j in ((i + 1) % n, (i + shifts[i]) % n):
        neighbors[i].add(j)
        neighbors[j].add(i)
adj = [sum(1 << j for j in v) for v in neighbors]

@lru_cache(maxsize=None)
def poly(available):
    if available == 0:
        return (1,)
    lowbit = available & -available
    v = lowbit.bit_length() - 1
    a = poly(available ^ lowbit)
    b = poly((available ^ lowbit) & ~adj[v])
    result = [0] * max(len(a), len(b) + 1)
    for k, val in enumerate(a):
        result[k] += val
    for k, val in enumerate(b):
        result[k + 1] += val
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)

expected = (1, 24, 240, 1304, 4212, 8328, 10024, 7072, 2668, 424, 8)
assert poly((1 << n) - 1) == expected
assert sum((-1) ** k * v for k, v in enumerate(expected)) == 1

# Independently enumerate by fixed cardinality; use all boundaries over F_2.
by_cardinality = {0: [0]}
for k in range(1, 11):
    current = []
    for vertex_set in combinations(range(n), k):
        m = 0
        for v in vertex_set:
            if m & adj[v]:
                break
            m |= 1 << v
        else:
            current.append(m)
    by_cardinality[k] = current
    assert len(current) == expected[k], (k, len(current))

ranks = {}
for k in range(1, 11):
    lower_idx = {mask: i for i, mask in enumerate(by_cardinality[k - 1])}
    pivots = {}
    for face in by_cardinality[k]:
        boundary = 0
        x = face
        while x:
            b = x & -x
            x -= b
            boundary ^= 1 << lower_idx[face ^ b]
        while boundary:
            pivot = boundary.bit_length() - 1
            if pivot in pivots:
                boundary ^= pivots[pivot]
            else:
                pivots[pivot] = boundary
                break
    ranks[k] = len(pivots)

betti = {}
for k in range(0, 11):
    outgoing = ranks.get(k, 0) # C_k -> C_{k-1}, with C_k indexed by size k
    incoming = ranks.get(k + 1, 0)
    betti[k - 1] = expected[k] - outgoing - incoming
assert betti == {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}, betti
print('MCGEE_HOMOLOGY_VERIFY_OK', 'faces_with_empty=34305',
      'independence_polynomial=' + str(expected),
      'boundary_ranks=' + str([ranks[k] for k in range(1,11)]),
      'reduced_mod2_betti_5=1')
