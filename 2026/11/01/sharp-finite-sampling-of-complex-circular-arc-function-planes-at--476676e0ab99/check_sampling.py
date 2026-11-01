"""Supplementary numerical stress test, not an infinite or global certificate."""
import math
import numpy as np
from scipy.optimize import brentq
checks=0
for theta in (0.35, 0.9, 1.7, 2.8, 3.09):
 for m in (3,4,5,8,12):
  s=math.sin(theta/2)
  x=brentq(lambda x:math.sin(x)-s*math.cos(x/(m-1)),1e-12,theta/2)
  nodes=np.linspace(-2*x,2*x,m)
  d=np.linspace(-math.pi,math.pi,100001)
  numerator=np.maximum(np.abs(np.cos((d-theta)/2)),np.abs(np.cos((d+theta)/2)))
  numerator=np.where(np.abs(d)<=theta,1.,numerator)
  denominator=np.max(np.abs(np.cos((d[:,None]-nodes[None,:])/2)),axis=1)
  K=float(np.max(numerator/denominator))
  theoretical=1/math.cos(x/(m-1))
  assert abs(K-theoretical)<2e-5, (theta,m,K,theoretical)
  assert abs(s/math.sin(x)-theoretical)<1e-10
  checks+=2
print(f"Passed {checks} supplementary comparisons across 25 grids")
