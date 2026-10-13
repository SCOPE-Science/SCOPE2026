from itertools import combinations
from collections import deque

def half_graph(n):
    adj=[set() for _ in range(2*n)]
    edges=[]
    for i in range(n):
        for j in range(i,n):
            u=i
            v=n+j
            adj[u].add(v)
            adj[v].add(u)
            edges.append((u,v))
    return adj,edges

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

def is_vertex_cover(edges,S):
    S=set(S)
    return all(u in S or v in S for u,v in edges)

def edge_signature(D,e,S):
    u,v=e
    return tuple(min(D[s][u],D[s][v]) for s in S)

def is_edge_resolving(D,edges,S):
    seen=set()
    for e in edges:
        r=edge_signature(D,e,S)
        if r in seen:
            return False
        seen.add(r)
    return True

def expected_bases(n):
    return {
        frozenset(list(range(t)) + [n+j for j in range(t,n)])
        for t in range(n+1)
    }

checked=0
print("VERIFY_OK")
for n in range(2,10):
    adj,edges=half_graph(n)
    D=distances(adj)

    for S in combinations(range(2*n),n-1):
        checked += 1
        assert not is_vertex_cover(edges,S)

    actual=set()
    covers=set()
    for S in combinations(range(2*n),n):
        checked += 1
        if is_vertex_cover(edges,S):
            covers.add(frozenset(S))
            if is_edge_resolving(D,edges,S):
                actual.add(frozenset(S))

    expected=expected_bases(n)
    assert covers==expected,(n,len(covers),len(expected),covers^expected)
    assert actual==expected,(n,len(actual),len(expected),actual^expected)
    print(f"n={n}: Ddim_e={n}, minimum_vertex_covers={len(covers)}, dominant_edge_metric_bases={len(actual)}")

print("candidate_subsets_checked =",checked)
print("all size-n minimum vertex covers were exactly the n+1 canonical cuts")
print("every canonical cut edge-resolved the half graph")
