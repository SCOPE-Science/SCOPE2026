"""Exact finite-field check of geometric twist point counts, for small primes."""
from math import isqrt

def primes_to(n):
 return [p for p in range(5,n+1) if all(p%d for d in range(2,isqrt(p)+1))]
def chi(a,p):
 a%=p
 return (0 if a==0 else 1 if pow(a,(p-1)//2,p)==1 else -1)
def nroots_quad(a,c,p):return sum((x*x+a*x+c)%p==0 for x in range(1,p))
for p in primes_to(37):
 d=next(x for x in range(2,p) if chi(x,p)<0)
 for c in range(1,p):
  A=list(range((p+1)//2)) # representatives a=0..(p-1)/2
  counts={i:sum(chi(a*a-4*c,p)==i for a in A) for i in (-1,0,1)}
  u=chi(c,p);v=chi(-c,p)
  assert counts[1]==(p-1-u+v)//4 and counts[0]==(1+u)//2 and counts[-1]==(p+1-u-v)//4,(p,c,counts)
  assert counts[1]>=1
  for a in A:
   s=chi(a*a-4*c,p)
   points=sum(1 for x in range(1,p) for y in range(p) if (-x-c*pow(x,-1,p)-a)%p==0)+2
   assert points==2+p*(1+s)==2+p*nroots_quad(a,c,p)
   # Hyperelliptic model quadratic twist d*W^2=(Y^p-Y-a)^2-4c
   points_h=sum(1 for Y in range(p) for W in range(p) if (d*W*W-(-a)**2+4*c)%p==0)
   assert points_h==p*(1-s),(p,c,a,points_h,s)
  # R and H(R) models
  points_r=sum(1 for X in range(1,p) for Y in range(p) if (2*Y-X-c*pow(d*X,-1,p))%p==0)+2
  assert points_r==p+1,(p,c,points_r)
  points_hr=sum(1 for Y in range(p) for W in range(p) if (d*W*W-(2*Y)**2+4*c*pow(d,-1,p))%p==0)
  assert points_hr==p+1,(p,c,points_hr)
 print('OK p=',p,'c values=',p-1,'classes each=',p+3)
print('VERIFY_OK')
