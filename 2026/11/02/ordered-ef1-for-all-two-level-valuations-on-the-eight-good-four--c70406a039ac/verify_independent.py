"""Independent finite spot tests for ordered EF1 with 4 heterogeneous binary agents."""
import itertools,random
GROUPS=(0,0,0,1,1,1,2,2)
def matchings(items):
 if not items:
  yield ()
  return
 u=items[0]
 for k in range(1,len(items)):
  v=items[k]
  if GROUPS[u]==GROUPS[v]:continue
  r=items[1:k]+items[k+1:]
  for p in matchings(r):yield ((u,v),)+p
PAIRINGS=list(matchings(tuple(range(8))))
ALLOCATIONS=[assignment for pairs in PAIRINGS for assignment in itertools.permutations(pairs)]
assert len(PAIRINGS)==36 and len(ALLOCATIONS)==864

def valid(allocation,preferences):
 for i in range(4):
  own=sum((preferences[i]>>g)&1 for g in allocation[i])
  for j in range(4):
   if j==i:continue
   other=sum((preferences[i]>>g)&1 for g in allocation[j])
   if i<j and own<other:return False
   if own<min(sum((preferences[i]>>g)&1 for g in allocation[j] if g!=removed) for removed in allocation[j]):return False
 return True

def witness(prefs):
 return next((A for A in ALLOCATIONS if valid(A,prefs)),None)

random.seed(810372)
for k in range(3200):
 p=tuple(random.randrange(256) for _ in range(4))
 assert witness(p) is not None,(k,p)
# Strengthen with 4x4 profiles whose favored masks vary over each conflict category.
subset=(0,1,2,3,7,15,31,63,127,128,192,224,240,248,252,255)
for prefs in itertools.product(subset,repeat=4):
 assert witness(prefs) is not None,prefs
print('PASS: independent direct verification, 36 matchings, 864 assignments, 3,200 random and 65,536 structured binary valuation profiles.')
