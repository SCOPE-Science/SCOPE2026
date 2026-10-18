#!/usr/bin/env python3
"""Exact finite checks for the Chvatal graph higher-independence plateau.
No external dependencies. All incidence and homology calculations are exact.
"""
from collections import Counter, defaultdict, deque
N=12
EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),
 (2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),
 (5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),
 (9,10),(9,11))
assert len(EDGES)==24
ADJ=[0]*N
for u,v in EDGES:ADJ[u]|=1<<v;ADJ[v]|=1<<u
assert all(z.bit_count()==4 for z in ADJ)
assert all(not ADJ[u]&ADJ[v] for u,v in EDGES) # no triangles

def component_bound(mask,r):
 rem=mask
 while rem:
  bit=rem&-rem;rem-=bit;front=bit;size=0
  while front:
   b=front&-front;front-=b;size+=1
   if size>r:return False
   add=ADJ[b.bit_length()-1]&rem;front|=add;rem-=add
 return True

def independent_degree_two(mask):
 return all((ADJ[u]&mask).bit_count()<=1 for u in range(N) if mask&(1<<u))

STAGES={r:{m for m in range(1,1<<N) if component_bound(m,r)} for r in range(1,5)}
assert all(component_bound(m,2)==independent_degree_two(m) for m in range(1<<N))
EXPECTED={1:(12,42,52,20),2:(12,66,148,142,52,4),
          3:(12,66,220,282,132,16),4:(12,66,220,495,324,58)}
for r,faces in STAGES.items():
 vec=tuple(sum(m.bit_count()==d+1 for m in faces) for d in range(len(EXPECTED[r])))
 assert vec==EXPECTED[r],(r,vec)
 assert all((m^(m&-m)) in faces for m in faces if m.bit_count()>1)

def homology_mod2(faces):
 by_d=defaultdict(list)
 for m in faces:by_d[m.bit_count()-1].append(m)
 ranks={0:0}
 for d in range(1,max(by_d)+1):
  down={m:j for j,m in enumerate(by_d[d-1])};pivots={}
  for m in by_d[d]:
   z=0;bits=m
   while bits:
    b=bits&-bits;bits-=b;z^=1<<down[m^b]
   while z:
    p=z.bit_length()-1
    if p not in pivots:pivots[p]=z;break
    z^=pivots[p]
  ranks[d]=len(pivots)
 return {d:len(fs)-ranks[d]-ranks.get(d+1,0) for d,fs in by_d.items()}

assert homology_mod2(STAGES[2])=={0:1,1:0,2:0,3:1,4:0,5:0}
assert homology_mod2(STAGES[3])=={0:1,1:0,2:0,3:1,4:0,5:0}

def chvatal_ind2_morse():
 faces=sorted(STAGES[2]);available=set(faces);mate={}
 for v in reversed(range(N)):
  b=1<<v
  for low in faces:
   high=low|b
   if not low&b and low in available and high in available:
    available.remove(low);available.remove(high)
    mate[low]=high;mate[high]=low
 crit=Counter(m.bit_count()-1 for m in available)
 assert crit=={0:1,3:1} and len(mate)==422
 idx={face:i for i,face in enumerate(faces)}
 indeg=[0]*len(faces);out=[[] for _ in faces];incidences=0
 for high in faces:
  bits=high
  while bits:
   b=bits&-bits;bits-=b;low=high^b
   if not low:continue
   a,z=(high,low) if mate.get(low)==high else (low,high)
   out[idx[a]].append(idx[z]);indeg[idx[z]]+=1;incidences+=1
 q=deque(i for i,x in enumerate(indeg) if x==0);visited=0
 while q:
  i=q.popleft();visited+=1
  for j in out[i]:
   indeg[j]-=1
   if indeg[j]==0:q.append(j)
 assert visited==len(faces), 'closed gradient cycle'
 assert incidences==sum((d+1)*c for d,c in enumerate(EXPECTED[2]) if d>0)
 return len(mate)//2,incidences,crit

def collapse_3_to_2():
 remaining=STAGES[3].copy();target=STAGES[2];pairs=[]
 while remaining!=target:
  found=False
  for low in sorted(remaining-target,key=lambda x:(x.bit_count(),x)):
   cofaces=[low|(1<<v) for v in range(N) if not low&(1<<v) and low|(1<<v) in remaining]
   if len(cofaces)==1 and cofaces[0] not in target:
    high=cofaces[0]
    # The only proper coface of low is high; hence low is a legal free face.
    assert high.bit_count()==low.bit_count()+1
    remaining.remove(low);remaining.remove(high)
    pairs.append((low,high));found=True;break
  assert found,'relative collapse stalled'
 assert len(pairs)==152
 return pairs

matching=chvatal_ind2_morse();pairs=collapse_3_to_2()
chi={r:sum((-1)**d*f for d,f in enumerate(EXPECTED[r])) for r in EXPECTED}
assert chi=={1:2,2:0,3:0,4:-63},chi
print('CHVATAL_IND2_IND3_SHARP_SIMPLE_HOMOTOPY_PLATEAU_VERIFIED')
print('Graph vertices',N,'edges',len(EDGES),'triangle-free and 4-regular')
print('Faces by stages', {r:len(s) for r,s in STAGES.items()})
print('Matching dim0/dim3, pairs/incidences',matching)
print('Elementary collapses of Ind3 onto Ind2',len(pairs))
print('Mod2 Betti dimensions 2/3',homology_mod2(STAGES[2]),homology_mod2(STAGES[3]))
print('Euler characteristics at thresholds 1..4',chi)
