from collections import Counter,defaultdict,deque
from itertools import product
from functools import lru_cache
E=(1,2,4,8)
ID=E

def apply(A,x):
    z=0
    for j in range(4):
        if (x>>j)&1:z^=A[j]
    return z

def mul(A,B):return tuple(apply(A,x) for x in B)

def invert(A):
    tab={apply(A,x):x for x in range(16)}
    if len(tab)!=16:raise Exception
    return tuple(tab[e] for e in E)

G=[]
for a in product(range(16),repeat=4):
    if len({apply(a,x) for x in range(16)})==16:G.append(a)
assert len(G)==20160
S=[]
for i in range(4):
 for j in range(4):
  if i!=j:
   z=list(E);z[i]^=E[j];S.append(tuple(z))
assert len(S)==12
I={a:invert(a) for a in S}
# direct conjugacy action for generators
seen=set();classes=[]
for initial in G:
 if initial in seen:continue
 queue=[initial];seen.add(initial)
 for a in queue:
  for s in S:
   x=mul(mul(s,a),I[s])
   if x not in seen:seen.add(x);queue.append(x)
 classes.append((initial,queue))
assert len(seen)==20160

# Cap masks
caps=set()
for mask in range(1<<15):
 v=[j+1 for j in range(15) if mask>>j&1]
 if not any((mask>>( (a^b)-1))&1 for i,a in enumerate(v) for b in v[i+1:]):caps.add(mask)
assert len(caps)==3049

def get_orbits(A):
 remain=set(range(1,16));orbits=[]
 while remain:
  x=next(iter(remain));o=[];y=x
  while y not in o:
   o.append(y);remain.remove(y);y=apply(A,y)
  assert y==x
  orbits.append(o)
 return orbits

def char(A):
 orbs=get_orbits(A);masks=[sum(1<<(x-1) for x in o) for o in orbs]
 # coefficient as sum over valid orbit unions (-1)^(orbits)
 ans=0
 for choice in range(1<<len(orbs)):
  face=0
  for j,orb in enumerate(masks):
   if choice>>j&1:face|=orb
  if face in caps:ans+=(-1)**(choice.bit_count())
 return -ans

def oriented_fixed_face_character(A):
 # Independent test using the sign of the induced permutation on every
 # invariant oriented simplex; subtract one for reduced homology.
 result=-1
 for face in caps:
  if face==0:continue
  v=[j+1 for j in range(15) if face>>j&1]
  images=[apply(A,x) for x in v]
  if set(images)!=set(v):continue
  inversions=sum(images[i]>images[j] for i in range(len(v)) for j in range(i+1,len(v)))
  result+=(-1)**(len(v)-1+inversions)
 return result

out=[]
for rep,cl in classes:
 orbits=get_orbits(rep);lens=tuple(sorted(Counter(map(len,orbits)).items()))
 order=1
 from math import lcm
 for o in orbits:order=lcm(order,len(o))
 print('size',len(cl),'order',order,'point_cycles',lens,'chi',char(rep),'rep',rep,flush=True)
 out.append((len(cl),order,lens,char(rep),rep))
assert all(oriented_fixed_face_character(rep)==char(rep) for rep,_ in classes)
print('independent signed fixed-face tests:',len(classes))
print('classes',len(classes),'total',sum(c[0] for c in out),'weighted trace',sum(a*d for a,_,_,d,_ in out),'invariants',sum(a*d for a,_,_,d,_ in out)//20160)
assert sum(a*d for a,_,_,d,_ in out)%20160==0
ref={a:i for i,(rep,cl) in enumerate(classes) for a in cl}
for a in G:
 assert char(a)==out[ref[a]][3]
print('all-group characters checked',len(G))

print("ALL_CHECKS_PASS")
