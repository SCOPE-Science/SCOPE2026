import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(457)
assertions=0
cases=0
for m in range(2,9):
 for j in range(18):
  b=float(rng.uniform(.03,.92));c2=float(rng.uniform(.002,0.98*(1+b)));a=np.sqrt(c2/(2*m))
  N=2*m+1
  A=np.eye(N);A[0,1:]=a;A[1:,0]=a
  for i in range(m):A[2*i+1,2*i+2]=A[2*i+2,2*i+1]=b
  assert np.linalg.eigvalsh(A)[0]>0;assertions+=1
  t0=1+b
  tcrit=2*b*(1-b)/(2*b-c2) if c2<2*b else np.inf
  t=tcrit if c2<=4*b*b/(1+b) else t0
  D=np.ones(N);D[0]=np.sqrt(t)
  w=np.linalg.eigvalsh(D[:,None]*A*D[None,:]);kap=w[-1]/w[0]
  lambdap=(t+1+b+np.sqrt((t-(1+b))**2+4*c2*t))/2
  lambdam=(t+1+b-np.sqrt((t-(1+b))**2+4*c2*t))/2
  model=lambdap/min(lambdam,1-b)
  assert abs(kap-model)<2e-10*max(1,kap);assertions+=1
  for fac in np.geomspace(.15,8,12):
   t1=t*fac;D1=np.ones(N);D1[0]=np.sqrt(t1)
   w1=np.linalg.eigvalsh(D1[:,None]*A*D1[None,:])
   assert w1[-1]/w1[0]>=kap*(1-2e-10);assertions+=1
  if j<5:
   def f(x):
    D=np.exp(np.r_[0,x]);w=np.linalg.eigvalsh(D[:,None]*A*D[None,:]);return np.log(w[-1]/w[0])
   x0=rng.normal(0,.3,N-1)
   res=minimize(f,x0,method='BFGS',options={'maxiter':400, 'gtol':1e-7})
   assert f(res.x)>=np.log(kap)-1e-7,(m,b,c2,kap,f(res.x));assertions+=1
  cases+=1
print('cases',cases,'assertions',assertions,'global asymmetric optimization',7*5)
