"""Independent evaluation of the seven high-bitangent orbit representatives."""
import json
from itertools import product
from sympy import symbols, Poly, groebner
J=json.load(open('restriction_data.json'))
O=json.load(open('orbit_certificate.json'))
X,Y,Z=symbols('X Y Z')
mon=J['monomials']
assert len(O)==7
assert sum(o['size'] for o in O)==2782
for o in O:
 v=tuple(map(int,o['form']))
 f=sum(c*X**a*Y**b*Z**d for c,(a,b,d) in zip(v,mon))
 r=0;bad=[]
 for a,u,w in J['lines']:
  s,t=symbols('s t')
  expr=f.subs({X:s*u[0]+t*w[0],Y:s*u[1]+t*w[1],Z:s*u[2]+t*w[2]}, simultaneous=True)
  pol=Poly(expr,s,t,modulus=3)
  coeff=[int(pol.coeff_monomial(s**(4-k)*t**k))%3 for k in range(5)]
  sq=any(all((lam*q)%3==e for q,e in zip(
       [A*A,2*A*B,B*B+2*A*C,2*B*C,C*C],coeff))
       for A,B,C in product(range(3),repeat=3) for lam in (1,2) if (A,B,C)!=(0,0,0))
  if sq:r+=1
  else:bad.append(a)
 assert r==o['num_bitangents'],(o,r)
 # The six nonmaximal orbits are singular at [1:0:0].
 if r!=10:
  assert all(int(g.subs({X:1,Y:0,Z:0}))%3==0 for g in [f,f.diff(X),f.diff(Y),f.diff(Z)])
 else:
  for coord,variables in [(X,(Y,Z)),(Y,(X,Z)),(Z,(X,Y))]:
   g=Poly(f.subs(coord,1),*variables,modulus=3).as_expr()
   gb=groebner([g,g.diff(variables[0]),g.diff(variables[1])],*variables,modulus=3)
   assert len(gb.polys)==1 and gb.polys[0].is_one
  assert len(bad)==3 and all(a[0]==0 for a in bad),bad
  points=[]
  for p in J['points']:
   if int(f.subs({X:p[0],Y:p[1],Z:p[2]}))%3==0:points.append(p)
  assert points==[[1,0,0]],points
 print('bitangents',r,'orbit_size',o['size'],'nonsmooth' if r!=10 else 'smooth','nonsquare_lines',bad)
print('independent symbolic restrictions, Jacobian charts, and incidence checks passed')
