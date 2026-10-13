#!/usr/bin/env python3
from itertools import product
from math import factorial


def stirling2(n,k):
    if k < 0 or k > n:
        return 0
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for a in range(1,n+1):
        for b in range(1,min(a,k)+1):
            dp[a][b] = dp[a-1][b-1] + b*dp[a-1][b]
    return dp[n][k]


def tau_formula(ns,k):
    N=sum(ns); L=max(ns); r=len(ns)
    if k > N-L:
        return None
    for t in range(1,N-k+1):
        S=sum(min(n,t) for n in ns)
        if r <= k+t <= S:
            return t
    raise AssertionError((ns,k,'feasible but no tau'))


def predicted_q(ns,k):
    t=tau_formula(ns,k)
    return None if t is None else k+t


def vector_minimum(ns,k):
    best=None; vecs=[]
    for cs in product(*[range(1,n+1) for n in ns]):
        q=sum(cs)
        if all(q-c >= k for c in cs):
            if best is None or q < best:
                best=q; vecs=[cs]
            elif q == best:
                vecs.append(cs)
    return best,vecs


def predicted_labeled_count(ns,k):
    t=tau_formula(ns,k)
    if t is None:
        return 0,None
    q=k+t
    total=0
    for cs in product(*[range(1,min(n,t)+1) for n in ns]):
        if sum(cs)==q:
            p=1
            for n,c in zip(ns,cs):
                p*=stirling2(n,c)
            total+=p
    return factorial(q)*total,q


def is_coloring(ns,k,assignment,q):
    if set(assignment) != set(range(q)):
        return False
    part_colors=[]; pos=0
    for n in ns:
        C=set(assignment[pos:pos+n]); pos+=n
        part_colors.append(C)
    for i in range(len(ns)):
        for j in range(i):
            if part_colors[i] & part_colors[j]:
                return False
    allc=set(range(q))
    return all(len(allc-part_colors[i]) >= k for i in range(len(ns)))


def compositions(total,r,prefix=()):
    if r==1:
        yield prefix+(total,)
    else:
        for x in range(1,total-r+2):
            yield from compositions(total-x,r-1,prefix+(x,))

vector_cases=0
for r in range(2,5):
    for ns in product(range(1,6), repeat=r):
        N=sum(ns)
        for k in range(1,N+2):
            brute,_=vector_minimum(ns,k)
            pred=predicted_q(ns,k)
            assert brute==pred,(ns,k,brute,pred)
            vector_cases+=1

assignment_cases=0
assignment_checks=0
count_checks=0
for N in range(2,7):
    for r in range(2,min(4,N)+1):
        for ns in compositions(N,r):
            L=max(ns)
            for k in range(1,N-L+1):
                expected,q=predicted_labeled_count(ns,k)
                actual=0
                for a in product(range(q), repeat=N):
                    assignment_checks+=1
                    if is_coloring(ns,k,a,q):
                        actual+=1
                assert actual==expected,(ns,k,q,actual,expected)
                if q>1:
                    any_smaller=False
                    for a in product(range(q-1), repeat=N):
                        assignment_checks+=1
                        if is_coloring(ns,k,a,q-1):
                            any_smaller=True; break
                    assert not any_smaller,(ns,k,q)
                assignment_cases+=1
                count_checks+=1

# Complete-bipartite corollary across a broad exact parameter grid.
bipartite_cases=0
for m in range(1,51):
    for n in range(m,51):
        for k in range(1,m+1):
            assert predicted_q((m,n),k)==2*k,(m,n,k,predicted_q((m,n),k))
            bipartite_cases+=1

print('ALL CHECKS PASSED; vector_cases=%d; assignment_cases=%d; assignment_checks=%d; labeled_count_checks=%d; bipartite_cases=%d; small_total_order<=6; vector_part_sizes<=5; bipartite_range=1<=m<=n<=50' % (vector_cases,assignment_cases,assignment_checks,count_checks,bipartite_cases))
