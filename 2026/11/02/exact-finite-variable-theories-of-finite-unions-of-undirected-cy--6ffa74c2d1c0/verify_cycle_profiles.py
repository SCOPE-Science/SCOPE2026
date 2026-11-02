#!/usr/bin/env python3
"""Direct checks of the length predicates and multiplicity invariants."""
from collections import Counter, deque
from itertools import combinations_with_replacement

def graph(lengths):
    lengths=list(lengths)
    adj=[]
    for n in lengths:
        if n<3: raise ValueError(n)
        start=len(adj)
        for i in range(n):
            adj.append({start+(i-1)%n,start+(i+1)%n})
    return adj

def distances(adj,start):
    dist={start:0}; q=deque([start])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    return dist

def local_size_predicate(adj,x,n):
    """Graph interpretation of the three-variable P_n(x) formula."""
    d=n//2
    ds=distances(adj,x)
    exact_d=sum(t==d for t in ds.values())
    if n%2==0:
        return exact_d==1
    return exact_d>=2 and all(t!=d+1 for t in ds.values())

def actual_profile(adj):
    seen=set(); result=Counter()
    for u in range(len(adj)):
        if u in seen:continue
        comp=distances(adj,u)
        seen.update(comp); result[len(comp)]+=1
    return result

def observed_profile(adj,max_n):
    out=Counter()
    for n in range(3,max_n+1):
        d=n//2; visited=set(); count=0
        for u in range(len(adj)):
            if local_size_predicate(adj,u,n):
                if u not in visited:
                    visited.update(distances(adj,u))
                    count+=1
        if count:out[n]=count
    return out

def main():
    cases=0; vertices=0; pred=0; counts=0
    for r in range(0,4):
        for lengths in combinations_with_replacement(range(3,9),r):
            adj=graph(lengths)
            target=Counter(lengths)
            empirical=observed_profile(adj,10)
            assert empirical==target,(lengths,empirical,target)
            for u in range(len(adj)):
                hits=[n for n in range(3,11) if local_size_predicate(adj,u,n)]
                assert hits==[len(distances(adj,u))],(lengths,u,hits)
                pred+=8
            for k in range(3,7):
                compressed={n:min(m,k) for n,m in target.items()}
                assert compressed=={n:min(actual_profile(adj)[n],k) for n in target}
                counts+=1
            cases+=1;vertices+=len(adj)
    print('PROFILE_OK cases=%d vertices=%d length_predicate_evaluations=%d cutoff_cases=%d' % (cases,vertices,pred,counts))
if __name__=='__main__':main()
