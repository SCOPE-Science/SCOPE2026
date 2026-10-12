#!/usr/bin/env python3
"""Symbolic and rational consistency checks for a two-step cyclic gradient theorem.

Run: python3 csd2_cycle_verify.py
Requires Python 3 and SymPy. The algebraic theorem is proved separately;
finite computational checks are corroborating evidence only.
"""
from fractions import Fraction
from sympy import symbols, factor, expand, simplify, discriminant, sqrt, Rational

k, r, a, x = symbols('k r a x', positive=True)
A = k**3
B = 2*k**3-2*k**2+4*k-1
C = -k**3+4*k**2-2*k+2
Q = A*r**3+B*r**2+C*r+1
P = 2*k**4-10*k**3+3*k**2-10*k+2
T = (5+3*sqrt(3))/2
K = (T+sqrt(T**2-4))/2
assert simplify(K**2-T*K+1) == 0
assert simplify(P/k**2 - (2*(k+1/k)**2-10*(k+1/k)-1)) == 0
assert factor(discriminant(Q, r) - 4*(k-1)**6*(k*k+1)*P) == 0

# The exact two-mode ratio for initial gradient g=(1,sqrt(r)).
N = (k-1)**4*(k*r**4+r)
D = (1+k*r)**4*(k+r)
assert factor(D-N-k*(1+r)**2*Q) == 0

# Cross-check moment polynomial on endpoint-supported normalized gradient weights.
mean = (1+k*r)/(1+r)
m2 = (1+k*k*r)/(1+r)
m3 = (1+k**3*r)/(1+r)
S = 2*mean**3 -4*mean*m2+m3
E = 2*mean**3+(k+1-4*mean)*((k+1)*mean-k)-k*mean
assert factor(S-E)==0
assert factor(E+Q/(1+r)**3)==0

# Explicit two-dimensional rational counterexample with A=diag(1,5), g=(4,1).
lam=(Fraction(1),Fraction(5))
g=(Fraction(4), Fraction(1))
step=sum(t*t for t in g)/sum(lam[i]*g[i]*g[i] for i in range(2))
x0=tuple(g[i]/lam[i] for i in range(2))
x1=tuple(x0[i]-step*g[i] for i in range(2))
x2=tuple(x1[i]-step*lam[i]*x1[i] for i in range(2))
f=lambda v: sum(lam[i]*v[i]*v[i] for i in range(2))/2
assert f(x2)>f(x0)
assert f(x2)/f(x0)==Fraction(5599232,5250987)
assert step == Fraction(17,21)
assert factor(Q.subs({k:5,r:Rational(1,16)}))==-Rational(723,4096)

# Coefficient-case discriminant and positive derivative criteria are verified algebraically.
poly=2*a**2-(k+1)*a+k
assert factor(discriminant(poly,a)-(k*k-6*k+1))==0
print('VERIFY_OK')
print('rational_counterexample_step',step)
print('objective_before',f(x0))
print('objective_after',f(x2))
print('objective_ratio',f(x2)/f(x0))
print('k_star_approx',K.evalf(18))
