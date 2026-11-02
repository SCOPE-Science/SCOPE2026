"""Exact symbolic and independent numerical tests for the shifted two-column ridge sketch example.

Run from this directory: python verify.py
Requires: Python 3, NumPy and SymPy. Calculations test the proof's identities,
not a computer enumeration of every real parameter.
"""
from fractions import Fraction as Q
import math
import numpy as np
import sympy as sp

x, t = sp.symbols('x t', real=True)
G = sp.diag(4, 1)
D = sp.Matrix([[5, sp.Rational(1, 4)], [sp.Rational(1, 4), 2]])
assert D.det() == sp.Rational(159, 16)
U = (x + 4) * (x + 1)
P = 37 * x**2 - 67*x + 40
W = 2 * U + t*(7*x+13)
F = 148*x**3 - 402*x**2 - (942+1431*t)*x + (1336+1431*t)
assert sp.expand(sp.diff(P,x)*W - 2*P*sp.diff(W,x) + F)==0
assert sp.discriminant(P,x)==-1431
assert sp.expand(F.subs(x,0))==1336+1431*t
assert sp.expand(F.subs(x,1))==140
assert sp.expand(F.subs(x,2))==-972-1431*t

# Direct generalized singular values: K(B R^-1), not only the symbolic formula.
A = np.array([[2.,0.],[0.,1.],[0.,0.],[0.,0.],[0.,0.],[0.,0.]])
Gf = A.T @ A
Df = np.array(D,float)
assert np.allclose(Gf, np.array(G,float))
assert np.min(np.linalg.eigvalsh(Df))>0

# Explicit realizing sketch: (X A)^T X A = G+tD.
def realization(tt):
    H = Gf + tt*Df
    # As the first two A rows are diag(2,1), choose X_{:,1:2} = chol(H).T diag(1/2,1).
    X = np.zeros((2,A.shape[0]))
    X[:,:2] = np.linalg.cholesky(H).T @ np.diag([.5,1.])
    assert np.allclose((X@A).T@(X@A),H,rtol=1e-13,atol=1e-13)
    return X,H

def direct_condition(tt,ll):
    X,H = realization(tt)
    R=np.linalg.cholesky(H+ll*np.eye(2)).T
    B=np.vstack([A, math.sqrt(ll)*np.eye(2)])
    return float(np.linalg.cond(B@np.linalg.inv(R)))

def analytic_condition(tt,ll):
    uu=(ll+4)*(ll+1)
    pp=37*ll*ll-67*ll+40
    ww=2*uu+tt*(7*ll+13)
    return math.sqrt((ww+tt*math.sqrt(pp)/2)/(ww-tt*math.sqrt(pp)/2))

checks=0
for tt in [0.005,0.01,0.1,0.5,1,2,5,10]:
    roots=sorted(float(sp.re(r)) for r in sp.nroots(F.subs(t,sp.Rational(str(tt))),maxsteps=200) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>0)
    assert len(roots)==2 and 1<roots[0]<2<roots[1]
    sample=[0.,.1,.8,1.,(1+roots[0])/2,roots[0],(roots[0]+roots[1])/2,roots[1],roots[1]+1,20,100]
    for ll in sample:
        observed=direct_condition(tt,ll)
        expected=analytic_condition(tt,ll)
        assert math.isclose(observed,expected,rel_tol=1e-10,abs_tol=1e-12),(tt,ll,observed,expected)
        checks+=1
    delta=min(.0001, .02*(roots[1]-roots[0]))
    assert analytic_condition(tt,roots[0]-delta)>analytic_condition(tt,roots[0])
    assert analytic_condition(tt,roots[0]+delta)>analytic_condition(tt,roots[0])
    assert analytic_condition(tt,roots[1]-delta)<analytic_condition(tt,roots[1])
    assert analytic_condition(tt,roots[1]+delta)<analytic_condition(tt,roots[1])
    checks+=4

# Analytic Gram-distortion verification: exactly t G^{-1/2}D G^{-1/2}.
M = np.diag([.5,1.]) @ Df @ np.diag([.5,1.])
for tt in [.000001,.001,.01,.1]:
    _,H=realization(tt)
    distortion=np.linalg.norm(np.diag([.5,1.])@(H-Gf)@np.diag([.5,1.]),2)
    assert math.isclose(distortion,tt*np.linalg.norm(M,2),rel_tol=2e-9,abs_tol=1e-14)
    checks+=1

# Direct finite difference sign versus polynomial at noncritical points.
for tt in [.01,.1,1.]:
    for ll in [0.01,.2,.9,1.0,1.5,2.0,3.0,4.0,8.0,20.0]:
        fval=float(F.subs({t:sp.Rational(str(tt)),x:sp.Rational(str(ll))}))
        if abs(fval)<.01: continue
        eps=1e-5
        derivative=(analytic_condition(tt,ll+eps)-analytic_condition(tt,ll-eps))/(2*eps)
        if abs(derivative)>1e-9:
            assert derivative*fval<0,(tt,ll,derivative,fval)
            checks+=1
print(f'PASS: {checks} independent matrix/derivative/distortion comparisons, plus exact polynomial identities')
