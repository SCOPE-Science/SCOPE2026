import sympy as S
r,z,a,A,b,c,e,eta=S.symbols('r z a A b c e eta', positive=True)
u=r*z
B = a*r*(1-u)/(u+A) - (a+b*r)/(1+b*u) + c*e/(e+eta*z)
assert S.simplify(B.subs(z,0)-((a/A-b)*r+c-a))==0
assert S.simplify(S.diff(B,r).subs({r:0,z:0})-(a/A-b))==0
assert S.simplify(S.diff(B,z).subs({r:0,z:0})+c*eta/e)==0
R=S.factor(A*(c-a)/(A*b-a))
d=S.factor(c-b*R)
assert S.simplify(d-a*(A*b-c)/(A*b-a))==0
assert S.simplify(R/d - A*(c-a)/(a*(A*b-c)))==0
vals={A:S.Rational(3,8),b:6,c:2,e:1,eta:2}
assert S.simplify(B.subs({**vals,a:2}) + S.Rational(2,3)*r).subs(z,0)==0
for aa in (S.Rational(1,2),S.Integer(2),S.Integer(3)):
 print('alpha',aa,'B at r=.3,v=.0001 =',S.N(B.subs({**vals,a:aa,r:S.Rational(3,10),z:S.Rational(1,10000)})))
assert S.simplify(R.subs({**vals,a:S.Rational(1,2)})-S.Rational(9,28))==0
assert S.simplify(d.subs({**vals,a:S.Rational(1,2)})-S.Rational(1,14))==0
x,y=S.symbols('x y', positive=True)
f=a*x*(x*(1-x)/(x+A)-y/(1+b*x))
g=y*(b*x/(1+b*x)-c*y/(1+(eta/e)*y))
J=S.Matrix([f,g]).jacobian([x,y]); J0=J.subs({**vals,a:S.Rational(1,2),x:S.Rational(1,4),y:S.Rational(3,4)})
assert S.trace(J0)==-S.Rational(11,100)
assert J0.det()==S.Rational(3,625)
assert f.subs({**vals,x:S.Rational(1,4),y:S.Rational(3,4)})==0
assert g.subs({**vals,x:S.Rational(1,4),y:S.Rational(3,4)})==0
J1=J.subs({**vals,a:S.Rational(1,2),x:S.Rational(1,12),y:S.Rational(1,4)})
assert J1.det()<0
print('Exact identities and coexistence stability check PASS')
