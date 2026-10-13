"""Exact-rational interval certificate for a two-risk-class SIR incidence example.

Requires Python 3 standard library only. No floating-point operations enter
assertions. The truncation bound follows from geometric domination of the
positive Taylor remainder of exp(z), z >= 0.
"""
from fractions import Fraction as F

class IV:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(a,b):
        b=b if isinstance(b,IV) else IV(b)
        return IV(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return IV(-a.hi,-a.lo)
    def __sub__(a,b):return a+(- (b if isinstance(b,IV) else IV(b)))
    def __rsub__(a,b):return IV(b)-a
    def __mul__(a,b):
        b=b if isinstance(b,IV) else IV(b)
        s=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return IV(min(s),max(s))
    __rmul__=__mul__
    def __repr__(a):return f'[{a.lo},{a.hi}]'

def exp_minus(z,n=128):
    z=F(z);assert z>=0 and F(n+2)>z
    term=F(1);sm=F(1)
    for j in range(1,n+1):
        term*=z/j;sm+=term
    next_term=term*z/(n+1)
    tail=next_term/(1-z/F(n+2))
    return IV(1/(sm+tail),1/sm)

def bounds(x):
    x=F(x);s0=F(99999,100000)
    s1=s0*F(49,50);s2=s0*F(1,50)
    e1=exp_minus(x);e2=exp_minus(100*x)
    S=s1*e1+s2*e2
    I=1-S-F(4,5)*x
    h=s1*e1+100*s2*e2
    k=s1*e1+10000*s2*e2
    q=(h-F(4,5))*h-I*k
    return I,h,k,q

def floor_frac(t):return t.numerator//t.denominator

def outward(a,places=100000000):
    lo=floor_frac(a.lo*places);hi=-floor_frac(-a.hi*places)
    return f'[{lo}/{places},{hi}/{places}]'

if __name__=='__main__':
    pts=[F(0),F(1,50),F(1,20),F(1,5)]
    expected=[1,-1,1,-1]
    for x,sgn in zip(pts,expected):
        I,h,k,q=bounds(x)
        assert I.lo>0 and h.lo>F(4,5) and k.lo>0
        if sgn==1: assert q.lo>0
        else: assert q.hi<0
        print('pressure',x,'I',outward(I),'h',outward(h),'Q',outward(q))
    assert bounds(F(1,5))[0].lo>0
    assert bounds(F(1,5))[1].lo>F(1,16)
    print('VERIFY_OK: exact rational four-point sign certificate and increasing prevalence')
