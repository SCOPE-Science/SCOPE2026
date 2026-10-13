from fractions import Fraction
from itertools import combinations
Q=Fraction
# Gaussian exact rationals tuple fractions
zero=(Q(0),Q(0));one=(Q(1),Q(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
 d=b[0]*b[0]+b[1]*b[1];return ((a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)
i=(Q(0),Q(1))
roots=[one,(Q(-1),Q(0)),i,(Q(0),Q(-1))]
p=[];labs=[]
for j in range(4):
 x=[zero]*4;x[j]=one;p.append(x);labs.append(('axis',j))
for a,b in combinations(range(4),2):
 for r,u in enumerate(roots):
  x=[zero]*4;x[a]=one;x[b]=u;p.append(x);labs.append(('edge',a,b,r))
def key(a,b):
 w=[sub(mul(a[i],b[j]),mul(a[j],b[i])) for i,j in combinations(range(4),2)]
 first=next(x for x in w if x!=zero)
 return tuple(div(x,first) for x in w)
lines={}
for a,b in combinations(range(28),2):lines.setdefault(key(p[a],p[b]),set()).update((a,b))
r={}
for line in lines.values():r[len(line)]=r.get(len(line),0)+1
print('line size counts',r)
from collections import Counter
for size in sorted(r,reverse=True):
 if size<3:continue
 sets=[z for z in lines.values() if len(z)==size]
 print('size',size,'count',len(sets),'axis dist',Counter(sum(z<4 for z in x) for x in sets))
 print('examples',[tuple(labs[z] for z in sorted(q)) for q in sets[:4]])
print('point incidence count by type',Counter((labs[z][0],sum(len(line)>=3 and z in line for line in lines.values())) for z in range(28)))
# plane intersections? compute full incidence linear projective planes from triples independent, linear normal
# Fixed planes of monomial reflections associated to 28 centers: for e_i axis plane Xi=0; for center e_a + u e_b, plane X_b + u X_a=0. Note automorphism sign as described.
planes=[]
for lab in labs:
 v=[zero]*4
 if lab[0]=='axis':v[lab[1]]=one
 else:_,a,b,r=lab;v[a]=roots[r];v[b]=one
 planes.append(v)
def ker2(v,w):
 M=[[v[z] for z in range(4)],[w[z] for z in range(4)]]
 piv=[]; row=0
 for col in range(4):
  q=next((j for j in range(row,2) if M[j][col]!=zero),None)
  if q is None: continue
  M[row],M[q]=M[q],M[row]
  a=M[row][col];M[row]=[div(x,a) for x in M[row]]
  for j in range(2):
   if j==row:continue
   z=M[j][col];M[j]=[sub(M[j][k],mul(z,M[row][k])) for k in range(4)]
  piv.append(col);row+=1
  if row==2:break
 free=[col for col in range(4) if col not in piv]
 out=[]
 for f in free:
  x=[zero]*4;x[f]=one
  for rr,col in enumerate(piv):x[col]=sub(zero,M[rr][f])
  out.append(x)
 return out
from math import comb
def poly_f(s,t):
 co=[zero]*5
 for a,b in zip(s,t):
  for k in range(5):
   a4=one;b4=one
   for _ in range(4-k):a4=mul(a4,a)
   for _ in range(k):b4=mul(b4,b)
   co[k]=add(co[k],mul((Q(comb(4,k)),Q(0)),mul(a4,b4)))
 return co
from sympy import Symbol,I,Poly
z=Symbol('z')
def to_sym(v):return s.Rational(v[0].numerator,v[0].denominator)+I*s.Rational(v[1].numerator,v[1].denominator)
import sympy as s
cases=Counter();samples={};special=[]
for j,k in combinations(range(28),2):
 basis=ker2(planes[j],planes[k]);coeff=poly_f(*basis)
 pp=s.Poly(sum(to_sym(v)*z**i for i,v in enumerate(coeff)),z,extension=I)
 deg=pp.degree(); d=s.degree(s.gcd(pp,pp.diff())) if not pp.is_zero else 9
 # if lead term 0, root at infinity of multiplicity 4-degree; repeated iff 4-degree>=2
 bad=max(0,4-deg-1)+(d if d else 0)
 cases[(deg,d,bad)]+=1
 samples.setdefault((deg,d,bad),(j,k,coeff))
 if bad:special.append((j,k,deg,d))
print('line quartic repeated status',cases)
for case, count in cases.items(): print(case, count,'example labels',tuple(labs[q] for q in samples[case][:2]), 'binary coeff',samples[case][2]);

assert Counter(len(z) for z in lines.values()) == {6: 6, 3: 64, 2: 96}
assert sum(cases.values()) == 378
assert all(v[2] == 0 for v in cases), cases
dx = s.symbols('d', integer=True, positive=True)
H=4+6*dx
flat_pair_weight=6*s.binomial(dx+2,2)+4*dx**2*s.binomial(3,2)+(12*dx+3*dx**2)
assert s.simplify(flat_pair_weight-s.binomial(H,2)) == 0
points=6*dx+4*dx**3+12*dx**2+3*dx**3
delta=6*dx*s.binomial(dx+2,2)+4*dx**3*3+12*dx**2+3*dx**3
genus=s.expand(H*(dx-1)*(dx-2)/2)
pa=s.expand(1+H*dx*(H+dx-4)/2)
assert s.simplify(delta-(18*dx**3+21*dx**2+6*dx)) == 0
assert s.simplify(genus+delta-H+1-pa) == 0
assert s.simplify(points-(7*dx**3+12*dx**2+6*dx)) == 0
assert [int(points.subs(dx,k)) for k in (4,6,8)] == [664,1980,4400]
print('REFLECTION_DIVISOR_VERIFY_OK')
