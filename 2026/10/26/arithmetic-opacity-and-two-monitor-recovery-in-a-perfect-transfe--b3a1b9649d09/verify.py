import math
import numpy as np
from scipy.linalg import eigh
from math import comb,isqrt

def kraw(N,j,k):
    return sum((-1)**h*comb(k,h)*comb(N-k,j-h) for h in range(max(0,j-N+k),min(j,k)+1))
def dark(N):
    return [k for k in range(N+1) if kraw(N,3,k)==0]
def arithmetic(N):
    vals=([N//2] if N%2==0 else [])
    m=3*N-2;s=isqrt(m)
    if s*s==m:
        vals.extend([(N-s)//2,(N+s)//2])
    return sorted(set(vals))
for N in range(3,55):
    assert dark(N)==arithmetic(N),(N,dark(N),arithmetic(N))
    if N<=22:
        H=np.zeros((N+1,N+1))
        for i in range(N): H[i,i+1]=H[i+1,i]=math.sqrt((i+1)*(N-i))
        evals,U=eigh(H)
        for k in range(N+1):
            theoretical=math.sqrt(comb(N,k)/2**N/comb(N,3))*kraw(N,3,k)
            assert abs(abs(theoretical)-abs(U[3,N-k]))<2e-9,(N,k,U[3,N-k],theoretical)
        endpoint=sum(comb(N,k)/2**N for k in dark(N))
        measured=sum(abs(U[0,N-k])**2 for k in dark(N))
        assert abs(endpoint-measured)<3e-11
        if dark(N): print('N',N,'dark',dark(N),'endpoint survival',round(endpoint,9))
print('PASS')
for N in [4,6,9,17,22,34]:
 H=np.zeros((N+1,N+1),complex)
 for i in range(N): H[i,i+1]=H[i+1,i]=math.sqrt((i+1)*(N-i))
 gamma=1.31
 for eta in [1e-3,1e-4]:
  K=H.copy();K[3,3]-=0.5j*gamma;K[2,2]-=0.5j*eta
  eig=np.linalg.eigvals(K)
  for k in dark(N):
   E=N-2*k
   lam=min(eig,key=lambda v:abs(v-E))
   p2=comb(N,k)/2**N/comb(N,2)*kraw(N,2,k)**2
   assert abs((-2*lam.imag/eta)-p2)<0.02,(N,k,eta,lam,p2)
 print('N',N,'weak second monitor slopes PASS')
