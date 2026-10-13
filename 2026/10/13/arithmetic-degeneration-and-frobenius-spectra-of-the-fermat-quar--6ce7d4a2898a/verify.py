#!/usr/bin/env python3
"""Exact cyclotomic and finite-field incidence verification for 28 Fermat-quartic bitangents.
Requires only Python 3.9+ standard library. No numerical approximations.
"""
from itertools import combinations,product
from collections import Counter,defaultdict
z=(0,0,0,0);one=(1,0,0,0)
def add(a,b):return tuple(a[i]+b[i] for i in range(4))
def neg(a):return tuple(-v for v in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 for k in range(6,3,-1):c[k-4]-=c[k]
 return tuple(c[:4])
def P(k):
 k%=8
 return tuple((1 if k<4 else -1) if j==(k%4) else 0 for j in range(4))
def sigma(a,k):
 c=z
 for i,x in enumerate(a):
  if x:c=add(c,tuple(x*v for v in P(k*i)))
 return c
def norm(a):
 c=one
 for k in (1,3,5,7):c=mul(c,sigma(a,k))
 assert c[1:]==(0,0,0),c
 return c[0]
def det3(a,b,c):
 return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))
lines=[]
for r,s in product((0,2,4,6),repeat=2):lines.append((neg(P(r)),neg(P(s)),one))
for a in (1,3,5,7):
 lines.extend(((one,neg(P(a)),z),(z,one,neg(P(a))),(neg(P(a)),z,one)))
assert len(lines)==28
for i,l in enumerate(lines):
 for j in range(i):
  assert any(mul(l[x],lines[j][y])!=mul(l[y],lines[j][x]) for x,y in ((0,1),(0,2),(1,2)))
pairs=list(combinations(range(28),2)); pind={pair:i for i,pair in enumerate(pairs)}
parent=list(range(len(pairs)))
def root(a):
 while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
 return a
def union(a,b):
 a,b=root(a),root(b)
 if a!=b:parent[b]=a
normc=Counter();triple_zero=0
for i,j,k in combinations(range(28),3):
 d=det3(lines[i],lines[j],lines[k])
 if d==z:
  triple_zero+=1
  union(pind[i,j],pind[i,k]);union(pind[i,j],pind[j,k])
 else:
  normc[abs(norm(d))]+=1
classes=defaultdict(list)
for t,pair in enumerate(pairs):classes[root(t)].append(pair)
mult=Counter();classrep={};pointfrompair={}
for q,L in classes.items():
 k=1
 while k*(k-1)//2 < len(L):k+=1
 assert k*(k-1)//2==len(L),('Noncomplete group',q,len(L))
 mult[k]+=1
 classrep[q]=L[0]
 for pair in L:pointfrompair[pair]=q
print('lines',len(lines),'total pairs',len(pairs),'triple concurrent',triple_zero,'point mult',mult,'total points',len(classes))
print('nonzero determinant norms',normc)
factors=Counter()
for n,num in normc.items():
 rem=n
 for p in (2,3,5,17):
  if rem%p==0:factors[p]+=num
  while rem%p==0:rem//=p
 assert rem==1,('unexpected norm prime',n)
print('exceptional candidate primes',factors)

def linekey(l):
 # Galois perm using projective proportionality
 for j,m in enumerate(lines):
  if all(mul(l[a],m[b])==mul(l[b],m[a]) for a,b in ((0,1),(0,2),(1,2))):return j
 raise ValueError(l)
fixes={};linefix={};cycleprofiles={};linecyc={}
for k in (1,3,5,7):
 perm=[linekey(tuple(sigma(a,k) for a in line)) for line in lines]
 assert sorted(perm)==list(range(28))
 pmap={}
 for q,(i,j) in classrep.items():
  a,b=sorted((perm[i],perm[j]));pmap[q]=pointfrompair[a,b]
 assert set(pmap.values())==set(classes)
 fixes[k]=Counter({m:sum(q==q2 and len(classes[q])==m*(m-1)//2 for q,q2 in pmap.items()) for m in mult})
 linefix[k]=sum(j==i for i,j in enumerate(perm))
 profiles=Counter();seen=set()
 for q in classes:
  if q not in seen:
   cycle=[];a=q
   while a not in seen:
    cycle.append(a);seen.add(a);a=pmap[a]
   assert a==q
   mm=len(classes[q]); order=1
   while order*(order-1)//2<mm:order+=1
   profiles[(order,len(cycle))]+=1
 cycleprofiles[k]=dict(profiles)
 print('k',k,'linefix',linefix[k],'pointfix',dict(fixes[k]),'cycles',dict(profiles))
print('q=1 mod8',fixes[1]);print('q=3 mod8',fixes[3]);print('q=5 mod8',fixes[5]);print('q=7 mod8',fixes[7]);

assert triple_zero==60
assert mult==Counter({2:288,4:15})
assert normc==Counter({1:384,2:64,4:864,8:384,9:192,16:560,17:192,32:96,36:192,64:192,256:64,400:32})
assert set(factors)=={2,3,5,17}
assert linefix=={1:28,3:4,5:16,7:4}
assert {k:dict(v) for k,v in fixes.items()}=={1:{2:288,4:15},3:{2:0,4:9},5:{2:48,4:15},7:{2:0,4:9}}

class F:
 def __init__(self,p):
  self.p=p; self.d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
  self.z=(0,0);self.o=(1,0)
 def elt(self,a):return(a%self.p,0)
 def plus(self,a,b):return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
 def neg(self,a):return((-a[0])%self.p,(-a[1])%self.p)
 def minus(self,a,b):return self.plus(a,self.neg(b))
 def mul(self,a,b):p=self.p;return ((a[0]*b[0]+self.d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
 def inv(self,a):p=self.p;t=pow((a[0]*a[0]-self.d*a[1]*a[1])%p,-1,p);return (a[0]*t%p,-a[1]*t%p)
 def div(self,a,b):return self.mul(a,self.inv(b))
 def pw(self,a,n):
  v=self.o
  for i in range(n):v=self.mul(v,a)
  return v
 def primitive8(self):
  for a in product(range(self.p),repeat=2):
   if self.pw(a,8)==self.o and self.pw(a,4)!=self.o:return a
  assert False
 def cross(self,a,b):
  sub=self.minus;mul=self.mul
  return tuple(sub(mul(a[(j+1)%3],b[(j+2)%3]),mul(a[(j+2)%3],b[(j+1)%3])) for j in range(3))
 def canon(self,v):
  for a in v:
   if a!=self.z:return tuple(self.div(x,a) for x in v)
  raise ValueError('zero cross')
 def frob(self,a):return self.pw(a,self.p)
expected={
 3:({4:63},{4:9},4),
 5:({2:240,3:16,4:15},{3:16,4:15},16),
 7:({2:288,4:15},{4:9},4),
 11:({2:288,4:15},{4:9},4),
 13:({2:288,4:15},{2:48,4:15},16),
 17:({2:144,3:48,4:15},{2:144,3:48,4:15},28),
 19:({2:288,4:15},{4:9},4),
 23:({2:288,4:15},{4:9},4),
 29:({2:288,4:15},{2:48,4:15},16),
 31:({2:288,4:15},{4:9},4),
 41:({2:288,4:15},{2:288,4:15},28),
}
for p in expected:
 f=F(p);z=f.z;o=f.o;e=f.primitive8(); neg=f.neg
 def E(k):return f.pw(e,k)
 lines=[]
 for r,s in product((0,2,4,6),repeat=2):lines.append((neg(E(r)),neg(E(s)),o))
 for a in (1,3,5,7):lines.extend(((o,neg(E(a)),z),(z,o,neg(E(a))),(neg(E(a)),z,o)))
 pts=defaultdict(set)
 for i,j in combinations(range(28),2):
  q=f.canon(f.cross(lines[i],lines[j]));pts[q].update((i,j))
 mc=Counter(len(v) for v in pts.values());rational=Counter(len(v) for q,v in pts.items() if all(f.frob(a)==a for a in q))
 linefix=sum(1 for v in lines if f.canon(v)==f.canon(tuple(f.frob(a) for a in v)))
 assert dict(mc)==expected[p][0],(p,dict(mc))
 assert dict(rational)==expected[p][1],(p,dict(rational))
 assert linefix==expected[p][2],(p,linefix)
 assert sum(k*(k-1)//2*v for k,v in mc.items())==378
 if p==5: assert sum(rational.values())==p*p+p+1
print('VERIFY_OK: 3276 cyclotomic triple determinants, 378 pair-intersection classes, Frobenius fixed-point counts, 11 finite-field incidence censuses')
