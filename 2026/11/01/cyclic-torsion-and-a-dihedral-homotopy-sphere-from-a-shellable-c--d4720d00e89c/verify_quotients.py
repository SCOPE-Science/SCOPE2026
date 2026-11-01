#!/usr/bin/env python3
"""Exact quotient chain computation for a sixteen-vertex independence complex.

Requires Python 3 and SymPy.  Run: python verify_quotients.py
All graph, group, chain and boundary data are reconstructed from definitions.
The numerical facet order is a directly checked shelling certificate.
Earl--Vander Meulen--Van Tuyl (2015) originally proved shellability.
"""
import itertools
from collections import Counter
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 16
STEPS = {1, 4, 8}
SHELLING = '''
4 10 13 15 2 4 13 15 2 8 13 15 8 10 13 15 2 4 9 15 4 6 9 15 4 6 13 15
6 8 13 15 2 4 7 13 2 4 7 9 4 7 10 13 6 9 12 15 2 9 12 15 2 7 9 12
1 6 8 15 1 8 10 15 1 6 12 15 1 10 12 15 1 4 10 15 1 4 6 15 1 4 7 10
3 8 10 13 1 3 8 10 3 6 8 13 1 3 6 8 1 3 6 12 1 3 10 12 3 6 9 12
2 5 8 15 2 5 12 15 5 10 12 15 5 8 10 15 3 5 10 12 3 5 8 10 2 5 7 12
3 5 12 14 1 3 12 14 1 3 8 14 3 5 8 14 5 7 12 14 3 9 12 14 7 9 12 14
4 7 9 14 0 3 5 10 0 3 5 14 0 5 7 14 0 3 9 14 0 7 9 14 0 2 7 9
0 2 5 7 0 3 10 13 0 3 6 13 0 3 6 9 2 8 11 13 6 8 11 13 2 5 8 11
5 8 11 14 4 6 11 13 2 4 11 13 0 5 11 14 0 2 5 11 0 2 9 11 0 9 11 14
2 4 9 11 4 9 11 14 4 6 9 11 0 6 9 11 0 6 11 13 0 2 11 13 0 2 7 13
0 7 10 13 0 5 7 10 5 7 10 12 1 7 10 12 1 7 12 14 1 4 7 14 1 6 8 11
1 4 6 11 1 8 11 14 1 4 11 14
'''

def independent(face):
    return all(min((a-b)%N, (b-a)%N) not in STEPS
               for a, b in itertools.combinations(face, 2))

faces = sorted(tuple(comb) for k in range(1, N+1)
               for comb in itertools.combinations(range(N), k)
               if independent(comb))
by_size = Counter(map(len, faces))
assert by_size == {1:16, 2:80, 3:144, 4:80}, by_size
facet_set = {f for f in faces if len(f) == 4}
nums = list(map(int, SHELLING.split()))
assert len(nums) == 320
shells = [tuple(sorted(nums[4*j:4*j+4])) for j in range(80)]
assert set(shells) == facet_set and len(set(shells)) == 80
seen = set()
for j, facet in enumerate(shells):
    existing_triangles = {t for t in itertools.combinations(facet, 3) if t in seen}
    if j > 0:
        assert existing_triangles, (j, 'empty codimension-one overlap')
        for k in range(1, 4):
            for face in itertools.combinations(facet, k):
                if face in seen:
                    assert any(set(face).issubset(t) for t in existing_triangles), (j,face)
    for k in range(1, 5):
        seen.update(itertools.combinations(facet, k))
assert seen == set(faces)
print('K_faces', [by_size[k] for k in range(1,5)])
print('shelling_check', 'PASS', 'facets', len(shells),
      'reduced_euler',sum((-1)**(len(f)-1) for f in faces)-1)

# A simplicial chain of nonempty faces of K is a simplex in sd(K).
chains = [set() for _ in range(4)]
for facet in facet_set:
    subs = [tuple(t) for k in range(1,5) for t in itertools.combinations(facet,k)]
    for k in range(1,5):
        for seq in itertools.combinations(subs,k):
            if all(set(seq[i]) < set(seq[i+1]) for i in range(k-1)):
                chains[k-1].add(seq)
chains = [sorted(c) for c in chains]
assert list(map(len, chains)) == [320,2144,3744,1920]
print('sd_faces',list(map(len,chains)))

# Rotation g=(k,+1): v -> v+k. Reflection g=(k,-1): v -> k-v.
rotation_group = [(k,1) for k in range(16)]
dihedral_group = [(k,s) for s in (1,-1) for k in range(16)]

def transformed(chain,g):
    k,s = g
    return tuple(tuple(sorted((k+s*x)%16 for x in face)) for face in chain)

# Invariance: every graph symmetry preserves every simplex and every flag.
for g in dihedral_group:
    assert {transformed((face,),g)[0] for face in faces} == set(faces)
# A nontrivial rotation has no invariant nonempty face; both reflections
# k=0 and k=1 have fixed points in the geometric realization.
for g in rotation_group[1:]:
    assert not any(transformed((f,),g)[0] == f for f in faces)
assert transformed(((0,),),(0,-1)) == ((0,),)
assert transformed(((2,15),),(1,-1)) == ((2,15),)
print('rotation_free',True,'reflection_fixed_witnesses',[(0,),(2,15)])

for name,group in [('cyclic16',rotation_group),('dihedral32',dihedral_group)]:
    def compute():
        representatives=[];orbit_index=[]
        for dim,cells in enumerate(chains):
            cells_set=set(cells)
            ids={};reps=[]
            for cell in cells:
                if cell in ids:continue
                ix=len(reps);reps.append(cell)
                for g in group:
                    gc=transformed(cell,g)
                    assert gc in cells_set
                    ids[gc]=ix
            assert len(ids)==len(cells)
            representatives.append(reps);orbit_index.append(ids)
        counts=list(map(len,representatives))
        boundaries=[]
        for d in range(1,4):
            entries={}
            for j,c in enumerate(representatives[d]):
                for i in range(d+1):
                    a=orbit_index[d-1][c[:i]+c[i+1:]]
                    entries[a,j]=entries.get((a,j),0)+(-1)**i
            entries={k:v for k,v in entries.items() if v}
            boundaries.append(SparseMatrix(counts[d-1],counts[d],entries))
        return counts,boundaries
    count, B=compute()
    assert (B[0]*B[1]).is_zero_matrix and (B[1]*B[2]).is_zero_matrix
    inv=[]
    for M in B:
        D=smith_normal_form(M,domain=ZZ)
        invariants=Counter(abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i])
        inv.append(dict(sorted(invariants.items())))
    assert sum((-1)**j*count[j] for j in range(4)) == 0
    ranks=[sum(v.values()) for v in inv]
    betti=[count[0]-ranks[0],count[1]-ranks[0]-ranks[1],
           count[2]-ranks[1]-ranks[2],count[3]-ranks[2]]
    assert betti==[1,0,0,1]
    if name=='cyclic16':
        assert inv == [{1:19},{1:114,16:1},{1:119}]
    else:
        assert inv == [{1:15},{1:58},{1:59}]
    print(name,'cells',count,'smith',inv,'betti_rational',betti)
print('VERIFY_OK')
