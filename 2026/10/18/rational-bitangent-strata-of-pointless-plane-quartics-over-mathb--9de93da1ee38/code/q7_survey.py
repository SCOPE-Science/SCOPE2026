import itertools,collections,sympy as sp
from pathlib import Path
q=7
x,y,z=sp.symbols('x y z');var=(x,y,z)
models=[]
for line in (Path(__file__).resolve().parents[1] / 'data' / 'q7_models.txt').read_text().splitlines():
 if line.strip():
  label,expr=line.split('|')
  P=sp.Poly(sp.sympify(expr.replace('^','**')),x,y,z)
  mon={k:int(v)%q for k,v in P.terms() if int(v)%q}
  assert all(sum(k)==4 for k in mon)
  models.append((label,mon,expr))

def ev(P,coords):
 a,b,c=coords
 return sum(k*pow(a,i,q)*pow(b,j,q)*pow(c,l,q) for (i,j,l),k in P.items())%q

def canonical(t):
 i=next(i for i,a in enumerate(t) if a)
 inv=pow(t[i],-1,q)
 return tuple((a*inv)%q for a in t)
points=sorted({canonical(t) for t in itertools.product(range(q),repeat=3) if any(t)})
lines=points
bsig=set()
for aa,bb,cc in itertools.product(range(q),repeat=3):
 if not (aa or bb or cc):continue
 val=[(aa+bb*t+cc*t*t)**2%q for t in range(5)]
 for lam in range(1,q):bsig.add(tuple((lam*v)%q for v in val))

def basis(L):
 v=[P for P in points if sum(a*b for a,b in zip(L,P))%q==0]
 A=v[0];B=next(t for t in v if t!=A)
 return A,B
basis_cache={L:basis(L) for L in lines}
assert len(lines)==q*q+q+1==57
print('lines',len(lines),'square signatures',len(bsig))
result=[]
for idx,(group,P,e) in enumerate(models):
 assert not any(ev(P,t)==0 for t in points),(idx,'has rational point')
 bit=[]
 for L,(A,B) in basis_cache.items():
  vals=tuple(ev(P,tuple((a+t*b)%q for a,b in zip(A,B))) for t in range(5))
  if vals in bsig:bit.append(L)
 result.append((idx+1,group,len(bit),bit))
 print(idx+1,group,len(bit))
print('summary',dict(sorted(collections.Counter(row[2] for row in result).items())))
