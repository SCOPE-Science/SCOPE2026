#!/usr/bin/env python3
"""Independent finite-field coefficient-square bitangent test."""
import itertools
from collections import Counter
from pathlib import Path
from sympy import symbols,sympify,Poly
u,v,X,Y,Z=symbols('u v X Y Z')
p=5

def normalize(c):
 c=[int(a)%p for a in c]
 if not any(c):return None
 d=pow(next(x for x in c if x),-1,p)
 return tuple(x*d%p for x in c)

# coefficient vectors of all nonzero scalar-squares of binary quadratics
sqset=set()
for a,b,c in itertools.product(range(p),repeat=3):
 if (a,b,c)==(0,0,0):continue
 h=Poly((a*u*u+b*u*v+c*v*v)**2,u,v,modulus=p)
 sqset.add(normalize([h.coeff_monomial(u**(4-i)*v**i) for i in range(5)]))
assert len(sqset)==31,len(sqset)

def projective_lines():
 out=[]
 for a,b,c in itertools.product(range(p),repeat=3):
  if (a,b,c)!=(0,0,0) and normalize((a,b,c))==(a,b,c):out.append((a,b,c))
 assert len(out)==31
 return out

def good(F,a,b,c):
 if c:
  substitutions={X:u,Y:v,Z:(-a*u-b*v)*pow(c,-1,p)}
 elif b:
  substitutions={X:u,Y:(-a*u-c*v)*pow(b,-1,p),Z:v}
 else:substitutions={X:0,Y:u,Z:v}
 h=Poly(F.subs(substitutions,simultaneous=True).expand(),u,v,modulus=p)
 k=normalize([h.coeff_monomial(u**(4-i)*v**i) for i in range(5)])
 assert k is not None
 return k in sqset

lines=projective_lines()
curves=Path(__file__).with_name('curves_f5.txt').read_text().splitlines()
assert len(curves)==31
counts=[]
for i,e in enumerate(curves,1):
 F=sympify(e.replace('^','**'),locals={'x':X,'y':Y,'z':Z})
 matching=[t for t in lines if good(F,*t)]
 counts.append(len(matching))
 print(i,len(matching),flush=True)
 if i==31:
  assert len(matching)==16 and all(all(t) for t in matching)
  print('FERMAT_LINES',matching)
print('DISTRIBUTION',dict(sorted(Counter(counts).items())))
print('MAX',max(counts),'AT',[i+1 for i,x in enumerate(counts) if x==max(counts)])
