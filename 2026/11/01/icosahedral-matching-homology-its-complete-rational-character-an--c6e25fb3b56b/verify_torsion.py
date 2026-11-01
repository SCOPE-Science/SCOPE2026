import itertools, collections
E=[(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),(9,10),(10,11)]
# antipodal from graph BFS
def ant_of(u):
 ss={u};front={u}
 for d in range(3):
  nxt={b if a in front else a for a,b in E if (a in front)!=(b in front)}-ss
  ss|=nxt;front=nxt
 assert len(front)==1,(u,front)
 return next(iter(front))
ant=tuple(ant_of(i) for i in range(12))
idx={e:i for i,e in enumerate(E)}
q=tuple(idx[tuple(sorted((ant[a],ant[b])))] for a,b in E)
faces={0:[()]}
for k in range(1,7):
 faces[k]=[c for c in itertools.combinations(range(30),k) if len({i for e in c for i in E[e]})==2*k]
print('ant',ant)
def act(f):
 b=[q[i] for i in f]
 inv=sum(b[i]>b[j] for i in range(len(b)) for j in range(i+1,len(b)))
 return tuple(sorted(b)), (-1 if inv%2 else 1)
# eigenbasis dictionaries orbits mapped to representative and sign for rep orientation
basis={}
lookup={}
for k in range(0,7):
 b={-1:[],1:[]};look={-1:{},1:{}}
 for f in faces[k]:
  p,s=act(f)
  if f>p:continue
  if f==p:
   b[s].append((f,p,s))
  else:
   for z in (-1,1): b[z].append((f,p,s))
 for z in (-1,1):
  look[z]={f:i for i,(f,p,s) in enumerate(b[z])}
 basis[k]=b;lookup[k]=look
print('Ck eigen dimensions',[(k,len(basis[k][1]),len(basis[k][-1])) for k in range(1,7)])
def rank_k(k,z):
 r=lookup[k-1][z];pivots={};mod=3
 for f,p,s in basis[k][z]:
  x={}
  for tup,coeff in ((f,1), (p,z*s)) if p!=f else ((f,1),):
   for j in range(len(tup)):
    low=tup[:j]+tup[j+1:]
    if low in r:
     rid=r[low];x[rid]=(x.get(rid,0)+coeff*((-1)**j))%mod
  x={i:v for i,v in x.items() if v%mod}
  while x:
   row=max(x)
   if row not in pivots:
    inv=pow(x[row],-1,mod);pivots[row]={q:v*inv%mod for q,v in x.items()};break
   w=pivots[row];a=x[row]
   for q,v in w.items():
    x[q]=(x.get(q,0)-a*v)%mod
    if not x[q]:x.pop(q,None)
 return len(pivots)
for z in [1,-1]:
 rank={k:rank_k(k,z) for k in range(1,7)}
 print('eigen',z,'ranks',rank,'betti',[len(basis[k][z])-rank[k]-rank.get(k+1,0) for k in range(1,7)])
assert len(faces[4])==2535
assert [len(basis[k][1]) for k in range(1,7)]==[15,150,700,1290,741,55]
assert [len(basis[k][-1]) for k in range(1,7)]==[15,165,700,1245,741,70]
assert [rank_k(k,1) for k in range(1,7)]==[1,14,136,564,686,55]
assert [rank_k(k,-1) for k in range(1,7)]==[0,15,150,550,670,70]
print('VERIFY_TORSION_OK')
