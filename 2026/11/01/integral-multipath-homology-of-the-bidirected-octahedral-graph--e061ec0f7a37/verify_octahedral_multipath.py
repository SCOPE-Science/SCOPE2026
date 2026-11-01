#!/usr/bin/env python3
"""Exact integral multipath-chain certificate for the bidirected octahedron.

The graph has vertices {0,...,5}, with opposite pairs (0,1), (2,3),
(4,5). Every remaining undirected edge is replaced by its two arcs.
No external packages are needed. Run with Python 3.10 or newer.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product

V = tuple(range(6))
PART = (0, 0, 1, 1, 2, 2)
ARCS = tuple(sorted((u, v) for u in V for v in V if PART[u] != PART[v]))
assert len(ARCS) == 24
N = len(ARCS)


def admissible(mask):
    """A directed edge set is a disjoint union of isolated vertices and paths."""
    indeg = [0] * 6
    outdeg = [0] * 6
    nxt = [-1] * 6
    for j, (u, v) in enumerate(ARCS):
        if mask >> j & 1:
            indeg[v] += 1
            outdeg[u] += 1
            if indeg[v] > 1 or outdeg[u] > 1:
                return False
            nxt[u] = v
    for origin in V:
        seen = set()
        u = origin
        while u != -1:
            if u in seen:
                return False
            seen.add(u)
            u = nxt[u]
    return True



def independent_union_find_test(mask):
    """Second validity criterion: vertex degrees and undirected forest."""
    parent = list(V)
    indeg = [0] * 6
    outdeg = [0] * 6
    def root(u):
        while parent[u] != u:
            u = parent[u]
        return u
    for j, (u, v) in enumerate(ARCS):
        if mask >> j & 1:
            indeg[v] += 1
            outdeg[u] += 1
            if indeg[v] > 1 or outdeg[u] > 1:
                return False
            a, b = root(u), root(v)
            if a == b:
                return False
            parent[a] = b
    return True


def enumerate_by_edges():
    # Every multipath has at most five arcs, since six arcs would force
    # a directed cycle (each nonisolated component must be a path).
    ans = {0}
    for size in range(1, 6):
        for choose in combinations(range(N), size):
            mask = sum(1 << k for k in choose)
            if admissible(mask):
                ans.add(mask)
    return ans


def enumerate_by_outgoing_choices():
    # A distinct enumeration: for each of the six graph vertices choose
    # either no outgoing arc or one of its four legal outgoing arcs.
    candidates = []
    arc_index = {arc: i for i, arc in enumerate(ARCS)}
    for u in V:
        candidates.append((-1,) + tuple(v for v in V if PART[u] != PART[v]))
    ans = set()
    assert len(list(product(*candidates))) == 15625
    for choices in product(*candidates):
        targets = [v for v in choices if v != -1]
        if len(set(targets)) != len(targets):
            continue
        mask = sum(1 << arc_index[(u, v)] for u, v in enumerate(choices) if v != -1)
        if independent_union_find_test(mask):
            ans.add(mask)
    return ans


def topo_check(faces, pairs):
    pairset = set(pairs)
    indegree = {f: 0 for f in faces}
    adj = defaultdict(list)
    arrows = 0
    for upper in faces:
        for j in range(N):
            if not (upper >> j & 1):
                continue
            lower = upper ^ (1 << j)
            if not lower:
                continue
            start, end = (lower, upper) if (lower, upper) in pairset else (upper, lower)
            adj[start].append(end)
            indegree[end] += 1
            arrows += 1
    q = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while q:
        f = q.popleft()
        visited += 1
        for v in adj[f]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert visited == len(faces), (visited, len(faces))
    return arrows


def lexicographic_matching(faces):
    alive = set(faces)
    pairs = []
    for index in range(N):
        bit = 1 << index
        for low in sorted(alive, key=lambda m: (m.bit_count(), m)):
            if low not in alive or (low & bit):
                continue
            high = low | bit
            if high in alive:
                alive.remove(low)
                alive.remove(high)
                pairs.append((low, high))
    assert len(alive) + 2 * len(pairs) == len(faces)
    return pairs, alive


def boundary_column(face):
    """Signed simplicial boundary with ascending directed-arc order."""
    out = {}
    sign = 1
    for j in range(N):
        if face >> j & 1:
            smaller = face ^ (1 << j)
            if smaller:
                out[smaller] = sign
            sign = -sign
    return out


def integer_morse(faces, pairs):
    # A unit Schur-complement cancellation is a chain homotopy equivalence.
    # Retain each differential as dictionary: upper face -> lower coefficients.
    maps = {
        size: {f: boundary_column(f) for f in faces if f.bit_count() == size}
        for size in range(1, 6)
    }
    pending = set(pairs)
    removed = 0
    while pending:
        chosen = None
        for low, high in sorted(pending, key=lambda p: (p[1].bit_count(), p[1])):
            d = high.bit_count()
            if abs(maps[d][high].get(low, 0)) == 1:
                chosen = (low, high)
                break
        assert chosen is not None, "The acyclic matching must yield another unit pivot"
        low, high = chosen
        d = high.bit_count()
        pivot = maps[d][high][low]  # +1 or -1
        col = maps[d][high]
        for other, bc in list(maps[d].items()):
            if other == high:
                continue
            coeff = bc.get(low, 0)
            if not coeff:
                continue
            for target, value in col.items():
                new_value = bc.get(target, 0) - coeff * pivot * value
                if new_value:
                    bc[target] = new_value
                else:
                    bc.pop(target, None)
        del maps[d][high]
        maps[d-1].pop(low, None)
        if d + 1 in maps:
            for bc in maps[d+1].values():
                bc.pop(high, None)
        pending.remove(chosen)
        removed += 1
    assert removed == 835
    return maps


def verify_chain_condition(maps):
    for size in range(3, 6):
        for upper, col in maps[size].items():
            composed = Counter()
            for middle, v in col.items():
                for lower, w in maps[size - 1][middle].items():
                    composed[lower] += v * w
            assert all(v == 0 for v in composed.values())


def unit_diagonalization(maps):
    # Integral elementary row/column operations. If all residual entries
    # become zero after 9 unit pivots, the cokernel has no torsion.
    columns = sorted(maps[4])
    rows = sorted(maps[3])
    A = [[maps[4][c].get(r, 0) for c in columns] for r in rows]
    R, C = len(rows), len(columns)
    units = 0
    for k in range(min(R, C)):
        pos = next(((i, j) for i in range(k, R) for j in range(k, C)
                    if abs(A[i][j]) == 1), None)
        if pos is None:
            break
        i, j = pos
        A[k], A[i] = A[i], A[k]
        for row in A:
            row[k], row[j] = row[j], row[k]
        if A[k][k] == -1:
            A[k] = [-v for v in A[k]]
        assert A[k][k] == 1
        for i in range(k + 1, R):
            coeff = A[i][k]
            if coeff:
                A[i] = [x - coeff * y for x, y in zip(A[i], A[k])]
        for j in range(k + 1, C):
            coeff = A[k][j]
            if coeff:
                for i in range(R):
                    A[i][j] -= coeff * A[i][k]
        assert all(A[i][k] == 0 for i in range(k+1, R))
        assert all(A[k][j] == 0 for j in range(k+1, C))
        units += 1
    assert units == 9
    assert all(A[i][j] == 0 for i in range(units, R) for j in range(units, C))
    return units


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        v = col
        while v:
            i = v.bit_length() - 1
            if i in pivots:
                v ^= pivots[i]
            else:
                pivots[i] = v
                break
    return len(pivots)


def direct_mod2_ranks(faces):
    result = {}
    for size in range(2, 6):
        lower = sorted(f for f in faces if f.bit_count() == size - 1)
        index = {f: j for j, f in enumerate(lower)}
        cols = []
        for upper in sorted(f for f in faces if f.bit_count() == size):
            v = 0
            for bit in range(N):
                if upper >> bit & 1:
                    v ^= 1 << index[upper ^ (1 << bit)]
            cols.append(v)
        result[size - 1] = mod2_rank(cols)
    return result


def main():
    family = enumerate_by_edges()
    second = enumerate_by_outgoing_choices()
    assert family == second
    faces = family - {0}
    fvector = tuple(sum(f.bit_count() == i for f in faces) for i in range(1, 6))
    assert fvector == (24, 192, 616, 744, 240)
    pairs, critical = lexicographic_matching(faces)
    assert len(pairs) == 835
    critical_counts = tuple(sum(f.bit_count() == i for f in critical) for i in range(1, 6))
    assert critical_counts == (1, 0, 12, 101, 32)
    incidences = topo_check(faces, pairs)
    maps = integer_morse(faces, pairs)
    assert all(set(maps[size]) == {f for f in critical if f.bit_count() == size}
               for size in range(1, 6))
    verify_chain_condition(maps)
    assert sum(len(b) for b in maps[3].values()) == 0
    assert sum(len(b) for b in maps[5].values()) == 0
    assert sum(len(b) for b in maps[4].values()) == 257
    units = unit_diagonalization(maps)
    ranks2 = direct_mod2_ranks(faces)
    assert ranks2 == {1: 23, 2: 169, 3: 444, 4: 208}
    # Homology: one 0-cell; and chain ranks 12,101,32 in degrees 2,3,4.
    # Only nonzero differential is the 12x101 matrix with nine unit pivots.
    betti = {2: 12 - units, 3: 101 - units, 4: 32}
    assert betti == {2: 3, 3: 92, 4: 32}
    assert sum((-1)**(i-1)*fvector[i-1] for i in range(1, 6)) == -56
    assert sum((-1)**d*r for d,r in betti.items()) == -57
    print('Directed arcs:', N)
    print('Independent edge-subset and outgoing-function enumerations: AGREE')
    print('Nonempty faces by dimension 0..4:', fvector)
    print('Hasse incidences checked:', incidences)
    print('Morse matched pairs:', len(pairs))
    print('Critical cells by dimension 0..4:', critical_counts)
    print('Directed Hasse acyclicity: PASS')
    print('Reduced signed Morse chain dimensions: (1,0,12,101,32)')
    print('Nonzero Morse boundary: 12 x 101 with 257 coefficients')
    print('Integral unit pivots / residual rank:', units, '/', 0)
    print('Other Morse boundaries: ZERO')
    print('Direct mod-2 simplicial boundary ranks:', tuple(ranks2[d] for d in range(1,5)))
    print('Integral reduced Betti numbers degrees 2,3,4:', tuple(betti[d] for d in (2,3,4)))
    print('All integral torsion: ABSENT')
    print('OCTAHEDRAL_MULTIPATH_INTEGRAL_HOMOLOGY_VERIFIED')


if __name__ == '__main__':
    main()
