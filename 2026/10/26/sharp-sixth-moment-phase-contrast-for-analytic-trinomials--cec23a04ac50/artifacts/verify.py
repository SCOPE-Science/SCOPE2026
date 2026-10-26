#!/usr/bin/env python3
"""Symbolic and quadrature checks for the sharp analytic-quadratic phase-contrast inequality."""
import sympy as sp
import math
A,B,C,U,Z,S,T=sp.symbols('A B C U Z S T', positive=True)
# Treat U as a formal unit complex phase for the middle coefficient.
P=sp.Poly(sp.expand((A+B*U*Z+C*Z**2)**3),Z)
M=sp.expand(sum(q*q.subs(U,U**-1) for _,q in P.terms()))
Q0=A**6+B**6+C**6+9*(A**4*B**2+A**4*C**2+A**2*B**4+A**2*C**4+B**4*C**2+B**2*C**4)+36*A**2*B**2*C**2
K=6*A*B**2*C*(3*A**2+2*B**2+3*C**2)
assert sp.simplify(M-(Q0+K*(U**2+U**-2)/2))==0
Mmin=sp.factor(Q0-K)
Cpoly=S**3+6*S+9*T*S**2-18*T*S+18*T+9*T**2*S-12*T**2+T**3
V=sp.symbols('V',positive=True)
check=sp.factor((Mmin/(A*C)**3).subs({A:V,C:1/V,B:sp.sqrt(T)})-Cpoly.subs(S,V**2+V**-2))
assert check==0
N=12*T*(3*S+2*T)
W=sp.factor(sp.diff(N,S)*Cpoly-N*sp.diff(Cpoly,S))
assert sp.expand(W+36*T*(2*S**3+12*S*T**2+5*T**3+T*(11*S**2-14)))==0
C2=sp.factor(Cpoly.subs(S,2))
assert C2==(T+2)*(T**2+4*T+10)
R=1+sp.cancel(N.subs(S,2)/C2)
quartic=T**4+6*T**3-40*T-60
assert sp.simplify(sp.diff(R,T)+24*quartic/((T+2)**2*(T**2+4*T+10)**2))==0
root=float(sp.nroots(quartic)[1]);assert 2.68<root<2.69
assert sum(complex(x).real>0 and abs(complex(x).imag)<1e-9 for x in sp.nroots(quartic))==1
r=float(R.subs(T,root));assert 3.7977<r<3.7978
# Independently approximate the defining Fourier integral at several nonzero coefficients.
import cmath
for a,b,c,theta in [(1.0,1.0,1.0,0.0),(1.0,1.0,1.0,math.pi/2),(0.8,2.0,1.9,math.pi/5),(1.0,math.sqrt(root),1.0,math.pi/2),(1.0,math.sqrt(root),1.0,0.0)]:
  n=8192
  # Keep ordinary Python's complex exponent literal separate from imaginary j.
  integral=sum(abs(a+b*cmath.exp(1j*(2*math.pi*k/n+theta))+c*cmath.exp(1j*(4*math.pi*k/n)))**6 for k in range(n))/n
  Q=float(Q0.subs({A:a,B:b,C:c}));kk=float(K.subs({A:a,B:b,C:c}));formula=Q+kk*math.cos(2*theta)
  assert abs(integral-formula)<2e-8*max(1.0,formula),(a,b,c,theta,integral,formula)
print(f'VERIFY_OK exact_identities=5 quadrature_cases=5 root={root:.12f} sharp_moment_ratio={r:.12f} sharp_norm_ratio={r**(1/6):.12f}')
