#!/usr/bin/env python3
"""Exact finite Morse certificate for width-three rectangular perfect-matching complexes.

No third-party modules are needed. Run: python verify_three_row_perfect_matching.py
All face-set and directed-Hasse checks are exhaustive, not random sampling.
"""
from collections import Counter, deque
from functools import lru_cache

CASES = {
    2: dict(tilings=3, faces=20, arcs=34, steps=((4, 7), (6, 3)), critical=()),
    4: dict(tilings=11, faces=495, arcs=1679, steps=((8, 164), (14, 83)), critical=(20480,)),
    6: dict(tilings=41, faces=12375, arcs=62994,
            steps=((12, 4089), (22, 2088), (16, 7), (26, 3)), critical=(5505024,)),
    8: dict(tilings=153, faces=309480, arcs=2101259,
            steps=((16, 102249), (30, 52233), (22, 171), (36, 86)),
            critical=(1426063360, 70078431232)),
}


def ordered_grid_edges(n):
    # Grid vertices are numbered r*n+c, 0<=r<3, 0<=c<n.
    # Edge IDs: first vertical edges, then horizontal edges, both row-major.
    vertical = [(r*n+c, (r+1)*n+c) for r in range(2) for c in range(n)]
    horizontal = [(r*n+c, r*n+c+1) for r in range(3) for c in range(n-1)]
    return vertical + horizontal


def perfect_matchings(n, edges):
    adj = [[] for _ in range(3*n)]
    for eid, (u, v) in enumerate(edges):
        adj[u].append((eid, v))
        adj[v].append((eid, u))
    result = []
    def visit(free, matching):
        if not free:
            result.append(matching)
            return
        u = min(free)
        for eid, v in adj[u]:
            if v in free:
                visit(free - {u, v}, matching | (1 << eid))
    visit(set(range(3*n)), 0)
    assert len(set(result)) == len(result)
    for matching in result:
        assert matching.bit_count() == 3*n//2
        covered = 0
        for eid, (u, v) in enumerate(edges):
            if matching & (1 << eid):
                assert not (covered & ((1 << u) | (1 << v)))
                covered |= (1 << u) | (1 << v)
        assert covered == (1 << (3*n)) - 1
    return result


def profile_tilings(n):
    # Independent enumeration: transfer through columns, tracking the three
    # squares already covered by horizontal dominoes from the preceding column.
    @lru_cache(maxsize=None)
    def count(col, incoming):
        if col == n:
            return int(incoming == 0)
        def fill(row, occupied, next_mask):
            if row == 3:
                return count(col+1, next_mask)
            if occupied & (1 << row):
                return fill(row+1, occupied, next_mask)
            total = 0
            if row + 1 < 3 and not occupied & (1 << (row+1)):
                total += fill(row+2, occupied | (3 << row), next_mask)
            if col+1 < n:
                total += fill(row+1, occupied | (1 << row), next_mask | (1 << row))
            return total
        return fill(0, incoming, 0)
    return count(0, 0)


def generated_complex(facets):
    faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub-1) & facet
    return faces


def stage_matching(faces, n_edges):
    remaining = set(faces)
    mate = {}
    stage_list = []
    while True:
        chosen = -1
        lowers = []
        # Find an edge ID maximizing the number of currently pairable faces.
        # Ties are resolved by the smallest edge ID.
        for v in range(n_edges):
            bit = 1 << v
            candidates = [f for f in remaining if not (f & bit) and ((f | bit) in remaining)]
            if len(candidates) > len(lowers):
                chosen, lowers = v, candidates
        if not lowers:
            break
        bit = 1 << chosen
        for f in lowers:
            mate[f] = f | bit
            mate[f | bit] = f
        remaining.difference_update(lowers)
        remaining.difference_update(f | bit for f in lowers)
        stage_list.append((chosen, len(lowers)))
    return mate, remaining, tuple(stage_list)


def exact_acyclicity(faces, mate, n_edges):
    # Every codimension-one face relation contributes one oriented arrow.
    # Reverse the arrows belonging to matched pairs. A topological sort
    # succeeds if and only if the resulting directed Hasse graph is acyclic.
    assert len(mate) == len(faces) - len(set(faces)-set(mate))
    for f, other in mate.items():
        assert mate.get(other) == f
        assert abs(f.bit_count() - other.bit_count()) == 1
        assert (f | other) in (f, other)
    bit_values = [1 << i for i in range(n_edges)]
    indegree = {}
    for f in faces:
        mf = mate.get(f)
        # One incoming arrow from the paired lower face, if present.
        val = int(mf is not None and mf.bit_count() == f.bit_count()-1)
        for bit in bit_values:
            higher = f | bit
            if higher != f and higher in faces and mf != higher:
                val += 1
        indegree[f] = val
    queue = deque(f for f in faces if indegree[f] == 0)
    processed = 0
    while queue:
        f = queue.popleft()
        processed += 1
        partner = mate.get(f)
        if partner is not None and partner.bit_count() == f.bit_count()+1:
            indegree[partner] -= 1
            assert indegree[partner] >= 0
            if indegree[partner] == 0:
                queue.append(partner)
        # All unpaired facets receive downward arrows from f.
        for bit in bit_values:
            if not (f & bit):
                continue
            lower = f & ~bit
            if lower in faces and partner != lower:
                indegree[lower] -= 1
                assert indegree[lower] >= 0
                if indegree[lower] == 0:
                    queue.append(lower)
    assert processed == len(faces), (processed, len(faces))
    assert all(v == 0 for v in indegree.values())
    return processed


def independent_mod_two_betti(faces):
    """Recompute reduced homology using ordinary simplicial boundary matrices."""
    by_dimension = {}
    for f in faces:
        by_dimension.setdefault(f.bit_count()-1, []).append(f)
    ranks = {}
    for d in sorted(k for k in by_dimension if k >= 0):
        below = {f:i for i,f in enumerate(by_dimension[d-1])} if d>0 else {0:0}
        pivot = {}
        for f in by_dimension[d]:
            column = 0
            for i in range(f.bit_length()):
                if f & (1 << i):
                    column ^= 1 << below[f & ~(1 << i)]
            while column:
                p = column.bit_length() - 1
                if p not in pivot:
                    pivot[p] = column
                    break
                column ^= pivot[p]
        ranks[d] = len(pivot)
    return {d:len(by_dimension[d])-ranks[d]-ranks.get(d+1,0)
            for d in by_dimension if d >= 0}


def verify(n):
    expected = CASES[n]
    edges = ordered_grid_edges(n)
    assert len(edges) == 5*n-3
    tilings = perfect_matchings(n, edges)
    assert len(tilings) == profile_tilings(n) == expected['tilings']
    complex_faces = generated_complex(tilings)
    assert len(complex_faces) == expected['faces']
    assert sum(f.bit_count() for f in complex_faces) == expected['arcs']
    mate, critical, steps = stage_matching(complex_faces, len(edges))
    assert steps == expected['steps'], (n, steps)
    assert tuple(sorted(critical)) == expected['critical']
    assert len(mate) + len(critical) == len(complex_faces)
    assert len(mate) % 2 == 0
    assert set(mate).isdisjoint(critical)
    assert not set(mate).difference(complex_faces)
    sorted_faces = Counter(f.bit_count()-1 for f in complex_faces)
    # The augmented Euler characteristic is the alternating sum including
    # the empty simplex, of dimension -1.
    euler = sum((-1 if dim%2 else 1)*count for dim,count in sorted_faces.items())
    predicted = sum((-1 if (f.bit_count()-1)%2 else 1) for f in critical)
    assert euler == predicted
    order_size = exact_acyclicity(complex_faces, mate, len(edges))
    if n <= 6:
        betti = independent_mod_two_betti(complex_faces)
        assert betti == {d:(int(n >= 4 and d == n//2-1)) for d in betti}

    # The unique pair containing the empty simplex disappears on removing
    # the augmentation, producing one critical ordinary 0-cell.
    assert 0 in mate and mate[0].bit_count() == 1
    assert all(x.bit_count()-1 == n//2-1 for x in critical)
    assert len(critical) == (0,1,1,2)[n//2-1]
    print('n=%d tilings=%d faces=%d pairs=%d critical=%s hasse_arcs=%d topo_sorted=%d reduced_euler=%d' %
          (n,len(tilings),len(complex_faces),len(mate)//2,
           sorted(f.bit_count()-1 for f in critical),expected['arcs'],order_size,euler))


if __name__ == '__main__':
    for n in (2,4,6,8):
        verify(n)
    print('VERIFICATION_OK four exhaustive grid cases')
