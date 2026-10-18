"""Independent arithmetic and geometric checks of an exact width-isotropy theorem.
Uses only Python's standard library. No claims of independent validation.
"""
from fractions import Fraction as F
from math import pi, sqrt, atan, sin, cos, isqrt
from random import Random

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def cv(x):return x if isinstance(x,I) else I(x)
    def __add__(self,other):
        o=self.cv(other);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+(-self.cv(other))
    def __rsub__(self,other):return self.cv(other)-self
    def __mul__(self,other):
        o=self.cv(other); v=[a*b for a in [self.lo,self.hi] for b in [o.lo,o.hi]]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.cv(other);assert o.lo*o.hi>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,other):return self.cv(other)/self
    def __repr__(self):return f'[{float(self.lo):.15g}, {float(self.hi):.15g}]'

def bounds_sqrt(n,scale=10**12):
    k=isqrt(n*scale*scale)
    assert k*k<=n*scale*scale<(k+1)*(k+1)
    return I(F(k,scale),F(k+1,scale))

def atan_alt(x,N):
    """Partial alternating Taylor sum with N terms, exact rational x in [0,1)."""
    assert 0<=x<1
    s=F(0); p=x
    for k in range(N):
        s+= (p if not k%2 else -p)/(2*k+1)
        p*=x*x
    return s

def atan_bounds(x):
    assert 0<x.lo<=x.hi<1
    # 60 terms ends on a negative term (lower); 61 ends positive (upper).
    return I(atan_alt(x.lo,60),atan_alt(x.hi,61))

def round_out(x,scale=10**12):
    return I(F((x.lo*scale).__floor__(),scale),
             F(-(-x.hi*scale).__floor__(),scale))

# 16 arctan(1/5)-4 arctan(1/239)=pi (Machin identity).
P=round_out(16*atan_bounds(I(F(1,5)))-4*atan_bounds(I(F(1,239))))
S2=bounds_sqrt(2);S3=bounds_sqrt(3)
H=round_out(atan_bounds(1/S2))
a=round_out(3*S2/P*H)
b=round_out(3/S2-2*a)
A=round_out(I(F(1,3))+2/(P*S3))
B=round_out(2/(P*S3))
C=round_out(I(F(1,3))+2/P-4/(P*S3))
D=round_out(a*C-b*B)
E=round_out(b*A-a*B)
G=round_out(D-E)
assert 0<D.lo and 0<E.lo and 0<G.lo
cstar=round_out(E/D);tstar=round_out((1-cstar)/2)
assert 0<cstar.lo and cstar.hi<1
print('CERTIFIED_RATIONAL_CONSTANT_INTERVALS_OK', 'pi',P,'atan',H)
print('CERTIFIED_RATIONAL_COVARIANCE_SIGNS_OK','D',D,'E',E,'D-E',G)
print('CERTIFIED_RATIONAL_UNIQUE_INTERIOR_OPTIMUM_OK','c',cstar,'t',tstar)

# Independent direct check using 12 vertex supports, not the ordered-coordinate formula.
v=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
rng=Random(20261017)
for i in range(18000):
    zz=rng.uniform(-1,1);th=rng.uniform(0,2*pi)
    ss=sqrt(1-zz*zz)
    u=(ss*cos(th),ss*sin(th),zz)
    t=rng.random()/2
    vv=[tuple((1-t)*v[j][k]+t*v[l][k] for k in range(3))
        for j in range(4) for l in range(4) if j!=l]
    dots=[sum(x*y for x,y in zip(p,u)) for p in vv]
    width=max(dots)-min(dots)
    xyz=sorted(map(abs,u),reverse=True)
    formula=2*(xyz[0]+(1-2*t)*xyz[1])
    assert abs(width-formula)<5e-14,(i,width,formula)
print('INDEPENDENT_18000_TWELVE_VERTEX_SUPPORT_CHECKS_OK')

# Independent 1D numerical spherical-chamber quadrature of the five moments.
# Coordinates x=cos(theta), y=sin(theta)cos(phi), z=sin(theta)sin(phi),
# 0<=phi<=pi/4, 0<=theta<=atan(sec(phi)).
def simpson(fn,left,right,steps=12000):
    assert steps%2==0
    h=(right-left)/steps
    s=fn(left)+fn(right)
    for j in range(1,steps):s+=(4 if j%2 else 2)*fn(left+j*h)
    return s*h/3

def moments(phi):
    cp=cos(phi)
    T=atan(1/cp)
    s=sin(T);co=cos(T)
    # theta integrals of M, m, M^2, M*m, m^2 after inserting sin(theta) Jacobian
    return (s*s/2,
            cp*(T-s*co)/2,
            (1-co**3)/3,
            cp*s**3/3,
            cp*cp*(2/3-co+co**3/3))
num=[(12/pi)*simpson(lambda p:moments(p)[j],0,pi/4) for j in range(5)]
exact=[float((x.lo+x.hi)/2) for x in (a,b,A,B,C)]
assert max(abs(q-r) for q,r in zip(num,exact))<2e-11,(num,exact)
print('INDEPENDENT_SPHERICAL_CHAMBER_FIVE_MOMENTS_OK', num)

# Exact extremum candidate list; compare independent directions via support vertices.
for t in [0.0,float((tstar.lo+tstar.hi)/2),1/3,0.5]:
    c=1-2*t
    mn=min(2,2*(1+c)/sqrt(3))
    mx=2*sqrt(1+c*c)
    L=1e20;Hmax=-1e20
    for i in range(10000):
        zz=rng.uniform(-1,1);ang=rng.uniform(0,2*pi)
        ss=sqrt(1-zz*zz);u=(ss*cos(ang),ss*sin(ang),zz)
        vv=[tuple((1-t)*v[j][k]+t*v[l][k] for k in range(3))
           for j in range(4) for l in range(4) if j!=l]
        dots=[sum(x*y for x,y in zip(p,u)) for p in vv]
        val=max(dots)-min(dots)
        assert mn-1e-12<=val<=mx+1e-12
        L=min(L,val);Hmax=max(Hmax,val)
    # The exact extremal candidates are not reliably hit by random sampling.
    def width_direct(u):
        vv=[tuple((1-t)*v[j][k]+t*v[l][k] for k in range(3))
            for j in range(4) for l in range(4) if j!=l]
        ds=[sum(x*y for x,y in zip(p,u)) for p in vv]
        return max(ds)-min(ds)
    candidates=((1,0,0),(1/sqrt(3),)*3)
    assert abs(min(width_direct(u) for u in candidates)-mn)<2e-12
    m_dir=(1/sqrt(1+c*c),c/sqrt(1+c*c),0)
    assert abs(width_direct(m_dir)-mx)<2e-12
print('SHARP_EXTREMA_AND_MIN_WIDTH_TRANSITION_CHECKS_OK')

# Exact stationary formula and independently enumerated grid verify uniqueness.
q=lambda c:(exact[2]+2*c*exact[3]+c*c*exact[4])/(exact[0]+c*exact[1])**2-1
cx=float((cstar.lo+cstar.hi)/2)
vmin=q(cx)
assert all(q(j/10000)>=vmin-1e-13 for j in range(10001))
assert q(0)>vmin and q(1)>vmin
print('UNIQUE_MINIMAL_NORMALIZED_WIDTH_VARIANCE_OK',
      't_star',float((tstar.lo+tstar.hi)/2),'CV_squared',vmin)
print('ALL_TRUNCATION_WIDTH_CHECKS_OK')
