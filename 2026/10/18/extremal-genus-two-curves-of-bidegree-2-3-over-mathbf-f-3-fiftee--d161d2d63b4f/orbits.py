import itertools,numpy as np,collections,json
q=3
M=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
 if (a*d-b*c)%3==0:continue
 z=np.array([a,b,c,d],dtype=np.int64)
 z=z*(1 if next(x for x in z if x)!=2 else 2)%3
 if not any(np.array_equal(z,w) for w in M):M.append(z)
assert len(M)==24

def mul(p,q):
 r=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]=(r[i+j]+a*b)%3
 return r

def sympow(z,D):
 a,b,c,d=map(int,z)
 out=np.zeros((D+1,D+1),dtype=np.int64)
 for j in range(D+1):
  p=[1]
  for _ in range(D-j):p=mul(p,[a,b])
  for _ in range(j):p=mul(p,[c,d])
  out[:,j]=p
 return out
U=[sympow(z,2) for z in M]; S=[sympow(z,3) for z in M]
K=np.array([np.kron(u,s) for u in U for s in S],dtype=np.int16)
print('group',K.shape, flush=True)
D={}
with open('smooth_models.csv') as f:
 for line in f:
  a,b,c=map(int,line.strip().split(','));D[a]=(b,c)
seen=set(); orbs=[]
scale=np.array([3**i for i in range(12)],dtype=np.int64)
for n in D:
 if n in seen:continue
 v=np.array([(n//int(3**i))%3 for i in range(12)],dtype=np.int16)
 z=(K@v)%3
 nonzero=np.argmax(z!=0,axis=1)
 zz=z[np.arange(z.shape[0]),nonzero]
 z=z*np.where(zz==2,2,1)[:,None]%3
 keys=(z@scale).tolist();keys=set(keys)
 if any(k not in D for k in keys):raise Exception('image not smooth')
 seen.update(keys)
 N,r=D[n];orbs.append((n,N,r,len(keys)))
print('orbits',len(orbs),'covered',len(seen))
with open('orbit_reps.csv','w') as f:
 f.write('rep,N,r,orbit_size\n')
 for o in orbs:f.write(','.join(map(str,o))+'\n')
for n in range(9):
 hits=[o for o in orbs if o[1]==n]
 if hits:print('N',n,'classes',len(hits),'eqns',sum(o[-1] for o in hits),'sizes',collections.Counter(o[-1] for o in hits))
print('max reps:')
for o in orbs:
 if o[1]==8:print(o)
