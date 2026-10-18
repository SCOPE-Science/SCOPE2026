"""Exhaustive cross-graph test of the rose characteristic-depth bound."""
from collections import defaultdict
from rose_check import rose

def graph_adj(n, mask):
    out=[set() for _ in range(n)]
    b=0
    for i in range(n):
        for j in range(i+1,n):
            if mask>>b&1:out[i].add(j);out[j].add(i)
            b+=1
    return out

def graphmask(A):
    b=0;mask=0;n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            if j in A[i]:mask|=1<<b
            b+=1
    return mask

def invariant_all(n,depth):
    masks=range(1<<(n*(n-1)//2)); adj=[graph_adj(n,m) for m in masks]
    colors=[[0]*n for _ in adj]
    for t in range(depth+1):
        if t==depth:break
        ks=[(colors[i][v], tuple(sorted(colors[i][u] for u in A[v]))) for i,A in enumerate(adj) for v in range(n)]
        enc={k:i for i,k in enumerate(sorted(set(ks)))}
        colors=[[enc[ks[i*n+v]] for v in range(n)] for i in range(len(adj))]
    return {m:tuple(sorted(c)) for m,c in enumerate(colors)}

for lengths in ((3,3),(3,4)):
    G=rose(lengths);n=len(G);D=max(L//2 for L in lengths)
    if n>7:continue
    hist=invariant_all(n,D+2)
    mask=graphmask(G)
    same=[m for m,s in hist.items() if s==hist[mask]]
    print('rose',lengths,'n',n,'D',D,'globally-matching-labelled-masks',len(same))
    # All matches should be isomorphic. Labelings of bouquet: at n=5, automorphism order 8 => 5!/8=15; at n=6, automorphism order 4 => 6!/4=180.
    if n==5:assert len(same)==15
    if n==6:assert len(same)==180
