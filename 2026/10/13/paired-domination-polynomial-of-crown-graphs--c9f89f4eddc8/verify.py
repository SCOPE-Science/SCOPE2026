#!/usr/bin/env python3
from itertools import combinations
from math import comb


def crown(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj


def dominates(adj,S):
    S=set(S)
    return all(v in S or bool(adj[v]&S) for v in range(len(adj)))


def perfect_matching_exists(adj,S,n):
    S=set(S)
    A=[v for v in S if v<n]
    B=[v for v in S if v>=n]
    if len(A)!=len(B): return False
    # Bipartite augmenting-path matcher from A to B.
    mate={}
    def aug(a,seen):
        for b in adj[a] & set(B):
            if b in seen: continue
            seen.add(b)
            if b not in mate or aug(mate[b],seen):
                mate[b]=a
                return True
        return False
    return all(aug(a,set()) for a in A)


def paired(adj,S,n):
    return dominates(adj,S) and perfect_matching_exists(adj,S,n)

checks=0
coeff_checks=0
minimal_checks=0
for n in range(3,9):
    adj=crown(n)
    counts={k:0 for k in range(2*n+1)}
    minsets=[]
    allsets=[]
    for mask in range(1<<(2*n)):
        S={v for v in range(2*n) if mask>>v & 1}
        p=sum(v<n for v in S); q=len(S)-p
        truth=paired(adj,S,n)
        pred=(p==q and p>=2)
        assert truth==pred,(n,S,p,q,truth,pred)
        checks+=1
        if truth:
            counts[len(S)]+=1
            allsets.append(S)
            if len(S)==4: minsets.append(S)
    for t in range(0,n+1):
        expected=comb(n,t)**2 if t>=2 else 0
        assert counts[2*t]==expected,(n,t,counts[2*t],expected)
        coeff_checks+=1
    for k,c in counts.items():
        if k%2: assert c==0
    assert len(minsets)==comb(n,2)**2
    assert sum(counts.values())==comb(2*n,n)-n*n-1
    # Every paired-dominating set with t>2 contains a t=2 paired-dominating subset;
    # hence minimal paired-dominating sets are exactly the size-4 ones.
    for S in allsets:
        p=sorted(v for v in S if v<n)
        q=sorted(v-n for v in S if v>=n)
        is_minimal=True
        for a2 in combinations(p,2):
            for b2 in combinations(q,2):
                T=set(a2)|{n+j for j in b2}
                if T!=S and paired(adj,T,n):
                    is_minimal=False; break
            if not is_minimal: break
        assert is_minimal==(len(S)==4)
        minimal_checks+=1
print(f"VERIFY_OK n_range=3..8 subset_checks={checks} coefficient_checks={coeff_checks} minimal_checks={minimal_checks} max_order=16")
