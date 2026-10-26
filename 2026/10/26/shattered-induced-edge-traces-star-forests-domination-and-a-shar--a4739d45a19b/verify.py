#!/usr/bin/env python3
"""Independent finite tests for induced-edge shattering and star-forest profile."""
from itertools import combinations
from math import comb
import random


def star_forest(n, selected):
    adj = [[] for _ in range(n)]
    for u, v in selected:
        adj[u].append(v); adj[v].append(u)
    seen = set()
    for root in range(n):
        if root in seen: continue
        todo=[root]; seen.add(root); comp=[]
        while todo:
            u=todo.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); todo.append(v)
        if sum(len(adj[v])>1 for v in comp)>1:
            return False
    return True


def shattered(n, S):
    if len(S)>n: return False
    traces=set()
    for mask in range(1<<n):
        trace=0
        for i,(u,v) in enumerate(S):
            if (mask>>u)&1 and (mask>>v)&1:
                trace |= 1<<i
        traces.add(trace)
    return len(traces)==(1<<len(S))


def gamma(n, E):
    for k in range(n+1):
        for D in combinations(range(n),k):
            dominated=set(D)
            for u,v in E:
                if u in D: dominated.add(v)
                if v in D: dominated.add(u)
            if len(dominated)==n: return k
    raise AssertionError


def profile(n):
    # Exponential component-formula recurrence, independent of subset enumeration.
    A=[[0]*(n+1) for _ in range(n+1)]
    A[0][0]=1
    for j in range(1,n+1):
        for s in range(1,j+1):
            stars=1 if s<=2 else s
            w=comb(j-1,s-1)*stars
            for k in range(j-s+1):
                A[j][k+s-1]+=w*A[j-s][k]
    return A[n]


def finite():
    total=0
    for n in range(1,7):
        E=list(combinations(range(n),2))
        counts=[0]*(len(E)+1)
        for z in range(1<<len(E)):
            S=[e for i,e in enumerate(E) if z>>i&1]
            sf=star_forest(n,S)
            assert shattered(n,S)==sf, (n,z)
            if sf: counts[len(S)]+=1
            total+=1
        formula=profile(n)
        assert counts[:n]==formula[:n],(n,counts,formula)
        assert sum(counts)==sum(formula)
        print('COMPLETE',n,'sets',1<<len(E),'profile',formula[:n],'PASS')
    domination_cases=0
    for n in range(1,6):
        E=list(combinations(range(n),2))
        for h in range(1<<len(E)):
            H=[e for j,e in enumerate(E) if h>>j&1]
            vc=max((len(S) for z in range(1<<len(H)) for S in [[e for j,e in enumerate(H) if z>>j&1]] if star_forest(n,S)),default=0)
            assert vc==n-gamma(n,H),(n,H,vc,gamma(n,H))
            domination_cases+=1
    print('ALL_HOST_GRAPHS_TO_5',domination_cases,'domination_identity=PASS')
    rng=random.Random(1083)
    hostchecks=0
    for n in range(2,10):
        E=list(combinations(range(n),2))
        for _ in range(32):
            H=[e for e in E if rng.randrange(2)]
            if n<=8:
                # Include isolates in domination calculation.
                vc=max((len(S) for z in range(1<<len(H)) for S in [[e for j,e in enumerate(H) if (z>>j)&1]] if star_forest(n,S)),default=0) if len(H)<=16 else None
                if vc is not None: assert vc==n-gamma(n,H),(n,H,vc)
            for _ in range(16):
                S=[e for e in H if rng.randrange(2)]
                if len(S)>n: continue
                assert shattered(n,S)==star_forest(n,S),(n,S)
                hostchecks+=1
    print('ARBITRARY_HOSTS',hostchecks,'PASS')
    print('PROFILE_N8',profile(8)[:8]);print('PROFILE_N10',profile(10)[:10]);
    print('VERIFY_OK universal_star_forest=PASS domination_identity=PASS labeled_egf=PASS total_subset_tests',total)

if __name__=='__main__': finite()
