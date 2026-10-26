#!/usr/bin/env python3
"""Self-contained finite verification for the 2-bounded Eventown stability bound."""
from itertools import product

def check(n):
    vectors = [x for x in product((0,1,2),repeat=n) if sum(x)%2==0]
    m=len(vectors)
    # Independent parity-embedding identity for all pairs, no assumptions.
    def emb(x):
        return tuple((int(v>0),int(v==2)) for v in x)
    e=[emb(x) for x in vectors]
    for i in range(m):
        for j in range(m):
            left=sum(min(a,b) for a,b in zip(vectors[i],vectors[j]))%2
            right=sum(a*c+b*d for (a,b),(c,d) in zip(e[i],e[j]))%2
            assert left==right,(n,vectors[i],vectors[j])
    adj=[0]*m
    for i in range(m):
        for j in range(i+1,m):
            if sum(min(a,b) for a,b in zip(vectors[i],vectors[j]))%2==0:
                adj[i] |=1<<j;adj[j]|=1<<i
    noncanonical=[any(v==1 for v in x) for x in vectors]
    best=[0]; max_cliques=[0]
    def bk(Rsize,P,X,odd):
        if not (P|X):
            max_cliques[0]+=1
            if odd and Rsize>best[0]: best[0]=Rsize
            return
        PX=P|X
        # pivot maximizing number of possible neighbors
        w=-1; k=-1
        while PX:
            b=PX&-PX; u=b.bit_length()-1; PX-=b
            score=(P&adj[u]).bit_count()
            if score>k: k=score;w=u
        candidates=P&~adj[w]
        while candidates:
            bit=candidates&-candidates;v=bit.bit_length()-1
            bk(Rsize+1,P&adj[v],X&adj[v],odd or noncanonical[v])
            P-=bit; X|=bit;candidates-=bit
    bk(0,(1<<m)-1,0,False)
    expected=3*(1<<(n-2))
    construction=[a+b for a in ((0,0),(1,1),(2,2)) for b in product((0,2),repeat=n-2)]
    assert len(construction)==expected and len(set(construction))==expected
    assert any(1 in x for x in construction)
    for x in construction:
        for y in construction:
            assert sum(min(a,b) for a,b in zip(x,y))%2==0
    assert best[0]==expected,(n,best[0],expected)
    print(f'n={n} even_vectors={m} maximal_cliques={max_cliques[0]} max_noncanonical={best[0]} expected={expected}')
for n in range(2,6): check(n)
print('VERIFY_OK')
