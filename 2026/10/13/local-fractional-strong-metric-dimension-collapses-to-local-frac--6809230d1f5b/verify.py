from itertools import combinations
from collections import deque, Counter

def distances(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    D=[]
    for s in range(n):
        d=[-1]*n
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return adj,D

def connected(D):
    return all(x >= 0 for x in D[0])

def strong_resolves_adjacent(D,w,u,v):
    return (
        D[w][v] == D[w][u] + 1
        or
        D[w][u] == D[w][v] + 1
    )

def local_resolves(D,w,u,v):
    return D[w][u] != D[w][v]

connected_graphs=0
edge_neighborhoods=0
vertex_tests=0
orders=Counter()

for n in range(2,7):
    pairs=list(combinations(range(n),2))
    for mask in range(1,1<<len(pairs)):
        edges=[pairs[i] for i in range(len(pairs)) if (mask>>i)&1]
        adj,D=distances(n,edges)
        if not connected(D):
            continue
        connected_graphs += 1
        orders[n] += 1
        for u,v in edges:
            edge_neighborhoods += 1
            local=set()
            local_strong=set()
            for w in range(n):
                vertex_tests += 1
                if local_resolves(D,w,u,v):
                    local.add(w)
                if strong_resolves_adjacent(D,w,u,v):
                    local_strong.add(w)
            assert local == local_strong, (n,edges,(u,v),local,local_strong)

# Explicit C4 consequence: every vertex belongs to every local/local-strong
# resolving neighborhood, so constant weight 1/4 is feasible and has weight 1.
n=4
edges=[(0,1),(1,2),(2,3),(3,0)]
adj,D=distances(n,edges)
for u,v in edges:
    L={w for w in range(n) if local_resolves(D,w,u,v)}
    LS={w for w in range(n) if strong_resolves_adjacent(D,w,u,v)}
    assert L==LS==set(range(n))
print("VERIFY_OK")
print("connected_labeled_graphs_checked =", connected_graphs)
print("counts_by_order =", dict(orders))
print("edge_neighborhoods_checked =", edge_neighborhoods)
print("vertex_membership_tests =", vertex_tests)
print("all local resolving neighborhoods equaled local strong resolving neighborhoods")
print("C4 has both fractional local dimensions equal to 1")
