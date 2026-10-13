from itertools import combinations
from collections import deque


def half_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(i,n):
            adj[i].add(n+j)
            adj[n+j].add(i)
    return adj


def distances(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[10**9]*N
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D


def visible_avoiding(adj,D,x,y,S):
    blocked=set(S)-{x,y}
    d=[10**9]*len(adj)
    d[x]=0
    q=deque([x])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v in blocked:
                continue
            if d[v]==10**9:
                d[v]=d[u]+1
                q.append(v)
    return d[y]==D[x][y]


def mutual_visible(adj,D,S):
    S=set(S)
    return all(visible_avoiding(adj,D,x,y,S) for x,y in combinations(S,2))

checked=0
print('VERIFY_OK')
for n in range(3,11):
    adj=half_graph(n)
    D=distances(adj)
    N=2*n
    candidate=frozenset(set(range(N))-{0,2*n-1})
    assert mutual_visible(adj,D,candidate)

    for S in combinations(range(N),N-1):
        checked += 1
        assert not mutual_visible(adj,D,S),(n,'size N-1',S)

    actual=[]
    for S in combinations(range(N),N-2):
        checked += 1
        if mutual_visible(adj,D,S):
            actual.append(frozenset(S))
    assert actual==[candidate] or set(actual)=={candidate},(n,actual)
    print(f'n={n}: mu={N-2}, maximum_sets=1, omitted=a1,b{n}')

print('candidate_sets_checked =',checked)
print('all maximum sets were exactly V(H_n) minus {a1,b_n}')
