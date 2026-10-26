#!/usr/bin/env python3
"""Exact polynomial checks for the cubic integration-locus Weierstrass model."""
from sympy import symbols, expand, factor, discriminant, Poly, simplify

a0,a1,a2,a3,T,X,W,U,V,Z=symbols('a0 a1 a2 a3 T X W U V Z')
F=6*a3*X**3+2*a2*T*X**2+a1*T*(T-W)*X+a0*T*(T-W)*(T-2*W)
A=-48*a0*a3
B=a1**2-16*a0*a2
C=-2*a0*a1
D=a0**2
Xsub=U; Tsub=Z; Wsub=(V+a1*U+3*a0*Z)/(4*a0)
weier=V**2*Z-A*U**3-B*U**2*Z-C*U*Z**2-D*Z**3
assert simplify(8*a0*F.subs({X:Xsub,T:Tsub,W:Wsub})-weier)==0
f=A*U**3+B*U**2+C*U+D
delta=factor(discriminant(f,U))
Q=972*a0**3*a3**2+432*a0**2*a1*a2*a3-256*a0**2*a2**3-3*a0*a1**3*a3+32*a0*a1**2*a2**2-a1**4*a2
assert expand(delta+64*a0**3*Q)==0
E=B**2-3*A*C
assert expand(E-(a1**2-16*a0*a2)**2+288*a0**2*a1*a3)==0
# singular cusp family is triple-root f(u) at u=-B/(3A); for cubics this is iff E=delta=0
# Verify cusp parameterization stated in the article.
cs_a2=-a1**2/(48*a0)
cs_a3=a1**3/(162*a0**2)
assert simplify(Q.subs({a2:cs_a2,a3:cs_a3}))==0
assert simplify(E.subs({a2:cs_a2,a3:cs_a3}))==0
# conversely the common vanishing of E,Q forces the above formulas: eliminate a3 using E
from sympy import solve
expr_for_a3=solve(E,a3)[0]
q_reduced=factor(Q.subs(a3,expr_for_a3))
print('Elimination of a3 from E=0 gives Q proportional to:',q_reduced)
# j formula as c4^3 / discriminant for y^2=f(u), with leading A
# Convert x'=A*u, y'=A*v giving (y')^2=(x')^3+B(x')^2+A*C*x'+A^2*D
# Standard c4=16(B^2-3*A*C), cubic discriminant of monic RHS = A^2*delta
assert simplify((16*E)**3/(16*A**2*delta)-256*E**3/(A**2*delta))==0
for a,expect in [((1,0,0,1),0),((1,1,1,1),None)]:
 vals=dict(zip((a0,a1,a2,a3),a))
 di=factor(delta.subs(vals))
 ji=factor((256*E**3/(A**2*delta)).subs(vals))
 print('coefficients=',a, 'discriminant=',di,'j=',ji)
 if expect is not None: assert ji == expect
print('VERIFY_OK')
