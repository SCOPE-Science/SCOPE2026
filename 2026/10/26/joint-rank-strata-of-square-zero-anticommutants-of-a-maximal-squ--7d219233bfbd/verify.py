#!/usr/bin/env python3
"""Reproducible finite-field tests for a square-zero anticommutation rank census."""
import itertools
from collections import Counter
from math import prod

def mats(n,q):
    for a in itertools.product(range(q), repeat=n*n):
        yield tuple(a)

def multiply(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def matrix_rank(a,n,q):
    m=[list(a[n*i:n*(i+1)]) for i in range(n)]
    h=0
    for col in range(n):
        pivot=next((i for i in range(h,n) if m[i][col]%q),None)
        if pivot is None: continue
        m[h],m[pivot]=m[pivot],m[h]
        inv=pow(m[h][col],-1,q)
        m[h]=[(x*inv)%q for x in m[h]]
        for i in range(h+1,n):
            a0=m[i][col]
            if a0: m[i]=[(x-a0*y)%q for x,y in zip(m[i],m[h])]
        h+=1
        if h==n: break
    return h

def gaussian(n,k,q):
    if k<0 or k>n: return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def gl(k,q):
    return prod(q**k-q**i for i in range(k))

def rank_matrices(n,u,q):
    return gaussian(n,u,q)*prod(q**n-q**i for i in range(u))

def predicted(r,q):
    d=Counter()
    for t in range(r//2+1):
        h=r-2*t
        c=(r-t)**2+t*t
        nP=gaussian(r,t,q)*gaussian(r-t,t,q)*gl(t,q)
        for u in range(h+1):
            d[(2*t+u,t)] += nP*q**(c-h*h)*rank_matrices(h,u,q)
    return d

def lift(P,Y,r,q):
    n=2*r
    B=[0]*(n*n)
    for i in range(r):
        for j in range(r):
            B[i*n+j]=P[i*r+j]
            B[i*n+(r+j)]=Y[i*r+j]
            B[(r+i)*n+(r+j)]=-P[i*r+j]%q
    return tuple(B)

def fixed_A(r):
    n=2*r
    A=[0]*(n*n)
    for i in range(r): A[i*n+r+i]=1
    return tuple(A)

def check(r,q):
    n=2*r
    A=fixed_A(r)
    zeros=(0,)*(r*r)
    observed=Counter()
    valid_P=[]
    for P in mats(r,q):
        if multiply(P,P,r,q)==zeros:
            valid_P.append(P)
    for P in valid_P:
        for Y in mats(r,q):
            if multiply(P,Y,r,q)!=multiply(Y,P,r,q): continue
            B=lift(P,Y,r,q)
            BB=multiply(B,B,n,q)
            assert BB==(0,)*(n*n)
            AB=multiply(A,B,n,q)
            BA=multiply(B,A,n,q)
            assert all((x+y)%q==0 for x,y in zip(AB,BA))
            observed[matrix_rank(B,n,q),matrix_rank(AB,n,q)]+=1
    wanted=predicted(r,q)
    assert observed==wanted,(r,q,observed,wanted)
    print('CHECK r=',r,'q=',q,'total=',sum(observed.values()),'squarezero P=',len(valid_P),'rank_pairs=',dict(sorted(observed.items())))

if __name__=='__main__':
    for r,q in [(1,2),(1,3),(2,2),(2,3),(2,5),(3,2)]: check(r,q)
    # Independent enumeration of every 4 by 4 binary matrix, not using the block parametrization.
    q=2; n=4; A=fixed_A(2); counted=Counter()
    for B in mats(n,q):
        if multiply(B,B,n,q)!=(0,)*(n*n): continue
        AB=multiply(A,B,n,q); BA=multiply(B,A,n,q)
        if any((x+y)%q for x,y in zip(AB,BA)): continue
        counted[(matrix_rank(B,n,q),matrix_rank(AB,n,q))]+=1
    assert counted==predicted(2,q)
    print('CHECK complete n=4 q=2 all 65536 matrices; valid=',sum(counted.values()))
    print('VERIFY_OK_MAX_RANK_EXTERIOR_PAIR_JOINT_RANK')
