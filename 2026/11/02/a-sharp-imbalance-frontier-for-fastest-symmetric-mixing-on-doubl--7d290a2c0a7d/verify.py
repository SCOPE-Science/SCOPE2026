"""Standalone finite checks of the double-star fastest-mixing formula.
Requires Python 3 and NumPy; finite numerical checks supplement the proof.
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np

def data(p,q):
    assert 2 <= p < q
    d=q*q+q-p
    a=F(q*(q-p),p*d); b=F(q*(p+1)-p,d); c=F(q-p,d)
    mu=F(q*q,d)
    u2=F(p*q*q,(q-p)**2)
    w2=F((q*(p+1)-p)**2,q*(q-p)**2)
    X=F(p**3,(q-p)**2)
    D=1+u2+w2
    H=1-F(p*p,(q-p)**2)-F((q*(p+1)-p)**2,q*q*(q-p)**2)
    return a,b,c,mu,X,w2,D,H

def det_characteristic(t,p,q,a,b,c):
    # Four-cell weighted-Laplacian quotient; products avoid square roots.
    d1=a-t
    d2=(1-t)*d1-p*a*a
    d3=(1-t)*d2-b*b*d1
    return (c-t)*d3-q*c*c*d2

def transition(p,q,a,b,c):
    n=p+q+2; P=np.zeros((n,n))
    for leaf in range(p):
        P[leaf,p]=P[p,leaf]=float(a)
    P[p,p+1]=P[p+1,p]=float(b)
    for leaf in range(p+2,n):
        P[p+1,leaf]=P[leaf,p+1]=float(c)
    np.fill_diagonal(P,1-P.sum(axis=1))
    return P

def slem(P):
    eig=np.linalg.eigvalsh(P)
    assert abs(eig[-1]-1)<1e-8
    return max(abs(eig[0]),eig[-2])

passed=0; covered=0; negative=0; comparisons=0
for p in range(2,13):
    for q in range(p+1,4*p+3):
        a,b,c,mu,X,w2,D,H=data(p,q)
        assert p*a+b==q*c+b==1
        assert a>=c>0 and 0<b<1
        for t0 in [-2,-1,0,1,2,3]:
            t=F(t0)
            expected=t*(t-c)*(t*t-(2+a)*t+(p+q+2)*a*b)
            assert det_characteristic(t,p,q,a,b,c)==expected
            passed+=1
        if H>=0:
            theta=D/(D+q*H)
            lamL=theta*X/(p*D)
            lamR=(theta*w2/D+1-theta)/q
            assert 0<theta<=1 and lamL>0 and lamR>0
            assert theta/D==lamL+lamR
            assert theta*X/D==lamL*p
            assert theta*w2/D+1-theta==lamR*q
            mat=transition(p,q,a,b,c)
            assert np.min(mat)>-1e-10 and np.max(abs(mat.sum(axis=1)-1))<1e-10
            assert abs(slem(mat)-float(mu))<1e-9
            covered+=1
            # Random, deliberately asymmetric feasible edge-transition designs.
            if p<=5 and q<=20:
                rng=np.random.default_rng(193*p+q)
                n=p+q+2
                for _ in range(40):
                    M=np.zeros((n,n))
                    # Ensure feasibility by scaling each original edge by <=1/3.
                    for leaf in range(p):
                        x=float(a)*float(rng.uniform(0,1/3));M[leaf,p]=M[p,leaf]=x
                    x=float(b)*float(rng.uniform(0,1/3));M[p,p+1]=M[p+1,p]=x
                    for leaf in range(p+2,n):
                        x=float(c)*float(rng.uniform(0,1/3));M[leaf,p+1]=M[p+1,leaf]=x
                    np.fill_diagonal(M,1-M.sum(axis=1))
                    assert slem(M)+1e-9>=float(mu)
                    comparisons+=1
        else:
            # The candidate is *not* optimal: both active eigenbranches
            # decrease on lowering b along the two saturated hub constraints.
            eps=1e-6
            nb=float(b)-eps
            if nb>0:
                na=(1-nb)/p; nc=(1-nb)/q
                if p<=5 and q<=20:
                    assert slem(transition(p,q,na,nb,nc))<float(mu)-1e-9
                    negative+=1
print('characteristic_polynomial_checks',passed)
print('KKT_and_spectrum_cases',covered)
print('finite_improvement_cases',negative)
print('asymmetric_feasible_comparisons',comparisons)
for p,q in [(2,5),(2,6),(2,8),(3,8),(4,11),(10,25)]:
    a,b,c,mu,X,w2,D,H=data(p,q)
    print(f'p={p} q={q}: sign(H)={int(H>0)-int(H<0)}, a={a}, b={b}, c={c}, mu={mu}')
