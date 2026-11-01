"""Independent exhaustive mod-two chains of Franklin perfect-matchings."""
from collections import Counter
N=12
edges=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|
             {tuple(sorted((i,(i+5)%N))) for i in range(0,N,2)}|
             {tuple(sorted((i,(i-5)%N))) for i in range(1,N,2)})
assert len(edges)==18
# No recursion or precomputed perfect-matchings: enumerate every subset.
perfs=[];all_matchings=set()
for mask in range(1<<18):
    used=0;ok=True
    for j,(a,b) in enumerate(edges):
        if mask>>j&1:
            vv=(1<<a)|(1<<b)
            if used&vv:ok=False;break
            used|=vv
    if ok:
        all_matchings.add(mask)
        if used==(1<<N)-1:perfs.append(mask)
assert len(perfs)==17
members={x for x in all_matchings if any(x&f==x for f in perfs)}
assert len(members)==762 and members<=all_matchings
assert len(all_matchings)==1092 # including empty, ordinary matching complex
by_dim=[[x for x in sorted(members) if x.bit_count()==k+1] for k in range(6)]
assert [len(a) for a in by_dim]==[18,117,264,243,102,17]

def rank_GF2(cols):
    basis={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in basis:v^=basis[k]
            else:basis[k]=v;break
    return len(basis)

ranks=[0]
for k in range(1,6):
    old={f:j for j,f in enumerate(by_dim[k-1])}; columns=[]
    for facet in by_dim[k]:
        v=0
        for j in range(facet.bit_length()):
            if facet>>j&1:v^=1<<old[facet^(1<<j)]
        columns.append(v)
    ranks.append(rank_GF2(columns))
# Homology of augmented nonempty chains, with H_0 reduced.
betti=[len(by_dim[k])-ranks[k]-(ranks[k+1] if k+1<6 else 0)-(1 if k==0 else 0) for k in range(6)]
assert betti==[0,0,6,0,0,0],betti
assert sum(((-1)**k)*len(by_dim[k]) for k in range(6))==7
print('perfect_matchings',len(perfs),'ordinary_matching_faces_including_empty',len(all_matchings))
print('extendible_faces_including_empty',len(members),'strictly_nonextendible',len(all_matchings-members))
print('boundary_ranks_GF2',ranks)
print('reduced_betti_GF2',betti)
print('INDEPENDENT_FRANKLIN_PMC_CHAIN_CHECK_PASS')
