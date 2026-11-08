from collections import Counter
from fractions import Fraction
from math import gcd

def deg(x):return x.bit_length()-1

def rem(a,p):
 while a and deg(a)>=deg(p): a^=p <<(deg(a)-deg(p))
 return a

def divmod2(a,p):
 q=0
 while a and deg(a)>=deg(p):
  k=deg(a)-deg(p);q^=1<<k;a^=p<<k
 return q,a

def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  a<<=1;b>>=1
 return z

def mulmod(a,b,p):return rem(mul(a,b),p)

def powmod(a,n,p):
 z=1
 while n:
  if n&1:z=mulmod(z,a,p)
  a=mulmod(a,a,p);n//=2
 return z

def invert(a,p):
 d=deg(p)
 r=powmod(rem(a,p),(1<<d)-2,p)
 assert mulmod(r,rem(a,p),p)==1
 return r

def der(a):
 return sum((1<<(i-1)) for i in range(1,deg(a)+1,2) if a>>i&1)

def trace(x,p):
 a=0
 for i in range(deg(p)):
  a^=x;x=mulmod(x,x,p)
 assert a in (0,1),(x,a,p)
 return a

def bit(f,P):
 q,r=divmod2(f,P)
 if r or rem(q,P)==0:return 0
 dd=mulmod(rem(0b110,P),der(P),P)
 v=mulmod(invert(dd,P),invert(rem(q,P),P),P)
 return trace(v,P)

P=0b111;Q=0b1011;d=10
c=Counter((bit((1<<d)|j,P),bit((1<<d)|j,Q)) for j in range(1<<d))
print('exact-degree-10',dict(c))
assert c=={(0,0):840,(1,0):120,(0,1):56,(1,1):8}
for R in (P,Q):
 print('R',R,'degree',deg(R),'1-bit count',sum(bit((1<<d)|j,R) for j in range(1<<d)),'of',1<<d)
print('SIMPLE_POLE_VERIFY_OK')

def bit_e2_h(h,P):
 a=mul(0b110,h)
 da=der(a)
 aa=rem(a,P)
 dp=der(P)
 den=mulmod(mulmod(aa,aa,P),mulmod(dp,dp,P),P)
 r=mulmod(rem(da,P),invert(den,P),P)
 return trace(r,P)
for R in (P,Q):
 j=deg(R);n=2*j
 values=[bit_e2_h((1<<n)|t,R) for t in range(1<<n) if rem((1<<n)|t,R)!=0]
 print('SECOND_POLE',R,'n',n,'ones',sum(values),'samples',len(values))
 assert sum(values)*2==len(values)

# Check polynomial prime counts and Euler-product constant independently.
import math

def divisors(n):
    return [a for a in range(1,n+1) if n%a==0]

def mu(n):
    t=n; sq=0; sign=1; p=2
    while p*p<=t:
        if t%p==0:
            t//=p;sign=-sign
            if t%p==0:return 0
            while t%p==0:t//=p
        p+=1
    return -sign if t>1 else sign

def irreducible_count(j):
    v=sum(mu(a)*(1<<(j//a)) for a in divisors(j))
    assert v%j==0
    return v//j

for j, target in [(2,1),(3,2),(4,3),(5,6),(6,9),(7,18)]:
    assert irreducible_count(j)==target,(j,irreducible_count(j))
s=0.0
for j in range(2,151):
    I=irreducible_count(j)
    q=2.0**(-j)
    beta=(q+q*q)/2
    s+=I*math.log1p(-beta)+1/(2*j)
constant=math.exp((1-math.euler_gamma)/2+s) if hasattr(math,'euler_gamma') else math.exp((1-0.5772156649015329)/2+s)
assert abs(constant-1.43035954186854)<2e-10,constant
for B in [10,20,50]:
    logH=sum(irreducible_count(j)*math.log1p(-(2.0**(-j)+2.0**(-2*j))/2) for j in range(2,B+1))
    print('SIEVE_PRODUCT',B, 'prob', f'{math.exp(logH):.12f}', 'scaled',f'{math.exp(logH)*math.sqrt(B):.12f}')
print('EULER_PRODUCT_C',f'{constant:.12f}')
print('VERIFY_OK exact_arithmetic_and_independent_sieve=yes')
