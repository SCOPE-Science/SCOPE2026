"""Reproducible numerical and exact checks for local two-point distance laws of orthotopes.
All assertions are checks of a separate analytic proof, not substitutes for it.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
from numpy.polynomial import Polynomial
from fractions import Fraction
from itertools import combinations


def elementary(values, k):
    if k == 0:
        return 1.
    return sum(math.prod(c) for c in combinations(values, k))


def coeffs(sides):
    d=len(sides);V=math.prod(sides);rec=[1/x for x in sides]
    return np.array([(-1)**k*math.pi**((d-k)/2)/gamma(1+(d+k)/2)*elementary(rec,k)/V for k in range(d+1)])


def poly_prob(sides,r):
    return sum(c*r**(len(sides)+k) for k,c in enumerate(coeffs(sides)))


def invert_from_first_d(cs,d):
    assert len(cs)==d
    nu=math.pi**(d/2)/gamma(1+d/2)
    V=nu/cs[0]
    e=[1.]
    for k in range(1,d):
        ck=math.pi**((d-k)/2)/gamma(1+(d+k)/2)
        e.append((-1)**k*cs[k]*V/ck)
    e.append(1/V)
    pp=np.array([(-1)**k*e[k] for k in range(d+1)])
    roots=np.roots(pp)
    assert max(abs(roots.imag))<2.e-3,(d,roots)
    return sorted(1/roots.real)


def planar_exact_numeric(a,b,r):
    # Independent one-dimensional polar-cap integration of the planar triangular-difference density.
    m=min(a,r)
    def integrand(x):
        ymax=min(b,math.sqrt(max(0.,r*r-x*x)))
        return (1-x/a)*(ymax-ymax*ymax/(2*b))
    split=math.sqrt(max(0.,r*r-b*b)) if r>b else 0.
    value=quad(integrand,0.,m,points=[split] if 0<split<m else None,epsabs=1.e-12)[0]
    return 4*value/(a*b)


def correction_d3(a,b,c,r):
    # Exact transverse disk moments integrated independently over the newly exposed caps.
    assert a<min(b,c) and a<r<min(b,c,math.sqrt(2)*a)
    V=a*b*c
    def integrand(x):
        R=math.sqrt(max(0.,r*r-x*x))
        transverse=math.pi*R**2-(4/3)*(1/b+1/c)*R**3+R**4/(2*b*c)
        return (x/a-1)*transverse
    return 2*quad(integrand,a,r,epsabs=1.e-14)[0]/V


def cusp_const(sides):
    d=len(sides);a=min(sides);m=sum(abs(x-a)<1.e-12 for x in sides)
    unit=math.pi**((d-1)/2)/gamma(1+(d-1)/2)
    return 8*m*unit*(2*a)**((d-1)/2)/(a*math.prod(sides)*(d+1)*(d+3))

# Symbolically nontrivial symmetric-polynomial / reciprocal-root cases, including equal sides.
for sides in [[1.,2.],[1.,2.,3.],[1.,1.,2.],[1.,1.4,2.2,3.3], [1.,1.,1.,1.], [1.,1.4,2.,3.2,4.1]]:
    got=invert_from_first_d(coeffs(sides)[:-1],len(sides))
    assert np.allclose(got, sorted(sides), atol=3.e-4, rtol=3.e-4),(sides,got)

# Independent exact-density quadratures of two-dimensional boxes.
for a,b in [(1.,1.),(1.,2.),(2.,3.),(.7,2.5)]:
    for f in (.2,.55,.8,.95):
        r=f*min(a,b)
        assert abs(planar_exact_numeric(a,b,r)-poly_prob([a,b],r))<2.e-11,(a,b,r)

# The signed first non-polynomial departure at the shortest side and the sharp exponent.
for a,b in [(1.,2.),(1.,1.),(.8,2.3)]:
    K=cusp_const([a,b])
    for delta in (.05,.025,.0125,.00625):
        r=a+delta
        actual=planar_exact_numeric(a,b,r)
        diff=actual-poly_prob([a,b],r)
        ratio=diff/(K*delta**2.5)
        assert 0.69<ratio<1.08,(a,b,delta,ratio)
for a,b,c in [(1.,1.5,2.),(.8,1.7,2.5)]:
    K=cusp_const([a,b,c])
    for delta in (.04,.02,.01,.005):
        ratio=correction_d3(a,b,c,a+delta)/(K*delta**3)
        assert .75<ratio<1.08,(a,b,c,delta,ratio)

# Independent high-dimensional cap integration with repeated shortest edges.
def generic_correction(sides, delta):
    d=len(sides);a=min(sides);r=a+delta
    assert r < min(math.sqrt(2)*a, min([x for x in sides if x>a] or [10**9]))
    V=math.prod(sides)
    result=0.
    for i,ai in enumerate(sides):
        if ai!=a:continue
        others=[s for j,s in enumerate(sides) if j!=i]
        p=d-1
        def transverse(R):
            return sum((-1)**k*math.pi**((p-k)/2)/gamma(1+(p+k)/2)*elementary([1/z for z in others],k)*R**(p+k) for k in range(p+1))
        result+=2*quad(lambda x: (x/a-1)*transverse(math.sqrt(max(0,r*r-x*x))),a,r,epsabs=1.e-15)[0]/V
    return result

for sides in ([1.,1.,2.],[1.,1.,1.,2.],[1.,1.5,2.,3.]):
    K=cusp_const(sides)
    for delta in (.04,.02,.01,.005):
        v=generic_correction(sides,delta)
        ratio=v/(K*delta**((len(sides)+3)/2))
        assert .7<ratio<1.08,(sides,delta,ratio)

# Independent Monte Carlo comparison in dimensions 3 and 4.
rng=np.random.default_rng(20261016)
for sides,r in [([1.,1.5,2.],.7),([1.,1.,2.],.85),([1.,1.5,2.,2.5],.9)]:
    sides=np.array(sides)
    n=700_000
    x=rng.random((n,len(sides)))*sides
    y=rng.random((n,len(sides)))*sides
    empirical=np.mean(np.sum((x-y)**2,axis=1)<r*r)
    truth=poly_prob(sides,r)
    std=math.sqrt(truth*(1-truth)/n)
    assert abs(empirical-truth)<6*std+0.0005,(sides,r,empirical,truth,std)

print('ORTHOTOPE_LOCAL_DISTANCE_OK root_cases=6 quadrature_cases=16 cusp_2d_cases=12 cusp_3d_cases=8 cusp_nd_cases=12 simulations=3')
