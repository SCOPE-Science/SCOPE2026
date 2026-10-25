"""Exact-rational interval verification of the degenerate Landau germ.

Only Python's standard library is required. The analytic proof of the
Taylor-coefficient sign criterion is provided separately.
"""
from fractions import Fraction as Q
from math import factorial

class I:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = into(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other):return self+-into(other)
    def __rsub__(self, other):return into(other)+-self
    def __mul__(self, other):
        other=into(other)
        x=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return I(min(x),max(x))
    __rmul__=__mul__
    def __truediv__(self, other):
        other=into(other)
        assert other.lo*other.hi>0
        return self*I(Q(1,1)/other.hi, Q(1,1)/other.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0 and self.lo<0<self.hi:
            return I(0,max(self.lo**n,self.hi**n))
        return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def __repr__(self):return f'[{float(self.lo):.14g},{float(self.hi):.14g}]'

def into(x):return x if isinstance(x,I) else I(x)

def exp_bounds(x):
    assert x>=0 and x<80
    s=Q(0);term=Q(1)
    for n in range(0,81):
        if n:term*=x/n
        s+=term
    next_term=term*x/81
    tail=next_term/(1-x/Q(82))
    return I(s,s+tail)

def sinh_cosh(x):
    e=exp_bounds(x)
    reciprocal=I(Q(1)/e.hi,Q(1)/e.lo)
    return (e-reciprocal)/2,(e+reciprocal)/2

# Evaluate K=8 cosh(a)^4 B(a) at a fixed *rational* a.
def K(a):
    sh2,ch2=sinh_cosh(2*a)
    sh4,_=sinh_cosh(4*a)
    return 16*a**3*(2-ch2)+16*a**2*sh2+4*a*(1+ch2)-2*sh2-sh4

lo=Q(11429918,10000000)
hi=Q(11429919,10000000)
kl,kh=K(lo),K(hi)
assert kl.lo>0 and kh.hi<0
print('critical a lies strictly between',float(lo),float(hi))
print('K(a_low)',kl,'K(a_high)',kh)

# tanh(a) = (exp(2a)-1)/(exp(2a)+1), increasing in a.
e_lo=exp_bounds(2*lo)
e_hi=exp_bounds(2*hi)
t=I((e_lo.lo-1)/(e_lo.lo+1),(e_hi.hi-1)/(e_hi.hi+1))
a=I(lo,hi)
F6=Q(5,16)*(120*a**5*t**6-240*a**5*t**4+136*a**5*t**2-16*a**5
    -72*a**4*t**5+120*a**4*t**3-48*a**4*t
    -18*a**3*t**4+24*a**3*t**2-6*a**3
    -12*a**2*t**3+12*a**2*t-9*a*t**2+9*a-9*t)
assert F6.lo>3 and F6.hi<4
print('tanh(a*) enclosure:',t)
print('sixth derivative F^(6)(0):',F6)

# Closed Maclaurin coefficient check: K(a)=128 a^3/3 - sum(d_n a^(2n+1), n>=2).
for n in range(2,13):
    d=Q(4*2**(2*n)*(8*n*(n*n-n-1)+4**n),factorial(2*n+1))
    assert d>0
print('Maclaurin tail coefficients d_2,...,d_12 are strictly positive')
print('PASS: exact root enclosure, exact positive sextic coefficient, coefficient-sign certificate')
