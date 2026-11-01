"""Exact finite proof for the two-independence complex of the dodecahedral graph.

Only the Python standard library is required. All simplices and all Hasse
incidences are constructed explicitly; no numerical rank inference is used.
"""
from collections import Counter, deque
from itertools import combinations

N = 20
PIVOTS = (11, 0, 1, 15, 13, 18, 9, 16, 4, 19,
          10, 7, 12, 8, 2, 6, 5, 3, 14, 17)
EXPECTED_F = (20, 190, 1080, 3985, 9772, 15870,
              16640, 10770, 4000, 750, 60, 5)


def edges():
    """The generalized Petersen graph GP(10,2), with u_i=i, v_i=10+i."""
    E = set()
    for i in range(10):
        for a, b in ((i, (i + 1) % 10),
                     (i, 10 + i),
                     (10 + i, 10 + (i + 2) % 10)):
            E.add(tuple(sorted((a, b))))
    assert len(E) == 30
    return E


def neighbors(E):
    out = [0] * N
    for a, b in E:
        out[a] |= (1 << b)
        out[b] |= (1 << a)
    assert all(v.bit_count() == 3 for v in out)
    return out


def faces_recursive(nb):
    """Inductively add vertices only when every induced degree remains <=1."""
    out = [0]
    for v in range(N):
        bit = 1 << v
        additions = []
        for s in out:
            selected_neighbors = s & nb[v]
            if selected_neighbors.bit_count() > 1:
                continue
            if selected_neighbors:
                w = selected_neighbors.bit_length() - 1
                if s & nb[w]:
                    continue
            additions.append(s | bit)
        out.extend(additions)
    return set(out)


def faces_forbidden_triples(nb):
    """Independent full enumeration using the 60 length-two forbidden wedges."""
    bad = set()
    for center in range(N):
        ns = [v for v in range(N) if nb[center] & (1 << v)]
        for a, b in combinations(ns, 2):
            bad.add((1 << a) | (1 << center) | (1 << b))
    assert len(bad) == 60
    out = set()
    for face in range(1 << N):
        if all(face & t != t for t in bad):
            out.add(face)
    return out


def morse_matching(all_faces):
    """Sequential vertex toggles; each pair differs in exactly one vertex."""
    remaining = set(all_faces)
    remaining.remove(0)  # ordinary, unaugmented CW face poset
    pairs = {}
    upper = set()
    per_pivot = []
    for v in PIVOTS:
        bit = 1 << v
        made = 0
        for lo in sorted(remaining):
            hi = lo | bit
            if lo != hi and lo in remaining and hi in remaining:
                assert (hi ^ lo) == bit and hi in all_faces
                pairs[lo] = hi
                upper.add(hi)
                remaining.remove(lo)
                remaining.remove(hi)
                made += 1
        per_pivot.append(made)
    assert not (set(pairs) & upper)
    assert 2 * len(pairs) + len(remaining) == len(all_faces) - 1
    return pairs, remaining, per_pivot


def verify_acyclic(all_faces, pairs):
    """Reverse every matched cover arrow, then exhaustively topologically sort."""
    V = all_faces - {0}
    adj = {f: [] for f in V}
    indegree = {f: 0 for f in V}
    incidence_count = 0
    for high in V:
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if not low:
                continue
            assert low in V
            if pairs.get(low) == high:
                source, target = low, high
            else:
                source, target = high, low
            adj[source].append(target)
            indegree[target] += 1
            incidence_count += 1
    q = deque(x for x in V if indegree[x] == 0)
    processed = 0
    while q:
        x = q.popleft()
        processed += 1
        for y in adj[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert processed == len(V), (processed, len(V))
    assert incidence_count == 410500
    return processed, incidence_count


def main():
    E = edges()
    nb = neighbors(E)
    faces = faces_recursive(nb)
    check = faces_forbidden_triples(nb)
    assert faces == check
    fvector = tuple(sum(f.bit_count() == k + 1 for f in faces) for k in range(12))
    assert fvector == EXPECTED_F
    assert len(faces) == 63143
    facets = [face for face in faces if not any(
        (face | (1 << v)) in faces for v in range(N) if not (face & (1 << v))
    )]
    facet_dimensions = tuple(sorted(Counter(f.bit_count() - 1 for f in facets).items()))
    assert facet_dimensions == ((7, 25), (8, 60), (9, 420), (11, 5))
    reduced_euler = sum(1 if face.bit_count() % 2 else -1 for face in faces)
    assert reduced_euler == 1
    pairs, critical, per_pivot = morse_matching(faces)
    assert len(pairs) == 31570
    assert critical == {1 << 11, 156434}
    assert sorted(face.bit_count() - 1 for face in critical) == [0, 6]
    processed, incidences = verify_acyclic(faces, pairs)
    print('GRAPH_VERTICES=20 GRAPH_EDGES=30 DEGREE=3')
    print('FORBIDDEN_LENGTH_TWO_TRIPLES=60')
    print('ENUMERATION_METHODS_AGREE=True')
    print('F_VECTOR=' + repr(fvector))
    print('NONEMPTY_FACES=' + str(len(faces) - 1))
    print('FACET_DIMENSION_COUNTS=' + repr(facet_dimensions))
    print('REDUCED_EULER=' + str(reduced_euler))
    print('PIVOT_ORDER=' + repr(PIVOTS))
    print('PAIRS_BY_PIVOT=' + repr(tuple(per_pivot)))
    print('MATCHED_PAIRS=' + str(len(pairs)))
    print('CRITICAL_MASKS=' + repr(sorted(critical)))
    print('CRITICAL_DIMENSIONS=' + repr([0, 6]))
    print('HASSE_INCIDENCES=' + str(incidences))
    print('TOPOLOGICAL_SORTED_FACES=' + str(processed))
    print('MATCHING_ACYCLIC=True')
    print('CONCLUSION=homotopy_equivalent_to_S6')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
