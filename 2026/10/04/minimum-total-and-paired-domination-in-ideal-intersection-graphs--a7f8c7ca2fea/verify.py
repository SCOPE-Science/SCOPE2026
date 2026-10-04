#!/usr/bin/env python3
from itertools import product, combinations
from math import prod, gcd


def valuation_graph(lengths):
    r=len(lengths)
    V=[a for a in product(*[range(L+1) for L in lengths])
       if a != tuple(0 for _ in lengths) and a != tuple(lengths)]
    supports=[frozenset(i for i,x in enumerate(a) if x<lengths[i]) for a in V]
    N=[set() for _ in V]
    for i,j in combinations(range(len(V)),2):
        if supports[i] & supports[j]:
            N[i].add(j); N[j].add(i)
    return V,supports,N


def is_total(D,N):
    D=set(D)
    return all(bool(N[v] & D) for v in range(len(N)))


def is_paired_pair(pair,N):
    i,j=pair
    return j in N[i] and is_total(pair,N)


def formula(lengths):
    r=len(lengths)
    L=prod(lengths)
    B=prod(x+1 for x in lengths)
    P=prod(x*(x+2) for x in lengths)
    num=P-(2**r+1)*L-2*B+4
    assert num%2==0
    return num//2


def predicted_exists(lengths):
    r=len(lengths)
    if r==1:
        return lengths[0]>=3
    if r==2 and lengths==(1,1):
        return False
    return True


def check_tuple(lengths):
    V,S,N=valuation_graph(lengths)
    pairs=[]
    for i,j in combinations(range(len(V)),2):
        if is_total((i,j),N):
            pairs.append((i,j))
            assert is_paired_pair((i,j),N)
            assert S[i] & S[j]
            assert S[i] | S[j] == frozenset(range(len(lengths)))
    # converse classification
    classified=[]
    for i,j in combinations(range(len(V)),2):
        if (S[i] & S[j]) and (S[i] | S[j] == frozenset(range(len(lengths)))):
            classified.append((i,j))
    assert pairs==classified
    assert len(pairs)==formula(lengths), (lengths,len(pairs),formula(lengths))
    assert bool(pairs)==predicted_exists(lengths), (lengths,len(pairs))
    # If a total set exists, size one is impossible in every simple graph and the pair proves gamma_t=gamma_pr=2.
    # In the three boundary forms, verify an isolated/empty obstruction directly.
    if not pairs:
        if len(V)==0:
            assert lengths==(1,)
        else:
            assert any(len(N[v])==0 for v in range(len(V)))
    return f"lengths={lengths} vertices={len(V)} min_pairs={len(pairs)} formula={formula(lengths)}"


def prime_factor_exponents(n):
    a=[]; d=2
    while d*d<=n:
        e=0
        while n%d==0:
            n//=d; e+=1
        if e: a.append(e)
        d+=1
    if n>1: a.append(1)
    return tuple(a)


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def check_Zn(n):
    # Nonzero proper ideals of Z/nZ are (d) with d|n and 1<d<n.
    V=[d for d in divisors(n) if 1<d<n]
    N=[set() for _ in V]
    for i,j in combinations(range(len(V)),2):
        l=V[i]*V[j]//gcd(V[i],V[j])
        if l<n:
            N[i].add(j);N[j].add(i)
    count=sum(1 for ij in combinations(range(len(V)),2) if is_total(ij,N))
    exps=prime_factor_exponents(n)
    assert count==formula(exps),(n,exps,count,formula(exps))
    return f"Z/{n}Z exponents={exps} vertices={len(V)} min_pairs={count}"

cases=[]
for L in range(1,8): cases.append((L,))
for a in range(1,5):
    for b in range(1,5): cases.append((a,b))
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,3): cases.append((a,b,c))
cases += [(1,1,1,1),(1,1,1,2),(1,1,2,2),(2,2,2,2)]
for Ls in cases:
    print(check_tuple(Ls))
for n in range(4,121):
    if len(divisors(n))>2:
        print(check_Zn(n))
print('VERIFY_OK')
