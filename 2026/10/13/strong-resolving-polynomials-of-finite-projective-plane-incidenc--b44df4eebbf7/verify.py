#!/usr/bin/env python3
"""Finite checks for strong resolving sets in small projective-plane incidence graphs."""
from collections import Counter, deque
from math import comb

def projective(q):
    def normal(a):
        for v in a:
            if v: return tuple((x*pow(v,-1,q))%q for x in a)
        raise ValueError('zero vector')
    triples={(x,y,z) for x in range(q) for y in range(q) for z in range(q)}-{(0,0,0)}
    pts=sorted({normal(t) for t in triples})
    n=len(pts); assert n==q*q+q+1
    adj=[set() for _ in range(2*n)]
    for i,p in enumerate(pts):
        for j,l in enumerate(pts):
            if sum(a*b for a,b in zip(p,l))%q==0:
                adj[i].add(n+j);adj[n+j].add(i)
    assert all(len(a)==q+1 for a in adj)
    dist=[]
    for s in range(2*n):
        d=[-1]*(2*n);d[s]=0;Q=deque([s])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[v]==-1: d[v]=d[u]+1;Q.append(v)
        assert max(d)==3
        dist.append(d)
    return n,adj,dist

def predicted(q):
    n=q*q+q+1;k=q+1
    c=Counter()
    for j in range(n+1):c[j]+=2*comb(n,j)
    c[0]-=1
    for j in range(1,k+1):c[j+1]+=2*n*comb(k,j)
    c[2]-=n*k
    return c

def check(q):
    n,adj,d=projective(q);N=2*n
    mmd=set(); nonincident=set(); stronger=[]
    for u in range(N):
        for v in range(u+1,N):
            if all(d[x][v]<=d[u][v] for x in adj[u]) and all(d[x][u]<=d[u][v] for x in adj[v]):mmd.add((u,v))
            if u<n and v>=n and v not in adj[u]: nonincident.add((u,v))
    assert mmd==nonincident
    C=predicted(q)
    incid=[sum(1<<j for j in range(n) if n+j in adj[i]) for i in range(n)]
    actual=Counter()
    maximal=Counter()
    line_points=[sum(1<<i for i in range(n) if (incid[i]>>j)&1) for j in range(n)]
    # Exhaust all point-choices and then all line choices meeting every chosen point.
    for p in range(1<<n):
        allowed=(1<<n)-1
        for i in range(n):
            if (p>>i)&1:allowed&=incid[i]
        l=allowed
        while True:
            actual[p.bit_count()+l.bit_count()]+=1
            allowed_points=(1<<n)-1
            for j in range(n):
                if (l>>j)&1:allowed_points&=line_points[j]
            if allowed==l and allowed_points==p: maximal[p.bit_count()+l.bit_count()]+=1
            if l==0:break
            l=(l-1)&allowed
    assert actual==C,(q,actual,C)
    assert max(actual)==n and actual[n]==2
    assert sum(actual.values())==sum(C.values())
    assert maximal==Counter({n:2,n-(n-(q+2)):2*n}), (q,maximal)
    print('VERIFY_OK',f'PG(2,{q})',f'points={n}',f'lines={n}',f'MMD_edges={len(mmd)}',f'all_independent_sets={sum(actual.values())}',f'strong_bases={actual[n]}')
    print('VERIFY_OK',f'PG(2,{q})',f'independent_counts={dict(sorted(actual.items()))}')
    print('VERIFY_OK',f'PG(2,{q})',f'maximal_independent_sets={dict(sorted(maximal.items()))}')
    if q==2:
        witness=[]
        for u in range(N):
            for v in range(u+1,N):
                wm=sum(1<<w for w in range(N) if d[w][u]==d[w][v]+d[u][v] or d[w][v]==d[w][u]+d[u][v])
                witness.append(wm)
        tested=Counter()
        for s in range(1<<N):
            direct=all(s&w for w in witness)
            covers=all(((s>>u)&1) or ((s>>v)&1) for u,v in mmd)
            assert direct==covers
            if direct:tested[s.bit_count()]+=1
        assert tested==Counter({N-j:num for j,num in C.items()})
        print('VERIFY_OK',f'PG(2,{q})',f'exhaustive_strong_resolvers={1<<N}',f'count={sum(tested.values())}',f'poly={dict(sorted(tested.items()))}')

for q in (2,3): check(q)
print('VERIFY_FINISHED all invariants established')
