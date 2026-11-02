#!/usr/bin/env python3
"""Finite-field checks of the nilpotent centralizer commuting-tuple formulas.
Run: python3 verify_nilpotent_centralizer.py
Only standard-library arithmetic and direct dense matrix multiplication are used.
"""
from itertools import product
from random import Random


def matmul(A, B, n, q):
    C = [0] * (n*n)
    for i in range(n):
        for k in range(n):
            a=A[i*n+k]
            if a:
                for j in range(n):
                    C[i*n+j] = (C[i*n+j] + a*B[k*n+j]) % q
    return tuple(C)


def matrices(r, q):
    n=r+2
    for v in product(range(q), repeat=r+4):
        # v=(a1,...,a_{r-1},d1,b0,b1,c0,c1).
        a=list(v[:r-1]); d,b0,b1,c0,c1=v[r-1:]
        A=[0]*(n*n)
        for degree,coefficient in enumerate(a,1):
            for i in range(r-degree):
                A[i*n+i+degree]=coefficient
        A[r*n+(r+1)] = d
        # B: R_2 -> R_r, C: R_r -> R_2.
        A[0*n+r]=b0; A[0*n+(r+1)]=b1; A[1*n+(r+1)]=b0
        # Bottom-left C: columns r-2 and r-1 of the top block.
        A[r*n+(r-2)]=c0
        A[r*n+(r-1)]=c1
        A[(r+1)*n+(r-1)]=c0
        yield tuple(A)


def check(r,q):
    n=r+2
    M=list(matrices(r,q))
    assert len(M)==q**(r+4) and len(set(M))==len(M)
    N=[0]*(n*n)
    for i in range(r-1): N[i*n+i+1]=1
    N[r*n+r+1]=1
    N=tuple(N)
    Z=tuple([0]*(n*n))
    for X in M:
        assert matmul(X,N,n,q)==matmul(N,X,n,q), 'not in centralizer'
        Y=X
        for _ in range(n-1): Y=matmul(Y,X,n,q)
        assert Y==Z, 'not nilpotent'
    neighbors=[]
    for i,X in enumerate(M):
        bits=0
        for j,Y in enumerate(M):
            if matmul(X,Y,n,q)==matmul(Y,X,n,q): bits|=1<<j
        neighbors.append(bits)
    m2=sum(row.bit_count() for row in neighbors)
    m3=sum((neighbors[i]&neighbors[j]).bit_count()
           for i,row in enumerate(neighbors)
           for j in range(len(M)) if (row>>j)&1)
    def f(m):
        return q**(n*m)+q*q*(q+1)*(q**((n-1)*m)-q**((n-2)*m))
    assert (len(M),m2,m3)==(f(1),f(2),f(3)), ((r,q),(len(M),m2,m3),(f(1),f(2),f(3)))
    print('matrix_case',n,q,len(M),m2,m3)


def rank_equations(v,w,q):
    x,b,c,B,C=v; xx,bb,cc,BB,CC=w
    return ((x*bb-xx*b)%q==0 and (x*cc-xx*c)%q==0 and
            (b*cc-bb*c)%q==0 and (b*CC+B*cc-bb*C-BB*c)%q==0)


def arithmetic_check(q,m):
    # Alternative independent count from five coordinate vectors, for m=2 and q<=3.
    assert m==2
    vals=list(product(range(q),repeat=5))
    ans=sum(rank_equations(v,w,q) for v in vals for w in vals)
    target=q**6 +q*q*(q+1)*(q**4-q**2)
    assert ans==target,(q,ans,target)
    print('coordinate_case',q,m,ans)

if __name__=='__main__':
    for r,q in [(3,2),(4,2)]: check(r,q)
    for q in [2,3]: arithmetic_check(q,2)
    print('NILPOTENT_TWO_BLOCK_CENTRALIZER_OK')
