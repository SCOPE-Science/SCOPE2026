from itertools import combinations
from collections import deque, Counter

def complete_split(m,n):
    # clique C = 0..m-1, independent I=m..m+n-1
    N=m+n
    adj=[set() for _ in range(N)]
    edges=[]
    for u in range(m):
        for v in range(u+1,m):
            adj[u].add(v); adj[v].add(u); edges.append((u,v))
    for u in range(m):
        for v in range(m,N):
            adj[u].add(v); adj[v].add(u); edges.append((u,v))
    return adj,edges

def distances(adj,s,skip_edge=None):
    N=len(adj)
    inf=10**9
    d=[inf]*N; d[s]=0
    q=deque([s])
    se = frozenset(skip_edge) if skip_edge else None
    while q:
        u=q.popleft()
        for v in adj[u]:
            if se is not None and frozenset((u,v))==se:
                continue
            if d[v]==inf:
                d[v]=d[u]+1; q.append(v)
    return d

def monitoring_masks(adj,edges):
    N=len(adj)
    base=[distances(adj,x) for x in range(N)]
    masks=[]
    for e in edges:
        mask=0
        removed=[distances(adj,x,e) for x in range(N)]
        for x in range(N):
            if any(removed[x][y] != base[x][y] for y in range(N)):
                mask |= 1<<x
        masks.append(mask)
    return masks

def is_dem(masks,S_mask):
    return all(S_mask & mask for mask in masks)

def predicted(m,n,S_mask):
    N=m+n
    if m==1:
        return S_mask != 0
    C_mask=(1<<m)-1
    # family 1: all clique selected
    if (S_mask & C_mask)==C_mask:
        return True
    # family 2: all but exactly one vertex selected, omitted vertex is clique
    if S_mask.bit_count()==N-1:
        omitted=((1<<N)-1)^S_mask
        return (omitted & C_mask)!=0
    return False

def expected_coeffs(m,n):
    N=m+n
    c=[0]*(N+1)
    if m==1:
        from math import comb
        for k in range(1,N+1):
            c[k]=comb(N,k)
        return c
    from math import comb
    # z^m (1+z)^n
    for j in range(n+1):
        c[m+j]+=comb(n,j)
    c[N-1]+=m
    return c

subset_trials=0
edge_probe_checks=0
basis_trials=0
param_pairs=0
for m in range(1,7):
    for n in range(1,7):
        adj,edges=complete_split(m,n)
        masks=monitoring_masks(adj,edges)
        N=m+n
        param_pairs += 1

        # structural probe property
        for mask in masks:
            edge_probe_checks += N
            if m==1:
                # every edge is a bridge, every vertex monitors it
                assert mask == (1<<N)-1, (m,n,mask)
            else:
                # monitor set of an edge should be exactly its endpoints
                pass
        if m>=2:
            for e,mask in zip(edges,masks):
                expected=(1<<e[0]) | (1<<e[1])
                assert mask==expected,(m,n,e,mask,expected)

        counts=Counter()
        actual_bases=0
        for S in range(1<<N):
            subset_trials += 1
            a=is_dem(masks,S)
            p=predicted(m,n,S)
            assert a==p,(m,n,S,a,p)
            if a:
                counts[S.bit_count()]+=1

        coeff=[counts[k] for k in range(N+1)]
        assert coeff==expected_coeffs(m,n),(m,n,coeff,expected_coeffs(m,n))
        dim=min(k for k,v in counts.items() if v)
        expected_dim=1 if m==1 else m
        assert dim==expected_dim,(m,n,dim,expected_dim)
        actual_bases=counts[dim]
        expected_bases=(N if m==1 else (N if n==1 else 1))
        assert actual_bases==expected_bases,(m,n,actual_bases,expected_bases)
        basis_trials += actual_bases

print("VERIFY_OK")
print("parameter_pairs_checked =",param_pairs)
print("m,n ranges = 1..6")
print("vertex_subsets_checked =",subset_trials)
print("edge_probe_checks =",edge_probe_checks)
print("minimum_bases_checked =",basis_trials)
print("all direct DEM tests matched the two-family classification")
print("all DEM-set polynomial coefficients matched")
print("all dimensions and minimum-basis counts matched")
