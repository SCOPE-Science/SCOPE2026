"""Independent numerical and symbolic checks for the priced three-part network theorem.

Requirements: numpy, scipy, sympy. Execute: python verify.py
Checks corroborate; the infinite-family argument is mathematical, not computational.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize

checks=0

def assert_close(a,b,atol=3e-8):
    global checks
    assert abs(a-b) <= atol*max(1,abs(a),abs(b)), (a,b)
    checks+=1

m,t,r=sp.symbols('m t r', positive=True)
a=(3*m-1)/2;b=6*(m-1);c=sp.Integer(3)
g=a+b/(1+t)+c/(1+2*t)
f=(2+r*t)*g
D=sp.diff(f,t)
target=r*a+b*(r-2)/(1+t)**2+c*(r-4)/(1+2*t)**2
assert sp.simplify(D-target)==0
checks+=1
rc=24*m/(15*m-7)
assert sp.simplify(D.subs(t,0).subs(r,rc))==0
assert sp.simplify(D.subs({r:sp.Rational(8,5),t:0})+sp.Rational(28,5))==0
assert sp.simplify(sp.diff(D,t).subs({r:sp.Rational(8,5),t:0})-sp.Rational(24,5)*(m+5))==0
checks+=3


def laplacian(n,x,y):
    N=3*n
    L=np.zeros((N,N),float)
    for i in range(N):
        for j in range(i+1,N):
            u,v=i//n,j//n
            if u==v: continue
            w=y if {u,v}=={0,2} else x
            L[i,i]+=w;L[j,j]+=w
            L[i,j]-=w;L[j,i]-=w
    return L

def K_formula(n,x,y):
    return 6*(n-1)/(x+y)+(3*n-1)/(2*x)+3/(x+2*y)

def eigenvalues_formula(n,x,y):
    return np.sort(np.array([0]+[n*(x+y)]*(2*(n-1))+[2*n*x]*(n-1)+[n*(x+2*y),3*n*x],float))

for n in range(2,10):
    for xx,yy in ((1,1),(0.25,2),(4,0),(2.5,.5),(.125,.3)):
        L=laplacian(n,xx,yy)
        eig=np.linalg.eigvalsh(L)
        for actual,want in zip(eig,eigenvalues_formula(n,xx,yy)):
            assert_close(actual,want)
        assert_close((3*n)*sum(1/eig[1:]),K_formula(n,xx,yy))
        W=np.linalg.pinv(L,hermitian=True)
        resist_sum=sum(W[i,i]+W[j,j]-2*W[i,j] for i in range(3*n) for j in range(i+1,3*n))
        assert_close(resist_sum,K_formula(n,xx,yy))


def derivative(n,price,tval):
    return (price*(3*n-1)/2+6*(n-1)*(price-2)/(1+tval)**2+3*(price-4)/(1+2*tval)**2)

def optimal_ratio(n,price):
    if price>=24*n/(15*n-7):return 0.
    upper=1.
    while derivative(n,price,upper)<0:upper*=2.
    return brentq(lambda z: derivative(n,price,z),0.,upper,xtol=1e-13)

for n in (2,3,5,7,10):
    threshold=24*n/(15*n-7)
    for rvalue in (.3,1.,1.5,1.6,2.,threshold*(1-1e-5),threshold,threshold*(1+1e-5),5.):
        ratio=optimal_ratio(n,rvalue)
        assert_close(derivative(n,rvalue,0)>=-1e-8,rvalue>=threshold,0)
        if ratio>0:assert_close(derivative(n,rvalue,ratio),0,1e-9)
        # Objective is minimized against several feasible perturbations.
        def obj(z):return (2+rvalue*z)*((3*n-1)/2+6*(n-1)/(1+z)+3/(1+2*z))
        for offset in (0,0.001,0.1,1.,5.):
            assert obj(ratio)<=obj(max(0,ratio-offset))+1e-7
            assert obj(ratio)<=obj(ratio+offset)+1e-7
            checks+=2

# Analytic asymptotic predictions tested at increasing network sizes.
for rvalue in (.3,.8,1.2,1.5):
    expected=2*sqrt((2-rvalue)/rvalue)-1
    for n in (200,1000,5000):
        assert_close(optimal_ratio(n,rvalue),expected,0.045)
for n in (200,1000,4000):
    assert_close(n*optimal_ratio(n,1.6),7/6,0.06)
for kappa in (-2.,0.,.3,.65,.7466666666667,1.,2.):
    limit=max(0.,7/6-25*kappa/16)
    for n in (500,2000):
        observed=n*optimal_ratio(n,1.6+kappa/n)
        assert_close(observed,limit,0.10)

# Independently sample nonsymmetric perturbations, optimizing all edge weights,
# to test equality with the two-orbit formula beyond the analytic reduction.
rng=np.random.default_rng(20261027)
for n,rvalue in ((2,.8),(2,3.),(3,1.),(3,1.65),(4,2.)):
    E=[(i,j) for i in range(3*n) for j in range(i+1,3*n) if i//n!=j//n]
    prices=np.array([rvalue if {i//n,j//n}=={0,2} else 1.0 for i,j in E])
    B=3*n*n
    ratio=optimal_ratio(n,rvalue)
    x=B/(n*n*(2+rvalue*ratio));y=ratio*x
    wopt=np.array([y if {i//n,j//n}=={0,2} else x for i,j in E])
    C=np.zeros((len(E),3*n,3*n))
    for k,(i,j) in enumerate(E):
        C[k,i,i]=1;C[k,j,j]=1;C[k,i,j]=-1;C[k,j,i]=-1
    def objective(w):
        L=np.einsum('k,kij->ij',w,C)
        M=L+np.ones_like(L)/(3*n)
        X=np.linalg.inv(M)
        return (3*n)*(np.trace(X)-1), -(3*n)*np.einsum('ij,kjl,li->k',X,C,X)
    for k in range(2):
        start=rng.uniform(0.15,1.0,len(E));start*=B/np.dot(prices,start)
        z=minimize(lambda w:objective(w),start,method='SLSQP',jac=True,
                   bounds=[(0.,None)]*len(E),constraints=[{'type':'eq','fun':lambda w:prices@w-B,'jac':lambda w:prices}],
                   options={'maxiter':250,'ftol':1e-10})
        assert z.success,z.message
        exact=(n*n/B)*((2+rvalue*ratio)*((3*n-1)/2+6*(n-1)/(1+ratio)+3/(1+2*ratio)))
        assert_close(z.fun,exact,2e-5)
        assert_close(np.linalg.norm(z.x-wopt,ord=np.inf),0,2e-4)

print(f'PASS: {checks} substantive symbolic/numeric checks; full matrix comparison; nonsymmetric optimization; critical scaling.')
