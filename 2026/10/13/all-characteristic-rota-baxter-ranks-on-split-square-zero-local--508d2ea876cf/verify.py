#!/usr/bin/env python3
"""Finite checks for rank counts of weight-zero Rota--Baxter maps on split square-zero local algebras.

Python 3, standard library. Exhaustive checks are finite corroboration, not proofs of the general theorem.
"""
import itertools
from collections import Counter
from math import prod


def rank(rows, p):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    n = len(a)
    m = len(a[0])
    rank_ = 0
    for j in range(m):
        pivot = next((i for i in range(rank_, n) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[rank_], a[pivot] = a[pivot], a[rank_]
        inv = pow(a[rank_][j] % p, -1, p)
        a[rank_] = [(v * inv) % p for v in a[rank_]]
        for i in range(n):
            if i == rank_:
                continue
            factor = a[i][j]
            if factor:
                a[i] = [(x - factor*y) % p for x, y in zip(a[i], a[rank_])]
        rank_ += 1
        if rank_ == n:
            break
    return rank_


def multiply(x, y, p):
    # Basis is (1,v1,...,vn), with vi*vj=0.
    return ((x[0]*y[0]) % p,) + tuple((x[0]*y[i] + y[0]*x[i]) % p for i in range(1, len(x)))


def apply(mat, vec, p):
    return tuple(sum(a*b for a,b in zip(row,vec)) % p for row in mat)


def is_rb(mat,p):
    d=len(mat)
    b=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    rb=[apply(mat, x,p) for x in b]
    for i in range(d):
        for j in range(i,d):
            lhs=multiply(rb[i],rb[j],p)
            rhs_input=tuple((a+b)%p for a,b in zip(multiply(rb[i],b[j],p),multiply(b[i],rb[j],p)))
            if lhs!=apply(mat,rhs_input,p):
                return False
    return True


def choose_q(n,k,q):
    if k<0 or k>n: return 0
    # Gaussian binomial coefficient as an exact quotient of integers.
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def squarezero_count(n,r,q):
    return choose_q(n,r,q)*choose_q(n-r,r,q)*prod(q**r-q**i for i in range(r))


def expected(n,q):
    c=Counter()
    idx3=0
    for r in range(n//2+1):
        N=squarezero_count(n,r,q)
        low=q**r
        high=q**n-low if q%2==0 else q**(n-r)-low
        c[r]+=N*low
        c[r+1]+=N*high
        if q%2==0: idx3+=N*(q**n-q**(n-r))
    return +c,idx3


def exhaustive(n,q):
    d=n+1
    rank_counts=Counter()
    cube_nonzero=0
    tested=0
    for vals in itertools.product(range(q),repeat=d*d):
        M=[list(vals[i*d:(i+1)*d]) for i in range(d)]
        if is_rb(M,q):
            rank_counts[rank(M,q)]+=1
            tested+=1
            # Count P^2 != 0 by checking each basis vector
            if any(any(apply(M,apply(M,tuple(int(j==k) for j in range(d)),q),q)) for k in range(d)):
                cube_nonzero+=1
    expected_counts, expected_cubes=expected(n,q)
    assert rank_counts == expected_counts,(n,q,rank_counts,expected_counts)
    assert cube_nonzero==expected_cubes,(n,q,cube_nonzero,expected_cubes)
    print('n=',n,'q=',q,'operators=',tested,'rank_distribution=',dict(sorted(rank_counts.items())),'P2_nonzero=',cube_nonzero)


def special_witness():
    # In characteristic two, n=2, R(1)=v2, R(v2)=v1, R(v1)=0.
    M=[[0,0,0],[0,0,1],[1,0,0]]
    assert is_rb(M,2)
    e0=(1,0,0)
    assert apply(M,apply(M,e0,2),2)==(0,1,0)
    assert apply(M,apply(M,apply(M,e0,2),2),2)==(0,0,0)
    print('sharp_index_three_witness=OK')


def main():
    for n,q in [(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)]:
        exhaustive(n,q)
    special_witness()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
