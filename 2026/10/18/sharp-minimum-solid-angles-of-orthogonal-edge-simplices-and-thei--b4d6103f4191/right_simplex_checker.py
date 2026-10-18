"""Reproducible supplementary checks for the right-simplex minimum solid-angle law.
Requires Python 3, NumPy, SciPy, and SymPy. Finite tests are not proofs of asymptotics.
"""
from math import atan, exp, lgamma, log, pi
import numpy as np
from scipy.integrate import quad
import sympy as sp


def base(d):
    return exp(lgamma(d/2) - log(2) - (d/2)*log(pi) - lgamma(d))

# Deterministic Dirichlet simplex quadrature for dimensions 2 and 3.
a2 = quad(lambda r: (1+r*r)**(-1), 0, 1, epsabs=2e-13)[0]
p2 = base(2)*a2
# The integral for d=2 has an elementary value: arctan(1)=pi/4.
assert abs(p2-1/8) < 5e-14, (p2,1/8)

integral3 = quad(lambda r: quad(lambda s: (1+r*r+s*s)**(-1.5),
                                   0, 1-r, epsabs=2e-12)[0],
                 0, 1, epsabs=2e-12)[0]
p3 = base(3)*2*integral3
angle3 = atan(3-2*np.sqrt(2))/(2*pi)
assert abs(p3-angle3) < 5e-13, (p3, angle3)

# A strict large-leg cone comparison is pointwise in directions, not simulated.
# Any non-equal positive leg tuple has a largest-leg vertex whose cone is
# a strict subset of the corresponding equal-leg vertex cone.

# Verify exact Dirichlet first and second moment expressions symbolically.
d = sp.symbols('d', integer=True, positive=True)
EA = 2*(d-1)/(d+1)
EA2 = d**2*(24*(d-1)+4*(d-1)*(d-2))/(d*(d+1)*(d+2)*(d+3))
var = sp.factor(EA2-EA**2)
assert sp.simplify(var-4*(d-1)*(d*d+3*d+6)/((d+1)**2*(d+2)*(d+3))) == 0

# Empirical Dirichlet normalization from iid exponentials in blocks.
def dirichlet_factor(d,n=50000,seed=271828):
    rng = np.random.default_rng(seed+d)
    collected=[]
    for size in [min(n,1000)]*(n//1000)+([n%1000] if n%1000 else []):
        e = rng.exponential(1.0,(size,d))
        q = np.sum(e[:,:-1]**2,axis=1)/np.sum(e,axis=1)**2
        collected.append(np.power(1+q,-d/2))
    z = np.concatenate(collected)
    return float(z.mean()),float(z.std(ddof=1)/np.sqrt(n))

for d_ in (16,64,256,1024):
    q,se=dirichlet_factor(d_,40000)
    target=exp(-1)
    print('dimension',d_,'normalization',q,'SE',se,'target',target)
    if d_ >= 256:
        assert abs(q-target) < .01, (d_,q)

print('d=2',p2,'d=3',p3)
print('verified Dirichlet finite moments and exact d=2,d=3 angles')
print('PASS')
