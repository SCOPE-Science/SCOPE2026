# Derived from exact Fano-plane substitutions, sample only.
from sympy import symbols
from itertools import product
X,Y,Z=symbols('X Y Z'); vv=[X,Y,Z]
mon=[X**a*Y**b*Z**(3-a-b) for a in range(3,-1,-1) for b in range(3-a,-1,-1)]
mi={m:i for i,m in enumerate(mon)}
net={100,421,449,523,623,942,970}
transitive=set()
ct=0
for rs in product(range(8),repeat=3):
 rows=[[((rs[i]>>j)&1) for j in range(3)] for i in range(3)]
 A=[row[:] for row in rows];rank=0
 for j in range(3):
  k=next((i for i in range(rank,3) if A[i][j]),None)
  if k is not None:
   A[k],A[rank]=A[rank],A[k]
   for i in range(3):
    if i!=rank and A[i][j]:A[i]=[u^v for u,v in zip(A[i],A[rank])]
   rank+=1
 if rank!=3:continue
 subs={vv[i]:sum(rows[i][j]*vv[j] for j in range(3)) for i in range(3)}
 def act(mask):
  e=sum(mon[j] for j in range(10) if mask>>j&1).subs(subs,simultaneous=True).expand()
  from sympy import Poly
  poly=Poly(e,*vv,modulus=2)
  return sum(1<<mi[X**a*Y**b*Z**c] for (a,b,c),v in poly.terms() if int(v)%2)
 if {act(m) for m in net}==net:
  ct+=1;transitive.add(act(100))
print(ct,len(transitive), sorted(transitive))
