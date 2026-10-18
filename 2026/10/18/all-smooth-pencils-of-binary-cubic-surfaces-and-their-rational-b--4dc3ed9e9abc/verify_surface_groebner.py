#!/usr/bin/env python3
"""Independently check geometric smoothness of 36 representative smooth cubic surfaces."""
from sympy import symbols, groebner, Poly
import csv
from pathlib import Path
x=symbols('x0:4')
mon=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):
   mon.append((a,b,c,3-a-b-c))
assert len(mon)==20
with open(str(Path(__file__).resolve().parent/'cubic_surface_orbits.tsv')) as f: rows=list(csv.DictReader(f,delimiter='\t'))
for k,row in enumerate(rows):
 mask=int(row['representative']);
 F=sum((x[0]**a*x[1]**b*x[2]**c*x[3]**d) for i,(a,b,c,d) in enumerate(mon) if mask>>i&1)
 for i in range(4):
  js=[j for j in range(4) if i!=j]; f=F.subs(x[i],1)
  deriv=[f.diff(x[j]) for j in js]
  G=groebner([f]+deriv,*[x[j] for j in js],order='grevlex',modulus=2)
  assert G.is_zero_dimensional is False or G.polys[0].as_expr()==1, (mask,i,G)
  assert len(G.polys)==1 and G.polys[0].as_expr()==1, (mask,i,G)
print('Independently checked 36 orbit representatives on all four affine charts (144 Groebner unit ideals).')
