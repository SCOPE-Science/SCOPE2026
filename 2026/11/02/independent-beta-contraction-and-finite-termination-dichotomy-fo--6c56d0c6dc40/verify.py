"""Reproduce exact algebraic and simulation checks for Gaussian-sketch RCGLS.
Scientific universal proofs are in RESULT.md; empirical checks do not certify infinite claims.
"""
from fractions import Fraction as F
from math import log
import numpy as np


def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def mv(H,x): return [dot(row,x) for row in H]
def scale(x,c): return [c*t for t in x]
def subtract(x,y): return [a-b for a,b in zip(x,y)]
def R(v): return [F(k) for k in v]
def rational_run(H, e, gs):
    e=R(e); H=[R(row) for row in H]; previous=None; hist=[e]
    for g in gs:
        g=R(g); hg=dot(g,mv(H,e))
        if previous is None:
            p=scale(g,hg)
        else:
            pp=dot(previous,mv(H,previous))
            assert pp!=0
            projection=subtract(g,scale(previous,dot(g,mv(H,previous))/pp))
            p=scale(projection,hg)
            assert dot(p,mv(H,previous))==0
            assert dot(e,mv(H,previous))==0
        den=dot(p,mv(H,p))
        if den==0:
            raise ArithmeticError('chosen exact rational sketch makes zero direction')
        alpha=dot(e,mv(H,p))/den
        e=subtract(e,scale(p,alpha))
        assert dot(e,mv(H,p))==0
        hist.append(e)
        previous=p
    return hist

# Exact rational checks, including a nonorthogonal two-column least-squares Hessian.
h2=[[4,2],[2,2]]
v2=rational_run(h2,[1,-2],[[1,3],[2,-1]])
assert v2[0]!=[F(0),F(0)] and v2[1]!=[F(0),F(0)] and v2[2]==[F(0),F(0)]
h3=[[4,2,0],[2,2,1],[0,1,2]]
# Its determinant is positive and its 2x2 leading principal minors are positive.
assert h3[0][0]>0 and h3[0][0]*h3[1][1]-h3[0][1]*h3[1][0]>0
v3=rational_run(h3,[1,-2,3],[[1,2,-1],[2,-1,1],[1,1,3],[2,3,-1]])
assert all(any(x!=0 for x in v) for v in v3)
print('exact_fraction_checks=2; d2_final_error=',v2[-1],'; d3_four_step_error=',v3[-1])

rng=np.random.default_rng(20261025)
max_two=0.0; trials=0
for _ in range(450):
    C=rng.normal(size=(2,2))
    H=C.T@C+np.eye(2)
    e=rng.normal(size=2)
    pprev=None
    for k in range(2):
        g=rng.normal(size=2)
        v=g @ H @ e
        p=g*v
        if pprev is not None:
            p-=pprev*((pprev@H@p)/(pprev@H@pprev))
        alpha=(e@H@p)/(p@H@p)
        e=e-alpha*p
        pprev=p
    max_two=max(max_two,np.linalg.norm(e))
    trials+=1
assert max_two<3e-12
print('d2_Gaussian_trials=',trials,'max_final_norm=',max_two)

# Isotropic Gaussian products: directly test conditional mean and two-step error law.
dims=[3,4,7,12]
for d in dims:
    count=10000
    e0=np.zeros((count,d));e0[:,0]=1.0
    e=e0.copy();prev=None
    ratios=[]
    for k in range(3):
        g=rng.normal(size=(count,d))
        if prev is None:
            u=g/np.linalg.norm(g,axis=1)[:,None]
        else:
            gp=np.einsum('ij,ij->i',g,prev)
            pp=np.einsum('ij,ij->i',prev,prev)
            proj=g-(gp/pp)[:,None]*prev
            u=proj/np.linalg.norm(proj,axis=1)[:,None]
        coeff=np.einsum('ij,ij->i',e,u)
        en=e-coeff[:,None]*u
        fac=np.einsum('ij,ij->i',en,en)/np.einsum('ij,ij->i',e,e)
        ratios.append(fac)
        e=en; prev=u
    obs0=float(ratios[0].mean()); obslate=[float(ratios[k].mean()) for k in (1,2)]
    expected0=(d-1)/d; expectedlate=(d-2)/(d-1)
    assert abs(obs0-expected0)<0.016
    assert all(abs(z-expectedlate)<0.016 for z in obslate)
    print('isotropic_d',d,'n',count,'E[factor0]',obs0,'target',expected0,'E[factor1,2]',obslate,'target',expectedlate)

# d=3 predicts an arcsine Beta(1/2,1/2) factor after the first step.
# Probability of contraction less than 1/2 equals 1/2 by symmetry.
print('total_model_paths=',4*10000,'universal_statements_checked_by_analytic_proof_only')
