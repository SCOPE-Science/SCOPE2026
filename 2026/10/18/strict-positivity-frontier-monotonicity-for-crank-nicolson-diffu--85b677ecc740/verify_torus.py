#!/usr/bin/env python3
"""Independent finite checks for the sharp positivity threshold on periodic square-lattice grids.

Pure Python 3, standard library only. Infinite and finite parameter statements
are proved in the accompanying paper; finite checks here are diagnostic.
"""
from fractions import Fraction as F
from math import cos, pi, sqrt, comb


def laplacian(m, n):
    if m < 3 or n < 3:
        raise ValueError('periods must be at least three')
    N = m*n
    L = [[F(0) for _ in range(N)] for _ in range(N)]
    for a in range(m):
        for b in range(n):
            i = a*n+b
            L[i][i] = F(4)
            for aa, bb in [((a+1)%m,b), ((a-1)%m,b), (a,(b+1)%n), (a,(b-1)%n)]:
                L[i][aa*n+bb] -= 1
    return L


def invert(A):
    N=len(A)
    T=[list(A[i])+[F(int(i==j)) for j in range(N)] for i in range(N)]
    for k in range(N):
        if not T[k][k]:
            pivot=next(i for i in range(k+1,N) if T[i][k])
            T[k],T[pivot]=T[pivot],T[k]
        p=T[k][k]
        T[k]=[v/p for v in T[k]]
        for i in range(N):
            if i!=k and T[i][k]:
                a=T[i][k]
                T[i]=[v-a*w for v,w in zip(T[i],T[k])]
    return [row[N:] for row in T]


def return_diag_fourier(m,n,h):
    return sum(1/(1+2*h-h*(cos(2*pi*j/m)+cos(2*pi*k/n)))
               for j in range(m) for k in range(n))/(m*n)


def threshold(m,n):
    lo,hi=0.,1.
    for _ in range(65):
        mid=(lo+hi)/2
        if return_diag_fourier(m,n,mid)>.5: lo=mid
        else: hi=mid
    return (lo+hi)/2


def elliptic_return(h):
    z=2*h/(1+2*h)
    a,b=1.,sqrt(1-z*z)
    for _ in range(30):
        a,b=(a+b)/2,sqrt(a*b)
    return 1/((1+2*h)*a)


def infinite_threshold():
    lo,hi=0.,1.
    for _ in range(70):
        mid=(lo+hi)/2
        if elliptic_return(mid)>.5: lo=mid
        else: hi=mid
    return (lo+hi)/2


def rigorous_series_bounds(h, N=23):
    z=2*h/(1+2*h)
    lower=sum(F(comb(2*k,k)**2, 16**k)*z**(2*k) for k in range(N))/(1+2*h)
    # central-binomial-square coefficients are <=1, yielding a geometric tail
    upper=lower+z**(2*N)/((1+2*h)*(1-z*z))
    return lower,upper


def main():
    for m,n in [(3,3),(3,4),(4,4),(3,5),(5,5)]:
        L=laplacian(m,n)
        S=len(L)
        for h in [F(1,2),F(3,5),F(3,4)]:
            A=[[F(int(i==j))+h*L[i][j]/2 for j in range(S)] for i in range(S)]
            R=invert(A)
            assert all(x>0 for row in R for x in row), (m,n,h,'resolvent')
            assert all(sum(row)==1 for row in R), (m,n,h,'mass')
            assert all(R[i][i]==R[0][0] for i in range(S)), (m,n,h,'transitivity')
            C=[[2*R[i][j]-F(int(i==j)) for j in range(S)] for i in range(S)]
            assert all(C[i][j]>0 for i in range(S) for j in range(S) if i!=j)
            assert all(sum(row)==1 for row in C)
            assert all(x>=0 for row in C for x in row)==(R[0][0]>=F(1,2))
            assert abs(float(R[0][0])-return_diag_fourier(m,n,float(h)))<2e-12
        print('exact matrix checks PASS',m,n)
    for m in range(3,9):
        for n in range(3,9):
            t=threshold(m,n)
            if m<8: assert t>threshold(m+1,n)+1e-12
            if n<8: assert t>threshold(m,n+1)+1e-12
    print('finite Fourier comparisons PASS (3..8 in both coordinates)')
    t0=infinite_threshold()
    z=2*t0/(1+2*t0)
    assert .588197<t0<.588198
    assert abs(threshold(3,3)-(1+sqrt(57))/14)<2e-12
    for m in range(3,9):
        for n in range(3,9):
            t=threshold(m,n)
            assert 0<t-t0<=12.5*z**min(m,n)+1e-14
    for h in (F(588197,1000000),F(588198,1000000)):
        lower,upper=rigorous_series_bounds(h)
        if h<F(588198,1000000): assert lower>F(1,2)
        else: assert upper<F(1,2)
    print('elliptic limit, exponential inequality and rigorous series brackets PASS')
    print('h_infinity =',format(t0,'.15f'))
    for m,n in ((3,3),(4,4),(5,5),(8,8)):
        print('threshold',m,n,format(threshold(m,n),'.15f'))

if __name__=='__main__': main()
