from itertools import combinations
from collections import deque

def spider2(q):
    # center c=0; arm i has u_i=1+2*i and v_i=2+2*i
    N=1+2*q
    adj=[set() for _ in range(N)]
    edges=[]
    def add(a,b):
        adj[a].add(b); adj[b].add(a); edges.append((a,b))
    for i in range(q):
        u=1+2*i; v=2+2*i
        add(0,u); add(u,v)
    return adj,edges

def distances(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[10**9]*N
        d[s]=0
        Q=deque([s])
        while Q:
            x=Q.popleft()
            for y in adj[x]:
                if d[y]==10**9:
                    d[y]=d[x]+1
                    Q.append(y)
        D.append(d)
    return D

def mixed_resolves(D,edges,S):
    S=tuple(S)
    reps=[]
    for v in range(len(D)):
        reps.append(tuple(D[s][v] for s in S))
    for a,b in edges:
        reps.append(tuple(min(D[s][a],D[s][b]) for s in S))
    return len(reps)==len(set(reps))

def dominates(adj,S):
    S=set(S)
    return all(v in S or bool(adj[v] & S) for v in range(len(adj)))

checked=0
print("VERIFY_OK")
for q in range(3,9):
    adj,edges=spider2(q)
    D=distances(adj)
    leaves={2+2*i for i in range(q)}
    expected={frozenset(leaves|{0})}
    expected |= {frozenset(leaves|{1+2*i}) for i in range(q)}

    # Verify every set smaller than q+1 fails the combined property.
    for k in range(q+1):
        for S in combinations(range(1+2*q),k):
            checked += 1
            assert not (mixed_resolves(D,edges,S) and dominates(adj,S))

    actual=set()
    for S in combinations(range(1+2*q),q+1):
        checked += 1
        if mixed_resolves(D,edges,S) and dominates(adj,S):
            actual.add(frozenset(S))

    assert actual==expected,(q,len(actual),len(expected),actual^expected)

    # Stronger structural check: every mixed resolving set contains every leaf.
    for S in combinations(range(1+2*q),q):
        if mixed_resolves(D,edges,S):
            assert set(S)==leaves

    print(f"q={q}: gamma_mr={q+1}, minimum_bases={len(actual)}")

print("candidate_subsets_checked =",checked)
print("all minimum dominant mixed bases matched leaves plus center-or-one-support classification")
