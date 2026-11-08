#!/usr/bin/env python3
"""Exact rational interval certificates for three rootfinding maps on a quartic."""
from fractions import Fraction as F

class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi
    @staticmethod
    def of(x): return x if isinstance(x, I) else I(x)
    def __add__(self, rhs):
        rhs=I.of(rhs)
        return I(self.lo+rhs.lo,self.hi+rhs.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, rhs): return self + (-I.of(rhs))
    def __rsub__(self, lhs): return I.of(lhs) + (-self)
    def __mul__(self, rhs):
        rhs=I.of(rhs); vals=[a*b for a in (self.lo,self.hi) for b in (rhs.lo,rhs.hi)]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self, rhs):
        rhs=I.of(rhs)
        assert rhs.lo>0 or rhs.hi<0
        return self*I(1/rhs.hi,1/rhs.lo)
    def __rtruediv__(self,lhs): return I.of(lhs)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0:
            if self.lo<=0<=self.hi:return I(0,max(abs(self.lo),abs(self.hi))**n)
            return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
        return I(self.lo**n,self.hi**n)
    def absmax(self):return max(abs(self.lo),abs(self.hi))
    def contains_zero(self):return self.lo<=0<=self.hi

def poly(t,cs):
    z=I(0)
    for c in reversed(cs):z=z*t+c
    return z
p=[33,-33,0,-576,395]
u=[-33,0,-1728,1580]
v=[0,-3456,4740]
w=[-3456,9480]

def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def polysub(a,b):
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def polydiff(a):
    return [i*a[i] for i in range(1,len(a))]

# Verify every explicitly used derivative polynomial independently from the coefficients.
assert u==polydiff(p) and v==polydiff(u) and w==polydiff(v)
rs=polysub([3*x for x in polymul(v,v)],polymul(u,w))
assert rs==[-114048,312840,29859840,-76446720,52424400]


def h(t):
    a,b,c=poly(t,p),poly(t,u),poly(t,v)
    return t-(2*a*b)/(2*b**2-a*c)
def s(t):
    a,b,c=poly(t,p),poly(t,u),poly(t,v)
    return t-a/b-(a*a*c)/(2*b**3)
def hd(t):
    a,b,c,d=poly(t,p),poly(t,u),poly(t,v),poly(t,w)
    return a*a*(3*c*c-2*b*d)/(2*b*b-a*c)**2
def sd(t):
    a,b,c,d=poly(t,p),poly(t,u),poly(t,v),poly(t,w)
    return a*a*poly(t,[-114048,312840,29859840,-76446720,52424400])/(2*b**4)

def mid(c,r):return I(c-r,c+r)

# Floquet-cycle certificates: in the exact transition order.
HC=[F(-995631,10000000),F(-51938703,100000000)]
HR=[F(1,10000),F(1,50000)]
HB=[F(1,10),F(3,2)]
SC=[F(-691524324611229810,10**18), F(-347921163893610440,10**18),F(61148311552932509,10**18)]
SR=[F(1,10**6),F(1,10**6),F(3,10**6)]
SB=[F(9,10),F(12,5),F(1,20)]

def check(name,func,deriv,centers,radii,bounds,center_tol):
    print(name)
    assert len(centers)==len(radii)==len(bounds)
    Q=len(centers); prod=F(1)
    for k in range(Q):
        J=mid(centers[k],radii[k]);L=bounds[k];prod*=L
        assert not poly(J,p).contains_zero(), (name,'non-root',k)
        b=poly(J,u)
        if name=='Schroeder':assert not b.contains_zero(),(name,'pole',k)
        else:assert not (2*b**2-poly(J,p)*poly(J,v)).contains_zero(),(name,'pole',k)
        ddmax=F(0)
        segments=64
        for jseg in range(segments):
            left=J.lo+(J.hi-J.lo)*jseg/segments
            right=J.lo+(J.hi-J.lo)*(jseg+1)/segments
            dd=deriv(I(left,right))
            ddmax=max(ddmax,dd.absmax())
        assert ddmax<L,(name,'deriv',k,float(ddmax),float(L))
        fc=func(I(centers[k]));j=(k+1)%Q
        center_deviation=max(abs(fc.lo-centers[j]),abs(fc.hi-centers[j]))
        assert center_deviation<center_tol, (name,"center",k)
        assert center_deviation+L*radii[k]<radii[j], (name,'mapping',k,float(center_deviation+L*radii[k]),float(radii[j]))
        print(f'  map {k+1} to {j+1}: |deriv| < {L}, center error < {float(center_deviation):.12g}, margin > {float(radii[j] - center_deviation-L*radii[k]):.12g}')
    assert prod < 1
    print('  return contraction bound',prod)

def squarefree_test():
    def rem(a,b):
        a=[F(x) for x in a];b=[F(x) for x in b]
        while len(a)>=len(b) and any(a):
            k=len(a)-len(b); factor=a[-1]/b[-1]
            for j in range(len(b)):a[j+k]-=factor*b[j]
            while a and a[-1]==0:a.pop()
        return a
    a=p[:];b=u[:]
    while b:a,b=b,rem(a,b)
    assert len(a)==1 and a[0]!=0, 'polynomial must have four simple roots'

if __name__=='__main__':
    squarefree_test()
    check('Halley',h,hd,HC,HR,HB,F(1,10**8))
    check('Schroeder',s,sd,SC,SR,SB,F(1,10**17))
    # Check the source's Newton two-cycle; nonzero values and a vanishing second derivative.
    assert poly(I(0),p).lo==33 and poly(I(0),u).lo==-33
    assert poly(I(1),p).lo==poly(I(1),u).lo==-181
    assert poly(I(0),v).lo==0
    print('Newton: exact cycle 0 -> 1 -> 0, superattracting')
    print('VERIFY_OK')
