from itertools import combinations
from collections import Counter
from sympy import symbols, Poly, groebner
F2=lambda x:x&1
# canonical 7 projective points
points=[(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1) if x+y+z>0]
lines=[sum(1<<i for i,(x,y,z) in enumerate(points) if (a*x+b*y+c*z)%2==0) for a,b,c in points]
lines=sorted(set(lines)); assert len(lines)==7
mons=[(a,b,3-a-b) for a in range(4) for b in range(4-a)]
E=[]
for a,b,c in mons:
 E.append(sum(1<<i for i,(x,y,z) in enumerate(points) if x**a*y**b*z**c==1))

def ev(mask):
 s=0
 for i, e in enumerate(E):
  if (mask>>i)&1:s^=e
 return s

nb={s for s in range(128) if any((s & line)==line for line in lines)}
print('points',points,'lines',lines,'monomials',mons,'rank',len(set(ev(f) for f in range(1024))),'nb',len(nb))
images={tuple(sorted((a,b,a^b))) for a in nb for b in nb if a!=b and (a^b) in nb}
print('image pencils',len(images), Counter(tuple(sorted((7-a.bit_count(),7-b.bit_count(),7-c.bit_count()))) for a,b,c in images))
Epre={s:[] for s in range(128)}
for m in range(1024):Epre[ev(m)].append(m)
pencils=set()
for im in images:
 a,b,c=im
 for f in Epre[a]:
  for g in Epre[b]:
   pencils.add(tuple(sorted((f,g,f^g))))
print('pencils',len(pencils),'members',len(set(m for p in pencils for m in p)))
print('rational basepoints',Counter(7-(ev(p[0])|ev(p[1])|ev(p[2])).bit_count() for p in pencils))
# smoothness exact symbolic groebner
X,Y,Z=symbols('X Y Z')
from sympy import GF
mons_expr=[X**a*Y**b*Z**c for a,b,c in mons]

def smooth(f):
 F=sum(mons_expr[i] for i in range(10) if (f>>i)&1)
 d=[F.diff(x) for x in (X,Y,Z)]
 for keep,others in [(X,(Y,Z)),(Y,(X,Z)),(Z,(X,Y))]:
  dd=[p.subs(keep,1) for p in d]
  if groebner(dd,*others,modulus=2).polys != [Poly(1,*others,modulus=2)]: return False
 return True
mem=sorted(set(m for p in pencils for m in p))
print('checking',len(mem),'members')
smoothmem={m for m in mem if smooth(m)}
print('smooth members',len(smoothmem),'distribution',Counter(sum(int(m in smoothmem) for m in p) for p in pencils))
print('type x smooth distribution',Counter((tuple(sorted(7-ev(m).bit_count() for m in p)),sum(m in smoothmem for m in p)) for p in pencils))

assert len(images)==287 and len(pencils)==18368
assert Counter(7-(ev(p[0])|ev(p[1])|ev(p[2])).bit_count() for p in pencils)=={0:9408,1:8960}
assert Counter(sum(m in smoothmem for m in p) for p in pencils)=={0:4816,1:9408,2:3360,3:784}
