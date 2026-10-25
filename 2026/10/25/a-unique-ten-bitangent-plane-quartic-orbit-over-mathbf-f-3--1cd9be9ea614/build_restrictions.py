from itertools import product
from math import comb
q=3
P=[]
for u in product(range(q),repeat=3):
 if u==(0,0,0): continue
 idx=next(i for i,x in enumerate(u) if x)
 inv=1 if u[idx]==1 else 2
 w=tuple((x*inv)%3 for x in u)
 if w not in P:P.append(w)
P.sort()
mon=[]
for i in range(4,-1,-1):
 for j in range(4-i,-1,-1):
  mon.append((i,j,4-i-j))
assert len(P)==13 and len(mon)==15
# choose u,v as first two points on line
lines=[]
for a in P:
 x=[p for p in P if sum(a[i]*p[i] for i in range(3))%3==0]
 assert len(x)==4
 u,v=x[:2]
 assert u!=v
 lines.append((a,u,v))
# expand substitutions for each monomial as 5 coeffs for s^(4-k) t^k
from itertools import combinations

def polymul(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B): C[i+j]=(C[i+j]+a*b)%3
 return C
rows=[]
for a,u,v in lines:
 mat=[]
 for power in mon:
  coeff=[1]
  for d,e in enumerate(power):
   for r in range(e): coeff=polymul(coeff,[u[d],v[d]])
  mat.append(coeff)
 rows.append(mat)
# square of quadric values, base3 code
sq=set()
for a,b,c in product(range(3),repeat=3):
 if a==b==c==0:continue
 for lam in (1,2):
  v=polymul([a,b,c],[a,b,c]);v=[lam*x%3 for x in v]
  sq.add(sum(x*3**i for i,x in enumerate(v)))
assert len(sq)==26
import json
json.dump({'points':P,'monomials':mon,'lines':lines,'restrictions':rows,'square_codes':sorted(sq)},open('restriction_data.json','w'))
print('monomial_basis',mon)
print('lines',lines)
print('square codes',len(sq))

with open('restrictions.dat','w') as stream:
 for row in rows:
  for k in range(5):
   stream.write(' '.join(str(monrow[k]) for monrow in row)+'\n')
 stream.write(str(len(sq))+'\n')
 stream.write(' '.join(map(str,sorted(sq)))+'\n')
