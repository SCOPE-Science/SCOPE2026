"""Exact finite certificate for the triangular-prism graph's discrete-Morse complex.

Run with Python 3.9+; uses only the standard library.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product

EDGES = tuple(sorted({(i, (i + 1) % 3) if i < (i + 1) % 3 else ((i + 1) % 3, i)
                      for i in range(3)}
                     | {(i + 3, (i + 1) % 3 + 3) if i < (i + 1) % 3
                        else ((i + 1) % 3 + 3, i + 3) for i in range(3)}
                     | {(i, i + 3) for i in range(3)}))
assert EDGES == ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4),
                 (2, 5), (3, 4), (3, 5), (4, 5))

# The first discrete-Morse complex of the triangle is the prism graph:
# its six vertices are the six vertex-edge incidences of C3.
from itertools import combinations, permutations
TRI_EDGES = ((0, 1), (0, 2), (1, 2))
TRI_INCIDENCES = tuple((v, e) for e in TRI_EDGES for v in e)
TRI_MORSE_EDGES = {
    (i, j) for i, j in combinations(range(6), 2)
    if TRI_INCIDENCES[i][0] != TRI_INCIDENCES[j][0]
    and TRI_INCIDENCES[i][1] != TRI_INCIDENCES[j][1]
}
assert len(TRI_MORSE_EDGES) == 9
assert any({tuple(sorted((p[i], p[j]))) for i, j in TRI_MORSE_EDGES}
           == set(EDGES) for p in permutations(range(6)))
# Every set of three distinct triangle edges matched with three vertices
# would be a directed cycle, so the first complex has no 2-faces.

# Each complex vertex is the ordered incidence (matched graph vertex, graph edge).
INC = tuple((v, e) for e in EDGES for v in e)
assert len(INC) == 18
OPTIONS = []
for v in range(6):
    OPTIONS.append((None,) + tuple((j, e[0] + e[1] - v)
                                    for j, (w, e) in enumerate(INC) if w == v))
assert all(len(o) == 4 for o in OPTIONS)


def is_dag(out):
    for v in out:
        x = v
        seen = set()
        while x in out:
            if x in seen:
                return False
            seen.add(x)
            x = out[x]
    return True


def enumerate_faces():
    F = set()
    for choice in product(*OPTIONS):
        out = {}
        mask = 0
        used_edges = set()
        for v, picked in enumerate(choice):
            if picked is None:
                continue
            j, target = picked
            edge = tuple(sorted((v, target)))
            if edge in used_edges:
                break
            out[v] = target
            used_edges.add(edge)
            mask |= 1 << j
        else:
            if mask and is_dag(out):
                F.add(mask)
    return F


F = enumerate_faces()
COUNTS = Counter((x.bit_count() - 1) for x in F)
assert tuple(COUNTS[i] for i in range(5)) == (18, 126, 428, 705, 450)
assert len(F) == 1727
assert max(x.bit_count() for x in F) == 5

# Independent count: choose an undirected spanning forest and a root in each
# component. For each component of size s, there are s orientations toward roots.
FOREST_COUNTS = Counter()
for bits in range(1 << len(EDGES)):
    parent = list(range(6))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    valid = True
    for j, (a, b) in enumerate(EDGES):
        if not (bits >> j) & 1:
            continue
        ra, rb = root(a), root(b)
        if ra == rb:
            valid = False
            break
        parent[ra] = rb
    if valid:
        sizes = Counter(root(v) for v in range(6))
        mult = 1
        for n in sizes.values():
            mult *= n
        FOREST_COUNTS[bits.bit_count()] += mult
assert tuple(FOREST_COUNTS[k] for k in range(6)) == (1, 18, 126, 428, 705, 450)

# A deterministic ordered collection of element matchings: for each incidence
# index i in ascending order, toggle i on the remaining faces whenever legal.
remain = set(F)
matched = []
for i in range(len(INC)):
    for low in sorted(tuple(remain)):
        if low not in remain or (low >> i) & 1:
            continue
        up = low | (1 << i)
        if up in remain:
            assert up.bit_count() == low.bit_count() + 1
            remain.remove(low)
            remain.remove(up)
            matched.append((low, up))
assert len(matched) == 828
CRITICAL = {d: sorted(x for x in remain if x.bit_count() == d + 1)
            for d in range(5)}
assert tuple(len(CRITICAL[d]) for d in range(5)) == (1, 0, 0, 3, 67)

LOW_TO_HIGH = dict(matched)
HIGH_TO_LOW = {b: a for a, b in matched}
assert len(LOW_TO_HIGH) == len(HIGH_TO_LOW) == len(matched)
assert set(LOW_TO_HIGH).isdisjoint(set(HIGH_TO_LOW))
assert set(LOW_TO_HIGH) | set(HIGH_TO_LOW) | remain == F


def boundary(g):
    m = g
    pos = 0
    while m:
        bit = m & -m
        yield (g ^ bit, -1 if pos % 2 else 1)
        m -= bit
        pos += 1


# Directed Hasse graph: unmatched coface -> face; matched face -> coface.
indegree = {f: 0 for f in F}
forward = defaultdict(list)
incidences = 0
for high in F:
    if high.bit_count() <= 1:
        continue
    for low, _ in boundary(high):
        assert low in F
        incidences += 1
        src, dst = (low, high) if LOW_TO_HIGH.get(low) == high else (high, low)
        forward[src].append(dst)
        indegree[dst] += 1
queue = deque(f for f in sorted(F) if indegree[f] == 0)
visited = 0
while queue:
    a = queue.popleft()
    visited += 1
    for b in forward[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            queue.append(b)
assert visited == len(F), (visited, len(F))
assert incidences == sum((d + 1) * COUNTS[d] for d in range(1, 5))

# Signed discrete-Morse boundary in dimension 4 -> 3. A lower cell is
# replaced by its coefficient-normalized matched upper-cell boundary.
cr3_idx = {f: i for i, f in enumerate(CRITICAL[3])}


@lru_cache(None)
def projection(face):
    assert face.bit_count() == 4
    if face in remain:
        assert face in cr3_idx
        return {cr3_idx[face]: 1}
    if face in HIGH_TO_LOW:
        return {}
    upper = LOW_TO_HIGH[face]
    coeff = dict(boundary(upper))[face]
    assert abs(coeff) == 1
    result = defaultdict(int)
    for lower, signed in boundary(upper):
        if lower == face:
            continue
        for target, value in projection(lower).items():
            result[target] -= coeff * signed * value
    return {k: v for k, v in result.items() if v}


columns = []
for top in CRITICAL[4]:
    column = defaultdict(int)
    for facet, signed in boundary(top):
        for target, value in projection(facet).items():
            column[target] += signed * value
    columns.append(tuple(column.get(i, 0) for i in range(len(CRITICAL[3]))))
assert len(columns) == 67
assert columns[0] == (1, 0, 0), columns[0]
assert columns[17] == (0, 1, 0), columns[17]
assert columns[28] == (0, 0, 1), columns[28]
assert (CRITICAL[3], [CRITICAL[4][j] for j in (0, 17, 28)]) == (
    [25602, 70658, 82946], [26692, 42272, 84036])
# The displayed three unit columns give a unimodular rank-three submatrix.
# Hence the integer attaching degrees have a split rank-three image; the
# remaining 64 four-cells attach nullhomotopically after basis changes.
print('VERIFY_OK faces=%s f_vector=%s incidences=%s pairs=%s critical=%s '
      'unit_columns=%s homotopy=wedge_64_S4'
      % (len(F), [COUNTS[i] for i in range(5)], incidences,
         len(matched), [len(CRITICAL[d]) for d in range(5)], (0, 17, 28)))
