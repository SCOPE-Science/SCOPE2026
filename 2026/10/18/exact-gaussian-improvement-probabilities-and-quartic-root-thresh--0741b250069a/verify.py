"""Independent finite-matrix and distribution checks for a Gaussian Nyström spectral preconditioner.
Requires numpy and scipy. Run: python verify.py
"""
import numpy as np
from scipy.special import betainc
from scipy.stats import norm

rng = np.random.default_rng(20261015)
checks = 0

def exact_condition(lam, mu, omega):
    a = np.diag([lam] + [mu] * (len(omega)-1))
    h = np.eye(len(omega)) + a
    n = np.outer(a @ omega, a @ omega) / (omega @ a @ omega)
    w, v = np.linalg.eigh(np.eye(len(omega)) + n)
    p12 = (v / np.sqrt(w)) @ v.T
    return np.linalg.cond(p12 @ h @ p12)

def scalar_condition(lam, mu, omega):
    x = omega[0]**2
    y = omega[1:] @ omega[1:]
    return (1+lam)*(1+mu)*(lam*x+mu*y)/(lam*(1+lam)*x+mu*(1+mu)*y)

def probability(lam, mu, m, ratio):
    h1, h2 = 1+lam, 1+mu
    if h1 <= h2*h2: return 0.0
    tstar = mu*mu*h2/(lam*(h1-h2*h2))
    return float(1-betainc(.5,m/2,tstar/(tstar+ratio)))

for m in range(1,9):
    for _ in range(90):
        mu = float(np.exp(rng.uniform(-2,2)))
        lam = float(mu * np.exp(rng.uniform(.05,4)))
        o = rng.standard_normal(m+1)
        val = exact_condition(lam, mu, o)
        th = scalar_condition(lam, mu, o)
        assert np.isclose(val, th, rtol=2e-10, atol=2e-10), (m, val, th)
        checks += 1

for mu in [0.1,0.5,1.,2.]:
    for lam in [mu+0.1, mu*mu+2*mu, mu*mu+2*mu+0.01, 4*(mu*mu+2*mu)]:
        if lam <= mu: continue
        h1,h2=1+lam,1+mu
        for m in [1,2,8,40,300]:
            for ratio in [0.25,1.0,lam*h1/(mu*h2),10.]:
                p=probability(lam,mu,m,ratio)
                assert 0 <= p <= 1
                if h1 <= h2*h2: assert p == 0
                checks += 1

# Normal tail critical-window checks: large m and spike growth.
for mu in [0.4,1.,2.]:
    h2=1+mu
    for c in [1.,2.,3.]:
        for m in [10000,1000000]:
            li=c*m**.25
            if li > mu:
                r=li*(1+li)/(mu*h2)
                p=probability(li,mu,m,r)
                lim=2*norm.sf(mu**1.5*h2/c**2)
                # Quantified values converge slowly; compare at two m scales.
                assert abs(p-lim)<0.24, (mu,c,m,p,lim)
                checks+=1
            ls=c*m**.5
            p=probability(ls,mu,m,1.)
            lim=2*norm.sf(mu*np.sqrt(h2)/c)
            assert abs(p-lim)<0.08,(mu,c,m,p,lim)
            checks+=1

# Independently simulate full Gaussian sketch vectors and compare finite beta law.
for m in [1,3,10,50]:
    for mu,lam in [(1.,3.),(1.,5.),(.25,3.),(2.,12.)]:
        g=rng.standard_normal((60000,m+1))
        for ratio in [1.,lam*(1+lam)/(mu*(1+mu))]:
            g[:,0]*=np.sqrt(ratio)
            obs=np.mean([scalar_condition(lam,mu,x)<(1+lam)/(1+mu) for x in g])
            th=probability(lam,mu,m,ratio)
            assert abs(obs-th)<.02,(m,mu,lam,ratio,obs,th)
            checks+=1
            g[:,0]/=np.sqrt(ratio)
print('PASS:', checks, 'finite numerical/distribution checks')
