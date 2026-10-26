#!/usr/bin/env python3
"""Standalone exact and numerical checks for a sixth-moment SU(2) character packet."""
from collections import defaultdict
from math import comb, isclose
import cmath
import sympy as sp
import numpy as np
from scipy.optimize import brentq

checks=0
def check(cond,description):
    global checks
    if not cond:
        raise AssertionError(description)
    checks+=1

def multiply(A,B):
    C=defaultdict(int)
    for a,u in A.items():
        for b,v in B.items():
            for k in range(abs(a-b),a+b+1,2):
                C[k]+=u*v
    return dict(C)

def integral_labels(labels):
    d={0:1}
    for ell in labels:
        d=multiply(d,{ell:1})
    return d.get(0,0)

def moment_coeffs(n):
    return [comb(6,j)*integral_labels([1]*(6-j)+[n]*j) for j in range(7)]

def predicted(n):
    s=(n**3+3*n**2+4*n+2)//2
    o=n%2
    return [5, (24 if n==3 else 6 if n==5 else 0), 90,160 if o else 0,60*n+15, (15*(n+1)**2//2) if o else 0,s]

def phase_moment(n,a,b):
    mm=[integral_labels([1]*(6-j)+[n]*j) for j in range(7)]
    return sum(comb(3,i)*comb(3,j)*a**(3-i)*b**i*a.conjugate()**(3-j)*b.conjugate()**j*mm[i+j]
               for i in range(4) for j in range(4)).real

def Q(n,t):
    co=predicted(n)
    return sum(co[j]*t**(6-j) for j in range(7))

def H(n,t):
    co=predicted(n)
    deriv=sum((6-j)*co[j]*t**(5-j) for j in range(6))
    return (1+t*t)*deriv-6*t*Q(n,t)

def optimum(n):
    co=predicted(n)
    if n%2==0:
        if n>=6:return float(co[6]),0.0,1.0
        s=co[6]
        # 25 + 2(20n-25) q + (s-20n-5) q^2 = 0, q=|b/a|^2.
        B=2*(20*n-25); C=s-20*n-5
        q=(-B-np.sqrt(B*B-100*C))/(2*C)
        t=1/np.sqrt(q)
        return Q(n,t)/(1+t*t)**3,t,1/np.sqrt(1+t*t)
    t=brentq(lambda x:H(n,x),0.0,2.0,xtol=1e-14)
    return Q(n,t)/(1+t*t)**3,t,1/np.sqrt(1+t*t)

for n in range(2,67):
    got=moment_coeffs(n)
    exp=predicted(n)
    for j in range(7):check(got[j]==exp[j],f'fusion moment n={n},j={j}: {got[j]} vs {exp[j]}')
    K,t,b=optimum(n)
    check(K>=exp[6]-1e-7,'max at least pure high char')
    check(K>=5-1e-7,'max at least fundamental char')
    if n%2:
        check(t>0,'odd strict admixture')
        check(abs(H(n,t)) < (n**3)*1e-9,'odd derivative zero')
    elif n>=6:
        check(t==0 and K==exp[6],'even exclusion')
    else:
        check(t>0,'small even strict admixture')
    for k in range(20):
        aa=np.cos((k+1)*np.sqrt(2)) + 1j*np.sin((k+1)*np.sqrt(3))
        bb=(1+k%6)*np.exp(1j*(k+1)*np.sqrt(5))
        val=phase_moment(n,aa,bb)
        check(val>=-1e-8,'integral nonnegative')
        check(val <= K*(abs(aa)**2+abs(bb)**2)**3 + 2e-5*(abs(aa)**2+abs(bb)**2)**3,'global complex inequality')
        p=abs(aa); q=abs(bb)
        check(val <= sum(got[j]*p**(6-j)*q**j for j in range(7))+1e-6,'phase alignment')

# independent exact polynomial-in-x integration, using Chebyshev and Catalan semicircle moments
x=sp.symbols('x')
catalan=lambda k: int(sp.catalan(k))
def semicircle_poly_moment(poly):
    P=sp.Poly(sp.expand(poly),x)
    return sum(int(c)*catalan(j//2) for (j,),c in P.terms() if j%2==0)
for n in range(2,20):
    u=sp.chebyshevu(n,x/2)
    for j in range(7):
        val=semicircle_poly_moment(x**(6-j)*u**j)
        check(comb(6,j)*val==predicted(n)[j],f'semicircle check n{n} j{j}')

# Exactly one positive derivative root: symbolic sign arguments for every finite exceptional case,
# plus sampled rational root tests of the general sign pattern.
t,N=sp.symbols('t N',real=True)
S=(N**3+3*N**2+4*N+2)/2
for n in [3,5,7,9,11,21,51,151]:
    co=predicted(n)
    q=sum(co[j]*t**(6-j) for j in range(7))
    h=sp.Poly(sp.expand((1+t*t)*sp.diff(q,t)-6*t*q),t)
    desc=[int(v) for v in h.all_coeffs() if v]
    sgn=[v>0 for v in desc]
    changes=sum(a!=b for a,b in zip(sgn,sgn[1:]))
    check(changes==1,f'Descartes root uniqueness n{n}')

# Exact ratio asymptotics follow from the leading coefficients of the stationarity polynomial.
for n in [101,201,501,1001]:
    k,tt,_=optimum(n)
    check(abs(n*tt-2.5)<0.05,'asymptotic root scale')
    check(abs((k-predicted(n)[6])/n-75/8)<0.2,'asymptotic gain scale')

print('PASS; assertions=',checks)
print('moment examples:')
for n in [2,3,4,5,6,7,9,51]:
    k,tt,bb=optimum(n)
    print(n,'moments=',predicted(n),'K6=',format(k,'.13f'),'a/b=',format(tt,'.13f'))
print('Analytical proof required for all-n assertions; numerical optimization and finite checks are not a replacement.')
