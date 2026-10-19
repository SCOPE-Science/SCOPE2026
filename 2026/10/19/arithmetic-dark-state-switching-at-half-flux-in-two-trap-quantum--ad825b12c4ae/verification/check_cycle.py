import numpy as np
from math import gcd,pi
from scipy.linalg import expm

def expected(N,d,m):
 g=gcd(N,d);M=N//g
 if m is None:return 0
 c=(g*gcd(2,M) if (m%gcd(2,M)==0) else 0)
 s=(gcd(2,N) if (m%gcd(2,N)==0) else 0)
 return (c-s)//2

def measured(N,d,phi):
 ks=np.arange(N)
 ens=2*np.cos((2*pi*ks+phi)/N)
 groups=[]
 for k,e in enumerate(ens):
  if not any(k in gr for gr in groups):
   groups.append([j for j in range(N) if abs(e-ens[j])<1e-8])
 total=0
 for gr in groups:
  V=np.exp(-2j*pi*np.outer([0,d],gr)/N)
  sv=np.linalg.svd(V,compute_uv=False)
  rank=np.sum(sv>1e-7)
  total+=len(gr)-rank
 return total

if __name__=='__main__':
 checks=0
 for N in range(3,61):
  for d in range(1,N):
   for m,phi in [(0,0),(1,pi),(None,.341)]:
    a=expected(N,d,m);b=measured(N,d,phi)
    assert a==b,(N,d,m,a,b)
    checks+=1
 print('spectral-constraint identities:',checks)
 # Independent integer-level verification of the congruence quotient.
 for N in range(3,121):
  for d in range(1,N):
   for m in (0,1):
    kset=[k for k in range(N) if (d*(2*k+m))%N==0 and (2*k+m)%N!=0]
    assert len(kset)%2==0
    assert len(kset)//2==expected(N,d,m), (N,d,m)
 print('integer congruence identities: complete for N=3..120')
 for N,d,m in [(6,2,0),(6,2,1),(12,4,0),(12,4,1),(9,3,0),(9,3,1),(8,2,0),(8,2,1)]:
  N=int(N);phi=m*pi;U=np.zeros((N,N),dtype=complex)
  for j in range(N):
   U[(j+1)%N,j]=np.exp(1j*phi/N)
  H=U+U.conj().T
  D=np.zeros((N,N),dtype=complex);D[0,0]=.5;D[d,d]=.5
  T=expm((-1j*H-D)*150)
  val=np.linalg.norm(T,'fro')**2/N
  expected_val=expected(N,d,m)/N
  print('N,d,m',N,d,m,'pred',expected_val,'time150',val)
  assert abs(val-expected_val)<2e-4
