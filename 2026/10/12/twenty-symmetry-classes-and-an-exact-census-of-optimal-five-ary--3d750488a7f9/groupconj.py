# Enumerates all collineations as permutations of 52 plane incidences;
# conjugacy classes are generated using the transvections and their inverses.
from collections import deque
p=[tuple(map(int,s.split()))for s in open('gmap.txt')]
I=tuple(range(52))
def prod(a,b):return tuple(a[b[i]]for i in range(52))
def inv(a):
 b=[0]*52
 for i,j in enumerate(a):b[j]=i
 return tuple(b)
group={I:0}; elems=[I]
for x in elems:
 for g in p:
  y=prod(x,g)
  if y not in group:group[y]=len(elems);elems.append(y)
assert len(elems)==5616
pinv=[inv(g) for g in p]
left=[prod(a,b) for a,b in zip(p,pinv)]
assert all(a==I for a in left)
remaining=set(range(len(elems)));cls=[]
while remaining:
 root=min(remaining); orbit={root};queue=[root]
 for i in queue:
  x=elems[i]
  for h,hi in zip(p,pinv):
   y=prod(prod(h,x),hi)
   j=group[y]
   if j not in orbit:orbit.add(j);queue.append(j)
 cls.append((root,len(orbit)))
 remaining-=orbit
print('group_order',len(elems),'conjugacy_classes',len(cls),'sizes', [m for _,m in cls]);assert sum(m for _,m in cls)==5616
with open('conjugacy_reps.txt','w')as f:
 for idx,sz in cls:f.write(str(sz)+' '+' '.join(map(str,elems[idx]))+'\n')
