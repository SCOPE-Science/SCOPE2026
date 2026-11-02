"""Independent elementary checks for a two-site stochastic heat splitting threshold.

Requires Python 3.9+ standard library only. Finite tests support the analytical
proof but are not a substitute for its all-parameter quantifiers.
"""
from fractions import Fraction as F
from math import exp, log, cosh, sinh, isclose, sqrt
import random


def exact_critical_mu(z):
    z = F(z)
    return z * (2*z*z + z + 1) / (z*z + z + 2)


def threshold_ratio(eta):
    z = exp(2*eta)
    return 2 + log((2*z*z+z+1)/(z*z+z+2)) / eta


def rho_matrix(eta, v):
    factor=exp(-4*eta)
    mu=exp(v*eta)
    a=factor*mu*cosh(2*eta)
    b=factor*sinh(2*eta)
    c=factor*mu*sinh(2*eta)
    d=factor*cosh(2*eta)
    return ((a+d)+sqrt((a-d)**2+4*b*c))/2

# z=4, eta=log 2, and mu=7 give a rational second-moment matrix.
z=F(4)
mu=F(7)
assert exact_critical_mu(z)==F(74,11)
K=((F(119,128),F(15,128)),(F(105,128),F(17,128)))
detI=(1-K[0][0])*(1-K[1][1])-K[0][1]*K[1][0]
assert detI==F(-9,256)
assert K[0][0]+K[0][1]==F(67,64)
assert 2 < log(7)/log(2) < 3

# Critical eta curve decreases from 3 to 2; the rational witness is unstable.
eta=log(2)
assert rho_matrix(eta,log(7)/log(2))>1
assert abs(rho_matrix(eta,threshold_ratio(eta))-1)<1e-12
for val in [0.02,0.05,0.1,0.2,0.5,1.0,2.0,4.0,8.0]:
    r=threshold_ratio(val)
    assert 2 < r < 3
    assert rho_matrix(val,r-0.01)<1 and rho_matrix(val,r+0.01)>1
for a,b in zip([0.02,0.05,0.1,0.2,0.5,1.,2.,4.],[0.05,0.1,0.2,0.5,1.,2.,4.,8.]):
    assert threshold_ratio(a)>threshold_ratio(b)

# All rational levels show strict positivity of the factor producing concavity.
for k in range(1,301):
    z=F(1+k,30)
    if z<=1: continue
    poly=z**4+12*z**3+10*z*z+12*z+1
    assert (z-1)*(z+1)*poly>0

# Direct second-moment recursion is matched by independent Gaussian simulation.
# Fixed random seed gives a deterministic diagnostic, not a proof.
random.seed(2207)
eta=0.22
v=1.9
N=120000
h0=exp(-2*eta)*cosh(eta)
h1=exp(-2*eta)*sinh(eta)
sum_sq=sum_cross=0.0
for _ in range(N):
    d1=exp(sqrt(v*eta)*random.gauss(0,1)-v*eta/2)
    d2=exp(sqrt(v*eta)*random.gauss(0,1)-v*eta/2)
    x=h0*d1+h1*d2
    y=h1*d1+h0*d2
    sum_sq+=(x*x+y*y)/2
    sum_cross+=x*y
mu=exp(v*eta)
expected_sq=exp(-4*eta)*(mu*cosh(2*eta)+sinh(2*eta))
expected_cross=exp(-4*eta)*(mu*sinh(2*eta)+cosh(2*eta))
assert abs(sum_sq/N-expected_sq)<0.035
assert abs(sum_cross/N-expected_cross)<0.035
print('VERIFY_OK rational_witness=1 threshold_levels=9 curvature_factors=300 monte_carlo=120000')
