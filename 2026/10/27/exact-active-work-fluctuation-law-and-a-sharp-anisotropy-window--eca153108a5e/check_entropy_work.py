"""Exact-event Monte Carlo and symbolic/numeric checks for active work in a two-speed telegraph-driven harmonic trap.

Uses exact Ornstein-Uhlenbeck transitions between switching events. The Monte Carlo is
finite-time corroboration; the proof of long-time formulas is analytical.
"""
import numpy as np
from scipy.optimize import brentq


def parameters(kappa, D, alpha_R, alpha_L, v_R, v_L):
    assert min(kappa,D,alpha_R,alpha_L,v_R,v_L)>0
    gR, gL=alpha_R/2,alpha_L/2
    G=gR+gL
    delta=v_R+v_L
    pR=gL/G; pL=gR/G
    mean=pR*v_R-pL*v_L
    sig2=pR*pL*delta**2
    h=(pL-pR)*delta
    return G, mean, sig2, h, gR,gL


def theory(kappa,D,alpha_R,alpha_L,v_R,v_L):
    G,m,sig2,h,_,_=parameters(kappa,D,alpha_R,alpha_L,v_R,v_L)
    mu=G*sig2/(D*(kappa+G))
    v=2*mu*(1+kappa*sig2/(D*(kappa+G)**2)+h*h/(D*(2*kappa+G)))
    return mu,v


def run_exact(n,t_end,kappa,D,alpha_R,alpha_L,v_R,v_L,seed=1):
    rng=np.random.default_rng(seed)
    G,m,sig2,h,gR,gL=parameters(kappa,D,alpha_R,alpha_L,v_R,v_L)
    right=rng.random(n)<gL/G
    x=np.zeros(n)
    t=np.zeros(n)
    work=np.zeros(n)
    numsteps=0
    while np.any(t<t_end-1e-12):
        q=np.where(right,gR,gL)
        tau=rng.exponential(1/q)
        remaining=t_end-t
        dt=np.minimum(tau,remaining)
        u=np.where(right,v_R,-v_L)
        decay=np.exp(-kappa*dt)
        xnew=decay*x+u*(-np.expm1(-kappa*dt))/kappa
        xnew+=np.sqrt(D*(-np.expm1(-2*kappa*dt))/kappa)*rng.standard_normal(n)
        work+=u*(xnew-x)/D
        x=xnew
        t+=dt
        right^=(tau<remaining-1e-12)
        numsteps+=1
        if numsteps>30000:raise RuntimeError('unexpected event count')
    return work,numsteps


def peak_condition(kappa,G,sig2,h):
    return sig2*(G-kappa)/(kappa+G)**3-2*h*h/(2*kappa+G)**2


if __name__=='__main__':
    cases=[(1.2,.7,3.,1.6,2.,1.), (1.,1.,2.,2.,2.,1.), (0.3,1.5,3.,1.,1.,2.),(2.,.6,1.,3.,3.,1.)]
    for j,c in enumerate(cases):
        mu,v=theory(*c)
        W,steps=run_exact(8000,250.,*c,seed=321+j)
        observed_mean=W.mean()/250.
        observed_var=W.var(ddof=1)/250.
        err1=abs(observed_mean-mu)/mu
        err2=abs(observed_var-v)/v
        print(j,'theory',mu,v,'observed',observed_mean,observed_var,'errors',err1,err2,'steps',steps,flush=True)
        assert err1<.06 and err2<.11
    for ar,al in [(1,1),(.6,1),(1,2),(2,1),(2.01,1),(.49,1)]:
        G,m,sig2,h,*_=parameters(1,1,ar,al,2,1)
        c=h*h/sig2
        # At positive kappa: either one critical point, or none.
        x=np.linspace(.000001,1.2*G,1500)
        deriv=np.array([peak_condition(k,G,sig2,h) for k in x])
        crossings=np.count_nonzero((deriv[:-1]>0)&(deriv[1:]<0))
        asserted=1 if .5<ar/al<2 else 0
        assert crossings==asserted,(ar,al,c,crossings)
        if asserted:
            root=brentq(lambda z:peak_condition(z,G,sig2,h),1e-12,G)
            assert 0<root<=G
        print('peak',ar,al,'ratio',ar/al,'c',c,'crossings',crossings,flush=True)
    print('ALL CHECKS PASSED')
