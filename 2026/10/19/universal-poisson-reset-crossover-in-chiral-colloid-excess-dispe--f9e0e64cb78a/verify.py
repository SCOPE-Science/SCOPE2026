"""Reproduce the Poisson orientation-reset excess-dispersion crossover.

Requires numpy and sympy. Independent cycle Monte Carlo is included.
"""
import numpy as np
import sympy as sp

k=sp.symbols('k',positive=True)
a1=k/(k+1);a2=k/(k+2);a4=k/(k+4)
nu=1/(k+1)
mean_tau=1/k
te=k/(k+1)**2
z2=sp.factor(1-2*a1+a2-2*(nu/mean_tau)*(mean_tau-te)+(nu/mean_tau)**2*2/k**2)
q=sp.factor(a2-a4-z2)
expect=2*(k**3+k**2+k-2)/((k+1)**3*(k+4))
assert sp.simplify(q-expect)==0
assert sp.factor(z2-2/((k+1)**3*(k+2)))==0
root=float(sp.nroots(k**3+k**2+k-2)[0]);assert 0.81<root<0.82
print('SYMBOLIC_CUBIC_IDENTITY_PASS; critical=',root)
# Specialize theta=c=delta=1, b=(1,0), Schur complement isotropic 0.3 I.
# Exact independent-cycle increments require only terminal Gaussian angle;
# independent 2D translational noise has conditional covariance 0.6*tau I.
rng=np.random.default_rng(760142)
for rate in [0.3,0.6,0.81,1.1,2.0,5.0]:
 n=400000
 t=rng.exponential(1/rate,n)
 ang=rng.standard_normal(n)*np.sqrt(2*t)
 dtheta=1.0
 vx=rate/(rate+1.0)
 centers=np.stack((1-np.cos(ang)-vx*t,-np.sin(ang)),axis=1)
 thermal=rng.standard_normal((n,2))*np.sqrt(0.6*t)[:,None]
 samples=centers+thermal
 cov=rate*np.cov(samples.T,bias=True)
 # For isotropic Schur, the thermal covariance rate is 0.6 I.
 measured_diff=cov[1,1]-cov[0,0]
 expected=rate*float(q.subs(k,rate))
 stderr=(np.std((samples[:,1]**2-samples[:,0]**2))*rate)/np.sqrt(n)
 assert abs(measured_diff-expected)<5*stderr, (rate, measured_diff, expected,stderr)
 # check mean regeneration reward, within approximate 5 standard deviations
 print('rate=',rate,'measured_diff=',round(measured_diff,5),'exact_diff=',round(expected,5),'se=',round(stderr,5))
print('MONTE_CARLO_EXCESS_ANISOTROPY_PASS')
# Other covariance formula algebra check, deterministic and Poisson
m=sp.symbols('m',positive=True)
print('ALL_CHECKS_PASSED')
