from itertools import combinations
import numpy as np
p=3;n=7
edges=list(combinations(range(n),2));V={e:i for i,e in enumerate(edges)}
faces=[t for t in combinations(range(len(edges)),2) if len(set(edges[t[0]]+edges[t[1]]))==4]
faces3=[t for t in combinations(range(len(edges)),3) if len(set(edges[t[0]]+edges[t[1]]+edges[t[2]]))==6]
F={f:i for i,f in enumerate(faces)}
b1=np.zeros((len(edges),len(faces)),dtype='int64')
for j,(a,b) in enumerate(faces):b1[a,j]=-1;b1[b,j]=1
b2=np.zeros((len(faces),len(faces3)),dtype='int64')
for j,(a,b,c) in enumerate(faces3):b2[F[(b,c)],j]+=1;b2[F[(a,c)],j]-=1;b2[F[(a,b)],j]+=1
assert not np.any(b1@b2)
def rref(A):
 A=(A.copy()%p).astype('int64'); rows,cols=A.shape;rank=0;pv=[]
 for j in range(cols):
  idx=next((k for k in range(rank,rows) if A[k,j]%p),None)
  if idx is None:continue
  A[[rank,idx]]=A[[idx,rank]]
  A[rank]=(A[rank]*pow(int(A[rank,j]),-1,p))%p
  for k in range(rows):
   if k!=rank and A[k,j]:A[k]=(A[k]-A[k,j]*A[rank])%p
  pv.append(j);rank+=1
  if rank==rows:break
 return A,pv
def nullspace(A):
 R,pv=rref(A);free=[j for j in range(A.shape[1]) if j not in pv];out=[]
 for j in free:
  x=np.zeros(A.shape[1],dtype='int64');x[j]=1
  for k,q in enumerate(pv):x[q]=-R[k,j]%p
  assert not np.any((A@x)%p)
  out.append(x)
 return out

def rank(A):return len(rref(A)[1])
Z=nullspace(b2.T); B=b1
assert rank(B)==20
cohom=next((z for z in Z if rank(np.concatenate([B,z.reshape(1,-1)],axis=0))==21),None)
assert cohom is not None
trans=lambda v:1-v if v in (0,1) else v
# the cochain pullback (g^*c)(simplex) = signed coefficient c(g simplex)
def action(co):
 out=np.zeros_like(co)
 for j,(a,b) in enumerate(faces):
  g1=V[tuple(sorted(map(trans,edges[a])))];g2=V[tuple(sorted(map(trans,edges[b])))]
  s=1 if g1<g2 else -1
  out[j]=(s*co[F[tuple(sorted((g1,g2)))]])%p
 return out
image=action(cohom)
for lam in (1,-1):
 print('lambda',lam,'class_trivial?',rank(np.concatenate([B,((image-lam*cohom)%p).reshape(1,-1)],axis=0))==20)
print('counts',len(edges),len(faces),len(faces3),'ranks',rank(b1),rank(b2),'mod3 H1 dim',len(faces)-rank(b1)-rank(b2))
# In every top simplex an odd transposition fixes each matching vertex.
# It fixes the oriented simplex with +1, so a sign-isotypic chain has zero coefficient.
for (a,b,c) in faces3:
 first_edge=edges[a]
 t=first_edge
 assert t[0]!=t[1]
 def local_trans(x):return t[1] if x==t[0] else t[0] if x==t[1] else x
 assert all(V[tuple(sorted(map(local_trans,edges[k])))]==k for k in (a,b,c))
print('facet_stabilizer_obstruction',len(faces3),'checked')
print('UCT_middle_dim',len(faces3)-rank(b2),'UCT_left_dim',len(faces3)-rank(b2)-1)
print('VERIFY_OK')
