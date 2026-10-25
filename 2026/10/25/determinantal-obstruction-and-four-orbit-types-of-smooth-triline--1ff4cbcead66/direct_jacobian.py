"""Independent projective-chart Jacobian test for selected trilinear complete intersections over F2."""
import itertools
from sympy import symbols,Poly,groebner
u,v,w=symbols('u v w')
REPS=[(22,129),(22,131),(22,139),(24,107)]

def affine(f,chart):
 ans=0
 for i,j,k in itertools.product(range(2),repeat=3):
  if f>>(4*i+2*j+k)&1:
   mon=1
   for exponent,t,choice in zip((i,j,k),(u,v,w),chart):
    mon*= t if exponent==choice else 1
   ans+=mon
 return Poly(ans,u,v,w,modulus=2).as_expr()

def smooth(f,g):
 for chart in itertools.product(range(2),repeat=3):
  a=affine(f,chart);b=affine(g,chart)
  aa=[Poly(a.diff(t),u,v,w,modulus=2).as_expr() for t in (u,v,w)]
  bb=[Poly(b.diff(t),u,v,w,modulus=2).as_expr() for t in (u,v,w)]
  ideals=[a,b]+[aa[i]*bb[j]-aa[j]*bb[i] for i,j in [(0,1),(0,2),(1,2)]]
  G=groebner(ideals,u,v,w,modulus=2,order='lex')
  if not (len(G.polys)==1 and G.polys[0].is_one):
   return False,chart,[str(p.as_expr()) for p in G.polys]
 return True,None,None

if __name__=='__main__':
 for f,g in REPS:
  ok,ch,other=smooth(f,g)
  print(f,g,'SMOOTH' if ok else 'SINGULAR',ch,other)
  assert ok
