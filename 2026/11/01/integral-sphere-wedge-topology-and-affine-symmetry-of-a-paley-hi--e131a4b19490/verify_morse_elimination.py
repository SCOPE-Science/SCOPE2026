# Exact integer Morse boundary at the single critical 2-cell for Ind_2(P_17)
from collections import defaultdict,deque,Counter
import random,math
p=17;residues={i*i%p for i in range(1,p)}
adj=[sum(1<<j for j in range(p) if (j-i)%p in residues) for i in range(p)]
F={m for m in range(1,1<<p) if all((adj[i]&m).bit_count()<=1 for i in range(p) if m>>i&1)}
seed=57;order=list(range(p));random.Random(seed).shuffle(order)
rem=set(F);pairs=[]
for v in order:
 for m in sorted(rem):
  b=m|(1<<v)
  if not (m>>v)&1 and b in rem:
   rem.remove(m);rem.remove(b);pairs.append((m,b))
print('cells',len(F),'matching',len(pairs),'critical',Counter(m.bit_count()-1 for m in rem),'order',order)
tcrit=next(m for m in rem if m.bit_count()==3)
three={m for m in F if m.bit_count()==4};two={m for m in F if m.bit_count()==3}
m23={a:b for a,b in pairs if a.bit_count()==3}
print('matched2/3',len(m23),'critical triangle',tcrit,'critical tetrahedra',len([m for m in rem if m.bit_count()==4]))

def sign_face(b,a):
 assert a & b==a and b.bit_count()-a.bit_count()==1
 v=next(i for i in range(p) if (b>>i)&1 and not ((a>>i)&1))
 return (-1)**((b&((1<<v)-1)).bit_count())
# For each triangle, tetrahedra containing it
cofac=defaultdict(list)
for b in three:
 for v in range(p):
  if b>>v&1:
   a=b^(1<<v);cofac[a].append(b)
# Directed dependency on tetrahedra from matched (a,b) to all other containing a
out=defaultdict(set);deg={b:0 for b in three}
for a,b in m23.items():
 for other in cofac[a]:
  if other!=b and other not in out[b]:out[b].add(other);deg[other]+=1
q=deque(b for b in three if deg[b]==0);topo=[]
while q:
 b=q.popleft();topo.append(b)
 for d in out[b]:
  deg[d]-=1
  if deg[d]==0:q.append(d)
assert len(topo)==len(three),(len(topo),len(three))
cols={b:{b^(1<<v):sign_face(b,b^(1<<v)) for v in range(p) if b>>v&1} for b in three}
active=set(three)
for b in topo:
 a=next((x for x,y in m23.items() if y==b),None)
 if a is None:continue
 v=cols[b].get(a,0)
 assert abs(v)==1,(a,b,v)
 for b2 in active-{b}:
  w=cols[b2].get(a,0)
  if w:
   for a2,coeff in cols[b].items():
    z=cols[b2].get(a2,0)-w*v*coeff
    if z:cols[b2][a2]=z
    elif a2 in cols[b2]:del cols[b2][a2]
 active.remove(b)
 cols[b].clear()
critical3=[b for b in rem if b.bit_count()==4]
degs=[cols[b].get(tcrit,0) for b in critical3]
print('Morse boundary critical3->critical2',Counter(degs),'gcd',math.gcd(*degs),'abs max',max(map(abs,degs)))
# all entries at unpaired higher 2cells (perhaps paired 1/2) allowed
print('remaining tetrahedra',len(active),'nonzero counts',Counter(len(cols[b]) for b in critical3))
