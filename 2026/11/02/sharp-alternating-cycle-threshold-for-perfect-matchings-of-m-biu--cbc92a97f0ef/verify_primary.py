#!/usr/bin/env python3
"""Exhaustive finite checks of perfect-matching alternating-cycle reconfiguration.
No external packages; uses vertex-pair recursion, independent four-cycle search,
and full symmetric-difference connectedness tests.
"""
from collections import Counter, deque
from math import comb


def graph(n):
    E=set()
    def e(a,b): E.add(tuple(sorted((a,b))))
    for j in range(n): e(j,j+n)
    for j in range(n-1): e(j,j+1);e(j+n,j+n+1)
    e(n-1,n);e(2*n-1,0)
    E=sorted(E)
    N=[[] for _ in range(2*n)]
    for i,(a,b) in enumerate(E): N[a].append((b,i));N[b].append((a,i))
    return E,N


def enumerate_matchings(n,nei):
    out=[]; full=(1<<(2*n))-1
    def rec(mask,chosen):
        if mask==full: out.append(chosen); return
        u=next(i for i in range(2*n) if not(mask>>i&1))
        for v,ei in nei[u]:
            if not(mask>>v&1): rec(mask|(1<<u)|(1<<v),chosen|(1<<ei))
    rec(0,0)
    return out


def cycles_of_difference(A,B,E):
    diff=A^B
    if not diff: return []
    adj={};count=0
    for j,(a,b) in enumerate(E):
        if diff>>j&1:
            adj.setdefault(a,[]).append(b)
            adj.setdefault(b,[]).append(a)
            count+=1
    assert all(len(nei)==2 for nei in adj.values())
    seen=set();sizes=[]
    for u in adj:
        if u in seen: continue
        stack=[u];seen.add(u);s=0
        while stack:
            a=stack.pop();s+=1
            for b in adj[a]:
                if b not in seen:seen.add(b);stack.append(b)
        sizes.append(s)
    assert sum(sizes)==count
    return sizes


def components(adj):
    seen=set(); sizes=[]
    for s in range(len(adj)):
        if s in seen:continue
        todo=[s];seen.add(s);cnt=0
        while todo:
            a=todo.pop();cnt+=1
            for b in adj[a]:
                if b not in seen:seen.add(b);todo.append(b)
        sizes.append(cnt)
    return sorted(sizes)


def check(n):
    E,nei=graph(n)
    matchings=enumerate_matchings(n,nei)
    ids={M:i for i,M in enumerate(matchings)}
    expected=0;independent=[];degs=Counter();D={}
    for mask in range(1<<n):
        if mask & ((mask<<1)&((1<<n)-1)) or ((mask&1) and (mask>>(n-1)&1)):continue
        independent.append(mask)
        # degree: remove an existing dimer or add a free dimer
        d=mask.bit_count()
        a=sum(not(mask>>j&1) and not(mask>>((j-1)%n)&1) and not(mask>>((j+1)%n)&1) for j in range(n))
        degs[d+a]+=1
    if n&1:degs[0]+=2
    assert len(matchings)==len(independent)+2*(n%2)
    rung_ids={i for i,(u,v) in enumerate(E) if v-u==n}
    bad=[]
    for M in matchings:
        nr=sum(bool(M>>i&1) for i in rung_ids)
        if not nr:bad.append(M)
        else:assert nr%2==n%2
    assert len(bad)==(2 if n%2 else 2) # even two all-horizontal are regular states
    four=[set() for _ in matchings]
    threshold=[set() for _ in matchings]
    smallest_from_bad=Counter()
    # brute symmetric difference enumerations, not square templates
    for i,A in enumerate(matchings):
        for j in range(i+1,len(matchings)):
            B=matchings[j]
            parts=cycles_of_difference(A,B,E)
            if len(parts)!=1:continue
            length=parts[0]
            if length==4:four[i].add(j);four[j].add(i)
            if length<= (n+1 if n&1 else 4):threshold[i].add(j);threshold[j].add(i)
            if n&1 and (A in bad or B in bad):smallest_from_bad[length]+=1
    assert Counter(map(len,four))==degs,(n,Counter(map(len,four)),degs)
    assert sum(map(len,four))//2==n*fib(n-1)
    cs=components(four)
    assert cs == ([1,1,len(independent)] if n&1 else [len(independent)]),(n,cs)
    assert components(threshold)==[len(matchings)]
    if n&1:
        assert min(smallest_from_bad)==n+1,(n,smallest_from_bad)
        assert all(len(four[ids[b]])==0 for b in bad)
        one_rung=[i for i,M in enumerate(matchings) if sum(bool(M>>q&1) for q in rung_ids)==1]
        assert len(one_rung)==n
        for b in bad:
            for j in one_rung:
                assert cycles_of_difference(b,matchings[j],E)==[n+1]
    print('PRIMARY_PASS',n,'matchings',len(matchings),'fourflip_edges',sum(map(len,four))//2,'components',cs,'degrees',sorted(degs.items()))

def fib(i):
    a,b=0,1
    for _ in range(i):a,b=b,a+b
    return a

if __name__=='__main__':
    for n in range(4,12):check(n)
    print('PRIMARY_ALL_PASS')
