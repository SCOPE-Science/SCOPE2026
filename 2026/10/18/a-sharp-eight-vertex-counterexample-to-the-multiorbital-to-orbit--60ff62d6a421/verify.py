import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from collections import defaultdict
from functools import lru_cache
from time import perf_counter
T0=perf_counter()

def multiply(a,b):
 z=defaultdict(int)
 for (i,j),v in a.items():
  for (k,l),w in b.items():z[(i+k,j+l)]+=v*w
 return {p:c for p,c in z.items() if c}

def prep(n):
 dp={}
 for k in range(n+1):
  for t in range(k+1):
   v={(0,0):1}
   for i in range(t):v=multiply(v,{(1,0):1,(0,1):-1,(0,0):-i})
   for j in range(k-t):v=multiply(v,{(1,0):1,(0,0):-(t+j)})
   dp[(k,t)]=v
 return dp

@lru_cache(None)
def partitions(n):
 if n==0:return ((),)
 out=[]
 for part in partitions(n-1):
  out.append(part+(1<<(n-1),))
  for i in range(len(part)):
   q=list(part);q[i]|=1<<(n-1);out.append(tuple(q))
 return tuple(out)

cache={}
def poly(n,edges):
 key=(n,tuple(sorted((min(a,b),max(a,b)) for a,b in edges)))
 if key in cache:return cache[key]
 edgeblocks=[(1<<a)|(1<<b) for a,b in edges]
 forced=[False]*(1<<n)
 for s in range(1<<n):
  forced[s]=any((e&s)==e for e in edgeblocks)
 cnt=defaultdict(int)
 for partition in partitions(n):
  t=sum(forced[b] for b in partition)
  cnt[(len(partition),t)]+=1
 out=defaultdict(int);basis=prep(n)
 for kt,cnt0 in cnt.items():
  for xy,v in basis[kt].items():out[xy]+=cnt0*v
 res=tuple(sorted((a,b,c) for (a,b),c in out.items() if c))
 cache[key]=res
 return res

def linear(p,q,a):
 z=defaultdict(int)
 for x,y,v in p:z[x,y]+=a*v
 for x,y,v in q:z[x,y]+=v
 return tuple(sorted((x,y,v) for (x,y),v in z.items() if v))

def quotient(n,E,p):
 orbits=[]; seen=set()
 for v in range(n):
  if v in seen:continue
  chain=[];u=v
  while u not in seen:seen.add(u);chain.append(u);u=p[u]
  orbits.append(chain)
 f={v:i for i,c in enumerate(orbits) for v in c}
 return len(orbits),tuple(sorted(set(tuple(sorted((f[a],f[b]))) for a,b in E)))


# The two explicitly specified eight-vertex C2-graphs.
A = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 6), (0, 7), (1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (6, 7)]
B = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6), (5, 6), (6, 7)]
tau=(1,0,2,3,4,5,6,7)

def minus(p,q):
 from collections import defaultdict
 z=defaultdict(int)
 for a,b,c in p:z[a,b]+=c
 for a,b,c in q:z[a,b]-=c
 return tuple(sorted((a,b,c) for (a,b),c in z.items() if c))

def evaluate(P,x,y):return sum(c*x**a*y**b for a,b,c in P)

P0,P1=poly(8,A),poly(8,B)
Q0=poly(*quotient(8,A,tau));Q1=poly(*quotient(8,B,tau))
F0,F1=linear(P0,Q0,3),linear(P1,Q1,3)
O0,O1=linear(P0,Q0,1),linear(P1,Q1,1)
assert F0==F1 and O0!=O1
pd=minus(P0,P1);qd=minus(Q0,Q1)
assert qd==tuple(sorted((a,b,-3*c) for a,b,c in pd))
assert evaluate(minus(O0,O1),3,1)==128  # doubled orbital difference
print('EXPLICIT_C2_COUNTEREXAMPLE_OK; orbital difference at (3,1):',evaluate(minus(O0,O1),3,1)//2)

# Complete graph atlas up to seven vertices, preserving only distinct quotient polynomials
# for each graph (the fixed identity term is unchanged within that graph).
stored={};cases=0;automorphisms=0;atlas_count=0
for G in nx.graph_atlas_g():
 n=G.number_of_nodes()
 if n<2 or n>7:continue
 atlas_count+=1
 E=tuple(sorted((min(a,b),max(a,b)) for a,b in G.edges()))
 P=poly(n,E);foundQ=set()
 for iso in GraphMatcher(G,G).isomorphisms_iter():
  p=tuple(iso[v] for v in range(n))
  if p==tuple(range(n)) or any(p[p[v]]!=v for v in range(n)):continue
  automorphisms+=1
  nq,eq=quotient(n,E,p);Q=poly(nq,eq)
  if Q in foundQ:continue
  foundQ.add(Q)
  F=linear(P,Q,3); O=linear(P,Q,1);k=(n,F)
  if k in stored:assert stored[k]==O, 'smaller counterexample detected'
  else:stored[k]=O
  cases+=1
assert atlas_count==1251 and cases==2729
print('MINIMALITY_OK; graph atlas members of orders 2..7:',atlas_count,'distinct action quotient cases:',cases)
print('VERIFICATION_OK')
