#!/usr/bin/env python3
"""Finite characteristic tests for explicit Cartier action (not an infinite proof)."""
from math import comb

def is_prime(p):
    return p >= 2 and all(p % q for q in range(2, int(p**0.5)+1))

def basis(p):
    return [(i,j) for j in range(p-1) for i in range(p-1-j)]

def matrix(p,a):
    B=basis(p); index={b:i for i,b in enumerate(B)}
    M=[[0]*len(B) for _ in B]
    for ci,(i,j) in enumerate(B):
        for k in range(j+1):
            n=j-k
            for s in range(n+1):
                e=i+(p+1)*s+2*(n-s)
                if e%p!=p-1: continue
                row=(e-p+1)//p,k
                assert row in index
                # As a lies in F_p, its p-th root is itself.
                c=(-1)**n*comb(j,k)*comb(n,s)*pow(a,n-s,p)
                M[index[row]][ci]=(M[index[row]][ci]+c)%p
    return M

def rank(M,p):
    A=[v.copy() for v in M]; n=len(A); r=0
    for col in range(n):
        pivot=next((k for k in range(r,n) if A[k][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][col],-1,p)
        A[r]=[x*inv%p for x in A[r]]
        for j in range(r+1,n):
            fac=A[j][col]
            if fac:
                A[j]=[(A[j][h]-fac*A[r][h])%p for h in range(n)]
        r+=1
        if r==n:break
    return r

def predicted_block_sum(p):
    r=(p-1)//2
    return sum(min(t//2+1,r-(t+1)//2) for t in range(p-2))

def main():
    for p in (3,5,7,11,13,17,19):
        assert is_prime(p)
        g=p*(p-1)//2; expected=(p*p-1)//8
        assert len(basis(p))==g
        assert predicted_block_sum(p)==expected
        for a in ((0,1,2) if p<=13 else (0,1)):
            observed=rank(matrix(p,a),p)
            assert observed == (0 if a==0 else expected),(p,a,observed)
        print(f'p={p} genus={g} rank(a=0)=0 rank(a!=0)={expected}')
    print('VERIFY_OK')

if __name__=='__main__':main()
