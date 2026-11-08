import itertools, collections, math

def oracle(m):
  k=m-1
  adj=[set() for _ in range(2*m+1)]
  for i in range(1,m+1):
   for a,b in ((0,i),(i,i+m)):
    adj[a].add(b);adj[b].add(a)
  nodes=[]
  for xs in itertools.combinations(range(2*m+1),k):
   s=set(xs)
   if all(not(adj[x]&s) for x in s):nodes.append(xs)
  ix={v:i for i,v in enumerate(nodes)}; nb=[set() for _ in nodes]
  for u,s in enumerate(nodes):
   for a in s:
    for b in adj[a]-set(s):
     v=ix.get(tuple(sorted((set(s)-{a})|{b})))
     if v is not None:nb[u].add(v)
  return nodes,nb

def tp(m,s):
 s=set(s)
 if 0 in s:
  holes=tuple(i for i in range(1,m+1) if i+m not in s)
  assert len(holes)==2 and not any(1<=i<=m for i in s)
  return ('V',holes)
 h=next(i for i in range(1,m+1) if i not in s and i+m not in s)
 assert len([i for i in range(1,m+1) if i not in s and i+m not in s])==1
 A=frozenset(i for i in range(1,m+1) if i in s)
 return ('U',h,A)

def du(u,v):
 _,h,A=u;_,k,B=v
 return len(A^B) if h==k else len(A)+len(B)+4-2*(int(k in A)+int(h in B))

def guess(u,v):
 if u[0]=='U' and v[0]=='U':return du(u,v)
 if u[0]=='V' and v[0]=='V':
  if u==v:return 0
  return 2+min(du(('U',i,frozenset({j})),('U',a,frozenset({b}))) for i,j in (u[1],u[1][::-1]) for a,b in (v[1],v[1][::-1]))
 if u[0]=='V':u,v=v,u
 a,b=v[1]
 return 1+min(du(u,('U',a,frozenset({b}))),du(u,('U',b,frozenset({a}))))

def bfs(nb,i):
 d=[-1]*len(nb);d[i]=0;q=collections.deque([i]);
 while q:
  u=q.popleft()
  for v in nb[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 return d

for m in range(3,8):
 nodes,nb=oracle(m); tp_list=[tp(m,s) for s in nodes]
 assert len(nodes)==m*2**(m-1)+m*(m-1)//2
 assert sum(map(len,nb))//2==m*(m-1)*2**(m-2)+m*(m-1)
 ds=[]
 for i in range(len(nodes)):
  d=bfs(nb,i);ds.append(max(d))
  for j in range(len(nodes)):
   pred=guess(tp_list[i],tp_list[j]);assert pred==d[j],(m,i,j,tp_list[i],tp_list[j],pred,d[j])
 print('PASS',m,'vertices',len(nodes),'edges',sum(map(len,nb))//2,'radius',min(ds),'diam',max(ds))
print('ALL_PAIRS_PASS')
