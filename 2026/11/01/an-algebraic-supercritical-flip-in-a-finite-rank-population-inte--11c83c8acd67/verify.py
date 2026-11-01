#!/usr/bin/env python3
"""Exact-rational interval verification of a rank-three-kernel flip theorem.

Requires Python 3 and SymPy. Each asserted sign or interval bound follows from
rational operations; decimal output is informational, not an assumption.
"""
from fractions import Fraction as F

# Independent symbolic reconstruction of the exact Fourier reduction.
import sympy as sp
a,b,c,lam,t=sp.symbols('a b c lam t')
G=sp.Matrix([lam*(5*a-4*a*a+4*a*b-8*b*b-8*c*c)/5,
             lam*(a*a+5*b-8*a*b+3*b*b+c*c)/10,
             lam*c*(5-8*a+2*b)/10])
ns=1-5*t*t+16*t**3; ds=1-4*t-t*t+8*t**3
xx=5*t/ns; yy=5*t*t/ns; ll=ns/ds
subs={a:xx,b:yy,c:0,lam:ll}
assert sp.factor(G[0].subs(subs)-xx)==0
assert sp.factor(G[1].subs(subs)-yy)==0
Ae=G[:2,:].jacobian([a,b]).subs(subs)
Q=384*t**6-44*t**5-447*t**4+122*t**3+88*t**2-34*t+3
assert sp.factor((Ae+sp.eye(2)).det()*ds**2-Q)==0
A_formula=sp.Matrix([[(16*t**3-t**2-8*t+1)/ds,-4*t*(4*t-1)/ds],
                     [-t*(4*t-1)/ds,(16*t**3+t**2-8*t+1)/(2*ds)]])
assert sp.simplify(Ae-A_formula)==sp.zeros(2)
assert sp.factor(sp.diff(G[2],c).subs(subs)-(16*t**3-3*t**2-8*t+1)/(2*ds))==0

class I:
    def __init__(self, a, b=None):
        if isinstance(a,I): self.lo,self.hi=a.lo,a.hi
        else:
            self.lo=F(a); self.hi=F(a if b is None else b)
        assert self.lo<=self.hi
    @staticmethod
    def cv(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=I.cv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-I.cv(o))
    def __rsub__(self,o): return I.cv(o)+(-self)
    def __mul__(self,o):
        o=I.cv(o); p=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I.cv(o); assert not(o.lo<=0<=o.hi), ('zero denominator',o)
        return self*I(F(1)/o.hi,F(1)/o.lo)
    def __rtruediv__(self,o): return I.cv(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==1: return I(self.lo**n,self.hi**n)
        if self.lo<=0<=self.hi:return I(0,max(self.lo**n,self.hi**n))
        return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def within(self, a, b): return F(a)<self.lo<=self.hi<F(b)
    def __repr__(self):return '[%.14g, %.14g]'%(float(self.lo),float(self.hi))

def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def mm(A,v):return [dot(row,v) for row in A]
def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def pol(coeff,x):
    y=I(0)
    for c in coeff:y=y*x+c
    return y

# The unique root used is isolated between these two exact rational endpoints.
lo=F(166763953195,10**12); hi=F(166763953197,10**12)
coeff=[384,-44,-447,122,88,-34,3]
assert pol(coeff,I(lo)).lo>0 and pol(coeff,I(hi)).hi<0
assert pol([6*384,5*(-44),4*(-447),3*122,2*88,-34],I(lo,hi)).hi<0
T=I(lo,hi)
N=1-5*T**2+16*T**3
D=1-4*T-T**2+8*T**3
Lam=N/D; X=5*T/N; Y=T*X
A=[[(16*T**3-T**2-8*T+1)/D,-4*T*(4*T-1)/D],
   [-T*(4*T-1)/D,(16*T**3+T**2-8*T+1)/(2*D)]]
assert Lam.within(F(273247,100000),F(273249,100000))
assert X.within(F(89163,100000),F(89165,100000))
assert Y.within(F(14868,100000),F(14871,100000))
assert (X-2*Y).lo>0
# Exact maximum of kappa(theta)*u(theta) on cos(theta) in [-1,1].
vertex=1-1/(4*T)
assert vertex.within(-1,1)
max_product=(4*T+1)**2/(4*N)
assert max_product.within(F(74,100),F(75,100))

# The critical even multiplier is -1. At a root of the flip polynomial,
# the second even eigenvalue is trace(A)+1.
other=A[0][0]+A[1][1]+1
odd=(16*T**3-3*T**2-8*T+1)/(2*D)
assert other.within(F(-181,1000),F(-178,1000))
assert odd.within(F(-503,1000),F(-500,1000))

# Center eigenvectors: v[0]=1, w*v=1. All critical formulas are rational.
v=[I(1),-(A[0][0]+1)/A[0][1]]
w0=[-(A[1][1]+1),A[0][1]]
w=[a/dot(w0,v) for a in w0]
assert v[1].within(F(-247,1000),F(-244,1000))

def B(u,v):
    return [Lam*(-F(8,5)*u[0]*v[0]+F(4,5)*(u[0]*v[1]+u[1]*v[0])-F(16,5)*u[1]*v[1]),
            Lam*(F(1,5)*u[0]*v[0]-F(4,5)*(u[0]*v[1]+u[1]*v[0])+F(3,5)*u[1]*v[1])]

# Inverse of A-I, using interval determinant bounded away from zero.
J=[[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]]
Jinv=inv2(J)
h=[-t for t in mm(Jinv,B(v,v))]
c=-dot(w,B(v,h))  # cubic coefficient of the second iterate
# Parameter derivative of the fixed point, then of its critical eigenvalue.
xdot=[-t for t in mm(Jinv,[X/Lam,Y/Lam])]
nu_prime=dot(w,[p/Lam+q for p,q in zip(mm(A,v),B(xdot,v))])
assert c.within(F(-192,10),F(-191,10)), c
assert nu_prime.within(F(-98,100),F(-96,100)), nu_prime
assert c.hi<0 and nu_prime.hi<0
print('Root bracket (exact rational):',lo,hi)
print('Growth threshold:',Lam)
print('Fixed Fourier coefficients:',X,Y)
print('Positive-density maximum kappa*u:',max_product)
print('Other even eigenvalue:',other)
print('Odd eigenvalue:',odd)
print('Second-iterate cubic coefficient:',c)
print('Critical multiplier derivative:',nu_prime)
print('All exact-rational assertions passed.')
