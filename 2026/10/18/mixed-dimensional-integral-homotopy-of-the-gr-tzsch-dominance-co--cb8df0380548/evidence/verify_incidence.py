"""Independent incidence, facet-generation and mod-2 homology check."""
from collections import Counter
from itertools import combinations

# Construct directly from a symmetric adjacency matrix rather than edge masks.
n=11
matrix=[[0]*n for _ in range(n)]
for j in range(5):
    for a,b in [(j,(j+1)%5),(5+j,(j+4)%5),(5+j,(j+1)%5),(5+j,10)]:
        matrix[a][b]=matrix[b][a]=1
assert sum(map(sum,matrix))==40

def dom(S):
    return all(v in S or any(matrix[v][u] for u in S) for v in range(n))

minimal_dominators=[]
for r in range(n+1):
    for subset in combinations(range(n),r):
        mask=sum(1<<i for i in subset)
        if dom(subset) and all(not dom(tuple(x for x in subset if x!=v)) for v in subset):
            minimal_dominators.append(mask)
full=(1<<n)-1
facets=[full^m for m in minimal_dominators]
complex=set()
for facet in facets:
    sub=facet
    while True:
        complex.add(sub)
        if sub==0:break
        sub=(sub-1)&facet
assert len(complex)==1435
assert all(dom(tuple(i for i in range(n) if (full^s) & (1<<i))) for s in complex)
assert set(s for s in range(1<<n) if dom(tuple(i for i in range(n) if (full^s)&(1<<i))))==complex
faces_by_dim={d:sorted(s for s in complex if s.bit_count()==d+1) for d in range(8)}
# Independent exact GF(2) column reduction for each simplicial boundary.
ranks={}
for d in range(1,8):
    rows={s:i for i,s in enumerate(faces_by_dim[d-1])}
    pivots={}
    for s in faces_by_dim[d]:
        col=0
        for v in range(n):
            if s&(1<<v): col ^= 1 << rows[s^(1<<v)]
        while col:
            p=col.bit_length()-1
            if p not in pivots:
                pivots[p]=col;break
            col^=pivots[p]
    ranks[d]=len(pivots)
betti={d:len(faces_by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(8)}
assert betti=={0:1,1:0,2:0,3:0,4:0,5:1,6:2,7:0}
assert sum(((-1)**d)*len(faces_by_dim[d]) for d in faces_by_dim)==sum(((-1)**d)*betti[d] for d in betti)
print('minimal_dominating_sets',len(minimal_dominators))
print('distinct_facets',len(set(facets)))
print('independently_enumerated_nonempty_faces',len(complex)-1)
print('full_face_vector',tuple(len(faces_by_dim[d]) for d in range(8)))
print('mod2_boundary_ranks',tuple(ranks[d] for d in range(1,8)))
print('mod2_betti',tuple(betti[d] for d in range(8)))
print('VERIFY_OK')
# A second field tests the signed orientation convention independently.
prime=3
ranks3={}
for d in range(1,8):
    rows={s:i for i,s in enumerate(faces_by_dim[d-1])}
    pivots={}
    for s in faces_by_dim[d]:
        verts=[v for v in range(n) if s & (1<<v)]
        col={rows[s^(1<<v)]:(-1 if k%2 else 1)%prime for k,v in enumerate(verts)}
        while col:
            p=max(col)
            if p not in pivots:
                a=pow(col[p],-1,prime)
                pivots[p]={i:(a*v)%prime for i,v in col.items()};break
            c=col[p]
            for i,v in pivots[p].items():
                nv=(col.get(i,0)-c*v)%prime
                if nv:col[i]=nv
                elif i in col:del col[i]
    ranks3[d]=len(pivots)
assert ranks3==ranks
print('mod3_boundary_ranks',tuple(ranks3[d] for d in range(1,8)))
print('VERIFY_PRIME3_OK')
