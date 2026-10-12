from itertools import combinations
from collections import deque, Counter

def split_graph(m,n):
    # clique C = 0..m-1, independent I = m..m+n-1
    N=m+n
    adj=[set() for _ in range(N)]
    edges=[]
    for u in range(m):
        for v in range(u+1,m):
            adj[u].add(v); adj[v].add(u); edges.append((u,v))
    for u in range(m):
        for j in range(n):
            v=m+j
            adj[u].add(v); adj[v].add(u); edges.append((u,v))
    return adj,edges

def all_dist(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def edist(D,s,e):
    u,v=e
    return min(D[s][u],D[s][v])

def local_edge_resolving(adj,edges,S):
    S=set(S)
    for i,e in enumerate(edges):
        for f in edges[i+1:]:
            if not (set(e)&set(f)):
                continue
            if not any(edist(D,s,e)!=edist(D,s,f) for s in S):
                return False
    return True

def predicted(m,n,S):
    S=set(S)
    N=m+n
    if m==1:
        # all but at most one leaf must be selected; center arbitrary
        leaves=set(range(1,N))
        return len(leaves-S)<=1
    return len(set(range(N))-S)<=1

graphs=0
subset_trials=0
basis_count=0
for m in range(1,7):
    for n in range(1,7):
        adj,edges=split_graph(m,n)
        D=all_dist(adj)
        N=m+n
        counts=Counter()
        for mask in range(1<<N):
            S=[v for v in range(N) if (mask>>v)&1]
            if not S:
                # introducing paper requires nonempty local edge metric generators
                actual=False
            else:
                actual=local_edge_resolving(adj,edges,S)
            pred=predicted(m,n,S) and bool(S)
            assert actual==pred,(m,n,S,actual,pred)
            subset_trials+=1
            if actual: counts[len(S)]+=1
        dim=min(counts)
        if m==1 and n==1:
            assert dim==1 and counts[1]==2
        elif m==1:
            assert dim==n-1
            assert counts[n-1]==n
        else:
            assert dim==N-1
            assert counts[N-1]==N
        basis_count += counts[dim]
        graphs+=1

print("VERIFY_OK")
print("parameter_pairs_checked =",graphs)
print("m,n ranges = 1..6")
print("vertex_subsets_checked =",subset_trials)
print("minimum_bases_checked =",basis_count)
print("all direct adjacent-edge tests matched the classification")
print("all minimum dimensions and basis counts matched")
