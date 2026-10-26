#!/usr/bin/env python3
"""Exact enumerator for strong odd colorings of gear graphs.
Only public mathematical data are encoded here. Python >=3.9, stdlib only.
"""
from collections import defaultdict
from itertools import product


def transitions(m, mode):
    if mode == 'hub':
        S = [(a,) for a in range(m)]
        return S, [[j for j,(b,) in enumerate(S) if a!=b] for (a,) in S]
    S = [(a,u) for a in range(m) for u in range(m) if a!=u]
    return S, [[j for j,(b,v) in enumerate(S) if a!=b and u!=b and u!=v] for a,u in S]


def closed_walks_odd(n,m,mode):
    S, T=transitions(m,mode)
    mask=(1<<m)-1
    total=0
    for start in range(len(S)):
        d={(start,0):1}
        for _ in range(n):
            e=defaultdict(int)
            for (i,odd),v in d.items():
                for j in T[i]:
                    e[j,odd^(1<<S[j][0])]+=v
            d=e
        total+=d.get((start,mask),0)
    return total


def count_opt(n,k):
    m=k-1
    return k*(closed_walks_odd(n,m,'hub')+closed_walks_odd(n,m,'other'))


def predicted_k(n):
    if n==5: return 6
    if n%4==2: return 3
    if n%4==0:return 5
    return 4


def sn(n):
    s=[3,0,-2]
    for i in range(3,n+1):s.append(-s[i-2]-2*s[i-3])
    return s[n]


def odd_formula(n):
    A=(2**n-2-3*sn(n))//4
    return 4*(A+ (6 if n%3==0 else 0))


def direct_rim_and_inserted(n,k):
    # Independent enumeration: named hub fixed to 0, enumerate rim words and
    # inserted vertex word by direct local choices, checking neighborhoods.
    m=k-1
    total=0
    for rim in product(range(1,k),repeat=n):
        if any(rim[i]==rim[(i+1)%n] for i in range(n)):continue
        multiplicities=[rim.count(a) for a in range(1,k)]
        if any(j%2==0 for j in multiplicities):continue
        # For optimized low-order verification classify inserted-word mode.
        for inserted in product(range(k),repeat=n):
            if any(inserted[i] in (rim[i],rim[(i+1)%n]) for i in range(n)):continue
            if any(not (inserted[i-1]==0 and inserted[i]==0 or 
                         inserted[i-1]!=0 and inserted[i]!=0 and inserted[i-1]!=inserted[i])
                   for i in range(n)):continue
            # Independently verify the actual graph's per-vertex open neighborhoods.
            graph=[set() for _ in range(2*n+1)]
            def edge(a,b):graph[a].add(b);graph[b].add(a)
            for i in range(n):
                edge(0,1+i)
                edge(1+i,1+n+i)
                edge(1+n+i,1+(i+1)%n)
            color=[0]+list(rim)+list(inserted)
            assert all(color[a]!=color[b] for a in range(len(graph)) for b in graph[a])
            assert all(all(sum(color[b]==c for b in graph[a])%2==1
                           for c in set(color[b] for b in graph[a])) for a in range(len(graph)))
            total+=1
    return k*total


def special_68():
    n=5
    sets=[set(range(n))-{i,(i+1)%n} for i in range(n)]
    signed=[0]*6
    for mask in range(1<<n):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for i in range(n):
            if mask&(1<<i):parent[root(i)]=root((i-1)%n)
        blocks={}
        for i in range(n):blocks.setdefault(root(i),[]).append(i)
        x=1
        for b in blocks.values():
            x*=len(set.intersection(*(sets[i] for i in b)))
        signed[mask.bit_count()]+=x
    assert signed==[243,270,105,10,0,0]
    return sum((-1)**i * a for i,a in enumerate(signed))


def main():
    assert special_68()==68
    # Fully enumerate with two methods (transition DP versus explicit vertex coloring).
    targets=[(3,4,48),(4,5,None),(5,6,49680),(6,3,6),(7,4,168)]
    for n,k,want in targets:
        q=count_opt(n,k)
        brute=direct_rim_and_inserted(n,k)
        assert q==brute,(n,k,q,brute)
        if want is not None:assert q==want,(n,q,want)
        print('DIRECT_OK',n,k,q)
    # All-order parity/transfer proof is separate from these finite experiments.
    for n in range(3,41,2):
        if n==5:continue
        assert count_opt(n,4)==odd_formula(n),(n,count_opt(n,4),odd_formula(n))
    for n in [4,8,12,16,20]:
        print('EVEN_MULT4_COUNT',n,count_opt(n,5))
    for n in [6,10,14,18,22]:assert count_opt(n,3)==6
    for n in range(3,13):
        k=predicted_k(n)
        assert count_opt(n,k)>0,(n,k)
        for j in range(2,k):assert count_opt(n,j)==0,(n,j)
    print('VERIFY_OK analytic_odd=3..39 parity_DP=3..12 boundary_and_two_modes=pass')

if __name__=='__main__':main()
