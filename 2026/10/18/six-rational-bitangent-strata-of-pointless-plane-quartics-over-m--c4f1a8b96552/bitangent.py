#!/usr/bin/env python3
import sympy as S,itertools
x,y,z,t=S.symbols('x y z t')
P=5

def rational_lines():
 seen=set()
 for tup in itertools.product(range(P),repeat=3):
  if tup==(0,0,0):continue
  k=next(v for v in tup if v)
  # inv mod 5
  a,b,c=tuple(v*pow(k,-1,5)%5 for v in tup)
  seen.add((a,b,c))
 return sorted(seen)

def restrict(F,line):
 a,b,c=line
 if c:
  X,Y,Z=1,t,(-a-b*t)*pow(c,-1,5)
 elif b:
  X,Y,Z=1,(-a-c*t)*pow(b,-1,5),t
 else:
  X,Y,Z=0,1,t
 return S.Poly(F.subs({x:X,y:Y,z:Z},simultaneous=True).expand(),t,modulus=5)

def is_bitangent(F,line):
 f=restrict(F,line)
 if f.is_zero:raise ValueError('line component')
 if (4-f.degree())%2: return False
 return all(k%2==0 for fact,k in f.sqf_list()[1])

def summarize(expr):
 F=S.sympify(expr.replace('^','**'),locals={'x':x,'y':y,'z':z})
 b=[l for l in rational_lines() if is_bitangent(F,l)]
 return len(b),b

if __name__=='__main__':
 for f in ['x^4+y^4+z^4','x^4 + y^4 + z^4 + x^2*y^2 + x^2*z^2 + y^2*z^2','x^4 + y^4 + 2*z^4','x^4 + x^2*y^2 + 2*y^4 + 2*z^4']:
  print(f,summarize(f))
