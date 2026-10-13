"""Exact rational verification of an Archimedean copula PQD/PMI witness.

Run with Python 3, without third-party modules. Every comparison below is
between exact fractions, including rigorous logarithm bounds.
"""
from fractions import Fraction as Q


def f(x):
    return x / 4 - x*x / 4 + x*x*x / 9 - Q(1,9)


def f_prime(x):
    return Q(1,4) - x / 2 + x*x / 3


def f_second(x):
    return -Q(1,2) + 2*x / 3


def ell(x):
    return 1/x - f_prime(x)


def curvature(x):
    return 1/(x*x) + f_second(x)


def log_bracket(z, terms=8):
    """Return rational lower and upper bounds for log(z), z>=1."""
    assert z >= 1
    t = (z - 1)/(z + 1)
    low = 2*sum((t ** (2*j+1))/Q(2*j+1) for j in range(terms))
    remainder = 2*t**(2*terms+1)/(Q(2*terms+1)*(1-t*t))
    return low, low + remainder


def g_bracket(x,u,v):
    lower,upper=log_bracket(x/(u*v))
    shift=f(x)-f(u)-f(v)
    return lower-shift, upper-shift


def rho(u,v,left,right):
    """Certify left < Archimedean copula(u,v) < right."""
    assert u*v < left < right < min(u,v)
    assert g_bracket(left,u,v)[1]<0, (u,v,'left')
    assert g_bracket(right,u,v)[0]>0, (u,v,'right')
    # g' = -phi'(x) = ell(x)>0.
    return left,right


def density_interval(u,v,left,right):
    """Rational enclosure for c(u,v) using monotonicity of ell,curvature."""
    pref=ell(u)*ell(v)
    # Both ell and curvature are positive and decreasing on (0,1).
    return pref*curvature(right)/ell(left)**3, pref*curvature(left)/ell(right)**3


pairs = [
    (Q(1,4),Q(1,4),Q(6433697255,100000000000),Q(6433697257,100000000000)),
    (Q(1,4),Q(3,4),Q(18897106192,100000000000),Q(18897106193,100000000000)),
    (Q(3,4),Q(3,4),Q(56538957970,100000000000),Q(56538957971,100000000000)),
]
intervals=[]
for u,v,left,right in pairs:
    rho(u,v,left,right)
    z=density_interval(u,v,left,right)
    intervals.append(z)
    print(f'density at ({u},{v}) in ({float(z[0]):.12f}, {float(z[1]):.12f})')

low=intervals[0][0]-2*intervals[1][1]+intervals[2][0]
high=intervals[0][1]-2*intervals[1][0]+intervals[2][1]
assert low > -Q(19002196, 1000000000)
assert high < -Q(19002192, 1000000000)
assert high < 0
print(f'PMI reflection defect strictly between {float(low):.12f} and {float(high):.12f}; certified NEGATIVE')

# Exact first variation of the same defect at independence (epsilon=0).
a={1:Q(1,4),2:-Q(1,4),3:Q(1,9)}
u=Q(1,4)
first=sum(a[m]*(m+1)**2*((1-u)**m-u**m)**2 for m in a)
assert first == -Q(11,576)
print('First variation: -11/576, certified')
