#!/usr/bin/env python3
"""Independent complete verification that the Chvatal independence complex collapses
in a graph-automorphism-invariant set of eight elementary pairs to its
ordinary open-neighborhood complex. All intermediate faces are explicit.
"""
import itertools
from collections import Counter
from verify_independent import NB,VERTICES,all_automorphisms,face_tuples

def face(mask):return tuple(i for i in VERTICES if mask>>i&1)
def mask(t):return sum(1<<i for i in t)

def compute():
    indep = set()
    for q in range(1,1<<12):
        vv=face(q)
        if all(v not in NB[u] for u,v in itertools.combinations(vv,2)):
            indep.add(q)
    nbrhd={mask(a) for s in face_tuples().values() for a in s}
    assert nbrhd <= indep
    assert Counter(q.bit_count()-1 for q in indep)=={0:12,1:42,2:52,3:20}
    assert Counter(q.bit_count()-1 for q in nbrhd)=={0:12,1:42,2:44,3:12}
    extra=indep-nbrhd
    tri={q for q in extra if q.bit_count()==3}
    tet={q for q in extra if q.bit_count()==4}
    assert len(extra)==16 and len(tri)==len(tet)==8
    pair={}
    for f in tri:
        tops=[t for t in indep if t.bit_count()==4 and (t & f)==f]
        assert len(tops)==1, (f,tops)
        assert tops[0] in tet
        pair[f]=tops[0]
    assert len(set(pair.values()))==8
    assert { (x,y) for x,y in pair.items() } == set((f,t) for t in tet for f in tri if t&f==f)
    # Every pair consists of a free triangle and its unique facet coface.
    # A fixed orbit of pairwise disjoint pairs is a D4-equivariant elementary collapse.
    automorphisms=all_automorphisms()
    seed=min(pair)
    orbit={mask(p[i] for i in face(seed)) for p in automorphisms}
    assert orbit==set(pair), (orbit,set(pair))
    for p in automorphisms:
        def move(q):return mask(p[i] for i in face(q))
        assert {move(q) for q in indep} == indep
        assert {move(q) for q in nbrhd} == nbrhd
        assert {(move(f),move(t)) for f,t in pair.items()} == set(pair.items())
    for lo,hi in pair.items():
        stabilizer_lower={i for i,p in enumerate(automorphisms) if mask(p[j] for j in face(lo))==lo}
        stabilizer_upper={i for i,p in enumerate(automorphisms) if mask(p[j] for j in face(hi))==hi}
        assert stabilizer_lower==stabilizer_upper and len(stabilizer_lower)==1
    print('COLLAPSE_OK independent=%d neighborhood=%d free_pairs=%d automorphisms=%d' % (len(indep),len(nbrhd),len(pair),len(automorphisms)))
    print('EXTRA_TRIANGLES_AND_TETRAHEDRA',sorted((face(f),face(t)) for f,t in pair.items()))
    return indep,nbrhd,pair
if __name__=='__main__':compute()
