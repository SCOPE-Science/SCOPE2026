#!/usr/bin/env python3
"""Verification for flat signed quadratic-chaos maximum asymptotics."""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import gammaln, kve
from scipy.stats import chi2, norm

# Symbolic Cramer-rate expansion for a flat spectrum with sign imbalance delta.
t, a, delta = sp.symbols('t a delta')
K = (-delta*t/sp.sqrt(2)
     -(1+delta)*sp.log(1-sp.sqrt(2)*t)/4
     -(1-delta)*sp.log(1+sp.sqrt(2)*t)/4)
c1,c2,c3,c4 = sp.symbols('c1 c2 c3 c4')
ts = c1*a+c2*a**2+c3*a**3+c4*a**4
eq = sp.series(sp.diff(K,t).subs(t,ts)-a,a,0,5).removeO().expand()
sol = sp.solve([sp.Eq(eq.coeff(a,i),0) for i in range(1,5)], [c1,c2,c3,c4], dict=True)[0]
ts = sp.expand(ts.subs(sol))
Ipoly = sp.series(a*ts-K.subs(t,ts),a,0,5).removeO().expand()
expected = a**2/sp.Integer(2)-sp.sqrt(2)*delta*a**3/sp.Integer(3)+(delta**2-sp.Rational(1,2))*a**4
assert sp.simplify(Ipoly-expected) == 0
print('rate_series =', expected, '+ O(a**5)')

# Critical Kolmogorov gap between two Gumbel laws shifted by shift>0.
def gumbel_gap(shift):
    return (1-math.exp(-shift))*math.exp(-shift/(math.exp(shift)-1))
print('D(4/(3*sqrt(8))) = %.15f' % gumbel_gap(4/(3*math.sqrt(8))))
print('D(2/8)           = %.15f' % gumbel_gap(2/8))

# Exact positive-flat maximum: Q=(chi2_R-R)/sqrt(2R).
def normal_extreme_center(L):
    b = norm.isf(math.exp(-L))  # p*P(Z>b)=1, with p=e^L
    return b, 1/b

def maxcdf_normal(L, y=0.0):
    p = math.exp(L)
    b,c = normal_extreme_center(L)
    x = b+c*y
    return math.exp(p*math.log1p(-norm.sf(x)))

def maxcdf_positive(L, R, y=0.0):
    p = math.exp(L)
    b,c = normal_extreme_center(L)
    x = b+c*y
    threshold = R+math.sqrt(2*R)*x
    return math.exp(p*math.log1p(-chi2.sf(threshold,R)))

print('\npositive-flat critical R=8*(log p)^3, y=0')
print('limit Q-max CDF = %.15f' % math.exp(-math.exp(4/(3*math.sqrt(8)))))
print('limit Z-max CDF = %.15f' % math.exp(-1))
for L in (6,10,20,30):
    R = int(8*L**3)
    print('L=%2d R=%7d Q=%.15f Z=%.15f' % (L,R,maxcdf_positive(L,R),maxcdf_normal(L)))

# Balanced spectrum exact density. With R=2m, Q=(chi2_m-chi2'_m)/(2*sqrt(m))
# equals (A-B)/sqrt(m), A,B iid Gamma(m/2,1).
def balanced_logpdf_q(x,m):
    u = abs(x)*math.sqrt(m)
    k = m/2.0
    nu = k-0.5
    if u == 0:
        raise ValueError('tail integration does not evaluate at zero')
    scaled_k = kve(nu,u)
    return (0.5*math.log(m)+(k-0.5)*math.log(u)+math.log(scaled_k)-u
            -(k-0.5)*math.log(2)-0.5*math.log(math.pi)-gammaln(k))

def balanced_tail(x,m):
    f = lambda q: math.exp(balanced_logpdf_q(q,m))
    value, error = quad(f,x,math.inf,epsabs=1e-14,epsrel=1e-10,limit=200)
    return value

def maxcdf_balanced(L,R,y=0.0):
    assert R%2==0
    m=R//2
    p=math.exp(L)
    b,c=normal_extreme_center(L)
    x=b+c*y
    tail=balanced_tail(x,m)
    return math.exp(p*math.log1p(-tail))

print('\nbalanced critical R=8*(log p)^2, y=0')
print('limit Q-max CDF = %.15f' % math.exp(-math.exp(2/8)))
print('limit Z-max CDF = %.15f' % math.exp(-1))
for L in (6,10,15):
    R=int(8*L**2)
    if R%2: R += 1
    print('L=%2d R=%5d Q=%.15f Z=%.15f' % (L,R,maxcdf_balanced(L,R),maxcdf_normal(L)))
