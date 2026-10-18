from fractions import Fraction as Q
import random

def pow2(e): return Q(2**e) if e>=0 else Q(1,2**(-e))
def round_binary(z,p):
    assert z>0
    n,d=z.numerator,z.denominator
    e=n.bit_length()-d.bit_length()
    if z<pow2(e): e-=1
    if z>=pow2(e+1): e+=1
    scaled=z/pow2(e-p+1)
    a,r=divmod(scaled.numerator,scaled.denominator)
    if 2*r>scaled.denominator or (2*r==scaled.denominator and a%2): a+=1
    return a*pow2(e-p+1)

def successor(s,p):
    n,d=s.numerator,s.denominator
    e=n.bit_length()-d.bit_length()
    if s<pow2(e):e-=1
    return s+pow2(e-p+1)

N=0
for p in range(3,11):
 for J in range(1,6):
  for lower in (True,False):
   s=Q(1); S=s
   while s<pow2(J):
    nxt=successor(s,p);gap=nxt-s
    c=Q(1,2)+pow2(-p) if lower else Q(3,2)-pow2(1-p)
    x=c*gap
    assert round_binary(x,p)==x,('not rep',p,J,lower,x)
    t=round_binary(s+x,p)
    assert t==nxt,(p,J,lower,s,x,t,nxt)
    assert t>s and t>x
    S+=x;s=t
    assert (s+1)/2<=S<=(Q(3,2)+pow2(-p))*s-Q(1,2)
    N+=1
   assert S==1+c*(pow2(J)-1)
print('constructive round-trip and bound checks:',N)
random.seed(341)
for p in range(3,10):
 for j in range(3000):
  a=random.randrange(0,pow(2,p))
  s=(2**(p-1)+a%(2**(p-1)))*pow2(random.randint(-5,5)-p+1)
  b=(2**(p-1)+random.randrange(2**(p-1)))*pow2(random.randint(-8,4)-p+1)
  y=round_binary(s+b,p)
  if y>s:
   assert (y+s)/2<=s+b<=(Q(3,2)+pow2(-p))*y-Q(1,2)*s, (p,s,b,y)
   N+=1
print('all exact checks:',N)
