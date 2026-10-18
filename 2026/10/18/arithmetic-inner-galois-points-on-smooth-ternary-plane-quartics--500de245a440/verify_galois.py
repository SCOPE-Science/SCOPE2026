import itertools, numpy as np, collections, math, json
p=3
exps=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
idx={e:k for k,e in enumerate(exps)}
P=[]
def norm(v):
 v=tuple(int(x)%3 for x in v);q=next((x for x in v if x),0);return tuple(x*pow(q,-1,3)%3 for x in v) if q else v
P=sorted({norm(v) for v in itertools.product(range(3),repeat=3) if any(v)})
# linear form arithmetic coefficient as map monomial exponent -> int
one={(0,0,0):1}
def times(a,b):
 out={}
 for e,v in a.items():
  for f,w in b.items():
   g=tuple(e[i]+f[i] for i in range(3));out[g]=(out.get(g,0)+v*w)%3
 return {e:v for e,v in out.items() if v}
def power(a,n):
 o=one
 for i in range(n):o=times(o,a)
 return o
def matrix(m):
 # substitution variables x=> rows m (input y), so polynomial F(m x) 3 rows
 forms=[{tuple(int(k==j) for k in range(3)): int(m[i,j])%3 for j in range(3) if m[i,j]%3} for i in range(3)]
 pp=[[power(forms[i],d) for d in range(5)] for i in range(3)]
 arr=np.zeros((15,15), dtype=np.int16)
 for a,e in enumerate(exps):
  prod=times(times(pp[0][e[0]],pp[1][e[1]]),pp[2][e[2]])
  for f,v in prod.items():arr[idx[f],a]=v
 return arr
D=lambda m: int(m[0,0]*(m[1,1]*m[2,2]-m[1,2]*m[2,1])-m[0,1]*(m[1,0]*m[2,2]-m[1,2]*m[2,0])+m[0,2]*(m[1,0]*m[2,1]-m[1,1]*m[2,0]))%3
# GL3 reps for each axis and center
reps={}
for vals in itertools.product(range(3),repeat=9):
 mm=np.array(vals,dtype=int).reshape(3,3)
 if D(mm)==0:continue
 # center mm * e_x = first col; axis from inverse second row
 det=D(mm)
 cof=np.array([[mm[(j+1)%3,(k+1)%3]*mm[(j+2)%3,(k+2)%3]-mm[(j+1)%3,(k+2)%3]*mm[(j+2)%3,(k+1)%3] for k in range(3)] for j in range(3)],dtype=int)
 inv=(cof.T*pow(int(det),-1,3))%3
 key=(norm(mm[:,0]),norm(inv[1,:]))
 if key not in reps:reps[key]=(mm,inv)
 if len(reps)==52:break
print('reps',len(reps));assert len(reps)==52
# canonical F from L=Y,M=aY+Z or Y. Use polynomial arithmetic
X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
def cadd(a,b,s=1):
 r=a.copy()
 for e,v in b.items():r[e]=(r.get(e,0)+s*v)%3
 return {e:v for e,v in r.items() if v}
def scale(a,s):return {e:(v*s)%3 for e,v in a.items() if v*s%3}
base=cadd(power(X,3),times(X,power(Y,2)),s=-1)
C=[]
for a in ['inf',0,1,2]:
 M=Y if a=='inf' else cadd(Z,Y,s=a)
 # for M=Y, nonzero Z4 coefficient, others arbitrary; M =Z+aY, require U4 and U V3 coeff!=0
 V=Z if a=='inf' else M
 for cs in itertools.product(range(3),repeat=5):
  if a=='inf':
   if cs[-1]==0:continue
  else:
   if cs[0]==0 or cs[3]==0:continue
  H={}
  for i,c in enumerate(cs):
   mon=times(power(Y,4-i),power(V,i))
   H=cadd(H,mon,s=c)
  F=cadd(times(base,M),H)
  cv=tuple(F.get(e,0)%3 for e in exps)
  assert cv[idx[(3,1,0)]] !=0 or cv[idx[(3,0,1)]]!=0
  C.append(cv)
assert len(C)==486,len(C)
print('canonical',len(C))
# vectorized projective normalize
C=np.asarray(C,dtype=np.int16).T
res=collections.defaultdict(set)
for key,(mm,inv) in reps.items():
 mat=matrix(inv)
 im=(mat@C)%3
 for i in range(im.shape[1]):
  u=im[:,i];leading=next(x for x in u if x);u=(u*pow(int(leading),-1,3))%3
  res[tuple(map(int,u))].add(key[0])
print('unique curves',len(res),'occurrences',sum(len(v) for v in res.values()))
counts=collections.Counter(map(len,res.values()));print('num rational inner galois points',counts)
for k in sorted(counts):
 v=next(u for u,pts in res.items() if len(pts)==k)
 print('rep k',k,v,'points',res[v]);
with open('galois_output.json','w') as f:json.dump({'counts':dict(counts),'reps':{str(k):list(next(u for u,pts in res.items() if len(pts)==k)) for k in sorted(counts)},'total':len(res)},f)
# projective equivalence classes via GL3 generators
G=[[[0,1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,1],[0,1,0]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]
A=list(res);ind={a:i for i,a in enumerate(A)}
Mats=[matrix(np.array(g)) for g in G]
seen=set();orbs=collections.defaultdict(list)
for i,u in enumerate(A):
 if i in seen:continue
 todo=[i];seen.add(i)
 for ii in todo:
  v=np.array(A[ii],dtype=np.int16)
  for M in Mats:
   w=(M@v)%3
   w=tuple(int(x*pow(int(next(c for c in w if c)), -1,3)%3) for x in w)
   assert w in ind,w
   k=ind[w]
   if k not in seen:seen.add(k);todo.append(k)
 cnt=len(res[u]);orbs[cnt].append((len(todo),u))
print('orbits of smooth quartics by Galois point count', {k:collections.Counter(n for n,r in vals) for k,vals in orbs.items()})
print('4 orbits',orbs[4]);print('1 orbits count',len(orbs[1]),'sizes',collections.Counter(s for s,u in orbs[1]));print('1 representatives',orbs[1])
with open('galois_output.json','w') as f:json.dump({'counts':dict(counts),'reps':{str(k):list(next(u for u,pts in res.items() if len(pts)==k)) for k in sorted(counts)},'total':len(res),'orbits':{str(k):[(s,list(u)) for s,u in v] for k,v in orbs.items()}},f)
