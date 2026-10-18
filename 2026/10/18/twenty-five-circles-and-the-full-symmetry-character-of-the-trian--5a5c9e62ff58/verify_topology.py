#!/usr/bin/env python3
"""Exact finite checks for the strong discrete-Morse complex of a graph prism.

Run with Python 3.10+ in the directory containing prism_morse_certificate.json.
No external dependencies or network access are required.
"""
import itertools
import collections
import json
from pathlib import Path

N = 6
EDGES = {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5),
         (0, 3), (1, 4), (2, 5)}
ARCS = sorted((v, u) for a, b in EDGES for v, u in ((a, b), (b, a)))
AIDX = {a: i for i, a in enumerate(ARCS)}
ADJ = [set() for _ in range(N)]
for a, b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)


def generated_match(order):
    earlier = set()
    out = 0
    for v in order:
        link = ADJ[v] & earlier
        if len(link) == 1:
            parent, = link
            out |= 1 << AIDX[(v, parent)]
        earlier.add(v)
    return out


def downward_closure(facets):
    faces = {0}
    for face in facets:
        t = face
        while t:
            faces.add(t)
            t = (t - 1) & face
    return faces


def greedy_face_matching(faces):
    unmatched = set(faces) - {0}
    pairs = []
    for i in range(len(ARCS)):
        bit = 1 << i
        for low in sorted((x for x in unmatched if not (x & bit)),
                          key=lambda x: (x.bit_count(), x)):
            high = low | bit
            if low in unmatched and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    return pairs, sorted(unmatched)


def check_hasse_acyclicity(faces, pairs):
    nonempty = faces - {0}
    matched = set(pairs)
    assert len(matched) == len(pairs)
    successors = {x: [] for x in nonempty}
    indegree = {x: 0 for x in nonempty}
    covers = 0
    for high in nonempty:
        for i in range(len(ARCS)):
            if (high >> i) & 1:
                low = high & ~(1 << i)
                if low:
                    # Reverse a matched covering edge; otherwise high -> low.
                    p, q = ((low, high) if (low, high) in matched
                            else (high, low))
                    successors[p].append(q)
                    indegree[q] += 1
                    covers += 1
    queue = collections.deque(x for x in nonempty if indegree[x] == 0)
    removed = 0
    while queue:
        x = queue.popleft()
        removed += 1
        for y in successors[x]:
            indegree[y] -= 1
            if not indegree[y]:
                queue.append(y)
    assert removed == len(nonempty), 'Directed face-poset cycle detected'
    return covers, removed


def main():
    generated = {generated_match(p) for p in itertools.permutations(range(N))}
    facets = {f for f in generated if not any(
        f != g and f & g == f for g in generated)}
    faces = downward_closure(facets)
    counts = collections.Counter(f.bit_count() - 1 for f in faces if f)
    facet_counts = collections.Counter(f.bit_count() - 1 for f in facets)
    assert len(ARCS) == 18
    assert len(generated) >= len(facets)
    assert len(facets) == 36 and dict(facet_counts) == {1: 12, 2: 24}
    assert dict(counts) == {0: 18, 1: 66, 2: 24}
    assert len(faces) == 109
    pairs, critical = greedy_face_matching(faces)
    assert len(pairs) == 41 and len(critical) == 26
    assert collections.Counter(f.bit_count()-1 for f in critical) == {0: 1, 1: 25}
    assert all(a in faces and b in faces and a & b == a and
               b.bit_count() == a.bit_count()+1 for a, b in pairs)
    covers, visited = check_hasse_acyclicity(faces, pairs)
    assert (covers, visited) == (204, 108)

    cert = json.loads(Path('prism_morse_certificate.json').read_text(encoding='utf-8'))
    assert cert['arcs'] == [list(arc) for arc in ARCS]
    assert cert['facets'] == sorted(facets)
    assert cert['matched_pairs'] == [list(pair) for pair in pairs]
    assert cert['critical_faces'] == critical
    assert cert['hasse_covers'] == covers

    print('GRAPH_VERTICES=6 GRAPH_EDGES=9 VERTEX_ORDERINGS=720')
    print('ARCS=18 FACETS=36 (EDGES=12 TRIANGLES=24)')
    print('NONEMPTY_FACE_VECTOR=(18,66,24)')
    print('MATCHED_HASSE_PAIRS=41 HASSE_COVERS=204 ACYCLIC_TOPO_SORT=108/108')
    print('CRITICAL_CELLS=(1 vertex,25 edges,0 triangles)')
    print('HOMOTOPY_TYPE=WEDGE_OF_25_CIRCLES')
    print('VERIFY_TOPOLOGY_OK')


if __name__ == '__main__':
    main()
