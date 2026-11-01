#!/usr/bin/env python3
"""Standalone exact checker for uniform labelled unicyclic graph Fourier sampling."""
from itertools import combinations
from math import factorial
from fractions import Fraction


def spectrum_formula(n):
    a = Fraction(n**(n-3),factorial(n-3))
    z = a / sum((Fraction(n**j,factorial(j)) for j in range(n-2)), Fraction(0))
    p = Fraction(2,n-1)
    q1 = Fraction(3,1)*(n-z)/(n*(n-1)*(n-2))
    q2 = 4*(n*(n-4)+3*z)/(n*(n-1)*(n-2)*(n-3))
    l1 = (n-3*z)/((n-1)*(n-2))
    l2 = 2*(n*(n*n-6*n+7)+3*(n-1)*z)/(n*(n-1)*(n-2)*(n-3))
    return p,q1,q2,l1,l2,z

def brute(n):
    ed=list(combinations(range(n),2)); E=len(ed)
    count=0
    freq1=[0]*E
    pair=[[0]*E for _ in range(E)]
    for inds in combinations(range(E),n):
        parents=list(range(n))
        def root(a):
            while a!=parents[a]:
                a=parents[a]
            return a
        for i in inds:
            u,v=ed[i]
            a,b=root(u),root(v)
            if a!=b: parents[a]=b
        if len({root(i) for i in range(n)})!=1: continue
        count+=1
        for i in inds:
            freq1[i]+=1
            for j in inds:
                pair[i][j]+=1
    p,q1,q2,l1,l2,z=spectrum_formula(n)
    assert count == factorial(n-1)*sum(Fraction(n**j,factorial(j)) for j in range(n-2))/2
    for i in range(E):
        assert Fraction(freq1[i],count)==p,(n,i)
        for j in range(E):
            exp=p if i==j else q1 if len(set(ed[i])&set(ed[j]))==1 else q2
            assert Fraction(pair[i][j],count)==exp,('pair failure',n,i,j,exp,Fraction(pair[i][j],count))
    # Directly verify explicit eigenvectors in row and cycle Johnson spaces
    C=[[Fraction(pair[i][j],count)-p*p for j in range(E)] for i in range(E)]
    vectors=[]
    # standard vertex-star vector: (1_{i in edge}-1_{j in edge})
    vectors.append(([int(0 in e)-int(1 in e) for e in ed], l1))
    # four-edge disjoint cycle: (01,23) - (02,13)
    vectors.append(([int(set(e)=={0,1})+int(set(e)=={2,3})-int(set(e)=={0,2})-int(set(e)=={1,3}) for e in ed],l2))
    for v,lam in vectors:
        assert any(v)
        for i in range(E):
            assert sum(C[i][j]*v[j] for j in range(E)) ==lam*v[i],('eig fail',n,i,lam)
    return n,count,z,l1,l2

if __name__=='__main__':
    for n in range(4,8): print('EXACT_PASS',*brute(n),flush=True)
