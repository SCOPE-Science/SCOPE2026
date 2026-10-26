"""Independent exhaustive verification of the F5-rational bitangents using only Python stdlib."""
from itertools import product
p=5
norm=lambda a:tuple((x*pow(next(x for x in a if x%p),-1,p))%p for x in a)
proj=sorted({norm(a) for a in product(range(p),repeat=3) if any(a)})
assert len(proj)==31
# Polynomial quartic on (s,t) as a list of coefficients of s**(4-i)*t**i.
def linpoly(a,b,c):
 if c: # z=-(a*x+b*y)/c
  x=(1,0);y=(0,1);z=((-a*pow(c,-1,p))%p,(-b*pow(c,-1,p))%p)
 elif b: # y=-(a*x+c*z)/b
  x=(1,0);z=(0,1);y=((-a*pow(b,-1,p))%p,(-c*pow(b,-1,p))%p)
 else: # x=0: x=0, y=s,z=t
  x=(0,0);y=(1,0);z=(0,1)
 def mul(f,g):
  out=[0]*(len(f)+len(g)-1)
  for i,fi in enumerate(f):
   for j,gj in enumerate(g):out[i+j]=(out[i+j]+fi*gj)%p
  return out
 def pw(q,n):
  out=[1]
  for _ in range(n):out=mul(out,q)
  return out
 f1=mul(pw(x,3),y);f2=mul(pw(y,3),z);f3=mul(pw(z,3),x)
 return tuple((f1[i]+f2[i]+f3[i])%p for i in range(5))
squares=set()
for q in proj:
 a,b,c=q
 for l in range(1,5):squares.add(tuple((l*v)%5 for v in (a*a,2*a*b,a*2*c+b*b,2*b*c,c*c)))
bit=[l for l in proj if linpoly(*l) in squares]
assert bit==[(1,1,1)],bit
print('F5_RATIONAL_BITANGENTS',len(bit),'LINES',bit,'PASS')
