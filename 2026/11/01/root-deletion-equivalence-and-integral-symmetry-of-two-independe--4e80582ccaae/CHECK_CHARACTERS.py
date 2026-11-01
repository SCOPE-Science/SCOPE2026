import itertools

def make(q):
 m=len(q);groups=[];k=1+m
 for t in q:groups.append(list(range(k,k+t)));k+=t
 edges=[]
 for i,g in enumerate(groups):
  edges.append((0,1+i));edges += [(1+i,j) for j in g]
 masks=[]
 for b in range(1<<k):
  ds=[[] for _ in range(k)]
  for a,c in edges:
   if b>>a&1 and b>>c&1:ds[a].append(c);ds[c].append(a)
  vis=set();ok=True
  for a in range(k):
   if b>>a&1 and a not in vis:
    todo=[a];vis.add(a)
    for v in todo:
     for w in ds[v]:
      if w not in vis:vis.add(w);todo.append(w)
    if len(todo)>2:ok=False;break
  if ok:masks.append(b)
 return groups,masks,k

def sign_on(b,p):
 a=[i for i in range(len(p)) if b>>i&1]
 x=[p[i] for i in a]
 return -1 if sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))%2 else 1

def lef(g,faces):
 r=-1
 for b in faces:
  if b==0:continue
  c=sum(1<<g[i] for i in range(len(g)) if b>>i&1)
  if c==b:r+=(-1)**(b.bit_count()-1)*sign_on(b,g)
 return r

def model_trace(q,sigma,ps):
 m=len(q);seen=set();trace=1
 for i in range(m):
  if i in seen:continue
  j=i;f=list(range(q[i]))
  while j not in seen:
   seen.add(j)
   f=[ps[j][x] for x in f]
   j=sigma[j]
  assert j==i
  trace*=sum(k==x for k,x in enumerate(f))-1
 return trace

def run(q):
 m=len(q);groups,faces,n=make(q); checks=0
 for sigma in itertools.permutations(range(m)):
  if any(q[i]!=q[sigma[i]] for i in range(m)):continue
  for ps in itertools.product(*(itertools.permutations(range(q[i])) for i in range(m))):
   p=list(range(n));p[0]=0
   for i,j in enumerate(sigma):p[i+1]=j+1
   for i,ls in enumerate(groups):
    for x,v in enumerate(ls):p[v]=groups[sigma[i]][ps[i][x]]
   got=lef(p,faces)
   expected=-model_trace(q,sigma,ps)
   assert got==expected,(q,sigma,ps,got,expected)
   checks+=1
 print(q,checks,'elements checked, faces=',len(faces))
for q in [(2,2),(2,3),(2,2,2),(3,3)]:run(q)
