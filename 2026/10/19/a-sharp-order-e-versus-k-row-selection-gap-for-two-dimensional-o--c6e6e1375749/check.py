import itertools,math
import numpy as np

def data(n):
 t=1/math.sqrt(4*n-11)
 a=2*math.sqrt(n-3)*t
 U=np.zeros((n,2)); U[0,0]=a; U[1,1]=2*t; U[2,0]=t; U[3,1]=t; U[4:,1]=2*t
 return U,t,a

def assess(U):
 v=[]
 for inds in itertools.combinations(range(len(U)),2):
  sv=np.linalg.svd(U[list(inds)],compute_uv=False)
  k=sv[0]/sv[1] if sv[1]>1e-12 else math.inf
  v.append((inds,sv[1],k))
 E=max(x[1] for x in v); best=[x for x in v if abs(x[1]-E)<1e-9]; K=min(x[2] for x in v)
 return E,best,K
for n in [5,6,7,11,23,50,100]:
 U,t,a=data(n)
 assert np.allclose(U.T@U,np.eye(2))
 E,best,K=assess(U)
 assert abs(E-2*t)<1e-10,(n,E,t)
 assert abs(K-1)<1e-10,(n,K)
 assert all(pair[0][0]==0 and pair[0][1] in [1,*range(4,n)] for pair in best)
 assert all(abs(pair[2]-math.sqrt(n-3))<1e-10 for pair in best)
 print('family',n,'E',round(E,8),'E selections',len(best),'kE',round(best[0][2],8),'kopt',round(K,8))
rng=np.random.default_rng(410021)
for n in range(3,26):
 for repeat in range(200):
  U=np.linalg.qr(rng.normal(size=(n,2)))[0]
  E,best,K=assess(U)
  assert E>=1/math.sqrt(2*(n-1))-1e-12,(n,repeat,E)
  assert best[0][2]/K<=math.sqrt(2*(n-1))+1e-12
print('PASS: 4,600 random orthonormal frames')
