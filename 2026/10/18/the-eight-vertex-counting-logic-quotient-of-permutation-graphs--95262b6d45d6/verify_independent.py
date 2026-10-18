import itertools,collections,hashlib,time,networkx as nx,sys

def graph(p):
 n=len(p);A=[0]*n
 for i in range(n):
  for j in range(i+1,n):
   if p[i]>p[j]:A[i]|=1<<j;A[j]|=1<<i
 return tuple(A)

def wl(A):
 n=len(A);colors=[0]*n
 for k in range(n+1):
  keys=[(colors[i],tuple(sorted(colors[j] for j in range(n) if A[i]>>j&1))) for i in range(n)]
  colors=[int.from_bytes(hashlib.blake2b(repr(key).encode(),digest_size=10).digest(),'big') for key in keys]
 return tuple(sorted(collections.Counter(colors).items()))

def nxg(A):
 g=nx.Graph();n=len(A);g.add_nodes_from(range(n));g.add_edges_from((i,j) for i in range(n) for j in range(i+1,n) if A[i]>>j&1);return g
for n in range(1,9):
 T=time.monotonic();parts=collections.defaultdict(list)
 for p in itertools.permutations(range(n)):
  A=graph(p);parts[wl(A)].append(A)
 nontrivial=[];distinct=0
 for sign,vs in parts.items():
  reps=[];gr=[]
  for a in vs:
   g=nxg(a)
   if not any(nx.is_isomorphic(g,h) for h in gr):
    gr.append(g);reps.append(a)
  distinct+=len(reps)
  if len(reps)>1:nontrivial.append(reps)
 print('n',n,'permutations',__import__('math').factorial(n),'iso',distinct,'C2classes',len(parts),'nonsingleton',len(nontrivial),'shapes',collections.Counter(map(len,nontrivial)),flush=True)
 if nontrivial: print('FIRSTEX',nontrivial[:3],flush=True)
