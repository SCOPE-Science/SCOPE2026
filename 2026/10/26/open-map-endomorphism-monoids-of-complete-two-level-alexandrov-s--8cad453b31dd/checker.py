from itertools import product
from math import factorial

def check(p,q):
 n=p+q
 pre={(i,j) for i in range(n) for j in range(n) if i==j or (i<p and j>=p)}
 count=0
 for f in product(range(n),repeat=n):
  if all((f[i],f[j]) in pre for i,j in pre) and all({f[j] for j in range(n) if (i,j) in pre}=={j for j in range(n) if (f[i],j) in pre} for i in range(n)):
   count+=1
 expected=((p+1)**p if q==1 else p**p*factorial(q)+q)
 assert count==expected,(p,q,count,expected)
 return p,q,count
for p in range(1,4):
 for q in range(1,4):print(check(p,q))
print('CHECK_OK')
