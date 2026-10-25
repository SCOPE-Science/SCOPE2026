#!/usr/bin/env python3
"""Independent finite checks for a Mycielskian zero-forcing classification.
Run: python3 verify_mycielski_zero_forcing.py
Requires only the Python 3 standard library.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def graph(n):
    # Original vertices a_i (0..n-1), clones b_i (n..2n-1), apex w (2n).
    adj = [set() for _ in range(2*n+1)]
    def edge(u,v):
        adj[u].add(v)
        adj[v].add(u)
    for i in range(n):
        for j in range(i+1,n):
            edge(i,j)
        for j in range(n):
            if j != i:
                edge(i,n+j)
        edge(n+i,2*n)
    return adj


def forces(adj, blue):
    blue=set(blue)
    while True:
        nxt=set()
        for v in blue:
            white=adj[v]-blue
            if len(white)==1:
                nxt.update(white)
        if not nxt-blue:
            return len(blue)==len(adj)
        blue |= nxt


def force_alternate(adj, mask):
    # Chronological single-force procedure, independently using bitmasks.
    N=len(adj)
    masks=[sum(1<<j for j in adj[i]) for i in range(N)]
    while True:
        newmask=mask
        for i in range(N):
            if mask & (1<<i):
                rem=masks[i]&~mask
                if rem and not(rem&(rem-1)):
                    newmask|=rem
                    break
        if newmask==mask:
            return mask==(1<<N)-1
        mask=newmask


def is_fort(adj, W):
    return bool(W) and all(len(adj[v]&W)!=1 for v in range(len(adj)) if v not in W)


def listed_forts(n):
    F=[]
    for i,j,k in combinations(range(n),3):
        F.extend([{i,j,k},{n+i,n+j,n+k}])
    for i,j in combinations(range(n),2):
        F.extend([{i,j,2*n},{i,j,n+i,n+j}])
    for i in range(n):
        F.append({i,n+i,2*n})
    return set(frozenset(s) for s in F)


def predicted_white(n,W):
    A={i for i in range(n) if i in W}
    B={i for i in range(n) if n+i in W}
    if 2*n in W:
        return len(A)<=1 and len(B)<=2 and not(A&B)
    return len(A)<=2 and len(B)<=2 and not(len(A)==len(B)==2 and A==B)


def predicted_coeff(n):
    return {0:1,1:2*n+1,2:comb(2*n+1,2),
            3:n*(n-1)*(2*n+3)//2,
            4:n*(n-1)*(n-2)*(n+3)//4}


def expected_stats(n):
    N0=n*(n-1)*(n-2)*(n-3)//4
    N1=n*(n-1)*(n-2)
    N2=n*(n-1)*(n-2)//2
    return {(0,False):(N0,4*n-6),(1,False):(N1,4*n-9),
            (-1,True):(N2,4*n-10)}


def check(n):
    adj=graph(n); N=2*n+1
    coeff=Counter(); opts=[]; all_mask=(1<<N)-1
    for mask in range(1<<N):
        W={i for i in range(N) if mask>>i&1}
        predicted=predicted_white(n,W)
        actual=forces(adj,set(range(N))-W)
        assert actual==predicted,(n,mask,W,'characterization')
        if n<=6:
            assert actual==force_alternate(adj,all_mask^mask),(n,mask,'alternate')
        if actual:
            coeff[len(W)]+=1
            if len(W)==4:opts.append(mask)
    assert dict(coeff)==predicted_coeff(n),(n,coeff,predicted_coeff(n))

    # Enumerate all actual forts and retain precisely those inclusion minimal.
    if n<=7:
        forts=[]
        for k in range(1,N+1):
            for tup in combinations(range(N),k):
                W=frozenset(tup)
                if any(f<=W for f in forts):
                    continue
                if is_fort(adj,set(W)):
                    forts.append(W)
        assert set(forts)==listed_forts(n),(n,'fort classification',len(forts))
    O={mask:i for i,mask in enumerate(opts)}
    nbr=[set() for _ in opts]
    for i,mask in enumerate(opts):
        for a in range(N):
            if not (mask>>a&1):continue
            for b in range(N):
                if mask>>b&1:continue
                j=O.get(mask^(1<<a)^(1<<b))
                if j is not None:
                    nbr[i].add(j)
    strata=Counter()
    for idx,mask in enumerate(opts):
        A={i for i in range(n) if mask>>i&1}
        B={i for i in range(n) if mask>>(n+i)&1}
        apex=bool(mask>>(2*n)&1)
        typ=(-1,True) if apex else (len(A&B),False)
        assert typ in expected_stats(n)
        assert len(nbr[idx])==expected_stats(n)[typ][1]
        strata[typ]+=1
    assert all(strata[t]==v[0] for t,v in expected_stats(n).items())
    vis={0};todo=deque([0])
    while todo:
        u=todo.popleft()
        for v in nbr[u]:
            if v not in vis:
                vis.add(v);todo.append(v)
    assert len(vis)==len(opts)
    E=sum(map(len,nbr))//2
    assert E==n*(n-1)*(n-2)*(2*n*n+3*n-19)//4
    print(f'n={n} white_coefficients={dict(sorted(coeff.items()))} minimum_sets={len(opts)} exchange_edges={E} connected=YES CHECK_OK')

if __name__=='__main__':
    for n in range(4,9):
        check(n)
    print('ALL_VERIFY_OK')
