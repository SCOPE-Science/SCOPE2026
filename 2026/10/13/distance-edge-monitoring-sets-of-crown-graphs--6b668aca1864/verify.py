from collections import deque, Counter
from math import comb


def crown(n):
    N=2*n
    A=list(range(n)); B=list(range(n,2*n))
    adj=[set() for _ in range(N)]
    edges=[]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            u=i; v=n+j
            adj[u].add(v); adj[v].add(u); edges.append((u,v))
    return A,B,adj,edges


def distances(adj,s,skip=None):
    N=len(adj); INF=10**9
    d=[INF]*N; d[s]=0
    q=deque([s]); skip=frozenset(skip) if skip else None
    while q:
        u=q.popleft()
        for v in adj[u]:
            if skip is not None and frozenset((u,v))==skip:
                continue
            if d[v]==INF:
                d[v]=d[u]+1; q.append(v)
    return d


def monitor_masks(adj,edges):
    N=len(adj)
    base=[distances(adj,x) for x in range(N)]
    masks=[]
    probe_edge_checks=0
    for e in edges:
        removed=[distances(adj,x,e) for x in range(N)]
        mask=0
        for x in range(N):
            probe_edge_checks += 1
            if any(removed[x][y] > base[x][y] for y in range(N)):
                mask |= 1<<x
        masks.append(mask)
    return masks,probe_edge_checks


def is_dem(masks,S):
    return all(S & m for m in masks)


def is_vertex_cover(edges,S):
    return all(((S>>u)&1) or ((S>>v)&1) for u,v in edges)


def expected_coeff(n):
    # D_n(z)=2 z^n(1+z)^n-z^(2n)+n z^(2n-2)
    c=[0]*(2*n+1)
    for j in range(n+1):
        c[n+j]+=2*comb(n,j)
    c[2*n]-=1
    c[2*n-2]+=n
    return c

print('VERIFY_OK')
total_subsets=0
total_probe_edge_checks=0
total_bases=0
for n in range(4,8):
    A,B,adj,edges=crown(n)
    masks,checks=monitor_masks(adj,edges)
    total_probe_edge_checks += checks
    N=2*n
    # Structural lemma: each probe monitors exactly its incident edges.
    for e,m in zip(edges,masks):
        want=(1<<e[0]) | (1<<e[1])
        assert m==want,(n,e,m,want)
    counts=Counter()
    for S in range(1<<N):
        total_subsets += 1
        d=is_dem(masks,S)
        vc=is_vertex_cover(edges,S)
        assert d==vc,(n,S,d,vc)
        if d: counts[S.bit_count()]+=1
    got=[counts[k] for k in range(N+1)]
    want=expected_coeff(n)
    assert got==want,(n,got,want)
    dim=min(counts)
    assert dim==n,(n,dim)
    assert counts[n]==2,(n,counts[n])
    total_bases += counts[n]
    print(f'n={n}: edges={len(edges)}, DEM_sets={sum(counts.values())}, minimum={dim}, bases={counts[n]}')

# Boundary: Cr_3=C_6 does not satisfy the theorem and has dem=2.
A,B,adj,edges=crown(3)
masks,checks=monitor_masks(adj,edges)
total_probe_edge_checks += checks
counts=Counter()
for S in range(1<<6):
    if is_dem(masks,S): counts[S.bit_count()]+=1
assert min(counts)==2
assert any(m != ((1<<e[0])|(1<<e[1])) for e,m in zip(edges,masks))
print('boundary_n=3: minimum=2, incident-edge-only property fails')
print('n_checked = 4..7 plus boundary n=3')
print('vertex_subsets_checked =',total_subsets + (1<<6))
print('probe_edge_checks =',total_probe_edge_checks)
print('minimum_bases_checked =',total_bases)
print('all n>=4 DEM sets matched vertex covers')
print('all DEM polynomial coefficients matched')
