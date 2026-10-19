from itertools import product
import numpy as np
P=3

def rref(M):
 A=np.array(M,dtype=np.int64)%P;rows,cols=A.shape; r=0
 for c in range(cols):
  i=next((i for i in range(r,rows) if A[i,c]),None)
  if i is None:continue
  A[[r,i]]=A[[i,r]];A[r]=(A[r]*pow(int(A[r,c]),-1,P))%P
  for j in range(rows):
   if j!=r:A[j]=(A[j]-A[j,c]*A[r])%P
  r+=1
  if r>=rows:break
 return tuple(A.ravel().tolist()),r

def inverse(A):
 C=np.concatenate((A%P,np.eye(len(A),dtype=np.int64)),axis=1)%P;n=len(A)
 for j in range(n):
  i=next(i for i in range(j,n) if C[i,j]); C[[j,i]]=C[[i,j]]
  C[j]=C[j]*pow(int(C[j,j]),-1,P)%P
  for k in range(n):
   if k!=j:C[k]=(C[k]-C[k,j]*C[j])%P
 return C[:,n:]

planes={}
for v in product(range(P),repeat=8):
 R=np.array(v,dtype=np.int64).reshape(2,4)
 key,rank=rref(R)
 if rank==2:planes[key]=np.array(key).reshape(2,4).T
print('planes',len(planes)); assert len(planes)==130
GL2=[]
for v in product(range(P),repeat=4):
 M=np.array(v,dtype=np.int64).reshape(2,2)
 if (int(M[0,0]*M[1,1]-M[0,1]*M[1,0])%P):GL2.append(M)
print('GL2',len(GL2));assert len(GL2)==48
A=np.zeros((4,4),dtype=np.int64);A[0,2]=1;A[1,3]=1
cnt=0;allB=0
for U in planes.values():
 W=[]
 for e in np.eye(4,dtype=np.int64).T:
  if rref(np.column_stack([U]+W+[e]).T)[1]>2+len(W):W.append(e)
  if len(W)==2:break
 Q=np.column_stack([U]+W);QI=inverse(Q)
 for F in GL2:
  B=(U@F@QI[2:4,:])%P
  assert not np.any(B@B%P)
  ab=A@B%P;ba=B@A%P
  kab,rab=rref(ab);kba,rba=rref(ba)
  if rab==1 and rba==1:
   # compare column spaces via RREF of transposes
   sa,_=rref(ab.T);sb,_=rref(ba.T)
   if sa==sb:cnt+=1
  allB+=1
print('enumerated B',allB,'extremal for fixed A',cnt,'expected',P*48)
assert allB==6240 and cnt==144
print('VERIFY_Q3_OK')
