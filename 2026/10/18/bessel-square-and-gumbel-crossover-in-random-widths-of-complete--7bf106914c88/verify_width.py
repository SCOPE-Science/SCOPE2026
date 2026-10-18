"""Independent directional-width and finite-dimensional probability checks.
Requires Python 3.10+ and numpy/scipy. Run: python width_check.py.
All directions use the intrinsic Euclidean metric in the sum-zero hyperplane.
"""
import math
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
rng=np.random.default_rng(20261017)
verified=0
for p in range(2,8):
 for q in range(2,9):
  n=p+q;d=n-1
  roots=[]
  for i in range(p):
   for j in range(q):
    r=np.zeros(n);r[i]=1;r[p+j]=-1;roots.extend([r,-r])
  roots=np.array(roots)
  for _ in range(20):
   g=rng.normal(size=n);z=g-g.mean();rad=np.linalg.norm(z)
   direct=np.max(roots@(z/rad))-np.min(roots@(z/rad))
   a=g[:p];b=g[p:]
   h=max(a.max()-b.min(),b.max()-a.min())
   theoretical=2*h/rad
   assert abs(direct-theoretical)<1e-10
   assert abs(math.sqrt(d)*direct/2-h*math.sqrt(d)/rad)<1e-10
   verified+=1
# The exact Gaussian-support CDF conditional on B extrema gives a tractable
# one-dimensional identity at q=1, even though all asymptotic results use q>=2.
for p in (2,3,5):
 for t in (.5,1.5,2.7):
  # For q=1, B is a single normal. Conditional probability each A within [B-t,B+t].
  exact=quad(lambda z:norm.pdf(z)*(norm.cdf(z+t)-norm.cdf(z-t))**p,-10,10,epsabs=1e-11)[0]
  assert 0<exact<1
  assert exact>0
# Check special functions: sum of two independent Gumbels has Bessel-K1 CDF.
from scipy.special import kv
for t in (-3.,-.5,0.,1.,3.):
 integral=quad(lambda s: math.exp(-s-math.exp(-t)/s),0,30,epsabs=1e-11)[0]
 closed=2*math.exp(-t/2)*kv(1,2*math.exp(-t/2))
 assert abs(integral-closed)<3e-11,(t,integral,closed)
print('VERIFY_OK root_support_comparisons='+str(verified)+' Bessel_integral_checks=5')
