"""Independent finite-sample geometry and exact Dirichlet-moment checks.

Python 3 standard library only. The asymptotic theorem follows from the
mathematical argument in RESULT.md; these checks independently verify
constants, identities and high-order numerical consistency.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import cos, sin, pi, hypot, factorial
from random import Random


def rise(n, k):
    v = 1
    for j in range(k):
        v *= n + j
    return v


def cov_dirichlet(n, k, l):
    """Covariance of sums of kth and lth powers of Dirichlet(1,...,1) gaps."""
    return (Fraction(n * (factorial(k+l) + (n-1)*factorial(k)*factorial(l)), rise(n,k+l))
            - Fraction(n*n*factorial(k)*factorial(l), rise(n,k)*rise(n,l)))


def influence_cov(k, l):
    return factorial(k+l) - (1+k*l)*factorial(k)*factorial(l)

assert influence_cov(3,3) == 360
assert influence_cov(3,5) == 28800
assert influence_cov(5,5) == 3254400
vper=Fraction(360,24**2)*2**6
varea=Fraction(360,12**2)*2**6
beta_pi2=Fraction(-24,320)*4*Fraction(28800,360)
residual_pi10=Fraction(2**10,320**2)*(3254400-Fraction(28800**2,360))
corr_pi4=residual_pi10/(2*varea)
assert (vper,varea,beta_pi2,residual_pi10,corr_pi4)==(40,160,-24,9504,Fraction(297,10))
print('EXACT_FACTORIAL_INFLUENCE_MOMENTS_AND_CONSTANTS_OK')

rng = Random(1472007)
for n in [3,4,7,13,25]:
    for _ in range(60):
        angles = sorted(rng.random()*2*pi for j in range(n))
        gaps = [angles[(i+1)%n] - angles[i] if i<n-1 else angles[0]+2*pi-angles[-1] for i in range(n)]
        vertices = [(cos(t),sin(t)) for t in angles]
        perimeter = sum(hypot(vertices[(i+1)%n][0]-vertices[i][0],
                              vertices[(i+1)%n][1]-vertices[i][1]) for i in range(n))
        area = sum(vertices[i][0]*vertices[(i+1)%n][1]-vertices[(i+1)%n][0]*vertices[i][1]
                   for i in range(n))/2
        pg = 2*sum(sin(g/2) for g in gaps)
        ag = sum(sin(g) for g in gaps)/2
        assert abs(pg-perimeter)<2e-12 and abs(ag-area)<2e-12
print('INDEPENDENT_CARTESIAN_SHOELACE_AND_GAP_GEOMETRY_OK')

# Validate the explicit mixed Dirichlet covariance against an independent
# binomial/factorial asymptotic calculation, without relying on symbolic packages.
for k,l in [(3,3),(3,5),(5,5)]:
    for n in [5000,20000]:
        scaled = float(cov_dirichlet(n,k,l))*n**(k+l-1)
        expected = influence_cov(k,l)
        assert abs(scaled/expected - 1) < 0.012
print('EXACT_DIRICHLET_MIXED_COVARIANCES_MATCH_ASYMPTOTICS_OK')

PI_STRING = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
with localcontext() as ctx:
    ctx.prec=85
    p = Decimal(PI_STRING)
    # Taylor coefficients for perimeter and unsigned area of an inscribed polygon.
    powers=(3,5,7,9,11)
    pc={k:Fraction(2*(-1)**((k-1)//2),2**k*factorial(k)) for k in powers}
    ac={k:Fraction((-1)**((k-1)//2),2*factorial(k)) for k in powers}
    def dd(fr):
        return Decimal(fr.numerator)/Decimal(fr.denominator)
    def covariance(n,c1,c2):
        return sum((dd(c1[k]*c2[l]*cov_dirichlet(n,k,l))*(2*p)**(k+l)
                    for k in powers for l in powers),Decimal(0))
    for n in [1000,10000]:
        vp=covariance(n,pc,pc); va=covariance(n,ac,ac); ca=covariance(n,ac,pc)
        beta=ca/vp; residual=va-ca*ca/vp; corr=ca/(vp*va).sqrt()
        beta_ratio=(Decimal(2)-beta)*n*n/(24*p*p)
        residual_ratio=residual*n**9/(9504*p**10)
        correlation_ratio=(Decimal(1)-corr)*n**4/(dd(Fraction(297,10))*p**4)
        assert abs(beta_ratio-1)<Decimal('0.035')
        assert abs(residual_ratio-1)<Decimal('0.07')
        assert abs(correlation_ratio-1)<Decimal('0.05')
        print('TAYLOR_DIRICHLET_FINITE_N_CONVERGENCE_OK',n,
              'slope',round(float(beta_ratio),8),'residual',round(float(residual_ratio),8),
              'correlation',round(float(correlation_ratio),8))
print('ALL_CYCLIC_POLYGON_LINEAR_PREDICTION_CHECKS_OK')
