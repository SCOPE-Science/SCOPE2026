"""Exact-rational regression checks for nonuniform Dirichlet P1 backward Euler heat stepping.

Run: python verify_graded_mesh.py
All assertions are exact. The analytic result for all mesh lengths and sizes is proved separately.
"""
from fractions import Fraction as F
from random import Random


def assemble(h):
    n = len(h)-1
    M = [[F(0) for _ in range(n)] for _ in range(n)]
    K = [[F(0) for _ in range(n)] for _ in range(n)]
    for cell, length in enumerate(h):
        verts = (cell-1, cell)
        for a in (0,1):
            for b in (0,1):
                i,j = verts[a],verts[b]
                if 0 <= i < n and 0 <= j < n:
                    M[i][j] += length*F(2 if a==b else 1,6)
                    K[i][j] += F(1 if a==b else -1,1)/length
    return M,K


def solve(A,B):
    n=len(A)
    W=[row[:] + B[i][:] for i,row in enumerate(A)]
    for k in range(n):
        pivot=W[k][k]
        assert pivot>0 # SPD tridiagonal elimination; no row swaps
        for j in range(k+1,2*n):
            W[k][j]/=pivot
        W[k][k]=F(1)
        for i in range(k+1,n):
            q=W[i][k]
            for j in range(k+1,2*n):
                W[i][j]-=q*W[k][j]
            W[i][k]=F(0)
    for k in range(n-1,-1,-1):
        for i in range(k):
            q=W[i][k]
            for j in range(n,2*n):
                W[i][j]-=q*W[k][j]
            W[i][k]=F(0)
    return [row[n:] for row in W]


def check(h,t):
    n=len(h)-1
    M,K=assemble(h)
    A=[[M[i][j]+t*K[i][j] for j in range(n)] for i in range(n)]
    P=solve(A,M)
    critical=max(x*x/6 for x in h[1:-1])
    predicted=(t==0 or t>=critical)
    actual=all(x>=0 for row in P for x in row)
    assert predicted==actual,(n,h,t,critical,P)
    if t>0:
        assert all(P[i][i+1]>0 and P[i+1][i]>0 for i in range(n-1))
    if 0<t<critical:
        for i in range(n-1):
            e=h[i+1]/6-t/h[i+1]
            if e>0:
                if i<n-2:
                    assert P[i][i+2]<0
                else:
                    assert P[n-1][n-3]<0
                break
        else:raise AssertionError('No non-Stieltjes offdiagonal')
    return P


def main():
    rng=Random(361022)
    trials=0
    for n in range(3,9):
        for case in range(14):
            h=[F(rng.randint(1,19),rng.randint(1,11)) for _ in range(n+1)]
            threshold=max(x*x/6 for x in h[1:-1])
            for ratio in (F(0),F(1,100),F(1,3),F(9,10),F(1),F(5,4),F(10)):
                check(h,threshold*ratio)
                trials+=1
    for n in range(3,9):
        h=[F(1)]*(n+1)
        for t in (F(0),F(1,100),F(1,7),F(1,6),F(1,5)):
            check(h,t)
            trials+=1
    print('PASS: ',trials,' exact rational cases across n=3..8; including thresholds and sign witnesses.')

if __name__=='__main__': main()
