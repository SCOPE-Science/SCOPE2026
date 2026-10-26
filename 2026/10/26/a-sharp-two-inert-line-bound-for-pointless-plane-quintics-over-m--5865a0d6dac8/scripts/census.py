import itertools,math, collections,time
from sympy import symbols, groebner
T=time.monotonic()
M=[(a,b,5-a-b) for a in range(6) for b in range(6-a)]
idx={m:i for i,m in enumerate(M)}
pts=list(range(1,8))
# Evaluate coeff bit for a point vector bits 1=x, 2=y,4=z.
def val(c,p):
 r=0
 for k,(a,b,d) in enumerate(M):
  if (c>>k)&1 and ((not a or p&1) and (not b or p&2) and (not d or p&4)):r^=1
 return r

def lin_basis_affine():
 # Solve seven equations E*c = all ones; free vars set independently
 A=[]
 for p in pts:
  mask=sum((1<<j) for j,m in enumerate(M) if ((m[0]==0 or p&1) and (m[1]==0 or p&2) and (m[2]==0 or p&4)))
  A.append(mask | (1<<21))
 piv=[]
 for col in range(21):
  rows=[i for i in range(len(piv),7) if (A[i]>>col)&1]
  if not rows:continue
  r=rows[0];A[len(piv)],A[r]=A[r],A[len(piv)]
  for i in range(7):
   if i!=len(piv) and (A[i]>>col)&1:A[i]^=A[len(piv)]
  piv.append(col)
  if len(piv)==7:break
 assert len(piv)==7
 free=[j for j in range(21) if j not in piv]
 # Augmented RREF with 21 coefficient bits and seven right-hand-side bits.
 A=[]
 for ii,p in enumerate(pts):
  mask=sum((1<<j) for j,m in enumerate(M) if ((m[0]==0 or p&1) and (m[1]==0 or p&2) and (m[2]==0 or p&4)))
  A.append(mask | (1<<(21+ii)))
 for k,col in enumerate(piv):
  r=next(i for i in range(k,7) if (A[i]>>col)&1)
  A[k],A[r]=A[r],A[k]
  for i in range(7):
   if i!=k and (A[i]>>col)&1: A[i]^=A[k]
 def sol(free_mask, rhs_7):
  c=free_mask
  for k,p in enumerate(piv):
   parity=((A[k] & free_mask).bit_count()+ ((A[k]>>21)&rhs_7).bit_count())%2
   if parity:c|=1<<p
  return c
 base=sol(0,127)
 B=[sol(1<<j,0) for j in free]
 assert all(val(base,p)==1 for p in pts)
 assert all(val(b,p)==0 for p in pts for b in B)
 return base,B,piv,free
base,B,piv,free=lin_basis_affine()
# Deterministic enumerated affine space.
# affine elements
forms=[]
for k in range(1<<14):
 c=base
 for j in range(14):
  if (k>>j)&1:c^=B[j]
 forms.append(c)
assert len(set(forms))==16384
# Lines in Fano plane = kernels nonzero linear masks
def parity(x):return x.bit_count()&1
lines={ell:[p for p in pts if parity(p&ell)==0] for ell in pts}
# ordered independent vectors A,B in kernel
pairs={ell:(v[0],v[1]) for ell,v in lines.items()}

def mul_uv(p,q):
 r=0
 for j in range(6):
  if p>>j&1:
   for k in range(6):
    if q>>k&1:
     if j+k<=5:r^=1<<(j+k)
 return r

def pw_lin(mask,n):
 if n==0:return 1
 x=(((mask>>0)&1)<<0)|(((mask>>1)&1)<<1)
 out=1
 for i in range(n):out=mul_uv(out,x)
 return out
# substitute projective point P=u*A+v*B in x,y,z;
line_maps={}
for ell,(A,Bp) in pairs.items():
 maps=[]
 for a,b,c in M:
  px=pw_lin(((A&1)>0)+2*((Bp&1)>0),a)
  py=pw_lin(((A&2)>0)+2*((Bp&2)>0),b)
  pz=pw_lin(((A&4)>0)+2*((Bp&4)>0),c)
  maps.append(mul_uv(mul_uv(px,py),pz))
 line_maps[ell]=maps

def restrict(f, maps):
 r=0
 while f:
  t=f&-f;j=t.bit_length()-1;r^=maps[j];f^=t
 return r
# irreducible iff no irreducible quadratic factor (given no F2 root)
def mul4(x,y):
 z=0
 for i in range(2):
  if y>>i&1:z^=x<<i
 if z&4:z^=0b111
 return z
alpha=2
powers=[1]
for i in range(5):powers.append(mul4(powers[-1],alpha))
def irreducible(r):
 z=0
 for j in range(6):
  if (r>>j)&1:z^=powers[5-j]
 return z!=0
# Line restriction squarefree automatically for pointless degree-five forms
patterns=collections.Counter()
for f in forms:
 k=sum(irreducible(restrict(f,line_maps[ell])) for ell in pts)
 patterns[k]+=1
assert sum(patterns.values())==len(forms)
# action of GL3(F2) via generator matrices (rows linear forms)
# transformation x->X+Y, y->Y, z->Z; swap x/y; swap y/z
mapsgen=[]
for rows in [(3,2,4),(2,1,4),(1,4,2)]:
 imgs=[]
 for a,b,c in M:
  P=[0b001 if (r&1) else 0 for r in rows]
  # trinomial multiplication GF2, polynomial degrees up to 5
  def mult(p,q):
   out={}
   for m,x in p.items():
    for n,y in q.items():
     key=tuple(m[i]+n[i] for i in range(3));out[key]=out.get(key,0)^(x*y)
   return {m:v for m,v in out.items() if v}
  def power(line,n):
   p={(0,0,0):1}
   for _ in range(n):p=mult(p,line)
   return p
  res={(0,0,0):1}
  for r,e in zip(rows,(a,b,c)):
   lin={(int(i==0),int(i==1),int(i==2)):1 for i in range(3) if (r>>i)&1}
   res=mult(res,power(lin,e))
  mask=0
  for m in res:mask^=1<<idx[m]
  imgs.append(mask)
 mapsgen.append(imgs)

def apply_map(f,imgs):
 o=0
 while f:
  t=f&-f; j=t.bit_length()-1; o^=imgs[j]; f^=t
 return o
# orbit traversal on 16384 pointless forms
pool=set(forms)
orbits=[]
while pool:
 rep=min(pool)
 orbit={rep};queue=[rep]
 for f in queue:
  for imgs in mapsgen:
   g=apply_map(f,imgs)
   if g not in orbit:orbit.add(g);queue.append(g)
 assert orbit <= pool
 pool-=orbit
 orbits.append((rep,len(orbit)))
assert sum(sz for _,sz in orbits)==len(forms)
# exact smoothness using Groebner bases in each projective chart
x,y=symbols('u v')
pwr=[(x**i,y**i) for i in range(6)]
def smooth(f):
 for chart in range(3):
  p=0
  for j,(a,b,c) in enumerate(M):
   if f>>j&1:
    e=[a,b,c];e.pop(chart)
    p+=x**e[0]*y**e[1]
  du=p.diff(x);dv=p.diff(y)
  G=groebner([p,du,dv],x,y,order='grevlex',modulus=2)
  # simpler: test unit ideal
  if len(G.polys)!=1 or G.polys[0].as_expr()!=1:return False
 return True
smooth_hist=collections.Counter(); smooth_orbits=[]
for ii,(rep,sz) in enumerate(orbits):
 if smooth(rep):
  k=sum(irreducible(restrict(rep,line_maps[ell])) for ell in pts)
  smooth_hist[k]+=sz
  smooth_orbits.append((rep,sz,k))


from pathlib import Path
import json
certificate=[{'representative_mask': rep, 'orbit_size': sz,
              'geometrically_smooth': rep in {r for r,_,_ in smooth_orbits},
              'irreducible_line_sections': sum(irreducible(restrict(rep,line_maps[e])) for e in pts)}
             for rep,sz in orbits]
expected_path=Path(__file__).resolve().parent.parent/'certificates'/'orbits.json'
assert certificate==json.loads(expected_path.read_text(encoding='utf-8'))
print(json.dumps({'pointless_quintics':len(forms),
                  'total_orbits':len(orbits),
                  'smooth_orbits':len(smooth_orbits),
                  'smooth_quintics':sum(smooth_hist.values()),
                  'smooth_histogram':dict(sorted(smooth_hist.items())),
                  'elapsed_seconds':round(time.monotonic()-T,4)},sort_keys=True))
