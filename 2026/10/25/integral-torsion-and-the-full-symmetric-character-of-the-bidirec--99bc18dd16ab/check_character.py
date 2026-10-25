from check_integral import make_complex
from itertools import permutations
from collections import defaultdict
arcs,faces=make_complex(); ai={a:i for i,a in enumerate(arcs)}
def cycle_type(p):
 vis=set(); cyc=[]
 for a in range(5):
  if a not in vis:
   x=a; length=0
   while x not in vis:
    vis.add(x); length+=1; x=p[x]
   cyc.append(length)
 return tuple(sorted(cyc,reverse=True))
def sign(seq):
 return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1
def calc(p,h):
 amap=[]
 for a,b in arcs:
  f=lambda x: ((1-x) if h else x) if x<2 else 2+p[x-2]
  amap.append(ai[f(a),f(b)])
 tr=[]
 for degree,F in enumerate(faces):
  count=0
  for m in F:
   ix=[i for i in range(20) if (m>>i)&1]; mapped=[amap[i] for i in ix]
   if m==sum(1<<j for j in mapped): count+=sign(mapped)
  tr.append(count)
 return (1-sum(((-1)**k)*val for k,val in enumerate(tr)),tuple(tr))
seen={}
for p in permutations(range(5)):
 ct=cycle_type(p)
 if ct in seen:continue
 seen[ct]=p
for ct,p in sorted(seen.items(),reverse=True):
 print(ct,*(calc(p,h) for h in [0,1]))
from functools import lru_cache
from math import factorial,prod
parts=list(sorted(seen,reverse=True))
def boxes(lam):return {(i,j) for i,n in enumerate(lam) for j in range(n)}
@lru_cache(None)
def subparts(lam,k):
 if not lam:
  return [()] if k==0 else []
 out=[]
 for a in range(min(lam[0],k)+1):
  for b in subparts(lam[1:],k-a):
   if not b or a>=b[0]:out.append(((a,)+b) if a else b)
 return [tuple(x for x in t if x) for t in set(out)]
@lru_cache(None)
def irreducible(lam,ctype):
 if not ctype:return int(not lam)
 if not lam:return 0
 v=0
 for mu in subparts(lam,sum(lam)-ctype[0]):
  skew=boxes(lam)-boxes(mu)
  if len(skew)!=ctype[0]:continue
  if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}<=skew for i,j in skew):continue
  visit={next(iter(skew))};stack=list(visit)
  while stack:
   i,j=stack.pop()
   for p in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
    if p in skew and p not in visit:visit.add(p);stack.append(p)
  if len(visit)==len(skew):
   h=len({i for i,j in skew})-1
   v+=(-1)**h*irreducible(mu,ctype[1:])
 return v
print('IRREPS')
for lam in parts:
 vals=[irreducible(lam,ct) for ct in parts]
 def coeff(h):
  numer=0
  for ct in parts:
   z=prod(i**ct.count(i)*factorial(ct.count(i)) for i in set(ct))
   numer+=(calc(seen[ct],h)[0]*irreducible(lam,ct)*(factorial(5)//z))
  return numer//factorial(5) if numer%factorial(5)==0 else ('invalid',numer)
 a,b=coeff(0),coeff(1)
 print(lam,vals,'mult+', (a+b)//2 if isinstance(a,int) else a,'mult-',(a-b)//2 if isinstance(a,int) else b, 'raw',a,b)

# Reconstruct all 14 characters by irreducible decomposition; integer multiplicities.
mult={
 (5,):(0,0),(4,1):(0,0),(3,2):(0,1),(3,1,1):(1,1),
 (2,2,1):(1,0),(2,1,1,1):(1,1),(1,1,1,1,1):(1,0)}
for ct,p in seen.items():
 for h in (0,1):
  expected=sum((a+b if h==0 else a-b)*irreducible(lam,ct) for lam,(a,b) in mult.items())
  actual=calc(p,h)[0]
  assert expected==actual,(ct,h,expected,actual)
assert sum((a+b)*irreducible(lam,(1,1,1,1,1)) for lam,(a,b) in mult.items())==31
print("VERIFIED complete S5 x C2 character and Specht decomposition")
