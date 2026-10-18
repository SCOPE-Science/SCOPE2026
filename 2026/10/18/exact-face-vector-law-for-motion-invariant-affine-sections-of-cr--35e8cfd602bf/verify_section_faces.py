import math,itertools,random
from scipy.integrate import quad
from scipy.special import erf
import numpy as np

def theoretical(d,k,j):
 s=j+2
 coeff=sum(math.comb(k,q)*math.comb(d-k,s-q)*2**q for q in range(s+1) if q<=k and s-q<=d-k)
 return (2**s)*math.comb(d,s)-coeff-(math.comb(d-k,s) if s<=d-k else 0)

def brute(d,a,s,j):
 out=0
 for coords in itertools.combinations(range(d),j+2):
  for signs in itertools.product([-1,1],repeat=j+2):
   vals=[signs[q]*a[i] for q,i in enumerate(coords)]
   out+= min(vals)<s<max(vals)
 return out
rng=np.random.default_rng(210149)
comparisons=0
for d in range(3,9):
 for rep in range(35):
  a=np.abs(rng.standard_normal(d))
  t=rng.uniform(0,np.max(a))
  k=sum(a<=t)
  for j in range(d-1):
   exp=theoretical(d,k,j)
   got=brute(d,a,t,j)
   assert exp==got,(d,k,j,exp,got)
   comparisons+=1
for d in (3,4,5,7):
 F=lambda t: erf(t/math.sqrt(2))
 den=quad(lambda t:1-F(t)**d,0,12,epsabs=2e-12)[0]
 probs=[]
 for k in range(1,d):
  ks=[0,1] if k==1 else [k]
  v= sum(quad(lambda t,k0=k0:math.comb(d,k0)*F(t)**k0*(1-F(t))**(d-k0),0,12,epsabs=2e-12)[0] for k0 in ks)
  probs.append(v/den)
 assert abs(sum(probs)-1)<2e-10
 print('d',d,'probabilities',[round(float(p),10) for p in probs],'f0',[theoretical(d,k,0) for k in range(1,d)])
 print('expected f0',sum(p*theoretical(d,k,0) for k,p in enumerate(probs,1)))
# deterministic integral quadrature law and iid Gaussian importance-sampled Monte Carlo
for d in (3,4,6):
 num=400000
 H=np.abs(rng.standard_normal((num,d)))
 M=H.max(axis=1)
 U=rng.uniform(size=num)
 K=np.sum(H<=U[:,None]*M[:,None],axis=1)
 w=M
 dnorm=w.sum()
 p=np.array([np.sum(w*(K==0 if k==1 else K==k))/dnorm for k in range(1,d)])
 p[0]+=np.sum(w*(K==1))/dnorm
 F=lambda t:erf(t/math.sqrt(2))
 den=quad(lambda t:1-F(t)**d,0,12)[0]
 exact=np.array([sum(quad(lambda t,k0=k0:math.comb(d,k0)*F(t)**k0*(1-F(t))**(d-k0),0,12)[0] for k0 in ([0,1] if k==1 else [k]))/den for k in range(1,d)])
 assert np.max(np.abs(p-exact))<0.006,(d,p,exact)
 print('mc',d,'max_error',np.max(np.abs(p-exact)))
print('CROSSPOLY_FACE_LAW_OK brute_comparisons=',comparisons)
