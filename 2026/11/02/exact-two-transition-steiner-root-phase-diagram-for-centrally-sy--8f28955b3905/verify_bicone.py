"""Exact rational interval checks for a circular bicone Steiner-root transition theorem.

Only the mathematical identities/signs asserted below are certified here.
The continuum statements rely on the accompanying analytic proof.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import isqrt

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(hi) if hi is not None else F(lo)
        assert self.lo<=self.hi
    def __add__(self,other):
        other=other if isinstance(other,I) else I(other)
        return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+(-other if isinstance(other,I) else I(-other))
    def __rsub__(self,other): return I(other)-self
    def __mul__(self,other):
        other=other if isinstance(other,I) else I(other)
        a=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=other if isinstance(other,I) else I(other)
        assert other.lo>0
        return self * I(1/other.hi,1/other.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        res=I(1)
        for _ in range(n):res=res*self
        return res
    def sign(self):return -1 if self.hi<0 else 1 if self.lo>0 else 0
    def fmt(self):return f'[{float(self.lo):.17g}, {float(self.hi):.17g}]'

def atan_interval(z, n=100):
    """Alternating arctan Maclaurin: even partial sum is lower, odd upper."""
    assert 0<z<1
    terms=[(-1)**k*F(z)**(2*k+1)/F(2*k+1) for k in range(n+1)]
    sn=sum(terms[:n]); sn1=sn+terms[n]
    return I(min(sn,sn1),max(sn,sn1))

def sqrt_fraction_interval(q, scale=10**25):
    assert q>0
    f=isqrt(q.numerator *scale*scale//q.denominator)
    lo,hi=F(f,scale),F(f+1,scale)
    assert lo*lo <=q <hi*hi
    return I(lo,hi)

PI = 16*atan_interval(F(1,5),60)-4*atan_interval(F(1,239),60)
assert F(333,106)< PI.lo <= PI.hi < F(355,113)
assert PI.lo>3 and PI.hi<F(22,7)


def roots_discriminant(x):
    x=F(x)
    # A=x+atan(1/x); for x<1 use arctan(1/x)=pi/2-atan(x)
    if x==1:
        A=I(x)+PI/4
    elif x<1:
        A=I(x)+PI/2-atan_interval(x)
    else:
        A=I(x)+atan_interval(1/x)
    B=sqrt_fraction_interval(1+x*x)
    return (3*A**2*B**2+12*A*B*x-8*B**3-4*A**3*x-4*x*x)/3

expected={F(1,2):-1,F(3,4):1,F(1,1):1,F(5,4):-1,F(2,1):-1}
for x,sign in expected.items():
    D=roots_discriminant(x)
    assert D.sign()==sign, (x,D.fmt())
    print('aspect=',x,'disc=',D.fmt(),'sign=',sign)

# Limit at height/radius x -> 0+: Delta -> pi^2/4-8/3 < 0.
limit_small=PI**2/4-I(F(8,3))
assert limit_small.sign()==-1
print('delta_0=',limit_small.fmt())
# Limit x -> infinity: Delta/x^4 -> -1/3; follows from A/x,B/x -> 1.
# Positivity of A B - 2x/9: A>x and B>=1, so A B>x>2x/9.

# Independent exact symbolic check, if SymPy is installed: discriminant of normalized cubic.
try:
    import sympy as s
    t,A,B,x=s.symbols('t A B x')
    f=s.Rational(2,3)*t**3+A*t*t+B*t+x/3
    assert s.factor(3*s.discriminant(f,t) - (3*A*A*B*B+12*A*B*x-8*B**3-4*A**3*x-4*x*x))==0
    print('symbolic cubic discriminant: verified')
except ImportError:
    print('symbolic extension unavailable (exact interval checks completed)')
print('VERIFY_OK')

def sqrt_I(z):
    assert z.lo>0
    return I(sqrt_fraction_interval(z.lo).lo,sqrt_fraction_interval(z.hi).hi)

def transition_functions(x):
    x=F(x)
    if x==1:
        a=I(1)+PI/4
    elif x<1:
        a=I(x)+PI/2-atan_interval(x)
    else:
        a=I(x)+atan_interval(1/x)
    b=sqrt_fraction_interval(1+x*x)
    q=sqrt_I(a*a-2*b)
    G=a**3-3*a*b+2*x
    return G+q**3,G-q**3

checks=[(F(1,2),+1,-1),(F(3,5),+1,+1),
        (F(23,20),-1,-1),(F(6,5),-1,+1)]
for x,sig,expected_sign in checks:
    values=transition_functions(x)
    value=values[0] if sig==1 else values[1]
    print('aspect=',x,'transition=',sig,'value=',value.fmt())
    assert value.sign()==expected_sign
# Algebraic identity for derivatives: a'=v², b'=v, q' = v(av-1)/q.
# With q²=a²-2b, verify phi' = 1/2 + 3/2(v(a ± q)-1)².
try:
    import sympy as s
    a,b,q,v=s.symbols('a b q v',real=True)
    dG=3*a*a*v*v-3*b*v*v-3*a*v+2
    for eps in (-1,1):
        actual=dG+eps*3*q*v*(a*v-1)
        certificate=s.Rational(1,2)+s.Rational(3,2)*(v*(a+eps*q)-1)**2
        assert s.factor((actual-certificate).subs(b,(a*a-q*q)/2))==0
    print('monotonicity derivative identities: verified')
except ImportError:
    print('symbolic derivative extension unavailable; proof in RESULT.md')
print('TRANSITION_VERIFY_OK')
# At stationary points z_-=(-a-q)/2 and z_+=(-a+q)/2,
# f(z_-)=Phi_+/6 and f(z_+)=Phi_-/6 (under q²=a²-2b).
try:
    import sympy as s
    z,a,b,q,x=s.symbols('z a b q x',real=True)
    cubic=s.Rational(2,3)*z**3+a*z**2+b*z+x/3
    G=a**3-3*a*b+2*x
    for eps in (-1,1):
        stationary=(-a+eps*q)/2
        phi=G-eps*q**3
        assert s.factor((6*cubic.subs(z,stationary)-phi).subs(b,(a*a-q*q)/2))==0
    print('stationary-value identities: verified')
except ImportError:
    print('stationary-value symbolic extension unavailable; proof in RESULT.md')
print('FINAL_VERIFY_OK')
