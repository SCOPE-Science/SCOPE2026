from itertools import permutations,product,combinations
from collections import Counter,defaultdict
n=4;VERT=1<<n
sq=[]
for vary in combinations(range(n),2):
 fix=[i for i in range(n) if i not in vary]
 for bits in range(4):
  mask=0
  for v in range(VERT):
   if all((v>>fix[j])&1==(bits>>j)&1 for j in range(2)):
    mask|=1<<v
  sq.append(mask)
assert len(set(sq))==24

def trace(perm,flip):
 action=[sum((((v>>perm[i])&1)^((flip>>i)&1))<<i for i in range(n)) for v in range(VERT)]
 seen=set();orbits=[]
 for v in range(VERT):
  if v in seen:continue
  mask=0;k=v
  while k not in seen:
   seen.add(k);mask|=1<<k;k=action[k]
  orbits.append(mask)
 K=len(orbits)
 tr=0
 for sel in range(1,1<<K):
  selected=0
  for i,m in enumerate(orbits):
   if sel>>i&1:selected|=m
  if any((selected&s)==0 for s in sq):
   tr+=1 if (sel.bit_count()%2==1) else -1
 return tr-1

def cycletype(perm,flip):
 seen=set();out=[]
 for i in range(n):
  if i in seen:continue
  cyc=[];x=i
  while x not in seen:seen.add(x);cyc.append(x);x=perm[x]
  parity=sum((flip>>j)&1 for j in cyc)%2
  out.append((len(cyc),parity))
 return tuple(sorted(out))

groups=defaultdict(list)
for perm in permutations(range(n)):
 for flip in range(1<<n):
  groups[cycletype(perm,flip)].append(trace(perm,flip))
assert sum(map(len,groups.values()))==384
print('20 conjugacy groups:',len(groups))
for k in sorted(groups):
 assert len(set(groups[k]))==1,(k,groups[k]);print(k,len(groups[k]),groups[k][0])
print('invariants',sum(len(v)*v[0] for v in groups.values())//384)
# Independently encoded target table: (signed permutation cycle length, parity of coordinate flips).
expected = {
 ((1,0),(1,0),(1,0),(1,0)):15,
 ((1,0),(1,0),(1,0),(1,1)):3,
 ((1,0),(1,0),(1,1),(1,1)):-1,
 ((1,0),(1,0),(2,0)):1,
 ((1,0),(1,0),(2,1)):1,
 ((1,0),(1,1),(1,1),(1,1)):3,
 ((1,0),(1,1),(2,0)):1,
 ((1,0),(1,1),(2,1)):1,
 ((1,0),(3,0)):0,
 ((1,0),(3,1)):0,
 ((1,1),(1,1),(1,1),(1,1)):15,
 ((1,1),(1,1),(2,0)):1,
 ((1,1),(1,1),(2,1)):1,
 ((1,1),(3,0)):0,
 ((1,1),(3,1)):0,
 ((2,0),(2,0)):-5,
 ((2,0),(2,1)):-1,
 ((2,1),(2,1)):3,
 ((4,0),):-1,
 ((4,1),):-1,
}
assert len(expected)==20
assert set(groups)==set(expected)
assert all(v[0] == expected[k] for k,v in groups.items())
assert sum(len(v)*v[0] for v in groups.values())==0
assert groups[((1,1),(1,1),(1,1),(1,1))][0]==15
print('ALL_384_GROUP_ACTIONS_AND_20_CHARACTERS_VERIFIED')
print('VERIFY_OK')
