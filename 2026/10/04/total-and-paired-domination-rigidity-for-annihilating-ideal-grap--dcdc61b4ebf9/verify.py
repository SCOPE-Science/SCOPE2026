#!/usr/bin/env python3
from itertools import combinations
def graph(r):
    verts=list(range(1,(1<<r)-1)); idx={v:i for i,v in enumerate(verts)}
    neigh=[]
    for a in verts:
        m=0
        for b in verts:
            if a!=b and (a&b)==0: m|=1<<idx[b]
        neigh.append(m)
    return verts,neigh
def total(D,N): return all(n&D for n in N)
def dom(D,N): return all(((D>>i)&1) or (N[i]&D) for i in range(len(N)))
def pm(C,N):
    C=frozenset(C); memo={}
    def f(T):
        if not T:return True
        if T in memo:return memo[T]
        v=next(iter(T)); R=T-{v}
        for u in R:
            if ((N[v]>>u)&1) and f(R-{u}): memo[T]=True; return True
        memo[T]=False; return False
    return f(C)
for r in range(2,6):
    V,N=graph(r); n=len(V); singles=[V.index(1<<i) for i in range(r)]
    SD=sum(1<<i for i in singles)
    for i in range(r):
        co=((1<<r)-1)^(1<<i); ci=V.index(co)
        assert [V[j] for j in range(n) if (N[ci]>>j)&1]==[1<<i]
    mins=[]
    for C in combinations(range(n),r):
        D=sum(1<<j for j in C)
        if total(D,N): mins.append(C)
    assert len(mins)==1 and set(mins[0])==set(singles)
    k=r if r%2==0 else r+1
    pmins=[]
    for C in combinations(range(n),k):
        D=sum(1<<j for j in C)
        if dom(D,N) and pm(C,N): pmins.append(C)
    exp=1 if r%2==0 else (1<<r)-r-2
    assert len(pmins)==exp
    if r%2==0:
        assert set(pmins[0])==set(singles)
    else:
        extras=set()
        for C in pmins:
            assert set(singles).issubset(C)
            e=set(C)-set(singles); assert len(e)==1
            mask=V[next(iter(e))]; assert mask&(mask-1); extras.add(mask)
        assert extras=={m for m in V if m&(m-1)}
    print(f"r={r} vertices={n} total_min_count={len(mins)} gamma_t={r} paired_min_count={len(pmins)} gamma_pr={k}")
print("VERIFY_OK")
