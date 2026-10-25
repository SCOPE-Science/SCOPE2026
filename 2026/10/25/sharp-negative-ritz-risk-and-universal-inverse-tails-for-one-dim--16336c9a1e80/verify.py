import math, random
import numpy as np
from scipy.stats import t
rng=np.random.default_rng(17032026)
for s in (1,2,4,8,16):
 for lo,hi in ((1.,2.),(.5,8.),(2.,3.)):
  b=np.array([(hi/lo)**0.5,1.]); A=np.diag([lo,hi]);X=A@b;Y=b
  alpha=(X@Y)/(X@X); beta=math.sqrt((Y@Y)/(X@X)-alpha**2)
  edge=(hi-lo)/(2*math.sqrt(lo*hi))
  assert abs(beta/alpha-edge)<1e-12
  expected=t.cdf(-math.sqrt(s)*alpha/beta,df=s)
  Z=rng.normal(size=(40000,s,2)); U=Z@X;V=Z@Y
  H=np.sum(U*U,axis=1)/np.sum(U*V,axis=1)
  measured=np.mean(H<0)
  assert abs(measured-expected)<.018,(s,lo,hi,measured,expected)
print('PASS: 15 Gaussian risk frequencies and exact sharp spectral extremizers')
