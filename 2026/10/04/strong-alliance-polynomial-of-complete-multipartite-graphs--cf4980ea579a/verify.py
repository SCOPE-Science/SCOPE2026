#!/usr/bin/env python3
from math import comb, ceil

MAX_ORDER = 9


def compositions(n, r, prefix=()):
    if r == 1:
        yield prefix + (n,)
        return
    for x in range(1, n-r+2):
        yield from compositions(n-x, r-1, prefix+(x,))


def vertices(parts):
    return [(i,j) for i,n in enumerate(parts) for j in range(n)]


def adjacent(u,v):
    return u[0] != v[0]


def connected_induced(S):
    if not S:
        return False
    if len(S)==1:
        return True
    todo=[next(iter(S))]
    seen=set(todo)
    while todo:
        u=todo.pop()
        for v in S:
            if v not in seen and adjacent(u,v):
                seen.add(v); todo.append(v)
    return len(seen)==len(S)


def literal_strong(parts, S):
    if not S:
        return False
    V=vertices(parts)
    Sset=set(S)
    for v in Sset:
        ds=sum(1 for u in Sset if u!=v and adjacent(u,v))
        dout=sum(1 for u in V if u not in Sset and adjacent(u,v))
        if ds < dout:
            return False
    return True


def criterion(parts, S):
    if not S:
        return False
    N=sum(parts); s=len(S)
    counts=[0]*len(parts)
    for i,_ in S: counts[i]+=1
    for i,si in enumerate(counts):
        if si:
            c=ceil((N-parts[i])/2)
            if s-si < c:
                return False
    return True


def tight_count(parts,S):
    N=sum(parts); s=len(S)
    counts=[0]*len(parts)
    for i,_ in S: counts[i]+=1
    z=0
    for i,si in enumerate(counts):
        if si and s-si == ceil((N-parts[i])/2):
            z+=1
    return z


def dp_capacity_poly(parts):
    N=sum(parts)
    coeff=[0]*(N+1)
    for s in range(1,N+1):
        dp=[0]*(s+1); dp[0]=1
        for i,ni in enumerate(parts):
            c=ceil((N-ni)/2)
            ui=min(ni,max(0,s-c))
            nd=[0]*(s+1)
            for a,ca in enumerate(dp):
                if ca:
                    for j in range(0,min(ui,s-a)+1):
                        nd[a+j]+=ca*comb(ni,j)
            dp=nd
        coeff[s]=dp[s]
    return coeff


def parity_min(parts):
    N=sum(parts)
    if N % 2:
        return (N+1)//2
    return N//2 if all(n%2==0 for n in parts) else N//2+1


def bipartite_formula(parts):
    n,m=parts
    lo_n=ceil(n/2); lo_m=ceil(m/2)
    N=n+m
    coeff=[0]*(N+1)
    for i in range(lo_n,n+1):
        for j in range(lo_m,m+1):
            coeff[i+j]+=comb(n,i)*comb(m,j)
    return coeff

profiles=subset_checks=criterion_checks=coefficient_checks=bipartite_checks=upset_checks=minimal_checks=density_checks=0
for N in range(2,MAX_ORDER+1):
    for r in range(2,N+1):
        for parts in compositions(N,r):
            profiles+=1
            V=vertices(parts)
            brute=[0]*(N+1)
            strong_sets=[]
            for mask in range(1,1<<N):
                S={V[k] for k in range(N) if mask>>k & 1}
                subset_checks+=1
                a=literal_strong(parts,S)
                b=criterion(parts,S)
                criterion_checks+=1
                if a!=b:
                    raise AssertionError(('criterion',parts,S,a,b))
                conn=connected_induced(S)
                if a and not conn:
                    raise AssertionError(('strong-not-connected',parts,S))
                if a:
                    strong_sets.append(S)
                    brute[len(S)]+=1
                    if len(S)*2 < N:
                        raise AssertionError(('half-bound',parts,S))
            strong_keys={frozenset(S) for S in strong_sets}
            for S in strong_sets:
                for v in V:
                    if v not in S:
                        upset_checks+=1
                        if frozenset(S|{v}) not in strong_keys:
                            raise AssertionError(('not-upset',parts,S,v))
                is_minimal=all(frozenset(S-{v}) not in strong_keys for v in S)
                pred=tight_count(parts,S)>=2
                minimal_checks+=1
                if is_minimal!=pred:
                    raise AssertionError(('minimal',parts,S,is_minimal,pred,tight_count(parts,S)))
            form=dp_capacity_poly(parts)
            for s in range(N+1):
                coefficient_checks+=1
                if brute[s]!=form[s]:
                    raise AssertionError(('coefficient',parts,s,brute[s],form[s]))
            brute_min=next((s for s in range(1,N+1) if brute[s]),None)
            pm=parity_min(parts)
            if brute_min!=pm:
                raise AssertionError(('minimum',parts,brute_min,pm))
            for s in range(1,N):
                density_checks+=1
                if brute[s]*(N-s) > brute[s+1]*(s+1):
                    raise AssertionError(('density',parts,s,brute[s],brute[s+1]))
            if r==2:
                bp=bipartite_formula(parts)
                bipartite_checks+=1
                if bp!=brute:
                    raise AssertionError(('bipartite',parts,bp,brute))
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} upset_checks={upset_checks} minimal_checks={minimal_checks} density_checks={density_checks} bipartite_checks={bipartite_checks} max_order={MAX_ORDER}')
