"""Exact integral multipath homology of the bidirected K_{2,4}."""
from collections import Counter
from itertools import combinations
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

LEFT=(0,1)
RIGHT=(2,3,4,5)
ARCS=tuple((a,b) for a in LEFT for b in RIGHT)+tuple((b,a) for b in RIGHT for a in LEFT)
assert len(ARCS)==16

def admissible(indices):
    outgoing={};incoming={}
    for j in indices:
        a,b=ARCS[j]
        if a in outgoing or b in incoming:return False
        outgoing[a]=b;incoming[b]=a
    for first in range(6):
        seen=set();v=first
        while v in outgoing:
            if v in seen:return False
            seen.add(v);v=outgoing[v]
    return True

faces=[list(comb for comb in combinations(range(16),size) if admissible(comb)) for size in range(5)]
assert [len(c) for c in faces]==[1,16,80,144,72]
assert not any(admissible(comb) for comb in combinations(range(16),5))
print('face_counts', [len(c) for c in faces])

matrices=[]
for size in range(1,5):
    row_index={f:i for i,f in enumerate(faces[size-1])}
    entries={}
    for column,face in enumerate(faces[size]):
        for k in range(size):
            entries[(row_index[face[:k]+face[k+1:]],column)]=(-1)**k
    d=SparseMatrix(len(faces[size-1]),len(faces[size]),entries)
    matrices.append(d)
    form=smith_normal_form(d,domain=ZZ)
    nz=Counter(abs(int(form[i,i])) for i in range(min(form.shape)) if form[i,i])
    print('boundary',size-1, 'shape', d.shape, 'nonzero_smith',sorted(nz.items()))
    if size>=2:assert matrices[-2]*d==SparseMatrix(matrices[-2].rows,d.cols,{})

assert matrices[0].shape==(1,16)
assert all(v==1 for v in matrices[0])
expected=[{1:1},{1:15},{1:65},{1:71,2:1}]
# C_{-1} <- C_0 <- C_1 <- C_2 <- C_3, with reduced augmentation.
for d,expect in zip(matrices,expected):
    S=smith_normal_form(d,domain=ZZ)
    observed=dict(Counter(abs(int(S[j,j])) for j in range(min(S.shape)) if S[j,j]))
    assert observed==expect,(observed,expect)
print('reduced_integral_homology',{'H_2_free_rank':7,'H_2_torsion':['Z/2'],'all_other_reduced_degrees':'zero'})
