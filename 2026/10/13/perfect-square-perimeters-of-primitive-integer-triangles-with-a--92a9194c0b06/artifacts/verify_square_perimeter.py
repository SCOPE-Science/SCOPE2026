import math
from collections import defaultdict

def original(a,b,c):
 return math.gcd(a, math.gcd(b,c))==1 and a>b>0 and a>c>b and a*a-a*b+b*b==c*c

def via_parameters(X):
 K=math.isqrt(X)//3; got=set()
 for u in range(1,4*math.isqrt(K)+10):
  for v in range(1,K//u+1):
   if math.gcd(u,v)!=1:continue
   for r,s,allow in ((3*u*u,v*v,v%3!=0),(u*u,3*v*v,u%3!=0)):
    if not allow or not r<s<2*r:continue
    m,n=r+s,2*r-s
    a=(m*m-n*n)//3
    b=n*(2*m-n)//3
    c=(m*m-m*n+n*n)//3
    assert original(a,b,c)
    assert a+b+c==9*(u*v)**2
    assert (a,b,c) not in got
    got.add((a,b,c))
 return got

def divisor_pairs_fourth_power(q):
 # q^4 is the factor pair product; derive its divisors from trial factoring q
 t=q;primes=[];e=[];p=2
 while p*p<=t:
  if t%p==0:
   z=0
   while t%p==0:t//=p;z+=1
   primes.append(p);e.append(z*4)
  p+=1
 if t>1:primes.append(t);e.append(4)
 divisors=[1]
 for p,z in zip(primes,e):
  powers=[p**i for i in range(z+1)]
  divisors=[d*h for d in divisors for h in powers]
 n=q**4
 for d in divisors:
  if d<=math.isqrt(n):yield d,n//d

def via_perimeter_factors(X):
 ans=set()
 for q in range(1,math.isqrt(X)+1):
  P=q*q
  for U,V in divisor_pairs_fourth_power(q):
   if (2*P-U)%3 or (2*P-V)%3:continue
   a,b=(2*P-U)//3,(2*P-V)//3
   c=P-a-b
   if original(a,b,c):ans.add((a,b,c))
 return ans

if __name__=='__main__':
 C=3*math.log(2)/(4*math.pi**2)
 for X in (100,1000,10000,100000,1000000,10000000):
  a=via_parameters(X);b=via_perimeter_factors(X)
  assert a==b,(X,len(a),len(b),sorted(a^b)[:5])
  print('X=',X,'count=',len(a),'norm=',f'{len(a)/math.sqrt(X):.9f}','constant=',f'{C:.9f}')
 print('SQUARE_PERIMETER_EISENSTEIN_EXACT_REGRESSION_OK')
