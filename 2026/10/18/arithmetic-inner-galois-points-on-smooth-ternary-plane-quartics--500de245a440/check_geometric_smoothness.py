"""Exact Jacobian tests for the projective-orbit representatives of ternary quartics over F3."""
import json, sympy as S
x,y,z=S.symbols('x y z');vars=(x,y,z)
exps=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
cat=json.load(open('galois_output.json'))
reps=[tuple(t[1]) for li in cat['orbits'].values() for t in li]
assert len(reps)==19
for i,cv in enumerate(reps):
 F=sum(a*x**e[0]*y**e[1]*z**e[2] for a,e in zip(cv,exps))
 partial=[S.diff(F,t) for t in vars]
 for j,w in enumerate(vars):
  other=[t for t in vars if t!=w]
  E=[S.expand(expr.subs(w,1)) for expr in [F]+partial]
  g=S.groebner(E,*other,order='lex',modulus=3)
  assert len(g.polys)==1 and g.polys[0].as_expr()==1,(i,j,g)
print('19 representative quartics x 3 charts: exact Jacobian ideals are unit ideals.')
