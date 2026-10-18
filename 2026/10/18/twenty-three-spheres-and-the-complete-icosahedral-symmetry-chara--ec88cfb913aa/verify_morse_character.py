#!/usr/bin/env python3
"""Exhaustive finite verification of a two-independence complex and its symmetry character.

Run with Python 3.10+; no nonstandard packages required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 12
EDGES = [
    (0,1),(0,5),(0,7),(0,8),(0,11),
    (1,2),(1,5),(1,6),(1,8),
    (2,3),(2,6),(2,8),(2,9),
    (3,4),(3,6),(3,9),(3,10),
    (4,5),(4,6),(4,10),(4,11),
    (5,6),(5,11),
    (7,8),(7,9),(7,10),(7,11),
    (8,9),(9,10),(10,11)
]
ADJ = [0] * N
for u, v in EDGES:
    assert 0 <= u < v < N
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
assert len(EDGES) == 30 and all(a.bit_count() == 5 for a in ADJ)

# Identify the edge-list graph with the standard two-pentagon icosahedron.
# Model: vertices 0/1 poles, vertices 2..6 and 7..11 two pentagonal belts.
model_to_code = [0, 3, 1, 8, 7, 11, 5, 2, 9, 10, 4, 6]
model_edges = set()
for i in range(5):
    for a, b in ((0, 2+i), (1, 7+i), (2+i, 2+(i+1)%5),
                 (7+i, 7+(i+1)%5), (2+i, 7+i), (2+i, 7+(i-1)%5)):
        model_edges.add(tuple(sorted((model_to_code[a], model_to_code[b]))))
assert model_edges == set(EDGES)


def admissible(s):
    return all((s & ADJ[u]).bit_count() <= 1
               for u in range(N) if (s >> u) & 1)

F = {s for s in range(1, 1 << N) if admissible(s)}
FV = {d: sorted(s for s in F if s.bit_count() == d + 1)
      for d in range(4)}
assert [len(FV[d]) for d in range(4)] == [12, 66, 140, 105]
assert len(F) == 323 and max(s.bit_count() for s in F) == 4
for s in F:
    for u in range(N):
        if s & (1 << u) and s != (1 << u):
            assert (s ^ (1 << u)) in F

# Successive element matchings on the remaining face poset.
PIVOTS = [7, 4, 5, 2, 9, 3, 6, 0, 10, 1, 8, 11]
assert sorted(PIVOTS) == list(range(N))
remaining = set(F)
matched = {}
matching = []
for u in PIVOTS:
    bit = 1 << u
    for lo in sorted(remaining):
        hi = lo | bit
        if not lo & bit and hi in remaining:
            remaining.remove(lo)
            remaining.remove(hi)
            matching.append((lo, hi))
            matched[lo] = hi
assert len(matching) == 151
assert Counter(s.bit_count() - 1 for s in remaining) == {0: 1, 3: 20}

# Full acyclicity certificate: reverse every matched cover, orient all others downward.
indegree = {s: 0 for s in F}
successors = defaultdict(list)
covers = 0
for high in F:
    if high.bit_count() == 1:
        continue
    for u in range(N):
        if not high & (1 << u):
            continue
        low = high ^ (1 << u)
        assert low in F
        if matched.get(low) == high:
            source, target = low, high
        else:
            source, target = high, low
        successors[source].append(target)
        indegree[target] += 1
        covers += 1
queue = deque(sorted(s for s, d in indegree.items() if d == 0))
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in successors[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(F), 'directed matching cycle detected'
assert all(k == 0 for k in indegree.values())
print('faces_by_dimension', [len(FV[d]) for d in range(4)])
print('matched_pairs', len(matching), 'critical_by_dimension', dict(sorted(Counter(s.bit_count()-1 for s in remaining).items())))
print('hasse_covers', covers, 'topological_sort_visits', visited)

# Exhaustively enumerate all graph automorphisms using adjacency and nonadjacency pruning.
def graph_automorphisms():
    answer = []
    mapping = [-1] * N
    used = [False] * N
    def rec(depth):
        if depth == N:
            answer.append(tuple(mapping))
            return
        unmapped = [u for u in range(N) if mapping[u] < 0]
        # Choose the source vertex with the largest number of already mapped neighbors.
        u = max(unmapped, key=lambda a: (sum((ADJ[a] >> b) & 1 for b in range(N)
                                              if mapping[b] >= 0), -a))
        for v in range(N):
            if used[v]:
                continue
            if any(bool(ADJ[u] & (1 << b)) != bool(ADJ[v] & (1 << mapping[b]))
                   for b in range(N) if mapping[b] >= 0):
                continue
            mapping[u] = v
            used[v] = True
            rec(depth + 1)
            used[v] = False
            mapping[u] = -1
    rec(0)
    return sorted(answer)

AUT = graph_automorphisms()
assert len(AUT) == 120 and len(set(AUT)) == 120
assert all(all(bool(ADJ[i] & (1 << j)) == bool(ADJ[p[i]] & (1 << p[j]))
               for i in range(N) for j in range(N)) for p in AUT)

# Unique opposite vertex at graph distance three gives the antipodal central involution.
opp = []
for root in range(N):
    distances = [-1] * N
    distances[root] = 0
    q = deque([root])
    while q:
        x = q.popleft()
        for y in range(N):
            if ADJ[x] & (1 << y) and distances[y] < 0:
                distances[y] = distances[x] + 1
                q.append(y)
    far = [u for u, d in enumerate(distances) if d == 3]
    assert len(far) == 1 and max(distances) == 3
    opp.append(far[0])
assert tuple(opp) in AUT
assert all(opp[p[u]] == p[opp[u]] for p in AUT for u in range(N))

def sign_of_map_on_vertices(vertices, p):
    im = [p[u] for u in vertices]
    if set(im) != set(vertices):
        return 0
    parity = sum(im[i] > im[j] for i in range(len(im)) for j in range(i+1, len(im)))
    return (-1) ** parity

ordered_faces = {d: [tuple(u for u in range(N) if s & (1 << u)) for s in FV[d]]
                 for d in range(4)}

def h3_trace(p):
    # Unreduced Hopf trace: L(g) = 1 - tr(g | H_3), since H_0 = Q.
    return 1 - sum((-1) ** d * sum(sign_of_map_on_vertices(vs, p)
                                    for vs in ordered_faces[d]) for d in range(4))

def cycle_lengths(p):
    seen = set()
    lengths = []
    for u in range(N):
        if u in seen:
            continue
        v = u
        k = 0
        while v not in seen:
            seen.add(v)
            k += 1
            v = p[v]
        lengths.append(k)
    return tuple(sorted(lengths))

characters = defaultdict(Counter)
identity = tuple(range(N))
for p in AUT:
    cy = cycle_lengths(p)
    if p == identity:
        cls = 'identity'
    elif p == tuple(opp):
        cls = 'antipodal'
    else:
        cls = {
            (2,2,2,2,2,2): 'rotation_order_2',
            (1,1,1,1,2,2,2,2): 'antipodal_times_rotation_order_2',
            (3,3,3,3): 'rotation_order_3',
            (6,6): 'antipodal_times_rotation_order_3',
            (1,1,5,5): 'rotation_order_5',
            (2,10): 'antipodal_times_rotation_order_5',
        }[cy]
    characters[cls][h3_trace(p)] += 1
expected = {
    'identity': (20, 1),
    'rotation_order_2': (4, 15),
    'rotation_order_3': (-1, 20),
    'rotation_order_5': (0, 24),
    'antipodal': (10, 1),
    'antipodal_times_rotation_order_2': (2, 15),
    'antipodal_times_rotation_order_3': (1, 20),
    'antipodal_times_rotation_order_5': (0, 24),
}
assert {key: (next(iter(c)), sum(c.values())) for key, c in characters.items()} == expected
assert all(len(c) == 1 for c in characters.values())
print('automorphism_group_size', len(AUT), 'antipodal_center', tuple(opp))
for key in expected:
    print('class', key, 'character', expected[key][0], 'size', expected[key][1])

# Standard A_5 character rows on 1, 2A, 3A, 5A, 5B (both 5A and 5B equal here).
# 1=(1,1,1,1,1), 4=(4,0,1,-1,-1), 5=(5,1,-1,0,0).
plus = tuple((a+b)//2 for a, b in zip(
    [20, 4, -1, 0], [10, 2, 1, 0]))
minus = tuple((a-b)//2 for a, b in zip(
    [20, 4, -1, 0], [10, 2, 1, 0]))
assert plus == (15, 3, 0, 0) and minus == (5, 1, -1, 0)
assert tuple(x+y+2*z for x,y,z in zip((1,1,1,1),(4,0,1,-1),(5,1,-1,0))) == plus
assert minus == (5,1,-1,0)
print('A5_rotation_positive_part: 1 + 4 + 2*5; antipodal_negative_part: 5')
print('ALL_CHECKS_PASS')
