from itertools import product
import heapq,random,math

def all_tree_edges(code,N):
 deg=[1]*N
 for i in code: deg[i]+=1
 heap=[i for i in range(N) if deg[i]==1];heapq.heapify(heap)
 edges=[]
 for u in code:
  v=heapq.heappop(heap);edges.append((u,v));deg[u]-=1;deg[v]-=1
  if deg[u]==1:heapq.heappush(heap,u)
 v=heapq.heappop(heap);u=heapq.heappop(heap);edges.append((u,v))
 return edges

def cost_tree(edges,coeff,p,r,N):
 adj=[[] for _ in range(N)]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 parent=[-1]*N;order=[0];parent[0]=0
 for a in order:
  for b in adj[a]:
   if parent[b]<0:parent[b]=a;order.append(b)
 mass=coeff[:]
 cost=0
 center=N-1
 for a in reversed(order[1:]):
  b=parent[a];w=r if a==center or b==center else 1
  cost+=w**p *abs(mass[a])**p
  mass[b]+=mass[a]
 return cost

def analytic(coeff,p,r):
 k=len(coeff)-2
 s=sum(x**p for x in coeff[1:-1]); mn=s
 for mask in range(1,1<<k):
  arr=[coeff[i+1] for i in range(k) if mask>>i&1]
  q=sum(x**p for x in arr)
  val=s-q+r**p*(q+sum(arr)**p)
  mn=min(mn,val)
 return mn
p=.5;r=.5;k=5;N=k+2
vectors=[[1]*k,[1,2,3,4,5],[1,1,1,1,50],[.01,.1,1,10,100],[1,2,3,1,4]]
vals=[math.inf]*len(vectors)
for code in product(range(N),repeat=N-2):
 e=all_tree_edges(code,N)
 for idx,v in enumerate(vectors):
  coeff=[-sum(v),*v,0];val=cost_tree(e,coeff,p,r,N)
  if val<vals[idx]:vals[idx]=val
for v,obt in zip(vectors,vals):
 expect=analytic([-sum(v),*v,0],p,r)
 print(v,'brute',round(obt,12),'formula',round(expect,12),'diff',obt-expect)
assert all(abs(x-analytic([-sum(v),*v,0],p,r))<1e-8 for x,v in zip(vals,vectors))
print('PASS exhaustive all 7^5 trees times 5 vectors')
