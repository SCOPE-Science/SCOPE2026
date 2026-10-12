from itertools import combinations
from collections import deque

def windmill_graph(r,m):
    # W_{r,m}=K_1 join r K_m. center=0; blade i has m outer vertices.
    n=1+r*m
    adj=[set() for _ in range(n)]
    edges=[]
    for i in range(r):
        blade=list(range(1+i*m,1+(i+1)*m))
        for v in blade:
            adj[0].add(v); adj[v].add(0); edges.append((0,v))
        for a,b in combinations(blade,2):
            adj[a].add(b); adj[b].add(a); edges.append((a,b))
    return adj,edges

def all_distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def edge_distance(D,s,e):
    u,v=e
    return min(D[s][u],D[s][v])

def adjacent_pairs(edges):
    return [(i,j) for i,j in combinations(range(len(edges)),2)
            if set(edges[i]).intersection(edges[j])]

def is_local_edge_resolving(D,edges,pairs,S):
    for i,j in pairs:
        if all(edge_distance(D,s,edges[i])==edge_distance(D,s,edges[j]) for s in S):
            return False
    return True

cases=0
subset_trials=0
bases_checked=0

for r in range(2,6):
    for m in range(2,4):
        adj,edges=windmill_graph(r,m)
        D=all_distances(adj)
        pairs=adjacent_pairs(edges)
        n=len(adj)
        target=r*m-1

        actual=set()
        for k in range(target+1):
            for S in combinations(range(n),k):
                subset_trials+=1
                good=is_local_edge_resolving(D,edges,pairs,S)
                if k<target:
                    assert not good,(r,m,k,S)
                elif good:
                    actual.add(frozenset(S))

        outer=set(range(1,n))
        expected={frozenset(outer-{v}) for v in outer}
        assert actual==expected,(r,m,len(actual),len(expected))
        assert len(actual)==r*m
        bases_checked+=len(actual)
        cases+=1

# Larger spot checks of every predicted basis.
for r,m in [(2,4),(2,5),(3,4),(4,4),(6,2)]:
    adj,edges=windmill_graph(r,m)
    D=all_distances(adj); pairs=adjacent_pairs(edges)
    outer=set(range(1,len(adj)))
    for v in outer:
        assert is_local_edge_resolving(D,edges,pairs,outer-{v}), (r,m,v)

print("VERIFY_OK")
print("fully_enumerated_parameter_pairs =", cases)
print("fully_enumerated r = 2..5, m = 2..3")
print("subset_trials =", subset_trials)
print("minimum_bases_checked =", bases_checked)
print("larger_spot_checks = (2,4), (2,5), (3,4), (4,4), (6,2)")
print("all local edge metric dimensions matched rm-1")
print("all minimum bases were exactly all outer vertices except one")
print("basis counts matched rm")
