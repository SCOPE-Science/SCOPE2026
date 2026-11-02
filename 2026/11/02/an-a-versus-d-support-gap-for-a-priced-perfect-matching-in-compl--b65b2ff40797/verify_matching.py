"""Reproducible numerical and symbolic checks for the priced-matching resistance theorem.

Run: python3 verify_matching.py (requires numpy, scipy, sympy).
This verifier tests finite instances; the accompanying analytic proof covers all stated parameters.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize, brentq


def cutoff_a(m):
    return m*m*(4*m*m-11*m+8)/((m-2)*(4*m**3-11*m*m+10*m-4))

def cutoff_d(m):
    return m*(2*m-3)/((m-2)*(2*m-1))

def H(m,u):
    return 1/(2*(u+m-1))+(m-1)/m+(m-1)/(2*u+m-2)

def Hp(m,u):
    return -1/(2*(u+m-1)**2)-2*(m-1)/(2*u+m-2)**2

def fprime(m,r,u):
    return r*H(m,u)+(r*u+m-1)*Hp(m,u)

def optimizer(m,P,Q,B):
    r=P/Q
    if r>=cutoff_a(m)-1e-13:
        u=0.
    else:
        hi=1.
        while fprime(m,r,hi)<0:
            hi*=2.
        u=brentq(lambda z:fprime(m,r,z),0,hi,xtol=1e-13)
    y=B/(m*(P*u+(m-1)*Q));x=u*y
    return x,y,u

def Kf_formula(m,x,y):
    d=x+(m-1)*y
    return 2*m*(1/(2*d)+(m-1)/(m*y)+(m-1)/(2*x+(m-2)*y))

def weighted_matrix(m,edges,weights):
    L=np.zeros((2*m,2*m))
    for (i,j),w in zip(edges,weights):
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L

def unrestricted_obj(weights,m,edges):
    L=weighted_matrix(m,edges,weights)
    lam=np.linalg.eigvalsh(L)
    if lam[1]<1e-12: return 1e15
    return 2*m*np.sum(1/lam[1:])

def run():
    m,r,u=sp.symbols('m r u', positive=True)
    HH=1/(2*(u+m-1))+(m-1)/m+(m-1)/(2*u+m-2)
    crit=sp.factor(sp.solve(sp.diff((r*u+m-1)*HH,u).subs(u,0),r)[0])
    asserted=m*m*(4*m*m-11*m+8)/((m-2)*(4*m**3-11*m*m+10*m-4))
    assert sp.simplify(crit-asserted)==0
    dd=m*(2*m-3)/((m-2)*(2*m-1))
    gap=sp.factor(crit-dd)
    assert gap==2*m*(m-1)*(4*m*m-9*m+6)/((m-2)*(2*m-1)*(4*m**3-11*m*m+10*m-4))
    assert sp.limit(m*(crit-1),m,sp.oo)==2
    assert sp.limit(m*(dd-1),m,sp.oo)==1
    gg=sp.symbols('g')
    assert sp.simplify(sp.limit(m*sp.diff(((1+gg/m)*u+m-1)*HH,u),m,sp.oo)-(2*gg+4*u-4))==0
    logdiff=1/(u+m-1)+2*(m-1)/(2*u+m-2)-(2*m-1)*(1+gg/m)/((1+gg/m)*u+m-1)
    assert sp.simplify(sp.limit(m*logdiff,m,sp.oo)-(-2*gg-2*u+2))==0
    print('symbolic identities: 7 passed')

    rng=np.random.default_rng(20261101)
    n_spectra=n_sensitivity=n_feasible=n_unrestricted=0
    for mm in range(3,10):
        edges=[(i,mm+j) for i in range(mm) for j in range(mm)]
        matching=np.array([i==j for i in range(mm) for j in range(mm)])
        for rvalue in [0.1,0.75,1,1.03,1.15,0.95*cutoff_a(mm),cutoff_a(mm),1.05*cutoff_a(mm),4.0]:
            P=float(rvalue);Q=1.;B=1.7+0.3*mm
            x,y,uu=optimizer(mm,P,Q,B)
            assert abs(mm*P*x+mm*(mm-1)*Q*y-B)<1e-10
            assert x>=-1e-14 and y>0
            assert (x<1e-11)==(rvalue>=cutoff_a(mm)-1e-12)
            v=np.where(matching,x,y)
            L=weighted_matrix(mm,edges,v)
            lam=np.linalg.eigvalsh(L)
            expected=np.sort(np.array([0,2*(x+(mm-1)*y)]+[mm*y]*(mm-1)+[2*x+(mm-2)*y]*(mm-1)))
            assert np.max(np.abs(lam-expected))<3e-11
            direct=2*mm*sum(1/lam[1:])
            assert abs(direct/Kf_formula(mm,x,y)-1)<3e-11
            n_spectra+=1
            # Tests unrestricted feasibility, not restricted symmetric competitors.
            for k in range(30):
                trial=rng.dirichlet(np.ones(mm*mm)*(0.4+0.1*k))
                trial=trial*B/np.dot(trial,np.where(matching,P,Q))
                assert unrestricted_obj(trial,mm,edges)>=direct*(1-5e-10)
                n_feasible+=1
            if mm in (3,4,5,6) and rvalue in (0.75,1.03,4.0):
                costs=np.where(matching,P,Q)
                rng_init=np.random.default_rng(999+mm+int(100*rvalue))
                init=rng_init.uniform(0.1,1.0,size=mm*mm)
                init*=B/(costs@init)
                def zobj(z):
                    return unrestricted_obj(z,mm,edges)
                res=minimize(zobj,init,method='SLSQP',bounds=[(0,None)]*(mm*mm),constraints={'type':'eq','fun':lambda zz:costs@zz-B},options={'maxiter':250,'ftol':1e-10})
                if res.success:
                    assert abs(res.fun/direct-1)<2e-6,(mm,rvalue,res.fun/direct)
                    n_unrestricted+=1
            n_sensitivity+=1
    assert n_unrestricted>=10,n_unrestricted
    print('spectra and formula:',n_spectra,'passed')
    print('budget and support:',n_sensitivity,'passed')
    print('asymmetric feasible allocations:',n_feasible,'passed')
    print('unrestricted optimizations:',n_unrestricted,'passed')
    print('critical ratios: m=3',cutoff_a(3),'m=4',cutoff_a(4),'m=5',cutoff_a(5))
if __name__=='__main__':run()
