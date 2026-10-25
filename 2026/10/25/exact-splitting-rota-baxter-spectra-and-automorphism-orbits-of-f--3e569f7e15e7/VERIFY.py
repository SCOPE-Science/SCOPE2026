from math import gcd
from itertools import product

def mul(x,y,n):
 a,b=x;c,d=y
 return ((a+(-1 if b else 1)*c)%n,(b+d)%2)

def subgroups(n):
 G=[(i,b) for b in (0,1) for i in range(n)]
 e={(0,0)}
 return [e]+[{(j*n//a,0) for j in range(a)} for a in sorted(divs(n)) if a!=1]+[{(j*n//a,0) for j in range(a)} | {((i+j*n//a)%n,1) for j in range(a)} for a in sorted(divs(n)) for i in range(n//a)]
def divs(n):return [k for k in range(1,n+1) if n%k==0]
def exact(n):
 G=set((i,b) for b in (0,1) for i in range(n)); pairs=[]
 S=subgroups(n)
 assert len(set(map(frozenset,S)))==len(S)
 for H in S:
  for L in S:
   if len(H)*len(L)!=2*n or H.intersection(L)!={(0,0)}:continue
   if {mul(h,l,n) for h in H for l in L}==G:pairs.append((H,L))
 return pairs

def rb(n,H,L):
 G=[(i,b) for b in (0,1) for i in range(n)]
 ans={mul(h,l,n):((-1 if l[1] else 1)*(-l[0])%n,l[1]) for h in H for l in L}
 assert len(ans)==2*n
 for x in G:
  for y in G:
   v=ans[x]; yy=mul(mul(mul(x,v,n),y,n), ((-1 if v[1] else 1)*(-v[0])%n,v[1]),n)
   assert mul(ans[x],ans[y],n)==ans[yy]
 return ans

def spec(n):
 return [(a,b) for a in divs(n) for b in divs(n) if a*b==n and gcd(a,b)==1]
for n in range(1,25):
 p=exact(n); predicted=2*sum(a for a,b in spec(n))+(n*(len(spec(n//2))) if n%2==0 else 0)
 assert len(p)==predicted,(n,len(p),predicted)
 if n<=10:
  for h,l in p:rb(n,h,l)
 print(n,len(p),predicted)
print('VERIFY_OK')

def phi(x,n,u,v):
 i,b=x;return ((u*i+v*b)%n,b)
def omega(x):
 q=2;t=0
 while q*q<=x:
  if x%q==0:
   t+=1
   while x%q==0:x//=q
  q+=1
 return t+(x>1)
for n in range(3,25):
 p=exact(n)
 maps=[]
 for H,L in p:
  b=rb(n,H,L) if n<7 else None
  maps.append((frozenset(H),frozenset(L)))
 unresolved=set(maps); orbits=[]
 while unresolved:
  H,L=next(iter(unresolved))
  orb=set((frozenset(phi(x,n,u,v) for x in H),frozenset(phi(x,n,u,v) for x in L))
           for u in range(n) if gcd(u,n)==1 for v in range(n))
  assert orb <= set(maps)
  unresolved-=orb;orbits.append(orb)
 predicted=2*2**omega(n)+(2**omega(n//2) if n%2==0 else 0)
 assert len(orbits)==predicted,(n,len(orbits),predicted)
 print('orbits',n,len(orbits))
print('ORBIT_VERIFY_OK')
