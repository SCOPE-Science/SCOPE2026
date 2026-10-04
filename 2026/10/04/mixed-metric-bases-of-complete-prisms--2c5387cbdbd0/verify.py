from itertools import combinations

def complete_prism(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for base in (0,n):
        for i in range(n):
            for j in range(i+1,n):
                adj[base+i].add(base+j); adj[base+j].add(base+i)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def all_distances(adj):
    n=len(adj)
    D=[]
    for s in range(n):
        d=[10**9]*n
        d[s]=0
        q=[s]
        for x in q:
            for y in adj[x]:
                if d[y]==10**9:
                    d[y]=d[x]+1
                    q.append(y)
        D.append(d)
    return D

def is_mixed_resolving(adj,D,S):
    n=len(adj)
    edges=[(u,v) for u in range(n) for v in adj[u] if u<v]
    seen={}
    for v in range(n):
        sig=tuple(D[v][s] for s in S)
        if sig in seen:
            return False
        seen[sig]=("v",v)
    for u,v in edges:
        sig=tuple(min(D[u][s],D[v][s]) for s in S)
        if sig in seen:
            return False
        seen[sig]=("e",(u,v))
    return True

def structural_basis(n,S):
    # exactly one of a_i,b_i per matching pair and at least two chosen in each layer
    x=0
    for i in range(n):
        a=(i in S); b=(n+i in S)
        if a+b != 1:
            return False
        if a:
            x += 1
    return 2 <= x <= n-2

pairs=subsets=bases=0
for n in range(5,10):
    adj=complete_prism(n)
    D=all_distances(adj)
    N=2*n

    # verify no set smaller than n resolves
    for k in range(n):
        for S in combinations(range(N),k):
            subsets += 1
            assert not is_mixed_resolving(adj,D,S), (n,k,S)

    actual=[]
    for S in combinations(range(N),n):
        subsets += 1
        good=is_mixed_resolving(adj,D,S)
        pred=structural_basis(n,set(S))
        assert good==pred,(n,S,good,pred)
        if good:
            actual.append(S)

    expected=(1<<n)-2*n-2
    assert len(actual)==expected,(n,len(actual),expected)
    bases += len(actual)
    pairs += 1

print("VERIFY_OK")
print("complete_prisms_checked =",pairs)
print("vertex_subsets_checked =",subsets)
print("minimum_mixed_bases_checked =",bases)
print("parameters n = 5..9")
print("all smaller subsets failed directly")
print("all size-n mixed bases matched the matching-transversal classification")
print("all basis counts matched 2^n - 2n - 2")
