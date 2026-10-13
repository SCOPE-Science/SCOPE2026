#!/usr/bin/env python3
"""Independent finite checks for the MEG-set polynomial of unicyclic graphs.
All computations use exact integers and the Python standard library.
"""
from collections import Counter, deque
from itertools import combinations
import random


def distances(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    dist=[]
    for s in range(n):
        ds=[n+1]*n; ds[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if ds[v]>n:
                    ds[v]=ds[u]+1; q.append(v)
        dist.append(ds)
    return dist


def pair_edge_masks(n,edges):
    base=distances(n,edges)
    result={p:0 for p in combinations(range(n),2)}
    for i,e in enumerate(edges):
        alt=distances(n,edges[:i]+edges[i+1:])
        for p in result:
            u,v=p
            if alt[u][v]>base[u][v]:result[p] |=1<<i
    return result


def structural_data(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    degrees=[len(a) for a in adj]
    leaves={i for i,d in enumerate(degrees) if d==1}
    remain=set(range(n))
    q=deque(leaves); deg=degrees[:]
    while q:
        v=q.popleft();remain.discard(v)
        for w in adj[v]:
            deg[w]-=1
            if deg[w]==1:q.append(w)
    assert len(remain)>=3 and all(len(adj[v]&remain)==2 for v in remain)
    c=[min(remain)]
    first=min(adj[c[0]]&remain);prev=c[0];v=first
    while v!=c[0]:
        c.append(v)
        nxt=next(w for w in adj[v]&remain if w!=prev)
        prev,v=v,nxt
    assert len(c)==len(remain)
    cycle=set(c)
    A={v for v in c if len(adj[v]-cycle)>0}
    return c,A,leaves


def predicted_membership(n,edges,selected):
    c,A,leaves=structural_data(n,edges)
    if not leaves.issubset(selected):return False
    P={i for i,v in enumerate(c) if v in A or v in selected}
    if not P:return False
    ids=sorted(P);m=(len(c)-1)//2
    gaps=[(ids[(j+1)%len(ids)]-ids[j])%len(c) for j in range(len(ids))]
    if len(ids)==1:gaps=[len(c)]
    return all(1<=g<=m for g in gaps)


def polynomial_predicted(n,edges):
    c,A,leaves=structural_data(n,edges)
    l=len(leaves); a=len(A); h=len(c); m=(h-1)//2
    roots=set(c);nontree_internal=n-h-l
    # independently calculate cycle polynomial by enumerating selected cycle vertices
    q=Counter()
    bare=[v for v in c if v not in A]
    for mask in range(1<<len(bare)):
        chosen={bare[j] for j in range(len(bare)) if mask>>j&1}
        P={i for i,v in enumerate(c) if v in A or v in chosen}
        if not P:continue
        ids=sorted(P); gaps=[(ids[(j+1)%len(ids)]-ids[j])%h for j in range(len(ids))]
        if len(ids)==1:gaps=[h]
        if all(1<=g<=m for g in gaps):q[len(chosen)]+=1
    from math import comb
    exp=Counter()
    for k,v in q.items():
        for t in range(nontree_internal+a+1):
            exp[l+k+t]+=v*comb(nontree_internal+a,t)
    return exp


def test_graph(n,edges):
    edges=sorted(tuple(sorted(e)) for e in edges)
    assert len(edges)==n
    assert all(v < n for e in edges for v in e)
    masks=pair_edge_masks(n,edges)
    expected=polynomial_predicted(n,edges)
    actual=Counter()
    tested=0
    for s in range(1<<n):
        S={i for i in range(n) if s>>i&1}
        coverage=0
        for p,msk in masks.items():
            if p[0] in S and p[1] in S:
                coverage |=msk
        brute=coverage==(1<<len(edges))-1
        pred=predicted_membership(n,edges,S)
        assert brute==pred,(n,edges,s,brute,pred)
        if brute:actual[len(S)]+=1
        tested+=1
    assert expected==actual,(n,edges,expected,actual)
    return tested,actual


def is_connected(n,edges):
    a=[[] for _ in range(n)]
    for u,v in edges:a[u].append(v);a[v].append(u)
    seen={0};todo=[0]
    while todo:
        for v in a[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==n

def R(d,m):
    # gap polynomial by compositions, independent of subset enumeration
    p=Counter()
    def rec(s,j):
        if s==d:p[j-1]+=1;return
        for k in range(1,min(m,d-s)+1):rec(s+k,j+1)
    rec(0,0)
    return p


def cycle_poly_formula(n,A):
    m=(n-1)//2
    if not A:
        from fractions import Fraction
        from math import comb
        ans=Counter()
        for k in range(1,n+1):
            coeff=0
            for j in range(k+1):
                u=n-k-j*m
                if u>=0:coeff+=(-1)**j * comb(k,j)*comb(u+k-1,k-1)
            val=Fraction(n*coeff,k)
            assert val.denominator==1
            if val:ans[k]=val.numerator
        return ans
    ids=sorted(A);dist=[(ids[(j+1)%len(ids)]-ids[j])%n for j in range(len(ids))]
    if len(ids)==1:dist=[n]
    ans=Counter({0:1})
    for d in dist:
        part=R(d,m)
        ans=Counter({k:sum(v*w for a0,v in ans.items() for b0,w in part.items() if a0+b0==k)
                    for k in {a0+b0 for a0 in ans for b0 in part}})
    return ans


def check_cycle_formula():
    cases=0
    for n in range(3,14):
        for mask in range(1<<n):
            A={i for i in range(n) if mask>>i&1}
            # direct B subset enumeration
            bare=[i for i in range(n) if i not in A]
            direct=Counter()
            for bm in range(1<<len(bare)):
                B={bare[j] for j in range(len(bare)) if bm>>j&1}
                ids=sorted(A|B)
                if not ids:continue
                gaps=[(ids[(j+1)%len(ids)]-ids[j])%n for j in range(len(ids))]
                if len(ids)==1:gaps=[n]
                if all(1<=g< n/2 for g in gaps):direct[len(B)]+=1
            via=cycle_poly_formula(n,A)
            assert direct==via,(n,A,direct,via)
            cases+=1
    return cases

if __name__=='__main__':
    tested=0;graphs=0
    from itertools import combinations
    for n in range(3,7):
        all_edges=list(combinations(range(n),2))
        for edges in combinations(all_edges,n):
            if is_connected(n,edges):
                k,_=test_graph(n,edges);tested+=k;graphs+=1
    print('all_labeled_unicyclic_orders_3_through_6',graphs,'subset_checks',tested)
    rng=random.Random(314159)
    for n in range(7,13):
        for sample in range(16):
            c=rng.randint(3,n)
            edges=[(i,(i+1)%c) for i in range(c)]
            for v in range(c,n): edges.append((v,rng.randrange(v)))
            k,_=test_graph(n,edges);tested+=k;graphs+=1
    print('with_random_graphs',graphs,'subset_checks',tested)
    c=check_cycle_formula()
    print('cycle_attachment_pattern_cases',c)
    print('PASS: direct edge-deletion distances, gap/leaf theorem, coefficient factorization')
