"""Independent upper-bound replay using subsets of all 5040 permutation concepts."""
import itertools, functools, math
n=7
perms=list(itertools.permutations(range(n)))
assert len(perms)==math.factorial(n)==5040
masks=[]
for a in range(n):
 for b in range(a+1,n):
  masks.append(sum(1<<i for i,p in enumerate(perms) if p.index(a)<p.index(b)))
full=(1<<len(perms))-1
@functools.lru_cache(None)
def can(s,d):
 if d==0:return True
 if s.bit_count()<(1<<d):return False
 for q in masks:
  one=s&q;zero=s&~q
  if min(one.bit_count(),zero.bit_count()) >= (1<<(d-1)):
   if can(one,d-1) and can(zero,d-1):return True
 return False
assert can(full,11)
assert not can(full,12)
print('BITSET_N7_LITTLESTONE_EXACT_11_PASS states='+str(can.cache_info().currsize))
