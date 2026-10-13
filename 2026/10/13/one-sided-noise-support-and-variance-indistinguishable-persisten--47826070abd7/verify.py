"""Exact-arithmetic checks of the matched-variance logistic support example.

This checks finite algebraic identities and inequalities, not the infinite-time
probabilistic theorem. See the accompanying proof for that argument.
"""
from fractions import Fraction as F
from math import exp

r = F(2)
a = F(1, 16)
v = a*a
left, right = F(3, 8), F(5, 8)
def f(x):
    return r*x*(1-x)

# Concavity gives the minimum at an endpoint and maximum at 1/2.
f_min = min(f(left), f(right))
f_max = f(F(1,2))
assert f_min == F(15,32)
assert f_max == F(1,2)
assert left < f_min-a and f_max+a < right
assert f_min-a == F(13,32)
assert f_max+a == F(9,16)
assert max(abs(r*(1-2*left)),abs(r*(1-2*right))) == F(1,2)

# Both noise laws have mean 0 and variance v; the shifted unit-
# exponential moments are E[1-Y]=0 and E[(1-Y)^2]=1.
assert v == F(1,256)
# Quartic Q from the motivating Gaussian moment closure at r=2.
def Q(x):
    return 16*x**4 - 32*x**3 + 18*x*x -3*x - 2*v
assert Q(F(1,4)) == -F(9,128)
assert Q(F(3,8)) == F(7,256)
assert Q(F(1,2)) == -F(1,128)

# In the blow-down proof, taking L=2 bounds the sum of all
# Chebyshev failure probabilities above by 1/3840.
L=F(2)
assert L >= F(4,1)/r
assert F(64)*v/(15*r*r*L**4)==F(1,3840)
print('VERIFY_OK')
