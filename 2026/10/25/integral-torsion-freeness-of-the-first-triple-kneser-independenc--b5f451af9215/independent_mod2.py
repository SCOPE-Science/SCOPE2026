"""Independent mod-two check for the intersection/transversal complex on triples of six points."""
from itertools import combinations
from collections import Counter
triangles=list(combinations(range(6),3))
# Incrementally enumerate clique subsets of the pairwise intersection graph via adjacency masks.
complements={i: triangles.index(tuple(x for x in range(6) if x not in t)) for i,t in enumerate(triangles)}
# Build 20-vertex graph adjacency and enumerate cliques incrementally, avoiding 3^10 construction.
# DFS with increasing vertex labels and pairwise intersection constraint
all_cliques=set()
def extend(f,next_index):
    if f:all_cliques.add(f)
    for v in range(next_index,20):
        if not (f & (1<<complements[v])):
            extend(f|(1<<v),v+1)
extend(0,0)
assert len(all_cliques)==3**10-1
# Filter by checking all possible point pairs, but without precomputed cover masks
F={mask for mask in all_cliques if any(all((a in triangles[v] or b in triangles[v]) for v in range(20) if mask>>v&1) for a,b in combinations(range(6),2))}
assert len(F)==54870
bydim={d:sorted(m for m in F if m.bit_count()-1==d) for d in range(10)}
ranks={0:0}
for d in range(1,10):
    idx={mask:j for j,mask in enumerate(bydim[d-1])}
    piv={}
    for f in bydim[d]:
        bit=0
        t=f
        while t:
            b=t&-t;t-=b
            bit^=1<<idx[f^b]
        while bit:
            p=bit.bit_length()-1
            if p in piv:bit^=piv[p]
            else:piv[p]=bit;break
    ranks[d]=len(piv)
    print('mod2 boundary',d,'rank',ranks[d])
red={}
for d in range(10):
    beta=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
    if d==0:beta-=1
    if beta:red[d]=beta
print('mod2 homology',red)
assert red=={5:29,8:6}
