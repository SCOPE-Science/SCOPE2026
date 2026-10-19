#!/usr/bin/env python3
"""Exact arithmetic checks for coordinate correlations of the twisted baker map.

Standalone; requires only Python's standard library. Mathematical proof is supplied
separately and is not replaced by these finite checks.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, cos, sin, acos, sqrt


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def ident(m):
    return [[Q(int(i==j)) for j in range(m)] for i in range(m)]


def matrix_B(m):
    B = [[Q(0) for _ in range(m)] for _ in range(m)]
    B[0][0], B[0][1] = Q(1,4), Q(1,2)
    for j in range(1,m-1):
        B[j][j], B[j][j+1] = Q(1,2), Q(1,2)
    B[m-1][m-1], B[m-1][0] = Q(1,2), Q(-1,4)
    return B


def branches(m):
    L, R = [[[Q(0) for _ in range(m)] for _ in range(m)] for _ in range(2)]
    cL, cR = [Q(0)]*m, [Q(0)]*m
    L[0][0], cL[0] = Q(1,2), Q(-1,2)
    for i in range(1,m): L[i][i] = Q(1)
    for i in range(m-1): R[i][i+1] = Q(1)
    R[m-1][0], cR[m-1] = Q(-1,2), Q(1,2)
    return (L,cL), (R,cR)


def apply_affine(phi, branch):
    a,c = phi
    A,b = branch
    return ([sum(a[k]*A[k][j] for k in range(len(a))) for j in range(len(a))],
            c+sum(a[k]*b[k] for k in range(len(a))))


def apply_P(phi, br):
    p, q = [apply_affine(phi, z) for z in br]
    return ([(u+v)/2 for u,v in zip(p[0],q[0])], (p[1]+q[1])/2)


def poly_mul(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def det(A):
    A = [row[:] for row in A]
    n=len(A); ans=Q(1)
    for i in range(n):
        piv=next((j for j in range(i,n) if A[j][i]),None)
        if piv is None: return Q(0)
        if piv!=i: A[piv], A[i]=A[i], A[piv]; ans=-ans
        d=A[i][i];ans*=d
        for j in range(i+1,n):
            if A[j][i]:
                c=A[j][i]/d
                for k in range(i+1,n): A[j][k]-=c*A[i][k]
                A[j][i]=Q(0)
    return ans


def check():
    checks=0
    for m in range(2,9):
        B=matrix_B(m); br=branches(m)
        means=[Q(0)]+[Q(1,2)]*(m-1)
        Bn=ident(m)
        phis=[([Q(int(j==i)) for j in range(m)],-means[i]) for i in range(m)]
        den=poly_mul([Q(1),Q(-1,4)], [Q(comb(m-1,k))*(-Q(1,2))**k for k in range(m)])
        den += [Q(0)]*(m+1-len(den))
        den[m]+=Q(1,2**(m+1))
        num=[Q(comb(m-1,k))*(-Q(1,2))**k for k in range(m)]
        coeff=[]
        for n in range(19):
            cn=( (num[n] if n<len(num) else 0) -sum(den[k]*coeff[n-k] for k in range(1,min(n,m)+1)))
            coeff.append(cn)
            assert cn==Bn[0][0],('generating-function',m,n,cn,Bn[0][0]);checks+=1
            for i in range(m):
                assert phis[i][0] == Bn[i],('affine',m,n,i);checks+=1
                assert phis[i][1] == -sum(Bn[i][j]*means[j] for j in range(m)),('constant',m,n,i);checks+=1
            if n<m: assert Bn[0][0]==Q(1,4)**n;checks+=1
            if n==m: assert Bn[0][0]==Q(1,4)**m-Q(1,2**(m+1));checks+=1
            phis=[apply_P(p,br) for p in phis]
            Bn=matmul(Bn,B)
        for lam in [Q(0),Q(1,4),Q(1,3),Q(1,2),Q(1),Q(2)]:
            d=det([[lam*int(i==j)-B[i][j] for j in range(m)] for i in range(m)])
            assert d==(lam-Q(1,4))*(lam-Q(1,2))**(m-1)+Q(1,2**(m+1));checks+=1
        # Independent complete inverse-word enumeration for finite lengths.
        for n in range(0,8):
            sums=[[Q(0) for _ in range(m)] for __ in range(m)]
            cc=[Q(0)]*m
            for word in product((0,1), repeat=n):
                A,c=ident(m),[Q(0)]*m
                for idx in word:
                    T,b=br[idx]
                    A,c=matmul(T,A),[sum(T[i][j]*c[j] for j in range(m))+b[i] for i in range(m)]
                for i in range(m):
                    for j in range(m): sums[i][j]+=A[i][j]/(2**n)
                    cc[i]+=(c[i]-means[i])/2**n
            Bn=ident(m)
            for _ in range(n): Bn=matmul(Bn,B)
            assert sums==Bn,('inverse-word',m,n);checks+=m*m
            assert cc==[-sum(Bn[i][j]*means[j] for j in range(m)) for i in range(m)],('inverse-constant',m,n);checks+=m
    # M=2 formula independent floating-point diagnostic.
    B=matrix_B(2);U=ident(2)
    phase=acos(.75)
    for n in range(32):
        c=float(U[0][0])/3
        expected=2**(-n)*(cos(n*phase)-sin(n*phase)/sqrt(7))/3
        assert abs(c-expected)<1e-10,('planar closed form',n,c,expected); checks+=1
        U=matmul(U,B)
    print('PASS: %d exact-rational identities / finite floating diagnostics' % checks)
    print('All exact transfer-branch, generating-function, inverse-word, and characteristic identities agree.')
    print('Finite checks do not prove the all-dimensional spectral statements.')

if __name__ == '__main__': check()
