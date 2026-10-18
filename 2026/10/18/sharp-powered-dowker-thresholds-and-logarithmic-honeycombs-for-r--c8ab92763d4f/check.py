"""Exact rational-interval verification for polygonal weak log-Dowker inequalities.
No external dependencies. Run python check.py.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial

class I:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo); self.hi=Q(hi) if hi is not None else self.lo
        assert self.lo <= self.hi
    def __add__(self,o):
        o=interval(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-interval(o))
    def __mul__(self,o):
        o=interval(o)
        pts=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I(min(pts),max(pts))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=interval(o);assert not (o.lo<=0<=o.hi)
        return self*I(1/o.hi,1/o.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if self.lo>=0:return I(self.lo**n,self.hi**n)
        if self.hi<=0 and n%2==1:return I(self.lo**n,self.hi**n)
        raise ValueError('pow only for nonnegative intervals')
    def __repr__(self):return f'[{float(self.lo):.15g},{float(self.hi):.15g}]'

def interval(z):return z if isinstance(z,I) else I(z)

def atan_unit(d,N):
    z=Q(1,d)
    summ=sum(((-1)**j*z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    e=z**(2*N+1)/Q(2*N+1)
    return I(summ,summ+e) if N%2==0 else I(summ-e,summ)

PI=16*atan_unit(5,55)-4*atan_unit(239,12)
assert Q(31415,10000)<PI.lo and PI.hi<Q(31416,10000)

@lru_cache(maxsize=None)
def trigon(kind,t):
    """Bounds for sin(pi*t) and cos(pi*t), t rational in [0,1]."""
    t=Q(t); assert 0<=t<=1
    x=PI*I(t)
    y=(x.lo+x.hi)/2
    eps=(x.hi-x.lo)/2
    J=16
    if kind=='sin':
        s=sum(((-1)**j*y**(2*j+1)/Q(factorial(2*j+1)) for j in range(J)),Q(0))
        err=y**(2*J+1)/Q(factorial(2*J+1))+eps
        return I(max(Q(0),s-err),min(Q(1),s+err))
    if kind=='cos':
        s=sum(((-1)**j*y**(2*j)/Q(factorial(2*j)) for j in range(J)),Q(0))
        err=y**(2*J)/Q(factorial(2*J))+eps
        return I(max(Q(-1),s-err),min(Q(1),s+err))
    raise ValueError(kind)

def tan(t):return trigon('sin',Q(t))/trigon('cos',Q(t))

@lru_cache(maxsize=None)
def A(k,n):
    N=2*k
    if n>=N:return N*tan(Q(1,N))
    if n==3:
        q,r=divmod(N,3)
        if r==0:return 3*tan(Q(1,3))
        z=(3-r)*trigon('sin',Q(q,k))+r*trigon('sin',Q(q+1,k))
        return 2*z/(trigon('cos',Q(1,N))**2)
    q,r=divmod(N,n)
    return (n-r)*tan(Q(q,N))+r*tan(Q(q+1,N))

def lower_int(a,scale=10**16):return a.lo.numerator*scale//a.lo.denominator
def upper_int(a,scale=10**16):return -((-a.hi.numerator*scale)//a.hi.denominator)

def verify():
    all_checked=0;smallest_margin=1e99;closest=None
    for k in range(2,16):
        if k in (4,5,7):continue
        b=upper_int(A(k,6))
        for m in (3,4,5):
            for n in range(7,2*k+1):
                a=lower_int(A(k,m));c=lower_int(A(k,n))
                lhs=a**(n-6)*c**(6-m)
                rhs=b**(n-m)
                assert lhs>rhs,(k,m,n)
                all_checked+=1
                margin=float(lhs/rhs)-1
                if margin<smallest_margin:smallest_margin,closest=margin,(k,m,n)
    for k in (4,5,7):
        a,b,c=A(k,5),A(k,6),A(k,7)
        assert (a+c).lo<=(2*b).hi and (2*b).lo<=(a+c).hi
        assert a.lo>b.hi and b.lo>c.hi
    def disk(n):return n*tan(Q(1,n))
    L=disk(5)*disk(7)/(disk(6)**2)
    C=I(1)/(trigon('cos',Q(1,32))**4)
    assert L.lo>Q(51,50)
    assert C.hi<Q(51,50)
    print('PASS: finite strict inequalities:',all_checked)
    print('Closest finite (relative difference):',closest,smallest_margin)
    print('PASS: exceptional spacing k=4,5,7; source exact linear identities')
    print('PASS: disk ratio > 51/50 > sec(pi/32)^4')
    print('PASS: exact rational interval bounds, outward integer rounding')

if __name__=='__main__':verify()
