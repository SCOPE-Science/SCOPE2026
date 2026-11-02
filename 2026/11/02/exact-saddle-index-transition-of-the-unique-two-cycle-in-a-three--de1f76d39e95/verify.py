import sympy as s
lam,a,b,u,v=s.symbols('lam a b u v')
J=lambda t:s.Matrix([[0,-2*t,-b],[1,0,0],[0,1,0]])
M=s.simplify(J(u)*J(v))
p=s.expand(M.charpoly(lam).as_expr().subs(u+v,b-1))
assert s.expand(M.charpoly(lam).as_expr()-(lam**3+2*(u+v)*lam**2+4*u*v*lam-b*b))==0
birth=(3*b*b-2*b-1)/4
flip=(5*b*b-6*b+3)/4
poly=lam**3+2*(b-1)*lam**2+4*(b*(b-1)-a)*lam-b*b
assert s.simplify(poly.subs(a,birth)-(lam-1)*(lam**2+(2*b-1)*lam+b*b))==0
assert s.simplify(poly.subs(a,flip)-(lam+1)*(lam**2+(2*b-3)*lam-b*b))==0
assert s.factor(poly.subs(lam,1))==-4*(a-birth)
assert s.factor(poly.subs(lam,-1))==4*(a-flip)
assert s.factor(s.diff(poly,lam).subs({lam:-1,a:flip}))==4-2*b-b*b
NS=(b**4+2*b**3+2*b*b-4*b-1)/4
assert s.factor(NS-birth)==b*(b+2)*(b-1)*(b+1)/4
assert s.simplify((flip-birth)-(b*b-2*b+2)/2)==0
for bv in [s.Rational(1,10),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)]:
 for dt in [s.Rational(1,100),s.Rational(1,10), s.Rational(1,2),s.Rational(3,2), s.Rational(10)]:
  aa=flip.subs(b,bv)+dt
  roots=s.nroots(poly.subs({a:aa,b:bv}),maxsteps=100)
  assert len([x for x in roots if abs(complex(x))>1+1e-8])==2
  aa=birth.subs(b,bv)+dt*(flip-birth).subs(b,bv)/(dt+2)
  roots=s.nroots(poly.subs({a:aa,b:bv}),maxsteps=100)
  assert len([x for x in roots if abs(complex(x))>1+1e-8])==1
  d=s.sqrt(4*aa-3*bv*bv+2*bv+1)
  uv=(bv-1+d)/2; vv=(bv-1-d)/2
  F=lambda P:s.Matrix([aa-P[1]**2-bv*P[2],P[0],P[1]])
  P=s.Matrix([uv,vv,uv]);Q=s.Matrix([vv,uv,vv]);assert s.simplify(F(P)-Q)==s.zeros(3,1)
  assert s.simplify(F(Q)-P)==s.zeros(3,1)
print('SYMBOLIC_AND_NUMERIC_CHECKS_PASS',M)
