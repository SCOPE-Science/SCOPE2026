"""Independent full simplicial chain-boundary rank computation in characteristic two."""
from mk_forest_verify import N, forest_independent
from collections import Counter,defaultdict
by_size=defaultdict(list)
for mask in range(1<<N):
 if forest_independent(mask):by_size[mask.bit_count()].append(mask)
assert sum(map(len,by_size.values()))==50997

def rank_boundary(size):
 lower={m:i for i,m in enumerate(by_size[size-1])}
 pivots={}
 for m in by_size[size]:
  col=0; s=m
  while s:
   b=s&-s;s-=b
   col^=1<<lower[m^b]
  while col:
   high=col.bit_length()-1
   if high not in pivots:
    pivots[high]=col;break
   col^=pivots[high]
 return len(pivots)
for size in range(11,0,-1):
 r=rank_boundary(size)
 print('boundary dim',size-1,'to',size-2,'rank mod2',r)
print('done')
