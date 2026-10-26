"""Independent deterministic quadrature checks of a Beta--Gaussian mode transition.
Run: python checks/verify.py (requires numpy and scipy).
These checks are finite corroborations, not proofs of the asymptotic statements.
"""
import math
import numpy as np
from scipy.special import roots_jacobi, hyp1f1
from scipy.optimize import brentq

N = 340
count = 0

def yes(condition, message):
    global count
    assert bool(condition), message
    count += 1

def beta_nodes(a):
    z, w = roots_jacobi(N, a - 1.0, -0.5)
    return (z + 1.0)/2.0, w / sum(w)

def Q(a, t):
    y, w = beta_nodes(a)
    return np.dot(w, (y-t)*np.exp(-y/(2*t)))

def curve(a):
    return brentq(lambda t: Q(a, t), .0001, 1.5, xtol=3e-14)

def Qhyper(a, t):
    lam = 1/(2*t)
    return 2*lam*hyp1f1(1.5,a+1.5,-lam)/(2*a+1)/hyp1f1(.5,a+.5,-lam)-1

def deriv(a,t,x):
    y,w=beta_nodes(a)
    u=np.sqrt(y)
    return np.dot(w, .5*((u-x)*np.exp(-(u-x)**2/(2*t))+(-u-x)*np.exp(-(-u-x)**2/(2*t))))

for a in [.1,.2,.35,.5,.7,.9]:
    t=curve(a)
    yes(0<t<1, f'critical range {a}')
    yes(abs(Qhyper(a,t))<2e-8, f'hypergeometric root {a}')
    yes(Q(a,t*.98)>0, f'bimodal side {a}')
    yes(Q(a,t*1.02)<0, f'unimodal side {a}')
    y,w=beta_nodes(a)
    he4=np.dot(w,(y*y-6*t*y+3*t*t)*np.exp(-y/(2*t)))
    yes(he4 < -1e-7, f'negative quartic at criticality {a}')
    for delta in [.001,.0004]:
        root=brentq(lambda x:deriv(a,t-delta,x),.0001,1.15,xtol=2e-14)
        yes(abs(root**2/delta-3)<.1,f'mode splitting {a},{delta}')

c0=math.exp(.5)*math.sqrt(2*math.pi)*math.erf(1/math.sqrt(2))
for a in [.01,.003,.001]:
    t=curve(a)
    yes(abs((1-t)/a-c0)<.17, f'small persistence expansion {a}')

# The slowly convergent logarithm is tested against a numerical root, not
# misrepresented as a certified remainder bound.
for delta in [.01,.001,.0001]:
    a=1-delta
    t=curve(a)
    lam=1/(2*t)
    L=math.log(1/delta)
    predicted=L+1.5*math.log(L)+math.log(2/math.sqrt(math.pi))
    yes(abs(lam-predicted)<.8, f'near-uniform expansion {delta}')

print(f'PASS: {count} independent deterministic assertions')
print('a=1/2: t_c=', curve(.5))
print('small-a coefficient=', c0)
