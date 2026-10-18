from itertools import product, combinations
from math import comb
# F4 polynomial alpha^2+alpha+1; multiplication in 2-bit binary

def mul(a,b):
 t=0
 for i in range(2):
  if b>>i&1:t^=a<<i
 for i in range(3,1,-1):
  if t>>i&1:t^=0b111<<(i-2)
 return t

def cl(x):
 nz=next(v for v in x if v)
 inv=next(i for i in (1,2,3) if mul(i,nz)==1)
 return tuple(mul(v,inv) for v in x)

def derivative(xs,i):
 z=[xs[k] for k in range(len(xs)) if k!=i]
 return __import__('functools').reduce(lambda a,b:a^b,(mul(z[u],z[v]) for u in range(len(z)) for v in range(u+1,len(z))),0)

def expected(xs):
 n=len(xs)
 distinct=set(xs)
 if n%4==2:
  if len(distinct)==1:return True
  if len(distinct)!=2:return False
  aa,bb=sorted(distinct)
  r=sum(x==aa for x in xs)
  s=n-r
  return r%4==1 and s%4==1
 return any(all(x==(v if i in I else 0) for i,x in enumerate(xs)) for v in [1,2,3] for r in range(1,n+1,4) for I in combinations(range(n),r))
for n in range(4,8):
 seen={cl(xs) for xs in product(range(4),repeat=n) if any(xs)}
 sings={xs for xs in seen if all(derivative(xs,i)==0 for i in range(n))}
 exp={xs for xs in seen if expected(xs)}
 assert sings==exp, (n,len(sings),len(exp),list(sings^exp)[:4])
 print(n,'F4sing',len(sings),'expected',len(exp),'formula binary',sum(comb(n,r) for r in range(1,n+1,4)) if n%4!=2 else 'line count '+str(sum(comb(n,r) for r in range(1,n,4))//2))

print("VERIFY_OK")
