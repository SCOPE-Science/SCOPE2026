import itertools,json,collections
import sympy as s
from pathlib import Path
pth=Path(__file__).resolve().parent;p=3
qexp=[(2,0),(1,1),(0,2)]
mons=[(a,b) for a in qexp for b in qexp]
pows=[3**i for i in range(9)]
def canon(ds):
 j=next((i for i,x in enumerate(ds) if x%3),None)
 if j is None:return 0
 if ds[j]==2:ds=[(2*x)%3 for x in ds]
 return sum(int(x)*pows[i] for i,x in enumerate(ds))
def digits(v):
 return [(v//x)%3 for x in pows]

def qaction(u,v):
 # transform x0 -> u0*x0+u1*x1, x1 -> v0*x0+v1*x1
 a,b=u;c,d=v
 return [[(a*a)%3,(2*a*b)%3,(b*b)%3],[(a*c)%3,(a*d+b*c)%3,(b*d)%3],[(c*c)%3,(2*c*d)%3,(d*d)%3]]
# for each image of monomial get coeff of new monomial
tr=[]
for mat in [qaction((0,1),(1,0)),qaction((1,1),(0,1)),qaction((2,0),(0,1))]:
 im=[[0]*9 for _ in range(9)]
 for i in range(3):
  for j in range(3):
   for a in range(3):im[3*i+j][3*a+j]=mat[i][a]
 tr.append(im)
tr.append([[int((j//3==i%3) and (j%3==i//3)) for j in range(9)] for i in range(9)])
# re-evaluate swap: transform old monomial i=(a,b) -> new (b,a)

def app(code,m):
 ds=digits(code);b=[0]*9
 for i,v in enumerate(ds):
  if v:
   for j,c in enumerate(m[i]): b[j]=(b[j]+v*c)%3
 return canon(b)
seen=set();orbits=[]
for n in range(1,3**9):
 if n in seen:continue
 ds=digits(n); norm=canon(ds)
 if norm in seen:continue
 que=[norm];seen.add(norm)
 for x in que:
  for m in tr:
   y=app(x,m)
   if y not in seen:seen.add(y);que.append(y)
 orbits.append((min(que),len(que)))
print('ORBIT_COUNT',len(orbits),'FORMS',sum(a[1] for a in orbits),flush=True)
x0,x1,y0,y1=s.symbols('x0 x1 y0 y1');xs=(x0,x1);ys=(y0,y1)
mexp=[xs[0]**a[0]*xs[1]**a[1]*ys[0]**b[0]*ys[1]**b[1] for a,b in mons]

def chart_gb(F,subs):
 gg=[s.expand(s.diff(F,v).subs(subs)) for v in [x0,x1,y0,y1]]
 # add F in Jacobian, although Euler bideg2 char3 invertible ensures F follows derivatives x/y
 vv=[v for v in [x0,x1,y0,y1] if v not in subs]
 gb=s.groebner(gg,*vv,order='grevlex',modulus=3)
 return len(gb.polys)==1 and gb.polys[0].as_expr()==1

def quartic_coeff_discr(ds, direction):
 # direction 'x' discriminant of degree2 in x, polynomial quartic in y
 basis=[y0,y1] if direction=='x' else [x0,x1]
 if direction=='x':A=sum(ds[0*3+j]*ys[0]**qexp[j][0]*ys[1]**qexp[j][1] for j in range(3));B=sum(ds[1*3+j]*ys[0]**qexp[j][0]*ys[1]**qexp[j][1] for j in range(3));C=sum(ds[2*3+j]*ys[0]**qexp[j][0]*ys[1]**qexp[j][1] for j in range(3))
 else:A=sum(ds[i*3+0]*xs[0]**qexp[i][0]*xs[1]**qexp[i][1] for i in range(3));B=sum(ds[i*3+1]*xs[0]**qexp[i][0]*xs[1]**qexp[i][1] for i in range(3));C=sum(ds[i*3+2]*xs[0]**qexp[i][0]*xs[1]**qexp[i][1] for i in range(3))
 D=s.Poly(s.expand(B**2-A*C),*basis,modulus=3)
 # homogeneous factor degrees polynomial in t if leading coefficient at infinity nonzero
 du=s.Poly(s.expand(D.as_expr().subs({basis[0]:1,basis[1]:s.Symbol('t')})),s.Symbol('t'),modulus=3)
 # factor uses x0=1 and x1=t -> infinity x0=0
 f=s.factor_list(du.as_expr(),s.Symbol('t'),modulus=3)[1]
 degs=[]
 for fac,e in f:degs.extend([s.Poly(fac,s.Symbol('t')).degree()]*e)
 degs.extend([1]*(4-du.degree()))
 assert sum(degs)==4,(D,du,degs)
 return tuple(sorted(degs)), str(D.as_expr())
res=[]
for idx,(rep,size) in enumerate(orbits):
 ds=digits(rep);F=sum(ds[i]*mexp[i] for i in range(9))
 ok=all(chart_gb(F,sub) for sub in [{x0:1,y0:1},{x0:1,y1:1},{x1:1,y0:1},{x1:1,y1:1}])
 if ok:
  sx,dx=quartic_coeff_discr(ds,'x');sy,dy=quartic_coeff_discr(ds,'y')
  # Projective rational points
  dirs=[(1,0),(0,1),(1,1),(1,2)]
  N=sum(int(s.expand(F).subs({x0:xx,x1:xy,y0:yx,y1:yy}))%3==0 for xx,xy in dirs for yx,yy in dirs)
 else:sx=sy=dx=dy=None;N=None
 res.append({'mask':rep,'size':size,'smooth':ok,'N':N,'branches_x':sx,'branches_y':sy,'disc_x':dx,'disc_y':dy,'equation':str(F)})
(pth/'biquad3_results.json').write_text(json.dumps(res,indent=2))
print('SMOOTH',sum(r['smooth'] for r in res),'FORMS',sum(r['size'] for r in res if r['smooth']))
for name in ['N','branches_x','branches_y']:
 print(name,collections.Counter({str(k):sum(r['size'] for r in res if r['smooth'] and str(r[name])==k) for k in set(str(r[name]) for r in res if r['smooth'])}))
joint=collections.Counter()
for r in res:
 if r['smooth']:joint[(r['branches_x'],r['branches_y'])]+=r['size']
print('JOINT', sorted((str(k),v) for k,v in joint.items()))
print('ORBIT JOINT',collections.Counter((r['branches_x'],r['branches_y']) for r in res if r['smooth']))
