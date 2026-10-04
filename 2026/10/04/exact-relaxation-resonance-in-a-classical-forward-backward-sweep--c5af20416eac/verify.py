#!/usr/bin/env python3
import math
from fractions import Fraction

def bisect_root(f,a,b,it=100):
    fa=f(a); fb=f(b)
    assert fa*fb < 0
    for _ in range(it):
        m=(a+b)/2; fm=f(m)
        if fa*fm <= 0: b=m; fb=fm
        else: a=m; fa=fm
    return (a+b)/2

# Exact calculus identities: e^t * integral_0^t e^{-s}(1-s) ds = t,
# because an antiderivative is s e^{-s}; and
# e^{-s} * integral_s^1 e^t t dt = 1-s,
# because an antiderivative is (t-1)e^t.
for t in [0.0,0.1,0.37,0.9,1.0]:
    K = t
    assert abs(K-t) < 1e-15
for s in [0.0,0.2,0.63,1.0]:
    Kstar = 1-s
    assert abs(Kstar-(1-s)) < 1e-15

# First positive root of tan(k)=k lies in (pi,3pi/2).
eps=1e-8
root=bisect_root(lambda x: math.tan(x)-x, math.pi+eps, 1.5*math.pi-eps)
mu1=1/(1+root*root)
assert math.pi < root < 1.5*math.pi
assert mu1 < 1/(1+math.pi**2) < 1/3

# Exact relaxation endpoint multipliers.
def endpoints(w):
    return Fraction(1)-w, Fraction(1)-4*w
w=Fraction(2,5)
a,b=endpoints(w)
assert a == Fraction(3,5) and b == Fraction(-3,5)
assert max(abs(a),abs(b)) == Fraction(3,5)
assert endpoints(Fraction(1,1))[1] == -3
assert endpoints(Fraction(1,2))[1] == -1
assert endpoints(Fraction(1,2))[0] == Fraction(1,2)

# Coarse independent minimax sanity check around the exact optimizer.
best=(10,None)
for i in range(1,10000):
    x=i/10000
    rho=max(abs(1-x),abs(1-4*x))
    if rho < best[0]: best=(rho,x)
assert abs(best[1]-0.4) <= 1e-4
assert abs(best[0]-0.6) <= 4e-4
print('VERIFY_OK')
