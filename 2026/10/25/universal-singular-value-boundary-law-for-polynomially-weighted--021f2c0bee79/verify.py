#!/usr/bin/env python3
"""Independent finite checks for the radial-power Fock dilation spectral law.
The infinite-dimensional statements are proved analytically in RESULT.md.
"""
import math
import numpy as np
from scipy.special import gammaln, gamma, lambertw
from scipy.linalg import svdvals

def monomial_weights(alpha, m, j, eps, n):
    n=np.arange(n,dtype=float)
    a=(2*n+2)/m
    return np.exp(-eps*n - j/m*math.log(alpha)+.5*(gammaln(a+2*j/m)-gammaln(a)))

def fock_matrix(alpha,m,cs,eps,N):
    k=len(cs)-1
    a=np.zeros((N+k,N),dtype=complex)
    for j,c in enumerate(cs):
        if c!=0:
            a[np.arange(N)+j,np.arange(N)] += c*monomial_weights(alpha,m,j,eps,N)
    return a

def theoretical(alpha,m,k,ck,p):
    g=k/m; c=abs(ck)*alpha**(-g)*(2/m)**g
    op=c*(g/math.e)**g
    pn=c*(gamma(p*g+1)/p**(p*g+1))**(1/p)
    return g,c,op,pn

checks=0
# Exact column and Hilbert--Schmidt identity for nonmonomial polynomial weights.
for alpha,m in [(1.,2.),(2.,1.5),(.7,3.)]:
    for cs in [(1+0j, 0.6-.2j, 1.0+.5j), (0.7+0j,-1j,2.,0.25+.3j)]:
        mat=fock_matrix(alpha,m,cs,.13,45)
        actual=(abs(mat)**2).sum()
        target=sum(abs(c)**2*(monomial_weights(alpha,m,j,.13,45)**2).sum() for j,c in enumerate(cs))
        assert abs(actual-target) <= 1e-10*max(1,actual)
        checks+=1
# Weyl singular-value perturbation inequality, checked on actual band matrices.
for alpha,m in [(1.,2.),(2.,1.5),(.7,3.)]:
    cs=[0.7+.2j, -0.4+0.5j, 1.-.3j]
    x=fock_matrix(alpha,m,cs,.075,82)
    y=fock_matrix(alpha,m,[0,0,cs[-1]],.075,82)
    rem=x-y
    sx=svdvals(x);sy=svdvals(y)
    assert (abs(sx-sy)).max() <= np.linalg.norm(rem,2)*(1+1e-9)
    checks+=1
# Uniform fixed-rank asymptotics at decreasing cutoffs in the monomial model.
for alpha,m,k in [(1,2,2),(.7,3,3),(2.,1.5,1)]:
    g,c,edge,_=theoretical(alpha,m,k,1,2)
    for eps in [.045,.025,.015]:
        w=monomial_weights(alpha,m,k,eps,7000)
        est=eps**g*w.max()
        assert abs(est/edge-1)<.13,(alpha,m,k,eps,est,edge)
        checks+=1
# Schatten-p scaling, including p<1: actual singular-value series, not matrix logs.
for m,k in [(2.,2),(3.,3),(1.5,1)]:
    for p in [.55,1.,2.,4.]:
        g,c,_,pconst=theoretical(1,m,k,1,p)
        eps=.013
        w=monomial_weights(1,m,k,eps,14000)
        empirical=eps**(g+1/p)*np.sum(w**p)**(1/p)
        assert abs(empirical/pconst-1)<.15,(m,k,p,empirical,pconst)
        checks+=1
# m=2,k=2 Hilbert--Schmidt closed form independent of gamma implementation.
for eps in [.17,.045,.012]:
    r=math.exp(-eps)
    exact=2/(1-r*r)**3
    numeric=np.sum(monomial_weights(1,2,2,eps,7000)**2)
    assert abs(numeric/exact-1)<1e-10
    checks+=1
# Lambert-W two-root superlevel law, with independently counted discrete singular weights.
for eps in [.012,.006,.003]:
    w=monomial_weights(1,2,2,eps,7000)
    for z in [.1,.2,.3]:
        xlo=-float(lambertw(-z,0).real)
        xhi=-float(lambertw(-z,-1).real)
        predicted=xhi-xlo
        observed=eps*int(np.count_nonzero(eps*w>z))
        assert abs(observed-predicted)<.08,(eps,z,observed,predicted)
        checks+=1
print('PASS: %d exact-identity, Weyl, asymptotic and two-branch counting checks' % checks)
