import numpy as np, math
from scipy.linalg import svdvals

def predicted(p):
 d=len(p)-1
 D=sum(j*abs(p[j])**2 for j in range(1,d+1))
 if D<=0: return None
 H=lambda j:sum(1/i for i in range(1,j+1))
 B=sum(j*H(j-1)*abs(p[j])**2 for j in range(1,d+1))
 E=sum(abs(sum(m*np.conj(p[m-n])*p[m] for m in range(n,d+1)))**2/n for n in range(1,d+1))
 return D,abs(p[0])**2-B+E/D

def norm2(p,a,N=200):
 d=len(p)-1
 coeff=np.ones(N+d+1)
 for n in range(1,N+d+1): coeff[n]=coeff[n-1]*(a+n-1)/n
 M=np.zeros((N,N),complex)
 for j in range(N):
  for k in range(min(d,N-j-1)+1): M[j+k,j]=p[k]*np.sqrt(coeff[j]/coeff[j+k])
 return svdvals(M)[0]**2
for p in [[1,1],[1,0,1],[1,1,1],[2+1j,.5-1j,2j,1],[0,1,1],[1,3,-2]]:
 D,C=predicted(p)
 print(p,'D C',D,C)
 for a in [.1,.025,.008]:
  val=norm2(p,a)
  print(a, round(val,8),round((val-D/a)-C,8))
