#!/usr/bin/env python3
"""Independent finite checks of minimum vertex-isometric-path cover for theta graphs.
Constructs original graph; enumerates geodesics through exact all-pairs distances.
"""
from collections import deque
from itertools import combinations_with_replacement
from random import Random

def graph(a,b,c):
    lens=(a,b,c); n=a+b+c-1; adj=[[] for _ in range(n)]; arms=[]; nxt=2
    for l in lens:
        vs=(0,*range(nxt,nxt+l-1),1);nxt+=l-1;arms.append(vs)
        for x,y in zip(vs,vs[1:]): adj[x].append(y);adj[y].append(x)
    assert nxt==n
    return adj,arms

def paths(adj):
    n=len(adj); D=[]
    for s in range(n):
        d=[n+1]*n;d[s]=0;q=deque([s]);
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w]>d[v]+1:
                    d[w]=d[v]+1;q.append(w)
        D.append(d)
    masks=set()
    for s in range(n):
      for t in range(s+1,n):
        d=D[s][t]
        def dfs(v,mask):
            if v==t: masks.add(mask);return
            for w in adj[v]:
                if D[s][w]==D[s][v]+1 and D[s][w]+D[w][t]==d:
                    dfs(w,mask|1<<w)
        dfs(s,1<<s)
    return list(masks),D

def has_two(paths,n):
    target=(1<<n)-1
    for i,x in enumerate(paths):
        for y in paths[i+1:]:
            if x|y==target:return True
    return False

def formula(a,b,c):
    return (a,b) in ((2,2),(2,3)) or (a,b)==(2,4) and c%2==0 or (a,b)==(3,3) and c%2==1

def main():
    count=0
    for a,b,c in combinations_with_replacement(range(2,15),3):
        G,arms=graph(a,b,c); P,D=paths(G)
        got=has_two(P,len(G))
        assert got==formula(a,b,c),(a,b,c,got)
        count+=1
    print('ALL_UNORDERED_LENGTH_TRIPLES_2_TO_14_OK',count)
    r=Random(251030)
    cases=[(a,b,c) for a in (2,3,4,5,6,7) for b in (a,max(a,7),max(a,16)) for c in (b,b+1,b+2,2*b,3*b+1) if c<=56]
    cases=list(set(cases));r.shuffle(cases)
    for a,b,c in cases[:80]:
        G,_=graph(a,b,c);P,D=paths(G)
        got=has_two(P,len(G))
        assert got==formula(a,b,c),(a,b,c,got)
    print('ADDITIONAL_WIDE_TRIPLES_OK',min(80,len(cases)))
    print('EXHAUSTIVE_GEODESIC_PAIR_CHECKS_OK')


def constructive_witnesses(a,b,c):
    G, (A,B,C)=graph(a,b,c)
    x,y=b//2,c//2
    three=[A, B[x::-1]+C[1:y+1], B[x+1:]+C[-2:y:-1]]
    two=None
    if formula(a,b,c):
        lo=(b+c-3)//2
        hi=(c-a+2)//2
        assert lo<=hi
        h=hi
        two=[A[-2::-1]+C[1:h+1], B[1:]+C[-2:h:-1]]
    return G,three,two

def verify_path_cover(adj,route_set):
    n=len(adj)
    union=set()
    for P in route_set:
        assert P and len(P)==len(set(P))
        assert all(v in adj[u] for u,v in zip(P,P[1:]))
        dist=[-1]*n
        dist[P[0]]=0
        q=deque([P[0]])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]<0:
                    dist[v]=dist[u]+1
                    q.append(v)
        assert dist[P[-1]]==len(P)-1
        union.update(P)
    assert union==set(range(n))

def check_constructions():
    count=0
    for a,b,c in combinations_with_replacement(range(2,20),3):
        G,three,two=constructive_witnesses(a,b,c)
        verify_path_cover(G,three)
        if two is not None:
            verify_path_cover(G,two)
        count+=1
    print('EXPLICIT_TWO_AND_THREE_PATH_CONSTRUCTIONS_OK',count)

if __name__=='__main__':
    main()
    check_constructions()
    print('VERIFY_OK')
