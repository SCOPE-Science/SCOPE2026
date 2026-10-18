"""Reproduce exact Gaussian covariance recurrences and robust minimax phase law."""
import math
import numpy as np

def c_lambda(d,step):
    c=1-2*step+2*step**2
    return c, c+d*step**2

def objective(t,d,r,alpha):
    return (alpha*t + 1-alpha)*(r/t + d-r)

def robust_ratio(d,r,amin,amax):
    w=r/d
    if amin>w:
        return math.sqrt(r*(1-amin)/((d-r)*amin))
    if amax<w:
        return math.sqrt(r*(1-amax)/((d-r)*amax))
    return 1.

def covariance_formula(d,step,k,sigma,x):
    c,L=c_lambda(d,step)
    val=float(np.trace(np.linalg.inv(sigma)) * x @ sigma @ x)
    return c**k*(x@x)+(L**k-c**k)*val/d

def exact_two_step(d,step,sigma,x):
    # Analytically propagate covariance using Gaussian fourth moments.
    c,L=c_lambda(d,step)
    Q=np.outer(x,x)
    inv=np.linalg.inv(sigma)
    for _ in range(2):
        Q=c*Q+step*step*np.trace(sigma@Q)*inv
    return np.trace(Q)

count=0
rng=np.random.default_rng(348729)
for d in (2,3,4,7,10):
  for r in range(1,d):
    for amin,amax in ((.02,.06),(.3,.6),(.75,.98)):
      t=robust_ratio(d,r,amin,amax)
      score=max(objective(t,d,r,amin),objective(t,d,r,amax))
      for v in np.exp(np.linspace(-8,8,401)):
        assert score <= max(objective(v,d,r,amin),objective(v,d,r,amax))+1e-9
        count+=1
      # the all-SPD symmetrization inequality on random positive-definite B
      for _ in range(12):
        W=rng.standard_normal((d,d))
        B=W@W.T+np.eye(d)*0.7
        B/=np.trace(B)
        ib=np.linalg.inv(B)
        # Random feasible directions are a lower bound on worst possible original B.
        Bbar=(np.trace(B[:r,:r])/r)*np.eye(r)
        Bbars=(np.trace(B[r:,r:])/(d-r))*np.eye(d-r)
        ibbar0=1/np.diag(Bbar)[0];ibbar1=1/np.diag(Bbars)[0]
        sym=max((a*ibbar0+(1-a)*ibbar1) for a in (amin,amax))
        # Spherical averaging over both subspaces gives a feasible lower bound
        # on the original supremum; operator Jensen controls symmetrization.
        averaging_bound=max(a*np.trace(ib[:r,:r])/r +
                            (1-a)*np.trace(ib[r:,r:])/(d-r)
                            for a in (amin,amax))
        assert averaging_bound+1e-10>=sym
        count+=1

for d in (2,3,7):
 for step in (.04,.11,.21):
  W=rng.standard_normal((d,d)); sigma=W@W.T+np.eye(d)*.25
  x=rng.standard_normal(d);x/=np.linalg.norm(x)
  for k in (0,1,2):
   formula=covariance_formula(d,step,k,sigma,x)
   if k==2:
    assert abs(formula-exact_two_step(d,step,sigma,x))<1e-10
   count+=1
  # A direct MC check for one step, with correlated Gaussian probes.
  probes=rng.multivariate_normal(np.zeros(d),sigma,size=60000)
  zstep= x[None,:]-step*(probes@x)[:,None]*(probes@np.linalg.inv(sigma).T)
  mean=np.mean(np.sum(zstep**2,axis=1))
  theoretical=covariance_formula(d,step,1,sigma,x)
  tolerance=.10+ 4*np.std(np.sum(zstep**2,axis=1))/np.sqrt(len(probes))
  assert abs(mean-theoretical)<tolerance,(d,mean,theoretical,tolerance)
  count+=1
print('PASS',count,'deterministic checks; 9 independent 60,000-sample Gaussian experiments')
