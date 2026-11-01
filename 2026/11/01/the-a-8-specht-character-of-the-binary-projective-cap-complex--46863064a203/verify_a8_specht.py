from itertools import permutations
from collections import defaultdict
from functools import lru_cache
from math import factorial
parts=[]
def partitions(n,max_part=None):
 if not n:yield ()
 else:
  for k in range(min(n,max_part or n),0,-1):
   for a in partitions(n-k,k):yield (k,)+a
@lru_cache(None)
def stable_assignments(cycles,sizes):
 if any(z<0 for z in sizes) or sum(cycles)!=sum(sizes):return 0
 if not cycles:return int(all(z==0 for z in sizes))
 c=cycles[0];n=0
 for j in range(len(sizes)):
  if sizes[j]>=c:
   t=list(sizes);t[j]-=c
   n+=stable_assignments(cycles[1:],tuple(t))
 return n

def sign_perm(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
@lru_cache(None)
def char(lam,cyc):
 l=len(lam);r=0
 for p in permutations(range(l)):
  shapes=tuple(lam[i]-i+p[i] for i in range(l))
  if any(s<0 for s in shapes):continue
  r+=sign_perm(p)*stable_assignments(cyc,shapes)
 return r
cs=[(1,)*8,(2,)*4,(2,2,1,1,1,1),(4,4),(3,3,1,1),(4,2,1,1),(6,2),(7,1),(7,1),(3,1,1,1,1,1),(3,2,2,1),(5,3),(5,3),(5,1,1,1)]
sz=[1,105,210,1260,1120,2520,3360,2880,2880,112,1680,1344,1344,1344]
our=[77,-3,5,-3,2,1,0,0,0,-1,-1,-1,-1,2]
# Only even cycle types appear in A8.  A8 classes of distinct odd
# cycle lengths split in two; both have the same restricted Specht trace.
from collections import Counter
from math import lcm

def cycle_type(p):
    seen=set(); lengths=[]
    for i in range(8):
        if i in seen: continue
        j=i;k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        lengths.append(k)
    return tuple(sorted(lengths,reverse=True))

types=Counter(cycle_type(p) for p in permutations(range(8)) if sign_perm(p)==1)
assert sum(types.values())==20160
orders=[1,2,2,4,3,4,6,7,7,3,6,15,15,5]
for typ, size, ord_ in zip(cs,sz,orders):
    assert lcm(*typ)==ord_
    # For split types only half of all even elements belong to each class.
    split=(typ in {(7,1),(5,3)})
    assert types[typ]==size*(2 if split else 1), (typ,size,types[typ])

rows={part:[char(part,cyc) for cyc in cs] for part in partitions(8)}
parts=((7,1),(4,3,1))
assert all(rows[parts[0]][j]+rows[parts[1]][j]==our[j] for j in range(len(cs)))
for part in parts:
    row=rows[part]
    numerator=sum(z*x*y for z,x,y in zip(sz,row,our))
    assert numerator==20160
    assert sum(z*x*x for z,x in zip(sz,row))==20160
    print('partition',part,'dimension',row[0],'inner_product_with_target',numerator//20160,'character',row)
assert sum(z*x for z,x in zip(sz,our))==0
assert sum(z*x*x for z,x in zip(sz,our))==2*20160
print('14 conjugacy class comparison, Specht decomposition, and invariant checks pass')
print('ALL_CHECKS_PASS')
