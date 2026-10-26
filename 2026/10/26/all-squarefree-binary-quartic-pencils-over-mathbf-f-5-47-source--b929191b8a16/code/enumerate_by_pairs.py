"""Independent projective-pair enumeration of squarefree binary-quartic pencils.

All arithmetic is exact over the field with five elements. Each pencil has
six projective members and fifteen unordered member-pairs.
"""
from itertools import product
from collections import Counter
P=5

def normalize(v):
 for x in v:
  if x%P:
   i=pow(x,-1,P)
   return tuple(y*i%P for y in v)
 raise ValueError('zero vector')

def trimmed(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a

def remainder(a,b):
 a=trimmed(a);b=trimmed(b)
 while len(a)>=len(b):
  n=len(a)-len(b);k=a[-1]*pow(b[-1],-1,P)%P
  for i,v in enumerate(b):a[n+i]=(a[n+i]-k*v)%P
  a=trimmed(a)
 return a

def gcd_degree(a,b):
 a=trimmed(a);b=trimmed(b)
 while b:a,b=b,remainder(a,b)
 return len(a)-1

def is_squarefree(v):
 f=v[::-1]
 deriv=[(i*f[i])%P for i in range(1,5)]
 return gcd_degree(f,deriv)==0 and (v[0]!=0 or v[1]!=0)

V=sorted({normalize(v) for v in product(range(P),repeat=5) if any(v)})
assert len(V)==781
S={v for v in V if is_squarefree(v)}
assert len(S)==600
lookup={}
for i,a in enumerate(V):
 for b in V[i+1:]:
  members=tuple(sorted([b]+[normalize([(a[k]+t*b[k])%P for k in range(5)]) for t in range(P)]))
  lookup.setdefault(members,(a,b))
assert len(lookup)==20306
smooth={key:b for key,b in lookup.items() if all(x in S for x in key)}
assert len(smooth)==3820
G=Counter()
for key,(a,b) in smooth.items():
 degree=gcd_degree(a[::-1],b[::-1])+min(4-len(trimmed(a[::-1]))+1,4-len(trimmed(b[::-1]))+1)
 G[degree]+=1
assert G=={0:3710,2:70,3:40}
print('PAIR_SPACE_SIZE',len(lookup))
print('SQUAREFREE_QUARTIC_FORMS',len(S))
print('SMOOTH_QUARTIC_PENCILS',len(smooth))
print('BASE_DIVISOR_DEGREES',sorted(G.items()))
print('PAIR_ENUMERATION_PASS')

# A second orbit enumeration, on canonical sets of six projective members.
def poly_mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):out[i+j]=(out[i+j]+v*w)%P
 return out

def power(a,n):
 v=[1]
 for _ in range(n):v=poly_mul(v,a)
 return v

def image(m,f):
 a,b,c,d=m
 x=[b,a];z=[d,c];out=[0]*5
 for i,u in enumerate(f):
  temp=poly_mul(power(x,4-i),power(z,i))
  for j,v in enumerate(temp):out[4-j]=(out[4-j]+u*v)%P
 return normalize(out)

M={normalize(v) for v in product(range(P),repeat=4) if (v[0]*v[3]-v[1]*v[2])%P}
assert len(M)==120
available=set(smooth)
orbit_size_counts=Counter()
while available:
 representative=min(available)
 orbit={tuple(sorted(image(m,f) for f in representative)) for m in M}
 assert orbit<=smooth.keys()
 available-=orbit
 orbit_size_counts[len(orbit)]+=1
assert orbit_size_counts=={120:20,60:21,40:3,20:1,10:2}
print('PAIR_ORBITS',sum(orbit_size_counts.values()),sorted(orbit_size_counts.items()))

# Factor-degree profiles via Frobenius gcd identities, without trial division.
def polynomial_power_mod(x,n,f):
 r=[1]
 while n:
  if n&1:r=remainder(poly_mul(r,x),f)
  x=remainder(poly_mul(x,x),f)
  n//=2
 return r

def root_profile(v):
 f=trimmed(v[::-1]);d=len(f)-1
 at_infinity=4-d
 assert at_infinity in (0,1)
 f=[x*pow(f[-1],-1,P)%P for x in f]
 counts={}
 for j in range(1,5):
  xpower=polynomial_power_mod([0,1],P**j,f)
  poly=trimmed([(xpower[k] if k<len(xpower) else 0)-(1 if k==1 else 0) for k in range(max(2,len(xpower)))])
  nd=gcd_degree(f,poly)
  accounts=sum(i*counts[i] for i in range(1,j) if j%i==0)
  counts[j]=(nd-accounts)//j
  assert counts[j]>=0
 profile=tuple(sorted([1]*at_infinity+sum(([j]*counts[j] for j in range(1,5)),[])))
 assert sum(profile)==4
 return profile

root_profiles={v:root_profile(v) for v in S}
fibre_profiles=Counter(tuple(sorted(root_profiles[f] for f in key)) for key in smooth)
assert len(fibre_profiles)==14
assert sum(fibre_profiles.values())==3820
print('PAIR_PROFILES',len(fibre_profiles),sorted(fibre_profiles.values()))
print('PAIR_ORBIT_PROFILE_PASS')
import json
with open('pair_profiles.generated.json','w',encoding='utf-8') as out:
 json.dump([{'profile':[list(k) for k in key],'count':n} for key,n in sorted(fibre_profiles.items())],out,indent=2)
