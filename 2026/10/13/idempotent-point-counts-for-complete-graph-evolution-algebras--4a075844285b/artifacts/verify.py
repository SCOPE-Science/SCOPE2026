from itertools import product
from math import comb

def formula(n,q,p,chi):
 c0=1 if (n-1)%p==0 else 2
 roots=[]
 for k in range(1,n):
  if (n-1)%p==0:
   r=0 if (2*k-1)%p==0 else 1
  else:
   delta=(1-4*k*(n-k))%p
   r=1+chi(delta) - int((n+1)%p==0)
  assert r>=0
  roots.append(comb(n,k)*r)
 assert sum(roots)%2==0,(n,q,roots)
 return c0+sum(roots)//2

def prime(q):
 p=q
 squares={a*a%p for a in range(p)}
 chi=lambda a: 0 if a%p==0 else (1 if a%p in squares else -1)
 return chi

for q,ns in [(3,range(3,10)),(5,range(3,7)),(7,range(3,6)),(11,range(3,6))]:
 chi=prime(q)
 sq=[(a*a)%q for a in range(q)]
 for n in ns:
  brute=0
  for x in product(range(q),repeat=n):
   S=sum(sq[z] for z in x)%q
   if all(z==(S-sq[z])%q for z in x): brute+=1
  pred=formula(n,q,q,chi)
  print(q,n,brute,pred)
  assert pred==brute

# F_9 = F_3[t]/(t^2+1); elements a+3*b for 0<=a,b<3.
def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a): return ((-a%3)%3)+3*((-(a//3))%3)
def sq9(x):
 a=x%3; b=x//3
 return (a*a-b*b)%3+3*((2*a*b)%3)
chi9=lambda a:0 if a%3==0 else 1
sqs=[sq9(a) for a in range(9)]
for n in (3,4,5):
 brute=0
 for coords in product(range(9),repeat=n):
  S=0
  for a in coords:S=add(S,sqs[a])
  if all(v==add(S,neg(sqs[v])) for v in coords):brute+=1
 pred=formula(n,9,3,chi9)
 print(9,n,brute,pred)
 assert brute==pred
print('VERIFY_OK')
