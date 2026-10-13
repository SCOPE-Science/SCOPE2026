"""Exact arithmetic checks for the Cesaro mixing spectrum of Q_r Cartesian K_q.
Public scientific verification; requires only Python's standard library.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def C(j):
    return F(comb(j, j//2), 2**j) if j%2 == 0 else F(0)


def e(j,q):
    z=F(q-2,q)*C(j)
    # The two nonzero frequencies of cos(qt) match terms of cos(2t)^j.
    if q%2==0 and q//2 <= j and (j-q//2)%2==0:
        k=(j-q//2)//2
        z+=F(2*comb(j,k),q*2**j)
    return z


def spectrum(r,q):
    return {(j,0):C(j) for j in range(r+1)} | {(j,1):e(j,q) for j in range(r+1)}


def prediction(r,q):
    return q*2**(r-1)+(q-1)*sum(comb(r,j) for j in range(1,r+1,2)
                                      if q%4==2 and q>=6 and j>=q//2)


def direct_projector_average(r,q):
    # Spectral idempotents are computed from Walsh characters and the two
    # eigenspaces of K_q, combining *equal total adjacency eigenvalues*.
    n=2**r*q
    P={}
    for j in range(r+1):
        for d in (0,1):
            theta=r-2*j+(q-1 if d==0 else -1)
            R=P.setdefault(theta,[[F(0) for _ in range(n)] for __ in range(n)])
            for u in range(n):
                a,x=divmod(u,q)
                for v in range(n):
                    b,y=divmod(v,q)
                    h=(a^b).bit_count()
                    kw=sum((-1)**k*comb(h,k)*comb(r-h,j-k)
                           for k in range(max(0,j-(r-h)),min(h,j)+1))
                    px=F(kw,2**r)
                    py=F(1,q) if d==0 else (int(x==y)-F(1,q))
                    R[u][v]+=px*py
    M=[[sum(Pt[u][v]**2 for Pt in P.values()) for v in range(n)]
       for u in range(n)]
    return M,sorted(P)


def exact_rank(A):
    A=[row[:] for row in A]
    m=len(A); rank=0
    for col in range(m):
        p=next((k for k in range(rank,m) if A[k][col]),None)
        if p is None:continue
        A[rank],A[p]=A[p],A[rank]
        pivot=A[rank][col]
        for k in range(rank+1,m):
            if A[k][col]:
                f=A[k][col]/pivot
                for c in range(col,m): A[k][c]-=f*A[rank][c]
        rank+=1
    return rank


def check():
    sectors=0
    for q in (3,4,5,6,8,10,14):
        for r in range(1,9):
            v=spectrum(r,q)
            assert all(F(0)<=x<=F(1) for x in v.values())
            rr=sum(comb(r,j)*(1 if d==0 else q-1)
                   for (j,d),x in v.items() if x)
            assert rr==prediction(r,q),(r,q,rr,prediction(r,q))
            sectors+=len(v)
    assert spectrum(3,6)[(3,1)]==F(1,24)
    assert prediction(3,6)==29
    assert prediction(2,6)==12
    assert prediction(5,10)==169
    # Direct exact spectral projection of the actual adjacency matrices,
    # independent of the trigonometric Fourier coefficient computation.
    cases=((1,3),(2,4),(2,6),(3,6),(4,6))
    for r,q in cases:
        M,theta=direct_projector_average(r,q)
        assert all(sum(row)==1 for row in M),(r,q,'stochastic')
        assert all(M[i][j]==M[j][i] for i in range(len(M)) for j in range(len(M)))
        rk=exact_rank(M)
        assert rk==prediction(r,q),(r,q,rk,prediction(r,q),theta)
        if (r,q)==(3,6):
            # The repeated adjacency energy 2 is the first overlap responsible
            # for the positive extra five-dimensional sector.
            assert theta==[-4,-2,0,2,4,6,8]
    print('VERIFY_OK Fourier_sectors=%s exact_projector_cases=%s first_resonant_rank=29/48 threshold_q6_r3=True' % (sectors,len(cases)))

if __name__=='__main__':check()
