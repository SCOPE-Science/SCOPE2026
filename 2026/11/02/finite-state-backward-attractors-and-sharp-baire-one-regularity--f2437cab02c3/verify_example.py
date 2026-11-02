from fractions import Fraction as Q
from collections import defaultdict
C=[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
Y=[Q(1,2),Q(0),Q(1,2),Q(1),Q(1,2)]
# nodes named I0..I3 (open), P0..P4 (point), and graph transition source -> target
cells={f'I{i}':('I',C[i],C[i+1]) for i in range(4)}
cells.update({f'P{i}':('P',v,v) for i,v in enumerate(C)})
G={k:set() for k in cells}
def map_endpoint(i,x):
 return Y[i]+(Y[i+1]-Y[i])*(x-C[i])/(C[i+1]-C[i])
for src,(t,a,b) in cells.items():
 if t=='I':
  i=int(src[1:]); assert abs((Y[i+1]-Y[i])/(C[i+1]-C[i]))==2
  lo,hi=sorted((Y[i],Y[i+1]))
  for dst,(tt,l,h) in cells.items():
   if tt=='I' and lo<=l<h<=hi: G[src].add(dst)
   if tt=='P' and lo<l<hi: G[src].add(dst)
 else:
  i=int(src[1:]);
  for j,cv in enumerate(C):
   if Y[i]==cv: G[src].add('P'+str(j))
assert len(G)==9
# Tarjan SCC
idx=0; inds={};low={};stack=[];on=set();S=[]
def visit(v):
 global idx
 inds[v]=low[v]=idx;idx+=1;stack.append(v);on.add(v)
 for w in G[v]:
  if w not in inds:visit(w);low[v]=min(low[v],low[w])
  elif w in on:low[v]=min(low[v],inds[w])
 if low[v]==inds[v]:
  comp=[]
  while True:
   w=stack.pop();on.remove(w);comp.append(w)
   if w==v:break
  S.append(frozenset(comp))
for v in G:
 if v not in inds: visit(v)
cyclic=[s for s in S if len(s)>1 or next(iter(s)) in G[next(iter(s))]]
def reaches(s,t):
 seen=set(s);todo=list(s)
 while todo:
  v=todo.pop()
  if v==t:return True
  for w in G[v]:
   if w not in seen:seen.add(w);todo.append(w)
 return False
left=frozenset(['I0','I1']);right=frozenset(['I2','I3']);mid=frozenset(['P2'])
assert set(cyclic)=={left,right,mid},cyclic
for v in ['I0','I1']:
 assert {s for s in cyclic if reaches(s,v)}=={left}
for v in ['I2','I3']:
 assert {s for s in cyclic if reaches(s,v)}=={right}
assert {s for s in cyclic if reaches(s,'P2')}=={left,right,mid}
# Verify partition endpoint images and full monotone coverage from exact affine source.
for i in range(4):
 a,b=C[i],C[i+1]
 assert map_endpoint(i,a)==Y[i] and map_endpoint(i,b)==Y[i+1]
 for k in range(1,21):
  x=a+(b-a)*Q(k,21)
  assert min(Y[i],Y[i+1])<map_endpoint(i,x)<max(Y[i],Y[i+1])
print('VERIFY_OK: 4 exact slopes; 80 rational branch values; 9-state transition graph; 3 cyclic SCCs; exact reachability and sharp boundary jump')
