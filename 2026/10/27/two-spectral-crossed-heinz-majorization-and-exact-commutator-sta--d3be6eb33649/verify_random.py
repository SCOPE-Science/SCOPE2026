import numpy as np
rng=np.random.default_rng(20261023)
count=0
min_gap=1e9
max_err=0
for n in range(2,9):
 for trial in range(120):
  def proj(rank):
   z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); q,_=np.linalg.qr(z)
   return q[:,:rank]@q[:,:rank].conj().T
  P=proj(rng.integers(1,n));Q=proj(rng.integers(1,n));a0,a1=sorted(rng.uniform(0.1,6,size=2));b0,b1=sorted(rng.uniform(0.1,6,size=2));t=rng.uniform(.05,.95)
  def powA(s):return a0**s*np.eye(n)+(a1**s-a0**s)*P
  def powB(s):return b0**s*np.eye(n)+(b1**s-b0**s)*Q
  C=powA(t)@powB(1-t)+powB(t)@powA(1-t)
  H=powA(t)@powB(1-t)+powA(1-t)@powB(t)
  sc=np.linalg.svd(C,compute_uv=False);sh=np.linalg.svd(H,compute_uv=False)
  gaps=np.cumsum(sh-sc)
  min_gap=min(min_gap, min(gaps))
  if min(gaps)<-1e-7: print('FAIL',n,trial,min(gaps));raise SystemExit
  expected=((a1**t-a0**t)*(a1**(1-t)-a0**(1-t))*(b1**t-b0**t)*(b1**(1-t)-b0**(1-t)))*np.linalg.norm(P@Q-Q@P)**2
  actual=np.linalg.norm(H)**2-np.linalg.norm(C)**2
  err=abs(expected-actual)/(1+abs(expected))
  max_err=max(max_err,err)
  if err>1e-7:print('IDENTITY FAIL',n,trial,expected,actual);raise SystemExit
  count+=1
print('PASS',count,'min gap',min_gap,'max relative error',max_err)
