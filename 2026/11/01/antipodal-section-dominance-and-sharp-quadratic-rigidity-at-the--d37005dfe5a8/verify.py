import numpy as np, math
rng=np.random.default_rng(326)
n=0; max_diff=-1e9
for d in range(2,9):
 for k in range(300):
  H=rng.normal(size=(d,d));H=(H+H.T)/2;H-=np.trace(H)*np.eye(d)/d
  e,Q=np.linalg.eigh(H)
  eps=0.035
  A=(Q*(d*np.exp(eps*e)))@Q.T
  c=np.ones(d)*(0.006/math.sqrt(d)) if k%2 else np.zeros(d)
  u=rng.normal(size=d);u/=np.linalg.norm(u)
  q=float(u@A@u);t=float(u@c)
  vplus=(q-(1-t)**2)**((d-1)/2)/q**(d/2)
  vminus=(q-(1+t)**2)**((d-1)/2)/q**(d/2)
  ratio=d**(d/2)*math.sqrt(vplus*vminus)/(d-1)**((d-1)/2)
  assert ratio<=1+2e-12, (d,k,ratio)
  if np.linalg.norm(c)>0 or abs(q-d)>1e-8:assert ratio<1+1e-12
  n+=1;max_diff=max(max_diff,ratio-1)
print('PASS',n,'max ratio-1',max_diff)
for d in range(2,10):
 for lam in (1.1,d*.75,d*1.5):
  if lam<=1 or abs(lam-d)<1e-10:continue
  H=np.diag([1,-1]+[0]*(d-2));u=np.eye(d)[0 if lam<d else 1];eps=1e-6
  A=lam*np.diag(np.exp(eps*np.diag(H)))
  q=u@A@u
  f=lambda q:(q-1)**((d-1)/2)/q**(d/2)
  assert f(q)>f(lam)
print('local critical-radius rigidity PASS')

# The full logarithmic second variation is derived analytically;
# sample a few fixed tangent directions at decreasing perturbation sizes.
for d in (2,3,5,8):
    H=np.diag([1.,-1.]+[0.]*(d-2))
    b=np.arange(1.,d+1.)/(d*10.)
    u=np.arange(1.,d+1.,dtype=float);u/=np.linalg.norm(u)
    a=u@H@u;t0=u@b
    coeff=d*a*a/(4*(d-1))+(d+1)*t0*t0/(2*(d-1))
    values=[]
    for ep in (1.e-3,5.e-4,2.5e-4):
        A=d*np.diag(np.exp(ep*np.diag(H)))
        q=u@A@u;t=ep*t0
        ratio=np.sqrt((q-(1-t)**2)*(q-(1+t)**2))**((d-1)/2) / q**(d/2)
        ratio *= d**(d/2)/(d-1)**((d-1)/2)
        values.append(-np.log(ratio)/ep**2)
    assert abs(values[-1]-coeff)<.004, (d,values,coeff)
print('Hessian small-parameter coefficients PASS')
