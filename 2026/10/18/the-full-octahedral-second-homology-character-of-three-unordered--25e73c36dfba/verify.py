#!/usr/bin/env python3
"""Exact finite cellular check for three unordered points on the cubical graph.
Only Python's standard library is required.  Source methods are mathematical,
with no need to obtain external data at execution time.
"""
from collections import defaultdict, deque
from itertools import combinations, permutations

P = 101
N_PARTICLES = 3


def sign_perm(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 else 1


def cycle_type(p):
    seen, lengths = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[a] = b
        return True


# Eight original cube vertices, one bivalent midpoint for each cube edge.
E = []
for a in range(8):
    for b in range(a + 1, 8):
        if (a ^ b).bit_count() == 1:
            mid = 8 + len(E) // 2
            E.extend(((a, mid), (mid, b)))
assert len(E) == 24
V = tuple(range(20))
original_edges = tuple(tuple(sorted((E[i][0], E[i+1][1]))) for i in range(0, 24, 2))
assert len(original_edges) == 12
original_lookup = {a: i for i, a in enumerate(original_edges)}
edge_lookup = {frozenset(pair): i for i, pair in enumerate(E)}

# An unordered k-cube is k closed-disjoint open edges together with
# (3-k) vertices disjoint from their endpoint sets.
cells, positions = [[] for _ in range(4)], [{} for _ in range(4)]
for k in range(4):
    for ee in combinations(range(len(E)), k):
        used = set()
        for e in ee:
            used.update(E[e])
        if len(used) != 2 * k:
            continue
        for vv in combinations(sorted(set(V) - used), N_PARTICLES - k):
            x = (vv, ee)
            positions[k][x] = len(cells[k])
            cells[k].append(x)
assert tuple(map(len, cells)) == (1140, 3672, 3840, 1296)


def boundary(cell):
    vv, ee = cell
    for j, e in enumerate(ee):
        for t, vertex in enumerate(E[e]):
            new = (tuple(sorted(vv + (vertex,))), ee[:j] + ee[j+1:])
            yield new, (-1) ** (j + 1 + t)

# Boundary squared vanishes over the integers, with every cell checked.
for k in (2, 3):
    for cell in cells[k]:
        dd = defaultdict(int)
        for face, a in boundary(cell):
            for subface, b in boundary(face):
                dd[subface] += a * b
        assert all(x == 0 for x in dd.values())

# Exact sequence of elementary 3/2 collapses. No Morse/spectral assumption.
cofaces = defaultdict(set)
for j, c in enumerate(cells[3]):
    for face, _ in boundary(c):
        cofaces[positions[2][face]].add(j)
removed3, removed2 = set(), set()
queue = deque(i for i, co in cofaces.items() if len(co) == 1)
while queue:
    i = queue.popleft()
    cand = cofaces[i] - removed3
    if len(cand) != 1 or i in removed2:
        continue
    j = next(iter(cand))
    removed2.add(i)
    removed3.add(j)
    for face, _ in boundary(cells[3][j]):
        f = positions[2][face]
        if len(cofaces[f] - removed3) == 1:
            queue.append(f)
assert len(removed3) == len(cells[3]) == 1296
assert len(removed2) == 1296

# Tree coordinates in the 1-skeleton. Exact integral cycles for
# every non-tree edge form a Z-basis before attaching 2-cells.
dsu = DSU(len(cells[0]))
tree, non_tree, endpoints = [], [], []
for j, c in enumerate(cells[1]):
    ep = tuple(positions[0][f] for f, _ in boundary(c))
    endpoints.append(ep)
    (tree if dsu.join(*ep) else non_tree).append(j)
assert len(tree) == 1139 and len(non_tree) == 2533
assert len({dsu.find(i) for i in range(len(cells[0]))}) == 1
non_tree_position = {e: i for i, e in enumerate(non_tree)}

# Over F_101, project d2 to fundamental-cycle coordinates and row-reduce.
relations = []
for c in cells[2]:
    row = defaultdict(int)
    for face, s in boundary(c):
        e = positions[1][face]
        if e in non_tree_position:
            i = non_tree_position[e]
            row[i] = (row[i] + s) % P
    relations.append({i: a for i, a in row.items() if a})

pivots = {}
for row in relations:
    row = row.copy()
    while row:
        key = max(row)
        if key not in pivots:
            inv = pow(row[key], -1, P)
            pivots[key] = {j: a * inv % P for j, a in row.items()}
            break
        a = row[key]
        for j, b in pivots[key].items():
            v = (row.get(j, 0) - a*b) % P
            if v:
                row[j] = v
            else:
                row.pop(j, None)
assert len(pivots) == 2527
free = sorted(set(range(len(non_tree))) - set(pivots))
assert len(free) == 6

# Independent binary rank check of the same projected integral d2.
binary_pivots = {}
for c in cells[2]:
    mask = 0
    for face, _ in boundary(c):
        e = positions[1][face]
        if e in non_tree_position:
            mask ^= 1 << non_tree_position[e]
    while mask:
        i = mask.bit_length() - 1
        if i not in binary_pivots:
            binary_pivots[i] = mask
            break
        mask ^= binary_pivots[i]
assert len(binary_pivots) == 2527

adj = [[] for _ in cells[0]]
for e in tree:
    a, b = endpoints[e]
    adj[a].append((b, e))
    adj[b].append((a, e))
parent = [-1] * len(cells[0])
parent_edge = [-1] * len(cells[0])
depth = [0] * len(cells[0])
parent[0] = 0
queue = deque([0])
while queue:
    a = queue.popleft()
    for b, e in adj[a]:
        if parent[b] == -1:
            parent[b], parent_edge[b], depth[b] = a, e, depth[a] + 1
            queue.append(b)
assert min(parent) >= 0


def cycle_from_non_tree_edge(e):
    low, high = endpoints[e]
    a, b = high, low
    chain = defaultdict(int)
    chain[e] += 1
    def step(x, y, edge, coef):
        chain[edge] += coef * (1 if endpoints[edge] == (x, y) else -1)
    while depth[a] > depth[b]:
        step(a, parent[a], parent_edge[a], 1)
        a = parent[a]
    while depth[b] > depth[a]:
        step(b, parent[b], parent_edge[b], -1)
        b = parent[b]
    while a != b:
        step(a, parent[a], parent_edge[a], 1)
        step(b, parent[b], parent_edge[b], -1)
        a, b = parent[a], parent[b]
    chain = {j: s for j, s in chain.items() if s}
    # Verify the resulting 1-chain is integrally closed.
    total = defaultdict(int)
    for j, coeff in chain.items():
        for vertex, sign in boundary(cells[1][j]):
            total[positions[0][vertex]] += coeff * sign
    assert all(x == 0 for x in total.values())
    return chain

basis = [cycle_from_non_tree_edge(non_tree[f]) for f in free]

def reduce_relation(row):
    while True:
        common = row.keys() & pivots.keys()
        if not common:
            return row
        key = max(common)
        a = row[key]
        for j, b in pivots[key].items():
            v = (row.get(j, 0) - a * b) % P
            if v:
                row[j] = v
            else:
                row.pop(j, None)


def cube_vertex_image(x, coordinate_perm, offset):
    return sum(((((x >> coordinate_perm[i]) & 1) ^ ((offset >> i) & 1))) << i for i in range(3))

TABLE = {
    '4': [1, 1, 1, 1, 1],
    '31': [3, 1, -1, 0, -1],
    '22': [2, 0, 2, -1, 0],
    '211': [3, -1, -1, 0, 1],
    '1111': [1, -1, 1, 1, -1],
}
TYPES = [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
classes = defaultdict(list)

for perm in permutations(range(3)):
    for offset in range(8):
        vm = [0] * 20
        for a in range(8):
            vm[a] = cube_vertex_image(a, perm, offset)
        for i, (a, b) in enumerate(original_edges):
            vm[8+i] = 8 + original_lookup[tuple(sorted((vm[a], vm[b])))]
        em, direction = [], []
        for a, b in E:
            j = edge_lookup[frozenset((vm[a], vm[b]))]
            em.append(j)
            direction.append(1 if E[j] == (vm[a], vm[b]) else -1)
        det = sign_perm(perm) * (-1) ** offset.bit_count()
        central = '+' if det == 1 else '-'
        diagonal_perm = tuple(min(vm[a], vm[a] ^ 7) for a in range(4))
        cycleclass = cycle_type(diagonal_perm)

        # Independent action on six H1 classes via fundamental loops.
        trace1 = 0
        for col, generator in enumerate(basis):
            image = defaultdict(int)
            for e, coefficient in generator.items():
                vv, ee = cells[1][e]
                target = (tuple(sorted(vm[v] for v in vv)), (em[ee[0]],))
                target_e = positions[1][target]
                if target_e in non_tree_position:
                    j = non_tree_position[target_e]
                    image[j] = (image[j] + coefficient*direction[ee[0]]) % P
            reduced = reduce_relation({j: v for j, v in image.items() if v})
            trace1 += reduced.get(free[col], 0)
        trace1 %= P
        if trace1 > P//2:
            trace1 -= P
        assert -6 <= trace1 <= 6

        # Check the first homology action also matches graph-flow plus Y-exchange.
        graph_h1_trace = (sum(direction[e] for e in range(24) if em[e] == e)
                          - sum(vm[i] == i for i in range(20)) + 1)
        assert trace1 == graph_h1_trace + det

        # Signed fixed-cell Lefschetz trace: no homology basis needed in H2.
        chain_traces = []
        for k in range(4):
            tr = 0
            for vv, ee in cells[k]:
                if tuple(sorted(vm[v] for v in vv)) != vv:
                    continue
                transformed = tuple(em[e] for e in ee)
                if set(transformed) != set(ee):
                    continue
                orientation = sign_perm(tuple(ee.index(e) for e in transformed))
                for e in ee:
                    orientation *= direction[e]
                tr += orientation
            chain_traces.append(tr)
        lefschetz = sum((-1)**k * tr for k, tr in enumerate(chain_traces))
        trace2 = lefschetz - 1 + trace1
        classes[(cycleclass, central)].append((trace1, trace2))

assert len(classes) == 10 and sum(map(len, classes.values())) == 48
assert all(len({v for x in a for v in [x[1]]}) == 1 for a in classes.values())
expected2 = {
    ((1,1,1,1), '+'): 17, ((1,1,1,1), '-'): -1,
    ((2,1,1), '+'): -3, ((2,1,1), '-'): 3,
    ((2,2), '+'): 1, ((2,2), '-'): -1,
    ((3,1), '+'): -1, ((3,1), '-'): -1,
    ((4,), '+'): 1, ((4,), '-'): -1,
}
for key, target in expected2.items():
    assert all(x[1] == target for x in classes[key])

multiplicities = {}
for part, row in TABLE.items():
    for parity in (1, -1):
        numerator = 0
        for i, typ in enumerate(TYPES):
            for central in ('+', '-'):
                a = classes[(typ, central)]
                numerator += len(a) * a[0][1] * row[i] * (1 if central == '+' else parity)
        assert numerator % 48 == 0
        multiplicities[(part, parity)] = numerator // 48
assert multiplicities == {
    ('4', 1): 0, ('4', -1): 0,
    ('31', 1): 1, ('31', -1): 0,
    ('22', 1): 1, ('22', -1): 1,
    ('211', 1): 1, ('211', -1): 2,
    ('1111', 1): 0, ('1111', -1): 1,
}
assert sum(multiplicities[(part, parity)] * TABLE[part][0]
           for part, parity in multiplicities) == 17
print('Cubes C0,C1,C2,C3:', tuple(map(len, cells)))
print('Elementary 3/2 collapses:', len(removed3))
print('Connected 1-skeleton: yes')
print('d2 projected ranks modulo 101 and 2:', len(pivots), len(binary_pivots))
print('Full-group H1 action checked: 48 elements, rank 6')
print('H2 integral rank: 17; H3: 0 (Ko-Park first homology theorem used)')
for t in TYPES:
    for central in ('+', '-'):
        print('H2 character', t, central, classes[(t, central)][0][1])
print('H2 S4 x C2 irreducible multiplicities:', multiplicities)
print('VERIFICATION SUCCESS')
