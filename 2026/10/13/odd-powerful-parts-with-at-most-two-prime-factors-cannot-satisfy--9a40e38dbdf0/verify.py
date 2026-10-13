from math import isqrt,gcd
from fractions import Fraction

def fac(n):
 d={};x=n;p=2
 while p*p<=x:
  while x%p==0:d[p]=d.get(p,0)+1;x//=p
  p+=1
 if x>1:d[x]=d.get(x,0)+1
 return d

def ff(n):
 a=fac(n);t=1;s=1
 for p,e in a.items():
  if e>=2:t*=p**e
  else:s*=p
 return s,t,a

def B(t):
 f=fac(t);x=y=1
 for p,a in f.items():
  assert a>=2
  x*=p**a+1
  y*=p**a-p**(a-1)+1
 return x-y

def sigmasf(s):
 a=1
 for p in fac(s):a*=p+1
 return a

def unitphi(d):
 return __import__('functools').reduce(lambda z,x:z*x,(p**e if e==1 else p**e-p**(e-1) for p,e in fac(d).items()),1)

def divisors(n):
 f=fac(n);d=[1]
 for p,a in f.items():d=[x*p**j for x in d for j in range(a+1)]
 return d

for n in range(2,10000):
 s,t,fs=ff(n)
 if t>1:
  T=sum(unitphi(d) for d in divisors(n) if gcd(d,n//d)>1)
  assert T==sigmasf(s)*B(t),(n,T,sigmasf(s)*B(t))
  if t%2 and len(fac(t))<=2: assert T!=n,(n,s,t)
print('Direct nonunitary totient identity and two-support obstruction CHECK_OK through 9999')

mx=(Fraction(0),None)
for p in (3,5,7,11,13,17,19):
 for q in (3,5,7,11,13,17,19):
  if q<=p:continue
  for a in range(2,7):
   for b in range(2,7):
    x=p**a*q**b
    bval=Fraction(B(x),x)
    if bval>mx[0]:mx=(bval,(p,q,a,b))
    assert bval<=Fraction(113,225), (p,q,a,b,bval)
print('Ratio maximum tested:',mx,'5/9=',Fraction(5,9))
