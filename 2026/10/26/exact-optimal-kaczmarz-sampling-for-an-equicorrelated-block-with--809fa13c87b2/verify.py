"""Reproduce the exact one-defect correlated-row Kaczmarz design checks.

Run with Python 3 and numpy, scipy and sympy. Finite checks supplement,
not replace, the analytic proof of the optimization theorem.
"""
import math
from fractions import Fraction
import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import minimize
import sympy as sp

COUNT={'spectral':0,'sampled':0,'optimized':0,'exact':0}

def design(m,alpha,beta):
    eta=1-alpha
    a=alpha+eta/m
    beta_crit=(math.hypot(eta,2*m*math.sqrt(alpha))-eta)/(2*m)
    if beta <= beta_crit+1.e-13:
        den=m*(alpha-beta*beta)+alpha*eta
        q=(alpha-beta*beta)/den
        r=alpha*eta/den
        t=eta*q
        regime='contrast'
    else:
        den=1+a+2*beta
        q=(1+beta)/(m*den)
        r=(a+beta)/den
        t=(a-beta*beta)/den
        regime='coupled'
    return q,r,t,beta_crit,regime

def gram(m,alpha,beta):
    g=np.eye(m+1)
    g[:m,:m] += alpha*(np.ones((m,m))-np.eye(m))
    g[:m,m]=beta
    g[m,:m]=beta
    return g

def min_eigen(g,p):
    root=np.sqrt(np.maximum(p,0.))
    return float(eigvalsh(g*root[:,None]*root[None,:])[0])

cases=[]
for m in [2,3,4,5,7,9]:
    for alpha in [.05,.125,.4,.75,.95]:
        crit=design(m,alpha,0.)[3]
        limit=math.sqrt(alpha+(1-alpha)/m)
        vals=[0.,alpha/2,alpha,(alpha+crit)/2,crit,(crit+math.sqrt(alpha))/2,math.sqrt(alpha),(math.sqrt(alpha)+limit)/2,.99*limit]
        for beta in vals:
            g=gram(m,alpha,beta)
            assert eigvalsh(g)[0]>1.e-12
            q,r,t,bc,regime=design(m,alpha,beta)
            p=np.array([q]*m+[r])
            assert min(q,r)>0 and abs(p.sum()-1)<5e-13
            eig=min_eigen(g,p)
            assert abs(eig-t)<3e-12,(m,alpha,beta,eig,t)
            eta=1-alpha
            a=alpha+eta/m
            zeta=((a*(1-r)+r)-math.sqrt((a*(1-r)-r)**2+4*beta*beta*r*(1-r)))/2
            assert abs(min(eta*q,zeta)-t)<3e-12
            cases.append((m,alpha,beta,g,p,t))
            COUNT['spectral']+=1
rng=np.random.default_rng(243891)
for m,alpha,beta,g,p,t in cases:
    for _ in range(24):
        x=rng.dirichlet(np.ones(m+1)*rng.uniform(.25,3))
        assert min_eigen(g,x)<=t+2.e-10,(m,alpha,beta,min_eigen(g,x),t)
        COUNT['sampled']+=1

# Independently optimize all probabilities (not restricted to the symmetric class).
for m,alpha,beta,g,p,t in [z for z in cases if z[0]<=4][::13]:
    out=minimize(lambda x:-min_eigen(g,x),
                 rng.dirichlet(np.ones(m+1)),
                 method='SLSQP',bounds=[(0.,1.)]*(m+1),
                 constraints=[{'type':'eq','fun':lambda x:x.sum()-1}],
                 options={'ftol':1e-13,'maxiter':750})
    assert out.success,(m,alpha,beta,out.message)
    assert abs(-out.fun-t)<2e-4,(m,alpha,beta,-out.fun,t)
    COUNT['optimized']+=1

# Rational arithmetic: characteristic-polynomial factors of the Gram law.
x=sp.symbols('x')
for m,al,be in [(3,sp.Rational(1,4),sp.Rational(1,8)),
                 (3,sp.Rational(1,4),sp.Rational(1,2)),
                 (2,sp.Rational(1,4),sp.Rational(1,4)),
                 (4,sp.Rational(2,5),sp.Rational(1,5)),
                 (3,sp.Rational(1,4),sp.Rational(7,10))]:
    A=sp.eye(m+1)
    for i in range(m):
        for j in range(m):
            if i!=j: A[i,j]=al
        A[i,m]=be
        A[m,i]=be
    eta=1-al
    a=al+eta/m
    crit=(sp.sqrt(eta**2+4*m**2*al)-eta)/(2*m)
    if be <= crit:
        den=m*(al-be*be)+al*eta
        q=(al-be*be)/den
        r=al*eta/den
        target=eta*q
    else:
        den=1+a+2*be
        q=(1+be)/(m*den)
        r=(a+be)/den
        target=(a-be*be)/den
    P=sp.diag(*([q]*m+[r]))
    cp=sp.factor((A*P).charpoly(x).as_expr())
    expected=sp.factor((x-eta*q)**(m-1)*
                       (x*x-(1+(m-1)*al)*q*x-r*x+
                        ((1+(m-1)*al)-m*be*be)*q*r))
    assert sp.simplify(cp-expected)==0,(m,al,be)
    assert sp.simplify(cp.subs(x,target))==0,(m,al,be)
    COUNT['exact']+=1

# Algebraic tangent certificate: determinant of the two-dimensional
# coupled-mode matrix minus its globally optimal lower eigenvalue.
a,b,z=sp.symbols('a b z',real=True)
d=1+a+2*b
ell=(a-b**2)/d
f=(a-b**2)*z*(1-z)-ell*(a*(1-z)+z)+ell**2
assert sp.factor(f+(a-b**2)*(z-(a+b)/d)**2)==0
COUNT['exact']+=1
print('PASS',COUNT)
print('Uniform row probabilities optimal only when exceptional coherence equals common coherence.')
