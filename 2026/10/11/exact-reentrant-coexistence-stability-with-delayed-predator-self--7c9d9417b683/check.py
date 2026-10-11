"""Exact rational checks for a delayed two-population model's stability switches.

The finite checks corroborate algebraic premises, not an independent proof of
infinite-dimensional root exclusion or nonlinear stability.
"""
from fractions import Fraction as Q
from math import acos, pi, sqrt, isclose

h1, a1, h2, a2, d1, b, d = Q(21, 2), Q(9, 2), Q(3, 10), Q(1), Q(12), Q(1), Q(7, 60)
x = y = Q(1)
assert x*(h1-a1*x)-d1*x*y/(1+b*x) == 0
assert y*(h2-a2*y)+d*d1*x*y/(1+b*x) == 0
# Differentiate the instantaneous right-hand side and its delayed term.
A11 = h1-2*a1*x-d1*y/(1+b*x)**2
A12 = -d1*x/(1+b*x)
A21 = d*d1*y/(1+b*x)**2
A22 = h2-a2*y+d*d1*x/(1+b*x)
B22 = -a2*y
assert (A11,A12,A21,A22,B22) == (Q(-3,2),Q(-6),Q(7,20),Q(0),Q(-1))
k, m, n = -A11, -(A12*A21), -B22
assert (k,m,n) == (Q(3,2),Q(21,10),Q(1))
# From P(lambda)=lambda^2+k lambda+m, Q(lambda)=n(lambda+k).
# F(X)=|P(i sqrt(X))|^2-|Q(i sqrt(X))|^2.
coefficient_X = k*k-2*m-n*n
constant = m*m-n*n*k*k
lo, hi = Q(27,20),Q(8,5)
assert coefficient_X == -(lo+hi)
assert constant == lo*hi
assert (lo-hi)<0 and (hi-lo)>0
for X, cosval, sin_square in [
    (lo,Q(-7,8),Q(15,64)),
    (hi,Q(-9,11),Q(40,121)),
]:
    assert -k*m/(n*(X+k*k)) == cosval
    assert X*(X+k*k-m)**2/(n*n*(X+k*k)**2) == sin_square
    assert cosval*cosval+sin_square==1
omega_minus=sqrt(float(lo)); omega_plus=sqrt(float(hi))
theta_minus=acos(-7/8);theta_plus=acos(-9/11)
tau_p0=theta_plus/omega_plus
tau_m0=theta_minus/omega_minus
tau_p1=(theta_plus+2*pi)/omega_plus
tau_m1=(theta_minus+2*pi)/omega_minus
assert 0<tau_p0<tau_m0<tau_p1<tau_m1
assert omega_plus<2*omega_minus
assert isclose(tau_p0,1.9993800252788306,rel_tol=1e-12)
assert isclose(tau_m0,2.268907375057647,rel_tol=1e-12)
assert isclose(tau_p1,6.966674158176881,rel_tol=1e-12)
print('CHECK_OK', 'J=',(A11,A12,A21,A22,B22),
      'X_roots=',(lo,hi),'taus=',(tau_p0,tau_m0,tau_p1,tau_m1))
