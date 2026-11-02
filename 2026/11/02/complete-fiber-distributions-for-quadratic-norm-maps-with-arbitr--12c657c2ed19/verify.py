from collections import Counter
from itertools import product
for p in (2,3,5,7):
 if p==2: a,b=1,1
 else:
  b=next(k for k in range(2,p) if pow(k,(p-1)//2,p)==p-1)
  a=0
 field=list(product(range(p),repeat=2))
 def mul(x,y):
  c,d=x; e,f=y
  return ((c*e+b*d*f)%p,(c*f+d*e+a*d*f)%p)
 def powf(z,n):
  ans=(1,0)
  while n:
   if n%2: ans=mul(ans,z)
   z=mul(z,z); n//=2
  return ans
 norm={z:powf(z,p+1) for z in field}
 assert all(v[1]==0 for v in norm.values())
 for mat in product(range(p),repeat=4):
  m00,m01,m10,m11=mat
  counts=Counter()
  for x,y in field:
   n=norm[(x,y)][0]
   out=((n+m00*x+m01*y)%p,(m10*x+m11*y)%p)
   counts[out]+=1
  h=Counter(counts.values()); h[0]=p*p-len(counts)
  if m10==m11==0:
   assert h[1]==1 and h[p+1]==p-1 and h[0]==p*p-p,(p,mat,h)
  else:
   assert h[1]==p and h[2]==p*(p-1)//2 and h[0]==p*(p-1)//2,(p,mat,h)
 print('CHECK_OK',p,'matrices',p**4)

print('VERIFY_OK matrices=3123 base_field_orders=2,3,5,7')
