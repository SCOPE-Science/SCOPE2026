"""Reproducibility checks for one-harmonic balanced circle Sobolev norms.
Run with Python 3, standard library only. Finite checks complement an analytic proof.
"""
from fractions import Fraction as F
from math import sqrt

def pivot_exact(n,m,lam,a):
    j = n % m
    h = F(1) + lam*F(j*j,n*n)
    while j+m <= n:
        j += m
        h = F(1)+lam*F(j*j,n*n) - a*a*lam*lam*F(j*j*(j-m)*(j-m),n**4)/h
    return h

def norm_exact(n,m,lam,a):
    # Independently form the full Gram matrix and solve the normal equations.
    G=[]
    for j in range(n+1):
        G.append([(F(1) if j==k else F(0)) +
                  lam*F(j*k,n*n)*((F(1) if j==k else a if abs(j-k)==m else F(0)))
                  for k in range(n+1)])
    M=[G[j][:n]+[-G[j][n]] for j in range(n)]
    for k in range(n):
        assert M[k][k] > 0
        piv=M[k][k]
        for i in range(k+1,n):
            fac=M[i][k]/piv
            if fac:
                for t in range(k,n+1):M[i][t]-=fac*M[k][t]
    x=[F(0)]*n
    for k in range(n-1,-1,-1):
        x[k]=(M[k][n]-sum(M[k][j]*x[j] for j in range(k+1,n)))/M[k][k]
    return G[n][n]+sum(G[n][j]*x[j] for j in range(n))

exact_count=0
for n in range(1,13):
    for m in range(1,6):
        for lam,a in [(F(1),F(1,4)),(F(3,2),F(-1,3))]:
            v=pivot_exact(n,m,lam,a)
            assert v==norm_exact(n,m,lam,a)
            exact_count+=1

asymp_count=0
for lam,a in [(0.5,0.2),(2.0,-0.35),(5.0,0.45)]:
    for m in [1,2,4,7]:
        d=1+lam
        delta2=d*d-4*a*a*lam*lam
        H=(d+sqrt(delta2))/2
        C=2*m*a*a*lam*lam/delta2
        errs=[]
        for n in [300,600,1200]:
            j=n%m
            h=1+lam*(j/n)**2
            while j+m<=n:
                j+=m
                h=1+lam*(j/n)**2-(a*lam*j*(j-m)/(n*n))**2/h
            errs.append(n*n*(h-H-C/n))
        # Analytic result asserts bounded n^2 errors, not empirical convergence proof.
        assert abs(errs[2]-errs[1])<1.0, (lam,a,m,errs)
        asymp_count+=1
print('EXACT_GRAM_VS_SCHUR',exact_count,'ASYMPTOTIC_FINITE_TESTS',asymp_count,'PASS')
