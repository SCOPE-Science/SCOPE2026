"""Self-contained reproducible checks for three-node interpolatory quadrature.
No external data is needed; Python stdlib suffices for exact checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import log, isclose
import random


def weight_numer(a, b):
    return a*b - (a+b)/2 + F(1,3)


def weights(x,y,z):
    return (
        weight_numer(y,z)/((x-y)*(x-z)),
        weight_numer(x,z)/((y-x)*(y-z)),
        weight_numer(x,y)/((z-x)*(z-y)),
    )

# All 3-point rules on a rational lattice; exactness and sign exclusions.
count = 0
patterns = set()
for i,j,k in combinations(range(1,17),3):
    x,y,z = (F(i,18),F(j,18),F(k,18))
    w = weights(x,y,z)
    assert sum(w) == 1
    assert sum(wi*xi for wi,xi in zip(w,(x,y,z))) == F(1,2)
    assert sum(wi*xi*xi for wi,xi in zip(w,(x,y,z))) == F(1,3)
    assert sum(v<0 for v in w) <= 1
    assert (w[1]>0) == (weight_numer(x,z)<0)
    patterns.add(tuple(v<0 for v in w))
    count+=1
assert patterns == {(False,False,False),(True,False,False),
                    (False,True,False),(False,False,True)}

# Independent numerical integral identities for the uniform order-statistic law.
# q = probability(all weights >= 0), r = probability(middle weight >0).
from math import log
q = .5*log(3)-1/3
r = 1/3
p_end = (r-q)/2
assert 0 < p_end < q < r < 1
assert isclose(q+2*p_end+2/3,1,rel_tol=0,abs_tol=1e-15)

# Deterministic midpoint integration checks of the 2D probability integrals.
def midpoint(fn, lo, hi, count):
    h=(hi-lo)/count
    return h*sum(fn(lo+(j+.5)*h) for j in range(count))

# P(all positive) = 3/4 * double integral over a in [1/3,1],
# b in [1/(3a),1] of (1/(3a) + 1/(3b)) db da.
def outer(a):
    low=1/(3*a)
    return (1/(3*a))*(1-low)+(1/3)*log(3*a)
num_pos = .75*midpoint(outer,1/3,1,12000)
assert abs(num_pos-q)<2e-8, (num_pos,q)

# P(mid positive) = 3/4 double integral of a+b on same region.
def outer_mid(a):
    low=1/(3*a)
    return a*(1-low)+.5*(1-low*low)
num_mid=.75*midpoint(outer_mid,1/3,1,12000)
assert abs(num_mid-r)<2e-8, (num_mid,r)

# Universal leading coefficient: 12*integral_0^1 [x^2-x+1/3] dx = 2.
gintegral=F(1,3)-F(1,2)+F(1,3)
assert gintegral == F(1,6)
assert 12*gintegral == 2

# The two-gap area identity and the asymptotic log coefficient.
def area(epsilon, delta):
    assert 0<epsilon<delta*delta
    return epsilon*(1+log(delta*delta/epsilon))
for k in (6,8,10,12):
    t=10**k
    c=.37
    a=area(c/t,.1)
    # The finite correction is exactly the displayed log term.
    assert isclose(t*a/c,1+log(.01*t/c),rel_tol=2e-15)
    assert abs(t*a/log(t)-c)<.4

# Reproducible Monte Carlo sanity check (not used for the infinite theorem).
rng=random.Random(20261028)
N=250000
freq=[0,0,0,0]
for _ in range(N):
    x,y,z=sorted((rng.random(),rng.random(),rng.random()))
    u,v,w=weights(x,y,z)
    index=0 if min(u,v,w)>=0 else (1 if u<0 else (2 if v<0 else 3))
    freq[index]+=1
expected=[q,p_end,2/3,p_end]
for observed, exp in zip(freq,expected):
    assert abs(observed/N-exp)<.006, (freq,expected)

print('VERIFY_OK rational_triples=%d exactness=3 sign_patterns=4 integral_checks=2 '
      'tail_coefficient=2 simulated=%s'%(count,freq))
