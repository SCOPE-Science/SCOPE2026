import numpy as np

def rankmod(mat,p):
 a=np.array(mat,dtype=np.int64)%p
 if a.ndim<2:return 0
 m,n=a.shape;r=0
 for j in range(n):
  piv=next((k for k in range(r,m) if a[k,j]%p),None)
  if piv is None:continue
  a[[r,piv]]=a[[piv,r]]
  a[r] = (a[r]*pow(int(a[r,j]),-1,p))%p
  for k in range(m):
   if k!=r and a[k,j]:a[k]=(a[k]-a[k,j]*a[r])%p
  r+=1
  if r==m:break
 return r

def matrices(H,p):
 r=H.shape[0]; n=4*r
 A=np.zeros((n,n),dtype=int);B=A.copy();I=np.eye(r,dtype=int)
 A[0:r,2*r:3*r]=I; A[r:2*r,3*r:4*r]=I
 B[0:r,r:2*r]=H; B[2*r:3*r,3*r:4*r]=I
 return A,B

def centralizer_dimension(A,B,p):
 n=len(A); cols=[]
 for i in range(n):
  for j in range(n):
   E=np.zeros((n,n),dtype=int);E[i,j]=1
   col=np.concatenate(((E@A-A@E).ravel(),(E@B-B@E).ravel()))
   cols.append(col)
 return n*n-rankmod(np.array(cols).T,p)

for H in [np.eye(2,dtype=int),np.array([[1,0],[0,2]]),np.array([[1,1],[0,1]])]:
 A,B=matrices(H,3)
 C=centralizer_dimension(A,B,3)
 print(H.tolist(),'centralizer_alg_dim',C)
 assert C== (16 if np.array_equal(H,np.eye(2,dtype=int)) else 14)
print('VERIFY_CENTRALIZER_OK')
