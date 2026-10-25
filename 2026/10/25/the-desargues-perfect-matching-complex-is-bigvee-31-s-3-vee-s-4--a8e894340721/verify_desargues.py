#!/usr/bin/env python3
"""Exact, dependency-free verification for the Desargues perfect-matching complex.

The graph and ordered cells are generated canonically; all integer operations
are exact. No previously recorded computational data is used.
"""
from collections import Counter, deque
from functools import lru_cache
import json


def graph():
    n = 10
    edges = set()
    for i in range(n):
        for a, b in ((i, (i + 1) % n),
                     (i, 10 + i),
                     (10 + i, 10 + (i + 3) % n)):
            edges.add(tuple(sorted((a, b))))
    edges = sorted(edges)
    assert len(edges) == 30 and len({v for e in edges for v in e}) == 20
    return edges


def matchings_and_faces(edges):
    nbr = [[] for _ in range(20)]
    for i, (a, b) in enumerate(edges):
        nbr[a].append((b, i))
        nbr[b].append((a, i))

    def generate(remaining):
        if not remaining:
            yield 0
            return
        a = (remaining & -remaining).bit_length() - 1
        for b, e in nbr[a]:
            if remaining & (1 << b):
                for rest in generate(remaining ^ (1 << a) ^ (1 << b)):
                    yield rest | (1 << e)

    perfect = sorted(generate((1 << 20) - 1))
    assert len(perfect) == len(set(perfect)) == 60
    assert all(m.bit_count() == 10 for m in perfect)

    @lru_cache(None)
    def count_by_remaining(remaining):
        if remaining == 0:
            return 1
        a = (remaining & -remaining).bit_length() - 1
        return sum(count_by_remaining(remaining ^ (1 << a) ^ (1 << b))
                   for b, e in nbr[a] if remaining & (1 << b))

    assert count_by_remaining((1 << 20) - 1) == len(perfect)

    faces = {0}
    for p in perfect:
        sub = p
        while sub:
            faces.add(sub)
            sub = (sub - 1) & p
    counts = Counter(m.bit_count() for m in faces if m)
    assert tuple(counts[k] for k in range(1, 11)) == (
        30, 375, 2320, 7320, 12096, 11700, 7080, 2700, 600, 60)
    assert len(faces) == 44282
    return nbr, perfect, faces, counts


def sequential_matching(faces):
    unpaired = set(faces)
    unpaired.remove(0)
    partner = {}
    for e in range(30):
        bit = 1 << e
        # The complete fixed-order element matching at each stage.
        for f in sorted(unpaired):
            g = f | bit
            if (f & bit) == 0 and g in unpaired:
                partner[f] = g
                unpaired.remove(f)
                unpaired.remove(g)
    counts = Counter(f.bit_count() - 1 for f in unpaired)
    assert counts == {0: 1, 3: 42, 4: 12}
    assert len(partner) == 22113
    return partner, unpaired


def acyclic_check(faces, partner):
    # Every codimension-one incidence is oriented downward except for
    # matched incidences, which are oriented upward.
    indegree = {f: 0 for f in faces if f}
    edges_count = 0
    for f in faces:
        if f == 0:
            continue
        for e in range(30):
            if f & (1 << e):
                g = f ^ (1 << e)
                if g == 0:
                    continue
                edges_count += 1
                if partner.get(g) == f:
                    indegree[f] += 1
                else:
                    indegree[g] += 1
    queue = deque(f for f, deg in indegree.items() if deg == 0)
    seen = 0
    while queue:
        f = queue.popleft()
        seen += 1
        # Upward matched edge, if f is its lower endpoint.
        g = partner.get(f)
        if g is not None:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
        # All downward incidences except an edge reversed by matching.
        for e in range(30):
            if f & (1 << e):
                g = f ^ (1 << e)
                if g and partner.get(g) != f:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        queue.append(g)
    assert seen == len(faces) - 1
    assert edges_count == 244830
    return edges_count


def sign_in_boundary(upper, deleted):
    return -1 if ((upper & ((1 << deleted) - 1)).bit_count() % 2) else 1


def signed_morse_boundary(unpaired, partner):
    critical_3 = sorted(f for f in unpaired if f.bit_count() == 4)
    critical_4 = sorted(f for f in unpaired if f.bit_count() == 5)
    indices = {f: i for i, f in enumerate(critical_3)}
    paired_upper = set(partner.values())

    @lru_cache(None)
    def project(face):
        if face in indices:
            return {indices[face]: 1}
        if face in paired_upper:
            return {}
        assert face in partner
        upper = partner[face]
        added = (upper ^ face).bit_length() - 1
        eps = sign_in_boundary(upper, added)
        ans = {}
        for i in range(30):
            if (upper & (1 << i)) and i != added:
                coefficient = -eps * sign_in_boundary(upper, i)
                for row, val in project(upper ^ (1 << i)).items():
                    ans[row] = ans.get(row, 0) + coefficient * val
        return {r: a for r, a in ans.items() if a}

    mat = [[0 for _ in critical_4] for _ in critical_3]
    for j, upper in enumerate(critical_4):
        for i in range(30):
            if upper & (1 << i):
                coeff = sign_in_boundary(upper, i)
                for r, val in project(upper ^ (1 << i)).items():
                    mat[r][j] += coeff * val
    nonzero = [(i, j, a) for i, row in enumerate(mat)
               for j, a in enumerate(row) if a]
    assert len(nonzero) == 64
    assert max(abs(a) for i, j, a in nonzero) == 1
    return critical_3, critical_4, mat, nonzero


def integral_unit_pivots(matrix):
    """Unimodular elementary changes of bases prove diag(I, 0)."""
    a = [row[:] for row in matrix]
    nr, nc = len(a), len(a[0])
    pivots = []
    k = 0
    while k < min(nr, nc):
        loc = next(((i, j) for i in range(k, nr)
                    for j in range(k, nc) if abs(a[i][j]) == 1), None)
        if loc is None:
            break
        i, j = loc
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        if a[k][k] == -1:
            a[k] = [-v for v in a[k]]
        for r in range(nr):
            if r != k:
                z = a[r][k]
                if z:
                    a[r] = [x - z * y for x, y in zip(a[r], a[k])]
        for c in range(nc):
            if c != k:
                z = a[k][c]
                if z:
                    for r in range(nr):
                        a[r][c] -= z * a[r][k]
        assert a[k][k] == 1
        assert all(a[r][k] == (r == k) for r in range(nr))
        assert all(a[k][c] == (c == k) for c in range(nc))
        pivots.append([i, j])
        k += 1
    assert len(pivots) == 11
    assert all(a[i][j] == (1 if i == j and i < 11 else 0)
               for i in range(nr) for j in range(nc))
    return pivots


def matching_obstructions(edges, faces):
    ends = [(1 << a) | (1 << b) for a, b in edges]
    ordinary = set()

    def rec(last, occupied, edge_mask):
        ordinary.add(edge_mask)
        for e in range(last + 1, 30):
            if not (occupied & ends[e]):
                rec(e, occupied | ends[e], edge_mask | (1 << e))

    rec(-1, 0, 0)
    assert len(ordinary) == 113192
    assert faces <= ordinary
    missing = ordinary - faces
    assert len(missing) == 68910
    minimal = [m for m in missing if all(
        (m ^ (1 << e)) in faces for e in range(30) if m & (1 << e))]
    assert dict(Counter(m.bit_count() for m in minimal)) == {3: 220, 4: 180}
    return len(ordinary), len(missing), len(minimal)


def main():
    edges = graph()
    _, perfect, faces, fv = matchings_and_faces(edges)
    partner, crit = sequential_matching(faces)
    incidences = acyclic_check(faces, partner)
    c3, c4, mat, nz = signed_morse_boundary(crit, partner)
    pivots = integral_unit_pivots(mat)
    ordinary, nonextendable, minimal = matching_obstructions(edges, faces)
    euler = sum(((-1) ** (k - 1)) * fv[k] for k in range(1, 11))
    assert euler == -29
    report = {
        'graph': 'GP(10,3)', 'graph_vertices': 20, 'graph_edges': len(edges),
        'perfect_matchings': len(perfect), 'simplices_nonempty': len(faces)-1,
        'f_vector': [fv[k] for k in range(1, 11)],
        'ordinary_matchings_including_empty': ordinary,
        'ordinary_nonextendable_matchings': nonextendable,
        'minimal_nonextendable_matchings': minimal,
        'morse_pairs': len(partner), 'critical_cells_by_dimension': {'0': 1, '3': 42, '4': 12},
        'hasse_incidences_nonempty': incidences,
        'morse_boundary_shape': [len(c3), len(c4)],
        'morse_boundary_nonzero_entries': len(nz),
        'unit_smith_factors': len(pivots),
        'remaining_free_dimensions': {'3': 31, '4': 1},
        'euler_characteristic': euler,
        'status': 'VERIFY_OK'
    }
    print(json.dumps(report, sort_keys=True))
    return json.loads(json.dumps({'edges': edges, 'critical3': c3, 'critical4': c4,
            'boundary_triplets': nz, 'unit_pivots_at_elimination_steps': pivots}))

if __name__ == '__main__':
    import sys
    reconstructed = main()
    if len(sys.argv) == 3 and sys.argv[1] == '--certificate':
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            expected = json.load(f)
        assert reconstructed == expected
        print('CERTIFICATE_OK')
    else:
        assert len(sys.argv) == 1, 'usage: verify_desargues.py [--certificate CERTIFICATE.json]'
# An optional supplied certificate is checked against a fresh exact reconstruction.
# It is not required for standalone proof replay.
