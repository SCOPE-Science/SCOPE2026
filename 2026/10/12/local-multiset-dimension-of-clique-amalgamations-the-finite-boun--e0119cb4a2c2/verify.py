from itertools import combinations
from collections import deque, Counter


def amalgamation_cliques(r,t):
    # r copies of K_t sharing center 0. Blade i has t-1 outer vertices.
    q=t-1
    n=1+r*q
    adj=[set() for _ in range(n)]
    blades=[]
    for i in range(r):
        B=list(range(1+i*q,1+(i+1)*q))
        blades.append(B)
        verts=[0]+B
        for a,b in combinations(verts,2):
            adj[a].add(b); adj[b].add(a)
    return adj,blades


def all_distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[-1]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def rep(D,v,S):
    return tuple(sorted(D[v][s] for s in S))


def is_local_multiset_resolving(adj,D,S):
    R=[rep(D,v,S) for v in range(len(adj))]
    for u in range(len(adj)):
        for v in adj[u]:
            if u<v and R[u]==R[v]:
                return False
    return True

subset_trials=0
finite_bases=0
cases=[]

# Exhaustively check a broad finite range. This directly evaluates definitions.
for t in (2,3,4,5):
    max_r = 5 if t<=4 else 4
    for r in range(2,max_r+1):
        adj,blades=amalgamation_cliques(r,t)
        D=all_distances(adj)
        n=len(adj)
        good_by_size=Counter()
        bases=[]
        for mask in range(1<<n):
            subset_trials+=1
            S=[v for v in range(n) if (mask>>v)&1]
            if is_local_multiset_resolving(adj,D,S):
                good_by_size[len(S)]+=1
                bases.append(frozenset(S))
        if t==2:
            assert min(good_by_size)==1, (r,t,good_by_size)
            actual={S for S in bases if len(S)==1}
            expected={frozenset([v]) for v in range(n)}
            assert actual==expected,(r,t,actual,expected)
            finite_bases+=len(actual)
        elif t==3:
            assert min(good_by_size)==r,(r,t,good_by_size)
            actual={S for S in bases if len(S)==r}
            expected=set()
            for choices in __import__('itertools').product((0,1), repeat=r):
                expected.add(frozenset(blades[i][choices[i]] for i in range(r)))
            assert actual==expected,(r,t,len(actual),len(expected))
            assert len(actual)==2**r
            finite_bases+=len(actual)
        else:
            assert not good_by_size,(r,t,good_by_size)
        cases.append((r,t,n))

print('VERIFY_OK')
print('parameter_pairs_checked =', len(cases))
print('parameters =', cases)
print('vertex_subsets_checked =', subset_trials)
print('finite_minimum_bases_checked =', finite_bases)
print('t=2: local multiset dimension 1; every singleton is a basis')
print('t=3: local multiset dimension r; bases choose one outer vertex per triangle')
print('t>=4: no local multiset resolving set exists in every checked case')
