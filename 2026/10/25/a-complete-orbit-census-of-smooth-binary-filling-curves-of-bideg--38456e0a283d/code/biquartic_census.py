import itertools,json,collections
import sympy as sp
x,y=sp.symbols('x y')
a,b=4,4
monos=[(i,j) for i in range(a+1) for j in range(b+1)]
pts=[(1,0),(0,1),(1,1)]
rows=[]
for X in pts:
 for Y in pts:
  bit=0
  for k,(i,j) in enumerate(monos):
   val=(X[0]**(a-i)*X[1]**i)*(Y[0]**(b-j)*Y[1]**j)
   bit|=(val%2)<<k
  rows.append(bit)
# rref row bitmasks
rref=[];pivs=[]
for row in rows:
 for r,p in zip(rref,pivs):
  if (row>>p)&1:row^=r
 if row:
  p=(row & -row).bit_length()-1
  for j,r in enumerate(rref):
   if (r>>p)&1:rref[j]^=row
  rref.append(row);pivs.append(p)
inds=sorted(range(len(rref)),key=lambda k:pivs[k]);rref=[rref[i] for i in inds];pivs=[pivs[i] for i in inds]
free=[j for j in range(25) if j not in pivs]
basis=[]
for j in free:
 u=1<<j
 for r,p in zip(rref,pivs):
  if (r>>j)&1:u|=1<<p
 assert all((u & row).bit_count()%2==0 for row in rows)
 basis.append(u)
print("basis-dim",len(basis),"rank",len(rref),flush=True)
print('rank',len(rref),'dim',len(basis),'basis',basis,flush=True)

def chart_polys(mask):
 for ix in [0,1]:
  for iy in [0,1]:
   out=0
   for k,(i,j) in enumerate(monos):
    if mask>>k&1:
     xx = i if ix==0 else a-i
     yy = j if iy==0 else b-j
     out+=x**xx*y**yy
   yield (ix,iy,sp.Poly(out,x,y,modulus=2))

def rsmooth(mask):
 for X in pts:
  for Y in pts:
   gx=gy=0
   for k,(i,j) in enumerate(monos):
    if mask>>k&1:
     gx^=(i%2)*(X[0]**(a-i)*X[1]**(i-1) if i else 0)*(Y[0]**(b-j)*Y[1]**j) if X[0] else (a-i)%2*(X[0]**(a-i-1)*X[1]**i if a-i else 0)*(Y[0]**(b-j)*Y[1]**j)
     gy^=(j%2)*(Y[0]**(b-j)*Y[1]**(j-1) if j else 0)*(X[0]**(a-i)*X[1]**i) if Y[0] else (b-j)%2*(Y[0]**(b-j-1)*Y[1]**j if b-j else 0)*(X[0]**(a-i)*X[1]**i)
   if gx%2==0 and gy%2==0:return False
 return True
# Chart-coordinate gradient computation at the nine rational points.
def rsmooth2(mask):
 for ix,X in enumerate([(1,0),(0,1)]):pass
 for X in pts:
  for Y in pts:
   ix=0 if X[0] else 1; iy=0 if Y[0] else 1
   xx=X[1] if ix==0 else X[0];yy=Y[1] if iy==0 else Y[0]
   dx=dy=0
   for k,(i,j) in enumerate(monos):
    if mask>>k&1:
     ex=i if ix==0 else a-i
     ey=j if iy==0 else b-j
     if ex%2 and (xx or ex==1) and (yy or ey==0):dx^=1
     if ey%2 and (yy or ey==1) and (xx or ex==0):dy^=1
   if not(dx or dy):return False
 return True
masks=[]
for v in range(1,1<<len(basis)):
 z=0
 for j,q in enumerate(basis):
  if v>>j&1:z^=q
 masks.append(z)
rr=[m for m in masks if rsmooth2(m)]
print('rational smooth',len(rr),'total',len(masks),flush=True)
assert all(rsmooth2(m)==rsmooth(m) for m in masks)
# matrices all GL2(F2)
GL=[(aa,bb,cc,dd) for aa,bb,cc,dd in itertools.product(range(2),repeat=4) if (aa*dd+bb*cc)%2]
assert len(GL)==6
# poly multiplication masks (exponents x0^a-i x1^i y0^b-j y1^j)
def poly_mul(u,v):
 out=set()
 for k in u:
  for ell in v:
   term=tuple(k[t]+ell[t] for t in range(4))
   if term in out:out.remove(term)
   else:out.add(term)
 return out

def powlin(alpha,beta,n,idx0,idx1):
 q={(0,0,0,0)}
 e=set()
 if alpha:e.add(tuple(1 if i==idx0 else 0 for i in range(4)))
 if beta:e.add(tuple(1 if i==idx1 else 0 for i in range(4)))
 for _ in range(n):q=poly_mul(q,e)
 return q

def action_matrix(A,B):
 a0,b0,c0,d0=A; a1,b1,c1,d1=B
 xp=[powlin(a0,b0,n,0,1) for n in range(a+1)]
 xq=[powlin(c0,d0,n,0,1) for n in range(a+1)]
 yp=[powlin(a1,b1,n,2,3) for n in range(b+1)]
 yq=[powlin(c1,d1,n,2,3) for n in range(b+1)]
 result=[]
 for i,j in monos:
  p=poly_mul(poly_mul(poly_mul(xp[a-i],xq[i]),yp[b-j]),yq[j])
  z=0
  for k,l in enumerate(monos):
   if (a-l[0],l[0],b-l[1],l[1]) in p:z|=1<<k
  result.append(z)
 return result
acts=[action_matrix(A,B) for A in GL for B in GL]
swap=[1<<monos.index((j,i)) for i,j in monos]
acts += [ [sum(swap[k] for k in range(len(monos)) if v>>k&1) for v in act] for act in acts[:]]
assert len(acts)==72
def apply(mask,act):
 z=0
 while mask:
  b=mask & -mask; mask^=b
  z^=act[b.bit_length()-1]
 return z
assert all((apply(u,act)&r).bit_count()%2==0 for act in acts for u in basis for r in rows)
assert all(apply(m,act) in rr for m in rr[:20] for act in acts)
rrs=set(rr)
orbits=[]
while rrs:
 seed=next(iter(rrs)); orb=set(apply(seed,g) for g in acts)
 assert orb<=rrs
 rrs-=orb; orbits.append((seed,sorted(orb)))
print('rational orbits',len(orbits),'sizes',dict(collections.Counter(len(q) for _,q in orbits)),flush=True)
# Check per orbit exact smoothness all 4 charts
def gsmooth(mask):
 for ix,iy,p in chart_polys(mask):
  f=p.as_expr();fx=sp.diff(f,x);fy=sp.diff(f,y)
  gb=sp.groebner([f,fx,fy],x,y,order='lex',modulus=2)
  if not gb.is_zero_dimensional and len(gb.polys)!=1:return False
  if not(len(gb.polys)==1 and gb.polys[0].as_expr()==1):return False
 return True
S=[];statuses=[]
for n,(seed,orb) in enumerate(orbits):
 v=gsmooth(seed);statuses.append((seed,len(orb),v));
 if v:S.extend(orb)
 if n%20==0: print('chk',n,'/',len(orbits),flush=True)
print('FULL',len(S),'ORBIT COUNTS',collections.Counter(k for _,k,v in statuses if v),flush=True)
with open('biquartic_census_output.json','w') as fp:json.dump({'monomials':monos,'basis':basis,'rank':len(rref),'rational_count':len(rr),'geometric_count':len(S),'orbit_counts':dict(collections.Counter(k for _,k,v in statuses if v)),'orbit_reps':[{'mask':m,'size':k,'smooth':v} for m,k,v in statuses],'smooth_masks':sorted(S)},fp)
