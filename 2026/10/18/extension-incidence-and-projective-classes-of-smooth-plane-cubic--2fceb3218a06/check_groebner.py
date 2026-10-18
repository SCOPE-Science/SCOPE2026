#!/usr/bin/env python3
"""Independent geometric-smoothness and extension-census check using SymPy.

Dependency: sympy>=1.12. Each affine Jacobian ideal is checked by its Groebner basis.
"""
from collections import Counter
from itertools import product
import json
import sympy as S
X,Y,Z=S.symbols('X Y Z')
mono=[X**a*Y**b*Z**(3-a-b) for a in range(4) for b in range(4-a)]
partials=[[S.diff(f,w) for f in mono] for w in (X,Y,Z)]
points=[(x,y,z) for x,y,z in product((0,1),repeat=3) if x+y+z]
# Construct evaluation masks independently from symbolic forms.
valuemask=[sum(1<<j for j,f in enumerate(mono) if f.subs({X:p[0],Y:p[1],Z:p[2]})%2)
           for p in points]

def smooth(mask):
 f=sum(mono[i] for i in range(10) if mask>>i&1)
 g=[sum(partials[j][i] for i in range(10) if mask>>i&1) for j in range(3)]
 for variables,unit in [((X,Y),Z),((X,Z),Y),((Y,Z),X)]:
  B=S.groebner([(f if j==0 else g[j-1]).subs(unit,1) for j in range(4)],
               *variables,order='lex',modulus=2)
  if len(B.polys)!=1 or B.polys[0].as_expr()!=1:return False
 return True

def run():
 sm={f for f in range(1,1024) if smooth(f)}
 ps={tuple(sorted((a,b,a^b))) for a in sm for b in sm if a<b and a^b in sm}
 ext=Counter(); base=Counter(); bi=Counter()
 for p in ps:
  e=sum(h not in p and all(h^f in sm for f in p) for h in sm)//4
  r=sum(not (p[0]&M).bit_count()%2 and not (p[1]&M).bit_count()%2 for M in valuemask)
  ext[e]+=1;base[r]+=1;bi[e,r]+=1
 out={'smooth_forms':len(sm),'pencils':len(ps),'extensions':dict(sorted(ext.items())),
      'base':dict(sorted(base.items())),'joint':[{'extensions':e,'base_points':r,'count':n} for (e,r),n in sorted(bi.items())],
      'nets':sum(e*n for e,n in ext.items())//7}
 print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':run()
