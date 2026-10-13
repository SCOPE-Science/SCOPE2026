"""Exact-rational checks for an impulsive Allee predator model.

This checker verifies a parameter witness and the algebraic hypotheses of
its global decay argument; the continuous-time comparison proof is in RESULT.md.
"""
from fractions import Fraction as F

r, K, a, q, e, mu = F(2), F(10), F(2), F(1,10), F(1,2), F(5,4)
eta, h, E, p1, p2, tau = F(1,2), F(1,2), F(1), F(1,2), F(1,100), F(0)
assert all(v > 0 for v in [r,K,a,q,e,mu,eta,h,E,p1,p2])
assert 0 < e < 1 and 0 < eta < 1
assert 0 < p1*E < 1 and 0 < p2*E < 1 and tau == 0

def psi(y): return y/(1+y)
def prey_rhs(x,y): return r*x*(1-x/K)-a*x*y/(1+a*q*x)
def predator_growth(x,y): return e*a*x*psi(y)/(1+a*q*x)-mu

def prey_nullcline(x): return (r/a)*(1-x/K)*(1+a*q*x)
roots = ((F(5),F(1)),(F(20,3),F(7,9)))
for x,y in roots:
    assert 0 < x < K and y > 0
    assert y == prey_nullcline(x)
    assert prey_rhs(x,y) == 0 and predator_growth(x,y) == 0
# Eliminating y gives 3x^2 - 35x + 100 = (x-5)(3x-20).
for x,y in roots:
    assert 3*x*x-35*x+100 == 0
# The two roots, discriminant and product identity are exact.
assert (-35)**2-4*3*100 == 25
assert roots[0][0]+roots[1][0] == F(35,3)
assert roots[0][0]*roots[1][0] == F(100,3)
(x1,y1),(x2,y2)=roots
assert x1 < x2
hstar=eta*x1+(1-eta)*y1
pbar=p1*h/(eta*K-(1-p1*E)*h)
theta=h/eta
max_gain=e*a*theta/(1+a*q*theta)
delta=mu-max_gain
assert theta == 1 and max_gain == F(5,6) and delta == F(5,12)
assert hstar == 3 and eta*K == 5 and h <= min(hstar,eta*K)
assert pbar == F(1,19) and 0 < p2 < pbar
assert 0 < 1-p2*E < 1 and 0 < 1-p1*E < 1
assert theta < x1 < x2
print('VERIFY_OK')
print('coexistence_points:', roots)
print('bar_p2:',pbar,'hstar:',hstar,'theta:',theta,'delta:',delta)
