from itertools import combinations,permutations,product
from math import factorial
from fractions import Fraction

def invol(n):
 out=[]
 for r in range(n+1):
  for dom in combinations(range(n),r):
   for im in permutations(dom):
    for signs in product((-1,1), repeat=r):
     vals=[0]*n
     for i,j,s in zip(dom,im,signs):vals[i]=s*(j+1)
     if sq(tuple(vals))==tuple((i+1 if i in dom else 0) for i in range(n)):
      out.append(tuple(vals))
 return out

def compose(a,b):
 # a after b
 n=len(a);z=[]
 for x in b:
  if x==0:z.append(0);continue
  y=a[abs(x)-1]
  if y==0:z.append(0)
  else:z.append((1 if x>0 else -1)*y)
 return tuple(z)
def sq(x):return compose(x,x)
def anticomm(a,b):
 ab=compose(a,b);ba=compose(b,a)
 return all(x==-y for x,y in zip(ab,ba))

for n in range(6):
 inv=invol(n)
 count=sum(1 for a in inv for b in inv if anticomm(a,b))
 # exp(5z +6z²+2z⁴)
 countf=0
 for p in range(n+1):
  for q in range(n//2+1):
   for r in range(n//4+1):
    if p+2*q+4*r==n:countf+=Fraction(5**p*6**q*2**r, factorial(p)*factorial(q)*factorial(r))
 pred=int(countf*factorial(n))
 print('CENSUS_OK',n,len(inv),count,pred)
 assert count==pred

print("VERIFY_OK")
