from itertools import combinations
from collections import deque


def build_half(n):
    edges=[]
    adj=[set() for _ in range(2*n)]
    for i in range(1,n+1):
        for j in range(i,n+1):
            eid=len(edges)
            u=i-1
            v=n+j-1
            edges.append((u,v,i,j))
            adj[u].add((v,eid)); adj[v].add((u,eid))
    return adj,edges


def all_dist(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[10**9]*N; d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v,_ in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def actual_geodesic_triples(n):
    adj,edges=build_half(n)
    D=all_dist(adj)
    out=set()
    # In H_n every geodesic containing three edges has length exactly three.
    # Enumerate all oriented length-three walks whose endpoint distance is three.
    for v0 in range(2*n):
        for v1,e1 in adj[v0]:
            for v2,e2 in adj[v1]:
                if v2==v0: continue
                for v3,e3 in adj[v2]:
                    if v3 in (v1,v0): continue
                    if D[v0][v3]==3:
                        out.add(frozenset((e1,e2,e3)))
    return out,edges


def formula_geodesic_triples(n,edges):
    idx={(i,j):eid for eid,(_,_,i,j) in enumerate(edges)}
    out=set()
    for l in range(1,n+1):
        for j in range(l,n+1):
            for i in range(j+1,n+1):
                for k in range(i,n+1):
                    out.add(frozenset((idx[(l,j)],idx[(l,k)],idx[(i,k)])))
    return out


def is_egp_mask(mask, forbidden_masks):
    return all((mask & t).bit_count() <= 2 for t in forbidden_masks)


def mapped_pair(i,j):
    return (i,j+1)


def predicted_max_masks(n,edges):
    N=n+1
    a=N//2
    sizes={a,N-a}
    masks=set()
    # Unordered balanced bipartitions, canonicalized by requiring bit 1 = 0
    # when the two sides have equal size; when unequal, side 0 is smaller.
    for bits in range(1<<N):
        ones=bits.bit_count()
        if N%2:
            if ones != a: continue
        else:
            if ones != a or (bits & 1): continue
        seq=[(bits>>p)&1 for p in range(N)]
        runs=1+sum(seq[p]!=seq[p-1] for p in range(1,N))
        if runs>3: continue
        m=0
        for eid,(_,_,i,j) in enumerate(edges):
            p,q=mapped_pair(i,j)
            if seq[p-1] != seq[q-1]:
                m |= 1<<eid
        masks.add(m)
    return masks


def brute_max_masks(n,edges,forbidden):
    m=len(edges)
    target=((n+1)*(n+1))//4
    fms=[sum(1<<e for e in t) for t in forbidden]
    # Show no set of target+1 is feasible, and collect all target sets.
    if target+1 <= m:
        for C in combinations(range(m),target+1):
            mask=sum(1<<e for e in C)
            assert not is_egp_mask(mask,fms), (n,'oversize',C)
    got=set()
    for C in combinations(range(m),target):
        mask=sum(1<<e for e in C)
        if is_egp_mask(mask,fms):
            got.add(mask)
    return got


print('VERIFY_OK')
subset_checks=0
triple_checks=0
for n in range(2,7):
    actual,edges=actual_geodesic_triples(n)
    formula=formula_geodesic_triples(n,edges)
    assert actual==formula,(n,len(actual),len(formula),actual^formula)
    triple_checks += len(list(combinations(range(len(edges)),3)))

    got=brute_max_masks(n,edges,actual)
    exp=predicted_max_masks(n,edges)
    target=((n+1)*(n+1))//4
    pred_count=(n+1 if n%2==0 else (n+1)//2)
    assert got==exp,(n,len(got),len(exp),got^exp)
    assert len(got)==pred_count,(n,len(got),pred_count)
    subset_checks += len(list(combinations(range(len(edges)),target)))
    if target+1<=len(edges):
        subset_checks += len(list(combinations(range(len(edges)),target+1)))
    print(f'n={n}: gp_e={target}, maximum_sets={len(got)}, geodesic_triples={len(actual)}')

# Construction-and-count verification at larger orders without exhaustive subset search.
for n in range(7,21):
    actual,edges=actual_geodesic_triples(n)
    exp=predicted_max_masks(n,edges)
    target=((n+1)*(n+1))//4
    pred_count=(n+1 if n%2==0 else (n+1)//2)
    fms=[sum(1<<e for e in t) for t in actual]
    assert len(exp)==pred_count
    assert all(mask.bit_count()==target and is_egp_mask(mask,fms) for mask in exp)

print('definition_level_triple_comparisons =',triple_checks)
print('near_extremal_subsets_checked =',subset_checks)
print('classification_exhaustive_through_n = 6')
print('predicted_maximum_constructions_checked_through_n = 20')
