from itertools import product
from verify_diamond import factor
# F4=F2[t]/(t^2+t+1)
def mul(a,b):
 c=0
 for i in range(2):
  if (b>>i)&1:c ^=a<<i
 if c&8:c ^=0b1100
 if c&4:c ^=0b111
 return c
for q,m in [(4,1)]:
 V=list(product(range(4),repeat=m));rows=list(product(V,repeat=3));cnt=0
 for A in rows:
  for B in rows:
   dot=lambda i,j:__import__('functools').reduce(lambda x,y:x^y,(mul(A[i][k],B[j][k]) for k in range(m)),0)
   if all(dot(i,i)==0 for i in range(3)) and all(dot(i,j)==dot(j,i) for i in range(3) for j in range(i+1,3)):cnt+=1
 p=factor(m,q,0)+(q**3-1)*factor(m,q,2)
 print('GF4 m1',cnt,p,'PASS',cnt==p)
 assert cnt==p
