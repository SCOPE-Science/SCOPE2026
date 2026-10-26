#!/usr/bin/env python3
"""Reproducible finite checks of exact spectral-gap allocation formulas."""
import math
import numpy as np
from scipy.optimize import minimize


def edge_list(m):
    # labels: terminal U=0, V=1, a_i=2+2i, b_i=3+2i
    edges=[(0,1,'short')]
    for i in range(m):
        a,b=2+2*i,3+2*i
        edges.extend([(0,a,'outer'),(a,b,'middle'),(b,1,'outer')])
    return edges

def laplacian(m,weights):
    L=np.zeros((2+2*m,2+2*m))
    for (u,v,_),w in zip(edge_list(m),weights):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    return L

def gap(m,weights):
    return float(np.linalg.eigvalsh(laplacian(m,weights))[1])

def closed(m,tau,B=1.0):
    tc=(m/(m-1))**2
    if tau<=tc:
        C=2*m+m*math.sqrt(tau)+(1-m)*tau/2
        lam=B/C
        x=lam; y=lam*math.sqrt(tau)/2
        z=lam*(1+m*(1/math.sqrt(tau)-1))/2
    else:
        C=2*m+m*m/(2*(m-1))
        lam=B/C
        x=lam; y=lam*m/(2*(m-1));z=0.
    w=[z]
    for i in range(m):w.extend((x,y,x))
    return lam, w, (x,y,z), C

def tests():
    rng=np.random.default_rng(20261024)
    cases=0; random_tests=0; local_tests=0
    max_eig=0.;max_budget=0.;max_random_over=-1e9;max_local_over=-1e9
    for m in range(2,11):
        tc=(m/(m-1))**2
        for tau in sorted(set([.01,.15,.7,1.,1.25,tc*.99,tc,tc*1.01,2*tc,100.])):
            B=1.0
            expected,w,(x,y,z),C=closed(m,tau,B)
            costs=np.array([tau if label=='short' else 1. for _,_,label in edge_list(m)])
            eig=gap(m,w)
            bud=float(np.dot(w,costs))
            max_eig=max(max_eig,abs(eig-expected))
            max_budget=max(max_budget,abs(bud-B))
            assert abs(eig-expected) < 5e-12,(m,tau,eig,expected)
            assert abs(bud-B)<5e-12,(m,tau,bud)
            for _ in range(100):
                prop=rng.dirichlet(np.ones(len(w)))
                wr=prop/(costs@prop)
                measured=gap(m,wr)
                max_random_over=max(max_random_over,measured-expected)
                assert measured <= expected+1e-10,(m,tau,measured,expected)
                random_tests+=1
            cases+=1
            if m<=5 and tau in (1.,tc,100.):
                ww=np.array(w,dtype=float)
                x0=ww+1e-5*rng.standard_normal(len(w));x0=np.maximum(0.,x0)
                x0=x0/(costs@x0)
                def objective(q):
                    return -gap(m,q)
                res=minimize(objective,x0,method='SLSQP',bounds=[(0,None)]*len(w),constraints=[{'type':'eq','fun':lambda q,c=costs:c@q-1}],options={'maxiter':1000,'ftol':1e-12})
                assert res.success,(res.message,m,tau)
                meas=-res.fun
                max_local_over=max(max_local_over,meas-expected)
                assert meas<expected+1e-7,(m,tau,meas,expected)
                local_tests+=1
    print('cases',cases,'random_asymmetric',random_tests,'numerical_optimizations',local_tests)
    print('max_abs_eigenvalue_discrepancy',f'{max_eig:.3e}')
    print('max_abs_budget_discrepancy',f'{max_budget:.3e}')
    print('largest_random_minus_theorem',f'{max_random_over:.6e}')
    print('largest_local_minus_theorem',f'{max_local_over:.6e}')
    print('FINITE_TESTS_PASS')
if __name__=='__main__':tests()
