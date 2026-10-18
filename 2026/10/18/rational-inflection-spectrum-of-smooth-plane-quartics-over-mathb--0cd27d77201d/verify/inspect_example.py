from itertools import product, combinations
from math import comb
exps=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
num=78753
c=[]
for _ in exps:c.append(num%3);num//=3
print('monomials=',[(str(v),e) for v,e in zip(c,exps) if v])
ps=[]
for p in product(range(3),repeat=3):
 if not any(p):continue
 if next(v for v in p if v)!=1:continue
 ps.append(p)
assert len(ps)==13
mod=lambda a:a%3
pow3=lambda p,e:pow(p,e,3)
def f(p):return mod(sum(a*pow3(p[0],e[0])*pow3(p[1],e[1])*pow3(p[2],e[2]) for a,e in zip(c,exps)))
def grad(p):return [mod(sum(a*e[k]*pow3(p[k],e[k]-1)*pow3(p[(k+1)%3],e[(k+1)%3])*pow3(p[(k+2)%3],e[(k+2)%3]) for a,e in zip(c,exps) if e[k])) for k in range(3)]
def cf(p,q,m):
 out=0
 for a,e in zip(c,exps):
  for t in product(*[range(v+1) for v in e]):
   if sum(t)!=m:continue
   v=a
   for j in range(3):v*=comb(e[j],t[j])*p[j]**(e[j]-t[j])*q[j]**t[j]
   out+=v
 return out%3
flex=[]
for p in ps:
 if f(p):continue
 g=grad(p)
 q=next(q for q in ps if q!=p and sum(x*y for x,y in zip(g,q))%3==0)
 mult=next(k for k in (2,3,4) if cf(p,q,k)!=0)
 print('point=',p,'tangent=',tuple(g),'order=',mult)
 if mult>=3:flex.append((p,g,mult))
print('flex=',flex)
lines=[l for l in ps]
for a,b in combinations(lines,2):
 union={p for p in ps if sum(u*v for u,v in zip(a,p))%3==0 or sum(u*v for u,v in zip(b,p))%3==0}
 if {p for p,_,_ in flex}.issubset(union):print('flex conic factors',a,b,'union',sorted(union))
print('coefs',c)
