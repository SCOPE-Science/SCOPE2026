#!/usr/bin/env python3
"""Exact power-domination and minimum-set reconfiguration census for five graphs.
Run: python3 power_main.py  (stdlib only). All graphs indexed as described in RESULT.md.
"""
from itertools import combinations
from collections import deque,Counter
import json,hashlib,sys

def gp(n,k):
 return 2*n,[(i,(i+1)%n) for i in range(n)]+[(i,i+n) for i in range(n)]+[(n+i,n+(i+k)%n) for i in range(n)]
def heawood():
 return 14,[(i,7+j) for j in range(7) for i in (j,(j+1)%7,(j+3)%7)]
def pappus():
 return 18,[(3*x+y,9+3*m+b) for x in range(3) for y in range(3) for m in range(3) for b in range(3) if (y-m*x-b)%3==0]
def tutte():
 points=list(combinations(range(6),2));lines=[]
 def part(t):
  if not t: yield ();return
  x,*rest=t
  for y in rest:
   for p in part([z for z in rest if z!=y]):yield tuple(sorted(((x,y),)+p))
 lines=list(part(list(range(6))))
 return 30,[(i,15+j) for i,p in enumerate(points) for j,ln in enumerate(lines) if p in ln]
GRAPH={'H':heawood(),'MK':gp(8,3),'P':pappus(),'D':gp(10,3),'T':tutte()}

def bit_iter(m):
 while m:
  b=m&-m;yield b.bit_length()-1;m-=b

def closure(n,adj,seed):
 blue=seed
 for x in bit_iter(seed):blue|=adj[x]
 while True:
  new=blue
  for x in bit_iter(blue):
   outside=adj[x]&~blue
   if outside and (outside&(outside-1))==0:new|=outside
  if new==blue:return blue
  blue=new

def min_sets(n,adj):
 allmask=(1<<n)-1
 for k in range(1,6):
  good=[sum(1<<x for x in C) for C in combinations(range(n),k) if closure(n,adj,sum(1<<x for x in C))==allmask]
  if good:return k,good
 raise RuntimeError('minimum exceeds 5')

def exchange(good,adj,sliding):
 indices={m:i for i,m in enumerate(good)}
 n=len(adj);N=len(good);nexts=[[] for _ in range(N)]
 for i,m in enumerate(good):
  for x in bit_iter(m):
   for y in range(n):
    if m>>y&1 or (sliding and not (adj[x]>>y&1)):continue
    j=indices.get(m^(1<<x)^(1<<y))
    if j is not None:nexts[i].append(j)
  nexts[i].sort()
 return nexts

def perms_tutte_generators():
 pts=list(combinations(range(6),2));pd={q:i for i,q in enumerate(pts)}
 def part(t):
  if not t:yield ();return
  a,*r=t
  for b in r:
   for pp in part([z for z in r if z!=b]):yield tuple(sorted(((a,b),)+pp))
 lns=list(part(list(range(6))));ld={q:i for i,q in enumerate(lns)}
 gen=[]
 for j in range(5):
  p=list(range(6));p[j],p[j+1]=p[j+1],p[j]
  perm=[pd[tuple(sorted(p[z] for z in q))] for q in pts]
  perm += [15+ld[tuple(sorted(tuple(sorted(p[z] for z in pair)) for pair in L))] for L in lns]
  gen.append(perm)
 return gen

def orbits(good,name):
 if name!='T':return list(range(len(good))),list(range(len(good)))
 ind={m:i for i,m in enumerate(good)};g=perms_tutte_generators()
 # group generator actions: five adjacent transpositions generate S_6
 nxt=[[ind[sum(1<<perm[v] for v in bit_iter(m))] for m in good] for perm in g]
 orbit=[-1]*len(good);reps=[]
 for i in range(len(good)):
  if orbit[i]!=-1:continue
  orbit[i]=len(reps);reps.append(i);q=[i]
  for v in q:
   for genmap in nxt:
    u=genmap[v]
    if orbit[u]==-1:orbit[u]=orbit[i];q.append(u)
 return orbit,reps

def bfs(g,source):
 d=[-1]*len(g);d[source]=0;q=deque([source]);
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 return d

def describe(g,orbit=None,reps=None):
 N=len(g); seen=set();comps=[]
 for i in range(N):
  if i in seen:continue
  cc=bfs(g,i);part={j for j,x in enumerate(cc) if x>=0};comps.append(len(part));seen|=part
 if orbit is None or reps is None or len(reps)==0:reps=list(range(N));orbit=list(range(N))
 ecc=[0]*N; prof={}
 for rep in reps:
  d=bfs(g,rep)
  prof[rep]=Counter(d)
  val=max(d)
  ecc[rep]=val
 for i in range(N):ecc[i]=ecc[reps[orbit[i]]]
 return {'vertices':N,'edges':sum(map(len,g))//2,'components':sorted(comps),
         'degrees':dict(sorted(Counter(map(len,g)).items())),'radius':min(ecc),'diameter':max(ecc),
         'eccentricities':dict(sorted(Counter(ecc).items())),'orbit_representatives':len(reps),
         'distance_profile_reps':{str(r):dict(sorted(ct.items())) for r,ct in prof.items()}}

def run():
 answer={}; certificate={}
 for name,(n,edges) in GRAPH.items():
  adj=[0]*n
  for x,y in edges:adj[x]|=1<<y;adj[y]|=1<<x
  k,good=min_sets(n,adj)
  orbit,reps=orbits(good,name)
  jgraph=exchange(good,adj,False); sgraph=exchange(good,adj,True)
  rs={'order':n,'edges':len(edges),'gamma_P':k,'minimum_sets':len(good),
      'side_profiles':dict(sorted(Counter((m&((1<<(n//2))-1)).bit_count() for m in good).items())),
      'jump':describe(jgraph,orbit,reps),
      'slide':describe(sgraph,orbit,reps)}
  answer[name]=rs
  if '--certificate' in sys.argv:
   certificate[name]={'graph_edges':sorted([sorted([x,y]) for x,y in edges]),
        'minimum_sets':good,
        'jump_edges':[(i,j) for i,nb in enumerate(jgraph) for j in nb if i<j],
        'slide_edges':[(i,j) for i,nb in enumerate(sgraph) for j in nb if i<j]}
  print(name,'gamma',k,'minima',len(good),'jump',(rs['jump']['edges'],rs['jump']['radius'],rs['jump']['diameter']),
        'slide',(rs['slide']['edges'],rs['slide']['components'][:5],rs['slide']['radius'],rs['slide']['diameter']), 'orbits',len(reps),flush=True)
 if '--json' in sys.argv:
  with open('power_main_summary.json','w') as f:json.dump(answer,f,sort_keys=True,indent=2)
 if '--certificate' in sys.argv:
  with open('power_certificate.json','w',encoding='utf-8') as f:json.dump(certificate,f,sort_keys=True,separators=(',',':'))
 return answer
if __name__=='__main__':run()
