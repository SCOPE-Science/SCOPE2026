"""Independent incidence-configuration construction of the same graph.

The eight-point, eight-line configuration has cyclic incidence shifts
{0,1,3}; the explicit bijection below certifies its graph isomorphism
to generalized Petersen G(8,3). Standard-library Python 3 only.
"""
from collections import Counter
m=16
G=set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        G.add(tuple(sorted((a,b))))
H={tuple(sorted((i,8+(i+d)%8))) for i in range(8) for d in (0,1,3)}
assert len(G)==len(H)==24
p=[0,11,2,13,4,15,6,9,8,3,10,5,12,7,14,1]
assert sorted(p)==list(range(m))
assert {tuple(sorted((p[a],p[b]))) for a,b in G}==H
neighbors=[{b for a,b in H if a==v}|{a for a,b in H if b==v} for v in range(m)]
assert all(len(a)==3 for a in neighbors)
counts=Counter()
chi_reduced=-1
for s in range(1<<m):
    complement={v for v in range(m) if not s>>v&1}
    if all(v in complement or neighbors[v]&complement for v in range(m)):
        if s:
            d=s.bit_count()-1
            counts[d]+=1
            chi_reduced+=(-1)**d
assert [counts[i] for i in range(12)]==[16,120,560,1804,4176,6976,8208,6462,3136,832,96,4]
assert chi_reduced==-7
print('Independent cyclic configuration check: PASS')
print('incidence edges:',len(H),'isomorphism witness:',p)
print('fvector:',[counts[i] for i in range(12)])
print('reduced Euler characteristic:',chi_reduced)
