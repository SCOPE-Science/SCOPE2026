"""Exhaustive direct graph/face checks for small cyclic hard-rod instances.
Run: python verify_direct.py
"""
from itertools import combinations
from collections import Counter,defaultdict,deque

def trial(k,m):
    q=k+1; n=q*m+2
    configurations=[]
    for a in combinations(range(n),m):
        if all(min((a[j]-a[i])%n,(a[i]-a[j])%n)>k for i in range(m) for j in range(i+1,m)):
            configurations.append(a)
    where={a:i for i,a in enumerate(configurations)}
    N=len(configurations); adj=[set() for _ in configurations]
    for i,a in enumerate(configurations):
        for x in a:
            for d in range(1,k+1):
                for sign in (-1,1):
                    y=(x+sign*d)%n
                    if y in a:continue
                    b=tuple(sorted((set(a)-{x})|{y}))
                    if b in where:adj[i].add(where[b])
    assert all(len(s)==4 for s in adj)
    assert all(i in adj[j] for i in range(N) for j in adj[i])
    assert N==n*(m+1)//2
    assert sum(len(s) for s in adj)//2==n*(m+1)
    A={i for i,a in enumerate(configurations) if any((a[(j+1)%m]-a[j])%n==q+2 for j in range(m))}
    assert len(A)==n
    triangles=[(i,j,l) for i in range(N) for j in adj[i] if j>i for l in adj[i]&adj[j] if l>j]
    squares=[]
    for i in range(N):
        for l in range(i+1,N):
            if l in adj[i]:continue
            for j,h in combinations(sorted(adj[i]&adj[l]),2):
                if h in adj[j]:continue
                squares.append((i,j,l,h))
    squares=list({tuple(sorted(f)):f for f in squares}.values())
    assert len(triangles)==n and len(squares)==n*(m-1)//2
    faces=triangles+squares
    incidences=Counter();links=[defaultdict(set) for _ in range(N)]
    for f in faces:
        for z,v in enumerate(f):
            u,w=f[z-1],f[(z+1)%len(f)]
            incidences[tuple(sorted((v,w)))]+=1
            links[v][u].add(w);links[v][w].add(u)
    boundary=defaultdict(set)
    for i in range(N):
        for j in adj[i]:
            if j<=i:continue
            times=incidences[i,j]
            assert times in (1,2)
            if times==1:
                assert i in A and j in A
                boundary[i].add(j);boundary[j].add(i)
    assert set(boundary)==A
    assert all(len(boundary[v])==2 for v in A)
    for v in range(N):
        link=links[v]
        seen={next(iter(link))};pending=list(seen)
        while pending:
            for w in link[pending.pop()]:
                if w not in seen:seen.add(w);pending.append(w)
        assert len(link)==4 and len(seen)==4
        degree_pattern=sorted(map(len,link.values()))
        assert degree_pattern==([1,1,2,2] if v in A else [2,2,2,2])
    remaining=set(A);bd_lengths=[]
    while remaining:
        seed=remaining.pop();todo=[seed];seen={seed}
        while todo:
            for v in boundary[todo.pop()]:
                if v in remaining:remaining.remove(v);seen.add(v);todo.append(v)
        bd_lengths.append(len(seen))
    assert sorted(bd_lengths)==[n//(2 if q%2==0 else 1)]*(2 if q%2==0 else 1)
    unseen=set(range(N));unseen.remove(0);queue=[0]
    for v in queue:
        for w in adj[v]:
            if w in unseen:unseen.remove(w);queue.append(w)
    assert not unseen
    print(f'DIRECT_PASS k={k} m={m} V={N} E={sum(map(len,adj))//2} F3={len(triangles)} F4={len(squares)} boundary={sorted(bd_lengths)}')

for k in range(2,6):
    for m in range(2,6):
        if (k+1)*m+2<=30:trial(k,m)
print('DIRECT_ALL_PASS')
