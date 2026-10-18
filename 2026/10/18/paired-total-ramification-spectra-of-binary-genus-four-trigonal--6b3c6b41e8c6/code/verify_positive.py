"""Algebraic geometric smoothness for every projective orbit representative."""
import json
from pathlib import Path
import sympy as sp
x,y=sp.symbols('x y')
obj=json.loads(Path('data/census.json').read_text())
rows=obj['orbit_representatives']
assert len(rows)==252
n=0
for row in rows:
    m=row['mask']
    for ix in (0,1):
        for iy in (0,1):
            expr=sum(x**(3-i if ix else i)*y**(3-j if iy else j)
                     for j in range(4) for i in range(4) if (m>>(4*j+i))&1)
            f=sp.Poly(expr,x,y,modulus=2)
            g=sp.groebner([f,f.diff(x),f.diff(y)],x,y,modulus=2)
            assert len(g.polys)==1 and g.polys[0]==sp.Poly(1,x,y,modulus=2), (m,ix,iy,g)
            n+=1
assert n==1008
print('positive algebraic verification:',n,'Groebner unit ideals across 252 orbits and four charts')
