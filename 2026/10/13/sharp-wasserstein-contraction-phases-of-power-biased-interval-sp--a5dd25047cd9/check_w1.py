"""Standalone finite cross-checks for an interval splitting Markov kernel.
Proof of the continuum theorem is analytical, not an exhaustive numerical test.
"""
from fractions import Fraction as Q
import math


def density_factors(x, p):
    d = x**p + (1-x)**p
    return x**(p-1)/d, (1-x)**(p-1)/d


def cdf(z, x, p):
    a,b=density_factors(x,p)
    return a*z if z<=x else 1-b*(1-z)


def w1_piecewise(x, y, p):
    # Integrate the absolute difference of the two CDFs exactly on each
    # interval of affine dependence in z (for rational input, rational result).
    k = sorted((0,x,y,1))
    total=0
    for lo,hi in zip(k,k[1:]):
        if lo==hi: continue
        d0=cdf(lo,x,p)-cdf(lo,y,p)
        d1=cdf(hi,x,p)-cdf(hi,y,p)
        if d0*d1>=0: area=(hi-lo)*(abs(d0)+abs(d1))/2
        else: area=(hi-lo)*(d0*d0+d1*d1)/(2*(abs(d0)+abs(d1)))
        total+=area
    return total


def local_slope(x,p):
    # Derived by differentiating the densities on either side of the state.
    d=x**p+(1-x)**p
    dp=p*(x**(p-1)-(1-x)**(p-1))
    da=((p-1)*x**(p-2)*d-x**(p-1)*dp)/(d*d)
    db=(-(p-1)*(1-x)**(p-2)*d-(1-x)**(p-1)*dp)/(d*d)
    return (x*x*abs(da)+(1-x)**2*abs(db))/2


def bound(p):
    if p==0:return Q(1,2)
    if p==1:return Q(0)
    if p>1:return max(Q(1,2),(p-1)/2)
    raise ValueError('infinite coefficient for 0<p<1')

checks=0
# Rational arithmetic verifies values, symmetry, bounds, and exact W1 from
# independent CDF integration (not replacing the universal proof).
for p in range(7):
    B=bound(Q(p))
    for ix in range(1,35):
        x=Q(ix,36)
        v=local_slope(x,p)
        assert v <= B
        assert v==local_slope(1-x,p)
        checks +=2
        for iy in range(ix+1,36):
            y=Q(iy,36)
            W=w1_piecewise(x,y,p)
            assert W>=0 and W<=B*(y-x)
            if p==0:assert W==(y-x)/2
            if p==1:assert W==0
            checks+=1

# Independent finite differences approximate the local CDF formula at
# noninteger parameters, including the singular near-boundary regime.
for p in (0.25,0.5,0.8,1.1,1.25,1.6,2.5,2.75,3.5,5.3):
    for x in (0.003,0.02,0.13,0.29,0.5,0.77):
        h=1e-7
        d=w1_piecewise(x,x+h,p)/h
        ell=local_slope(x,p)
        assert abs(d-ell)<2e-4*(1+ell), (p,x,d,ell)
        checks+=1

for p in (0.25,0.5,0.8):
    a=local_slope(1e-9,p)
    b=local_slope(1e-6,p)
    assert a>b*3,(p,a,b)
    checks+=1

print('CHECKED',checks,'finite exact-rational/numerical assertions')
