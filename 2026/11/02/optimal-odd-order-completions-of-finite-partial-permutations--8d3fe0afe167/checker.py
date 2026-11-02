from itertools import permutations,combinations
from math import factorial
from functools import lru_cache

def odd_perms(n):
 for sig in permutations(range(n)):
  seen=set();good=True
  for i in range(n):
   if i not in seen:
    j=i;length=0
    while j not in seen:
     seen.add(j);length+=1;j=sig[j]
    if length%2==0:good=False;break
  if good:yield sig

def profile(n,p):
 incoming=set(p.values()); visited=set();a=b=0;bad=False
 for i in range(n):
  if i in incoming:continue
  j=i;length=0
  while j is not None:
   assert j not in visited
   visited.add(j);length+=1;j=p.get(j)
  if length%2:a+=1
  else:b+=1
 for i in range(n):
  if i in visited:continue
  j=i;length=0
  while j not in visited:
   visited.add(j);length+=1;j=p[j]
  assert j==i
  if length%2==0:bad=True
 return a,b,bad

@lru_cache(None)
def cnt(a,b):
 # cycle of fixed distinguished component must have odd # odd comps
 if a+b==0:return 1
 total=0
 from math import comb
 if a:
  # pick a-1 additional odd and s even, total cycle odd -> # additional odd even
  for r in range(0,a,2):
   for s in range(b+1):
    z=r+s+1
    total+=comb(a-1,r)*comb(b,s)*factorial(z-1)*cnt(a-r-1,b-s)
 else:
  # 0 odd implies no possible even-only cycles
  return 0
 return total

for n in range(0,6):
 perms=list(odd_perms(n)); counts={};partials=0
 for k in range(n+1):
  for dom in combinations(range(n),k):
   for image in permutations(range(n),k):
    p=dict(zip(dom,image)); a,b,bad=profile(n,p)
    found=sum(all(g[i]==j for i,j in p.items()) for g in perms)
    expected=0 if bad else cnt(a,b)
    if found!=expected:
     raise AssertionError((n,p,(a,b,bad),found,expected))
    partials+=1
 print('ground_size',n,'partial_maps',partials,'all_completions_match',flush=True)
# Minimal addition: only one possible when all path components even and positive, t! permutations
for n in range(0,5):
 odd=list(odd_perms(n+1));ns=0
 for k in range(n+1):
  for dom in combinations(range(n),k):
   for image in permutations(range(n),k):
    p=dict(zip(dom,image));a,b,bad=profile(n,p)
    if bad or a or not b:continue
    found=sum(all(g[i]==j for i,j in p.items()) for g in odd)
    expected=factorial(b)
    if found!=expected:raise AssertionError((n,p,found,expected))
    ns+=1
 print('ground_size',n,'one_point_minimum_cases',ns,'all_multiplicities_match',flush=True)

# Independently verify the closed form and distinguished-cycle enumeration.
def double_fact(n):
    z=1
    while n>0:
        z*=n
        n-=2
    return z

def odd_cycle_closed(a):
    if a%2:
        return double_fact(a)*double_fact(a-2)
    return double_fact(a-1)**2

for a in range(1,12):
    for b in range(0,10):
        expected=odd_cycle_closed(a)*factorial(a+b-1)//factorial(a-1)
        assert cnt(a,b)==expected,(a,b,cnt(a,b),expected)
assert cnt(0,0)==1
assert all(cnt(0,b)==0 for b in range(1,12))
print('ALL_CHECKS_OK')
