from itertools import product
from collections import Counter
import json
from pathlib import Path
Q=3
N=7

def norm(v):
 for a in reversed(v):
  if a:
   inv=1 if a==1 else 2
   return tuple((x*inv)%Q for x in v)
 raise ValueError('zero')

vecs=sorted({norm(v) for v in product(range(3),repeat=7) if any(v)})
idx={v:i for i,v in enumerate(vecs)}

def add(a,b,s=1):return tuple((a[i]+s*b[i])%3 for i in range(7))

def trim(a):
 l=list(a)
 while l and l[-1]==0:l.pop()
 return l

def mod_inv(a):return 1 if a==1 else 2

def rem(a,b):
 a=trim(a);b=trim(b)
 if not b:raise ValueError('zero')
 while len(a)>=len(b):
  fac=a[-1]*mod_inv(b[-1])%3
  for i,x in enumerate(b):a[len(a)-len(b)+i]=(a[len(a)-len(b)+i]-fac*x)%3
  a=trim(a)
 return a

def gcd(a,b):
 a=trim(a);b=trim(b)
 while b:a,b=b,rem(a,b)
 return a

def smooth(v):
 a=trim(v)
 return len(a)>=6 and len(gcd(a,[(i*a[i])%3 for i in range(1,len(a))]))==1
smoothidx=set(i for i,v in enumerate(vecs) if smooth(v))
# construct 2-dimensional subspaces; for pair line, canonical lex tuple of its 4 normalized projective forms
lines={}
for i,a in enumerate(vecs):
 for j in range(i+1,len(vecs)):
  b=vecs[j]
  p=idx[norm(add(a,b))]
  m=idx[norm(add(a,b,-1))]
  key=tuple(sorted((i,j,p,m)))
  if key[0]!=i or key[1]!=j:continue
  lines[key]=1
all_smooth=[k for k in lines if all(i in smoothidx for i in k)]
# count rational branch points of each form f(X,Y) over P1(F3) [infty,0,1,-1], and rational C points (twists sign sensitive)
def evalf(v,x,y):return sum(v[i]*pow(x,i,3)*pow(y,6-i,3) for i in range(7))%3
points=[(1,0),(0,1),(1,1),(2,1)]
roots=[sum(evalf(vecs[i],x,y)==0 for x,y in points) for i in range(len(vecs))]
profile=Counter(tuple(sorted(roots[i] for i in k)) for k in all_smooth)
# common radical roots over algebraic closure: gcd(f,g) with degree at infinity. Characterize minimal common degree via gcd homogeneous
bases={}
for k in all_smooth:
 i,j=k[:2]; a,b=vecs[i],vecs[j]
 af=trim(a);bf=trim(b)
 common_deg=(6-max(len(af),len(bf))+1)+(len(gcd(af,bf))-1)
 bases[k]=common_deg
# group matrices over F3 up to F3^*, 24
mats=sorted({norm((a,b,c,d)) for a,b,c,d in product(range(3),repeat=4) if (a*d-b*c)%3})
assert len(mats)==24

def multiply(p,q):
 z=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):z[i+j]=(z[i+j]+a*b)%3
 return z

def powpoly(p,n):
 r=[1]
 for _ in range(n):r=multiply(r,p)
 return r

def action(v,m):
 a,b,c,d=m
 out=[0]*7
 for i,w in enumerate(v):
  if w:
   x= multiply(powpoly([b,a],i),powpoly([d,c],6-i))
   for j in range(7):out[j]=(out[j]+w*x[j])%3
 return norm(out)
perms=[]
for m in mats:
 pi=tuple(idx[action(v,m)] for v in vecs)
 assert sorted(pi)==list(range(len(vecs)))
 perms.append(pi)
S=set(all_smooth)
orbits=[]
while S:
 k=min(S)
 orbit={tuple(sorted(pi[i] for i in k)) for pi in perms}
 assert orbit<=S,(len(orbit),len(orbit-S))
 S-=orbit
 orbits.append((k,len(orbit)))
res=dict(count_forms=len(vecs),smooth_forms=len(smoothidx),all_lines=len(lines),all_smooth_lines=len(all_smooth),root_profiles={','.join(map(str,k)):v for k,v in profile.items()},base_degrees=dict(Counter(bases.values())),orbit_count=len(orbits),orbit_sizes=dict(Counter(sz for k,sz in orbits)),orbit_data=[dict(representatives=[list(vecs[i]) for i in k[:2]],members=list(k),orbit_size=sz,roots=sorted(roots[i] for i in k),common_degree=bases[k]) for k,sz in orbits])
assert res['count_forms']==1093 and res['smooth_forms']==648
assert res['all_lines']==99463 and res['all_smooth_lines']==10005
assert res['orbit_count']==440
expected=json.loads(Path(__file__).with_name('orbit_catalogue.json').read_text(encoding='utf-8'))
assert expected==json.loads(json.dumps(res)), 'reference catalogue differs'
print('PRIMARY PASS: 10005 all-smooth pencils in 440 PGL2-orbits')
