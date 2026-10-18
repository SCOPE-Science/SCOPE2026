import sympy as s,re
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
T=__import__('json').load(open(ROOT/'data/quartic_tab.json'))
monos=T['monos']
x,y,z=s.symbols('x y z');xyz=[x,y,z]
ors=[]
for l in open(ROOT/'out/plane_qorbits.txt'):
 if l.startswith('ORBIT'):
  w=l.strip().split();ors.append((int(w[1]),int(w[2]),int(w[3]),int(w[4])))
@lru_cache(None)
def smooth(n):
 d=[n//3**j%3 for j in range(15)]
 F=sum(c*x**m[0]*y**m[1]*z**m[2] for c,m in zip(d,monos))
 for p in range(3):
  others=[xyz[j] for j in range(3) if j!=p]
  f=s.expand(F.subs(xyz[p],1));dy=f.diff(others[0]);dz=f.diff(others[1])
  gb=s.groebner([f,dy,dz],*others,order='grevlex',modulus=3)
  if not (len(gb.polys)==1 and gb.polys[0].is_one):return False
 return True
for t,oid,n,size in ors:
 if t>3:continue
 ok=smooth(n)
 print(t,oid,n,size,'SMOOTH' if ok else 'SINGULAR',flush=True)
