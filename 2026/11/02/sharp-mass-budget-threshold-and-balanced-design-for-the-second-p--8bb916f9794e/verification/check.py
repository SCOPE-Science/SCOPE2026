import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def bands(a,b,d):
    def eig(t, sign):
        s=a+b
        root=math.sqrt(max(0.0,s*s-4*a*b*(-math.expm1(-2*d*t))))
        coth=1/math.tanh(t/2)
        return .5*coth*(s+sign*root)
    vals=[]
    for sign in (1,-1):
        if sign==-1 and 4*d*a*b/(a+b)<=1: continue
        f=lambda t: eig(t,sign)-1
        lo=1e-7
        while f(lo)<=0: lo*=.1
        hi=2
        while f(hi)>0: hi*=2
        t=brentq(f,lo,hi,xtol=1e-14)
        vals.append(2+2*math.cosh(t))
    return sorted(vals,reverse=True)

checks=0
for d in (1,2,3,4,7,10):
  for a,b in ((.18,.3),(.4,.7),(.5,.5),(.8,.8),(.15,.9),(.3,.95),(.8,.23),(.98,.99)):
    evals=bands(a,b,d)
    N=201+2*d
    diag=np.full(N,2.0)
    off=np.full(N-1,-1.0)
    m=np.ones(N)
    m[N//2]=1-a; m[N//2+d]=1-b
    diag/=m; off/=np.sqrt(m[:-1]*m[1:])
    H=diags([off,diag,off],[-1,0,1],format='csr')
    obs=np.sort(eigsh(H,k=3,which='LA',return_eigenvectors=False))[::-1]
    assert len(evals)==1+int(4*d*a*b/(a+b)>1+1e-12)
    for o,e in zip(obs,evals):
      if e>4.02: assert abs(o-e)<2e-7,(a,b,d,o,e)
    checks+=1
for d in range(1,10):
 for s in (.4,.8,1.2,1.6):
  if d*s<=1.1: continue
  r0=bands(s/2,s/2,d)
  r1=bands(s*.41,s*.59,d)
  if len(r1)==2: assert r0[1]>r1[1]
  checks+=1
print('PASS',checks,'spectral/allocation cases')
for d in (1,2,3,4):
  s=1.001/d
  a=b=s/2
  C=4*a*b*d*d*(a*a+b*b)/(s*s*s)
  e=4*d*a*b/s-1
  root=bands(a,b,d)[1]
  ratio=(root-4)/((e/C)**2)
  print('onset d',d, 'eta',e,'pred gap',(e/C)**2,'actual',root-4,'ratio',ratio)
