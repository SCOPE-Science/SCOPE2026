#!/usr/bin/env python3
"""Exact symbolic and rational checks for a three-coordinate OU feedback model.

Requires Python 3 and SymPy. The symbolic identities, not any finite
parameter sample, certify the formulas across the stated parameter domain.
"""
import sympy as sp

h, k = sp.symbols('h k', real=True)
lam = sp.Symbol('lam')
A = sp.Matrix([[-1-k, 1, 0], [0, -1, -h], [-1, h, -1]])
s11, s12, s13, s22, s23, s33 = sp.symbols('s11 s12 s13 s22 s23 s33')
S0 = sp.Matrix([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])
res = A*S0 + S0*A.T + 2*sp.eye(3)
unknown = (s11,s12,s13,s22,s23,s33)
sol = sp.solve([res[i,j] for i in range(3) for j in range(i,3)],unknown,simplify=False)
assert set(sol) == set(unknown)
S = S0.subs(sol)
assert all(sp.cancel(v)==0 for v in A*S+S*A.T+2*sp.eye(3))
Q = A*S + sp.eye(3)
assert all(sp.cancel(v)==0 for v in Q+Q.T)

D = 2*h*h + h + 2*k*k + 8*k + 8
N = 4*h**4 + 4*h*h*k*k + 16*h*h*k + 20*h*h - 4*h*k - 8*h + 4*k + 9
phi = sp.cancel(sp.trace(S.inv()*Q.T*Q))
assert sp.cancel(phi - N/D)==0
assert sp.cancel(Q[0,1] - 2*(h*h-h+k+2)/D)==0
assert sp.cancel(Q[0,2] + (2*h*k+2*h-2*k-5)/D)==0
assert sp.cancel(Q[1,2] + (2*h**3+2*h*k*k+8*h*k+9*h-k-2)/D)==0

P = sp.expand(A.charpoly(lam).as_expr())
P_expected = (lam**3+(k+3)*lam**2+(h*h+2*k+3)*lam + (h*h+1)*(k+1)-h)
assert sp.expand(P-P_expected)==0
# The Routh-Hurwitz positivity criterion is proved analytically in RESULT.md;
# here we check the polynomial identity for the last determinant.
a2,a1,a0=(k+3),(h*h+2*k+3),((h*h+1)*(k+1)-h)
assert sp.expand(a2*a1-a0-D)==0

dphi_expected=4*(h*h-h+k+2)*(2*(h-1)*k+2*h-5)/D**2
assert sp.cancel(sp.diff(phi,k)-dphi_expected)==0
F=2*h**3-4*h*h+8*h-9
phi_diff_expected=2*k*(F*k+2*(2*h-5)*(h*h-h+2))/((2*h*h+h+8)*D)
assert sp.cancel(phi-phi.subs(k,0)-phi_diff_expected)==0
assert sp.limit(phi,k,sp.oo)==2*h*h
assert sp.expand(sp.diff(F,h)-2*(3*h*h-4*h+4)) == 0

# Exact evaluations of a nonmonotone witness; these illustrate, not certify,
# the general theorem.
p2=sp.factor(phi.subs(h,2))
assert sp.cancel(p2 - (16*k*k+60*k+137)/(2*(k*k+4*k+9))) == 0
assert p2.subs(k,0)==sp.Rational(137,18)
assert p2.subs(k,sp.Rational(1,2))==sp.Rational(38,5)
assert sp.cancel(p2-p2.subs(k,0)-k*(7*k-8)/(18*(k*k+4*k+9)))==0
assert p2.subs(k,sp.Rational(8,7))==p2.subs(k,0)
assert sp.limit(p2,k,sp.oo)==8
print('PASS: symbolic covariance, current, rate, stability, derivative, crossings, and exact witness.')
