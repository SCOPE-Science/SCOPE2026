import sympy as s
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
from itertools import product
X=s.symbols('X0 X1 X2'); u,v=s.symbols('u v');p=3
mons=[(a,b,6-a-b) for a in range(7) for b in range(7-a)]
pts=[]
for xx,yy in product(range(3),repeat=2):pts.append((xx,yy,1))
for xx in range(3):pts.append((xx,1,0))
pts.append((1,0,0))
assert len(pts)==13
# row reduce mod3
M=[[pow(P[0],a,3)*pow(P[1],b,3)*pow(P[2],c,3)%3 for a,b,c in mons] for P in pts]
A=[r[:] for r in M];pivot=[];i=0
for j in range(len(mons)):
 where=next((k for k in range(i,len(A)) if A[k][j]),None)
 if where is None:continue
 A[i],A[where]=A[where],A[i]
 inv=pow(A[i][j],-1,3);A[i]=[(w*inv)%3 for w in A[i]]
 for k in range(len(A)):
  if k!=i:
   factor=A[k][j]
   A[k]=[(a-factor*b)%3 for a,b in zip(A[k],A[i])]
 pivot.append(j);i+=1
 if i==len(A):break
free=[j for j in range(len(mons)) if j not in pivot]
basis=[]
for j in free:
 B=[0]*len(mons);B[j]=1
 for i,k in enumerate(pivot):B[k]=(-A[i][j])%3
 basis.append(B)
print('rank',len(pivot),'dim',len(basis))
assert len(basis)==15
jets=[]
for B in basis:
 f=sum(int(B[j])*s.prod(X[k]**e for k,e in enumerate(mons[j])) for j in range(len(mons)))
 jet=[]
 for P in pts:
  pivot_axis=next(k for k in range(3) if P[k]!=0)
  other=[k for k in range(3) if k!=pivot_axis]
  subs={X[pivot_axis]:P[pivot_axis],X[other[0]]:P[other[0]]+u,X[other[1]]:P[other[1]]+v}
  local=s.Poly(s.expand(f.subs(subs)),u,v)
  jet.append([int(local.coeff_monomial(m))%3 for m in [u,v,u**2,u*v,v**2]])
 jets.append(jet)
print('points',pts)
with open(ROOT/'jet_data.json','w') as h:json.dump(dict(mons=mons,pts=pts,basis=basis,jets=jets),h)
arr='{' + ',\n'.join('{' + ','.join('{' + ','.join(map(str,row))+'}' for row in jet)+'}' for jet in jets) + '}'
with open(ROOT/'jet_data.h','w') as h:h.write('static const signed char J[15][13][5] = '+arr+';\n')
