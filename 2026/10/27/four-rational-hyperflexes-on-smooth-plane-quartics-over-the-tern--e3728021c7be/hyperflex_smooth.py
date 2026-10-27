import json,sympy as s
M=json.load(open('hyperflex_flags.json'))['monomials']
orbs=json.load(open('hyperflex_orbits.json'))
X=s.symbols('X Y Z')
from time import time
for i,o in enumerate(orbs):
 code=o['rep'];c=[]
 for k in range(15):c.append(code%3);code//=3
 F=sum(int(v)*X[0]**m[0]*X[1]**m[1]*X[2]**m[2] for m,v in zip(M,c))
 D=[s.diff(F,x) for x in X]
 info=[]
 for j in range(3):
  vv=[x for k,x in enumerate(X) if k!=j]
  gb=s.groebner([u.subs(X[j],1) for u in D],*vv,modulus=3,order='lex')
  info.append(all(g.as_expr()==1 for g in gb.polys))
 print(i,o['rep'],o['size'],info,'SMOOTH' if all(info) else 'SINGULAR',F,flush=True)
