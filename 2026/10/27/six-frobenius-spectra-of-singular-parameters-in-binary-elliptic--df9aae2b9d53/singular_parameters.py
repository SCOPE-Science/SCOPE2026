#!/usr/bin/env python3
"""Algebraic singular-parameter calculation for finite-field biquadratic pencils."""
import sympy as sp, json, collections, sys
x,y,t=sp.symbols('x y t')
MON=[(i,j) for i in range(3) for j in range(3)]

def ff(a,chart):
 return sum(x**(i if (chart&1)==0 else 2-i)*y**(j if (chart&2)==0 else 2-j) for bit,(i,j) in enumerate(MON) if a>>bit&1)

def trim2(z):
 return sp.Poly(sp.expand(z),t,modulus=2).as_expr()

def eqn(a,b,c):
 f=sp.Poly(ff(a,c)+t*ff(b,c),x,y,t,modulus=2).as_expr()
 gx=sp.diff(f,x);gy=sp.diff(f,y)
 G=sp.groebner([f,gx,gy],x,y,t,order='lex',modulus=2)
 pure=[sp.Poly(g.as_expr(),t,modulus=2) for g in G.polys if not (g.as_expr().free_symbols & {x,y})]
 assert pure
 # this reduced Groebner basis has a unique monic elimination generator
 assert len(pure)==1
 return pure[0]

def alt(a,b,c):
 f=sp.Poly(ff(a,c)+t*ff(b,c),x,y,t,modulus=2).as_expr()
 fx=sp.Poly(sp.diff(f,x),x,y,t,modulus=2).as_expr();fy=sp.Poly(sp.diff(f,y),x,y,t,modulus=2).as_expr()
 # classical Sylvester resultants: first eliminate x using f_y(x), then y with f_x(y).
 g=sp.Poly(sp.resultant(f,fy,x),y,t,modulus=2).as_expr()
 h=sp.resultant(g,fx,y)
 return sp.Poly(h,t,modulus=2)

def radical(g):
 if g.is_zero:return sp.Poly(0,t,modulus=2)
 return sp.prod(p.as_expr() for p,e in sp.factor_list(g,modulus=2)[1])

def lcmchart(a,b,method):
 # union of geometric singular-value sets = lcm of squarefree parts
 factors={}
 for c in range(4):
  eq=method(a,b,c)
  if eq.is_zero:
   raise RuntimeError('unexpected identically zero elimination for a smooth rational pencil')
  for fac,e in sp.factor_list(eq,modulus=2)[1]:
   if fac.degree()>0:factors[str(fac.as_expr())]=fac
 return factors

if __name__=='__main__':
 from pathlib import Path
 inp=json.loads(Path(__file__).with_name('pencil_catalogue.json').read_text())
 out=[]
 for i,entry in enumerate(inp['orbit_representatives']):
  a,b=entry['pencil'][:2]
  GB=lcmchart(a,b,eqn)
  RES=lcmchart(a,b,alt)
  assert set(GB)==set(RES), (i,GB,RES)
  degrees=sorted(f.degree() for f in GB.values())
  assert all(d>1 for d in degrees)
  out.append({'representative':entry['pencil'],'orbit_size':entry['size'],'factors':sorted(GB),'degrees':degrees,'fibre_point_profile':entry['profile']})
  print(i,entry['pencil'],'orbit_size',entry['size'],'singular_Frobenius_degrees',degrees,flush=True)
 dist=collections.Counter()
 for r in out:dist[tuple(r['degrees'])]+=r['orbit_size']
 print('weighted:',sorted(dist.items()))
 print('total',sum(dist.values()))
 assert sum(dist.values())==804
 with open(Path(__file__).with_name('singular_spectra.json'),'w') as f:json.dump({'orbit_representatives':out,'weighted_degree_spectra':[{'degrees':list(k),'pencils':v} for k,v in sorted(dist.items())]},f,indent=2)
