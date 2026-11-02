"""Reproducibility checks for a thermal dimer's joint pinning/friction budget optimum.

Dependencies: Python 3, numpy, scipy, sympy.
The paper's universal statements rely on its analytical proof, not finite tests.
"""
import math
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import minimize_scalar
import sympy as sp


def current_formula(k, a, b, g, h, TL=2.0, TR=1.0):
    G, prod = g+h, g*h
    den = (a-b)**2 + G*(a*h+b*g) + k*G**2 + k**2*G**2/prod
    return k**2*G*(TL-TR)/den


def current_lyapunov(k, a, b, g, h, TL=2.0, TR=1.0):
    A = np.array([[0,0,1,0], [0,0,0,1],
                  [-a-k,k,-g,0], [k,-b-k,0,-h]], dtype=float)
    Q = np.diag([0,0,2*g*TL,2*h*TR])
    cov = solve_continuous_lyapunov(A, -Q)
    assert np.linalg.norm(A@cov + cov@A.T + Q) < 1e-7
    return g*(TL-cov[2,2])


def budget_current(k, P, G, delta, eta):
    a, b = (P+delta)/2, (P-delta)/2
    g, h = G*(1-eta)/2, G*(1+eta)/2
    return current_formula(k,a,b,g,h)


def theoretical_optimum(k,P,G):
    if G*G <= 8*k:
        return (0.0,0.0,'balanced')
    r0 = math.sqrt(1-8*k/G**2)
    d0 = G*G*r0/4
    if P >= d0:
        return (-d0,r0,'interior')
    def root_fn(r): return 8*k*k*r/(1-r*r)**2 - G*G*P/2
    from scipy.optimize import brentq
    r = brentq(root_fn, 1e-14, 1-1e-12)
    return (-P,r,'boundary')


def main():
    # Independent symbolic covariance check at a nontrivial rational parameter point.
    kk, aa, bb, gg, hh = map(sp.Rational, ['3/2','2/3','5/4','7/3','4/5'])
    T1,T2=sp.Rational(13,4),sp.Rational(3,5)
    A=sp.Matrix([[0,0,1,0],[0,0,0,1],[-aa-kk,kk,-gg,0],[kk,-bb-kk,0,-hh]])
    s=sp.symbols('s0:10'); C=sp.zeros(4);n=0
    for i in range(4):
        for j in range(i,4): C[i,j]=C[j,i]=s[n];n+=1
    Q=sp.diag(0,0,2*gg*T1,2*hh*T2)
    eq=(A*C+C*A.T+Q)
    sol=sp.solve([eq[i,j] for i in range(4) for j in range(i,4)],s)
    exact=sp.factor(gg*(T1-sol[C[2,2]]))
    G=gg+hh
    expect=sp.factor(kk**2*G*(T1-T2)/((aa-bb)**2+G*(aa*hh+bb*gg)+kk*G**2+kk**2*G**2/(gg*hh)))
    assert exact == expect, (exact,expect)
    print('Exact rational 4x4 covariance check: PASS')

    rng = np.random.default_rng(20261026)
    for i in range(600):
        k,a,b,g,h=np.exp(rng.uniform(-2,2,size=5))
        if i%8==0: a=0.0
        if i%11==0: b=0.0
        if a==0 and b==0: b=0.5
        TL,TR = rng.uniform(.1,4),rng.uniform(.1,4)
        j1=current_formula(k,a,b,g,h,TL,TR)
        j2=current_lyapunov(k,a,b,g,h,TL,TR)
        assert abs(j1-j2) < 1.2e-8 * max(1,abs(j1)),(i,j1,j2)
    print('Independent floating-point Lyapunov comparisons: 600 PASS')

    for i in range(180):
        k=float(np.exp(rng.uniform(-1.5,1.5)))
        G=float(np.sqrt(8*k)*np.exp(rng.uniform(-.6,.8)))
        P=float(np.exp(rng.uniform(-1.5,2)))
        delta,eta,kind=theoretical_optimum(k,P,G)
        jtheory=budget_current(k,P,G,delta,eta)
        # Globally optimize a one-dimensional expression after exact minimization over delta.
        def neg_j(r):
            d=-min(G*G*r/4,P)
            return -budget_current(k,P,G,d,r)
        numeric=minimize_scalar(neg_j,bounds=(0,.99999999),method='bounded',options={'xatol':1e-12})
        assert jtheory >= -numeric.fun-1e-8*max(1,jtheory),(i,k,G,P,delta,eta,numeric.x)
        assert jtheory >= budget_current(k,P,G,0,0) - 1e-10
        assert abs(budget_current(k,P,G,delta,eta)-budget_current(k,P,G,-delta,-eta)) < 1e-11
        if kind=='balanced': assert delta == eta == 0.0
        if kind=='boundary': assert abs(delta+P)<1e-12
        if kind=='interior': assert abs(delta+G*G*eta/4)<1e-10
    print('Closed optimizer versus independent bounded scalar optimization: 180 PASS')

    k,G,P=1.0,4.0,3.0
    delta,eta,kind=theoretical_optimum(k,P,G)
    assert kind=='interior'
    assert abs(delta+2*math.sqrt(2))<1e-12
    assert abs(eta-1/math.sqrt(2))<1e-12
    assert abs(budget_current(k,P,G,delta,eta)-.1)<1e-12
    assert abs(budget_current(k,P,G,0,0)-1/11)<1e-12
    print('Exact-parameter witness k=1,P=3,G=4: 1/10 versus 1/11 PASS')

if __name__=='__main__': main()
