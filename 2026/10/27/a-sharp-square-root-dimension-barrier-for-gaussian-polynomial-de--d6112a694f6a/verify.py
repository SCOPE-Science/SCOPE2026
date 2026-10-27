import itertools,math
import numpy as np
from scipy.linalg import eigh_tridiagonal

def radial_eig(r,d):
 m=r//2
 a=np.array([4*j+d for j in range(m+1)],float)
 b=np.array([2*math.sqrt((j+1)*(j+d/2)) for j in range(m)],float)
 return eigh_tridiagonal(a,b,select='i',select_range=(0,0))[0][0]

def full_eig(r,d):
 mi=[a for a in itertools.product(range(r+1),repeat=d) if sum(a)<=r]
 dic={a:i for i,a in enumerate(mi)}
 M=np.zeros((len(mi),len(mi)))
 for i,a in enumerate(mi):
  M[i,i]=2*sum(a)+d
  for j in range(d):
   b=list(a);b[j]+=2
   if tuple(b) in dic:M[i,dic[tuple(b)]]=math.sqrt((a[j]+1)*(a[j]+2))
 M=M+M.T-np.diag(np.diag(M))
 return np.linalg.eigvalsh(M)[0]
for d in range(1,5):
 for r in range(1,7):
  f=full_eig(r,d);t=radial_eig(r,d)
  assert abs(f-t)<2e-12,(r,d,f,t)
print('PASS: 24 comparisons of full multivariate Hermite compression and radial Jacobi matrix')
for r in (100,500,2000,8000):
 for c in (.5,1.,2.):
  d=max(1,round(c*math.sqrt(r)))
  lam=radial_eig(r,d)
  lb=(math.sqrt(r+d)-math.sqrt(r))**2
  print('r=%d d=%d c=%g lambda=%.9f prediction=%.9f lower=%.9f'%(r,d,c,lam,c*c/4,lb))

print('PASS: all finite-dimensional checks completed')
