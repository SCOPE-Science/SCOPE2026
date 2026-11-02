#!/usr/bin/env python3
"""Finite consistency checks of a proposed exact reversible-path hitting-time allocation theorem.
Requires Python 3, NumPy and SciPy. These computations supplement, not replace, proofs.
"""
import numpy as np
from scipy.optimize import minimize, minimize_scalar

rng = np.random.default_rng(361030)
checks = 0

def near(a,b,rtol=1e-8,atol=1e-8):
    global checks
    assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
    checks += 1

def truth(ok):
    global checks
    assert bool(ok)
    checks += 1

def solve(pi,p,B=1.0):
    n=len(pi)
    assert n>=3
    M=np.cumsum(pi)[:-1]
    d=2*M-1
    def S(t):
        a=1-M+t*d
        return float(np.sqrt(p*a).sum())
    def deriv(t):
        a=1-M+t*d
        return float((np.sqrt(p)*d/np.sqrt(a)).sum()/2)
    if deriv(0)<=0:
        lam=0.0
    elif deriv(1)>=0:
        lam=1.0
    else:
        from scipy.optimize import brentq
        lam=brentq(deriv,0,1,xtol=2e-14)
    a=1-M+lam*d
    ss=S(lam)
    c=(B/ss)*np.sqrt(a/p)
    HF=np.sum(M/c)
    HB=np.sum((1-M)/c)
    return lam,c,max(HF,HB),HF,HB,S

def generator(pi,c):
    n=len(pi)
    G=np.zeros((n,n))
    for i,conduct in enumerate(c):
        G[i,i+1]=conduct/pi[i]
        G[i+1,i]=conduct/pi[i+1]
    G[np.diag_indices(n)]=-G.sum(axis=1)
    return G

def hit(G,i,j):
    ids=[k for k in range(len(G)) if k!=j]
    v=np.linalg.solve(-G[np.ix_(ids,ids)],np.ones(len(ids)))
    return v[ids.index(i)]

# Fully independent generator linear-system tests for the first-hitting formulas.
for n in range(3,10):
    for rep in range(20):
        pi=rng.uniform(.2,3.0,n);pi/=pi.sum()
        p=rng.uniform(.15,5,n-1)
        c=rng.uniform(.25,4,n-1)
        G=generator(pi,c);M=np.cumsum(pi)[:-1]
        near(hit(G,0,n-1),np.sum(M/c),rtol=2e-10)
        near(hit(G,n-1,0),np.sum((1-M)/c),rtol=2e-10)
        vals=[hit(G,i,j) for i in range(n) for j in range(n) if i!=j]
        near(max(vals),max(np.sum(M/c),np.sum((1-M)/c)),rtol=2e-10)

# Dual closed-form optimality against full (unrestricted) nonlinear optimization.
for n in range(3,11):
    for rep in range(26):
        pi=rng.uniform(.1,3,n);pi/=pi.sum()
        p=np.exp(rng.uniform(-1.5,1.5,n-1));B=float(rng.uniform(.3,4))
        lam,c,val,HF,HB,S=solve(pi,p,B)
        M=np.cumsum(pi)[:-1]
        near(np.dot(p,c),B,rtol=1e-10)
        near(val,S(lam)**2/B,rtol=2e-10)
        if 1e-8<lam<1-1e-8:near(HF,HB,rtol=1e-9)
        elif lam==1:truth(HF>=HB-1e-8)
        else:truth(HB>=HF-1e-8)
        def obj(x):
            return max(np.sum(M/x),np.sum((1-M)/x))
        # SLSQP minimizes smooth epigraph form; ties are handled by two constraints.
        def f(z):return z[-1]
        def jac(z):
            w=np.zeros(len(z));w[-1]=1;return w
        x0=np.concatenate([c,[val*1.1]])
        eps=1e-8
        constraints=[{'type':'ineq','fun':lambda z:B-np.dot(p,z[:-1])},
                     {'type':'ineq','fun':lambda z:z[-1]-np.sum(M/z[:-1])},
                     {'type':'ineq','fun':lambda z:z[-1]-np.sum((1-M)/z[:-1])}]
        res=minimize(f,x0,method='SLSQP',jac=jac,bounds=[(eps,None)]*(n-1)+[(eps,None)],constraints=constraints,options={'maxiter':900,'ftol':1e-11})
        if res.success:
            near(res.fun,val,rtol=1e-5,atol=2e-6)
        for trial in range(5):
            weight=rng.dirichlet(np.ones(n-1))
            y=B*weight/p
            truth(obj(y)>=val-1e-8)

# Exceptional-price surcharge and near-critical directional regimes.
for n in range(3,101):
    i=np.arange(1,n,dtype=float)
    A=np.sum((2*i-n)/np.sqrt(i))
    truth(A<0)
    for k in range(n//2+1,n):
        a=(2*k-n)/np.sqrt(k)
        qc=(1-A/a)**2
        truth(qc>1)
        pi=np.full(n,1/n)
        for factor in (1.0, .6, 1.5):
            Q=1+(qc-1)*factor
            prices=np.ones(n-1);prices[k-1]=Q
            lam,c,T,forward,back,S=solve(pi,prices)
            if factor<1:
                truth(.5<lam<1)
                near(forward,back,rtol=1e-9)
            elif factor>1:
                near(lam,1.,rtol=0,atol=1e-9)
                truth(forward>back)
            else:
                near(lam,1.,rtol=0,atol=2e-8)
                near(forward,back,rtol=1e-8)

# Asymptotic constants from the theorem (numerical sanity checks only).
for theta in (.61,.7,.85,1.0):
    for n in (2000,10000,40000):
        k=min(n-1,int(theta*n))
        i=np.arange(1,n,dtype=float)
        A=np.sum((2*i-n)/np.sqrt(i))
        a=(2*k-n)/np.sqrt(k)
        qc=(1-A/a)**2
        predicted=4*theta/(9*(2*theta-1)**2)
        truth(abs(qc/n**2-predicted)<.15*predicted)
for s in (1,2,3):
    for n in (2000,10000):
        k=n//2+s
        i=np.arange(1,n,dtype=float)
        A=np.sum((2*i-n)/np.sqrt(i))
        qc=(1-A/((2*k-n)/np.sqrt(k)))**2
        truth(abs(qc/n**4-1/(18*s*s))<.15/(18*s*s))

# Exact three-state regime: balanced rates until Q=2, one-sided rates thereafter.
for Q in (1.0,1.25,1.9,2.0,2.1,3.0,10.0,100.0):
    lam,c,T,HF,HB,S=solve(np.ones(3)/3,np.array([1.0,Q]),B=2.5)
    if Q<=2:
        near(c, [2.5/(1+Q)]*2,rtol=1e-10)
        near(T,(1+Q)/2.5,rtol=1e-10)
    else:
        near(c[0]/c[1],np.sqrt(Q/2),rtol=1e-10)
        near(T,(1+np.sqrt(2*Q))**2/(3*2.5),rtol=1e-10)
# One completely explicit nontrivial exact threshold n=3,k=2 -> qcrit=2.
near((1-(-1+1/np.sqrt(2))/(1/np.sqrt(2)))**2,2,atol=1e-13)
print('PASS: %d deterministic finite assertions (not a proof of the universal theorem)'%checks)
