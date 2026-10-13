#!/usr/bin/env python3
from math import comb, ceil, factorial

def base_graph(n):
    # vertices 0..n-1 are a_i, n..2n-1 are b_i
    edges=[]
    for i in range(n):
        for j in range(n):
            if i!=j:
                edges.append((i,n+j))
    return edges

def dominates_pair(n, edges, pair):
    adj=[set([v]) for v in range(2*n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    covered=adj[pair[0]]|adj[pair[1]]
    return len(covered)==2*n

def direct_kill_masks(n, edges):
    pos={tuple(sorted(e)):k for k,e in enumerate(edges)}
    dom=[]
    for u in range(2*n):
        for v in range(u+1,2*n):
            if not dominates_pair(n,edges,(u,v)):
                continue
            kill=0
            P={u,v}
            for w in range(2*n):
                if w in P: continue
                incident=[]
                for p in P:
                    e=tuple(sorted((w,p)))
                    if e in pos: incident.append(pos[e])
                # A base dominating pair must reach w. In these crowns there is
                # exactly one such edge, but use the graph-derived list.
                if len(incident)!=1:
                    raise AssertionError((n,(u,v),w,incident))
                kill |= 1<<incident[0]
            dom.append(((u,v),kill))
    return dom

def formula_coeffs(n):
    m=n*(n-1)
    out=[0]*(m+1)
    for j in range(n+1):
        e=(n-j)*(n-j-1)
        s=(-1)**j*comb(n,j)
        for k in range(e+1):
            out[k]+=s*comb(e,k)
    return out

def odd_df(k):
    z=1
    while k>0:
        z*=k; k-=2
    return z

def expected_min_count(n):
    if n%2==0:
        return (2**(n//2))*odd_df(n-1)
    return (2**((n+1)//2))*(n*(n-1)//2)*odd_df(n-2)

subset_checks=0
pair_checks=0
coefficient_checks=0
for n in range(3,6):
    edges=base_graph(n)
    m=len(edges)
    dom=direct_kill_masks(n,edges)
    assert len(dom)==n
    # The graph-derived minimum dominating pairs are exactly the deleted-matching pairs.
    got={p for p,_ in dom}
    want={(i,n+i) for i in range(n)}
    assert got==want
    endpoint=[0]*m
    for e,(u,v) in enumerate(edges):
        endpoint[e]=(1<<u)|(1<<(v-n))
    coeff=[0]*(m+1)
    cover=[0]*(1<<m)
    allidx=(1<<n)-1
    for mask in range(1<<m):
        if mask:
            lsb=mask & -mask
            e=lsb.bit_length()-1
            cover[mask]=cover[mask^lsb] | endpoint[e]
        aux_disrupt=(cover[mask]==allidx)
        direct_disrupt=True
        for _,kill in dom:
            pair_checks+=1
            if mask & kill == 0:
                direct_disrupt=False
                break
        assert aux_disrupt==direct_disrupt
        subset_checks+=1
        if direct_disrupt:
            coeff[mask.bit_count()]+=1
    f=formula_coeffs(n)
    assert coeff==f
    coefficient_checks+=len(f)
    k0=next(k for k,c in enumerate(coeff) if c)
    assert k0==ceil(n/2)
    assert coeff[k0]==expected_min_count(n)

# Algebraic coefficient and minimum-count checks beyond exhaustive subset range.
for n in range(6,13):
    f=formula_coeffs(n)
    k0=next(k for k,c in enumerate(f) if c)
    assert k0==ceil(n/2)
    assert f[k0]==expected_min_count(n)
    coefficient_checks+=len(f)

print(f"VERIFY_OK n_exhaustive=3..5 subset_checks={subset_checks} pair_survival_checks={pair_checks} coefficient_checks={coefficient_checks} formula_range=3..12")
