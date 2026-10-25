#!/usr/bin/env python3
"""Independent exact finite checks for zero forcing bases of the Möbius ladder."""
from itertools import combinations
from collections import Counter, deque

def adj_mob(n):
    N=2*n
    return [((1<<((i-1)%N)) | (1<<((i+1)%N)) | (1<<((i+n)%N))) for i in range(N)]

def force(adj,blue):
    full=(1<<len(adj))-1
    while blue!=full:
        add=0
        for u,row in enumerate(adj):
            if blue & (1<<u):
                white=row & ~blue
                if white and not (white & (white-1)):
                    add|=white
        if not add: return False
        blue|=add
    return True

def reps(n):
    N=2*n
    return [(0,1,2,3),(0,1,2,n),(0,1,2,n+2),
            (0,1,3,n+1),(0,1,n-1,n),(0,1,n,N-2),(0,1,n,n+1)]

def templates(n):
    N=2*n
    return {sum(1<<((x+j)%N) for x in r) for r in reps(n) for j in range(N)}

def exchange(states,N):
    state_set=set(states)
    graph={s:set() for s in states}
    for s in states:
        for v in range(N):
            if s>>v&1:
                for w in range(N):
                    if not (s>>w&1):
                        t=(s & ~(1<<v)) | (1<<w)
                        if t in state_set:graph[s].add(t)
    return graph

for n in range(6,15):
    N=2*n
    adj=adj_mob(n)
    actual=set()
    for c in combinations(range(N),4):
        s=sum(1<<v for v in c)
        if force(adj,s):actual.add(s)
    predicted=templates(n)
    assert actual==predicted,('classification failure',n,actual^predicted)
    if n<=10:
        assert not any(force(adj,sum(1<<v for v in c)) for c in combinations(range(N),3))
    graph=exchange(actual,N)
    dist=Counter(len(v) for v in graph.values())
    assert dist==Counter({5:4*n,8:8*n,12:n}),('degrees',n,dist)
    edgecount=sum(map(len,graph.values()))//2
    assert edgecount==48*n
    root=next(iter(actual));reached={root};queue=deque([root])
    while queue:
        for t in graph[queue.popleft()]:
            if t not in reached:reached.add(t);queue.append(t)
    assert reached==actual
    print('n=%d vertices=%d edges=%d degree=(%s) connected=yes four_sets_checked=%d' %
          (n,len(actual),edgecount,sorted(dist.items()),len(actual)))
print('PASS exhaustive enumeration through n=14; 3-set lower bound through n=10')
