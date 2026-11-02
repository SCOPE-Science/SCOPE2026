#!/usr/bin/env python3
"""Exact-arithmetic checks for a flat-spectral single-channel absorber.
Python standard library only. Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def inverse_square_gap_sum(energy):
    return sum((F(1, (x-y)**2) for x,y in combinations(energy,2)), F(0))


def formula(energy, kappa):
    n=len(energy)
    return F(n,1)/kappa+F(2, n*n)*kappa*inverse_square_gap_sum(energy)


def constructed_solution(energy,kappa):
    n=len(energy)
    s=[sum((F(1,energy[j]-energy[k]) for k in range(n) if k!=j),F(0)) for j in range(n)]
    re=[[F(0) for _ in range(n)] for _ in range(n)]
    im=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        re[j][j]=F(1)/kappa+kappa*sum(((s[j]-s[k])/(energy[j]-energy[k]) for k in range(n) if k!=j),F(0))/F(2*n*n)
        for k in range(n):
            if j!=k:
                re[j][k]=-kappa*(s[j]-s[k])/F(2*n*n*(energy[j]-energy[k]))
                im[j][k]=F(1,n*(energy[j]-energy[k]))
    # Directly substitute exact rational real and imaginary entries in the Lyapunov equation.
    for j in range(n):
        for k in range(n):
            delta=energy[j]-energy[k]
            real=-delta*im[j][k]+kappa*sum((re[l][k]+re[j][l] for l in range(n)), F(0))/F(2*n)
            imag=delta*re[j][k]+kappa*sum((im[l][k]+im[j][l] for l in range(n)), F(0))/F(2*n)
            assert real==(F(1,n) if j==k else F(0)), ('real',j,k)
            assert imag==0, ('imag',j,k)
            assert re[j][k]==re[k][j] and im[j][k]==-im[k][j]
    assert sum((re[j][j] for j in range(n)), F(0)) == formula(energy,kappa)
    return re,im


def linear_solve(A,b):
    n=len(b)
    A=[list(A[i])+[b[i]] for i in range(n)]
    for c in range(n):
        i=next((k for k in range(c,n) if A[k][c]),None)
        assert i is not None
        A[c],A[i]=A[i],A[c]
        v=A[c][c]
        A[c]=[x/v for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]:
                v=A[r][c]
                A[r]=[A[r][h]-v*A[c][h] for h in range(n+1)]
    return [row[-1] for row in A]


def independent_lyapunov_solve(energy,kappa):
    n=len(energy)
    q=n*n
    A=[[F(0)]*(2*q) for _ in range(2*q)]
    b=[F(0)]*(2*q)
    def r(j,k):return j*n+k
    def z(j,k):return q+j*n+k
    for j in range(n):
        for k in range(n):
            row=r(j,k)
            A[row][z(j,k)]-=energy[j]-energy[k]
            A[z(j,k)][r(j,k)]+=energy[j]-energy[k]
            for l in range(n):
                for ix in (r(l,k),r(j,l)):
                    A[row][ix]+=kappa/F(2*n)
                for ix in (z(l,k),z(j,l)):
                    A[z(j,k)][ix]+=kappa/F(2*n)
            b[row]=F(1,n) if j==k else F(0)
    x=linear_solve(A,b)
    return sum((x[r(j,j)] for j in range(n)),F(0))


def weighted_cube(d,eps,J=F(1)):
    weights=[J*(1+eps*2**i) for i in range(d)]
    energy=[sum((weights[i]*(-1 if mask>>i&1 else 1) for i in range(d)),F(0)) for mask in range(1<<d)]
    return energy


def coefficient(d):
    a=[2**i for i in range(d)]
    c=F(0)
    for m in range(d+1):
        sums=[sum(a[i] for i in subset) for subset in combinations(range(d),m)]
        c+=sum((F(1,(x-y)**2) for x,y in combinations(sums,2)),F(0))
    return c


def test():
    cases=[([F(-2),F(0),F(1)],F(3,2)),
           ([F(-3),F(-1),F(2),F(7)],F(2,3)),
           ([F(-8),F(-2),F(1),F(5),F(11)],F(5,4)),
           ([F(-9),F(-4),F(-1),F(2),F(8),F(13)],F(7,3))]
    for E,k in cases:
        constructed_solution(E,k)
    independent=0
    for E,k in cases[:2]:
        assert independent_lyapunov_solve(E,k)==formula(E,k)
        independent+=1
    for d in (2,3,4):
        eps=F(1,2**d)
        E=weighted_cube(d,eps)
        assert len(set(E))==2**d
        constructed_solution(E,F(3,2))
        if d==2:
            assert independent_lyapunov_solve(E,F(3,2))==formula(E,F(3,2))
            independent+=1
        E0=weighted_cube(d,F(0))
        assert len(set(E0))==d+1
        assert len(E0)==2**d
    assert coefficient(2)==1
    assert coefficient(3)==F(49,18)
    assert coefficient(4)==F(2401501,396900)
    for d in range(2,6):
        n=2**d
        assert sum((comb(d,m) for m in range(d+1)))==n
        for eps in (F(1,10*(2**d-1)), F(1,100*(2**d-1))):
            E=weighted_cube(d,eps)
            S=inverse_square_gap_sum(E)
            C=coefficient(d)
            # Exact finite-epsilon lower bound: equal-cardinality spectral pairs alone.
            assert S>=C/(4*eps**2)
    print('PASS: exact Lyapunov identities for 7 distinct spectra (sizes 3,4,5,6,4,8,16)')
    print(f'PASS: {independent} independent exact Gaussian eliminations')
    print('PASS: weighted binary cubes d=2,3,4; nondegenerate perturbed spectra')
    print('PASS: exact equal-cardinality inverse-gap coefficients C2=1, C3=49/18, C4=2401501/396900')
    print('PASS: exact finite-epsilon gap lower bounds d=2,3,4,5')
    print('No finite sample substitutes for the general algebraic proof.')

if __name__=='__main__':test()
