from itertools import combinations
from collections import deque

def half_graph(n):
    # vertices 0..n-1 = a_1..a_n, n..2n-1 = b_1..b_n
    N=2*n
    adj=[set() for _ in range(N)]
    edges=[]
    for i in range(n):
        for j in range(n):
            if i <= j:
                u=i; v=n+j
                adj[u].add(v); adj[v].add(u); edges.append((u,v))
    return adj,edges

def distances(adj):
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

def element_signatures(D,edges):
    N=len(D)
    sig=[]
    # vertices first
    for v in range(N):
        sig.append(tuple(D[s][v] for s in range(N)))
    for u,v in edges:
        sig.append(tuple(min(D[s][u],D[s][v]) for s in range(N)))
    return sig

def separator_masks(sig):
    N=len(sig[0]); out=[]
    for i,j in combinations(range(len(sig)),2):
        m=0
        si,sj=sig[i],sig[j]
        for s in range(N):
            if si[s]!=sj[s]: m |= 1<<s
        assert m != 0
        out.append(m)
    return out

def is_mixed(mask,seps):
    return all(mask & s for s in seps)

def expected_bases(n):
    # forced b_1 (index n) and a_n (index n-1); exactly one of a_i,b_i for 2<=i<=n-1
    fixed=(1<<(n-1)) | (1<<n)
    out=set()
    for bits in range(1 << max(0,n-2)):
        m=fixed
        for i in range(1,n-1):
            # i is zero-based index for diagonal pair a_{i+1}, b_{i+1}
            if (bits>>(i-1))&1:
                m |= 1<<i
            else:
                m |= 1<<(n+i)
        out.add(m)
    return out

total_subsets=0
total_bases=0
for n in range(2,9):
    adj,edges=half_graph(n)
    D=distances(adj)
    sig=element_signatures(D,edges)
    seps=separator_masks(sig)
    N=2*n
    exp=expected_bases(n)
    assert len(exp)==2**(n-2)
    for m in exp:
        assert m.bit_count()==n and is_mixed(m,seps)
    # Exhaust every subset of size <= n, which is enough to prove the minimum and basis classification.
    got=set()
    smaller=0
    checks=0
    for k in range(n+1):
        for comb in combinations(range(N),k):
            mask=0
            for v in comb: mask |= 1<<v
            checks += 1
            if is_mixed(mask,seps):
                if k<n: smaller += 1
                elif k==n: got.add(mask)
    assert smaller==0, (n,smaller)
    assert got==exp, (n,len(got),len(exp),got^exp)
    total_subsets += checks
    total_bases += len(got)
    print(f'n={n}: order={N}, edges={len(edges)}, elements={len(sig)}, subsets_size_le_n={checks}, bases={len(got)}')

print('VERIFY_OK')
print('n_range = 2..8')
print('subsets_checked_size_at_most_n =', total_subsets)
print('minimum_bases_checked =', total_bases)
print('all smaller subsets failed mixed resolution')
print('all size-n mixed bases matched the forced-endpoint diagonal-transversal classification')
