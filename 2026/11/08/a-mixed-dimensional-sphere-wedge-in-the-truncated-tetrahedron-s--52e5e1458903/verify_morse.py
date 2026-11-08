"""Integral discrete-Morse certificate for the second independence complex of the truncated tetrahedral graph.

Run with Python 3.10+; this file uses only the standard library.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

VERTICES = [(a, b) for a in range(4) for b in range(4) if a != b]
assert len(VERTICES) == 12
EDGES = {
    (u, v)
    for u, v in combinations(range(12), 2)
    if VERTICES[u][0] == VERTICES[v][0]
    or VERTICES[u] == (VERTICES[v][1], VERTICES[v][0])
}
assert len(EDGES) == 18
ADJ = [0] * 12
for u, v in EDGES:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u


def allowed(mask):
    remaining = mask
    while remaining:
        component = 0
        frontier = remaining & -remaining
        while frontier:
            component |= frontier
            remaining &= ~frontier
            nxt = 0
            bits = frontier
            while bits:
                bit = bits & -bits
                bits -= bit
                nxt |= ADJ[bit.bit_length() - 1]
            frontier = (nxt & mask) & ~component
        if component.bit_count() > 2:
            return False
    return True


FACES = [m for m in range(1, 1 << 12) if allowed(m)]
assert len(FACES) == 863
assert [Counter(m.bit_count() - 1 for m in FACES)[i] for i in range(6)] == [12, 66, 192, 303, 228, 62]
FSET = set(FACES)
assert all((f ^ (1 << i)) in FSET for f in FACES for i in range(12) if (f & (1 << i)) and f.bit_count() > 1)

# Partition the matching into 12 consecutively applied element matchings.
# At each step, pair every currently unmatched face not containing v
# with its coface containing v, if that coface remains unmatched.
ORDER = [0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8, 11]
unmatched = set(FACES)
pairs = []
for v in ORDER:
    bit = 1 << v
    for a in FACES:
        b = a | bit
        if a in unmatched and not (a & bit) and b in unmatched:
            unmatched.remove(a)
            unmatched.remove(b)
            pairs.append((a, b))

critical = sorted(unmatched, key=lambda c: (c.bit_count(), c))
assert len(pairs) == 428
assert len(critical) == 7
assert Counter(c.bit_count() - 1 for c in critical) == {0: 1, 3: 3, 4: 3}

# Explicitly reverse each matched face-poset cover and check the entire
# directed face-poset has no directed cycle by Kahn's algorithm.
matched_covers = set(pairs)
adj_dir = defaultdict(list)
indegree = {f: 0 for f in FACES}
num_covers = 0
for top in FACES:
    bits = top
    while bits:
        z = bits & -bits
        bits -= z
        bottom = top ^ z
        if not bottom:
            continue
        num_covers += 1
        a, b = (top, bottom) if (bottom, top) in matched_covers else (bottom, top)
        adj_dir[a].append(b)
        indegree[b] += 1
queue = [f for f in FACES if indegree[f] == 0]
i = 0
while i < len(queue):
    f = queue[i]
    i += 1
    for g in adj_dir[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert len(queue) == len(FACES), "Directed cycle in the proposed matching"


def boundary(top):
    """Signed simplicial boundary in increasing vertex order."""
    idx = 0
    bits = top
    while bits:
        z = bits & -bits
        bits -= z
        bot = top ^ z
        if bot:
            yield bot, (-1 if idx % 2 else 1)
        idx += 1


upper_of_lower = dict(pairs)
critical_set = set(critical)


@lru_cache(maxsize=None)
def reduction(cell):
    """Integral gradient-path expansion of a face into critical faces.

    Only same-dimensional unmatched lower cells have upward gradient steps;
    matched upper cells terminate with zero coefficient. The incidence
    of a simplex in its unique paired coface is ±1.
    """
    if cell in critical_set:
        return {cell: 1}
    if cell not in upper_of_lower:
        return {}
    upper = upper_of_lower[cell]
    bdry = list(boundary(upper))
    unit = next(v for x, v in bdry if x == cell)
    assert abs(unit) == 1
    result = defaultdict(int)
    for other, c in bdry:
        if other == cell:
            continue
        for tgt, val in reduction(other).items():
            result[tgt] -= unit * c * val
    return {k: v for k, v in result.items() if v}


crit3 = [c for c in critical if c.bit_count() == 4]
crit4 = [c for c in critical if c.bit_count() == 5]
assert len(crit3) == len(crit4) == 3
morse_matrix = []
for top in crit4:
    row = defaultdict(int)
    for bot, c in boundary(top):
        for tgt, val in reduction(bot).items():
            row[tgt] += c * val
    morse_matrix.append([row.get(s, 0) for s in crit3])
assert morse_matrix == [[0, 0, 0]] * 3
print('VERTICES=12 EDGES=18')
print('FACE_VECTOR=' + ','.join(map(str, [12, 66, 192, 303, 228, 62])))
print('FACES=863 MATCHED_PAIRS=428 FACE_POSET_COVERS=' + str(num_covers))
print('ACYCLICITY_TOPOLOGICAL_SORT=' + str(len(queue)))
print('MATCHING_VERTEX_ORDER=' + ','.join(map(str, ORDER)))
print('CRITICAL=' + ','.join(map(str, critical)))
print('CRITICAL_DIMS=0:1,3:3,4:3')
print('INTEGER_MORSE_D4_TO_D3=' + repr(morse_matrix))
print('INTEGRAL_HOMOTOPY_VERIFICATION_PASS')
