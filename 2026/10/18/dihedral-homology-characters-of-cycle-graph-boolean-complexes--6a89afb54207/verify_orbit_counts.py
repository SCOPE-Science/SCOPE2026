import itertools,math
from functools import lru_cache

def lucas(n):
 a,b=2,1
 for _ in range(n):a,b=b,a+b
 return a

def fib(n):
 if n==-1:return 1
 a,b=0,1
 for _ in range(n):a,b=b,a+b
 return a

def F(k):return (-1)**k*fib(k-1)

def num_fix_orient(n,p,S):
 E=[(i,(i+1)%n) for i in range(n) if i in S and (i+1)%n in S]
 cnt=0
 for mask in range(1<<len(E)):
  arcs={((b,a) if (mask>>j)&1 else (a,b)) for j,(a,b) in enumerate(E)}
  if any((p[a],p[b]) not in arcs for (a,b) in arcs):continue
  if len(S)==n and (all(((i,(i+1)%n) in arcs) for i in range(n)) or all((((i+1)%n,i) in arcs) for i in range(n))): continue
  cnt+=1
 return cnt

def sign_restrict(p,S):
 seen=set();sign=1
 for a in S:
  if a not in seen:
   cur=a;k=0
   while cur not in seen:seen.add(cur);k+=1;cur=p[cur]
   sign*=(-1)**(k-1)
 return sign

def char_brut(n,p):
 accum=-1
 for mask in range(1,1<<n):
  S={i for i in range(n) if mask>>i&1}
  if {p[i] for i in S}!=S:continue
  k=len(S)
  a=num_fix_orient(n,p,S)
  accum+=(-1)**(k-1)*sign_restrict(p,S)*a
 return (-1)**(n-1)*accum

def char_formula(n,j,ref=False):
 if not ref:
  d=math.gcd(n,j)
  return (-1)**(n+d)*(lucas(d)-2)
 if n%2:
  k=n//2;return -F(k)
 k=n//2
 return F(k+1) if j%2==0 else F(k-2)  # p(i)=j-i, for even n j even vertex-axis

for n in range(3,12):
 tests=[]
 for j in range(n):
  p=[(i+j)%n for i in range(n)]
  got=char_brut(n,p);wanted=char_formula(n,j)
  assert got==wanted,(n,j,'rotation',got,wanted)
 for j in range(n):
  p=[(j-i)%n for i in range(n)]
  got=char_brut(n,p);wanted=char_formula(n,j,True)
  assert got==wanted,(n,j,'reflection',got,wanted)
 print('n=',n,'dim=',lucas(n)-2,'rot',[char_formula(n,j) for j in range(n)], 'ref',[char_formula(n,j,True) for j in range(n)])
print('PASS')
