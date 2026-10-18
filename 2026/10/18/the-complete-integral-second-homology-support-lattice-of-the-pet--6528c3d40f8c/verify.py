#!/usr/bin/env python3
"""Exact finite checks for the Petersen independence-complex support classification.
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from collections import Counter

V = list(combinations(range(5), 2))
position = {e:i for i,e in enumerate(V)}
N = len(V)
conflict = [sum(1<<j for j in range(N) if j != i and not (set(V[i]) & set(V[j]))) for i in range(N)]
faces = [f for f in range(1,1<<N) if all(not (conflict[i] & f) for i in range(N) if f >> i & 1)]
assert Counter(f.bit_count() for f in faces) == {1:10,2:30,3:30,4:5}

def rank2(col_vectors):
    basis={}
    for v in col_vectors:
        while v:
            pivot=v.bit_length()-1
            if pivot in basis: v ^= basis[pivot]
            else: basis[pivot]=v; break
    return len(basis)

def get_homology2(m):
    tri=[f for f in faces if f.bit_count()==3 and f&m==f]
    edg=[f for f in faces if f.bit_count()==2 and f&m==f]
    tetra=[f for f in faces if f.bit_count()==4 and f&m==f]
    edge_id={f:i for i,f in enumerate(edg)}
    tri_id={f:i for i,f in enumerate(tri)}
    d2=[sum(1<<edge_id[f^(1<<i)] for i in range(N) if f>>i&1) for f in tri]
    d3=[sum(1<<tri_id[f^(1<<i)] for i in range(N) if f>>i&1) for f in tetra]
    return len(tri) - rank2(d2) - rank2(d3)

profile=Counter(); good_six=[]
for m in range(1<<N):
    missing=[e for e in V if not (m >> position[e]&1)]
    expected = 4 if not missing else sum(all(i in edge for edge in missing) for i in range(5))
    actual=get_homology2(m)
    assert actual==expected, ('H2 mismatch',m,missing,expected,actual)
    profile[(m.bit_count(),actual)]+=1
    if m.bit_count()==6 and actual: good_six.append(m)
assert len(good_six)==5
expected_six = [sum(1<<position[e] for e in V if i not in e) for i in range(5)]
assert set(good_six)==set(expected_six)
assert get_homology2((1<<N)-1)==4
# Independently verify concentration of reduced homology in degree two.
by_dim={k:[f for f in faces if f.bit_count()==k+1] for k in range(4)}
full_ranks={}
for k in (1,2,3):
    lower={f:j for j,f in enumerate(by_dim[k-1])}
    cols=[sum(1<<lower[f^(1<<j)] for j in range(N) if f>>j&1) for f in by_dim[k]]
    full_ranks[k]=rank2(cols)
assert (full_ranks[1],full_ranks[2],full_ranks[3])==(9,21,5)
assert len(by_dim[1])-full_ranks[1]-full_ranks[2]==0
assert len(by_dim[3])-full_ranks[3]==0

# Construct each fundamental 2-cycle as the oriented boundary of the
# tetrahedron on the four labels other than i, using the triangle-coordinate model.
triangles=list(combinations(range(5),3)); tri_index={t:j for j,t in enumerate(triangles)}
tetrahedra=[tuple(j for j in range(5) if j!=i) for i in range(5)]
columns=[]
for f in tetrahedra:
    vec=0
    for t in combinations(f,3):vec ^= 1<<tri_index[t]
    columns.append(vec)
assert rank2(columns)==4
for omit in range(5):
    assert rank2([columns[i] for i in range(5) if i!=omit])==4
assert (columns[0]^columns[1]^columns[2]^columns[3]^columns[4])==0

# Independent character computation by signed simplicial Lefschetz trace.
def perm_sign(arr):
    inversions=sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))
    return -1 if inversions%2 else 1
character_counter=Counter()
for p in permutations(range(5)):
    acted=[position[tuple(sorted((p[a],p[b])))] for a,b in V]
    reduced_lefschetz=-1
    for f in faces:
        verts=[i for i in range(N) if f>>i&1]
        images=[acted[i] for i in verts]
        if set(verts)!=set(images):continue
        # permutation of a fixed simplex, expressed relative to sorted vertex ordering
        positions={v:j for j,v in enumerate(verts)}
        sgn=perm_sign([positions[v] for v in images])
        reduced_lefschetz += ((-1)**(len(verts)-1))*sgn
    expected=perm_sign(p)*(sum(p[i]==i for i in range(5))-1)
    assert reduced_lefschetz==expected,(p,reduced_lefschetz,expected)
    character_counter[reduced_lefschetz]+=1
assert sum(character_counter.values())==120
print('VERIFY_OK PETERSEN_INDEPENDENCE F_VECTOR_10_30_30_5 1024_SUBSETS')
print('MINIMAL_CARRIERS_5 SIX_VERTICES INTEGRAL_RELATION_MODEL_RANK_4')
print('INDUCED_H2_PROFILE',sorted((k,dict(sorted((r,c) for (v,r),c in profile.items() if v==k))) for k in range(11)))
print('S5_SIGN_TWISTED_STANDARD CHARACTER_HISTOGRAM',sorted(character_counter.items()))
