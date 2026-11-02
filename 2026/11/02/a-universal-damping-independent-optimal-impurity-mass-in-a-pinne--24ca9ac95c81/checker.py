"""Exact symbolic certificate and independent numerical tests for a pinned Langevin trimer."""
from __future__ import annotations
import json
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov

u, g, w, k = sp.symbols('u g w k', positive=True)
M = sp.diag(1, u, 1)
K = sp.Matrix([[w+k, -k, 0], [-k, w+2*k, -k], [0, -k, w+k]])
A = sp.zeros(6)
A[:3,3:] = M.inv()
A[3:,:3] = -K
A[3,3] = -g
A[5,5] = -g
Q = sp.zeros(6)
Q[3,3] = 2*g   # Unit temperature difference with right reservoir at zero
pairs = [(i,j) for i in range(6) for j in range(i,6)]
xs = sp.symbols('c0:'+str(len(pairs)))
C = sp.zeros(6)
for (i,j), x in zip(pairs, xs):
    C[i,j]=C[j,i]=x
L = A*C + C*A.T + Q
coeff, rhs = sp.linear_eq_to_matrix([L[i,j] for i,j in pairs], xs)
soln = coeff.inv()*rhs
solved = C.subs(dict(zip(xs,soln)), simultaneous=True)
assert all(sp.cancel(z)==0 for z in (A*solved+solved*A.T+Q))
current = sp.factor(g*(1-solved[3,3]))
R = k*k+3*k*w+w*w
B = k**3+7*k*k*w+8*k*w*w+2*w**3
E = 2*k**3+7*k*k*w+5*k*w*w+w**3
a = k+w
D = g**4*u*R + g*g*(a**3*u*u -B*u +E)+k**4
expected = g*k*k*(g*g*u*a+k*k)/(2*D)
assert sp.cancel(current-expected)==0
num_pos = g*g*(u*a*a+R)+2*k*k*a
opt = 1+k*w/a**2
expected_derivative = -g**3*k*k*(a*a*u-R)*num_pos/(2*D**2)
assert sp.cancel(sp.diff(expected,u)-expected_derivative)==0
assert sp.expand(4*a**3*E-B**2)==sp.expand(k*k*a*a*(7*k*k+24*k*w+8*w*w))
assert sp.cancel(opt-R/a**2)==0
assert sp.factor(expected.subs({u:sp.Rational(5,4),g:1,k:1,w:1}))==sp.Rational(1,7)
assert sp.factor(expected.subs({u:1,g:1,k:1,w:1}))==sp.Rational(3,22)

cases = [(1,1,1,sp.Rational(1,3)),(1,1,1,sp.Rational(5,4)),(1,1,1,4),
         (2,1,sp.Rational(2,3),1),(1,2,3,sp.Rational(3,2)),
         (sp.Rational(1,2),sp.Rational(4,3),2,sp.Rational(8,5)),
         (3,sp.Rational(1,3),sp.Rational(1,4),sp.Rational(7,3)),
         (sp.Rational(7,4),sp.Rational(1,5),sp.Rational(3,2),sp.Rational(9,10)),
         (2,3,1,sp.Rational(17,9)),(3,2,sp.Rational(5,2),sp.Rational(7,4)),
         (sp.Rational(1,5),sp.Rational(1,3),sp.Rational(3,5),sp.Rational(5,9)),
         (sp.Rational(9,5),sp.Rational(2,5),sp.Rational(1,10),sp.Rational(3,2))]
max_err=0.0
for gv,wv,kv,uv in cases:
    av = np.array(A.subs({g:gv,w:wv,k:kv,u:uv}),dtype=float)
    qv = np.array(Q.subs({g:gv,w:wv,k:kv,u:uv}),dtype=float)
    cv = solve_continuous_lyapunov(av,-qv)
    direct = float(gv)*(1-cv[3,3]); formula=float(expected.subs({g:gv,w:wv,k:kv,u:uv}))
    err=abs(direct-formula)
    max_err=max(max_err,err)
    assert err<2e-10, (gv,wv,kv,uv,err)
    assert np.max(np.real(np.linalg.eigvals(av))) < -1e-12
print(json.dumps({'status':'PASS','symbolic_lyapunov_certificate':'exact 21-equation solve',
                  'symbolic_current':'exact identity','derivative_factorization':'exact identity',
                  'denominator_discriminant':'exact negative discriminant',
                  'independent_numeric_cases':len(cases),'maximum_absolute_error':max_err,
                  'sample_optimum_current':'1/7','sample_equal_mass_current':'3/22'}))
