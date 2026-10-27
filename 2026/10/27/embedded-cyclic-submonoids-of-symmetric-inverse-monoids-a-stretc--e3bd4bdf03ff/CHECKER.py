from itertools import combinations,permutations
from math import comb,factorial,gcd
from fractions import Fraction

def phi(n):
 return sum(gcd(i,n)==1 for i in range(1,n+1))
def allmaps(n):
 for k in range(n+1):
  for dom in combinations(range(n),k):
   for img in permutations(range(n),k):
    f=[-1]*n
    for i,j in zip(dom,img): f[i]=j
    yield tuple(f)
def mul(f,g):
 return tuple(-1 if x==-1 else g[x] for x in f)
def ord_perm(p):
 seen=set();v=1
 for i in range(len(p)):
  if i in seen:continue
  k=0;j=i
  while j not in seen:
   seen.add(j);k+=1;j=p[j]
  v=v*k//gcd(v,k)
 return v
def direct(n):
 identity=tuple(range(n))
 groups={}
 for f in allmaps(n):
  p=identity; s=[];seen=set()
  while p not in seen:
   s.append(p);seen.add(p);p=mul(p,f)
  key=frozenset(s)
  groups.setdefault(key,[]).append(f)
 return groups
for n in range(1,7):
 total=sum(comb(n,k)**2*factorial(k) for k in range(n+1))
 H=sum(comb(n,m)*factorial(m) for m in range(n+1))
 W_num=Fraction(0)
 for m in range(n+1):
  if m==0: W_num+=comb(n,m);continue
  W_num += comb(n,m)*sum(Fraction(1,phi(ord_perm(p))) for p in permutations(range(m)))
 formula=total-H+W_num
 assert formula.denominator==1
 formula=int(formula)
 d=direct(n) if n<=5 else None
 if d is not None:
  sizes={};bad=0
  for key,gens in d.items():
   t=len(gens)
   sizes[t]=sizes.get(t,0)+1
  assert len(d)==formula,(n,len(d),formula)
  print(n,'total',total,'embedded',len(d),'collisions',total-len(d),'generator-fiber census',sizes)
 else:print(n,'total',total,'formula',formula,'collisions',total-formula)
print('ALL_PARTIAL_CYCLIC_FINITE_CHECKS_PASSED')
