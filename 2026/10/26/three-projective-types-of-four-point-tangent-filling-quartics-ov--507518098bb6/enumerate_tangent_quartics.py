from pathlib import Path
BASE = Path(__file__).resolve().parent
import numpy as np,itertools,time,collections
q=3
MON=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
assert len(MON)==15
P=[tuple(v) for v in itertools.product(range(3),repeat=3) if v!=(0,0,0) and next(c for c in v if c)!=2]
assert len(P)==13
L=[(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
pts=[]
for b,c in [(1,0),(0,1),(1,2),(1,1)]: # line Y*? + Z*? zero? choose directly
 pts.append([tuple((np.array((a,b,c))*(1 if a!=2 else 2)%3).tolist()) for a in range(3)])
assert all(len(p)==3 for p in pts)

def vals(v):return np.array([int(pow(v[0],i)*pow(v[1],j)*pow(v[2],k))%3 for i,j,k in MON],dtype=np.int16)
def grad(v,h):
 w=[]
 for s in range(3):
  z=[]
  for t in MON:
   p=list(t)
   if p[s]==0:z.append(0)
   else:
    co=p[s];p[s]-=1
    z.append(co*pow(v[0],p[0])*pow(v[1],p[1])*pow(v[2],p[2])%3)
  w.append(np.array(z,dtype=np.int16))
 return w

def null_basis(rows,n=15):
 A=np.array(rows,dtype=np.int16)%3
 piv=[];r=0
 for c in range(n):
  idx=next((i for i in range(r,A.shape[0]) if A[i,c]),None)
  if idx is None:continue
  A[[r,idx]]=A[[idx,r]]
  A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  for i in range(A.shape[0]):
   if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%3
  piv.append(c);r+=1
  if r==A.shape[0]:break
 free=[c for c in range(n) if c not in piv]
 B=[]
 for c in free:
  v=np.zeros(n,dtype=np.int16);v[c]=1
  for ii,p in enumerate(piv):v[p]=-A[ii,c]%3
  B.append(v)
 return np.array(B),len(piv)

PV=np.stack([vals(x) for x in P]);PG=[np.stack([grad(x,None)[s] for x in P]) for s in range(3)]
allq=np.array(list(itertools.product(range(3),repeat=7)),dtype=np.int16)
Pcenter=(1,0,0)
pts_plus=[]
for i in range(4):
 sets=[([Pcenter] if j==i else pts[j]) for j in range(4)]
 pts_plus.extend(itertools.product(*sets))
Pset=set(P)
results=[]; by_rank=collections.Counter(); pass_f4=0; arbitrary=0
st=time.time()
for tup in itertools.chain(itertools.product(*pts),pts_plus):
 rows=[]
 for v,(a,b,c) in zip(tup,L):
  g=grad(v,None)
  rows.extend([g[0],(c*g[1]-b*g[2])%3])
 B,r=null_basis(rows)
 by_rank[r]+=1
 if len(B)!=7: continue
 C=allq@B%3 # 2187 x 15
 pointzero=((C@PV.T)%3==0)
 cnt=pointzero.sum(axis=1)
 chosen=np.array([P.index(x) for x in tup])
 mask=(cnt==4)&np.all(pointzero[:,chosen],axis=1)
 sel=C[mask]
 arbitrary+=len(sel)
 for vector in sel:
  grads=np.array([g@vector%3 for g in PG]).T
  if np.any(np.all(grads[chosen]==0,axis=1)):continue
  tangent=set(tuple(grads[i]) for i in chosen)
  if len(tangent)!=4:continue
  # each gradient proportional to L for corresponding chosen by construction; verify coverage
  linecanon=set()
  for l in tangent:
   k=next(x for x in l if x)
   inv=1 if k==1 else 2
   linecanon.add(tuple(int(t*inv%3) for t in l))
  if len(linecanon)!=4:continue
  if not all(any(sum(x*y for x,y in zip(p,l))%3==0 for l in linecanon) for p in P):continue
  k=next(x for x in vector if x)
  inv=1 if k==1 else 2
  vv=tuple(int(t*inv%3) for t in vector)
  results.append((vv,tup))
print('time',round(time.time()-st,2),'ranks',by_rank,'four rational raw',arbitrary,'count contact solutions',len(results),'distinct',len(set(x[0] for x in results)))
print('first 12',list(dict.fromkeys(x[0] for x in results))[:12]);print('MON',MON);print('P',P)
open(str(BASE/'candidate_vectors.csv'),'w').write('\n'.join(','.join(map(str,x)) for x in sorted(set(x[0] for x in results)))+'\n')
