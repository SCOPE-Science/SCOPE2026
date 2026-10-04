#!/usr/bin/env python3
from itertools import combinations, product

def span(vs,p,n):
    S={(0,)*n}
    for v in vs:
        T=set()
        for a in range(p):
            av=tuple((a*x)%p for x in v)
            for s in S:
                T.add(tuple((s[i]+av[i])%p for i in range(n)))
        S=T
    return frozenset(S)

def subspaces(p,n):
    vecs=[v for v in product(range(p),repeat=n) if any(v)]
    out={frozenset({(0,)*n})}
    for k in range(1,n):
        for C in combinations(vecs,k):
            S=span(C,p,n)
            if 1<len(S)<p**n:
                out.add(S)
    out.add(frozenset(product(range(p),repeat=n)))
    return out

def graph(p,n):
    z=frozenset({(0,)*n})
    whole=frozenset(product(range(p),repeat=n))
    V=[S for S in subspaces(p,n) if S not in (z,whole)]
    N=[set() for _ in V]
    for i,A in enumerate(V):
        for j in range(i+1,len(V)):
            if len(A & V[j])>1:
                N[i].add(j);N[j].add(i)
    return V,N

def is_total(C,N):
    D=set(C)
    return all(bool(N[v]&D) for v in range(len(N)))

def min_total(V,N,max_k):
    for k in range(1,max_k+1):
        ans=[C for C in combinations(range(len(V)),k) if is_total(C,N)]
        if ans:
            return k,ans
    raise AssertionError("no total dominating set found")

def dim(S,p):
    d=0; x=len(S)
    while x>1:
        assert x%p==0
        x//=p; d+=1
    return d

def inter_family(F):
    I=set(F[0])
    for S in F[1:]:
        I &= set(S)
    return frozenset(I)

def perfect_matching(C,N):
    C=frozenset(C)
    memo={}
    def rec(S):
        if not S:return True
        if len(S)%2:return False
        if S in memo:return memo[S]
        v=next(iter(S))
        for u in S-{v}:
            if u in N[v] and rec(S-{v,u}):
                memo[S]=True
                return True
        memo[S]=False
        return False
    return rec(C)

def is_paired(C,N):
    D=set(C)
    dominating=all(v in D or bool(N[v]&D) for v in range(len(N)))
    return dominating and perfect_matching(C,N)

def min_paired(V,N,max_k):
    for k in range(2,max_k+1,2):
        ans=[C for C in combinations(range(len(V)),k) if is_paired(C,N)]
        if ans:return k,ans
    raise AssertionError("no paired dominating set found")

for p,n in [(2,3),(3,3),(2,4)]:
    V,N=graph(p,n)
    kt,Ts=min_total(V,N,p+1)
    expected=p+1
    gauss=((p**n-1)*(p**(n-1)-1))//((p**2-1)*(p-1))
    assert kt==expected
    assert len(Ts)==gauss
    for C in Ts:
        F=[V[i] for i in C]
        assert all(dim(S,p)==n-1 for S in F)
        assert dim(inter_family(F),p)==n-2
    print(f"F_{p}^{n}: |V(G)|={len(V)}, gamma_t={kt}, min_total_sets={len(Ts)}")

for p,n in [(2,3),(3,3)]:
    V,N=graph(p,n)
    kp,Ps=min_paired(V,N,p+2)
    expected=(p+1 if p%2 else p+2)
    assert kp==expected
    if p%2:
        gauss=((p**n-1)*(p**(n-1)-1))//((p**2-1)*(p-1))
        assert len(Ps)==gauss
    print(f"F_{p}^{n}: gamma_pr={kp}, min_paired_sets={len(Ps)}")

print("VERIFY_OK")
