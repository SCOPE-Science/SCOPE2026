import sympy as s,itertools,collections
from pathlib import Path
q=7
x,y,z,t=s.symbols('x y z t')
models=[]
for line in (Path(__file__).resolve().parents[1] / 'data' / 'q7_models.txt').read_text().splitlines():
 if line.strip():
  group,txt=line.split('|')
  F=s.expand(s.sympify(txt.replace('^','**')))
  models.append((group,F))
lines=[]
for tup in itertools.product(range(q),repeat=3):
 if not any(tup):continue
 j=next(i for i,a in enumerate(tup) if a)
 tmp=tuple(a*pow(tup[j],-1,q)%q for a in tup)
 if tmp not in lines:lines.append(tmp)
lines.sort()

def basis(L):
 a,b,c=L
 j=next(i for i,u in enumerate(L) if u)
 pts=[]
 for i in range(3):
  if i==j:continue
  t=[0]*3;t[i]=1;t[j]=(-L[i]*pow(L[j],-1,q))%q
  pts.append(t)
 return pts

def bitangent(F,L):
 A,B=basis(L)
 f=s.Poly(s.expand(F.subs({x:A[0]+B[0]*t,y:A[1]+B[1]*t,z:A[2]+B[2]*t},simultaneous=True)),t,modulus=q)
 if f.is_zero:return False
 infinity_mult=4-f.degree()
 if infinity_mult%2:return False
 coeff,factors=s.factor_list(f,modulus=q)
 return all(m%2==0 for _,m in factors)

res=[]
for i,(grp,F) in enumerate(models,1):
 bx=[L for L in lines if bitangent(F,L)]
 res.append(len(bx))
 print(i,grp,len(bx),bx)
 for K,other in [(x,(y,z)),(y,(x,z)),(z,(x,y))]:
  affine=s.expand(F.subs(K,1))
  polys=[affine]+[s.diff(affine,w) for w in other]
  G=s.groebner(polys,*other,modulus=q)
  assert len(G.polys)==1 and G.polys[0].is_one,('singular',i,K,G)
print('smooth 32/32 and histogram:',dict(collections.Counter(res)))
