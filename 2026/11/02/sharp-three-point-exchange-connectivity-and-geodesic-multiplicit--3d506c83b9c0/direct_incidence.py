from itertools import product,combinations
from collections import Counter,deque

def mul(a,b):
 x=0
 for i in range(2):
  if (b>>i)&1:x^=a<<i
 if x&8:x^=0b1010
 if x&4:x^=0b111
 return x

def inv(a):
 for b in range(1,4):
  if mul(a,b)==1:return b
 raise Exception('bad')

def normalize(v):
 q=next(x for x in v if x)
 return tuple(mul(x,inv(q)) for x in v)
points=sorted({normalize(v) for v in product(range(4),repeat=3) if any(v)})
lines=sorted({normalize(v) for v in product(range(4),repeat=3) if any(v)})
assert len(points)==len(lines)==21
L=[]
for u in lines:
 mask=0
 for k,v in enumerate(points):
  c=0
  for a,b in zip(u,v):c^=mul(a,b)
  if c==0:mask|=1<<k
 assert mask.bit_count()==5
 L.append(mask)
H=[]
for C in combinations(range(21),6):
 mask=sum(1<<i for i in C)
 if all((l&mask).bit_count()<=2 for l in L):H.append(mask)
print('hyperovals',len(H));assert len(H)==168
four_arc_frequencies=Counter()
for h in H:
 for arc in combinations([j for j in range(21) if h&(1<<j)],4):
  four_arc_frequencies[arc]+=1
four_arcs=[arc for arc in combinations(range(21),4)
           if all((l & sum(1<<i for i in arc)).bit_count()<=2 for l in L)]
assert len(four_arcs)==2520
assert set(four_arc_frequencies)==set(four_arcs)
assert set(four_arc_frequencies.values())=={1}
print('four-arcs',len(four_arcs),'unique hyperoval completion proved exhaustively')
ic=Counter((a&b).bit_count() for a,b in combinations(H,2))
print('intersection',dict(sorted(ic.items())))
for sh in (5,4,3,2,1,0):
 adj=[[] for _ in H]
 for i in range(len(H)):
  for j in range(i+1,len(H)):
   if (H[i]&H[j]).bit_count()>=sh:adj[i].append(j);adj[j].append(i)
 seen=set();components=[]
 for i in range(len(H)):
  if i in seen:continue
  d={i};stack=[i]
  for u in stack:
   for v in adj[u]:
    if v not in d:d.add(v);stack.append(v)
  components.append(len(d));seen|=d
 degrees=Counter(map(len,adj))
 print('threshold shared >=',sh,'components',Counter(components),'degrees',degrees,'edges',sum(map(len,adj))//2)
 if len(components)==1:
  hist=Counter();ecc=[]
  for i in range(len(H)):
   dst=[-1]*len(H);dst[i]=0;qq=deque([i])
   while qq:
    u=qq.popleft()
    for v in adj[u]:
     if dst[v]<0:dst[v]=dst[u]+1;qq.append(v)
   hist.update(x for x in dst if x>0)
   ecc.append(max(dst))
  print('distances ordered',sorted(hist.items()),'ecc',Counter(ecc));break

AD=[set() for _ in H]
for i in range(len(H)):
 for j in range(i+1,len(H)):
  if (H[i]&H[j]).bit_count()==3:
   AD[i].add(j);AD[j].add(i)
assert set(map(len,AD))=={40}
assert sum(map(len,AD))//2==3360
profile={r:set() for r in range(4)}
for i in range(len(H)):
 for j in range(i+1,len(H)):
  r=(H[i]&H[j]).bit_count()
  assert 0<=r<=3
  profile[r].add(len(AD[i]&AD[j]))
assert profile=={0:{4},1:{5},2:{16},3:{11}}
print('DIRECT_FINITE_INCIDENCE_AND_EXCHANGE_PASS')
