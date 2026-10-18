#!/usr/bin/env python3
"""Exact integer checks for path-network single-input reachability volume."""
from math import gcd, factorial
from fractions import Fraction


def path_laplacian(n):
    a = [[0]*n for _ in range(n)]
    for i in range(n-1):
        a[i][i] += 1
        a[i+1][i+1] += 1
        a[i][i+1] -= 1
        a[i+1][i] -= 1
    return a


def det_exact(m):
    a = [list(row) for row in m]
    n = len(a)
    sign=1; prior=1
    for k in range(n-1):
        if not a[k][k]:
            t=next((i for i in range(k+1,n) if a[i][k]), None)
            if t is None: return 0
            a[k],a[t]=a[t],a[k]; sign=-sign
        d=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*d-a[i][k]*a[k][j]
                q,rem=divmod(val,prior)
                assert rem==0
                a[i][j]=q
            a[i][k]=0
        prior=d
    return sign*a[-1][-1]


def matvec(a, v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]


def krylov(a,j):
    n=len(a); v=[int(i==j) for i in range(n)]; cols=[]
    for t in range(n):
        cols.append(v);v=matvec(a,v)
    return [[cols[t][i] for t in range(n)] for i in range(n)]


def gramian_from_krylov(k):
    n=len(k)
    return [[sum(k[i][t]*k[j][t] for t in range(n)) for j in range(n)] for i in range(n)]


def solve_fraction(a,b):
    n=len(b); m=[[Fraction(v) for v in row]+[Fraction(y)] for row,y in zip(a,b)]
    for k in range(n):
        r=next(i for i in range(k,n) if m[i][k]);m[k],m[r]=m[r],m[k]
        p=m[k][k];m[k]=[z/p for z in m[k]]
        for i in range(n):
            if i!=k:
                p=m[i][k]
                if p: m[i]=[u-p*v for u,v in zip(m[i],m[k])]
    return [row[-1] for row in m]


def lyapunov_gramian(l,gamma,j):
    n=len(l); h=[[v+int(i==k)*gamma for k,v in enumerate(row)] for i,row in enumerate(l)]
    lhs=[]; rhs=[]
    for i in range(n):
        for k in range(n):
            lhs.append([int(q==k)*h[i][p]+int(i==p)*h[k][q] for p in range(n) for q in range(n)])
            rhs.append(int(i==j and k==j))
    x=solve_fraction(lhs,rhs)
    return [x[i*n:(i+1)*n] for i in range(n)]


def verify():
    tested=0; grams=0; lyaps=0
    for n in range(2,19):
        l=path_laplacian(n)
        for j in range(n):
            a=[[-x for x in row] for row in l]
            k=krylov(a,j); d=det_exact(k)
            predicted=int(gcd(2*j+1,n)==1)
            assert abs(d)==predicted,(n,j,d,predicted)
            tested+=1
            if n<=8:
                g=gramian_from_krylov(k)
                assert det_exact(g)==predicted,(n,j,det_exact(g))
                grams+=1
            if n<=4:
                # Exact symmetric Hurwitz continuous-time infinite horizon,
                # solved without eigenvalue approximations.
                w=lyapunov_gramian(l,1,j)
                # Convert rational determinant to integer via common denominator.
                from math import lcm
                den=lcm(*(v.denominator for row in w for v in row))
                num=det_exact([[int(v*den) for v in row] for row in w]); dd=Fraction(num,den**n)
                if predicted:
                    # Exact Kronecker-sum characteristic product; its eigenvalues
                    # are all pairwise sums 2*gamma + lambda_k + lambda_l.
                    kr = [[2*int(p==q)+l[p//n][q//n]*int(p%n==q%n)
                           +int(p//n==q//n)*l[p%n][q%n]
                           for q in range(n*n)] for p in range(n*n)]
                    expected=Fraction(1,det_exact(kr))
                    assert dd==expected,(n,j,dd,expected)
                    if j==0: baseline=dd
                    assert dd==baseline, (n,j,dd,baseline)
                else: assert dd==0
                lyaps+=1
    # Distinct symmetric affine discrete dynamics at the minimal full-rank horizon.
    affine=0
    for n in range(2,10):
        l=path_laplacian(n)
        for b in (1,2,3):
            a=[[4*int(i==t)-b*l[i][t] for t in range(n)] for i in range(n)]
            for j in range(n):
                d=det_exact(krylov(a,j))
                v=int(gcd(2*j+1,n)==1)*b**(n*(n-1)//2)
                assert abs(d)==v,(n,b,j,d,v)
                affine+=1
    print(f'VERIFY_OK integer_krylov_cases={tested} minimal_horizon_gramians={grams} rational_lyapunov={lyaps} affine_cases={affine}')

if __name__=='__main__': verify()
