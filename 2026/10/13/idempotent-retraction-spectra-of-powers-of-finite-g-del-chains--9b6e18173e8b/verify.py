#!/usr/bin/env python3
"""Exact finite checks for retract-rank polynomials of products of Heyting chains.
Standard-library only. Runs independently by exhaustive enumeration of poset maps.
"""
from itertools import product
from collections import Counter
from math import comb, factorial

def B(n,k):
    return sum(comb(n-1,i) for i in range(k)) if k else 0

def predicted(m,n):
    endo=Counter(); idem=Counter()
    for targets in product(range(m),repeat=m):
        for lengths in product(range(1,n+1), repeat=m):
            weight=1
            K=[0]*m
            for i in range(m):
                weight*=comb(n-1,lengths[i]-1)
                K[targets[i]]=max(K[targets[i]],lengths[i])
            rank=1
            for j in range(m):rank*=K[j]+1
            endo[rank]+=weight
    for r in range(1,m+1):
        for active in __import__('itertools').combinations(range(m),r):
            for ks in product(range(1,n+1),repeat=r):
                rank=1
                for k in ks:rank*=k+1
                idem[rank]+=sum(B(n,k) for k in ks)**(m-r)
    return endo,idem

def brute(m,n):
    N=m*n
    def upper(a,b):return a//n==b//n and a%n<=b%n
    domains=range(N)
    endo=Counter();idem=Counter(); maps=0
    for f in product(domains,repeat=N):
        maps+=1
        if any(upper(a,b) and not upper(f[a],f[b]) for a in domains for b in domains):continue
        if any({f[b] for b in domains if upper(a,b)}!={b for b in domains if upper(f[a],b)} for a in domains):continue
        im=set(f)
        sizes=[sum(y//n==j for y in im)+1 for j in range(m)]
        rank=__import__('math').prod(sizes)
        endo[rank]+=1
        if all(f[f[x]]==f[x] for x in domains):idem[rank]+=1
    return endo,idem,maps

def validate_dual_heyting(m,n):
    """Independently check every p-morphism pullback is a full Heyting endomorphism."""
    N=m*n;V=range(N)
    up=lambda x,y: x//n==y//n and x%n<=y%n
    sets=[frozenset(S) for r in range(N+1) for S in __import__('itertools').combinations(V,r) if all(y in S for x in S for y in V if up(x,y))]
    U=set(sets)
    assert len(sets)==(n+1)**m
    impl=lambda A,B:frozenset(x for x in V if all((y not in A or y in B) for y in V if up(x,y)))
    homs=0;checked=0
    for f in product(V,repeat=N):
        if any(up(a,b) and not up(f[a],f[b]) for a in V for b in V):continue
        if any({f[b] for b in V if up(a,b)}!={b for b in V if up(f[a],b)} for a in V):continue
        homs+=1
        inv=lambda A:frozenset(x for x in V if f[x] in A)
        assert all(inv(A) in U for A in sets)
        for A in sets:
            for B in sets:
                assert inv(impl(A,B))==impl(inv(A),inv(B))
                checked+=1
        assert len({inv(A) for A in sets})==__import__('math').prod(1+sum(y//n==j for y in set(f)) for j in range(m))
    return homs,checked

def run():
    assert B(3,1)==1 and B(3,2)==3 and B(3,3)==4
    checks=0
    for m,n in [(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
        pE,pI=predicted(m,n)
        bE,bI,total=brute(m,n)
        assert pE==bE,(m,n,'endo',pE,bE)
        assert pI==bI,(m,n,'idem',pI,bI)
        assert sum(pE.values())==(m*2**(n-1))**m
        assert pI<=pE
        print(f'm={m}, n={n}; candidate maps={total}; hom={sum(bE.values())}; idem={sum(bI.values())}; endo-ranks={dict(sorted(pE.items()))}; idem-ranks={dict(sorted(pI.items()))}')
        checks+=4
    # Distinct isomorphism types of poset cone images: components labelled only by their suffix length.
    for m in range(1,6):
        for n in range(1,5):
            count=sum(comb(n+r-1,r) for r in range(1,m+1))
            assert count==comb(n+m,m)-1
            checks+=1
    for m,n in [(1,2),(2,1),(2,2),(2,3),(3,1)]:
        h,pairs=validate_dual_heyting(m,n)
        assert h==sum(predicted(m,n)[0].values())
        checks+=pairs+1
        print(f'Heyting-operation consistency m={m}, n={n}: {h} homomorphisms, {pairs} implication pairs')
    print(f'VERIFY_OK {checks} exact comparisons; exhaustive maps for ten parameter pairs; algebraic implication preservation through 6 dual points')

if __name__=='__main__':run()
