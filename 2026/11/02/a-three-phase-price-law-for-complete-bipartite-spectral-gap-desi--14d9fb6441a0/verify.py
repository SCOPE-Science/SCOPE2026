#!/usr/bin/env python3
"""Checks for a priced complete-bipartite spectral-gap allocation theorem.
Requires Python 3, NumPy, SymPy and SciPy. All runs are deterministic.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize

checks = 0

def check(cond, message):
    global checks
    checks += 1
    if not bool(cond):
        raise AssertionError(message)


def formula(p, m, P, Q):
    t = p-1
    beta = (m + 2*t + math.sqrt(m*m-4*t))/(2*t*(m+p))
    d = m*(m+p)*beta-(m+1)
    threshold = d*d
    ratio = P/Q
    if ratio < 1:
        a,b = 1-t/m, 1/m
        cost = (m-t)*P+t*Q
    elif ratio <= threshold:
        a,b = 1-t*beta, beta
        cost = m*(P*a+t*Q*b)
    else:
        a = (m+t+t/math.sqrt(ratio))/(m*(m+p))
        b = (m+1+math.sqrt(ratio))/(m*(m+p))
        cost = ((m+t)*P+t*(m+1)*Q+2*t*math.sqrt(P*Q))/(m+p)
    return a,b,cost,threshold,beta


def laplacian(p,m,a,b, symbolic=False):
    typ = object if symbolic else float
    L = sp.zeros(p+m) if symbolic else np.zeros((p+m,p+m),dtype=typ)
    for i in range(p):
        for j in range(m):
            v = a if i==0 else b
            u,w=i,p+j
            L[u,u]+=v;L[w,w]+=v;L[u,w]-=v;L[w,u]-=v
    return L

# Algebraic characteristic-polynomial factorization, evaluated with
# independent whole-matrix exact arithmetic rather than a quotient matrix.
z=sp.symbols('z')
for p in range(3,6):
    for m in range(p,p+3):
        for a,b in [(sp.Rational(1,3),sp.Rational(2,5)),
                    (sp.Rational(7,11),sp.Rational(5,8))]:
            L=laplacian(p,m,a,b,True)
            S=a+(p-1)*b
            T=(m+1)*a+(m+p-1)*b
            target= z*(z-S)**(m-1)*(z-m*b)**(p-2) * \
                    (z*z-T*z+m*(m+p)*a*b)
            check(sp.Poly(L.charpoly(z).as_expr()-target,z).is_zero,
                  ('spectrum',p,m,a,b))

# Independently verify the one-variable lower envelope and its derivatives
# as polynomial/rational identities.
m,t,b=sp.symbols('m t b',positive=True)
beta_den=m*(m+t+1)*b-(m+1)
g=((m+t)*b-1)/beta_den
check(sp.simplify(sp.diff(g,b)+t/beta_den**2)==0,'envelope derivative')
check(sp.simplify(sp.diff(g,b,2)-2*t*m*(m+t+1)/beta_den**3)==0,'envelope curvature')
f=sp.expand(m*(m+t+1)*(1-t*b)*b-(m+1)*(1-t*b)-(m+t)*b+1)
check(sp.simplify(f - m*(-t*(m+t+1)*b*b+(m+2*t)*b-1))==0,'intersection quadratic')
check(sp.simplify(f.subs(b,1/m)-t*(m-t-1)/m)==0,'left boundary condition')

# Whole-graph eigenvalue tests and independent one-variable numerical
# constrained minimization. These are finite consistency checks, not proof.
ratios = (0.02,0.3,0.99,1.0,1.01,2.0,4.0,16.0,100.0,1e4,1e8)
for p in range(3,9):
    for m0 in range(p,p+5):
        for r in ratios:
            a,b,c,R,beta=formula(p,m0,r,1)
            spectrum=np.linalg.eigvalsh(laplacian(p,m0,a,b))
            check(abs(spectrum[1]-1)<5e-8,('gap',p,m0,r,spectrum[:4]))
            check(min(a,b)>0,('positive',p,m0,r))
            check(abs(m0*(r*a+(p-1)*b)-c)<1e-7*max(1,c),('cost',p,m0,r))
            check(R >= (p-1)**2-1e-8,('threshold',p,m0))
            check(beta >= 1/m0-1e-9,('beta lower',p,m0))

successful_optimizations=0
for p in range(3,6):
    for m0 in range(p,p+3):
        for r in (0.25,1.0,2.0,20.0,10000.0):
            a,b,c,_,_=formula(p,m0,r,1)
            def small_gap(x):
                return np.linalg.eigvalsh(laplacian(p,m0,x[0],x[1]))[1]-1
            def objective(x):
                return m0*(r*x[0]+(p-1)*x[1])
            opt=minimize(objective,(a*1.1,b*1.1),method='SLSQP',
                         bounds=((0,None),(0,None)),
                         constraints=({'type':'ineq','fun':small_gap},),
                         options={'ftol':1e-11,'maxiter':300})
            if opt.success:
                successful_optimizations += 1
                check(opt.fun >= c-1e-5*max(1,c),('optimization',p,m0,r,opt.fun,c))
check(successful_optimizations>=25,('numerical optimizers',successful_optimizations))

# Exact phase joins for square dimensions p=m: R=(p-1)^2,
# while the off-diagonal price-asymptotic threshold scales as m^4/(p-1)^2.
for p in range(3,10):
    _,_,_,R,beta=formula(p,p,1,1)
    check(abs(R-(p-1)**2)<1e-8,('balanced threshold',p))
    check(abs(beta-1/p)<1e-9,('balanced join',p))
for p in (3,4,5):
    m0=10000
    _,_,_,R,_=formula(p,m0,1,1)
    check(abs(R*(p-1)**2/m0**4-1)<0.002,('large m',p))
print(f'PASS: {checks} deterministic assertions; {successful_optimizations} independent numeric optimizations')
