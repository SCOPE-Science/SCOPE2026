"""Independent rowmotion enumeration from the cyclic Singer difference set."""
from collections import Counter
from math import lcm
D={0,1,3,9}; n=13; M=(1<<n)-1
blocks=[sum(1<<((d+j)%n) for d in D) for j in range(n)]
assert len(set(blocks))==13
assert all(sum(bool((b>>a)&1 and (b>>c)&1) for b in blocks)==1 for a in range(13) for c in range(a+1,13))
# prerequisites: zero for a point, its four points for a line.
prereq=[0]*n+blocks
states=[]
for p in range(1<<n):
 available=[j for j,b in enumerate(blocks) if b&p==b]
 for t in range(1<<len(available)):
  lines=sum(1<<available[j] for j in range(len(available)) if t>>j&1)
  states.append(p|lines<<n)
assert len(states)==38730
S=set(states)
def row(i):
 outsiders=0
 for v in range(26):
  if not (i>>v)&1 and (prereq[v]&i)==prereq[v]:outsiders|=1<<v
 out=outsiders
 for v in range(n,26):
  if outsiders>>v&1:out|=prereq[v]
 return out
perm={x:row(x) for x in states}
assert set(perm.values())==S
unused=S.copy();spec=Counter()
while unused:
 a=next(iter(unused));z=a;k=0
 while 1:
  assert z in unused,(a,z)
  unused.remove(z);k+=1;z=perm[z]
  if z==a:break
 spec[k]+=1
want={2:468,3:1249,5:702,6:624,7:1521,9:936,11:702}
assert dict(spec)==want,spec
ord=1
for k in spec:ord=lcm(ord,k)
assert ord==6930
print('SINGER_INDEPENDENT_38730_IDEALS_6202_ORBITS_ORDER_6930_PASS',sorted(spec.items()))
