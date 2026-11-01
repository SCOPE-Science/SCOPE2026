#!/usr/bin/env python3
"""Exact integral simplicial Morse certificate for a 7-vertex digraph.

Python standard library only. Running the program independently reconstructs the
complex, its complete gradient Hasse digraph and integer Morse boundary.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

# The directed edges of the bidirected complete bipartite graph with parts
# {0,1,2} and {3,4,5,6}; no loops or repeated edges.
EDGES = tuple(
    edge
    for left in range(3)
    for right in range(3, 7)
    for edge in ((left, right), (right, left))
)
ORDER = (0, 23, 5, 12, 17, 11, 15, 1, 21, 6, 14, 13,
         4, 22, 10, 2, 9, 18, 8, 7, 16, 20, 19, 3)


def is_multipath(indices):
    """Independent test: each vertex has in/out degree <=1, no directed cycle."""
    succ = [-1] * 7
    pred = [-1] * 7
    for k in indices:
        u, v = EDGES[k]
        if succ[u] != -1 or pred[v] != -1:
            return False
        succ[u] = v
        pred[v] = u
    for u in range(7):
        seen = set()
        p = u
        while p != -1:
            if p in seen:
                return False
            seen.add(p)
            p = succ[p]
    return True


def enumerate_by_backtracking():
    faces = []
    succ = [-1] * 7
    pred = [-1] * 7

    def rec(k, mask):
        if k == len(EDGES):
            faces.append(mask)
            return
        rec(k + 1, mask)
        u, v = EDGES[k]
        if succ[u] != -1 or pred[v] != -1:
            return
        p = v
        while p != -1 and p != u:
            p = succ[p]
        if p == u:
            return
        succ[u] = v
        pred[v] = u
        rec(k + 1, mask | (1 << k))
        succ[u] = -1
        pred[v] = -1

    rec(0, 0)
    return faces


def boundary(mask):
    bits = [i for i in range(24) if mask & (1 << i)]
    for pos, i in enumerate(bits):
        yield mask ^ (1 << i), (-1 if pos % 2 else 1)


def mod2_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            lead = vector.bit_length() - 1
            if lead in pivots:
                vector ^= pivots[lead]
            else:
                pivots[lead] = vector
                break
    return len(pivots)


def verify():
    faces = enumerate_by_backtracking()
    all_faces = set(faces)
    assert len(faces) == len(all_faces) == 3301
    assert set(ORDER) == set(range(24))

    # An unrelated enumeration using all subsets of size at most six checks
    # that the backtracker omitted no legal faces and accepted no illegal ones.
    independent = set()
    for size in range(7):
        for indices in combinations(range(24), size):
            if is_multipath(indices):
                independent.add(sum(1 << i for i in indices))
    assert independent == all_faces
    face_vector = Counter(mask.bit_count() - 1 for mask in faces)
    assert tuple(face_vector[d] for d in range(-1, 6)) == (
        1, 24, 204, 768, 1296, 864, 144
    )
    assert all(
        any(((mask | (1 << i)) in all_faces)
            for i in range(24) if not mask & (1 << i))
        for mask in faces if mask.bit_count() < 6
    ), "all maximal faces must be six-edge Hamilton paths"

    # Repeated elementary element toggles. An augmented face, including the
    # empty face, is paired at most once. The next acyclicity test is global.
    partner = {}
    lower_to_upper = {}
    for i in ORDER:
        for low in faces:
            if low in partner or low & (1 << i):
                continue
            high = low | (1 << i)
            if high in all_faces and high not in partner:
                partner[low] = high
                partner[high] = low
                lower_to_upper[low] = high
    assert len(lower_to_upper) == 1608
    assert 0 in lower_to_upper  # deleting this augmented pair leaves 1607 ordinary pairs
    critical = [m for m in faces if m not in partner]
    assert Counter(m.bit_count() - 1 for m in critical) == {3: 37, 4: 48}

    # Directed Hasse graph: reversed orientation exactly on paired cover
    # relations. A full topological-sort traversal proves acyclicity.
    idx = {mask: j for j, mask in enumerate(faces)}
    adjacency = [[] for _ in faces]
    indegree = [0] * len(faces)
    covers = 0
    for high in faces:
        for low, _ in boundary(high):
            if lower_to_upper.get(low) == high:
                source, target = idx[low], idx[high]
            else:
                source, target = idx[high], idx[low]
            adjacency[source].append(target)
            indegree[target] += 1
            covers += 1
    assert covers == 13104
    queue = deque(j for j, deg in enumerate(indegree) if deg == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert visited == len(faces)

    critical_3 = [m for m in critical if m.bit_count() == 4]
    critical_4 = [m for m in critical if m.bit_count() == 5]
    basis_3 = {mask: j for j, mask in enumerate(critical_3)}

    # Exact integral algebraic Morse projection in dimension three. A lower
    # matched cell is eliminated by its matched upper cell's signed boundary;
    # an upper matched cell projects to zero. Termination follows from the
    # preceding complete acyclicity check.
    @lru_cache(maxsize=None)
    def reduce_3(mask):
        if mask in basis_3:
            return {basis_3[mask]: 1}
        if mask not in partner:
            return {}
        high = partner[mask]
        if high.bit_count() < mask.bit_count():
            return {}  # matched upper three-cell
        epsilon = next(c for f, c in boundary(high) if f == mask)
        answer = defaultdict(int)
        for other, coeff in boundary(high):
            if other == mask:
                continue
            for j, value in reduce_3(other).items():
                answer[j] -= epsilon * coeff * value
        return {j: value for j, value in answer.items() if value}

    nonzero = []
    for col, high in enumerate(critical_4):
        projected = defaultdict(int)
        for low, coeff in boundary(high):
            for row, value in reduce_3(low).items():
                projected[row] += coeff * value
        for row, value in projected.items():
            if value:
                nonzero.append((row, col, value))
    assert not nonzero, "the 37 x 48 integral Morse boundary must be zero"

    # Independent direct chain-complex calculation, over F_2. This is only a
    # corroboration; integral homotopy follows from the exact Morse matching.
    by_dim = {d: [m for m in faces if m.bit_count() == d + 1]
              for d in range(-1, 6)}
    ranks = {}
    for d in range(6):
        row = {m: k for k, m in enumerate(by_dim[d - 1])}
        columns = []
        for high in by_dim[d]:
            column = 0
            for low, _ in boundary(high):
                column ^= 1 << row[low]
            columns.append(column)
        ranks[d] = mod2_rank(columns)
    assert tuple(ranks[d] for d in range(6)) == (1, 23, 181, 587, 672, 144)
    betti = {d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in range(6)}
    assert betti == {0: 0, 1: 0, 2: 0, 3: 37, 4: 48, 5: 0}

    print('face_vector=(-1:1,0:24,1:204,2:768,3:1296,4:864,5:144)')
    print('maximal_faces=144,dimension=5')
    print('augmented_gradient_pairs=1608,ordinary_pairs=1607')
    print('ordinary_critical=(0:1,3:37,4:48)')
    print('directed_Hasse_covers=13104,acyclic=True')
    print('integer_Morse_boundary_37_by_48=zero')
    print('mod2_boundary_ranks=(1,23,181,587,672,144)')
    print('K34_BIDIRECTED_MULTIPATH_MIXED_WEDGE_EXACT_OK')


if __name__ == '__main__':
    verify()
