#!/usr/bin/env python3
"""Independent finite certificates for induced-matching complexes of GP(10,2) and GP(10,3).

Standard-library-only verifier. The specified bit order is the lexicographic order
of unordered graph edges. A face mask has bit j exactly when its j-th edge is selected.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

ORDERS = {
    2: [25, 2, 7, 1, 5, 0, 15, 16, 22, 12, 20, 27, 23, 9, 10, 6, 29, 19, 3, 28, 24, 14, 8, 18, 13, 11, 17, 21, 26, 4],
    3: [13, 3, 16, 12, 29, 0, 11, 21, 26, 27, 28, 22, 19, 25, 18, 15, 10, 23, 14, 20, 8, 2, 1, 9, 5, 17, 24, 7, 4, 6],
}
EXPECTED_VECTORS = {
    2: {0: 1, 1: 30, 2: 255, 3: 620, 4: 315, 5: 30, 6: 5},
    3: {0: 1, 1: 30, 2: 255, 3: 700, 4: 615, 5: 42, 6: 5},
}


def graph(k):
    assert k in (2, 3)
    edges = set()
    for i in range(10):
        for a, b in ((i, (i+1) % 10), (i, i+10), (10+i, 10+(i+k) % 10)):
            edges.add(tuple(sorted((a, b))))
    edges = sorted(edges)
    assert len(edges) == 30
    A = [set() for _ in range(20)]
    for a, b in edges:
        A[a].add(b)
        A[b].add(a)
    assert all(len(a) == 3 for a in A)
    # The half-turn i -> i+5 is a deck involution, and the quotient is Petersen.
    quotient = {tuple(sorted((a % 5 + (5 if a >= 10 else 0),
                              b % 5 + (5 if b >= 10 else 0)))) for a, b in edges}
    petersen = set()
    for i in range(5):
        for a, b in ((i, (i+1) % 5), (i, i+5), (5+i, 5+(i+2) % 5)):
            petersen.add(tuple(sorted((a, b))))
    assert quotient == petersen and len(quotient) == 15
    assert all(sum(1 for a, b in edges
                   if tuple(sorted((a % 5 + (5 if a >= 10 else 0),
                                    b % 5 + (5 if b >= 10 else 0)))) == e) == 2
               for e in quotient)
    return edges, A


def masks_by_independent_insertion(edges, A):
    """Construct face set by hereditary extension, with graph-endpoint tests."""
    faces = [0]
    endpoints = [set(e) for e in edges]
    for j, (a, b) in enumerate(edges):
        new = []
        for mask in faces:
            vertices = set().union(*(endpoints[i] for i in range(j) if mask & (1 << i)))
            if not vertices.intersection((a, b)) and all(
                x not in A[a] and x not in A[b] for x in vertices
            ):
                new.append(mask | (1 << j))
        faces += new
    assert len(faces) == len(set(faces))
    return set(faces)


def masks_by_combinations(edges, A):
    """Independent exhaustive subset test through cardinality seven.

    All larger faces contain a seven-face. Thus verifying that none exists
    at seven makes this an exhaustive enumeration of the full complex.
    """
    conflict = [[False] * len(edges) for _ in edges]
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            conflict[i][j] = bool(i != j and (
                a in (c, d) or b in (c, d) or
                c in A[a] or d in A[a] or c in A[b] or d in A[b]))
    faces = {0}
    seven = 0
    for r in range(1, 8):
        for chosen in combinations(range(len(edges)), r):
            if any(conflict[i][j] for i, j in combinations(chosen, 2)):
                continue
            if r == 7:
                seven += 1
            else:
                faces.add(sum(1 << i for i in chosen))
    assert seven == 0
    return faces


def toggle_matching(faces, order):
    """Each stage pairs exactly those currently unpaired cells differing by one bit."""
    assert sorted(order) == list(range(30))
    free = set(faces)
    pairs = []
    for j in order:
        bit = 1 << j
        lows = sorted(mask for mask in free if not (mask & bit) and (mask | bit) in free)
        for low in lows:
            high = low | bit
            assert low in free and high in free
            free.remove(low)
            free.remove(high)
            pairs.append((low, high))
    assert 2 * len(pairs) + len(free) == len(faces)
    return pairs, free


def acyclic_hasse(faces, pairs):
    """Check complete augmented directed Hasse graph by Kahn topological sort."""
    matched = set(pairs)
    indegree = {mask: 0 for mask in faces}
    arcs = {mask: [] for mask in faces}
    total = 0
    for high in faces:
        x = high
        while x:
            bit = x & -x
            x -= bit
            low = high - bit
            if (low, high) in matched:
                src, dst = low, high
            else:
                src, dst = high, low
            arcs[src].append(dst)
            indegree[dst] += 1
            total += 1
    queue = deque(mask for mask, degree in indegree.items() if degree == 0)
    popped = 0
    while queue:
        src = queue.popleft()
        popped += 1
        for dst in arcs[src]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
    assert popped == len(faces), (popped, len(faces))
    return total


def boundary_rank_mod2(faces, degree):
    lower = sorted(s for s in faces if s.bit_count() == degree)
    higher = sorted(s for s in faces if s.bit_count() == degree+1)
    index = {s: i for i, s in enumerate(lower)}
    pivots = {}
    for high in higher:
        col = 0
        x = high
        while x:
            bit = x & -x
            x -= bit
            col ^= 1 << index[high - bit]
        while col:
            p = col.bit_length()-1
            if p not in pivots:
                pivots[p] = col
                break
            col ^= pivots[p]
    return len(pivots)


def run(k):
    edges, A = graph(k)
    faces = masks_by_independent_insertion(edges, A)
    assert faces == masks_by_combinations(edges, A)
    f = Counter(mask.bit_count() for mask in faces)
    assert dict(f) == EXPECTED_VECTORS[k], (k, dict(f))
    pairs, remaining = toggle_matching(faces, ORDERS[k])
    assert set(mask.bit_count()-1 for mask in remaining) == {k}
    assert len(remaining) == 104
    empty_pair = [pair for pair in pairs if pair[0] == 0]
    assert len(empty_pair) == 1
    assert len(pairs) == (len(faces)-104)//2
    incidences = acyclic_hasse(faces, pairs)
    betti = {}
    rank = {}
    for d in range(1, 7):
        rank[d] = boundary_rank_mod2(faces, d)
    for dim in range(0, 6):
        betti[dim] = f[dim+1] - rank.get(dim, 0) - rank.get(dim+1, 0)
    assert betti == {dim: (104 if dim == k else (1 if dim == 0 else 0)) for dim in range(6)}
    # Following deletion of the empty-face pair, exactly one critical vertex remains.
    assert empty_pair[0][1].bit_count() == 1
    print(f'GP(10,{k}): 20 vertices, 30 edges, {len(faces)} augmented faces')
    print('    face counts by cardinality 0..6: ' + ','.join(str(f[i]) for i in range(7)))
    print(f'    toggled pairs {len(pairs)}; directed Hasse incidences {incidences}; acyclic YES')
    print(f'    critical after empty-pair deletion: one 0-cell and 104 {k}-cells')
    print(f'    mod-2 Betti numbers degrees 0..5: {[betti[d] for d in range(6)]}')


if __name__ == '__main__':
    for k in (2, 3):
        run(k)
    print('VERIFY_OK')
