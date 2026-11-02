"""Exact outward-rational interval verification for a fifth-order Hopf branch coefficient.
Python 3 standard library only; no approximate floating point operations.
"""
from math import isqrt
from collections import defaultdict
S=10**36
def ceildiv(a,b): return -((-a)//b)
class I:
 def __init__(self, a, b=None):
  self.a=a;self.b=a if b is None else b
  assert self.a<=self.b
 @staticmethod
 def integer(n): return I(n*S)
 @staticmethod
 def root(n):
  t=isqrt(n*S*S)
  assert t*t<=n*S*S<(t+1)*(t+1)
  return I(t,t+1)
 def __add__(self,other):
  other=lift(other);return I(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,other):return self+-lift(other)
 def __rsub__(self,other):return lift(other)+-self
 def __mul__(self,other):
  if isinstance(other,Z): return NotImplemented
  other=lift(other);t=[self.a*other.a,self.a*other.b,self.b*other.a,self.b*other.b]
  return I(min(t)//S,ceildiv(max(t),S))
 __rmul__=__mul__
 def inverse(self):
  assert self.a*self.b>0
  return I((S*S)//self.b,ceildiv(S*S,self.a))
 def __truediv__(self,other):return self*lift(other).inverse()
 def __rtruediv__(self,other):return lift(other)/self
 def out(self,digits=18):
  from decimal import Decimal
  return f'[{Decimal(self.a)/Decimal(S):.{digits}g}, {Decimal(self.b)/Decimal(S):.{digits}g}]'
def lift(x):
 if isinstance(x,I):return x
 assert isinstance(x,int)
 return I.integer(x)
class Z:
 def __init__(self,re=0,im=0):self.re=lift(re);self.im=lift(im)
 def __add__(self,z):
  z=c(z);return Z(self.re+z.re,self.im+z.im)
 __radd__=__add__
 def __neg__(self):return Z(-self.re,-self.im)
 def __sub__(self,z):return self+-c(z)
 def __rsub__(self,z):return c(z)+-self
 def __mul__(self,z):
  z=c(z);return Z(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
 __rmul__=__mul__
 def conj(self):return Z(self.re,-self.im)
 def __truediv__(self,z):
  z=c(z);den=z.re*z.re+z.im*z.im
  t=self*z.conj()
  return Z(t.re/den,t.im/den)
 def __rtruediv__(self,z):return c(z)/self
 def out(self):return f'{self.re.out()} + i {self.im.out()}'
def c(x):
 if isinstance(x,Z):return x
 return Z(x)
rt2=I.root(2);rt6=I.root(6)
gamma=rt2*4/9-I.integer(2)/3
qabs={0:Z(0),1:Z(rt2/2,rt2/2),2:Z(1,1),3:Z(rt6/2,rt6/2),4:Z(rt2,rt2)}
def q(k):return qabs[abs(k)] if k>=0 else qabs[-k].conj()
L0=lambda k:Z(1,k)-rt2*q(k)
Lu=lambda k:-q(k)
Lw=lambda k:Z(0,k)-rt2*q(k)/2
u={(1,1):Z(I.integer(1)/2),(1,-1):Z(I.integer(1)/2)}
def product(*ds):
 d={(0,0):Z(1)}
 for v in ds:
  w={}
  for (n,k),x in d.items():
   for (m,j),y in v.items():w[n+m,k+j]=w.get((n+m,k+j),Z(0))+x*y
  d=w
 return d
def nonlinear(n,k):
 return product(u,u).get((n,k),Z(0)) +gamma*product(u,u,u).get((n,k),Z(0))
def solve(A,B,r):
 det=A.re*B.im-A.im*B.re
 return (r.re*B.im-r.im*B.re)/det,(A.re*r.im-A.im*r.re)/det
for k in (-2,0,2):u[2,k]=nonlinear(2,k)/L0(k)
mu2res,omega2res=solve(Lu(1),Lw(1),nonlinear(3,1)*2)
# Symbolic identity from the exact third-order solvability formula:
# gamma=4 sqrt(2)/9-2/3 makes mu2 exactly zero.
mu2=I.integer(0)
omega2=-(I.integer(7)/6+gamma*3/4)
assert mu2res.a<=0<=mu2res.b
assert omega2res.a<=omega2.b and omega2.a<=omega2res.b
print('mu2 exactly 0; omega2',omega2.out())
for k in (-3,3):u[3,k]=nonlinear(3,k)/L0(k)
L2=lambda k:Lu(k)*mu2+Lw(k)*omega2
for k in (-4,-2,0,2,4):u[4,k]=(nonlinear(4,k)-L2(k)*u.get((2,k),Z(0)))/L0(k)
B4=lambda k:rt2*q(k)*omega2*omega2/8-q(k)*mu2*omega2/2
rhs=(nonlinear(5,1)-B4(1)/2)*2
mu4,omega4=solve(Lu(1),Lw(1),rhs)
print('mu4',mu4.out(34),'omega4',omega4.out(34))
assert mu4.a>70584603791928416421*S//10**20
assert mu4.b<70584603791928416422*S//10**20
assert omega4.b<0
print('EXACT_OUTWARD_INTERVAL_QUINTIC_SIGN_PASS')
