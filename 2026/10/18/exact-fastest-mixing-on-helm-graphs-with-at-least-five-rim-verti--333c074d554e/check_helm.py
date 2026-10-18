"""Exact finite-bound checks and independent floating matrix-spectrum sanity checks.
Run: python check_helm.py. The all-order conclusion relies on the written proof.
"""
from fractions import Fraction as F
from math import factorial, cos, pi, sqrt

class Interval:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=I(o);return Interval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-I(o))
    def __rsub__(self,o):return I(o)-self
    def __mul__(self,o):
        o=I(o)
        terms=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return Interval(min(terms),max(terms))
    __rmul__=__mul__
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        v=Interval(1)
        for _ in range(k):v=v*self
        return v

def I(x):return x if isinstance(x,Interval) else Interval(x)

def arctan_interval_reciprocal(q,terms=25):
    total=F(0)
    for j in range(terms): total+= F((-1)**j,(2*j+1)*q**(2*j+1))
    delta=F(1,(2*terms+1)*q**(2*terms+1))
    return Interval(total-delta,total+delta)

pi_bounds=16*arctan_interval_reciprocal(5)-4*arctan_interval_reciprocal(239)
assert pi_bounds.lo>F(314159,100000) and pi_bounds.hi<F(314160,100000)

# For 0<x<=2*pi/5<1.26, the alternating cosine series brackets cos(x).
def cos_series(x,terms):
    return sum(((-1)**j)*x**(2*j)/factorial(2*j) for j in range(terms+1))

rough={5:(F(69,100),F(70,100)),6:(F(1,2),F(1,2)),
       7:(F(376,1000),F(377,1000)),
       8:(F(292,1000),F(294,1000)),
       9:(F(233,1000),F(235,1000))}
for n,(low,high) in rough.items():
    a=F(1,n)
    theta_lo=2*pi_bounds.lo/n
    theta_hi=2*pi_bounds.hi/n
    s_lo=1-cos_series(theta_lo,6)
    s_hi=1-cos_series(theta_hi,7)
    assert (low<=s_lo<=s_hi<=high) or (n==6 and s_lo<F(1,2)<s_hi),(n,float(s_lo),float(s_hi))
    s=Interval(low,high)
    K=a+s*(1-a)
    def P(c):return s*(s*s+4)*c*c -2*K*s*s*c +K*K*(s-1)
    assert P(a).hi<0,(n,'lower')
    assert P(F(1,2)).lo>0,(n,'upper')
    print('exact finite enclosure n=',n, 'P(a)<0<P(1/2)')

try:
    import numpy as np
    from numpy.linalg import eigvalsh
    for n in range(5,111):
        s=1-cos(2*pi/n);u=sqrt(s);a=1/n;K=a+s*(1-a)
        c=K*(1+u)/(u*(s+2*u+2));b=(1-a-c)/2
        t=1-K/(s+2*u+2)
        assert a>0 and b>0 and a<c<0.5
        P=np.zeros((2*n+1,2*n+1))
        # Hub 0; rim 1...n; leaves n+1...2n
        for j in range(n):
            v=j+1;w=(j+1)%n+1;leaf=n+1+j
            for x,y,p in [(0,v,a),(v,w,b),(v,leaf,c)]:
                P[x,y]+=p;P[y,x]+=p
        for i in range(2*n+1):P[i,i]=1-P[i].sum()
        assert P.min()>=-1e-12
        spectrum=eigvalsh(P)
        sl=max(abs(spectrum[0]),abs(spectrum[-2]))
        assert abs(sl-t)<2e-9,(n,sl,t)
    print('106 full-matrix spectral sanity tests passed')
except ImportError:
    print('NumPy unavailable: exact finite bounds passed; numerical sanity tests skipped')
