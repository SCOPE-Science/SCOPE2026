#!/usr/bin/env python3
"""Signed Lefschetz cross-checks for small uniform clique bouquets.

The direct signed simplex enumeration is independent from exterior-algebra
character calculations for the two predicted integral homology lattices.
"""
from itertools import combinations
from math import comb


def sign_on_subset(perm, S):
    a=[perm[i] for i in S]
    inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return -1 if inv%2 else 1


def exterior_trace_from_permutation(perm, degree, domain):
    seen=set()
    poly=[1]
    for start in domain:
        if start in seen: continue
        x=start; length=0
        while x not in seen:
            seen.add(x); length+=1; x=perm[x]
        new=[0]*(len(poly)+length)
        for i,c in enumerate(poly):
            new[i]+=c
            new[i+length]+=c*(-1 if length%2==0 else 1)
        poly=new
    # divide det(I+t P) by 1+t; coefficientwise exact
    coeff=[]
    for i in range(degree+1):
        coeff.append((poly[i] if i<len(poly) else 0)-(coeff[-1] if coeff else 0))
    return coeff[degree]


def verify(r,m):
    n=2; N=2*m
    assert m==r+1
    blocks=[list(range(1,m+1)),list(range(m+1,2*m+1))]
    faces=[]
    for size in range(1,N+2):
        for S in combinations(range(N+1),size):
            if 0 in S:
                ok=len(S)-1<=r-1
            else:
                ok=all(len(set(S).intersection(B))<=r for B in blocks)
            if ok:faces.append(S)
    gens={
      'identity':list(range(N+1)),
      'first_block_transposition':[0,2,1]+list(range(3,N+1)),
      'swap_equal_blocks':[0]+list(range(m+1,2*m+1))+list(range(1,m+1)),
    }
    for name,perm in gens.items():
        lef=-1
        for S in faces:
            if set(perm[v] for v in S)==set(S):
                lef+=(-1 if (len(S)-1)%2 else 1)*sign_on_subset(perm,S)
        low=exterior_trace_from_permutation(perm,r-1,list(range(1,N+1)))
        high=1
        if name=='first_block_transposition': high=-1
        if name=='swap_equal_blocks': high=(-1)**r
        pred=((-1)**(r-1))*low+((-1)**(2*r-1))*high
        assert lef==pred,(r,m,name,lef,pred,low,high)
        print('r=',r,'m=',m,'element=',name,'direct_reduced_lefschetz=',lef,'exterior_wedge_prediction=',pred,'PASS')

if __name__=='__main__':
    verify(3,4)
    verify(4,5)
    print('ALL SIX EQUIVARIANT TESTS PASSED')
