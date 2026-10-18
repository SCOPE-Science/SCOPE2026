#!/usr/bin/env python3
"""Independent finite checks for chain-nucleus compatibility and maximal families."""
from itertools import product, combinations
from functools import lru_cache
from collections import Counter

def closure_axioms(f):
    n=len(f)
    return (all(x<=f[x] for x in range(n)) and
            all(f[x]<=f[x+1] for x in range(n-1)) and
            all(f[f[x]]==f[x] for x in range(n)))

def maps_by_fixed(n):
    ans=[]
    for mask in range(1 << (n-1)):
        fixed=[i for i in range(n-1) if mask & (1 << i)] + [n-1]
        ans.append(tuple(min(j for j in fixed if j>=i) for i in range(n)))
    return ans

def blocks(f):
    out={}
    for i,j in enumerate(f): out.setdefault(j,set()).add(i)
    return [frozenset(v) for v in out.values()]

def laminar(A,B):
    return all(not (a&b) or a<=b or b<=a for a in A for b in B)

def commute(f,g):
    return all(f[g[i]]==g[f[i]] for i in range(len(f)))

@lru_cache(None)
def trees(n):
    if n==1:return (None,)
    return tuple((L,R) for k in range(1,n) for L in trees(k) for R in trees(n-k))

def family_size(t):
    return 1 if t is None else 1+family_size(t[0])*family_size(t[1])

def maximal_cliques(adjacency):
    n=len(adjacency); out=[]
    def rec(R,P,X):
        if not P and not X:
            out.append(frozenset(R));return
        pivot=max(P|X,key=lambda v:len(P & adjacency[v])) if P or X else None
        for v in list(P-(adjacency[pivot] if pivot is not None else set())):
            rec(R|{v},P & adjacency[v],X & adjacency[v])
            P.remove(v);X.add(v)
    rec(set(),set(range(n)),set())
    return out

def main():
    expected_pairs=[1,4]
    while len(expected_pairs)<10:
        expected_pairs.append(4*expected_pairs[-1]-2*expected_pairs[-2])
    catalan=[1]
    for k in range(1,10):
        catalan.append(sum(catalan[i]*catalan[k-1-i] for i in range(k)))
    for n in range(1,10):
        F=maps_by_fixed(n)
        assert len(F)==2**(n-1)
        for f in F:assert closure_axioms(f)
        B=[blocks(f) for f in F]
        adj=[set() for _ in F]
        pair=0
        for i in range(len(F)):
            for j in range(len(F)):
                c=commute(F[i],F[j]); l=laminar(B[i],B[j])
                assert c==l,(n,i,j)
                pair+=c
                if c and i!=j:adj[i].add(j)
        assert pair==expected_pairs[n-1], (n,pair)
        if n<=5:
            naive=[f for f in product(range(n),repeat=n) if closure_axioms(f)]
            assert set(naive)==set(F),(n,'naive')
        hist=Counter(family_size(t) for t in trees(n))
        assert len(trees(n))==catalan[n-1]
        if n<=6:
            cl=maximal_cliques(adj)
            assert len(cl)==catalan[n-1]
            assert Counter(map(len,cl))==hist,(n,'maximal family sizes')
        print(f'CHAIN {n}: nuclei={len(F)} pairs={pair} maximal={len(trees(n))} size_spectrum={sorted(hist.items())}')
    print('VERIFY_OK')

if __name__=='__main__':main()
