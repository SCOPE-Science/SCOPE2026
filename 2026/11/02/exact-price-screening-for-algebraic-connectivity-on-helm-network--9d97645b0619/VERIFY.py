"""Finite independent checks of the spectral-gap formula on priced helm graphs.

Dependencies: Python 3, NumPy, SciPy, SymPy.
This tests instances; the infinite-family theorem rests on the proof in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize


def helm_laplacian(m, edge_weights):
    L = np.zeros((2*m+1, 2*m+1))
    for i in range(m):
        for a,b,w in ((0,1+i,edge_weights[3*i]),
                      (1+i,1+(i+1)%m,edge_weights[3*i+1]),
                      (1+i,1+m+i,edge_weights[3*i+2])):
            L[a,a] += w; L[b,b] += w
            L[a,b] -= w; L[b,a] -= w
    return L


def optimum(m,P,Q,R,B):
    c=2-2*math.cos(2*math.pi/m)
    alpha=Q/c
    if P <= alpha:
        Z=1+math.sqrt(P/R)
        X=2+1/(Z-1)
        Y=0.
    else:
        def D(z): return (2*m+1)*z-(m+1)
        def fprime(z):
            return R-alpha/(z-1)**2-(P-alpha)/D(z)**2
        Z=brentq(fprime,1+1e-9, 10+math.sqrt(P/R),xtol=1e-14)
        X=(2*Z-1)/D(Z)
        Y=(2+1/(Z-1)-X)/c
    C=P*X+Q*Y+R*Z
    scale=B/(m*C)
    return scale*np.array([X,Y,Z]),scale


def reduced_gap(m,x,y,z):
    c=2-2*math.cos(2*math.pi/m)
    s=x+c*y
    f=(s+2*z-math.sqrt(s*s+4*z*z))/2
    h=((m+1)*x+2*z-math.sqrt(((m+1)*x+2*z)**2-4*(2*m+1)*x*z))/2
    return min(f,h)


def check_symbolic():
    m,x,z,s,t=sp.symbols('m x z s t')
    H=sp.Matrix([[m*x,-m*x,0],[-x,x+z,-z],[0,-z,z]])
    F=sp.Matrix([[s+z,-z],[-z,z]])
    assert sp.simplify((t*sp.eye(3)-H).det()-t*(t*t-((m+1)*x+2*z)*t+(2*m+1)*x*z))==0
    assert sp.simplify((t*sp.eye(2)-F).det()-(t*t-(s+2*z)*t+s*z))==0
    # At six rim sites and unit prices, both endpoint designs use cost 30.
    for X,Y,Z in ((sp.Rational(3),sp.Rational(0),sp.Rational(2)),
                  (sp.Rational(3,19),sp.Rational(54,19),sp.Rational(2))):
        assert 6*(X+Y+Z)==30
        s=X+Y  # c_6 = 1
        assert (Z-1)*s-(2*Z-1)==0
        assert ((2*6+1)*Z-(6+1))*X-(2*Z-1)>=0


def check_direct():
    cases=0
    for m in range(3,15):
        for P,Q,R in ((1,1,1),(3,1,1),(1,3,1),(.4,1,2),
                      (5,2,.5),(1,2,5),(.1,3,2)):
            B=3*m
            (x,y,z),v=optimum(m,P,Q,R,B)
            L=helm_laplacian(m,[x,y,z]*m)
            direct=np.linalg.eigvalsh(L)[1]
            assert abs(direct-v)<4e-10,(m,P,Q,R,direct,v)
            assert abs(direct-reduced_gap(m,x,y,z))<4e-10
            assert abs(m*(P*x+Q*y+R*z)-B)<1e-9
            cases+=1
    return cases


def check_asymmetric():
    rng=np.random.default_rng(20261030)
    cases=0
    for m in (3,4,5,6):
        for P,Q,R in ((1,1,1),(.3,1,2),(2,1,1)):
            B=5*m
            (_,_,_),v=optimum(m,P,Q,R,B)
            costs=np.array([P,Q,R]*m)
            def objective(weights):
                return -np.linalg.eigvalsh(helm_laplacian(m,weights))[1]
            for _ in range(4):
                start=rng.uniform(.05,2,size=3*m)
                start*=B/np.dot(costs,start)
                res=minimize(objective,start,method='SLSQP',
                    bounds=[(0,None)]*(3*m),
                    constraints=[{'type':'eq','fun':lambda w:np.dot(costs,w)-B}],
                    options={'maxiter':200,'ftol':1e-9})
                # A local search cannot prove global optimality; it may only
                # reveal a counterexample to the analytic claimed bound.
                assert -res.fun <= v+2e-6,(m,P,Q,R,-res.fun,v)
                cases+=1
    return cases

if __name__=='__main__':
    check_symbolic()
    n=check_direct()
    k=check_asymmetric()
    print('PASS: two exact symbolic characteristic-polynomial identities')
    print('PASS: two exact rational six-cycle threshold allocations')
    print(f'PASS: {n} direct full-Laplacian spectrum, cost and gap cases')
    print(f'PASS: {k} asymmetric random-start nonlinear search comparisons')
    print('Finite tests do not certify all dimensions or unrestricted global optimality.')
