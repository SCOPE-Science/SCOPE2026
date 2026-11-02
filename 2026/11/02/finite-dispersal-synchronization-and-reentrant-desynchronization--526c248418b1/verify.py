"""Exact and independent numerical checks for heterogeneous two-patch synchrony."""
from __future__ import annotations
import sympy as sp
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

m, a, b, s, t = sp.symbols('m a b s t', positive=True)
X, Y, Z = sp.symbols('X Y Z')
A = sp.Matrix([[a + m, -m], [-m, b + m]])
g = sp.Matrix([s, t])
Sigma = sp.Matrix([[X, Z], [Z, Y]])
stationarity = A * Sigma + Sigma * A.T - g * g.T
sol = sp.solve(list(stationarity), [X, Y, Z], simplify=False)
assert len(sol) == 3
for expression in stationarity:
    assert sp.cancel(expression.subs(sol)) == 0

det_observed = sp.factor(sol[X]*sol[Y]-sol[Z]**2)
det_claim = ((b-a)*s*t+m*(t*t-s*s))**2 / (
    4*(a*b+(a+b)*m)*(a+b+2*m)**2)
assert sp.factor(det_observed-det_claim) == 0
assert sp.factor((A*g)[0]*t-(A*g)[1]*s +
                 ((b-a)*s*t+m*(t*t-s*s))) == 0

sub = {a: sp.Integer(3), b: sp.Integer(1), s: sp.Integer(1), t: sp.Integer(2)}
Px=sp.factor(sol[X].subs(sub))
Py=sp.factor(sol[Y].subs(sub))
Pz=sp.factor(sol[Z].subs(sub))
D=2*(4+2*m)*(3+4*m)
assert sp.cancel(Px-(9*m*m+10*m+4)/D) == 0
assert sp.cancel(Py-(9*m*m+52*m+48)/D) == 0
assert sp.cancel(Pz-(9*m*m+29*m+12)/D) == 0

R=sp.factor(Pz**2/(Px*Py))
R_expected=(9*m*m+29*m+12)**2/((9*m*m+10*m+4)*(9*m*m+52*m+48))
assert sp.factor(R-R_expected) == 0
assert sp.factor(sp.diff(R,m)-
  2*(3*m-4)*(9*m*m+29*m+12)*(54*m**3-309*m*m-664*m-360)/
  ((9*m*m+10*m+4)**2*(9*m*m+52*m+48)**2)) == 0
cubic=54*m**3-309*m*m-664*m-360
assert cubic.subs(m,sp.Rational(4,3)) < 0
assert cubic.subs(m,7)<0<cubic.subs(m,8)
assert [int(i) for i in sp.Poly(cubic,m).all_coeffs()]==[54,-309,-664,-360]
assert sp.simplify(R.subs(m,sp.Rational(4,3))-1)==0
assert sp.simplify(Px.subs(m,sp.Rational(4,3))-sp.Rational(3,10))==0
assert sp.simplify(Pz.subs(m,sp.Rational(4,3))-sp.Rational(3,5))==0
assert sp.simplify(Py.subs(m,sp.Rational(4,3))-sp.Rational(6,5))==0
assert sp.limit(R,m,sp.oo)==1
assert R.subs(m,0)==sp.Rational(3,4)

# The following forcing covariance is strictly positive definite, rather than
# the rank-one perfect-common-weather boundary case.
rho=sp.Rational(99,100)
Q=sp.Matrix([[sp.Integer(1),2*rho],[2*rho,sp.Integer(4)]])
assert sp.factor(Q.det())==sp.Rational(199,2500)
A0=A.subs({a:3,b:1})
s2=sp.solve(list(A0*Sigma+Sigma*A0.T-Q),[X,Y,Z],simplify=False)
R2=sp.factor(s2[Z]**2/(s2[X]*s2[Y]))
R2_expected=(224*m*m+721*m+297)**2 / (
       (224*m*m+249*m+100)*(224*m*m+1297*m+1200))
assert sp.factor(R2-R2_expected)==0
quartic=(2609152*m**4-17076864*m**3-10302432*m*m
         +25830809*m+22887750)
assert sp.factor(sp.diff(R2,m)-
       2*(224*m*m+721*m+297)*quartic/
       ((224*m*m+249*m+100)**2*(224*m*m+1297*m+1200)**2))==0
assert quartic.subs(m,1)>0>quartic.subs(m,2)
assert quartic.subs(m,6)<0<quartic.subs(m,8)
# The quartic has two sign changes, so Descartes gives at most two
# positive roots; the sign tests above force exactly two.
assert [sp.sign(x) for x in sp.Poly(quartic,m).all_coeffs()]==[1,-1,-1,1,1]

for r in [sp.Integer(1),sp.Rational(99,100)]:
  qq=np.array([[1., 2.*float(r)], [2.*float(r), 4.]])
  for h in [0., 0.1, 1., 4./3., 2., 5., 7., 8., 25., 100.]:
    aa=np.array([[3.+h,-h],[-h,1.+h]])
    ss=solve_continuous_lyapunov(aa, qq)
    r2=float((R if r==1 else R2).subs(m,sp.Rational(str(h))))
    measured=ss[0,1]**2/(ss[0,0]*ss[1,1])
    assert abs(r2-measured)<2e-12,(r,h,r2,measured)
    assert np.min(np.linalg.eigvalsh(ss))>-1e-12

print('PASS: exact Lyapunov covariance and determinant; perfect synchrony;')
print('      two stationary points in both rank-one and full-rank forcing;')
print('      all independent numerical covariance comparisons.')
