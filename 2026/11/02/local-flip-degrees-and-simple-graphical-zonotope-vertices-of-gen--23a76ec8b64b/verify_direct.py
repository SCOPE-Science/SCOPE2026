import itertools,collections,math

def make(lengths):
 E=[]; s=0;t=1;nxt=2
 for length in lengths:
  path=[s]+list(range(nxt,nxt+length-1))+[t];nxt+=length-1
  E.extend(zip(path,path[1:]))
 return list(E),nxt

def DAG(edges,n,mask):
 adj=[[] for _ in range(n)]; indeg=[0]*n
 for i,(u,v) in enumerate(edges):
  if mask & (1<<i):u,v=v,u
  adj[u].append(v);indeg[v]+=1
 stack=[i for i,d in enumerate(indeg) if d==0];count=0
 while stack:
  u=stack.pop();count+=1
  for v in adj[u]:
   indeg[v]-=1
   if indeg[v]==0:stack.append(v)
 return count==n

def formula(ls):
 m=len(ls); E=sum(ls)
 # polynomial over number of non-reversible edges
 def mul(P,Q):
  R=[0]*(len(P)+len(Q)-1)
  for i,a in enumerate(P):
   for j,b in enumerate(Q):R[i+j]+=a*b
  return R
 p=[1];q=[1]
 for l in ls:
  t=2**l-l-2
  p=mul(p,[1+t,l]);q=mul(q,[t,l])
 return {E-d:(2*(p[d]-q[d])+(math.prod(2**r-2 for r in ls) if d==0 else 0)) for d in range(m+1) if 2*(p[d]-q[d])+(math.prod(2**r-2 for r in ls) if d==0 else 0)>0}

cnt=0
for m in range(3,7):
 for ls in itertools.combinations_with_replacement(range(2,6),m):
  if sum(ls)>12:continue
  for lss in (ls, ((1,)+ls[1:]) if ls[1]>=2 else ls):
   if lss!=ls and len(lss)!=m: continue
   edges,n=make(lss); E=len(edges); observed=collections.Counter()
   for mask in range(1<<E):
    if DAG(edges,n,mask):
     d=sum(DAG(edges,n,mask^(1<<i)) for i in range(E))
     observed[d]+=1
   expected=formula(lss)
   assert dict(observed)==expected,(lss,observed,expected)
   tau=sum(math.prod(lss[j] for j in range(m) if j!=i) for i in range(m))
   assert observed[n-1]==2*tau,(lss,observed,n,2*tau)
   cnt+=1
print('GENERAL_THETA_DIRECT_CHECK_PASS cases=',cnt)
for lengths in [(2,2,2),(2,3,4),(3,3,3),(2,2,2,2),(1,2,3,4),(2,2,2,2,2)]:
 print(lengths,formula(lengths))
