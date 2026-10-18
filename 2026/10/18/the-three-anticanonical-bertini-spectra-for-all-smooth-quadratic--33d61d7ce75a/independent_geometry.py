"""Exact characteristic-two Jacobian tests of three intersections and their anticanonical sections."""
import sympy as s
from itertools import combinations
from collections import Counter
X=s.symbols('x0:5')
E=list(combinations(range(5),2))
def q(m):
 return sum(((m>>i)&1)*X[i]**2 for i in range(5))+sum(((m>>(5+k))&1)*X[i]*X[j] for k,(i,j) in enumerate(E))
def rational(f,x):
 return sum(int(t.as_coeff_Mul()[0]) for t in []) if False else int(s.Poly(f,*X).eval({X[i]:(x>>i)&1 for i in range(5)}))%2
def rank_test(fs,variables):
 for pivot in variables:
  vs=[x for x in variables if x!=pivot]
  exprs=[s.Poly(s.expand(f.subs({pivot:1})),*vs,modulus=2).as_expr() for f in fs]
  mat=[[s.diff(f,v) for v in vs] for f in exprs]
  minors=[s.expand(mat[0][i]*mat[1][j]-mat[0][j]*mat[1][i]) for i,j in combinations(range(len(vs)),2)]
  gb=s.groebner(exprs+minors,*vs,modulus=2)
  if not(len(gb.polys)==1 and gb.polys[0].is_one):return False
 return True
if __name__=='__main__':
 for a,b in [(4144,778),(4144,792),(4144,793)]:
  print('surface',a,b,'smooth',rank_test([q(a),q(b)],list(X)),flush=True)
  pts=[x for x in range(1,32) if not rational(q(a),x) and not rational(q(b),x)]
  ln=sum(all(u in pts for u in (i,j,i^j)) for i in range(1,32) for j in range(i+1,32))//3
  print('rational_points',len(pts),'rational_lines',ln,flush=True)
