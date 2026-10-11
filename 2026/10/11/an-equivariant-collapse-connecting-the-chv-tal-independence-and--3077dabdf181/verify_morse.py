#!/usr/bin/env python3
"""Finite certificate for the ordinary open-neighborhood complex of a specified graph.
No external dependencies. Run with Python >=3.9.
"""
from collections import Counter, deque
from pathlib import Path
import json

EDGES = (
    (0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),
    (2,3),(2,6),(2,8),(3,4),(3,7),(3,9),
    (4,5),(4,8),(5,10),(5,11),(6,10),(6,11),
    (7,8),(7,11),(8,10),(9,10),(9,11),
)
N = 12

def neighborhoods():
    nb = [set() for _ in range(N)]
    for a,b in EDGES:
        assert 0 <= a < b < N
        nb[a].add(b)
        nb[b].add(a)
    return nb

def complex_faces():
    nb = neighborhoods()
    faces = set()
    for i in range(N):
        m = sum(1 << j for j in nb[i])
        sub = m
        while sub:
            faces.add(sub)
            sub = (sub - 1) & m
    return faces

def matching(faces):
    unmatched = set(faces)
    pairs = []
    for i in range(N):
        bit = 1 << i
        for lo in sorted(tuple(unmatched), key=lambda q: (q.bit_count(), q)):
            hi = lo | bit
            if lo in unmatched and not (lo & bit) and hi in unmatched:
                assert lo != 0
                unmatched.remove(lo)
                unmatched.remove(hi)
                pairs.append((lo, hi))
    return unmatched, pairs

def acyclic(faces, pairs):
    # In a matched cover the lower face points upwards; otherwise upper points downwards.
    matched = set(pairs)
    succ = {q: [] for q in faces}
    indeg = {q: 0 for q in faces}
    incidence_count = 0
    for hi in faces:
        x = hi
        while x:
            bit = x & -x
            lo = hi ^ bit
            x -= bit
            if not lo: continue  # ordinary non-augmented face poset
            incidence_count += 1
            u,v = (lo,hi) if (lo,hi) in matched else (hi,lo)
            succ[u].append(v)
            indeg[v] += 1
    queue = deque(q for q in faces if indeg[q] == 0)
    topo = 0
    while queue:
        v = queue.popleft();topo+=1
        for w in succ[v]:
            indeg[w] -= 1
            if indeg[w] == 0: queue.append(w)
    assert topo == len(faces), (topo,len(faces))
    return incidence_count,topo

def main():
    nbh = neighborhoods()
    assert len(EDGES) == 24 and {len(nb) for nb in nbh} == {4}
    F = complex_faces()
    assert len(F) == 110
    fvec = {d: sum(m.bit_count()-1==d for m in F) for d in range(4)}
    assert fvec == {0:12,1:42,2:44,3:12}, fvec
    critical,pairs = matching(F)
    certificate = json.loads((Path(__file__).parent/'MORSE_CERTIFICATE.json').read_text(encoding='utf-8'))
    assert certificate['face_masks'] == sorted(F)
    assert certificate['matched_cover_pairs'] == [list(x) for x in pairs]
    assert certificate['critical_face_masks'] == sorted(critical)
    assert len(pairs) == 54, len(pairs)
    critical_by_dim = Counter(t.bit_count()-1 for t in critical)
    assert critical_by_dim == {0:1,2:1}, critical_by_dim
    assert not any((lo in critical or hi in critical) for lo,hi in pairs)
    assert len({q for pair in pairs for q in pair}) == 2*len(pairs)
    incidence_count,topo = acyclic(F,pairs)
    assert sum((-1)**(d)*fvec[d] for d in fvec) == 2
    print('MORSE_OK faces=%d f_vector=%s pairs=%d critical=%s incidence=%d topo=%d'
          % (len(F),[fvec[d] for d in range(4)],len(pairs),
             sorted([(x.bit_count()-1,x) for x in critical]),incidence_count,topo))
    print('CRITICAL_FACES', sorted(critical))
    print('MATCHED_PAIRS_MASKS',pairs)

if __name__ == '__main__': main()
