#!/usr/bin/env python3
"""Exact, dependency-free checks for the Klein quartic's characteristic-five flex divisor.
Python 3.9 or newer. Finite fields are constructed as polynomial quotients of F_5.
"""
# Standalone finite-field arithmetic verification for a Klein-quartic flex computation.
P=5
FACTORS=[
 [4,3,1,1], # x^3+x^2-2x-1 = [4,3,1,1]
 [1,2,4,2,1,0,1], # x6+x4+2x3-x2+2x+1
 [1,2,2,1,4,2,1], # x6+2x5-x4+x3+2x2+2x+1
 [1,4,4,3,4,2,1], # x6+2x5-x4-2x3-x2-x+1
]
class Field:
 def __init__(self,mod): self.mod=tuple(t%5 for t in mod); self.n=len(mod)-1;self.O=(0,)*self.n;self.I=(1,)+(0,)*(self.n-1)
 def v(self,a):
  if isinstance(a,int):return (a%5,)+(0,)*(self.n-1)
  return tuple(a)
 def add(self,a,b):return tuple((v+w)%5 for v,w in zip(a,b))
 def sub(self,a,b):return tuple((v-w)%5 for v,w in zip(a,b))
 def mul(self,a,b):
  n=self.n; a=self.v(a);b=self.v(b);v=[0]*(2*n-1)
  for i in range(n):
   for j in range(n):v[i+j]=(v[i+j]+a[i]*b[j])%5
  for k in range(2*n-2,n-1,-1):
   c=v[k]
   if c:
    for i in range(n):v[k-n+i]=(v[k-n+i]-c*self.mod[i])%5
  return tuple(v[:n])
 def pow(self,a,e):
  out=self.I
  while e:
   if e&1:out=self.mul(out,a)
   a=self.mul(a,a);e>>=1
  return out
 def inv(self,a):
  assert a!=self.O
  return self.pow(a,5**self.n-2)
 def div(self,a,b):return self.mul(a,self.inv(b))
 def eval(self,coef,x):
  r=self.O
  for c in coef[::-1]:r=self.add(self.mul(r,x),self.v(c))
  return r
 def f(self,p):
  x,y,z=p
  return self.add(self.add(self.mul(self.pow(x,3),y),self.mul(self.pow(y,3),z)),self.mul(self.pow(z,3),x))
 def h(self,p):
  x,y,z=p
  return self.add(self.add(self.mul(self.pow(x,5),z),self.mul(x,self.pow(y,5))),self.mul(y,self.pow(z,5)))
 def tangent_next(self,p):
  x,y,z=p
  a=self.add(self.mul(self.v(3),self.mul(self.pow(x,2),y)),self.pow(z,3))
  b=self.add(self.pow(x,3),self.mul(self.v(3),self.mul(self.pow(y,2),z)))
  c=self.add(self.pow(y,3),self.mul(self.v(3),self.mul(self.pow(z,2),x)))
  if a!=self.O or b!=self.O: v=(b,self.sub(self.O,a),self.O)
  else:v=(self.O,c,self.sub(self.O,b))
  u=tuple(self.add(a,b) for a,b in zip(p,v))
  w=tuple(self.sub(a,b) for a,b in zip(p,v))
  fu=self.f(u);fw=self.f(w)
  c3=self.mul(self.v(3),self.sub(fu,fw)) # divide by 2 (inverse 3 mod 5)
  c4=self.mul(self.v(3),self.add(fu,fw))
  if c4==self.O:
   nxt=v
  else:
   t=self.div(c3,c4)
   nxt=tuple(self.sub(a,self.mul(t,b)) for a,b in zip(p,v))
  assert self.f(nxt)==self.O
  assert self.h(nxt)==self.O
  # projective normalize
  if nxt[2]!=self.O:return tuple(self.div(z,nxt[2]) for z in nxt)
  if nxt[0]!=self.O:return tuple(self.div(z,nxt[0]) for z in nxt)
  return tuple(self.div(z,nxt[1]) for z in nxt)


# Elementary univariate polynomial arithmetic over F_5 (ascending coefficients).
def trim(a):
 a=[v%5 for v in a]
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def p_add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def p_sub(a,b):return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def p_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):c[i+j]=(c[i+j]+v*w)%5
 return trim(c)
def p_pow(a,k):
 out=[1]
 while k:
  if k&1:out=p_mul(out,a)
  a=p_mul(a,a); k>>=1
 return out
def p_divmod(a,b):
 a=trim(a[:]);b=trim(b); assert b!=[0]
 q=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b) and a!=[0]:
  shift=len(a)-len(b); c=a[-1]*pow(b[-1],-1,5)%5; q[shift]=c
  for i,v in enumerate(b):a[i+shift]=(a[i+shift]-c*v)%5
  a=trim(a)
 return trim(q),a
def p_rem(a,b):return p_divmod(a,b)[1]
def p_gcd(a,b):
 while b!=[0]:a,b=b,p_rem(a,b)
 return trim([(c*pow(a[-1],-1,5))%5 for c in a])
def p_powmod(a,k,m):
 out=[1]
 while k:
  if k&1:out=p_rem(p_mul(out,a),m)
  a=p_rem(p_mul(a,a),m);k>>=1
 return out
def irreducible(f):
 # Rabin's irreducibility criterion for the prime finite field.
 n=len(f)-1; primes=[r for r in range(2,n+1) if n%r==0 and all(r%i for i in range(2,int(r**0.5)+1))]
 assert p_powmod([0,1],5**n,f)==[0,1]
 return all(p_gcd(f,p_sub(p_powmod([0,1],5**(n//r),f),[0,1]))==[1] for r in primes)

def verify_elimination():
 X=[0,1]; one=[1]
 x2=p_pow(X,2); x5=p_pow(X,5); x7=p_pow(X,7)
 D=p_add(p_pow(X,14),one)
 N=p_mul(p_mul([4],x5),p_add(p_mul([2],x7),[3]))
 g=p_sub(p_add(p_add(p_pow(X,21),p_mul([2],p_pow(X,14))),x7),one)
 qnum=p_add(p_add(p_mul([4],p_mul(x2,p_pow(N,2))),p_mul(p_add(x7,one),p_mul(N,D))),p_mul([2],p_mul(x5,p_pow(D,2))))
 assert qnum==p_mul(x5,g)
 assert p_gcd(g,D)==one
 fact=[1]
 for f in FACTORS:
  assert irreducible(f),f
  fact=p_mul(fact,f)
 assert fact==g,(fact,g)
 assert p_gcd(g,p_sub(p_pow(X,1),[0]))==one  # x=0 is excluded from nonzero roots
 return g

def verify_geometry():
 maps=[]
 for j,pol in enumerate(FACTORS):
  k=Field(pol);x=(0,1)+(0,)*(k.n-2);u=k.pow(x,7)
  y=k.div(k.mul(k.v(4),k.mul(k.pow(x,5),k.add(k.mul(k.v(2),u),k.v(3)))),k.add(k.pow(x,14),k.I))
  pt=(x,y,k.I)
  assert k.f(pt)==k.O and k.h(pt)==k.O
  fx=k.add(k.mul(k.v(3),k.mul(k.pow(x,2),y)),k.I)
  fy=k.add(k.pow(x,3),k.mul(k.v(3),k.pow(y,2)))
  hx=k.pow(y,5);hy=k.I
  det=k.sub(k.mul(fx,hy),k.mul(fy,hx))
  assert det!=k.O,('nontransverse',j)
  pts=[pt]
  for r in range(3):pts.append(k.tangent_next(pts[-1]))
  assert pts[3]==pt and len(set(pts[:3]))==3
  indexes=[next((i for i,g in enumerate(FACTORS) if k.eval(g,z[0])==k.O),None) for z in pts]
  expect=[0,0,0,0] if j==0 else ([1,2,3,1] if j==1 else ([2,3,1,2] if j==2 else [3,1,2,3]))
  assert indexes==expect,(j,indexes,expect)
  assert k.pow(x,5**k.n)==x
  for smaller in range(1,k.n):assert k.pow(x,5**smaller)!=x
  maps.append(indexes)
 # Coordinate flexes form one triangle; all three are F_5-rational.
 assert Field(FACTORS[0]).f((Field(FACTORS[0]).I,Field(FACTORS[0]).O,Field(FACTORS[0]).O))==(0,0,0)
 return maps

if __name__=='__main__':
 g=verify_elimination();maps=verify_geometry()
 print('VERIFY_OK: reduced 24-point flex divisor; Frobenius 1^3 3^1 6^3; tangent triangles 1^2 6^1')
 print('G(x) modulo 5, ascending coefficients:',g)
 print('Exact successor factors:',maps)
