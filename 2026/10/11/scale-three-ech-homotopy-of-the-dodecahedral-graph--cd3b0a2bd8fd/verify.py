#!/usr/bin/env python3
"""Exact, standalone verification for the scale-three dodecahedral graph Cech nerve.

Uses integer bit masks, complete face enumeration, full Hasse DAG checking,
exact signed algebraic discrete-Morse boundary recursion, and finite-field
chain ranks. Requires only Python 3 standard library.
"""
from collections import Counter, deque
from functools import lru_cache

N = 20
PIVOT_ORDER = [17, 15, 11, 18, 7, 6, 19, 3, 14, 0,
               9, 5, 16, 8, 13, 2, 1, 12, 4, 10]
EXPECTED_FACE_VECTOR = [20, 150, 380, 410, 180, 30]
EXPECTED_HASSE = 4160
EXPECTED_MATCHED_PAIRS = 578
EXPECTED_CRITICAL_DIMENSIONS = {0: 1, 2: 1, 3: 12}
EXPECTED_BOUNDARY_RANKS = {1: 19, 2: 131, 3: 248, 4: 150, 5: 30}


def graph():
    edges = set()
    for i in range(10):
        for x, y in ((i, (i + 1) % 10),
                     (i, 10 + i),
                     (10 + i, 10 + (i + 2) % 10)):
            edges.add(tuple(sorted((x, y))))
    assert len(edges) == 30
    degree = Counter(v for e in edges for v in e)
    assert len(degree) == N and set(degree.values()) == {3}
    return sorted(edges)


def faces():
    edges = graph()
    neighbor = [1 << i for i in range(N)]
    for u, v in edges:
        neighbor[u] |= 1 << v
        neighbor[v] |= 1 << u
    facets = {neighbor[u] | neighbor[v] for u, v in edges}
    assert len(facets) == 30
    assert all(f.bit_count() == 6 for f in facets)
    assert all(not (a != b and (a & b) == a)
               for a in facets for b in facets)
    all_faces = {0}
    for facet in facets:
        s = facet
        while s:
            all_faces.add(s)
            s = (s - 1) & facet
    by_dim = {d: sorted(f for f in all_faces if f and f.bit_count() == d + 1)
              for d in range(6)}
    assert [len(by_dim[d]) for d in range(6)] == EXPECTED_FACE_VECTOR
    return all_faces, by_dim


def matching(all_faces):
    unmatched = set(all_faces)
    unmatched.remove(0)
    pairs = []
    for v in PIVOT_ORDER:
        bit = 1 << v
        for low in sorted(unmatched, key=lambda f: (f.bit_count(), f)):
            high = low | bit
            if not (low & bit) and low in unmatched and high in unmatched:
                assert high.bit_count() == low.bit_count() + 1
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    assert len(pairs) == EXPECTED_MATCHED_PAIRS
    profile = dict(Counter(f.bit_count() - 1 for f in unmatched))
    assert profile == EXPECTED_CRITICAL_DIMENSIONS, profile
    assert len(all_faces) - 1 == 2 * len(pairs) + len(unmatched)
    return pairs, unmatched


def hasse_acyclic(all_faces, pairs):
    faces_nonempty = all_faces - {0}
    matched = set(pairs)
    indegree = {f: 0 for f in faces_nonempty}
    out = {f: [] for f in faces_nonempty}
    incidence_count = 0
    for high in faces_nonempty:
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if low == 0:
                continue
            assert low in faces_nonempty
            incidence_count += 1
            source, target = (low, high) if (low, high) in matched else (high, low)
            out[source].append(target)
            indegree[target] += 1
    assert incidence_count == EXPECTED_HASSE
    q = deque(x for x in faces_nonempty if indegree[x] == 0)
    visited = 0
    while q:
        source = q.popleft()
        visited += 1
        for target in out[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                q.append(target)
    assert visited == len(faces_nonempty), (visited, len(faces_nonempty))
    return incidence_count


def oriented_faces(simplex):
    """Sorted-vertex orientation: delete vertex number j with coefficient (-1)^j."""
    bits = simplex
    j = 0
    while bits:
        bit = bits & -bits
        bits -= bit
        yield simplex ^ bit, (1 if j % 2 == 0 else -1)
        j += 1


def critical_three_boundary(pairs, critical):
    low_partner = dict(pairs)
    high_partner = {high: low for low, high in pairs}
    critical_two = {f for f in critical if f.bit_count() == 3}
    critical_three = sorted(f for f in critical if f.bit_count() == 4)
    assert len(critical_two) == 1 and len(critical_three) == 12

    @lru_cache(None)
    def projection(two_face):
        if two_face in critical_two:
            return {two_face: 1}
        if two_face in high_partner:
            # A matched upper two-cell is killed with its paired one-cell.
            return {}
        assert two_face in low_partner, two_face
        partner_three = low_partner[two_face]
        boundary = dict(oriented_faces(partner_three))
        pivot = boundary[two_face]
        assert abs(pivot) == 1
        result = Counter()
        for alternate_face, sign in boundary.items():
            if alternate_face != two_face:
                for critical_face, coefficient in projection(alternate_face).items():
                    result[critical_face] += -pivot * sign * coefficient
        return {k: v for k, v in result.items() if v != 0}

    entries = {}
    for simplex in critical_three:
        boundary_coeffs = Counter()
        for triangle, sign in oriented_faces(simplex):
            for critical_face, coefficient in projection(triangle).items():
                boundary_coeffs[critical_face] += sign * coefficient
        entries[simplex] = {f: v for f, v in boundary_coeffs.items() if v}
    assert all(not x for x in entries.values()), entries
    return entries


def rank_mod_p(columns, modulus):
    pivots = {}
    for column in columns:
        work = {row: coef % modulus for row, coef in column.items() if coef % modulus}
        while work:
            row = max(work)
            pivot = pivots.get(row)
            if pivot is None:
                inv = pow(work[row], -1, modulus)
                pivots[row] = {j: (v * inv) % modulus for j, v in work.items()}
                break
            coefficient = work[row]
            for j, val in pivot.items():
                new = (work.get(j, 0) - coefficient * val) % modulus
                if new:
                    work[j] = new
                else:
                    work.pop(j, None)
    return len(pivots)


def check_chain_ranks(by_dim):
    ranks_by_modulus = {}
    for p in (2, 3):
        ranks = {}
        for dim in range(1, 6):
            basis = {face: idx for idx, face in enumerate(by_dim[dim - 1])}
            columns = []
            for f in by_dim[dim]:
                col = {basis[s]: sign for s, sign in oriented_faces(f)}
                columns.append(col)
            ranks[dim] = rank_mod_p(columns, p)
        assert ranks == EXPECTED_BOUNDARY_RANKS, (p, ranks)
        reduced_betti = {}
        for d in range(6):
            b = len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            if d == 0:
                b -= 1
            reduced_betti[d] = b
        assert reduced_betti == {0: 0, 1: 0, 2: 1, 3: 12, 4: 0, 5: 0}
        ranks_by_modulus[p] = ranks
    return ranks_by_modulus


def main():
    all_faces, by_dim = faces()
    pairs, critical = matching(all_faces)
    hasse_acyclic(all_faces, pairs)
    critical_three_boundary(pairs, critical)
    check_chain_ranks(by_dim)
    assert sum((-1)**d * len(by_dim[d]) for d in range(6)) == -10
    print('VERIFY_OK')
    print('vertices=20 edges=30 facets=30 nonempty_faces=1170 Hasse=4160')
    print('f_vector=' + repr(EXPECTED_FACE_VECTOR))
    print('pairs=578 critical={0:1,2:1,3:12} integer_Morse_d3=zero')
    print('mod2_and_mod3_boundary_ranks=' + repr(EXPECTED_BOUNDARY_RANKS))


if __name__ == '__main__':
    main()
