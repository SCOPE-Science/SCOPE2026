#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import comb


def adjacency(n):
    adj=[set() for _ in range(2*n)]
    for base in (0,n):
        for i in range(n):
            for j in range(i+1,n):
                u=base+i; v=base+j
                adj[u].add(v); adj[v].add(u)
    adj[n-1].add(2*n-1); adj[2*n-1].add(n-1)
    return adj


def is_isolate_dominating(n,S):
    adj=adjacency(n); S=set(S)
    if not S:
        return False
    for v in range(2*n):
        if v not in S and not (adj[v] & S):
            return False
    return any(not (adj[v] & S) for v in S)


def is_minimal_isolate_dominating(n,S):
    S=set(S)
    return is_isolate_dominating(n,S) and all(
        not is_isolate_dominating(n,S-{v}) for v in S
    )


def predicted_bivariate(n):
    # F = Bx By - Ax Ay - xy[(1+x)^(n-1)+(1+y)^(n-1)-1]
    out=Counter()
    # Bx By: nonempty choices on both sides.
    for a in range(1,n+1):
        for b in range(1,n+1):
            out[a,b]+=comb(n,a)*comb(n,b)
    # Ax Ay: choices of size at least two on both sides.
    for a in range(2,n+1):
        for b in range(2,n+1):
            out[a,b]-=comb(n,a)*comb(n,b)
    # xy(1+x)^(n-1)
    for a_extra in range(0,n):
        out[a_extra+1,1]-=comb(n-1,a_extra)
    # xy(1+y)^(n-1)
    for b_extra in range(0,n):
        out[1,b_extra+1]-=comb(n-1,b_extra)
    # The bracket has -1, hence the whole subtraction contributes +xy.
    out[1,1]+=1
    return +out


def predicted_univariate(n):
    out=Counter()
    # 2 n z ((1+z)^n-1)
    for k in range(1,n+1):
        out[k+1]+=2*n*comb(n,k)
    # -2 z^2 (1+z)^(n-1)
    for k in range(0,n):
        out[k+2]-=2*comb(n-1,k)
    # -(n^2-1)z^2
    out[2]-=n*n-1
    return +out

subset_checks=0
isolate_sets=0
minimal_sets=0
bivariate_checks=0
univariate_checks=0
for n in range(2,8):
    actual_bi=Counter(); actual_uni=Counter(); actual_min=[]
    for mask in range(1<<(2*n)):
        subset_checks+=1
        S={v for v in range(2*n) if (mask>>v)&1}
        if is_isolate_dominating(n,S):
            isolate_sets+=1
            a=sum(v<n for v in S); b=len(S)-a
            actual_bi[a,b]+=1
            actual_uni[len(S)]+=1
        if is_minimal_isolate_dominating(n,S):
            minimal_sets+=1
            actual_min.append(S)
    pb=predicted_bivariate(n)
    pu=predicted_univariate(n)
    assert actual_bi==pb, (n,actual_bi,pb)
    assert actual_uni==pu, (n,actual_uni,pu)
    bivariate_checks+=len(set(actual_bi)|set(pb))
    univariate_checks+=len(set(actual_uni)|set(pu))
    assert len(actual_min)==n*n-1, (n,len(actual_min),n*n-1)
    for S in actual_min:
        assert len(S)==2
        assert sum(v<n for v in S)==1
        assert not ({n-1,2*n-1} <= S)
    total=sum(actual_uni.values())
    expected_total=(2*n-1)*(2**n)-n*n-2*n+1
    assert total==expected_total, (n,total,expected_total)

print(
    'VERIFY_OK '
    f'n_range=2..7 subset_checks={subset_checks} isolate_sets={isolate_sets} '
    f'minimal_sets={minimal_sets} bivariate_checks={bivariate_checks} '
    f'univariate_checks={univariate_checks} max_order=14'
)
