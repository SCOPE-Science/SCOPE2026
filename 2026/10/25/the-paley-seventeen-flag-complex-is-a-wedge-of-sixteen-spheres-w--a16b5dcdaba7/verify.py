#!/usr/bin/env python3
"""Exact finite certificate for the Paley-17 flag complex.
No optional dependencies: python3 verify.py
"""
from itertools import combinations
from collections import Counter

p = 17
R = {x*x % p for x in range(1,p)}
assert R == {1,2,4,8,9,13,15,16}
V = list(range(p))
def edge(a,b): return a != b and (b-a)%p in R
E = [e for e in combinations(V,2) if edge(*e)]
T = [t for t in combinations(V,3) if all(edge(*z) for z in combinations(t,2))]
assert (len(V), len(E), len(T)) == (17,68,68)
assert not any(all(edge(*z) for z in combinations(f,2)) for f in combinations(V,4))
Eset = set(E)
Tedge=[set(combinations(t,2)) for t in T]
# Fixed spanning-tree and triangular-relator elimination sequence. Each selected
# triangle meets the currently unknown non-tree edges in exactly one edge.
tree = [(0,1),(0,2),(0,4),(0,8),(0,9),(0,13),(0,15),(0,16),
        (1,3),(1,5),(1,10),(1,14),(2,6),(2,11),(4,12),(7,8)]
order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
         20,21,22,23,24,25,26,27,28,29,33,34,35,36,37,38,39,
         41,44,45,40,30,31,32,42,46,47,49,52,56,59,61]
assert len(order) == 52 and len(set(order)) == 52
assert len(tree) == 16 and len(set(tree))==16 and set(tree)<=Eset
# Check spanning tree by integral graph reachability.
reached={0}
while True:
    update = reached | {v for u,v in tree if u in reached} | {u for u,v in tree if v in reached}
    if update == reached:break
    reached=update
assert len(reached)==17
killed=set(tree)
for i in order:
    unknown=Tedge[i]-killed
    assert len(unknown)==1, (i,unknown)
    killed.update(unknown)
assert killed==Eset
# This triangular elimination is a unimodular 52x52 minor of the
# simplicial 2-boundary, and gives an explicit contraction of pi_1.
# Together with 16 tree edges, establishes integral H_1=0, and
# top H_2 free of rank 68-52=16.
# For an affine graph automorphism, calculate signed chain traces:
# on an invariant simplex sign is permutation parity of its vertices.
def sign_on_face(f,g):
    moved=[g[x] for x in f]
    if sorted(moved)!=list(f):return 0
    return (-1)**sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
records=Counter()
for a in sorted(R):
    for b in V:
        g={x:(a*x+b)%p for x in V}
        assert all(edge(*e)==edge(g[e[0]],g[e[1]]) for e in combinations(V,2))
        traces=[sum(sign_on_face(f,g) for f in faces) for faces in ([tuple([v]) for v in V],E,T)]
        h2=traces[0]-traces[1]+traces[2]-1
        fix=sum(g[v]==v for v in V)
        assert h2==fix-1, ((a,b),traces,h2,fix)
        key=('identity' if a==1 and b==0 else 'translation' if a==1 else 'nontranslation')
        records[key,h2]+=1
assert records == {('identity',16):1,('translation',-1):16,('nontranslation',0):119},records
print('FACES',len(V),len(E),len(T),'TETRAHEDRA',0)
print('PI1_ELIMINATION_TREE',len(tree),'UNIT_TRIANGLE_RELATORS',len(order))
print('INTEGRAL_HOMOLOGY_H1',0,'H2_FREE',16)
print('AFFINE_GROUP',17*len(R),'CHARACTER_COUNTS',dict(records))
print('VERIFY_OK_PALEY17_FLAG_HOMOTOPY_CHARACTER')
