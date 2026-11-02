#!/usr/bin/env python3
"""Exact polynomial checks for a three-parameter genus-five hyperelliptic family."""
import sympy as S
x,a,b,c=S.symbols('x a b c')
f=x**11+a*x**7+b*x**5+c*x**3+x
H=S.Matrix(5,5,lambda i,j:S.Poly(f,x).coeff_monomial(x**(3*(i+1)-(j+1))) if 3*(i+1)-(j+1)>=0 else 0)
expected=S.Matrix([[0,1,0,0,0],[b,0,c,0,1],[0,a,0,b,0],[1,0,0,0,a],[0,0,0,1,0]])
assert H==expected, (H,expected)
B=H.extract([0,2,4],[1,3]); C=H.extract([1,3],[0,2,4]);
assert B==S.Matrix([[1,0],[a,b],[0,1]])
assert C==S.Matrix([[b,c,1],[1,0,a]])
D=(C.applyfunc(lambda v:v**3)*B).T
u=b**3+a*c**3
T=a**3*b**3+c**3*(a**4-b)-1
E=u+a**27
assert D==S.Matrix([[u,1],[1+b*c**3,a**3]])
assert S.expand(D.det()-T)==0
assert S.expand(D[1,0]-a**3*u+T)==0
assert S.expand((S.Matrix([[u,1]])*S.Matrix([1,a**27]))[0]-E)==0
h=x**5+a*x**3+b*x**2+c*x+1
R=S.Poly(S.resultant(h,S.diff(h,x),x),a,b,c,modulus=3)
expected_R=S.Poly(a**4*c**3+a**3*b**3-a**3*b**2*c**2-a**2*b*c**2+a**2*c**4-a*c**2-b*c**3+c**5-1,a,b,c,modulus=3)
assert R==expected_R,(R,expected_R)
assert R.eval({a:1,b:1,c:1})%3!=0
assert R.eval({a:0,b:1,c:2})%3!=0
assert R.eval({a:0,b:0,c:0})%3!=0
# On U intersect V(T), c cannot vanish: c=0,T=0 implies ab=1, singular.
# On c!=0, T_b=-c^3, E_a=c^3, E_b=E_c=0 imply transversality.
assert S.Poly(S.diff(T,b)+c**3,a,b,c,modulus=3).is_zero
assert S.Poly(S.diff(E,a)-c**3,a,b,c,modulus=3).is_zero
assert S.Poly(S.diff(E,b),a,b,c,modulus=3).is_zero
assert S.Poly(S.diff(E,c),a,b,c,modulus=3).is_zero
assert T.subs({a:1,b:1,c:1})%3==0
assert E.subs({a:1,b:1,c:1})%3==0
print('SYMBOLIC_GENUS5_CHAR3_CERTIFICATE_OK')
print('Hasse determinant D:',S.expand(D.det()))
print('resultant h,hprime:',R.as_expr())
