import itertools,collections,functools
from sympy import symbols,Poly,groebner
u,v=symbols('u v')
# 2x2x2 F as coefficients; matrices Fz0 and Fz1, each bilinear in x,y
# compute resultant B=Fz0 Gz1+Fz1 Gz0 by bit integer monomials 0..8, i*3+j coefficient x1^i y1^j in homogeneous bidegree2

def mul(a,b):
 out=0
 for ij in range(4):
  if a>>ij&1:
   for kl in range(4):
    if b>>kl&1:
     i,j=ij//2,ij%2;k,l=kl//2,kl%2
     out ^=1<<((i+k)*3+j+l)
 return out

def slices(f):
 a=b=0
 for i,j in itertools.product(range(2),repeat=2):
  a |= ((f>>(4*i+2*j))&1)<<(2*i+j)
  b |= ((f>>(4*i+2*j+1))&1)<<(2*i+j)
 return a,b

slices=[slices(f) for f in range(256)]
def res(f,g):
 a,b=slices[f];c,d=slices[g]
 return mul(a,d)^mul(b,c)

# smooth biquadratic via jacobian ideals in 4 charts
powers=[[(2-i,i,2-j,j) for j in range(3)] for i in range(3)]
Bsm={}
for n in range(1,512):
 yes=True
 for ax,ay in itertools.product(range(2),repeat=2):
  B=0
  for i,j in itertools.product(range(3),repeat=2):
   if n>>(i*3+j)&1:
    B+=u**(i if ax==0 else 2-i)*v**(j if ay==0 else 2-j)
  fx=Poly(B.diff(u),u,v,modulus=2).as_expr();fy=Poly(B.diff(v),u,v,modulus=2).as_expr()
  gb=groebner([B,fx,fy],u,v,order='lex',modulus=2)
  if not (len(gb.polys)==1 and gb.polys[0].is_one):yes=False;break
 Bsm[n]=yes
print('smooth B count',sum(Bsm.values()),flush=True)
S=[]
for f in range(1,256):
 for g in range(f+1,256):
  h=f^g
  if g>h:continue
  R=res(f,g)
  if Bsm.get(R,False):S.append((f,g,h,R))
print('total pencils',len(S),'R counts',collections.Counter(R for f,g,h,R in S).most_common(10),flush=True)
# rational point profiles
pts=[]
for x,y,z in itertools.product(((1,0),(0,1),(1,1)),repeat=3):
 mask=0
 for i,j,k in itertools.product(range(2),repeat=3):
  if x[i]&y[j]&z[k]:mask|=1<<(4*i+2*j+k)
 pts.append(mask)

def pt_count(f,g):return sum(((f&p).bit_count()%2==0) and ((g&p).bit_count()%2==0) for p in pts)
print('point counts',collections.Counter(pt_count(f,g) for f,g,h,R in S),flush=True)
# Group generators transformations dimensions and axes swaps, full group for orbit propagation
GL=[]
for a,b,c,d in itertools.product(range(2),repeat=4):
 if a*d^b*c:GL.append(((a,b),(c,d)))
E=((1,0),(0,1))
transform=[]
for mats in itertools.product(GL,repeat=3):
 for perm in itertools.permutations(range(3)):
  cols=[]
  for ijk in itertools.product(range(2),repeat=3):
   out=0
   for abc in itertools.product(range(2),repeat=3):
    t=1
    for axis in range(3):t &= mats[axis][abc[axis]][ijk[perm[axis]]]
    if t:out|=1<<(abc[0]*4+abc[1]*2+abc[2])
   cols.append(out)
  transform.append(tuple(cols))
assert len(transform)==1296

def action(F,trans):
 o=0
 for i in range(8):
  if F>>i&1:o^=trans[i]
 return o

def canon(a,b):return tuple(sorted([a,b,a^b]))
Ss=set(canon(f,g) for f,g,h,R in S)
seen=set();orb=[]
for p in sorted(Ss):
 if p in seen:continue
 O=set()
 for T in transform:
  a,b=p[:2];O.add(canon(action(a,T),action(b,T)))
 assert O<=Ss, ('not invariant',p,len(O-Ss))
 seen |= O
 orb.append((p,len(O),pt_count(*p[:2])))
print('orbits',len(orb), 'sum',len(seen));print('orbit categories',collections.Counter((sz,npt) for p,sz,npt in orb));print('reprs',orb,flush=True)
