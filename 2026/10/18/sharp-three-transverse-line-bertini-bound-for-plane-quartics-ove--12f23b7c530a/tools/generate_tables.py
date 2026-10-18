from pathlib import Path
from itertools import product
import json, sympy as sp
x=sp.symbols('x')
monos=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
lines=[]
for a,b,c in product(range(3),repeat=3):
 if not (a or b or c): continue
 first=next(z for z in (a,b,c) if z)
 v=tuple(z*pow(first,-1,3)%3 for z in (a,b,c))
 if v not in lines:lines.append(v)
lines.sort()
from math import comb
mat=[]
for L in lines:
 pivot=next(i for i,z in enumerate(L) if z)
 others=[i for i in range(3) if i!=pivot]
 basis=[[0,0,0] for _ in range(2)]
 for j,idx in enumerate(others):
  basis[j][idx]=1
  basis[j][pivot]=(-L[idx]*pow(L[pivot],-1,3))%3
 basis=[tuple(v) for v in basis]
 row=[]
 for mono in monos:
  poly=[1,0,0,0,0]
  deg=0
  for ix,ex in enumerate(mono):
   for _ in range(ex):
    a,b=basis[0][ix],basis[1][ix]
    new=[0]*5
    for i in range(deg+1):
     new[i]=(new[i]+a*poly[i])%3
     new[i+1]=(new[i+1]+b*poly[i])%3
    poly=new;deg+=1
  row.append(poly)
 mat.append(row)
good=[]
for coeff in product(range(3),repeat=5):
 # coefficient = c0 u^4 + c1 u^3v +...
 if coeff==(0,)*5: good.append(0);continue
 first=next(i for i,c in enumerate(coeff) if c)
 if first>=2:good.append(0);continue
 p=sp.Poly(sum(coeff[r]*x**(4-r) for r in range(5)),x,modulus=3)
 good.append(1 if sp.gcd(p,p.diff()).degree()==0 else 0)
assert len(good)==243
# encode order c0 lower index trit
out={'monos':monos,'lines':lines,'mat':mat,'good':good}
open(Path(__file__).resolve().parent.parent/'data/quartic_tab.json','w').write(json.dumps(out))
print('monos',monos,'lines',lines,'separable',sum(good))
