"""Independent numerical checks for the Poisson-line selective-sweep persistence formulas.
Run: python verify.py (Python 3.10+, NumPy, SciPy).
Finite simulations corroborate but do not establish the exact infinite-process identities.
"""
import math
import numpy as np
from scipy.integrate import quad

checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1

# Integrate one-point Campbell expression after integrating out height.
for s, t in [(1.0, 1.01), (1.0, 1.5), (1.0, 2.0), (2.0, 6.0), (0.3, 3.0)]:
    val, err = quad(lambda x: math.exp(-x/s)/(s*(1-math.exp(-x/s))+t*math.exp(-x/s)), 0, math.inf if s>=0.3 else 100, epsabs=1e-11)
    exact = s * math.log(t/s) / (t-s)
    check(abs(val-exact)<1e-9, 'Campbell two-time integral')
    mix, err = quad(lambda v: 1/(1+(t-s)*v/s), 0, 1, epsabs=1e-12)
    check(abs(mix-exact)<1e-12, 'rate-mixture Laplace transform')

# Exact two-point crossing intensity integrates to log(t/s)/2.
for s, t in [(0.1, 0.5), (1.0, 2.0), (2.0, 8.0), (9.0, 10.0)]:
    value, err = quad(lambda u: 1/(2*u), s, t)
    check(abs(value-0.5*math.log(t/s))<1e-12, 'crossing intensity integral')

# Direct finite-window planar PPP check (not a proof; truncation can lose distant contenders).
rng=np.random.default_rng(92560011)
replicates=1600
L=40.0
YMIN=-3.5
accepted=0
for _ in range(replicates):
    n=rng.poisson(L*math.exp(-YMIN))
    x=rng.uniform(0,L,size=n)
    y=YMIN+rng.exponential(size=n)
    i=np.argmax(y-x)
    j=np.argmax(2*y-x)
    accepted+=int(i==j)
emp=accepted/replicates
check(abs(emp-math.log(2))<0.045, f'finite PPP comparison: {emp}')
print(f'{checks} checks passed; sampled same-leader frequency={emp:.6f}; exact={math.log(2):.6f}')

# Independent numerical renewal simulation of the proved Gamma(2,1) increment law.
from scipy.special import logsumexp
rng2 = np.random.default_rng(421083)
for count in [4000, 10000]:
    increments = rng2.gamma(shape=2.0, scale=1.0, size=count)
    multipliers = rng2.exponential(size=count)
    fitness = np.cumsum(increments)-increments
    log_T = logsumexp(fitness + np.log(multipliers))
    check(abs(count/log_T-0.5)<0.02, 'renewal almost-sure frequency simulation')
print('Gamma-renewal frequency checks passed; total checks:', checks)
