"""Independent elementary enumeration of tame quartic covers over F_3 with >=3 rational branch values."""
import itertools, math, collections
q=3
n=4
vectors=[tuple(v) for v in itertools.product(range(3),repeat=5) if any(v)]

def trim(a):
 a=list(a)
 while a and a[-1]==0:a.pop()
 return tuple(a)

def divmod3(a,b):
 a=list(trim(a));b=trim(b)
 if not b:raise ZeroDivisionError
 R=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b):
  i=len(a)-len(b);v=a[-1]*pow(b[-1],-1,3)%3;R[i]=v
  for j,bj in enumerate(b):a[i+j]=(a[i+j]-v*bj)%3
  while a and a[-1]==0:a.pop()
 return trim(R),trim(a)

def gcd3(a,b):
 while b:
  _,r=divmod3(a,b);a,b=b,r
 if not a:return ()
 return tuple(x*pow(a[-1],-1,3)%3 for x in a)

def polyfac(a):
 a=trim(a);fac=[]
 if not a:return []
 while len(a)>1:
  found=False
  for d in range(1,len(a)):
   for tail in itertools.product(range(3),repeat=d):
    g=tuple(tail)+(1,)
    h,r=divmod3(a,g)
    if not r:
     mult=0
     while True:
      h,r=divmod3(a,g)
      if r:break
      a=h;mult+=1
     fac.append((g,mult))
     found=True;break
   if found:break
  if not found:
   fac.append((tuple(x*pow(a[-1],-1,3)%3 for x in a),1));break
 return fac

P={};support={}
for v in vectors:
 a=tuple(reversed(v));fac=polyfac(a)
 at_inf=next(i for i,z in enumerate(v) if z)
 ps=[at_inf]*bool(at_inf);S={(0,1)} if at_inf else set()
 for g,k in fac:
  ps.extend([k]*(len(g)-1));S.add(('poly',g))
 assert sum(ps)==4, (v,fac,ps)
 P[v]=tuple(sorted(ps,reverse=True));support[v]=S

part_plain=(1,1,1,1)
allowed={(4,), (2,2), (2,1,1),part_plain}
passcodes=collections.Counter()
three=collections.Counter();four=collections.Counter();others=collections.Counter()
accepted={};three_reps={};raw3=collections.Counter();raw4=collections.Counter()
allpairs=0;sepcnt=0
for a in vectors:
 for b in vectors:
  if next(z for z in a+b if z)!=1:continue
  if support[a]&support[b]:continue
  allpairs+=1
  ps=tuple(P[b] if t is None else P[tuple((u-t*v)%3 for u,v in zip(a,b))] for t in (None,0,1,2))
  branch=sum(p!=part_plain for p in ps)
  if branch<3:continue
  if not all(p in allowed for p in ps):continue
  r=sum(4-len(p) for p in ps)
  if r>6:continue
  if branch==4:
   raw4[r]+=1
   four[(tuple(sorted(ps)),r)]+=1
   continue
  raw3[(r,tuple(sorted(ps)))]+=1
  # branch = 3. Residual ram must occur at nonrational source (because every rational source maps to a rational target), hence degree >= 2.
  if r==6:
   t=('ALL_RATIONAL',tuple(sorted(ps)))
  elif r==3 and tuple(sorted(ps))==(part_plain,(2,1,1),(2,1,1),(2,1,1)):
   # Test Wronskian residual irreducible cubic, separate from rational critical points.
   ap=tuple(reversed(a));bp=tuple(reversed(b))
   def mul(c,d):
    out=[0]*(len(c)+len(d)-1)
    for j,cj in enumerate(c):
     for k,dk in enumerate(d):out[j+k]=(out[j+k]+cj*dk)%3
    return tuple(out)
   def deriv(c):return tuple(j*c[j]%3 for j in range(1,len(c)))
   z1=mul(deriv(ap),bp);z2=mul(ap,deriv(bp))
   zz=[(x-y)%3 for x,y in itertools.zip_longest(z1,z2,fillvalue=0)]
   ff=polyfac(zz)
   inf=6-(len(trim(zz))-1)
   # W = four? here exactly three simple critical over F3 and one irreducible cubic.
   types=sorted([(len(g)-1,k) for g,k in ff]+([(1,inf)] if inf else []))
   if types != [(1,1),(1,1),(1,1),(3,1)]:continue
   t=('CUBIC_EXTRA',tuple(sorted(ps)))
  else:continue
  three[t]+=1
  accepted[(a,b)]=t
  three_reps.setdefault(t,(a,b))
print('all normalized separable deg4',allpairs)
print('raw three candidates',raw3);print('raw four',raw4);print('three branch values',three,'total',sum(three.values()))
print('four rational branch profiles (need checking other ramification)',four)
print('representatives',three_reps)
assert allpairs==17496
assert sum(three.values())==864
assert not four
assert len(accepted)==864
