#!/usr/bin/env python3
"""Exact, standalone F_3 point-count and Weil-polynomial certificate.

Curve: y^3-y=x+1/(x^3-x); smooth projective model.
Uses only integer and polynomial arithmetic over F_3. The four simple
poles (three F_3 points and infinity) each contribute one rational point.
"""
from math import gcd

MODULI = {  # coefficients increasing from constant to leading monic term
 1:(0,1), 2:(1,0,1), 3:(1,0,2,1),
 4:(1,0,1,1,1), 5:(1,0,0,0,2,1), 6:(1,0,0,0,1,1,1),
 7:(1,0,0,0,0,1,2,1), 8:(1,0,0,0,0,1,1,0,1),
 9:(1,0,0,0,0,0,2,1,0,1),
}

def trim(c):
 c=list(c)
 while len(c)>1 and c[-1]%3==0:c.pop()
 return [x%3 for x in c]

def rem(a,b):
 a=trim(a); b=trim(b); inv=pow(b[-1],-1,3)
 while len(a)>=len(b) and any(a):
  k=len(a)-len(b);c=a[-1]*inv%3
  for j,v in enumerate(b):a[k+j]=(a[k+j]-c*v)%3
  a=trim(a)
 return a

def is_irreducible(f):
 n=len(f)-1
 if n==1:return True
 # An explicitly terminating certificate: trial-divide by every monic
 # polynomial of degree <= floor(n/2), over F_3.
 for d in range(1,n//2+1):
  for i in range(3**d):
   coeff=[(i//(3**j))%3 for j in range(d)]+[1]
   if rem(f,coeff)==[0]:return False
 return True

class FiniteField:
 def __init__(self,n,modulus=None):
  self.n=n;self.q=3**n;self.mod=modulus if modulus is not None else MODULI[n]
  assert is_irreducible(self.mod)
  self.place=[3**j for j in range(n)]
  self.digits=[tuple((i//b)%3 for b in self.place) for i in range(self.q)]
  self.neg=[sum((-d%3)*b for d,b in zip(v,self.place)) for v in self.digits]
 def add(self,a,b):
  return sum((u+v)%3*w for u,v,w in zip(self.digits[a],self.digits[b],self.place))
 def multiply(self,a,b):
  n=self.n;aa=self.digits[a];bb=self.digits[b];out=[0]*(2*n-1)
  for i,u in enumerate(aa):
   if u:
    for j,v in enumerate(bb):out[i+j]+=u*v
  for k in range(2*n-2,n-1,-1):
   c=out[k]%3
   if c:
    for j in range(n):out[k-n+j]-=c*self.mod[j]
  return sum((out[j]%3)*self.place[j] for j in range(n))
 def power(self,x,e):
  t=1
  while e:
   if e&1:t=self.multiply(t,x)
   e//=2
   if e:x=self.multiply(x,x)
  return t
 def cube(self,x):return self.multiply(self.multiply(x,x),x)
 def trace(self,x):
  z=0
  for _ in range(self.n):z=self.add(z,x);x=self.cube(x)
  assert z in (0,1,2)
  return z
 def image(self):
  D=[0]*self.q
  for y in range(self.q):D[self.add(self.cube(y),self.neg[y])]+=1
  return D
 def count(self):
  D=self.image();assert sorted(set(D))==[0,3]
  N_via_image=4;N_via_trace=4
  for x in range(self.q):
   d=self.add(self.cube(x),self.neg[x])
   if d==0:continue
   inv=self.power(d,self.q-2)
   assert self.multiply(d,inv)==1
   f=self.add(x,inv)
   N_via_image+=D[f]
   if self.trace(f)==0:N_via_trace+=3
  assert N_via_image==N_via_trace
  return N_via_image

def polynomial_mul(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):C[i+j]+=a*b
 return C

def main():
 counts={}
 for n in range(1,10):
  F=FiniteField(n);counts[n]=F.count()
  if n==3:assert FiniteField(n,(1,1,2,1)).count()==counts[n]
  if n==6:assert FiniteField(n,(1,0,0,0,1,2,1)).count()==counts[n]
  if n%3:assert counts[n]==3**n+1  # translation-orbit theorem
 assert [counts[n] for n in range(1,10)]==[4,10,76,82,244,670,2188,6562,18868]
 # Newton identities (C(T)=exp(-sum_n s_n T^n/n)), s_n=3^n+1-N_n.
 c=[1]
 for n in range(1,7):
  s=[3**j+1-counts[j] for j in range(1,n+1)]
  num=-sum(c[n-j]*s[j-1] for j in range(1,n+1))
  assert num%n==0
  c.append(num//n)
 for n in range(7,13):c.append(3**(n-6)*c[12-n])
 expected=[1,0,0,16,0,0,118,0,0,432,0,0,729]
 assert c==expected
 # Factorization, plus exact coefficient and rational-point checks.
 E=[1,-1,3];A=[1,1,-2,3,9]
 p=polynomial_mul(polynomial_mul(E,E),polynomial_mul(A,A))
 assert p==expected
 assert sum(p)==1296
 for n in (7,8,9):
  s=3**n+1-counts[n]
  assert -sum(c[k]*(3**(n-k)+1-counts[n-k]) for k in range(1,n)) - n*c[n]==s
 # Show irreducibility of z^4+z^3-2z^2+3z+9:
 # Every rational monic factor inherits Weil roots of modulus sqrt(3),
 # so each integral quadratic factor has constant term +3 or -3.
 # Verify all coefficient comparisons: a+c=1, bd=9,
 # ac+b+d=-2, ad+bc=3. Explicit finite bounds are valid because
 # the quadratic Weil factors have |a|,|c| <= 2sqrt(3)<4.
 assert not any(a+c==1 and b*d==9 and a*c+b+d==-2 and
                a*d+b*c==3 for a in range(-3,4)
                for c in range(-3,4) for b in (-3,3) for d in (-3,3))
 print('COUNTS',counts)
 print('WEIL_COEFFICIENTS',expected)
 print('FACTOR_E',E,'FACTOR_A2',A)
 print('JAC_F3',sum(p))
 print('VERIFY_OK')

if __name__=='__main__':main()
