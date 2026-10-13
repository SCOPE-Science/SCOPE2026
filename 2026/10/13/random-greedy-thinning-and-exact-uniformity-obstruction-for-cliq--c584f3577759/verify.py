#!/usr/bin/env python3
"""Exact independent permutation-fibre test of the clique-corona thinning law."""
from fractions import Fraction
from itertools import permutations
from collections import Counter
from math import factorial


def greedy_core(mask, edges, order):
    chosen=0
    for v in order:
        if mask>>v&1 and all(not (chosen>>u&1) for u in edges[v]):
            chosen|=1<<v
    return chosen

def expected(n,s,edges):
    # Counts of core-output probabilities using independent cluster minima.
    p=Fraction(1,s+1); q=1-p
    d={}
    for A in range(1<<n):
        support=[i for i in range(n) if A>>i&1]
        cnt=Counter(greedy_core(A,edges,order) for order in permutations(support))
        for S,c in cnt.items():
            d[S]=d.get(S,Fraction(0))+p**len(support)*q**(n-len(support))*Fraction(c,factorial(len(support)))
    return d

def brute(n,s,edges):
    # Brute permutation scan; choose one accepted member from each clique cluster.
    N=n*(s+1); adj=[set() for _ in range(N)]
    for u in range(n):
        for v in edges[u]:
            adj[u].add(v)
        priv=list(range(n+u*s,n+(u+1)*s))
        for a in priv:
            adj[u].add(a);adj[a].add(u)
            for b in priv:
                if a!=b:adj[a].add(b)
    cnt=Counter(); leafchoices=Counter()
    for order in permutations(range(N)):
        selected=set()
        for v in order:
            if not selected.intersection(adj[v]):selected.add(v)
        cores=sum(1<<i for i in range(n) if i in selected)
        private=tuple((next((j for j in range(s) if n+i*s+j in selected),None) if i not in selected else None) for i in range(n))
        assert len(selected)==n
        cnt[cores]+=1;leafchoices[(cores,private)]+=1
    return N,cnt,leafchoices

def test(label,n,s,pairs):
    edges=[set() for i in range(n)]
    for i,j in pairs:edges[i].add(j);edges[j].add(i)
    theory=expected(n,s,edges)
    N,cnt,choice=brute(n,s,edges)
    denom=factorial(N)
    assert set(cnt)==set(theory), (label,'support mismatch')
    for S,pr in theory.items():
        assert Fraction(cnt[S],denom)==pr,(label,S,pr,Fraction(cnt[S],denom))
        ch=[k for k in choice if k[0]==S]
        assert len(ch)==s**(n-S.bit_count()),(label,S,'leaf choice count')
        assert all(Fraction(choice[k],denom)==pr/Fraction(s**(n-S.bit_count())) for k in ch),(label,S,'leaf-law mismatch')
    if len(pairs)==n*(n-1)//2:
        no_core=theory[0]
        uniform_no=Fraction(s**n,s**n+n*s**(n-1))
        tv=sum(abs(Fraction(choice[k],denom)-Fraction(1,s**n+n*s**(n-1))) for k in choice)/2
        assert tv==uniform_no-no_core,(label,'TV mismatch')
    print(f'{label}: n={n}, s={s}, permutations={denom}, core outcomes={len(cnt)}, labelled maximal outputs={len(choice)}, OK')

if __name__=='__main__':
    test('K3_s2',3,2,[(0,1),(0,2),(1,2)])
    test('P3_s2',3,2,[(0,1),(1,2)])
    test('K4_s1',4,1,[(i,j) for i in range(4) for j in range(i+1,4)])
    test('C4_s1',4,1,[(0,1),(1,2),(2,3),(3,0)])
    test('P4_s1',4,1,[(0,1),(1,2),(2,3)])
    test('E4_s1',4,1,[])
    print('ALL EXACT CORONA TESTS PASSED')
