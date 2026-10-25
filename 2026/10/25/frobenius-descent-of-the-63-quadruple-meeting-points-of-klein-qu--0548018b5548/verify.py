# Finite field F_{3^6} = F27(v), v^2=-1, with F27=F3[u]/(u^3-u-1)
from collections import Counter

def d27(a):return (a%3,(a//3)%3,a//9)
def e27(t):return (t[0]%3)+3*(t[1]%3)+9*(t[2]%3)
def add27(a,b):return e27(tuple(x+y for x,y in zip(d27(a),d27(b))))
def neg27(a):return e27(tuple(-x for x in d27(a)))
def mul27(a,b):
 A=d27(a);B=d27(b);c=[0]*5
 for i in range(3):
  for j in range(3):c[i+j]+=A[i]*B[j]
 for i in (4,3):
  v=c[i];c[i]=0;c[i-2]+=v;c[i-3]+=v
 return e27(c)
def ed(a,b):return a+27*b
def dd(a):return a%27,a//27
def add(a,b):
 x,y=dd(a);z,w=dd(b)
 return ed(add27(x,z),add27(y,w))
def neg(a):
 x,y=dd(a);return ed(neg27(x),neg27(y))
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 x,y=dd(a);z,w=dd(b)
 return ed(add27(mul27(x,z),neg27(mul27(y,w))),add27(mul27(x,w),mul27(y,z)))
def powf(a,n):
 r=1
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n>>=1
 return r
def inv(a):assert a;return powf(a,727)
def norm(v):
 for e in v:
  if e:
   iv=inv(e);return tuple(mul(iv,t) for t in v)
 raise ValueError('zero vec')
def cr(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
def fr(v,n=1):return norm(tuple(powf(t,3**n) for t in v))
def curve(v):
 x,y,z=v
 return add(add(mul(powf(x,3),y),mul(powf(y,3),z)),mul(powf(z,3),x))==0
roots=[t for t in range(1,729) if add(add(powf(t,28),powf(t,21)),1)==0]
assert len(roots)==28
assert Counter(next(i for i in range(1,7) if powf(t,3**i)==t) for t in roots)==Counter({1:1,3:3,6:24})
points=[];lines=[]
for t in roots:
 p=norm((1,t,powf(inv(t),9)))
 assert curve(p)
 assert fr(p,2)==norm((p[2],p[0],p[1]))
 l=norm((powf(p[2],3),powf(p[0],3),powf(p[1],3)))
 assert dot(p,l)==0
 points.append(p);lines.append(l)
assert len(set(lines))==28
assert Counter(len(set(tuple(fr(l,k)) for k in range(1,7))) for l in lines)==Counter({1:1,3:3,6:24})
inte={}
for i in range(28):
 for j in range(i+1,28):
  p=norm(cr(lines[i],lines[j]))
  assert not curve(p)
  inte.setdefault(p,[])
  inte[p].append((i,j))
assert len(inte)==63
assert Counter(len(k) for k in inte.values())==Counter({6:63})
assert len(inte)==63 and all(len(v)==6 for v in inte.values())
for p in inte:
 through=sum(dot(p,l)==0 for l in lines)
 assert through==4
visited=set();cycle=[]
for p in inte:
 if p in visited:continue
 orbit=[];r=p
 while r not in orbit:
  orbit.append(r);visited.add(r);r=fr(r)
 assert r==p
 cycle.append(len(orbit))
assert Counter(cycle)==Counter({3:3,6:9})
# Arithmetic consequences for the reduced incidence sets.
assert sum(fr(p)==p for p in points)==1
assert sum(fr(p,2)==p for p in points)==1
assert sum(fr(p,3)==p for p in points)==4
assert sum(fr(p)==p for p in inte)==0
assert sum(fr(p,2)==p for p in inte)==0
assert sum(fr(p,3)==p for p in inte)==9
print('VERIFY_OK: bitangents 1+3+4*6; quadruple intersections 3*3+9*6')
