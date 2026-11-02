"""Independent numerical and exact checks for priced wheel resistance allocation.
Run with Python 3 and NumPy, SciPy, SymPy installed.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize


def rim_modes(n):
    return 2-2*np.cos(2*np.pi*np.arange(1,n)/n)

def spectral_sum(n,z):
    c=rim_modes(n)
    return 1/(n+1)+np.sum(1/(1+c*z))

def spectral_derivative(n,z,P,Q):
    c=rim_modes(n)
    return Q*spectral_sum(n,z)-(P+Q*z)*np.sum(c/(1+c*z)**2)

def opt_ratio(n,P,Q):
    if Q>=2*P*(n+1)/n: return 0.0
    hi=1.
    while spectral_derivative(n,hi,P,Q)<=0:hi*=2
    return brentq(lambda z: spectral_derivative(n,z,P,Q),0.,hi,xtol=2e-14)

def allocation(n,P,Q,B):
    z=opt_ratio(n,P,Q)
    a=B/(n*(P+Q*z))
    return a,a*z

def laplacian(n,w):
    L=np.zeros((n+1,n+1),dtype=float)
    edges=[(0,j) for j in range(1,n+1)]+[(j,1+(j%n)) for j in range(1,n+1)]
    for (u,v),c in zip(edges,w):
        L[u,u]+=c; L[v,v]+=c; L[u,v]-=c; L[v,u]-=c
    return L

def kirchhoff(L):
    ev=np.linalg.eigvalsh(L)
    if ev[1]<=1e-11: return float('inf')
    return L.shape[0]*np.sum(1/ev[1:])

def direct_sp(n,a,b):
    c=rim_modes(n)
    return (n+1)*(1/((n+1)*a)+np.sum(1/(a+b*c)))

def series_sp(n,z):
    if z==0: return n*n/(n+1)
    r=math.sqrt(1+4*z)
    t=(2*z)/(1+2*z+r)  # algebraically stable expression for small z
    return n/r*(1+t**n)/(1-t**n)-n/(n+1)

# Exact rational check at nontrivial prices; all 8 edges are freely designable.
n=4; P=sp.Rational(13); Q=sp.Rational(17); a=sp.Rational(1,120); b=a
M=sp.zeros(5)
for j in range(1,5):
    for u,v,w in [(0,j,a),(j,1+j%4,b)]:
        M[u,u]+=w;M[v,v]+=w;M[u,v]-=w;M[v,u]-=w
assert sorted(M.eigenvals().keys())==[0,sp.Rational(1,40),sp.Rational(1,24)]
assert M.eigenvals()[sp.Rational(1,40)]==2
assert M.eigenvals()[sp.Rational(1,24)]==2
assert sp.simplify(5*(2*40+2*24))==640
assert 4*(P*a+Q*b)==1
assert sp.simplify(Q*(sp.Rational(1,5)+2/sp.Integer(3)+sp.Rational(1,5))-(P+Q)*(sp.Rational(4,9)+sp.Rational(4,25)))==0
print('exact_symbolic_checks 6')

rng=np.random.default_rng(314159265)
spectral_checks=0; closed_checks=0; feasible_checks=0; stationary_checks=0
for n in range(3,15):
    for _ in range(12):
        P=float(rng.uniform(0.45,3.0));Q=float(rng.uniform(0.2,4.6));B=float(rng.uniform(0.8,4.0))
        a,b=allocation(n,P,Q,B)
        target=direct_sp(n,a,b)
        observed=kirchhoff(laplacian(n,[a]*n+[b]*n))
        assert np.isclose(observed,target,rtol=1e-10,atol=1e-9),(n,P,Q,a,b,target,observed)
        spectral_checks+=1
        assert np.isclose(spectral_sum(n,b/a),series_sp(n,b/a),rtol=2e-11,atol=1e-11)
        closed_checks+=1
        assert np.isclose(n*(P*a+Q*b),B,rtol=1e-12)
        assert abs(spectral_derivative(n,b/a,P,Q))<1e-9 if b>0 else spectral_derivative(n,0,P,Q)>=-1e-10
        stationary_checks+=1
        # Unrestricted asymmetric individual conductance allocations.
        for _ in range(15):
            v=rng.dirichlet(np.ones(2*n))
            costs=np.array([P]*n+[Q]*n)
            w=B*v/costs
            assert np.dot(costs,w)>B*(1-1e-11)
            K=kirchhoff(laplacian(n,w))
            assert K+1e-8>=target,(n,P,Q,K,target)
            feasible_checks+=1
print('direct_spectral',spectral_checks,'closed_sum',closed_checks,'KKT_budget',stationary_checks,'asymmetric_feasible',feasible_checks)

# A separate unrestricted constrained optimizer, checking all individual edges.
opt_checks=0
for n in (3,4,6,9):
    for P,Q in ((1.,1.),(1.,2.),(1.,3.)):
        B=1.;a,b=allocation(n,P,Q,B);target=direct_sp(n,a,b)
        edges=2*n; costs=np.array([P]*n+[Q]*n)
        x0=np.ones(edges)*(B/np.sum(costs))
        # Optimize using normalized budget-share variables with simplex constraints.
        def fun(s): return kirchhoff(laplacian(n,s/costs))
        sol=minimize(fun,np.ones(edges)/edges,method='SLSQP',bounds=[(0.,1.)]*edges,
                     constraints=[{'type':'eq','fun':lambda x: x.sum()-B}],
                     options={'maxiter':700,'ftol':1e-10})
        if sol.success:
            assert sol.fun>=target-2e-5,(n,P,Q,sol.fun,target)
            assert abs(sol.fun-target)<2e-3,(n,P,Q,sol.fun,target)
        opt_checks+=1
print('unrestricted_optimizer_cases',opt_checks)

critical=[]
for eta in (-2.,0.,0.5,1.,2.):
    n=2000;Q=2*(1+eta/n)
    z=opt_ratio(n,1.,Q)
    critical.append((eta,n*z,max(0,(1-eta)/2)))
    assert abs(n*z-max(0,(1-eta)/2))<0.018,(eta,z)
print('critical_scaling_cases',critical)
print('ALL_CHECKS_PASS')
