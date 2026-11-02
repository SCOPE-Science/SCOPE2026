"""Independent finite checks for fractional combinatorial-star gradients.
SciPy and NumPy are used solely for supplementary numerical diagnostics.
The mathematical proof is in RESULT.md, not in this checker.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar

checks=0

def close(a,b,atol=4e-10):
 global checks
 assert abs(a-b)<=atol*max(1,abs(a),abs(b)), (a,b)
 checks+=1

def predicted(m,s):
 a=(m+1)**(-s)
 out=np.empty((m,m+1))
 out[:,0]=-a
 out[:,1:]=np.eye(m)-(1-a)/m
 return out

def direct(m,s):
 B=np.concatenate((-np.ones((m,1)),np.eye(m)),axis=1)
 L=B.T@B
 w,V=eigh(L)
 w[np.abs(w)<1e-9]=0
 Lneg=(V*(np.array([float(z)**(-s) if z>0 else 0.0 for z in w])))@V.T
 return B@Lneg

def cp(p):
 def ratio(t):
  return ((t**(p-1)+(1-t)**(p-1))**(1/p)
          *(t**(1/(p-1))+(1-t)**(1/(p-1)))**(1-1/p))
 r=minimize_scalar(lambda t:-ratio(t),bounds=(1.e-8,.49999999),method='bounded',options={'xatol':1e-13})
 return -r.fun,r.x

# Eigenoperator reconstruction and exact endpoint norms for independent m, s.
for m in (2,3,4,5,9,16,32):
 for s in (0.125,0.25,0.5,0.8,1.,1.5,2.):
  r=predicted(m,s)
  d=direct(m,s)
  close(np.max(np.abs(r-d)),0,atol=2e-8)
  a=(m+1)**(-s)
  norm1=max(m*a,2-2/m-(m-2)*a/m)
  norminf=2-2/m+2*a/m
  norm2=max(1,(m+1)**(.5-s))
  close(np.abs(r).sum(axis=0).max(),norm1)
  close(np.abs(r).sum(axis=1).max(),norminf)
  close(np.linalg.svd(r,compute_uv=False)[0],norm2)

# At p=2 the critical constant is exactly one.
for m in (2,3,5,17):
 close(np.linalg.svd(predicted(m,.5),compute_uv=False)[0],1)

# Strict extra critical resonance: two-valued centering extremizer
# improves when a free scalar coordinate is introduced.
for p in (1.25,1.5,1.75,2.5,3.,4.,6.):
 C,t=cp(p)
 assert C>1+1e-5
 checks+=1
 q=1/(p-1)
 b=t**q/(t**q+(1-t)**q)
 A=1-b
 B=-b
 mean=t*A+(1-t)*B
 centeredA=A-mean
 centeredB=B-mean
 base=(t*abs(centeredA)**p+(1-t)*abs(centeredB)**p)**(1/p)
 denom=(t*abs(A)**p+(1-t)*abs(B)**p)**(1/p)
 close(base/denom,C,atol=1e-7)
 slope= -p*(t*np.sign(centeredA)*abs(centeredA)**(p-1)
            +(1-t)*np.sign(centeredB)*abs(centeredB)**(p-1))
 assert abs(slope)>1e-8
 checks+=1
 for dc in (1e-5,1e-4):
  c=np.sign(slope)*dc
  val=((t*abs(centeredA-c)**p+(1-t)*abs(centeredB-c)**p)/
       (abs(c)**p+t*abs(A)**p+(1-t)*abs(B)**p))**(1/p)
  assert val>C, (p,t,C,val)
  checks+=1

# A fixed binary critical input converges under leaf-grid refinement.
for p in (1.5,3.,4.):
 C,t=cp(p)
 b=t**(1/(p-1))/(t**(1/(p-1))+(1-t)**(1/(p-1)))
 v0,v1=1-b,-b
 c=0.005*(1 if p>2 else -1)
 for m in (20,50,150,500):
  k=round(t*m)
  f=np.r_[np.full(k,v0),np.full(m-k,v1)]
  x=np.r_[c,m**(-1/p)*f]
  out=predicted(m,1/p)@x
  val=np.linalg.norm(out,ord=p)/np.linalg.norm(x,ord=p)
  assert math.isfinite(val) and val>1
  checks+=1

print('PASS',checks,'supplementary assertions')
