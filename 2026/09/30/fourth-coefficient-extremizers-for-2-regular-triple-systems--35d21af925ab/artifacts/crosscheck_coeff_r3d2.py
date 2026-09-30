from itertools import combinations
from collections import Counter
from math import comb

# Direct enumeration of all simple 3-uniform 2-regular hypergraphs on six labeled vertices.
def indep4_count(n, edges):
    E={frozenset(e) for e in edges}
    c=0
    for S in combinations(range(n),4):
        SS=set(S)
        if all(not set(e)<=SS for e in E):
            c+=1
    return c

n=6
triples=list(combinations(range(n),3))
vals=[]
for chosen in combinations(triples,4):
    deg=[0]*n
    for e in chosen:
        for v in e: deg[v]+=1
    if deg==[2]*n:
        vals.append(indep4_count(n,chosen))
mx=max(vals)
assert mx == comb(6,4)-6*(2*6-7)//3 == 5
print(f'n=6 direct_labeled_hypergraphs={len(vals)} max_i4={mx} equality_count={sum(v==mx for v in vals)}')

# Construct the connected equality family dual to an alternating-doubled C_{2ell}.
def equality_hypergraph(ell):
    N=2*ell
    dual_edges=[]
    # cycle edges (i,i+1); double those with even i, single those with odd i
    for i in range(N):
        j=(i+1)%N
        mult=2 if i%2==0 else 1
        for _ in range(mult): dual_edges.append((i,j))
    # Hypergraph vertices are dual edges; hyperedge at dual vertex is its 3 incident dual-edge labels.
    H=[]
    for v in range(N):
        inc=[k for k,(a,b) in enumerate(dual_edges) if a==v or b==v]
        assert len(inc)==3
        H.append(tuple(sorted(inc)))
    nH=len(dual_edges)
    assert nH==3*ell
    assert len(set(H))==len(H)
    deg=[0]*nH
    for e in H:
        for x in e: deg[x]+=1
    assert all(d==2 for d in deg)
    return nH,H

for ell in range(2,8):
    nH,H=equality_hypergraph(ell)
    got=indep4_count(nH,H)
    expect=comb(nH,4)-nH*(2*nH-7)//3
    assert got==expect
    print(f'ell={ell} n={nH} i4={got} formula={expect}')
print('CROSSCHECK_OK')
