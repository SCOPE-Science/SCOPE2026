from itertools import combinations
from math import gcd
from functools import reduce

N = 14
P = 7


def edge(a, b):
    return (a, b) if a < b else (b, a)


def canonical_cycle(cycle):
    cycle = tuple(cycle)
    n = len(cycle)
    candidates = []
    for s in range(n):
        candidates.append(tuple(cycle[(s + i) % n] for i in range(n)))
    rev = cycle[::-1]
    for s in range(n):
        candidates.append(tuple(rev[(s + i) % n] for i in range(n)))
    return min(candidates)


facets = set()
for i in range(N):
    facets.add(tuple(sorted((i, (i + 1) % N, (i + 2) % N))))
    facets.add(tuple(sorted((i, (i + 2) % N, (i + P + 1) % N))))
facets = sorted(facets)
edges = sorted({edge(a, b) for f in facets for a, b in combinations(f, 2)})
edge_set = set(edges)
assert (N, len(edges), len(facets)) == (14, 42, 28)

edge_degree = {e: 0 for e in edges}
for f in facets:
    for a, b in combinations(f, 2):
        edge_degree[edge(a, b)] += 1
assert set(edge_degree.values()) == {2}

# A two-dimensional simplicial complex is flag exactly when every graph clique is a face.
graph_triangles = {
    t for t in combinations(range(N), 3)
    if all(edge(a, b) in edge_set for a, b in combinations(t, 2))
}
assert graph_triangles == set(facets)
assert not any(
    all(edge(a, b) in edge_set for a, b in combinations(s, 2))
    for s in combinations(range(N), 4)
)

# Collapse the spanning tree 0-1-...-13. The remaining 29 oriented edges generate H_1.
tree = {edge(i, i + 1) for i in range(N - 1)}
assert tree <= edge_set
non_tree = [e for e in edges if e not in tree]
index = {e: j for j, e in enumerate(non_tree)}
assert len(non_tree) == 29


def edge_coordinate(a, b):
    e = edge(a, b)
    if e in tree:
        return None, 0
    return index[e], 1 if a < b else -1


def triangle_relation(f):
    a, b, c = sorted(f)
    row = [0] * 29
    for x, y, coeff in ((b, c, 1), (a, c, -1), (a, b, 1)):
        j, sign = edge_coordinate(x, y)
        if j is not None:
            row[j] += coeff * sign
    return row


relations = [triangle_relation(f) for f in facets]


def det_bareiss(matrix):
    A = [list(map(int, row)) for row in matrix]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if pivot_row is None:
                return 0
            A[k], A[pivot_row] = A[pivot_row], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // previous
        previous = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]


maximal_minors = []
for omitted in range(29):
    square = [[row[j] for j in range(29) if j != omitted] for row in relations]
    maximal_minors.append(det_bareiss(square))
assert any(maximal_minors)
determinantal_gcd = 0
for value in maximal_minors:
    determinantal_gcd = gcd(determinantal_gcd, abs(value))
assert determinantal_gcd == 2

# Cofactors give a primitive homomorphism from the presentation to the free summand.
free_cocycle = [((-1) ** j) * maximal_minors[j] // determinantal_gcd for j in range(29)]
assert reduce(gcd, (abs(x) for x in free_cocycle if x), 0) == 1
assert all(sum(row[j] * free_cocycle[j] for j in range(29)) == 0 for row in relations)


def gf2_basis(rows):
    basis = {}
    for row in rows:
        x = 0
        for j, value in enumerate(row):
            if value & 1:
                x |= 1 << j
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return basis


gf2_relations = gf2_basis(relations)
assert len(gf2_relations) == 27


def reduce_mod2(x):
    for p in sorted(gf2_relations, reverse=True):
        if (x >> p) & 1:
            x ^= gf2_relations[p]
    return x


def cycle_vector(cycle):
    vector = [0] * 29
    cycle = list(cycle)
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        j, sign = edge_coordinate(a, b)
        if j is not None:
            vector[j] += sign
    return vector


def homology_coordinates(cycle):
    vector = cycle_vector(cycle)
    free = sum(vector[j] * free_cocycle[j] for j in range(29))
    bits = 0
    for j, value in enumerate(vector):
        if value & 1:
            bits |= 1 << j
    return free, reduce_mod2(bits)


def simple_cycles(length):
    found = set()
    def dfs(path):
        if len(path) == length:
            if edge(path[-1], path[0]) in edge_set:
                found.add(canonical_cycle(path))
            return
        for v in range(N):
            if v not in path and edge(path[-1], v) in edge_set:
                dfs(path + [v])
    for start in range(N):
        dfs([start])
    return found


cycles3 = simple_cycles(3)
cycles4 = simple_cycles(4)
assert len(cycles3) == 28
assert {tuple(sorted(c)) for c in cycles3} == set(facets)
assert len(cycles4) == 77

null_cycles = []
torsion_cycles = []
primitive_cycles = []
for cycle in sorted(cycles4):
    free, mod2 = homology_coordinates(cycle)
    if free == 0 and mod2 == 0:
        null_cycles.append(cycle)
    elif free == 0:
        torsion_cycles.append(cycle)
    else:
        assert abs(free) == 1
        primitive_cycles.append(cycle)
assert (len(null_cycles), len(torsion_cycles), len(primitive_cycles)) == (42, 21, 14)

essential = set(torsion_cycles) | set(primitive_cycles)
assert len(essential) == 35


def translate(cycle, amount):
    return canonical_cycle(tuple((v + amount) % N for v in cycle))


def orbit(cycle):
    return {translate(cycle, amount) for amount in range(N)}


representatives = [(0, 1, 7, 6), (0, 1, 7, 8), (0, 2, 4, 6)]
orbits = [orbit(canonical_cycle(c)) for c in representatives]
assert [len(o) for o in orbits] == [14, 7, 14]
assert set().union(*orbits) == essential
assert all(homology_coordinates(c)[0] == 0 and homology_coordinates(c)[1] != 0 for c in orbits[0] | orbits[1])
assert all(abs(homology_coordinates(c)[0]) == 1 for c in orbits[2])

print('VERIFY_OK f=14,42,28 flag=yes H1=Z+Z/2 cycles4=77 essential4=35 torsion4=21 primitive4=14 orbits=14T,7T,14P systole=4')
