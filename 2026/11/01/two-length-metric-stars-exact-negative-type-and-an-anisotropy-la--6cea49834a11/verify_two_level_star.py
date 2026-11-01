#!/usr/bin/env python3
"""Independent finite checks for two-length star metric negative-type formulas.

Uses standard-library arithmetic and a Jacobi eigensolver. The universal
all-real-parameter statements require the separate analytic proof.
"""
from fractions import Fraction
from math import log, sqrt, cosh, sinh, isclose
from random import Random


def dist(m,n,a,b):
    N=m+n+1
    D=[[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(1,N):
        ell=a if i<=m else b
        D[0][i]=D[i][0]=ell
        for j in range(1,i):
            ellj=a if j<=m else b
            D[i][j]=D[j][i]=ell+ellj
    return D


def direct_quadratic(D,z,p):
    return sum(z[i]*z[j]*D[i][j]**p for i in range(len(z)) for j in range(len(z)))


def symbolic_decomposition(m,n,a,b,z,p):
    A=z[1:m+1]; B=z[m+1:]
    x=sum(A)/m; y=sum(B)/n
    SA=sum((u-x)**2 for u in A)
    SB=sum((v-y)**2 for v in B)
    Fm=2*m-(m-1)*2**p
    Fn=2*n-(n-1)*2**p
    delta=(a+b)**p-a**p-b**p
    return -(2*a)**p*SA-(2*b)**p*SB-m*a**p*Fm*x*x-n*b**p*Fn*y*y+2*m*n*delta*x*y


def F(k,p):
    return 2*k-(k-1)*2**p


def delta(a,b,p):
    return ((a+b)**p-a**p-b**p)/(a*b)**(p/2)


def pstar(m,n,a,b):
    limit=min(log(2*m/(m-1),2), log(2*n/(n-1),2))
    lo,hi=1.,limit
    for _ in range(90):
        mid=(lo+hi)/2
        if F(m,mid)*F(n,mid)>m*n*delta(a,b,mid)**2:lo=mid
        else:hi=mid
    return (lo+hi)/2


def jacobi_eigvals(A):
    A=[list(map(float,row)) for row in A]
    n=len(A)
    for _ in range(70*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1e-11*max(1.,max(abs(A[k][k]) for k in range(n))):break
        t=(A[q][q]-A[p][p])/(2*A[p][q])
        t=(1 if t>=0 else -1)/(abs(t)+sqrt(1+t*t))
        c=1/sqrt(1+t*t); s=t*c
        apq=A[p][q]; app=A[p][p]; aqq=A[q][q]
        A[p][p]=app-t*apq; A[q][q]=aqq+t*apq
        A[p][q]=A[q][p]=0.
        for k in range(n):
            if k==p or k==q:continue
            akp=A[k][p]; akq=A[k][q]
            A[k][p]=A[p][k]=c*akp-s*akq
            A[k][q]=A[q][k]=s*akp+c*akq
    return sorted(A[i][i] for i in range(n))


def restricted_positive_form(D,p):
    # The vectors e_i-e_0 (i>0) form an independent zero-sum basis.
    K=len(D)-1
    return [[-.5*(float(D[i+1][j+1])**p-float(D[i+1][0])**p-float(D[0][j+1])**p) for j in range(K)] for i in range(K)]


def main():
    rng=Random(1907)
    exact=0
    for m,n,a,b in ((2,2,Fraction(1),Fraction(1)),(2,3,Fraction(3,2),Fraction(5,3)),(3,4,Fraction(7,2),Fraction(2,3)),(4,5,Fraction(2),Fraction(5))):
        D=dist(m,n,a,b)
        for p in (1,2,3):
            for _ in range(14):
                leaves=[Fraction(rng.randrange(-4,5)) for i in range(m+n)]
                z=[-sum(leaves)]+leaves
                assert direct_quadratic(D,z,p)==symbolic_decomposition(m,n,a,b,z,p)
                if p==1:
                    assert direct_quadratic(D,z,p)==-2*(a*sum(t*t for t in leaves[:m])+b*sum(t*t for t in leaves[m:]))
                exact+=1
    print('EXACT_QUADRATIC_DECOMPOSITION_OK tests=',exact)

    numeric=0
    for m,n in ((2,2),(2,3),(3,5),(4,4)):
        ratios=[1,1.5,3,10,100]
        roots=[]
        for ratio in ratios:
            a,b=float(ratio),1.
            p=pstar(m,n,a,b); roots.append(p)
            assert 1<p<min(log(2*m/(m-1),2),log(2*n/(n-1),2))
            assert abs(F(m,p)*F(n,p)-m*n*delta(a,b,p)**2)<2e-9
            D=dist(m,n,Fraction(str(a)),Fraction(1))
            for q,kind in ((p-.002,'below'),(p,'critical'),(p+.002,'above')):
                spec=jacobi_eigvals(restricted_positive_form(D,q))
                # Strictness/endpoint nullity and the unique emerging negative mode.
                scale=max(1,max(abs(w) for w in spec))
                if kind=='below': assert spec[0]>1e-9*scale,(m,n,ratio,q,spec)
                if kind=='critical':assert abs(spec[0])<1e-8*scale and spec[1]>1e-9*scale,(m,n,ratio,q,spec)
                if kind=='above':assert spec[0]<-1e-9*scale and spec[1]>1e-9*scale,(m,n,ratio,q,spec)
            numeric+=1
        assert roots==sorted(roots) and all(roots[i]<roots[i+1] for i in range(len(roots)-1))
        p_unif=log(2*(m+n)/(m+n-1),2)
        assert abs(roots[0]-p_unif)<2e-13
        assert abs(pstar(m,n,7.,1.)-pstar(m,n,1.,7.))<1e-13
        print('FAMILY_OK m,n=',m,n,'p_uniform=',round(roots[0],12),'p_ratio100=',round(roots[-1],12))
    print('ENDPOINT_INERTIA_OK cases=',numeric)
    print('ALL_TWO_LEVEL_STAR_CHECKS_OK')

if __name__=='__main__':main()
