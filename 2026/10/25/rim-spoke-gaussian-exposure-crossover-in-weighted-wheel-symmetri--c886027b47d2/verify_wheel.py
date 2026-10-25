"""Independent finite tests of weighted-wheel support and angular crossover.

Requirements: numpy, scipy. Run: python verify_wheel.py
"""
import math
import numpy as np
from scipy.stats import norm

def test_support():
 rng=np.random.default_rng(521220)
 count=0
 for m in (4,5,7,10):
  for a in (0.3, 1., math.sqrt(2),2.4):
   roots=[]
   for i in range(1,m+1):
    roots.extend((np.eye(m+1)[i]-np.eye(m+1)[(i%m)+1],-(np.eye(m+1)[i]-np.eye(m+1)[(i%m)+1])))
    roots.extend((a*(np.eye(m+1)[0]-np.eye(m+1)[i]),-a*(np.eye(m+1)[0]-np.eye(m+1)[i])))
   roots=np.stack(roots)
   for _ in range(100):
    g=rng.normal(size=m+1)
    direct=np.max(roots@g)
    formula=max(np.max(np.abs(g[1:]-np.roll(g[1:],-1))),a*np.max(np.abs(g[1:]-g[0])))
    assert abs(direct-formula)<1e-12
    count+=1
 return count

def test_scaling():
 rng=np.random.default_rng(404)
 diagnostics=[]
 for m in (300,1500,7000):
  r=math.sqrt(2*math.log(m))
  n=10000
  rs,sp=[],[]
  for _ in range(0,n,100):
   g=rng.normal(size=(100,m+1))
   rim=np.max(np.abs(g[:,1:]-np.roll(g[:,1:],-1,axis=1)),axis=1)
   hub=np.max(np.abs(g[:,1:]-g[:,:1]),axis=1)
   rs.append(rim)
   sp.append(hub)
  rim=np.concatenate(rs); hub=np.concatenate(sp)
  for c in (-2,0,1):
   a=math.sqrt(2)+c/r
   prob=np.mean(a*hub>rim)
   target=2*norm.cdf(c/math.sqrt(2)) if c<0 else 1.
   diagnostics.append((m,c,float(prob),float(target)))
 assert abs(diagnostics[-6][2]-diagnostics[-6][3])<0.15
 return diagnostics

if __name__=='__main__':
 print('VERIFY_OK support=',test_support())
 for d in test_scaling():print('limit_diagnostic',d)
