"""Exact Q(phi) certificate for central sections of the regular dodecahedron.

Run with: python check.py

Arithmetic uses a+b*phi, phi=(1+sqrt(5))/2, phi^2=phi+1.
All combinatorial sign decisions use provable rational bounds on phi.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from math import acos, pi, sqrt

ZERO=(0,0); ONE=(1,0); PHI=(0,1); INV=(-1,1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def vecneg(x):return tuple(map(neg,x))
def vecsub(x,y):return tuple(map(sub,x,y))
def dot(x,y):
 out=ZERO
 for xx,yy in zip(x,y):out=add(out,mul(xx,yy))
 return out
def cross(x,y):
 return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
         sub(mul(x[2],y[0]),mul(x[0],y[2])),
         sub(mul(x[0],y[1]),mul(x[1],y[0])))
def det(x,y,z):return dot(x,cross(y,z))

LO=Fraction(161803398874989,100000000000000)
HI=Fraction(161803398874990,100000000000000)
assert (2*LO-1)**2 < 5 < (2*HI-1)**2
assert LO>1 and HI<2
def sign(x):
 a,b=x
 lower=a+b*(LO if b>=0 else HI)
 upper=a+b*(HI if b>=0 else LO)
 if lower>0:return 1
 if upper<0:return -1
 if a==0 and b==0:return 0
 raise ArithmeticError('Insufficient rational precision for algebraic sign: '+str(x))

def vadd(x,y):return tuple(map(add,x,y))
def smul(s,x):return tuple((s*t[0],s*t[1]) for t in x)

V=[]
for s in product((-1,1),repeat=3):V.append(tuple((s_i,0) for s_i in s))
for a,b in product((-1,1),repeat=2):
 V.extend(((ZERO,smul(a,(INV,))[0],smul(b,(PHI,))[0]),
           (smul(a,(INV,))[0],smul(b,(PHI,))[0],ZERO),
           (smul(a,(PHI,))[0],ZERO,smul(b,(INV,))[0])))
assert len(V)==20 and len(set(V))==20
assert all(dot(v,v)==(3,0) for v in V)
D=(8,-4)   # (2/phi)^2=4*(2-phi)
EDGE=[(i,j) for i,j in combinations(range(20),2) if dot(vecsub(V[i],V[j]),vecsub(V[i],V[j]))==D]
assert len(EDGE)==30
assert all(sign(sub(dot(vecsub(V[i],V[j]),vecsub(V[i],V[j])),D))>=0 for i,j in combinations(range(20),2))
reps=[];used=set()
for i in range(20):
 if i in used:continue
 j=V.index(vecneg(V[i]));assert j!=i
 reps.append(V[i]);used.add(i);used.add(j)
assert len(reps)==10
U=reps
assert all(sign(det(U[i],U[j],U[k]))!=0 for i,j,k in combinations(range(10),3))
# Every cell vertex is one of 90 directed intersections of two great circles.
CROSS=[]
for i,j in combinations(range(10),2):
 w=cross(U[i],U[j]);assert sign(dot(w,w))>0
 CROSS.append((w,i,j));CROSS.append((vecneg(w),i,j))
assert len(CROSS)==90

def cell(code):
 s=[1 if (code>>i)&1 else -1 for i in range(10)]
 visible=[]
 for w,i,j in CROSS:
  if all(s[l]*sign(dot(U[l],w))>=0 for l in range(10)):
   constraints=[l for l in range(10) if sign(dot(U[l],w))==0]
   assert constraints==[i,j],(code,i,j,constraints)
   visible.append((w,i,j))
 if len(visible)<3:return None
 normal=(ZERO,ZERO,ZERO)
 for w,_,_ in visible:normal=vadd(normal,w)
 # Strict positivity shows the spherical cell is nonempty and two-dimensional.
 if not all(s[l]*sign(dot(U[l],normal))>0 for l in range(10)):
  raise AssertionError(('degenerate cell',code))
 vsign=[sign(dot(v,normal)) for v in V]
 assert set(vsign)=={-1,1}
 nfaces=sum(vsign[i]!=vsign[j] for i,j in EDGE)
 angles=Counter()
 for w,i,j in visible:
  cc=dot(smul(s[i],U[i]),smul(s[j],U[j]))
  angles[cc]+=1
 return len(visible),nfaces,angles

categories=Counter(); angular_types={}
for code in range(1024):
 d=cell(code)
 if d is None:continue
 sides,nfaces,angles=d
 categories[(nfaces,sides)]+=1
 key=(nfaces,sides)
 cc=tuple(sorted(angles.items()))
 angular_types.setdefault(key,cc)
 assert angular_types[key]==cc,(key,angular_types[key],cc)

A=(1,0)    # dot-product numerators: 1 and sqrt(5)=2*phi-1
B=(-1,2)
assert categories=={(6,6):20,(8,3):60,(10,5):12},categories
assert angular_types[(6,6)]==tuple(sorted(((A,3),(B,3))))
assert angular_types[(8,3)]==tuple(sorted(((neg(A),2),(neg(B),1))))
assert angular_types[(10,5)]==((A,5),)
# Great-circle arrangement independent global count:
# ten great circles, no triple concurrence, implies F=10^2-10+2=92.
assert sum(categories.values())==10*10-10+2
arccos_a=acos(1/3); arccos_b=acos(sqrt(5)/3)
areas={6:2*pi-3*(arccos_a+arccos_b),
       8:2*arccos_a+arccos_b-pi,
       10:2*pi-5*arccos_a}
probs={6:20*areas[6]/(4*pi),8:60*areas[8]/(4*pi),10:12*areas[10]/(4*pi)}
assert all(0<v<1 for v in probs.values())
assert abs(sum(probs.values())-1)<1e-12
for n in (6,8,10):
 print(f'N={n}, number_of_chambers={categories[(n,{6:6,8:3,10:5}[n])]}, '
       f'area_per_chamber={areas[n]:.15f}, probability={probs[n]:.15f}')
print('EXACT_ALGEBRAIC_ARRANGEMENT_CERTIFICATE_PASSED')
