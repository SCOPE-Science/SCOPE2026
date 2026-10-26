"""Reproduce analytic identities for direction-selective killing in a two-velocity process.

Usage: python verify.py
Requires Python 3, numpy, scipy. Numerical checks support, but do not replace, proofs.
"""
import math
import numpy as np
from scipy.linalg import expm
from numpy.random import default_rng

COUNT=0

def close(x,y,atol=2e-10,rtol=2e-10):
    global COUNT
    COUNT+=1
    if not np.allclose(x,y,atol=atol,rtol=rtol):
        raise AssertionError((x,y))

def formulas(lam,c,pplus,pminus):
    d=pplus+pminus-pplus*pminus
    delta=(pplus-pminus)/2
    r=math.sqrt((1-pplus)*(1-pminus))
    A=(2-pplus-pminus)/(2*r)
    kappa=lam*math.sqrt(d)/c
    right=0.5+delta/(2*math.sqrt(d))
    return d,delta,r,A,kappa,right

def cf_direct(lam,c,pplus,pminus,k):
    qplus=1-pplus;qminus=1-pminus
    M=np.array([[lam-1j*k*c,-lam*qplus],[-lam*qminus,lam+1j*k*c]])
    return 0.5*np.sum(np.linalg.solve(M,lam*np.array([pplus,pminus])))

def S(lam,pplus,pminus,t):
    r=math.sqrt((1-pplus)*(1-pminus))
    A=(2-pplus-pminus)/(2*r)
    return math.exp(-lam*t)*(math.cosh(lam*r*t)+A*math.sinh(lam*r*t))

def hazard(lam,pplus,pminus,t):
    _,_,r,A,_,_=formulas(lam,1,pplus,pminus)
    z=lam*r*t
    return lam-lam*r*(math.sinh(z)+A*math.cosh(z))/(math.cosh(z)+A*math.sinh(z))

pars=[(0.8,0.4,0.05,0.23),(3.2,1.1,0.12,0.83),(0.6,2.7,0.73,0.03),
      (5.,1.8,0.5,0.5),(1.1,0.9,0.93,0.98),(1.7,1.3,0.34,0.61)]
for lam,c,pplus,pminus in pars:
    d,delta,r,A,kappa,right=formulas(lam,c,pplus,pminus)
    for k in np.linspace(-5,5,29):
        target=(lam*lam*d+1j*k*c*lam*delta)/(lam*lam*d+c*c*k*k)
        close(cf_direct(lam,c,pplus,pminus,k),target)
    # Fourier inversion of two exponentially decaying half-line densities.
    for k in np.linspace(-4,4,23):
        plus=lam/(2*c)*(math.sqrt(d)+delta)/(kappa-1j*k)
        minus=lam/(2*c)*(math.sqrt(d)-delta)/(kappa+1j*k)
        close(plus+minus,cf_direct(lam,c,pplus,pminus,k))
    close(right,0.5+delta/(2*math.sqrt(d)))
    close(lam/(2*c)*(2*math.sqrt(d))/kappa,1.)
    close(lam/(2*c)*(math.sqrt(d)+delta)/kappa,right)
    close(lam/(2*c)*(math.sqrt(d)-delta)/kappa,1-right)
    close(lam*math.sqrt(d)/c,kappa)
    for t in np.linspace(0,2,35):
        Q=lam*np.array([[-1,1-pplus],[1-pminus,-1]])
        close(S(lam,pplus,pminus,t),np.array([0.5,0.5])@expm(Q*t)@np.ones(2))
        z=lam*r*t
        hp=lam**2*(pplus-pminus)**2/(4*(math.cosh(z)+A*math.sinh(z))**2)
        ht=hazard(lam,pplus,pminus,t)
        h_eps=(hazard(lam,pplus,pminus,t+1e-5)-hazard(lam,pplus,pminus,t-1e-5))/2e-5
        close(h_eps,hp,atol=6e-10,rtol=1e-7)
        close(ht>=0,True)
    close(hazard(lam,pplus,pminus,0),lam*(pplus+pminus)/2)
    close(lam*(1-r)>=hazard(lam,pplus,pminus,0),True)
    close((right>=0.5-math.sqrt(d)/4) and (right<=0.5+math.sqrt(d)/4),True)
    recovered_delta=2*math.sqrt(d)*(right-0.5)
    mm=1-math.sqrt(1-d+recovered_delta**2)
    close(mm+recovered_delta,pplus)
    close(mm-recovered_delta,pminus)

# Realizability: every interior point in the sharp envelope admits unique probabilities.
for d in np.linspace(0.02,0.98,31):
    for frac in np.linspace(-0.97,0.97,25):
        delta=frac*d/2
        m=1-math.sqrt(1-d+delta**2)
        pp,pm=m+delta,m-delta
        close(0<pp<1 and 0<pm<1,True)
        close(pp+pm-pp*pm,d)
        close((pp-pm)/2,delta)

# Independent stochastic construction from exponential interarrival times.
lam,c,pp,pm=1.7,2.3,0.24,0.69
rng=default_rng(731081)
ns=180000
v=np.where(rng.random(ns)<0.5,1,-1).astype('int8')
x=np.zeros(ns)
t=np.zeros(ns)
active=np.ones(ns,dtype=bool)
for j in range(60):
    inds=np.flatnonzero(active)
    if len(inds)==0:break
    dt=rng.exponential(1/lam,size=len(inds))
    x[inds]+=c*v[inds]*dt
    t[inds]+=dt
    ps=np.where(v[inds]==1,pp,pm)
    killed=rng.random(len(inds))<ps
    active[inds[killed]]=False
    v[inds[~killed]]*=-1
close(not np.any(active),True)
d,delta,r,A,kappa,right=formulas(lam,c,pp,pm)
# Independent standard-error-calibrated Monte Carlo tests, not proof of infinite population laws.
observed_right=np.mean(x>0)
se=math.sqrt(right*(1-right)/ns)
close(abs(observed_right-right)<6*se,True)
observed_abs=np.mean(np.abs(x))
close(abs(observed_abs-1/kappa)<6/(kappa*math.sqrt(ns)),True)
# Sign and radius are independent: identical conditional mean radii within sampling uncertainty.
positive=np.abs(x[x>0]);negative=np.abs(x[x<0])
sem=math.sqrt((1/kappa)**2/len(positive)+(1/kappa)**2/len(negative))
close(abs(positive.mean()-negative.mean())<6*sem,True)
# Survival time check (competing-mark simulation, distinct from resolvent calculation).
for t0 in [0.4,0.9,1.8]:
    truth=S(lam,pp,pm,t0)
    empirical=np.mean(t>t0)
    close(abs(empirical-truth)<6*math.sqrt(truth*(1-truth)/ns),True)

print(f'PASS: {COUNT} algebraic/matrix/numerical comparison checks')
print('simulation right mass',observed_right,'theory',right)
print('simulation mean abs',observed_abs,'theory',1/kappa)
print('simulation conditional means',positive.mean(),negative.mean())
