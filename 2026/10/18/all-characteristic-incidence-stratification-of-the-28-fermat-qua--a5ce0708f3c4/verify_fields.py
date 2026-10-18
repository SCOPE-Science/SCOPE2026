from collections import Counter,defaultdict

def run(p):
 d=next(k for k in range(2,p) if pow(k,(p-1)//2,p)==p-1)
 A=[(a,b) for a in range(p) for b in range(p)]
 Z=(0,0);ONE=(1,0)
 def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
 def neg(x):return ((-x[0])%p,(-x[1])%p)
 def sub(x,y):return add(x,neg(y))
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def power(x,n):
  r=ONE
  while n:
   if n&1:r=mul(r,x)
   x=mul(x,x);n>>=1
  return r
 def inv(x):return power(x,p*p-2)
 def norm(V):
  f=next(x for x in V if x!=Z);finv=inv(f)
  return tuple(mul(finv,x) for x in V)
 def cross(V,W):return (sub(mul(V[1],W[2]),mul(V[2],W[1])),sub(mul(V[2],W[0]),mul(V[0],W[2])),sub(mul(V[0],W[1]),mul(V[1],W[0])))
 mu4=[x for x in A if power(x,4)==ONE]
 mu8minus=[x for x in A if power(x,4)==neg(ONE)]
 L=[]
 for a in mu4:
  for b in mu4:L.append(norm((a,b,ONE)))
 for j in range(3):
  for rho in mu8minus:
   v=[Z,Z,Z];a,b=[x for x in range(3) if x!=j];v[a]=ONE;v[b]=neg(rho);L.append(norm(v))
 assert len(set(L))==28
 at=defaultdict(set)
 for j in range(28):
  for k in range(j+1,28):at[norm(cross(L[j],L[k]))].update([j,k])
 counts=Counter(map(len,at.values()))
 assert sum(z*(z-1)//2*n for z,n in counts.items())==378
 groups=Counter()
 for lid in range(28):
  profile=tuple(sum(lid in mask and len(mask)==r for mask in at.values()) for r in (2,3,4))
  groups[(('ordinary' if lid<16 else 'hyperflex'),profile)]+=1
 assert dict(counts)==expect[p]
 print('FIELD_OK',p,dict(sorted(counts.items())),dict(groups))
expect={3:{4:63},5:{2:240,3:16,4:15},7:{2:288,4:15},17:{2:144,3:48,4:15}}
for p in expect: run(p)
