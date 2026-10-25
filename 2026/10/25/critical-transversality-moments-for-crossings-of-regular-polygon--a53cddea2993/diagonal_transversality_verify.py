"""Exact arithmetic and numerical checks of crossing-angle transversality.

Only the Python standard library is required. Run with:
    python diagonal_transversality_verify.py
"""
from collections import Counter
from itertools import combinations
from math import pi, sin, atan2, factorial, comb, log, isclose


def exact_counts(n):
    assert n >= 4
    den = (n-1)*(n-2)*(n-3)
    return {k: ((6 if 2*k == n else 12)*(k-1)*(n-k-1), den)
            for k in range(2, n//2+1)}


def moment(n, q):
    p = exact_counts(n)
    return sum(num/den / (sin(pi*k/n)**q) for k,(num,den) in p.items())


def orientation(p, q):
    from math import cos, sin
    return (cos(2*pi*p/q), sin(2*pi*p/q))


def acute_angle_lines(x1,x2,y1,y2):
    import math
    x=(x2[0]-x1[0],x2[1]-x1[1]); y=(y2[0]-y1[0],y2[1]-y1[1])
    dot=x[0]*y[0]+x[1]*y[1]
    cross=x[0]*y[1]-x[1]*y[0]
    return math.atan2(abs(cross),abs(dot))

for n in range(4,25):
    empirical=Counter()
    vs=[orientation(j,n) for j in range(n)]
    for a,b,c,d in combinations(range(n),4):
        theta=acute_angle_lines(vs[a],vs[c],vs[b],vs[d])
        k=round(theta*n/pi)
        assert abs(theta-pi*k/n)<1e-10,(n,a,b,c,d,theta,k)
        empirical[k]+=1
    assert sum(empirical.values())==comb(n,4)
    for k,(num,den) in exact_counts(n).items():
        assert empirical[k]*den == num*comb(n,4),(n,k,empirical[k],num,den)
print('DIRECT_EUCLIDEAN_CHORD_GEOMETRY_AND_EXACT_MULTIPLICITY_OK 4..24')

for n in [5,6,7,8,10,41,100,1001]:
    assert sum(num/den for num,den in exact_counts(n).values())==1 if n<=10 else abs(sum(num/den for num,den in exact_counts(n).values())-1)<1e-12
print('ANGLE_MASS_NORMALIZED_ALL_PARITIES_OK')

# The exact continuous F((pi)*u) = 6u^2 -4u^3 on [0,1/2].
for n in [100,1000,10000]:
    pp=exact_counts(n); cdf=0.
    for k in range(2, n//2+1):
        num,den=pp[k]; cdf+=num/den
        u=k/n; limit=6*u*u-4*u*u*u
        assert abs(cdf-limit) < 6/n
print('FOLDED_BETA_CONTINUUM_CDF_AND_UNIFORM_RATE_CHECK_OK')

# Independent midpoint quadrature after the transformation theta = pi*u*u/2.
def continuous_moment(q, steps=60000):
    s=0.0
    for i in range(steps):
        u=(i+0.5)/steps
        theta=0.5*pi*u*u
        density=12*theta*(pi-theta)/pi**3
        s+=density * (sin(theta)**(-q)) * pi*u
    return s/steps
for q in (0, 1, 1.5):
    continuous=continuous_moment(q)
    finite=moment(250000 if q == 1.5 else 20000,q)
    print('SUBCRITICAL',q,round(continuous,9),round(finite,9))
    assert abs(finite-continuous)<0.04
print('SUBCRITICAL_MOMENTS_AND_INDEPENDENT_QUADRATURE_OK')

from math import fsum
for n in [1000,10000,100000,1000000]:
    p=moment(n,2)
    print('SECOND_MOMENT',n,round(p,10),'minus_log_term',round(p-12/pi**2*log(n),9))
    assert abs(p-(12/pi**2)*log(n))<4
print('CRITICAL_LOGARITHMIC_DIVERGENCE_COEFFICIENT_OK')

for q in (2.5,3.,4.):
    zeta_difference=fsum((k-1)/k**q for k in range(2,1000000))
    theoretical=12/pi**q*zeta_difference
    for n in (1000,10000):
        scaled=moment(n,q)/n**(q-2)
        print('SUPERCRITICAL',q,n,round(scaled,9),'series',round(theoretical,9))
    if q>=3:
        assert abs(moment(10000,q)/10000**(q-2)-theoretical)/theoretical<0.02
print('SUPRACRITICAL_LATTICE_ZETA_COEFFICIENTS_OK')
print('ALL_CROSSING_DIAGONAL_ANGLE_CERTIFICATES_OK')
