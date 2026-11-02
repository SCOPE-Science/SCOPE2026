#!/usr/bin/env python3
"""Reproduce exact spectra, cost transitions, and independent numerical checks.

Requires Python 3, sympy, numpy, scipy. Run: python verify.py
"""
from fractions import Fraction
import math
import numpy as np
import sympy as s
from scipy.optimize import minimize


def normalized_solution(k, P, Q, R):
    # All prices and target gap are positive. Return rates with target gap 1.
    if R >= k*k*P:
        a=(2+math.sqrt(R/P))/(k+2)
        b=0.
        phase='pendant-expensive'
    elif Q >= 2*(k*k*P-R)/(k*(k-1)):
        a=1.
        b=0.
        phase='internal-edges-deleted'
    else:
        D=k*P-(k-1)*Q/2
        a=(2+math.sqrt(k*R/D))/(k+2)
        b=(1-a)/k
        phase='all-edges-active'
    c=((k+1)*a-1)/((k+2)*a-2)
    cost=k*P*a+(k*(k-1)/2)*Q*b+R*c
    return a,b,c,cost,phase


def edge_data(k,P,Q,R):
    E=[(0,i) for i in range(1,k+1)]
    E += [(i,j) for i in range(1,k+1) for j in range(i+1,k+1)]
    E += [(0,k+1)]
    return E,np.array([P]*k+[Q]*(k*(k-1)//2)+[R],float)


def laplacian(k,edges,weights,dtype=float):
    M=np.zeros((k+2,k+2),dtype=dtype)
    for (i,j),w in zip(edges,weights):
        M[i,i]+=w;M[j,j]+=w;M[i,j]-=w;M[j,i]-=w
    return M


def symbolic_spectra():
    a,b,c,z=s.symbols('a b c z')
    for k in range(2,7):
        edges,_=edge_data(k,1,1,1)
        w=[a]*k+[b]*(k*(k-1)//2)+[c]
        L=s.zeros(k+2)
        for (i,j),v in zip(edges,w):
            L[i,i]+=v; L[j,j]+=v;L[i,j]-=v;L[j,i]-=v
        expression=s.factor(L.charpoly(z).as_expr())
        expected=z*(z-a-k*b)**(k-1)*(z*z-(2*c+(k+1)*a)*z+(k+2)*a*c)
        assert s.expand(expression-expected)==0, ('spectrum',k)
    return 5


def exact_cases():
    cases=[(3,s.Rational(1),s.Rational(1),s.Rational(2,3),s.Rational(3,5),s.Rational(2,15),s.Rational(7,5)),
           (3,s.Rational(1),s.Rational(4),s.Rational(2),s.Rational(1),s.Rational(0),s.Rational(1)),
           (3,s.Rational(1),s.Rational(2),s.Rational(16),s.Rational(6,5),s.Rational(0),s.Rational(19,20))]
    for k,P,Q,R,a,b,c in cases:
        ed,_=edge_data(k,float(P),float(Q),float(R))
        L=s.zeros(k+2)
        for (i,j),v in zip(ed,[a]*k+[b]*(k*(k-1)//2)+[c]):
            L[i,i]+=v;L[j,j]+=v;L[i,j]-=v;L[j,i]-=v
        eigenvals=L.eigenvals()
        assert min([ev for ev in eigenvals if ev!=0])==1,(k,P,Q,R,eigenvals)
        total=k*P*a+(k*(k-1)//2)*Q*b+R*c
        pred=normalized_solution(k,float(P),float(Q),float(R))
        assert abs(float(total)-pred[3])<1e-10
    return len(cases)


def unconstrained_numerics():
    rng=np.random.default_rng(123)
    successful=0
    for k in (2,3,4,5):
        for P,Q,R in ((1,.1,.2),(1,1,2),(1,3,2),(1,2,20),(.5,2,5)):
            ed,prices=edge_data(k,P,Q,R)
            a,b,c,C,phase=normalized_solution(k,P,Q,R)
            candidate=np.array([a]*k+[b]*(k*(k-1)//2)+[c])/C
            eig=np.linalg.eigvalsh(laplacian(k,ed,candidate))[1]
            assert abs(eig-1/C)<1e-9
            # Independent, edgewise-unconstrained nonnegative allocations.
            def neg_gap(x):return -np.linalg.eigvalsh(laplacian(k,ed,x))[1]
            for init in (candidate,rng.dirichlet(np.ones(len(ed)))/prices):
                optimum=minimize(neg_gap,init,method='SLSQP',bounds=[(0,None)]*len(ed),
                                 constraints=[{'type':'eq','fun':lambda x:float(1-prices@x)}],
                                 options={'ftol':1e-11,'maxiter':500})
                assert -optimum.fun <= 1/C+1e-7,(k,P,Q,R,-optimum.fun,1/C)
                successful+=1
    return successful


def boundary_checks():
    for k in range(2,8):
        P=1.0
        for R in (0.2*k*k,0.75*k*k):
            Qcrit=2*(k*k*P-R)/(k*(k-1))
            for q in (Qcrit*(1-1e-7),Qcrit,Qcrit*(1+1e-7)):
                a,b,c,C,ph=normalized_solution(k,P,q,R)
                assert 2/(k+2)<a+1e-10 and b>=-1e-10 and abs((k+2)*a*c-2*c-(k+1)*a+1)<1e-7
        for R in (k*k*(1-1e-7),k*k,k*k*(1+1e-7)):
            a,b,c,C,ph=normalized_solution(k,P,3,R)
            assert abs((k+2)*a*c-2*c-(k+1)*a+1)<1e-7
    return 54


if __name__=='__main__':
    print('SYMBOLIC_SPECTRA',symbolic_spectra())
    print('EXACT_RATIONAL_REGIMES',exact_cases())
    print('PHASE_BOUNDARY_CHECKS',boundary_checks())
    print('UNRESTRICTED_NUMERICAL_CHECKS',unconstrained_numerics())
    print('ALL CHECKS PASSED (numerical checks are supplementary)')
