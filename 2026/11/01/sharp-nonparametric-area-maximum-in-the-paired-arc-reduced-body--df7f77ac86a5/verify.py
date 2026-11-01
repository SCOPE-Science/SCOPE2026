"""Standalone checks for the stated exact area extremum.

The universal claims are proved in RESULT.md. This script certifies the
numerical area interval by rational arithmetic and independently checks
several geometric specializations by boundary polygonization.
"""
from fractions import Fraction as F
from math import isqrt, sin, cos, asin, sqrt, pi

SCALE = 10**24

def sqrt_bracket(x):
    assert x >= 0
    v = (x.numerator * SCALE * SCALE) // x.denominator
    q = isqrt(v)
    return F(q, SCALE), F(q + 1, SCALE)

def asin_bracket(x, terms=140):
    """Rational interval for arcsin(x), 0 < x < 1.
    All series coefficients positive and <=1, so the geometric tail is valid.
    """
    assert 0 < x < 1
    coef = F(1); power = x; total = F(0)
    for k in range(terms):
        total += coef * power
        coef *= F((2*k+1)**2, 2*(k+1)*(2*k+3))
        power *= x*x
    return total, total + power / (1-x*x)

root17_lo, root17_hi = sqrt_bracket(F(17))
tlo, thi = (1+root17_lo)/8, (1+root17_hi)/8
slo = sqrt_bracket(tlo)[0]
shi = sqrt_bracket(thi)[1]
clo = sqrt_bracket(1-thi)[0]
chi = sqrt_bracket(1-tlo)[1]
alo_sin = 2*slo - 1/slo
ahi_sin = 2*shi - 1/shi
assert 0 < alo_sin < ahi_sin < 1
calo = sqrt_bracket(1-ahi_sin**2)[0]
cahi = sqrt_bracket(1-alo_sin**2)[1]
ml, _ = asin_bracket(slo)
_, mh = asin_bracket(shi)
al, _ = asin_bracket(alo_sin)
_, ah = asin_bracket(ahi_sin)
area_lo = ml-ah/2+clo*alo_sin-ahi_sin*cahi/2
area_hi = mh-al/2+chi*ahi_sin-alo_sin*calo/2
assert F(79457850, 10**8) < area_lo < area_hi < F(79457852, 10**8)

# For the candidate, the endpoint moment constraint is an algebraic identity:
# sin(a)=2 sin(m)-1/sin(m), and s^2=(1+sqrt(17))/8.
# The derivative numerator changes sign uniquely when 4t^2-t-1=0.
# Exact boundary area values of pi/4 are below 0.786;
# the rigorous area interval above separates the interior maximum.

s = sqrt((1+sqrt(17))/8)
m = asin(s)
a = asin(2*s-1/s)
Aexact = m-a/2 + cos(m)*sin(a)-sin(2*a)/4
assert 0.79457850 < Aexact < 0.79457852

def u(t): return (cos(t),sin(t))

def point_c(t,m,a):
    ell=m-a
    z=min(t,ell)
    c1=(.5*(cos(z)-1),.5*sin(z))
    if t>m+a:
        return (c1[0]+.5*(cos(t)-cos(m+a)),c1[1]+.5*(sin(t)-sin(m+a)))
    return c1

def boundary_area(m,a,steps=8000):
    A=[]; B=[]
    for i in range(steps+1):
        t=2*m*i/steps
        c=point_c(t,m,a); v=u(t)
        A.append((c[0]+v[0]/2,c[1]+v[1]/2))
        B.append((c[0]-v[0]/2,c[1]-v[1]/2))
    vertices=A+B
    return abs(sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1]
               -vertices[i][1]*vertices[(i+1)%len(vertices)][0]
               for i in range(len(vertices)))/2)

checks=0
for mm in [pi/4+.02, .85, .9375, m,1.1,1.35,pi/2-.02]:
    ss=sin(mm)
    aa=asin(-cos(2*mm)/ss)
    expected=mm-aa/2+cos(mm)*sin(aa)-sin(2*aa)/4
    observed=boundary_area(mm,aa,steps=5000)
    assert abs(observed-expected)<3e-7,(mm,observed,expected)
    checks+=1
    # Closure and precise thickness: all active pairs have width 1.
    endpoint=point_c(2*mm,mm,aa)
    target=((cos(2*mm)-1)*cos(mm)**2/(2*sin(mm)**2),
            sin(2*mm)*cos(mm)**2/(2*sin(mm)**2))
    assert abs(endpoint[0]-target[0])<1e-13
    assert abs(endpoint[1]-target[1])<1e-13
    checks+=2
    # Stationarity and first-variation complementarity by independent
    # quadrature of the convolution potential.
    alpha=cos(aa)-cos(mm)
    ngrid=1000
    for j in range(0,ngrid,137):
        x=-mm+2*mm*(j+.5)/ngrid
        # Composite Simpson on smooth subintervals split at every
        # curvature jump and at the absolute-value kink y=x.
        bounds=sorted([-mm,-aa,aa,mm,x])
        lhs=0.0
        for left,right in zip(bounds,bounds[1:]):
            if right-left<1e-15: continue
            N=200
            h=(right-left)/N
            def integrand(y):
                return (.5 if abs(y)>aa else 0.0)*sin(abs(x-y))
            # Interior endpoint values are taken as one-sided values
            # to avoid the discontinuity at +/-aa.
            mid=(left+right)/2
            active=.5 if abs(mid)>aa else 0.0
            vals=active*sin(abs(x-left))+active*sin(abs(x-right))
            for ii in range(1,N):
                vals+=(4 if ii%2 else 2)*active*sin(abs(x-left-ii*h))
            lhs+=h*vals/3
        rhs=alpha*cos(x)+(1-cos(abs(x)-aa) if abs(x)>aa else 0.)
        assert abs(lhs-rhs)<1e-5,(mm,x,lhs,rhs)
        checks+=1

print('VERIFY_OK',checks,'geometric and potential checks; rational area bounds',
      format(float(area_lo),'.12f'),format(float(area_hi),'.12f'))
