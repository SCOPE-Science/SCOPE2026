"""Second verification: Groebner elimination, no finite extension bounds."""
import sympy as sp
from itertools import product
from collections import Counter
from time import monotonic
x,y,z=sp.symbols('x y z')
mon=[x**3,x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y**3,y*y*z,y*z*z,z**3]
P=[]
for v in product(range(3),repeat=3):
 if v != (0,0,0):
  s=next(q for q in v if q)
  t=tuple(q*s%3 for q in v)
  if t not in P:P.append(t)
assert len(P)==13
mat=[[int(m.subs({x:v[0],y:v[1],z:v[2]}))%3 for m in mon] for v in P]
LM=[]
for a in P:
 LM.append(sum(1<<i for i,v in enumerate(P) if sum(w*u for w,u in zip(a,v))%3==0))
CH=[]
for a,b,c in ((x,y,z),(x,z,y),(y,z,x)):
 CH.append((a,b,[sp.Poly(m.subs(c,1),a,b,modulus=3) for m in mon]))

def smooth(c):
 for a,b,ms in CH:
  f=sum((int(t)*m for t,m in zip(c,ms) if t),sp.Poly(0,a,b,modulus=3))
  if list(sp.groebner([f,f.diff(a),f.diff(b)],a,b,modulus=3)) != [sp.Integer(1)]:return False
 return True
start=monotonic();nblocking=nsmooth=0;nb=Counter();supports=Counter()
for c in product(range(3), repeat=10):
 lead=next((t for t in c if t),0)
 if lead !=1:continue
 mask=0
 for i,m in enumerate(mat):
  if sum(a*b for a,b in zip(c,m))%3==0:mask|=1<<i
 if not all(mask & L for L in LM):continue
 nblocking+=1
 if smooth(c):
  nsmooth+=1;nb[mask.bit_count()]+=1;supports[mask]+=1
print('GLOBAL_GROEBNER_OK',nblocking,nsmooth,dict(nb),'supports',len(supports),'support multiplicity',sorted(set(supports.values())),flush=True)
assert (nblocking,nsmooth)==(4940,936)
assert dict(nb)=={6:936}
assert len(supports)==234 and set(supports.values())=={4}

print("VERIFY_GLOBAL_GROEBNER_OK")
