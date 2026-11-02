"""Exact symbolic identities for a rational quintic and its prime-characteristic specializations.
Requires sympy. All equalities are polynomial equalities over Z or stated F_p."""
import sympy as S
s,t,u = S.symbols('s t u')
X,Y,Z = S.symbols('X Y Z')
P = S.Matrix([s**4*t, s**2*t**3-s**5, t**5+2*s**3*t**2])
F = 27*X**5+18*X**3*Y*Z-2*X**2*Y**3-X**2*Z**3+2*X*Y**2*Z**2-Y**4*Z
assert S.expand(F.subs({X:P[0],Y:P[1],Z:P[2]}))==0
A = S.Matrix([u**4,u**2-u**5,1+2*u**3]); cross=A.cross(A.diff(u))
assert [S.factor(c) for c in cross]==[u*(u**3+2)*(4*u**3-1), 2*u**3*(u**3+2),-u**5*(u**3+2)]
Q = S.Matrix([4*u**3-1,2*u**2,-u**4]);assert all(S.expand(c-u*(u**3+2)*q)==0 for c,q in zip(cross,Q))
# Exact rational inverse of Gauss parameter when characteristic !=2.
assert S.cancel(Q[0]/(2*Q[1])-Q[1]/(8*Q[2])-u)==0
# Change of local coordinates at u=0 in odd characteristic.
assert S.expand(A[0]*A[2]-A[1]**2-u**7*(4-u**3))==0
# Characteristic 3: points u=0,1; local chart X nonzero at u=1.
v=S.symbols('v')
Ap=[S.Poly(z.subs(u,1+v),v,modulus=3) for z in A]
assert Ap[0].eval(0)==1
# In char 3: Y=-u^2(u-1)^3, Z=-(u-1)^3, and Y-Z=(u-1)^4(1-(u-1)).
assert S.Poly(A[1].subs(u,1+v)+v**3*(1+v)**2,v,modulus=3).is_zero
assert S.Poly(A[2].subs(u,1+v)+v**3,v,modulus=3).is_zero
assert S.Poly((A[1]-A[2]).subs(u,1+v)-v**4*(1-v),v,modulus=3).is_zero
# In char2 affine Z=1, x=u^4, y=u^2+u^5 and eta=x+y^2+y^5 starts in order 13.
eta=S.Poly(u**4+(u**2+u**5)**2+(u**2+u**5)**5,u,modulus=2)
assert eta.as_expr()==u**25+u**22+u**13
assert S.Poly(F.subs({X:X,Y:Y,Z:1})-(X**5+X**2+Y**4),X,Y,modulus=2).is_zero
assert S.Poly(Q[0]-1,u,modulus=2).is_zero
assert S.Poly(Q[1],u,modulus=2).is_zero
assert S.Poly(Q[2]-u**4,u,modulus=2).is_zero
# Characteristic 3 derivative of Gauss map is generically nonzero.
assert S.Poly(Q[1].diff(u),u,modulus=3).degree()==1
print('QUINTIC_REDUCTION_IMPLICIT_GAUSS_CUSP_IDENTITIES_OK')
