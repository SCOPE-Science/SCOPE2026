#!/usr/bin/env python3
"""Exact algebraic and trapping-interval checks for a rational interval map.
Requires only Python 3 standard library. Run: python3 verify.py.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb

@dataclass(frozen=True)
class Quad:
    a: F = F(0)
    b: F = F(0)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, 'a', F(a))
        object.__setattr__(self, 'b', F(b))

    def __add__(self, y):
        y = as_quad(y)
        return Quad(self.a + y.a, self.b + y.b)
    __radd__ = __add__
    def __neg__(self):
        return Quad(-self.a, -self.b)
    def __sub__(self, y):
        return self + (-as_quad(y))
    def __rsub__(self, y):
        return as_quad(y) - self
    def __mul__(self, y):
        y = as_quad(y)
        return Quad(self.a*y.a + 2*self.b*y.b, self.a*y.b + self.b*y.a)
    __rmul__ = __mul__

def as_quad(x):
    return x if isinstance(x, Quad) else Quad(x)

def sign(z):
    """Exact sign in Q(sqrt(2)): compare a^2 with 2b^2."""
    z = as_quad(z)
    a,b = z.a,z.b
    if b == 0: return (a>0)-(a<0)
    if a == 0: return (b>0)-(b<0)
    if (a>0) == (b>0): return (a>0)-(a<0)
    c = a*a-2*b*b
    if c == 0: raise AssertionError('sqrt(2) rational')
    return ((a>0)-(a<0)) * ((c>0)-(c<0))

def poly_add(p,q):
    return [ (p[i] if i<len(p) else Quad()) + (q[i] if i<len(q) else Quad()) for i in range(max(len(p),len(q))) ]

def poly_neg(p): return [-v for v in p]
def poly_sub(p,q): return poly_add(p,poly_neg(q))
def poly_mul(p,q):
    r=[Quad() for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]=r[i+j]+a*b
    return r

def poly_scale(p,x):return [a*x for a in p]
def poly_eval(p,x):
    z=Quad()
    for a in reversed(p):z=z*x+a
    return z

s=Quad(0,1)
c=s-1
k=3-2*s
m=[Quad(),Quad(1)]
one=[Quad(1)]
u=poly_scale(m,k)
V=poly_mul(poly_mul(m,u),poly_sub(one,u))
W=poly_add(one,u)
N=poly_sub(poly_mul(poly_mul(m,V),poly_sub(W,V)),poly_scale(poly_mul(W,poly_add(W,V)),c))
Q=[-99-70*s,-75-53*s,-51-36*s,20+14*s,9+6*s,-5-3*s,Quad(1)]
C=-577+408*s
assert sign(C)<0
assert N==poly_scale(poly_mul([-(1+s),Quad(1)],Q),C), 'critical-return factorization'

# Descartes certificate: Q negative on [0,4], exactly one positive root >4.
J=[sum((Q[i]*(4**i)*comb(6-i,j-i) for i in range(j+1)),Quad()) for j in range(7)]
J_expected=[-99-70*s,-894-632*s,-3801-2686*s,-6964-4928*s,-3237-2402*s,-2030-1096*s,1345-1498*s]
assert J==J_expected and all(sign(a)<0 for a in J)
shift=[sum((Q[i]*comb(i,j)*4**(i-j) for i in range(j,7)),Quad()) for j in range(7)]
shift_expected=[1345-1498*s,2525-1973*s,1693-1212*s,644-370*s,149-54*s,19-3*s,Quad(1)]
assert shift==shift_expected
assert [sign(a) for a in shift]==[-1,-1,-1,1,1,1,1]
lo=F(56449,10000)
hi=F(5645,1000)
assert sign(poly_eval(Q,Quad(lo)))<0 and sign(poly_eval(Q,Quad(hi)))>0
assert sign((3+2*s)-hi)>0

# Exact, uniform, cyclic trapping intervals for every parameter in [lo,hi].
J0=(F(413,1000),F(415,1000))
A=(F(9685,10000),F(9686,10000))
B=(F(872,10000),F(875,10000))

def f(mu,x):return mu*x*(1-x)/(1+x)
def der(mu,x):return mu*(1-2*x-x*x)/(1+x)**2
assert B[1]<J0[0] and J0[1]<A[0]
# Unique maximizer of g(x)=x(1-x)/(1+x) is c=sqrt(2)-1 in J0.
assert sign(c-J0[0])>0 and sign(J0[1]-c)>0
assert min(f(lo,J0[0]),f(lo,J0[1]))>A[0]
assert sign(A[1]-hi*k)>0
# f decreases on A and increases on B.
assert A[0]>F(1,2) and B[1]<F(1,4)
assert f(lo,A[1])>B[0] and f(hi,A[0])<B[1]
assert f(lo,B[0])>J0[0] and f(hi,B[1])<J0[1]
# f''(x)=-4mu/(1+x)^3<0, so f' decreases in x;
# with fixed x, f' is linear in mu.
def derivative_bound(interval):
    x0,x1=interval
    return max(abs(der(mu,x)) for mu in (lo,hi) for x in (x0,x1))
assert derivative_bound(J0)<F(1,100)
assert derivative_bound(A)<F(11,4)
assert derivative_bound(B)<F(4)
assert F(1,100)*F(11,4)*F(4)<1

# A superattracting three-cycle at the unique critical-return parameter.
# Numeric values are supplementary and are not used for acceptance.
from decimal import Decimal, getcontext
getcontext().prec=50
sq=Decimal(2).sqrt()
c0=sq-1
kd=3-2*sq
def fd(mu,x):return mu*x*(1-x)/(1+x)
def qd(mu):
    return (mu**6-(5+3*sq)*mu**5+(9+6*sq)*mu**4+
            (20+14*sq)*mu**3-(51+36*sq)*mu**2-
            (75+53*sq)*mu-(99+70*sq))
a,b=Decimal(lo.numerator)/Decimal(lo.denominator),Decimal(hi.numerator)/Decimal(hi.denominator)
for _ in range(160):
    h=(a+b)/2
    if qd(h)<0:a=h
    else:b=h
mu=(a+b)/2
x=c0
orbit=[x]
for _ in range(3):
    x=fd(mu,x)
    orbit.append(x)
assert abs(orbit[3]-orbit[0])<Decimal('1e-36')
assert Decimal(J0[0].numerator)/Decimal(J0[0].denominator)<orbit[0]<Decimal(J0[1].numerator)/Decimal(J0[1].denominator)
print('PASS: factorization in Q(sqrt2), root uniqueness and rational root bracket;')
print('      exact cyclic interval inclusions and derivative contraction for a parameter band')
print('superstable_parameter =', mu)
print('critical_three_cycle =', [str(z) for z in orbit[:3]])
print('bound_multiplier =',F(1,100)*F(11,4)*F(4))
