#!/usr/bin/env python3
"""Exact exhaustive finite certificate for the Clebsch dominance complex.

Run with Python 3.10 or later in the same directory as matching_pairs.tsv and
critical_faces.txt.  No third-party dependencies or network access required.
"""
from collections import Counter, deque
from pathlib import Path

N = 16
STEPS = (1, 2, 4, 8, 15)
FULL = (1 << N) - 1

def graph():
    adjacency = [set() for _ in range(N)]
    for a in range(N):
        for move in STEPS:
            adjacency[a].add(a ^ move)
    assert all(len(s) == 5 and i not in s for i, s in enumerate(adjacency))
    assert all(i in adjacency[j] for i in range(N) for j in adjacency[i])
    for a in range(N):
        for b in range(a+1, N):
            assert len(adjacency[a] & adjacency[b]) == (0 if b in adjacency[a] else 2)
    return adjacency

def independent_face_models(adjacency):
    closed = [sum(1 << w for w in (nbr | {v}))
              for v, nbr in enumerate(adjacency)]
    by_forbidden = {s for s in range(FULL+1)
                    if all(s & mask != mask for mask in closed)}
    # Independently test the original definition, using complementary vertex sets.
    by_dominating = set()
    for s in range(FULL+1):
        complement = {v for v in range(N) if not (s >> v) & 1}
        if all((v in complement) or bool(adjacency[v] & complement)
               for v in range(N)):
            by_dominating.add(s)
    assert by_forbidden == by_dominating
    return by_forbidden

def deterministic_matching(faces):
    unmatched = set(faces) - {0}
    pairs = []
    stages = []
    for vertex in range(N):
        bit = 1 << vertex
        stage_pairs = [(s, s | bit) for s in sorted(unmatched)
                       if not (s & bit) and (s | bit) in unmatched]
        for lo, hi in stage_pairs:
            assert lo in unmatched and hi in unmatched
            assert hi == lo | bit
            unmatched.remove(lo)
            unmatched.remove(hi)
        pairs.extend(stage_pairs)
        stages.append(len(stage_pairs))
    return pairs, unmatched, stages

def acyclicity(faces, pairs):
    """Construct every Hasse edge with Forman matching orientations.

    Ordinary cover: higher-dimensional face -> codimension-one face.
    Reversed paired cover: lower-dimensional face -> higher-dimensional face.
    A topological ordering of this complete digraph proves acyclicity.
    """
    face_to_id = {s:i for i,s in enumerate(sorted(faces - {0}))}
    paired_up = {lo:hi for lo,hi in pairs}
    assert len(paired_up) == len(pairs)
    indegree = [0] * len(face_to_id)
    outbound = [[] for _ in face_to_id]
    cover_count = 0
    for hi in face_to_id:
        current = hi
        while current:
            bit = current & -current
            lo = hi ^ bit
            if lo != 0:
                cover_count += 1
                if paired_up.get(lo) == hi:
                    src, dst = lo, hi
                else:
                    src, dst = hi, lo
                a, b = face_to_id[src], face_to_id[dst]
                outbound[a].append(b)
                indegree[b] += 1
            current -= bit
    queue = deque(k for k,v in enumerate(indegree) if v == 0)
    seen = 0
    while queue:
        a = queue.popleft()
        seen += 1
        for b in outbound[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                queue.append(b)
    assert seen == len(face_to_id), f'Directed cycle: {seen}/{len(face_to_id)}'
    return cover_count, seen

def read_pairs():
    text = Path(__file__).with_name('matching_pairs.tsv').read_text('utf-8')
    assert text.endswith('\n')
    return [tuple(map(int,line.split('\t'))) for line in text.splitlines()]

def read_critical():
    text = Path(__file__).with_name('critical_faces.txt').read_text('utf-8')
    assert text.endswith('\n')
    return {int(s) for s in text.splitlines()}

def main():
    adjacency = graph()
    faces = independent_face_models(adjacency)
    fvector = Counter(s.bit_count()-1 for s in faces)
    expected = {-1:1, 0:16,1:120,2:560,3:1820,4:4368,
                5:7992,6:11280,7:12150,8:9520,9:4768,10:1056,11:80}
    assert dict(fvector) == expected
    pairs, critical, stages = deterministic_matching(faces)
    assert pairs == read_pairs()
    assert critical == read_critical()
    assert len(pairs) == 26799
    assert Counter(s.bit_count()-1 for s in critical) == {0:1,9:131}
    assert len(set.union({lo for lo,hi in pairs},
                         {hi for lo,hi in pairs}, critical)) == len(faces)-1
    assert len({x for pair in pairs for x in pair}) == 2 * len(pairs)
    covers, seen = acyclicity(faces, pairs)
    assert sum((-1)**dim*ct for dim,ct in fvector.items() if dim >= 0) == -130
    print('graph=Clebsch_FQ5, degree=5, strongly_regular=(16,5,0,2)')
    print('nonempty_faces=', len(faces)-1)
    print('f_vector=', [fvector[d] for d in range(12)])
    print('matching_pairs=', len(pairs))
    print('stage_pairs=', stages)
    print('critical_vector=',dict(sorted(Counter(s.bit_count()-1 for s in critical).items())))
    print('cover_edges=',covers,'topological_order_vertices=',seen)
    print('reduced_Euler=',-131)
    print('conclusion=one_0_cell_and_131_9_cells; wedge_of_131_S9')

if __name__ == '__main__':
    main()
