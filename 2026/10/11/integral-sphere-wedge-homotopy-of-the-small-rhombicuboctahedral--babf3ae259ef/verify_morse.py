from itertools import product
from collections import Counter,defaultdict,deque
from functools import lru_cache
verts=[(a,s) for a in range(3) for s in product((-1,1),repeat=3)]
edges=[]
for i,(a,s) in enumerate(verts):
 for j,(b,t) in enumerate(verts):
  if i>=j:continue
  if a==b and sum(x!=y for x,y in zip(s,t))==1 and s[a]==t[a]:edges.append((i,j))
  elif a!=b and s==t:edges.append((i,j))
assert len(verts)==24 and len(edges)==48
adj=[0]*24
for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
F=[0]
for k in range(24):F += [f|(1<<k) for f in F if not (f&adj[k])]
F=set(F);F.remove(0)
order=[23,22,17,4,13,8,2,6,18,20,1,21,19,11,3,10,9,0,15,16,5,7,12,14]
free=set(F);upper={};lower={}
for v in order:
 bit=1<<v
 for f in sorted(free):
  if f in free and not(f&bit):
   g=f|bit
   if g in free:
    free.remove(f);free.remove(g);upper[f]=g;lower[g]=f
assert len(F)==13874 and len(upper)==(13874-6)//2
assert Counter(f.bit_count()-1 for f in free)=={0:1,4:1,5:4}
print('critical',sorted((f.bit_count()-1,f) for f in free),'matching',len(upper))
# verify acyclicity via topo sort; natural Hasse oriented high to low except matching low to high.
faces=sorted(F);indeg={f:0 for f in faces};out=defaultdict(list);arcs=0
for f in faces:
 bits=[1<<k for k in range(24) if f&(1<<k)]
 if len(bits)==1:continue
 for b in bits:
  g=f^b
  if lower.get(f)==g:src,dst=g,f
  else:src,dst=f,g
  out[src].append(dst);indeg[dst]+=1;arcs+=1
q=deque(f for f in faces if indeg[f]==0)
seen=0
while q:
 f=q.popleft();seen+=1
 for g in out[f]:
  indeg[g]-=1
  if not indeg[g]:q.append(g)
print('acyclic',seen==len(faces),'incidences',arcs,'faces',len(faces))
assert seen==len(F)
@lru_cache(None)
def flowed(f):
 if f in free: return {f:1}
 if f in lower:return {}
 g=upper[f]
 # flow from f to all other facets of g
 b=g^f
 par=(f & (b-1)).bit_count()
 sign=1 if par%2==0 else -1
 result=defaultdict(int)
 for i in range(24):
  bit=1<<i
  if bit==b or not (bit&g): continue
  h=g^bit
  if not h:continue
  csign=1 if (g&(bit-1)).bit_count()%2==0 else -1
  for crit, coeff in flowed(h).items():result[crit]-=csign*sign*coeff
 return {x:y for x,y in result.items() if y}
def boundary(c):
 ret=defaultdict(int)
 for k in range(24):
  bit=1<<k
  if not c&bit:continue
  f=c^bit
  if not f:continue
  sgn=1 if (c&(bit-1)).bit_count()%2==0 else -1
  for face,coef in flowed(f).items():ret[face]+=sgn*coef
 return {x:y for x,y in ret.items() if y}
assert sorted(x for x in free if x.bit_count()==5)==[2163272]
assert sorted(x for x in free if x.bit_count()==6)==[99426,807456,2183304,3146889]
for c in sorted(free,key=lambda x:(x.bit_count(),x)):
 d=boundary(c)
 print('crit',c.bit_count()-1,c,'boundary',d)
 assert not d, (c,d)
print('Morse boundary zero in all degrees; integral homotopy wedge verified')
