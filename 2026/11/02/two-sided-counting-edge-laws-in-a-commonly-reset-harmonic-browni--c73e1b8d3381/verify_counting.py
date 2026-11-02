"""Deterministic consistency checks for the two-sided counting-edge theorem.

Requires Python 3, SciPy. These tests support but do not replace the proof.
"""
import math
from scipy.integrate import quad
from scipy.special import erf, erfc, erfinv, gamma, ndtr
from scipy.stats import binom


def params(mu, D, r, a):
    A = a * math.sqrt(mu / (2.0 * D))
    theta = r / (2.0 * mu)
    p0 = erf(A)
    B = A * math.exp(-A*A) / math.sqrt(math.pi)
    sd = math.sqrt(p0*(1.0-p0))
    return A, theta, p0, B, sd


def q(y, A):
    if y >= 1.0:
        return 1.0
    return erf(A / math.sqrt(1.0-y))


def F(x, A, theta, p0):
    if x <= p0:
        return 0.0
    if x >= 1.0:
        return 1.0
    return (1.0 - (A / erfinv(x))**2)**theta


def finite_left(N, A, theta, p0, B, x=0.0):
    k = math.floor(N*p0 + x*math.sqrt(N))
    m = B * math.sqrt(N)
    def integrand(z):
        y = z / m
        prob = binom.cdf(k, N, q(y, A)) if y < 1 else 0.0
        return z**(theta-1.0) * prob
    val = quad(integrand, 0.0, min(m,100.0), epsabs=1e-9,
               limit=350)[0]
    return (theta/B**theta) * val / N**(theta/2.0)


def left_coefficient(A, theta, p0, B, x=0.0):
    sd = math.sqrt(p0*(1-p0))
    integrand = lambda z: z**(theta-1.0) * ndtr((x-z)/sd)
    val = quad(integrand, 0.0, max(25.0,abs(x)+15.0),
               epsabs=1e-10, limit=350)[0]
    return theta*val/B**theta


def all_inside(N, mu, D, r, a):
    A, theta, p0, B, sd = params(mu, D, r, a)
    def integrand(t):
        if t == 0.0:
            return r
        den = -math.expm1(-2.0*mu*t)
        outside = erfc(A/math.sqrt(den))
        return r*math.exp(-r*t + N*math.log1p(-outside))
    return quad(integrand, 0.0, max(12.0/r,20.0*a*a/D),
                epsabs=1e-12, limit=350)[0]


def run():
    checks = 0
    for mu, D, r, a in [(1.,1.,0.7,1.), (1.,1.,2.,1.),
                         (1.,1.,5.,1.), (2.,0.8,1.5,0.7)]:
        A, theta, p0, B, sd = params(mu,D,r,a)
        for y in (0.001,0.04,0.2,0.6,0.9):
            assert abs(F(q(y,A),A,theta,p0)-y**theta)<3e-11
            checks += 1
        for N in (1,3,8):
            probs=[]
            for k in range(N+1):
                fun=lambda y:theta*y**(theta-1)*binom.pmf(k,N,q(y,A))
                probs.append(quad(fun,0.,1.,epsabs=1e-10,limit=350)[0])
            assert abs(sum(probs)-1)<3e-10
            checks += 1
        for y in (1e-4,1e-5):
            assert abs((q(y,A)-p0)/(B*y)-1)<0.002
            checks += 1
        for x in (-0.35, 0., 0.5):
            assert left_coefficient(A,theta,p0,B,x)>0
            checks += 1
        central=left_coefficient(A,theta,p0,B)
        gamma_constant=(sd/B)**theta*(2**(theta/2-1))*gamma((theta+1)/2)/math.sqrt(math.pi)
        assert abs(central/gamma_constant-1)<3e-9
        checks += 1
        # The Gaussian-rounding limit converges more slowly for large theta.
        scaled=finite_left(100000,A,theta,p0,B)*100000**(theta/2)
        assert abs(scaled/central-1)<0.12
        checks += 1
        # Logarithmic all-inside asymptotic: convergence is intentionally slow.
        ratio_10000=all_inside(10000,mu,D,r,a)*math.log(10000)/(r*a*a/(4*D))
        ratio_1000000=all_inside(1000000,mu,D,r,a)*math.log(1000000)/(r*a*a/(4*D))
        assert abs(ratio_1000000-1)<abs(ratio_10000-1)
        assert 0.80 < ratio_1000000 < 1.25
        checks += 2
    print('PASS',checks,'deterministic quadrature and asymptotic-consistency assertions')

if __name__ == '__main__':
    run()
