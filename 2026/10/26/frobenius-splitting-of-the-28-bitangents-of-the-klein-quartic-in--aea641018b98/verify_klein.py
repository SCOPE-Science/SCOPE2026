"""Exact arithmetic of the twenty-eight bitangents of a plane quartic over GF(5).
Requires SymPy. Run: python verify_klein.py
"""
import sympy as s
X,Y,U,V,W=s.symbols('X Y U V W')
F=X**3*Y+Y**3*(U*X+V*Y)+(U*X+V*Y)**3*X
A,B,C,D,E=[s.expand(F).coeff(X,4-i).coeff(Y,i) for i in range(5)]
P=s.Poly(s.expand(8*A**2*D-B*(4*A*C-B**2)),U,V,modulus=5).as_expr()
Q=s.Poly(s.expand(64*A**3*E-(4*A*C-B**2)**2),U,V,modulus=5).as_expr()
G=s.groebner([P,Q,W*U-1],W,V,U,order='lex',modulus=5)
H=s.Poly(U**28+U**21+2*U**14-2*U**7+1,U,modulus=5)
assert {str(g.as_expr()) for g in G.polys}=={str(W+U**27+U**20+2*U**13-2*U**6),str(V+U**26),str(H.as_expr())}
assert s.gcd(H,H.diff()).degree()==0
fac=s.factor_list(H.as_expr(),modulus=5)[1]
assert sorted([s.Poly(f,U,modulus=5).degree() for f,k in fac])==[1,3,6,6,6,6]
assert all(k==1 for f,k in fac)
assert s.Poly(s.resultant(P,Q,V),U,modulus=5).monic()==s.Poly(U**24,U,modulus=5)*H
assert s.expand((X**3*Y+Y**3*(-X-Y)+(-X-Y)**3*X)+(X**2+X*Y+Y**2)**2).expand().as_poly(X,Y,modulus=5).is_zero
for f,k in fac:
 p=s.Poly(f,U,modulus=5)
 d=p.degree()
 def r(e):return s.rem(s.Poly(e,U,modulus=5),p)
 u=r(U);v=r(-U**26)
 a=r(u**3);b=r(3*u*u*v+1);c=r(3*u*v*v)
 assert s.gcd(a,p).degree()==0
 delta=r(2*(b*b-a*c)*s.invert(a*a,p))
 e=(5**d-1)//2
 power=r(1); base=delta
 while e:
  if e&1:power=r(power*base)
  base=r(base*base);e//=2
 expected=4 if d==1 else 1
 assert power==r(expected), (d,p,power)
 print('IRREDUCIBLE',d,p.as_expr(),'CONTACT_EULER',power.as_expr())
# Smoothness: Fx Fy Fz nonzero simultaneous; in the torus equations imply 1=(-3)^3, contradicted mod 5.
print('BITANGENT_ORBITS 1:1 3:1 6:4; ALL_CONTACTS over F_(5^6); PASS')
