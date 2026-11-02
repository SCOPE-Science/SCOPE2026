#!/usr/bin/env python3
"""Exact, dependency-free polynomial certificate for the two-year seed-bank threshold.

Run: python3 proof_checker.py
All operations use Python integers and rational fractions; no sampled inequality
is used to establish the universal parameter statements.
"""
from fractions import Fraction as F
from math import comb

class Poly:
    def __init__(self, c=0):
        if isinstance(c, Poly):
            self.a = c.a.copy()
        elif isinstance(c, dict):
            self.a = {k: F(v) for k, v in c.items() if v}
        else:
            self.a = {(0,0): F(c)} if c else {}
    @staticmethod
    def make(x): return x if isinstance(x, Poly) else Poly(x)
    def __add__(self, other):
        other = self.make(other)
        q = self.a.copy()
        for k, v in other.a.items():
            q[k] = q.get(k,F(0))+v
            if not q[k]: del q[k]
        return Poly(q)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-v for k,v in self.a.items()})
    def __sub__(self,other):return self+-self.make(other)
    def __rsub__(self,other):return self.make(other)+-self
    def __mul__(self,other):
        other=self.make(other)
        q={}
        for (i,j),a in self.a.items():
            for (k,l),b in other.a.items():
                m=(i+k,j+l)
                q[m]=q.get(m,F(0))+a*b
        return Poly(q)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        ans=Poly(1);x=self
        while n:
            if n&1:ans=ans*x
            x=x*x;n//=2
        return ans
    def __eq__(self,other):return self.a==self.make(other).a

class Rat:
    def __init__(self,n=0,d=1):
        self.n=Poly.make(n);self.d=Poly.make(d)
        assert self.d.a
    @staticmethod
    def make(x): return x if isinstance(x,Rat) else Rat(x)
    def __add__(self,other):
        o=self.make(other)
        return Rat(self.n*o.d+o.n*self.d,self.d*o.d)
    __radd__=__add__
    def __neg__(self):return Rat(-self.n,self.d)
    def __sub__(self,other):return self+-self.make(other)
    def __rsub__(self,other):return self.make(other)+-self
    def __mul__(self,other):
        o=self.make(other);return Rat(self.n*o.n,self.d*o.d)
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.make(other);return Rat(self.n*o.d,self.d*o.n)
    def __rtruediv__(self,other):return self.make(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        return Rat(self.n**n,self.d**n)
    def equals(self,other):
        o=self.make(other)
        return self.n*o.d==o.n*self.d

h=Poly({(1,0):1});t=Poly({(0,1):1});one=Poly(1)
Q=h**2+5*h+5
P0=2*h**2+6*h+4
bs=Rat(P0,Q)
g=one-t
z=Rat(one-t)+bs*t
A=z/(z+h)
B=z*h/(one+h)
D=Rat(g)/(g+h)+Rat(g)*h/(one+h)
C=bs*t/(Rat(one+h)+bs*t)
E=A*(A+B)+B*D+(Rat(1)-A)*C
U=h**2+2*h*t+5*h+4*t+5
V=h**3+h**2*t+6*h**2+h*t+10*h-t+5
positive_den=(one+h)**2*(one+h-t)*Q*U*V**2

# Each row is the Bernstein basis coefficients of degree 4 in t
# for successive powers of h.  B_{k,4}(t)=binomial(4,k)*t^k*(1-t)^(4-k).
rows = [
 ['350','235','419/3','62','0'],
 ['2750','2165','9941/6','4851/4','824'],
 ['9790','8517','43937/6','12429/2','5189'],
 ['20585','76629/4','105889/6','64429/4','14578'],
 ['28339','55381/2','80299/3','51187/2','24219'],
 ['26982','54725/2','54895/2','108783/4','26576'],
 ['18378','38363/2','118907/6','20226','20333'],
 ['9147','38997/4','20601/2','43073/4','11110'],
 ['3355','7237/2','11627/3','8237/2','4337'],
 ['896','967','2077/2','4439/4','1180'],
 ['166','177','1129/6','399/2','211'],
 ['19','79/4','41/2','85/4','22'],
 ['1','1','1','1','1'],
]
assert len(rows)==13 and all(len(row)==5 for row in rows)
assert all(F(x)>=0 for row in rows for x in row)
bern=[comb(4,k)*t**k*(one-t)**(4-k) for k in range(5)]
R=Poly(0)
for j,row in enumerate(rows):
    for k,coefficient in enumerate(row):
        R=R+F(coefficient)*h**j*bern[k]
assert (Rat(1)-E).__mul__(positive_den).equals(Rat(h*t**2*R))
assert rows[0][-1]=='0' and all(F(x)>0 for x in rows[-1])

# Independent exact-rational example using the original probability formulas.
b=F(9,10); H=F(1,10); gg=F(3,4)
zz=gg+(1-gg)*b
AA=zz/(zz+H);BB=zz*H/(1+H)
DD=gg/(gg+H)+gg*H/(1+H)
CC=(1-gg)*b/(1+H+(1-gg)*b)
example=AA*(AA+BB)+BB*DD+(1-AA)*CC
assert example-1==F(19650205,6450554528)
assert F(2*H*H+6*H+4,H*H+5*H+5)==F(462,551)
print('PASS: 65 nonnegative exact Bernstein coefficients establish R(h,t)>=0.')
print('PASS: exact polynomial identity D(h,t)[1-E(b_star)]=h*t^2*R(h,t).')
print('PASS: independent rational example E-1=',example-1)
