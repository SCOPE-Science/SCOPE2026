"""Finite-canonical checks for critical occupations of finitely many defect sites.
No external data and no claimed proof by computation.
"""
from math import sqrt, gamma, log
import numpy as np
from scipy.special import gammaln,logsumexp
from scipy.integrate import quad

def canonical_total(L, q, r, lam=0):
    N=round(L*q/(1-q)+lam*sqrt(L))
    s=np.arange(N+1)
    b=N-s
    lognb=(gammaln(L+b)-gammaln(L)-gammaln(b+1)
           +L*np.log1p(-q)+b*np.log(q))
    logmultip=gammaln(s+r)-gammaln(s+1)-gammaln(r)
    logprob=lognb+logmultip
    p=np.exp(logprob-logsumexp(logprob))
    return s/sqrt(L),p

def theory_total_mean(q, r, lam):
    v=q/(1-q)**2
    num=quad(lambda s: s**r*np.exp(-(s-lam)**2/(2*v)),0,np.inf,epsabs=1.e-10)[0]
    den=quad(lambda s: s**(r-1)*np.exp(-(s-lam)**2/(2*v)),0,np.inf,epsabs=1.e-10)[0]
    return num/den

def main():
  tests=0
  for q in [.25,.4,.7]:
   for r in [1,2,3,4]:
    for lam in [0.,.8]:
     theory=theory_total_mean(q,r,lam)
     errs=[]
     for L in [120,480,1920]:
      scaled,p=canonical_total(L,q,r,lam)
      val=sum(scaled*p)
      errs.append(abs(val-theory))
      assert np.isfinite(val)
      tests+=1
     assert errs[2]<errs[0]+.025, (q,r,lam,errs)
     print('MOMENT', q,r,lam, 'limit',round(theory,6),'errors', [round(x,5) for x in errs])
  # r=2,3 chi moments critical
  for q in [.2,.45]:
   v=q/(1-q)**2
   for r in [1,2,3,4]:
    expectation=sqrt(2*v)*gamma((r+1)/2)/gamma(r/2)
    theo=theory_total_mean(q,r,0)
    assert abs(expectation-theo)<1e-9
    tests+=1
  # direct sum dynamic log weights vs simple combinatorial product for small systems
  from itertools import product
  for L in [2,3,4]:
   for r in [1,2,3]:
    for N in [0,1,2,3,4,5]:
     weights={}
     for conf in product(range(N+1),repeat=L+r):
      if sum(conf)!=N: continue
      s=sum(conf[-r:]);weights[s]=weights.get(s,0)+(.41)**(-s)
     s=np.array(sorted(weights))
     b=N-s
     direct=np.array([weights[int(z)] for z in s],float)
     exact=np.exp(gammaln(s+r)-gammaln(s+1)-gammaln(r)+gammaln(L+b)-gammaln(L)-gammaln(b+1)+b*np.log(.41))
     assert np.allclose(direct /sum(direct),exact/sum(exact), atol=2e-14)
     tests+=1
  print('ALL TESTS',tests,'PASS')
if __name__=='__main__':main()

# Additional independent nonzero-tilt tests are available by importing this module.
def verify_tilt():
 from scipy.special import xlogy
 from scipy.integrate import quad
 tests=0
 q=.43;v=q/(1-q)**2
 for theta in [-1.1,-.4,.4,1.1]:
  for lam in [-.5,.8]:
   def H(s):return np.expm1(theta*s)/theta
   def density_integrals():
    den=quad(lambda s:H(s)*np.exp(-(s-lam)**2/(2*v)),0,40)[0]
    num=quad(lambda s:s*H(s)*np.exp(-(s-lam)**2/(2*v)),0,40)[0]
    return num/den
   tmean=density_integrals();errs=[]
   for L in [120,480,1920]:
    N=round(L*q/(1-q)+lam*sqrt(L))
    s=np.arange(N+1,dtype=float)
    b=N-s
    a=theta/sqrt(L)
    x=a*(s+1)
    logH=np.log(np.abs(np.expm1(x)))-np.log(np.abs(np.expm1(a)))
    lognb=gammaln(L+b)-gammaln(L)-gammaln(b+1)+L*np.log1p(-q)+b*np.log(q)
    probs=np.exp(lognb+logH-logsumexp(lognb+logH))
    mean=np.sum(s/sqrt(L)*probs)
    errs.append(abs(mean-tmean))
    tests+=1
   assert errs[-1]<errs[0]+.02,(theta,lam,errs)
 print('TILT CHECKS',tests,'PASS')
 return tests

def verify_generator():
    from itertools import product
    cases=0
    for bulk in (1,2,3):
      for defects in (2,3):
       rates=[1.]*bulk + [.39*(1+.13*j) for j in range(defects)]
       T=len(rates)
       for N in (1,2,3,4):
        for cfg in product(range(N+1),repeat=T):
         if sum(cfg)!=N: continue
         # π(η) ∝ ∏ r_i^{-η_i}
         mass=np.prod([rates[j]**(-cfg[j]) for j in range(T)])
         outbound=sum(rates[j] for j in range(T) if cfg[j]>0)*mass
         inbound=0.
         for j in range(T):
          i=(j+1)%T
          if cfg[i]==0:continue
          prec=list(cfg)
          prec[j]+=1;prec[i]-=1
          precmass=np.prod([rates[k]**(-prec[k]) for k in range(T)])
          inbound+=rates[j]*precmass
         assert np.isclose(outbound,inbound,rtol=1e-12,atol=1e-12),(cfg,inbound,outbound)
         cases+=1
    print('GENERATOR BALANCE',cases,'PASS')
    return cases
if __name__=='__main__':
 verify_tilt()
 verify_generator()
