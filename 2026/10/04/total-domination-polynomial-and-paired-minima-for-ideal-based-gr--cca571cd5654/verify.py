#!/usr/bin/env python3
from itertools import combinations
from math import comb

def graph_Zpn(p,n,k):
    # R=Z/(p^n), I=(p^k), so R/I ~= Z/(p^k), |I|=p^(n-k).
    mod=p**n
    Ik=p**k
    V=[x for x in range(mod) if x%Ik!=0 and x%p==0]
    idx={x:i for i,x in enumerate(V)}
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if (x*y)%Ik==0:
                N[i].add(j); N[j].add(i)
    return V,N

def is_total(C,N):
    S=set(C)
    return all(N[v] & S for v in range(len(N)))

def perfect_matching(C,N):
    S=frozenset(C)
    memo={}
    def rec(T):
        if not T: return True
        if len(T)%2: return False
        if T in memo: return memo[T]
        v=next(iter(T)); R=T-{v}
        for u in R:
            if u in N[v] and rec(R-{u}):
                memo[T]=True; return True
        memo[T]=False; return False
    return rec(S)

def paired(C,N):
    S=set(C)
    if not perfect_matching(C,N): return False
    return all(v in S or N[v]&S for v in range(len(N)))

def polynomial_counts(N, pred):
    out=[]
    for j in range(N+1):
        c=0
        for C in combinations(range(N),j):
            if pred(C): c+=1
        out.append(c)
    return out

def check(p,n,k):
    V,Nb=graph_Zpn(p,n,k)
    s=p**(n-k); q=p
    N=s*(q**(k-1)-1)
    m=s*(q-1)
    assert len(V)==N
    # universal lifts are precisely elements of quotient valuation k-1
    U={i for i,x in enumerate(V) if x%(p**(k-1))==0}
    assert len(U)==m
    for u in U:
        assert len(Nb[u])==N-1
    if k>=3:
        w=next(i for i,x in enumerate(V) if x%p==0 and x%(p*p)!=0)
        assert Nb[w]==U
    expected=[0]*(N+1)
    for j in range(2,N+1):
        expected[j]=comb(N,j)-comb(N-m,j) if N-m>=j else comb(N,j)
    got=polynomial_counts(N, lambda C:is_total(C,Nb))
    assert got==expected, (p,n,k,got,expected)
    if N>=2:
        paired2=sum(1 for C in combinations(range(N),2) if paired(C,Nb))
        expected2=m*(N-m)+comb(m,2)
        assert paired2==expected2
        assert expected[2]==expected2
    else:
        assert not any(is_total(C,Nb) for j in range(N+1) for C in combinations(range(N),j))
    print(f'p={p} n={n} k={k} vertices={N} universal={m} total_coeffs={got} paired_min_pairs={got[2] if N>=2 else 0}')

# Direct ring-table examples spanning the isolated boundary, complete-graph case,
# and noncomplete chain quotients with nontrivial ideal fibres.
for params in [(2,2,2),(2,3,2),(3,2,2),(2,3,3),(3,3,3),(2,4,3),(2,5,4)]:
    check(*params)
print('VERIFY_OK')
