"""Independent orbit certification for smooth binary biquadratics over F2."""
import itertools, collections
from sympy import symbols, Poly, groebner
u,v=symbols('u v')
GL=[((a,b),(c,d)) for a,b,c,d in itertools.product(range(2), repeat=4) if (a*d ^ b*c)==1]
Bsm={}
for B in range(1,512):
 ok=True
 for chart in itertools.product(range(2),repeat=2):
  f=sum(u**(i if chart[0]==0 else 2-i)*v**(j if chart[1]==0 else 2-j) for i,j in itertools.product(range(3),repeat=2) if B>>(3*i+j)&1)
  jac=[f,Poly(f.diff(u),u,v,modulus=2).as_expr(),Poly(f.diff(v),u,v,modulus=2).as_expr()]
  gb=groebner(jac,u,v,modulus=2)
  if not (len(gb.polys)==1 and gb.polys[0].is_one):ok=False;break
 Bsm[B]=ok

# coefficient of homogeneous biquadratic (y1-exponent j, x1-exponent i).
# use literal degree two coefficient transformation of GL2 matrices

def square_product(i,j,A):
 # (a x0+b x1)^(2-i) * (c x0+d x1)^i modulo 2
 a,b=A[0];c,d=A[1]
 p=[[1,0,0],[a,b,0],[a,b,0]] # not used
 v=[1,0,0]
 for L in ([a,b],)*(2-i)+([c,d],)*i:
  w=[0,0,0]
  for k in range(3):
   if v[k]:
    if k<2:w[k]^=L[0];w[k+1]^=L[1]
  v=w
 return v

trans=[]
for A,D in itertools.product(GL,repeat=2):
 for swap in [False,True]:
  mon=[]
  for i,j in itertools.product(range(3),repeat=2):
   polyx=square_product(i,2-i,A);polyy=square_product(j,2-j,D)
   out=0
   for k,l in itertools.product(range(3),repeat=2):
    if polyx[k]&polyy[l]:
     if swap:out^=1<<(3*l+k)
     else:out^=1<<(3*k+l)
   mon.append(out)
  trans.append(mon)
assert len(trans)==72

def act(f,t):
 o=0
 for i in range(9):
  if f>>i&1:o^=t[i]
 return o

S={b for b,v in Bsm.items() if v}
seen=set();ors=[]
for b in sorted(S):
 if b in seen:continue
 O={act(b,t) for t in trans}
 assert O<=S,('not invariance',b,O-S)
 seen|=O;ors.append((b,len(O)))
print('total',len(S),'orbits',ors)
