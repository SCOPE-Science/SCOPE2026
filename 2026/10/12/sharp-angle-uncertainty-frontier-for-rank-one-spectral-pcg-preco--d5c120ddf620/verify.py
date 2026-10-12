"""Reproducibility checks for a robust two-mode rank-one PCG preconditioner.
Run: python verify.py  (needs numpy). Analytical proofs are in RESULT.md.
"""
from fractions import Fraction as Q
import math
import numpy as np

def factor(r,q,t):
    tr=q+r+(1-q)*(1-r)*t
    return 1-4*r*q/(tr*tr)

def robust(r,T):
    if T < .5:
        q=(r+(1-r)*T)/(1-(1-r)*T)
        H=(1-r)**2*T*(1-T)
        return q,H/(r+H)
    return 1,((1-r)/(1+r))**2

# Exact rational identities: entries of F in A eigenbasis, trace,
# determinant, endpoint objective, and the closed-form minimax value.
checks=0
for ir in range(1,14):
    r=Q(ir,17)
    for iq in range(1,17):
        q=Q(iq,11)
        for it in range(0,18):
            t=Q(it,17)
            f11=1+(q-1)*(1-t)
            f22=1+(q-1)*t
            cross_square=(q-1)**2*t*(1-t)
            assert f11*f22-cross_square==q
            direct_trace=f11+ r*f22
            want_trace=q+r+(1-q)*(1-r)*t
            assert direct_trace==want_trace
            det_B=r*(f11*f22-cross_square)
            assert det_B==r*q
            assert want_trace*want_trace>=4*det_B
            checks+=1
for ir in range(1,14):
    r=Q(ir,17)
    for it in range(0,18):
        T=Q(it,17)
        if T < Q(1,2):
            q=(r+(1-r)*T)/(1-(1-r)*T)
            h=(1-r)**2*T*(1-T)
            optimum=h/(r+h)
        else:
            q=Q(1)
            optimum=((1-r)/(1+r))**2
        vals=[factor(r,q,Q(0)),factor(r,q,T)]
        assert max(vals)==optimum
        for iq in range(1,51):
            alternative=Q(iq,31)
            assert max(factor(r,alternative,Q(0)),factor(r,alternative,T))>=optimum
            checks+=1

# Independent matrix eigenspectrum calculation and explicit first PCG step:
# for the optimal error weights, the computed energy loss attains the bound.
rng=np.random.default_rng(20261010)
num_cases=0
for _ in range(2400):
    r=float(np.exp(rng.uniform(math.log(0.005),math.log(0.95))))
    q=float(np.exp(rng.uniform(math.log(0.005),math.log(2.5))))
    t=float(rng.uniform(0,1))
    v=np.array([np.sqrt(1-t),np.sqrt(t)])
    A=np.diag([1.,r])
    F=np.eye(2)+(q-1)*np.outer(v,v)
    eigF,U=np.linalg.eigh(F)
    sqrtF=(U*np.sqrt(eigF))@U.T
    B=sqrtF@A@sqrtF
    lambdas,Z=np.linalg.eigh(B)
    actual=((lambdas[1]-lambdas[0])/(lambdas[1]+lambdas[0]))**2
    stated=factor(r,q,t)
    assert abs(actual-stated)<2.e-12,(actual,stated)
    # In transformed coordinates y0, enforce sharp Kantorovich weights.
    la,lb=lambdas[1],lambdas[0]
    ya=math.sqrt(lb/(la*(la+lb)))
    yb=math.sqrt(la/(lb*(la+lb)))
    y0=Z@np.array([yb,ya])
    e0=sqrtF@y0
    res=A@e0
    p=F@res
    alpha=(res@p)/(p@A@p)
    e1=e0-alpha*p
    observed=(e1@A@e1)/(e0@A@e0)
    assert abs(observed-stated)<1.e-11,(observed,stated)
    num_cases+=1

# Robust q global minimax: numerical compare including angles inside bound.
robust_cases=0
for _ in range(850):
    r=float(rng.uniform(.002,.999))
    T=float(rng.uniform(0,1))
    q_opt,loss=robust(r,T)
    assert abs(max(factor(r,q_opt,0),factor(r,q_opt,T))-loss)<1e-12
    for alternate in (np.exp(rng.uniform(-9,7)) for _ in range(15)):
        worst=max(factor(r,alternate,0),factor(r,alternate,T))
        assert worst+1e-12>=loss,(r,T,q_opt,alternate,loss,worst)
    robust_cases+=1

# Nominal scale threshold and asymptotic scaling assertions.
for r in (.0001,.01,.1,.25,.81):
    threshold=math.sqrt(r)/(1+math.sqrt(r))**2
    baseline=factor(r,1,0)
    assert abs(factor(r,r,threshold)-baseline)<1e-12
    assert factor(r,r,threshold*.9)<baseline
    assert factor(r,r,threshold*1.1)>baseline
for c in (.1,1,4):
    vals=[]
    for r in (1e-5,1e-6,1e-7):
        _,loss=robust(r,c*r)
        vals.append(loss)
    assert abs(vals[-1]-c/(1+c))<2e-6,(c,vals)
print('VERIFY_OK rational_matrix_and_minimax_identities=',checks)
print('VERIFY_OK independent_eigensystem_and_worst_PCG_cases=',num_cases)
print('VERIFY_OK robust_minimax_sample_cases=',robust_cases)
print('VERIFY_OK exact_nominal_safety_threshold_and_small_curvature_limits=1')
