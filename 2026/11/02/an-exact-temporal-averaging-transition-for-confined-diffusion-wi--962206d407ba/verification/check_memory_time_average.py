"""Reproducible checks for equilibrium-start OU resetting to uniform past.
Only scientific identities and reproducibility; numerical checks are not proofs.
Python 3; requires numpy, scipy, mpmath.
"""
from math import exp, sqrt
import numpy as np
import scipy.integrate as si
import mpmath as mp

mp.mp.dps=45

def closed(t,k,r,D):
    # J(t)=E[(int_0^t X_s ds)^2], start X_0~N(0,D/k).
    sig2=mp.mpf(D)/k
    a=mp.mpf(k)+r
    beta=2*mp.mpf(r)/a
    t=mp.mpf(t)
    if t==0: return mp.mpf('0')
    if abs(beta-1)<mp.mpf('1e-30'):
        return (2*sig2/a)*(t*(mp.euler+mp.log(a*t)+mp.e1(a*t))-t+(1-mp.exp(-a*t))/a)
    return 2*sig2*t/(a*(beta-1))*(mp.hyp1f1(1-beta,2,-a*t)-1)

def ode(t,k,r,D):
    a=k+r; sig2=D/k
    def rhs(z,y):
        j,h=y
        return [2*h, sig2-a*h+r*j/z if z else sig2]
    # initial small-z Taylor using c_2 and c_3 and c_4
    z0=min(1e-5,t*1e-3)
    c2=sig2
    c3=-k*sig2/3
    c4=-(3*a-2*r)/(12)*c3
    j0=c2*z0**2+c3*z0**3+c4*z0**4
    h0=c2*z0+1.5*c3*z0**2+2*c4*z0**3
    sol=si.solve_ivp(rhs,(z0,t),[j0,h0],rtol=2e-12,atol=3e-13)
    assert sol.success
    return sol.y[0,-1]

checks=0
for k,r,D in [(1,0.2,1),(1,0.5,2),(1,1,1),(1,1.6,0.3),(1,3,1.5),(2.5,0.4,0.7),(2.5,2.5,0.7),(2.5,7,0.7)]:
    for t in [0.01,0.1,0.3,1,2,5,10,20]:
        j=float(closed(t,k,r,D)); num=ode(t,k,r,D)
        assert abs(j-num)<=max(5e-9,5e-8*j),(k,r,D,t,j,num)
        checks+=1

# Compare numerical inverse Laplace with direct formula and positive limit coefficients.
for k,r,D in [(1,.4,1),(1,1,1),(1,2.2,1)]:
    a=k+r; beta=2*r/a; sig2=D/k
    for t in [0.2,1,2.4,6]:
        def transform(s):
            s=mp.mpc(s)
            if abs(beta-1)<1e-12:
                return 2*sig2/a*s**(-2)*mp.log(1+a/s)
            return 2*sig2/(a*(beta-1))*(s**(-1-beta)*(s+a)**(beta-1)-s**(-2))
        inverse=mp.invertlaplace(transform,t,method='talbot')
        assert abs(inverse-closed(t,k,r,D))<mp.mpf('1e-9')
        checks+=1

for k,r in [(1,.2),(1,.8),(1,1),(1,2),(1,4)]:
    D=1; a=k+r; beta=2*r/a; sig2=D/k
    t=mp.mpf(10)**7
    j=closed(t,k,r,D)
    if r<k:
        target=2*sig2*t/(k-r)
    elif r>k:
        target=2*sig2*a**(beta-2)*t**beta/((beta-1)*mp.gamma(1+beta))
    else:
        target=2*sig2/a*t*mp.log(a*t)
    assert abs(j/target-1)<mp.mpf('0.18'),(k,r,float(j/target))
    checks+=1

# Check single-trajectory Monte Carlo moments independently of ODE and Laplace transform.
# OU evolves by exact transition over dt; resets choose a uniformly sampled grid history.
rg=np.random.default_rng(20261026)
mc=[]
for k,r,D in [(1,.5,1),(1,1,1),(1,2,1)]:
    T=3.; dt=.006; steps=round(T/dt); N=18000
    sig2=D/k
    x=rg.normal(0,sqrt(sig2),N)
    history=np.empty((steps+1,N),dtype=np.float64)
    history[0]=x
    integ=np.zeros(N)
    ee=exp(-k*dt); noise=sqrt(sig2*(1-ee*ee))
    ids=np.arange(N)
    for i in range(steps):
        old=x.copy()
        x=ee*x+noise*rg.standard_normal(N)
        take=rg.random(N)<r*dt
        ix=np.where(take)[0]
        if len(ix):
            past=rg.integers(0,i+1,len(ix))
            x[ix]=history[past,ix]
        integ+=.5*dt*(old+x)
        history[i+1]=x
    empirical=float(np.mean(integ**2))
    exact=float(closed(T,k,r,D))
    rel=abs(empirical-exact)/exact
    assert rel<.075,(k,r,empirical,exact,rel)
    mc.append((k,r,empirical,exact,rel))
    checks+=1
print('PASS:',checks,'independent ODE / Laplace / asymptotic / sampled-path checks')
for row in mc: print('MC',row)
