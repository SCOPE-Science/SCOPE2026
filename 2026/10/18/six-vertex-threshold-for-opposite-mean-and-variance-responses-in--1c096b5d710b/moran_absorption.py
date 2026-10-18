"""Exact first/second absorption-time moments for the neutral birth-death Moran process.
No nonstandard packages required. Run: python moran_absorption.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from functools import lru_cache


def pairs(n):
    return tuple(combinations(range(n), 2))


def connected(n, mask):
    adj=[0]*n
    for k,(u,v) in enumerate(pairs(n)):
        if mask >> k & 1:
            adj[u]|=1<<v;adj[v]|=1<<u
    seen=1
    while True:
        nxt=seen
        for u in range(n):
            if seen>>u&1:nxt |= adj[u]
        if nxt==seen: return seen==(1<<n)-1
        seen=nxt


def edge_mask(n,edges):
    inds={e:k for k,e in enumerate(pairs(n))}
    return sum(1<<inds[tuple(sorted(e))] for e in edges)


@lru_cache(None)
def reindex_maps(n):
    ed=pairs(n);idx={e:i for i,e in enumerate(ed)}
    return tuple(tuple(idx[tuple(sorted((perm[u],perm[v])))] for u,v in ed) for perm in permutations(range(n)))


@lru_cache(None)
def canonical(n,mask):
    active=[i for i in range(len(pairs(n))) if mask>>i&1]
    return min(sum(1<<m[i] for i in active) for m in reindex_maps(n))


def linear_solve(M,b):
    n=len(M)
    a=[row[:] + [bb] for row,bb in zip(M,b)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        if k!=j:a[k],a[j]=a[j],a[k]
        pivot=a[j][j]
        for t in range(j,n+1):a[j][t]/=pivot
        for k in range(j+1,n):
            scale=a[k][j]
            if scale:
                for t in range(j,n+1):a[k][t]-=scale*a[j][t]
    x=[F(0) for _ in range(n)]
    for j in range(n-1,-1,-1):
        x[j]=a[j][n]-sum(a[j][i]*x[i] for i in range(j+1,n))
    return x


@lru_cache(None)
def stats(n,mask):
    ed=[e for i,e in enumerate(pairs(n)) if mask>>i&1]
    deg=[0]*n;nbr=[[] for _ in range(n)]
    for u,v in ed:
        deg[u]+=1;deg[v]+=1;nbr[u].append(v);nbr[v].append(u)
    assert all(deg) and connected(n,mask)
    states=(1<<n)-2
    A=[[F(0) for _ in range(states)] for _ in range(states)]
    for state in range(1,states+1):
        for u in range(n):
            for v in nbr[u]:
                target=(state|(1<<v)) if (state>>u)&1 else (state&~(1<<v))
                if target==state:continue
                p=F(1,n*deg[u])
                A[state-1][state-1]+=p
                if 0<target<states+1:A[state-1][target-1]-=p
    x=linear_solve(A,[F(1) for _ in range(states)])
    y=linear_solve(A,[2*val-1 for val in x])
    mean=sum(x[(1<<v)-1] for v in range(n))/n
    second=sum(y[(1<<v)-1] for v in range(n))/n
    return mean,second-mean**2,second


def check_small():
    for n in range(2,6):
        total=0; canonical_pairs=set(); disag=0
        for mask in range(1<<len(pairs(n))):
            if not connected(n,mask):continue
            first=canonical(n,mask)
            v=stats(n,first)
            for i in range(len(pairs(n))):
                if mask>>i&1:continue
                other=canonical(n,mask|(1<<i))
                w=stats(n,other)
                da=w[0]-v[0];dv=w[1]-v[1]
                total+=1
                canonical_pairs.add((first,other))
                if da*dv<0:disag+=1
        print('n',n,'labeled comparisons',total,'canonical pairs',len(canonical_pairs),'discordant',disag,flush=True)
        assert disag==0,(n,disag)


def check_witnesses():
    graphs=[
      ([(0,1),(1,2),(1,4),(1,5),(2,3),(2,4),(2,5)],(4,5),'mean_down_variance_up'),
      ([(0,1),(0,5),(2,3),(3,4),(4,5)],(0,4),'mean_up_variance_down'),
    ]
    for edges,extra,direction in graphs:
        m=edge_mask(6,edges); h=m|edge_mask(6,[extra])
        before=stats(6,m);after=stats(6,h)
        delta_mean=after[0]-before[0];delta_var=after[1]-before[1]
        print(direction,'before',before,'after',after,flush=True)
        print('differences',delta_mean,delta_var,flush=True)
        if direction=='mean_down_variance_up':assert delta_mean<0<delta_var
        else:assert delta_var<0<delta_mean


if __name__=='__main__':
    check_small();check_witnesses()
