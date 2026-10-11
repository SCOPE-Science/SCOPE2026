import itertools, math
import numpy as np
from fractions import Fraction

def expected(n,q,k,as_float=True):
  p=Fraction(q-1,q); a=Fraction(k,n); w=Fraction(math.comb(n,k)*(q-1)**k,q**n)
  R=1+n*(a-p)**2/(p*(1-p))
  S=Fraction(k*(n-k),n*(n-1))/(p*(1-p))
  T=a/p
  return [((float(v) if as_float else v),m) for v,m in [(w*R,1),(w*S,n-1),(w*T,n*(q-2)),(Fraction(0),1)]]

def test(n,q,k):
  G=list(itertools.product(range(q),repeat=n))
  freq=[(0,)*n]
  for i in range(n):
    for a in range(1,q):
      x=[0]*n;x[i]=a;freq.append(tuple(x))
  B=[x for x in G if sum(v!=0 for v in x)==k]
  mat=np.array([[np.exp(2j*np.pi*sum(u*v for u,v in zip(h,x))/q) for h in freq] for x in B],complex)
  C=mat.conj().T@mat/len(G)
  ev=np.linalg.eigvalsh(C)
  ex=np.array(sorted(v for (eig,m) in expected(n,q,k) for v in [eig]*m))
  err=max(abs(np.sort(ev)-ex))
  assert err<1e-10,(n,q,k,err,ev,ex)
  return err

cases=0
for q in (3,4,5):
 for n in (2,3,4):
  if q**n>700:continue
  for k in range(1,n):
   test(n,q,k);cases+=1
for q in range(3,16):
 for n in range(2,80):
  for k in range(1,n):
   vals=[x for x,m in expected(n,q,k,False) if m>0 and x>0]
   equal=max(vals)==min(vals)
   formula=(n-1)%q==0 and k==((q-1)*n+1)//q and ((q-1)*n+1)%q==0
   assert equal==formula,(q,n,k,vals)
print(f'VERIFY_OK explicit_Fourier_cases={cases} arithmetic_tight_cases=verified')
