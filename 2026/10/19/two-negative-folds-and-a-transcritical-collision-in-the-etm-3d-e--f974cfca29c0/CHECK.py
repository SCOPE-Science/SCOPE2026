"""Exact algebraic checks for the negative-parameter ETM-3D equilibrium diagram.
Run with Python 3 and SymPy: python CHECK.py.
All asserted root counts and sign enclosures are rational computations.
"""
from fractions import Fraction as Q
import sympy as s

r,x=s.symbols('r x')
d=2*x*x+r*x+5-r*r
f=s.expand(2*d*d+5*r*d-5*x*(r+x))
p=(594*r**8-2076*r**7-5948*r**6+20050*r**5+25505*r**4
   -66100*r**3-63325*r**2+77500*r+75000)
assert s.expand(s.discriminant(f,x)-12000*p)==0
# Check the complete original equilibrium elimination, not just the quartic.
Y=5*x/d
Z=x*(r+x)/d
assert s.cancel((-2*x-r*Y+Y*Z)*d**2+x*f)==0
assert s.cancel((x-Y+r*Z-2*x*Z)*d)==0
assert s.cancel(((r+x)*Y-5*Z)*d)==0
assert s.expand(s.det(s.Matrix([[-1,r-2*x],[r+x,-5]]))-d)==0
y,z,lam=s.symbols('y z lam')
J=s.Matrix([[-2,z-r,y],[1-2*z,-1,r-2*x],[y,r+x,-5]])
assert s.expand(s.trace(J)+8)==0
expected_c2=17+(r-z)*(1-2*z)-y**2-(r-2*x)*(r+x)
assert s.expand(s.Poly(J.charpoly(lam).as_expr(),lam).coeff_monomial(lam)-expected_c2)==0
assert s.gcd(p,s.diff(p,r))==1
P=s.Poly(p,r)
assert P.count_roots(-s.oo,0)==2
cases=[(Q(-2011934533282,10**12),Q(-2011934533281,10**12),
        Q(620900,10**6),Q(620902,10**6),
        (-32,-30),(-40,-37),(-43,-40)),
       (Q(-1308660544092,10**12),Q(-1308660544091,10**12),
        Q(103166,10**6),Q(103169,10**6),
        (13,15),(30,34),(16,20))]
for lo,hi,*_ in cases:
    assert P.count_roots(s.Rational(lo.numerator,lo.denominator),s.Rational(hi.numerator,hi.denominator))==1
for rv,ct in [(s.Integer(-3),4),(-s.Rational(3,2),2),(s.Integer(-1),0)]:
    assert s.Poly(f.subs(r,rv),x).count_roots(-s.oo,s.oo)==ct
assert s.factor(f.subs(x,0))==(r*r-5)*(2*r*r-5*r-10)

# The degree-one signed subresultant of f and d f/dx is -1280*(A*x+B).
A=576*r**4-1000*r**3-3280*r**2+2900*r+5250
B=306*r**5-610*r**4-2120*r**3+2275*r**2+4325*r
assert s.expand(s.subresultants(f,s.diff(f,x),x)[-2]+1280*(A*x+B))==0

class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.lo,self.hi=a.lo,a.hi;return
        self.lo=Q(a);self.hi=Q(b) if b is not None else Q(a)
        assert self.lo<=self.hi
    def __add__(self,z):
        z=I(z);return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,z):return self+(-I(z))
    def __rsub__(self,z):return I(z)-self
    def __mul__(self,z):
        z=I(z);t=[a*b for a in (self.lo,self.hi) for b in (z.lo,z.hi)]
        return I(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=I(z)
        assert z.lo>0 or z.hi<0, (z.lo,z.hi)
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,z):return I(z)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0 and self.lo<=0<=self.hi:return I(0,max(self.lo**n,self.hi**n))
        if n%2==0:return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
        return I(self.lo**n,self.hi**n)
    def within(self,low,high):return Q(low)<self.lo and self.hi<Q(high)

# Evaluate integer polynomials by Horner with no floating point operations.
def poly_iv(expr,var,t):
    cs=s.Poly(expr,var).all_coeffs()
    out=I(0)
    for c in cs:
        assert c.is_Rational
        out=out*t+I(Q(int(s.numer(c)),int(s.denom(c))))
    return out

for lo,hi,xlo,xhi,c2bounds,frbounds,fxxbounds in cases:
    R=I(lo,hi)
    X=-poly_iv(B,r,R)/poly_iv(A,r,R)
    assert X.lo>xlo and X.hi<xhi,(float(X.lo),float(X.hi),float(xlo),float(xhi))
    D=2*X**2+R*X+5-R**2
    Y=5*X/D
    Z=X*(R+X)/D
    c2=17+(R-Z)*(1-2*Z)-Y**2-(R-2*X)*(R+X)
    fx2=4*(4*X+R)**2+16*D+20*R-10
    fr=4*D*(X-2*R)+5*D+5*R*(X-2*R)-5*X
    assert c2.within(*c2bounds),(float(c2.lo),float(c2.hi))
    assert fr.within(*frbounds),(float(fr.lo),float(fr.hi))
    assert fx2.within(*fxxbounds),(float(fx2.lo),float(fx2.hi))
    print('fold parameter interval:',float(lo),float(hi),
          '; x interval:',float(X.lo),float(X.hi),
          '; nonzero lambda coefficient:',float(c2.lo),float(c2.hi))

# The negative origin transition is strictly between the folds and is simple.
tau=(5-s.sqrt(105))/4
assert s.simplify(f.subs(x,0).subs(r,tau))==0
assert s.simplify(s.diff(f,x).subs({x:0,r:tau}))!=0
assert -s.Rational(2011934533281,10**12)<tau< -s.Rational(1308660544092,10**12)
# Right/left origin zero eigenvectors and nondegenerate reduced normal form.
M=s.Matrix([[-2,-r,0],[1,-1,r],[0,r,-5]])
v=s.Matrix([-r/2,1,r/5]);w=s.Matrix([1,2,2*r/5]);
q=s.Matrix([v[1]*v[2],-2*v[0]*v[2],v[0]*v[1]])
Mp=s.diff(M,r)
assert all(s.simplify(c.subs(r,tau))==0 for c in M*v)
assert all(s.simplify(c.subs(r,tau))==0 for c in M.T*w)
inner=s.factor((w.T*v)[0].subs(r,tau))
a=s.simplify(((w.T*q)[0]/(w.T*v)[0]).subs(r,tau))
b=s.simplify(((w.T*Mp*v)[0]/(w.T*v)[0]).subs(r,tau))
assert inner>0 and a>0 and b<0
print('negative transcritical tau:',s.N(tau,18),'; a:',s.N(a,12),'; b:',s.N(b,12))
print('All exact-rational/sturm/subresultant checks passed.')
