#!/usr/bin/env python3
"""Independent brute check for minimal forts of triangular graphs L(K_n)."""
from itertools import combinations
from math import comb, factorial
from collections import Counter
from functools import lru_cache

def make(n):
    pairs=list(combinations(range(n),2)); m=len(pairs)
    nb=[sum(1<<j for j,(c,d) in enumerate(pairs) if j!=i and (a==c or a==d or b==c or b==d)) for i,(a,b) in enumerate(pairs)]
    return pairs,nb

def is_fort(F,nb):
    if not F:return False
    return all((F>>i)&1 or (F&adj).bit_count()!=1 for i,adj in enumerate(nb))

def predictable(F,pairs,n):
    if not F:return False
    deg=[0]*n;adj=[[] for _ in range(n)]
    for i,(a,b) in enumerate(pairs):
        if F>>i&1:
            deg[a]+=1;deg[b]+=1
            adj[a].append(b);adj[b].append(a)
    # Spanning star forest is a minimal edge cover of K_n.
    starforest=all(d>=1 for d in deg) and all(deg[a]==1 or deg[b]==1 for i,(a,b) in enumerate(pairs) if F>>i&1)
    used=[v for v in range(n) if deg[v]>0]
    iscycle=False
    if len(used)<n and len(used)>=3 and all(d==0 or d==2 for d in deg):
        visited={used[0]};todo=[used[0]]
        while todo:
            v=todo.pop()
            for w in adj[v]:
                if w not in visited:
                    visited.add(w);todo.append(w)
        iscycle=len(visited)==len(used)
    return starforest or iscycle

def minF_by_scan(n):
    edges,nb=make(n)
    mins=[]
    allforts=0
    for s in range(1,len(edges)+1):
        for verts in combinations(range(len(edges)),s):
            F=sum(1<<j for j in verts)
            actual=is_fort(F,nb)
            if actual:allforts+=1
            if actual and not any(F&G==G for G in mins): mins.append(F)
    return mins,allforts,edges,nb

def star_count(n):
    # independently enumerate partition block sizes via set partitions on labeled vertices
    @lru_cache(None)
    def sp(mask):
        if not mask:return 1
        idx=(mask&-mask).bit_length()-1
        rest=mask^(1<<idx)
        inds=[i for i in range(n) if rest>>i&1]
        total=0
        for k in range(1,len(inds)+1):
            for subset in combinations(inds,k):
                blockmask=(1<<idx)|sum(1<<x for x in subset)
                size=k+1
                total+=(1 if size==2 else size)*sp(mask^blockmask)
        return total
    return sp((1<<n)-1)

def main():
    checked=0
    for n in range(4,7):
        minima,forts,pairs,nb=minF_by_scan(n)
        actual=set(minima)
        expect={F for F in range(1,1<<len(pairs)) if predictable(F,pairs,n)}
        assert actual==expect,(n,len(actual),len(expect),len(actual-expect),len(expect-actual))
        cycle_count=sum(comb(n,k)*factorial(k-1)//2 for k in range(3,n))
        star_n=star_count(n)
        assert len(actual)==cycle_count+star_n, (n,len(actual),cycle_count,star_n)
        mincard=min(x.bit_count() for x in actual)
        assert mincard==min((n+1)//2,3)
        checked+=1<<len(pairs)
        print('n=%d ground_edges=%d minimal_forts=%d starforests=%d nonspanning_cycles=%d all_forts=%d' % (n,len(pairs),len(actual),star_n,cycle_count,forts))
    # For 7 vertices verify each constructed minimum fort directly, and
    # 80,000 pseudorandom subsets against all candidate subforts.
    import random
    n=7;pairs,nb=make(n);N=len(pairs)
    expected={F for F in range(1,1<<N) if predictable(F,pairs,n)}
    assert len(expected)==star_count(n)+sum(comb(n,k)*factorial(k-1)//2 for k in range(3,n))
    for f in expected:
        assert is_fort(f,nb)
        for s in range(1,f):
            if (s&f)==s:assert not is_fort(s,nb)
    rng=random.Random(4729001)
    for _ in range(80000):
        f=rng.randrange(1<<N)
        # Forts are NOT upward-closed. Only necessity holds:
        # each fort must contain an inclusion-minimal fort.
        if is_fort(f,nb):
            assert any((f&g)==g for g in expected)
    print('n=7 candidate_minimal_forts=%d verified_all_candidates_and_80000_subsets' % len(expected))
    print('VERIFICATION_OK exhaustive_subsets=%d n7_samples=80000' % checked)
if __name__=='__main__':main()
