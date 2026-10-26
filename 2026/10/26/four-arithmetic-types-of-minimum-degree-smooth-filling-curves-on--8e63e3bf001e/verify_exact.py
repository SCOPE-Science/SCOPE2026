# Exact finite-field enumeration of minimal smooth filling curves.
from itertools import product,combinations
from collections import Counter
import time
A,B=3,4
points=((1,0),(1,1),(0,1))
mons=[(i,j) for i in range(A+1) for j in range(B+1)]
# On rational points, direct homogeneous evaluation
pows=lambda z,k: (1 if k==0 else z)
def evalmon(i,j,p,q):
 x0,x1=p; y0,y1=q
 return pows(x0,A-i)*pows(x1,i)*pows(y0,B-j)*pows(y1,j)
rows=[]
for p in points:
 for q in points:
  rows.append(sum(evalmon(i,j,p,q)<<k for k,(i,j) in enumerate(mons)))
def kernel(rows,N):
 piv={}
 for r in rows:
  while r:
   p=(r&-r).bit_length()-1
   if p in piv:r^=piv[p]
   else:piv[p]=r;break
 basis=[]
 for i in range(N):
  if i in piv:continue
  v=1<<i
  for p in sorted(piv,reverse=True):
   if (piv[p]&v).bit_count()%2:v^=1<<p
  basis.append(v)
 return basis
basis=kernel(rows,len(mons))
assert len(basis)==11 and len(mons)==20 and len(rows)==9
assert all(not (r&b).bit_count()%2 for r in rows for b in basis)
# dehomogeneous local chart uses x=X1/X0 when 0, x=X0/X1 when 1; same for y.
chartmon=[]
for cx,cy in product(range(2),repeat=2):
 chartmon.append([(i if cx==0 else A-i,j if cy==0 else B-j) for i,j in mons])
def poly_int(mask,cx,cy):
 res=0
 for k,(i,j) in enumerate(chartmon[2*cx+cy]):
  if mask>>k&1:res^=1<<(i*8+j)
 return res
# int mask with monomial index i*8+j; polynomial F2 operations
polys=[]
for i in range(1,1<<len(basis)):
 mask=0
 for j,v in enumerate(basis):
  if (i>>j)&1:mask ^= v
 polys.append(mask)
# Local derivative and rational regularity checks
chartcache={}
def chart(mask,cx,cy):
 key=(mask,cx,cy)
 if key not in chartcache:chartcache[key]=poly_int(mask,cx,cy)
 return chartcache[key]
def deriv(p,axis):
 d=0
 while p:
  z=p&-p;p^=z;k=z.bit_length()-1;i,j=divmod(k,8)
  if axis==0 and i%2:d^=1<<((i-1)*8+j)
  if axis==1 and j%2:d^=1<<(i*8+j-1)
 return d
def ev(p,x,y):
 while p:
  z=p&-p;p^=z;k=z.bit_length()-1;i,j=divmod(k,8)
  if (x or not i) and (y or not j):
   # add parity from nonzero 1 terms
   yield 1

def issmooth_rat(mask):
 for p in points:
  x=0 if p==(1,0) or p==(0,1) else 1
  cx=1 if p[0]==0 else 0
  for q in points:
   y=0 if q==(1,0) or q==(0,1) else 1
   cy=1 if q[0]==0 else 0
   f=chart(mask,cx,cy)
   if (sum(ev(deriv(f,0),x,y))%2)==0 and (sum(ev(deriv(f,1),x,y))%2)==0:return False
 return True
rat=[m for m in polys if issmooth_rat(m)]
# Independent rational regularity is also checked for the smooth list below.
assert len(set(polys))==2047
# Groebner lex 2 vars
# leading lex order highest exponent i then j

def unpack(p):
 s=set()
 while p:
  z=p&-p;p^=z;k=z.bit_length()-1;s.add(divmod(k,8))
 return s
def pack(poly):return sum(1<<(8*i+j) for i,j in poly)
def monmul(poly,di,dj):return {(i+di,j+dj) for (i,j) in poly}
def reduce(poly,basis):
 rem=set()
 while poly:
  m=max(poly)
  found=False
  for f in basis:
   a,b=max(f)
   if m[0]>=a and m[1]>=b:
    poly.symmetric_difference_update(monmul(f,m[0]-a,m[1]-b));found=True;break
  if not found:poly.remove(m);rem.add(m)
 return rem
def grob_unit(polys):
 basis=[];pairs=[]
 for p in polys:
  if not p:continue
  q=reduce(unpack(p),basis)
  if not q:continue
  if q=={(0,0)}:return True
  for i in range(len(basis)):pairs.append((i,len(basis)))
  basis.append(q)
 while pairs:
  i,j=pairs.pop(0)
  f,g=basis[i],basis[j]; (a,b),(c,d)=max(f),max(g)
  m,n=max(a,c),max(b,d)
  if (m==a+c and n==b+d):continue # product criterion
  s=monmul(f,m-a,n-b)^monmul(g,m-c,n-d)
  q=reduce(s,basis)
  if not q:continue
  if q=={(0,0)}:return True
  for i in range(len(basis)):pairs.append((i,len(basis)))
  basis.append(q)
 return False

def smooth_geom(mask):
 for cx,cy in product(range(2),repeat=2):
  f=chart(mask,cx,cy)
  if not grob_unit([f,deriv(f,0),deriv(f,1)]):return False
 return True

# In bidegree (3,4), any smooth filling equation restricts on each
# Y-rational fiber to the unique nonzero cubic vanishing at P1(F2).
# Thus all three fiber restrictions are X0^2*X1 + X0*X1^2.
def restrict_y(mask, y0, y1):
    z=[0]*4
    for k,(i,j) in enumerate(mons):
        if mask>>k&1:
            z[i]^=pows(y0,B-j)*pows(y1,j)
    return tuple(z)

allowed=[]
for mask in polys:
    if all(restrict_y(mask,*q)==(0,1,1,0) for q in points):
        allowed.append(mask)
assert len(allowed)==256
smooth_list=[mask for mask in allowed if smooth_geom(mask)]
assert all(issmooth_rat(mask) for mask in smooth_list)
assert len(smooth_list)==66
smooth_set=set(smooth_list)
assert all((a^b) not in smooth_set for i,a in enumerate(smooth_list) for b in smooth_list[i+1:])

# The coordinate-preserving projective group PGL2(F2)^2 has order 36.
matrices=[((a,b),(c,d)) for a,b,c,d in product(range(2),repeat=4) if (a*d^b*c)==1]
assert len(matrices)==6

def mul_set(p,q):
    out=set()
    for i,j in p:
        for k,l in q:
            x=i+k,j+l
            if x in out:out.remove(x)
            else:out.add(x)
    return out

def pow_set(p,k):
    r={(0,0)}
    for _ in range(k):r=mul_set(r,p)
    return r

def form_set(a,b,axis):
    z=set()
    if a:z.add((0,0))
    if b:z.add((1,0) if axis==0 else (0,1))
    return z

def monomial_image(i,j,mx,my):
    x0=form_set(*mx[0],axis=0);x1=form_set(*mx[1],axis=0)
    y0=form_set(*my[0],axis=1);y1=form_set(*my[1],axis=1)
    return mul_set(mul_set(pow_set(x0,A-i),pow_set(x1,i)),mul_set(pow_set(y0,B-j),pow_set(y1,j)))

def transformation(mx,my):
    return [sum(1<<mons.index(v) for v in monomial_image(i,j,mx,my)) for i,j in mons]

def apply(mask,tran):
    z=0
    while mask:
        low=mask&-mask;mask^=low
        z^=tran[low.bit_length()-1]
    return z

actions=[transformation(mx,my) for mx,my in product(matrices,repeat=2)]
assert len(actions)==36
assert all(apply(s,t) in smooth_set for t in actions for s in smooth_set)
classes=[]
remain=set(smooth_set)
while remain:
    representative=min(remain)
    orbit={apply(representative,t) for t in actions}
    assert orbit<=remain
    remain-=orbit
    classes.append((representative,len(orbit)))
assert len(classes)==4 and sorted(sz for _,sz in classes)==[6,6,18,36]
assert sum(sz for _,sz in classes)==66

# Direct finite-field point counting (for arithmetic separation of the classes).
# The polynomials listed are irreducible over F2, for extension degrees 1..4.
moduli={1:0b11,2:0b111,3:0b1011,4:0b10011}
def fmultiply(a,b,n,mod):
    result=0
    while b:
        if b&1:result^=a
        b>>=1;a<<=1
        if a&(1<<n):a^=mod
    return result&((1<<n)-1)
def rational_points_in_extension(mask,n):
    mod=moduli[n]
    field=list(range(1<<n))
    projective=[(1,t) for t in field]+[(0,1)]
    powers={}
    for t in field:
        z=[1]
        for k in range(1,5):z.append(fmultiply(z[-1],t,n,mod))
        powers[t]=z
    support=[(i,j) for k,(i,j) in enumerate(mons) if mask>>k&1]
    result=0
    for (x0,x1),(y0,y1) in product(projective,repeat=2):
        value=0
        for i,j in support:
            x=fmultiply(powers[x0][A-i],powers[x1][i],n,mod)
            y=fmultiply(powers[y0][B-j],powers[y1][j],n,mod)
            value^=fmultiply(x,y,n,mod)
        result+=not value
    return result

import json
from pathlib import Path
print('linear-space-dimension',len(basis))
print('fiber-normalized-candidates',len(allowed))
print('geometrically-smooth-candidates',len(smooth_list))
print('coordinate-orbits',classes)
print('no-all-smooth-pencil',True)
profiles=[]
for mask,orbit_size in classes:
    Ns=[rational_points_in_extension(mask,m) for m in range(1,5)]
    profiles.append({'mask':mask,'orbit_size':orbit_size,'stabilizer_size':36//orbit_size,'N2_to_N16':Ns})
print('profiles',profiles)
Path(__file__).with_name('smooth_masks.txt').write_text(''.join(str(x)+'\n' for x in sorted(smooth_list)),encoding='utf-8')
Path(__file__).with_name('exact_output.json').write_text(json.dumps({'total_bidegree_forms':1<<20,'filling_space_dimension':len(basis),'filling_nonzero':len(polys),'fiber_normalized_candidates':len(allowed),'geometrically_smooth_count':len(smooth_list),'number_of_orbits':len(classes),'profiles':profiles,'smooth_masks':sorted(smooth_list)},sort_keys=True,indent=2)+'\n',encoding='utf-8')
