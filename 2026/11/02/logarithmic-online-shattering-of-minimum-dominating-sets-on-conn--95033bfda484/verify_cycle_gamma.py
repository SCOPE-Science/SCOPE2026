#!/usr/bin/env python3
"""Independent finite checks of minimum-domination cycle membership classes."""
from itertools import combinations
from pathlib import Path
import json
from functools import lru_cache
from math import comb,log2,floor

def constructor(k):
    n=3*k+2
    P={0}|{3*a-1 for a in range(1,k+1)}
    assert len(P)==k+1
    return n,[sum(1<<((t+p)%n) for p in P) for t in range(n)]

def independent_gamma_sets(n,k):
    ans=[]
    closed=[(1<<i)|(1<<((i-1)%n))|(1<<((i+1)%n)) for i in range(n)]
    for chosen in combinations(range(n),k+1):
        mask=sum(1<<i for i in chosen)
        if all(mask&c for c in closed):ans.append(mask)
    return ans

def exact_ld(H,n):
    qmask=[sum(1<<i for i,h in enumerate(H) if h>>q&1) for q in range(n)]
    @lru_cache(maxsize=None)
    def f(V):
        if V.bit_count()<2: return 0
        best=0
        for q in range(n):
            yes=V&qmask[q]
            if yes and yes!=V:
                z=1+min(f(yes),f(V^yes))
                if z>best:best=z
        return best
    return f((1<<len(H))-1)

def verify(k,full=False):
    n,H=constructor(k)
    assert len(set(H))==n
    assert all(h.bit_count()==k+1 for h in H)
    assert all(all((h>>i&1) or (h>>((i+1)%n)&1) or (h>>((i-1)%n)&1) for i in range(n)) for h in H)
    # Exhaustive independent enumeration for manageable n.
    if k<=6:
        gamma=independent_gamma_sets(n,k)
        assert set(gamma)==set(H),(k,len(gamma),n)
    # Every 3-query support fails to shatter, and a fixed 2-query support shatters.
    assert {((h&1)>0)+2*((h>>2&1)>0) for h in H}=={0,1,2,3}
    for a,b,c in combinations(range(n),3):
        seen=0
        for h in H:
            pat=((h>>a)&1)|(((h>>b)&1)<<1)|(((h>>c)&1)<<2)
            seen|=1<<pat
            if seen==255: raise AssertionError(('triple shattered',k,(a,b,c)))
    # Replay every branch of the explicit complete depth-three witness.
    if k>=3:
        T=json.loads(Path(__file__).with_name("C11_TREE.json").read_text(encoding="utf-8"))
        def walk(node,path):
            if "witness_shift" in node:
                t=node["witness_shift"]
                assert all(bool(H[t]>>q&1)==value for q,value in path),(k,path,t)
                return 1
            q=node["query"]
            return walk(node["zero"],path+[(q,False)])+walk(node["one"],path+[(q,True)])
        assert walk(T,[])==8
    # The selected n/3 rotation subsequence forms a full threshold class.
    for j in range(k+1):
        for b in range(k):
            q=3*b+2
            assert bool(H[3*j]>>q&1)==(j<=b),(k,j,b)
    if full:
        ld=exact_ld(H,n)
        assert floor(log2(k+1))<=ld<=floor(log2(n))
        print('CYCLE',n,'gamma',k+1,'hypotheses',len(H),'VC',2,'Ldim',ld)
    return 1

if __name__=='__main__':
    # Independent ground-truth generation for all n <= 20 and exact online ranks there.
    for k in range(1,7):verify(k,full=True)
    # Broad finite stress-test of the universal bound, not a substitute for proof.
    for k in range(7,26):verify(k)
    print('MINIMUM_CYCLE_DOMINATION_ENUMERATION_PASS n=5,8,11,14,17,20')
    print('CYCLIC_TRIPLE_OBSTRUCTION_PASS k=1..25')
    print('ADAPTIVE_THRESHOLD_SUBCLASS_PASS k=1..25')
    print('UNIFORM_DEPTH_THREE_WITNESS_PASS k=3..25')
    print('ALL_GAMMA_CYCLE_SHATTERING_CHECKS_PASS')
