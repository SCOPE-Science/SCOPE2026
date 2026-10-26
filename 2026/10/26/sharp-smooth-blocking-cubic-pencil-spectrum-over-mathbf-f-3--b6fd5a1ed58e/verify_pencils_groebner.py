"""Independent exact Groebner-basis test for smooth basepoint-free cubic pencils over F3."""
from itertools import product
from collections import Counter
from time import monotonic
import sympy as sp
x,y,z=sp.symbols('x y z')
MON=[x**3,x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y**3,y*y*z,y*z*z,z**3]
F=(2,0,2,0,0,1,0,1,0,0)
P=[]
for v in product(range(3), repeat=3):
 if v!=(0,0,0):
  a=next(t for t in v if t)
  u=tuple(i*a%3 for i in v)
  if u not in P:P.append(u)
assert len(P)==13
vM=[[int(m.subs({x:v[0],y:v[1],z:v[2]}))%3 for m in MON] for v in P]
B=[j for j,m in enumerate(vM) if sum(t*s for t,s in zip(m,F))%3==0]
assert len(B)==6
mons_chart=[]
for ch in [(x,y,z),(x,z,y),(y,z,x)]:
 a,b,c=ch
 mons_chart.append((a,b,[sp.Poly(m.subs(c,1),a,b,modulus=3) for m in MON]))

def smooth(c):
 for a,b,mons in mons_chart:
  f=sum((int(v)*m for v,m in zip(c,mons) if v),sp.Poly(0,a,b,modulus=3))
  basis=sp.groebner([f,f.diff(a),f.diff(b)],a,b,order='lex',modulus=3)
  if list(basis) != [sp.Integer(1)]: return False
 return True

start=monotonic();ct=Counter();dist=Counter();good=[]
for coeffs in product(range(3),repeat=8):
 G=(0,*coeffs,1)
 if any(sum(a*b for a,b in zip(vM[j],G))%3==0 for j in B):continue
 ct['basefree']+=1
 H=tuple((a+b)%3 for a,b in zip(G,F));J=tuple((a+2*b)%3 for a,b in zip(G,F))
 if not smooth(G):continue
 ct['Gsmooth']+=1
 if not smooth(H) or not smooth(J):continue
 ct['all_smooth']+=1
 counts=sorted(sum(sum(a*b for a,b in zip(m,C))%3==0 for m in vM) for C in (G,H,J))
 dist[tuple(counts)]+=1
 good.append(''.join(map(str,G)))
print('B=',B,'ct=',dict(ct),'dist=',dict(sorted(dist.items())))
print('goodies:',len(good),'min',min(good),'max',max(good))
with open('pencils_groebner_recomputed.txt','w') as f:f.write('\n'.join(sorted(good))+'\n')

assert dict(ct)=={'basefree':864,'Gsmooth':576,'all_smooth':312}
assert dict(dist)=={(1,1,5):24,(1,2,4):132,(1,3,3):42,(2,2,3):114}
print('VERIFY_PENCILS_GROEBNER_OK')
