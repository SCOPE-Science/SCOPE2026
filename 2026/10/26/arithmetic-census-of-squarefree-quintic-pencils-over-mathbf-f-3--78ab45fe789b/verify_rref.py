"""Independent row-reduced matrix enumeration, SymPy finite-field gcd."""
import itertools,json,collections
import sympy as sp
x=sp.Symbol('x')
D=6

def code(v):return sum(t*3**i for i,t in enumerate(v))
def normalize(v):
 c=next((q for q in v if q),None)
 assert c is not None
 return code([t*pow(c,-1,3)%3 for t in v])
def smooth(v):
 deg=max(i for i,t in enumerate(v) if t)
 if deg<4:return False
 f=sp.Poly(sum(int(t)*x**i for i,t in enumerate(v)),x,modulus=3)
 return sp.gcd(f,f.diff()).degree()==0
cnt=0; valid=[];sz=collections.Counter()
for i in range(D):
 for j in range(i+1,D):
  A=[k for k in range(i+1,D) if k!=j]
  B=list(range(j+1,D))
  for values in itertools.product(range(3),repeat=len(A)+len(B)):
   v=[0]*D;w=[0]*D;v[i]=1;w[j]=1
   for k,t in zip(A,values[:len(A)]):v[k]=t
   for k,t in zip(B,values[len(A):]):w[k]=t
   cnt+=1
   projectives=[v,w,[(v[k]+w[k])%3 for k in range(D)],[(v[k]+2*w[k])%3 for k in range(D)]]
   if all(smooth(f) for f in projectives):
    valid.append(tuple(sorted(normalize(f) for f in projectives)))
print('all rref',cnt,'good',len(valid),'unique',len(set(valid)),flush=True)
assert cnt==11011 and len(valid)==1098 and len(set(valid))==len(valid)

from pathlib import Path
expected={tuple(map(int,line.split())) for line in (Path(__file__).resolve().parent/'pencils.txt').read_text().splitlines()}
assert set(valid)==expected
print('INDEPENDENT RREF AND SQUAREFREE GCD CHECK PASSED')
