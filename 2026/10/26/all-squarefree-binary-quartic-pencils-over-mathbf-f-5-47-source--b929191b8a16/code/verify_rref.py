"""Independent finite-field census of smooth binary-quartic pencils over F5.
Polynomial discriminants and unique RREF bases are independent of the
pairwise-projective-lines/gcd strategy used in census.py.
"""
from itertools import combinations,product
from collections import Counter
from math import comb
import json,sys
P=5

def normalize(v):
  i=next(i for i,x in enumerate(v) if x%P)
  k=pow(v[i]%P,-1,P)
  return tuple(x*k%P for x in v)

def D(f):
  a,b,c,d,e=f
  I=(12*a*e-3*b*d+c*c)%P
  J=(72*a*c*e+9*b*c*d-27*a*d*d-27*e*b*b-2*c**3)%P
  return (4*I**3-J**2)%P

# one unique 2x5 RREF matrix per pencil
pencils=[]
for i,j in combinations(range(5),2):
  free1=[k for k in range(i+1,5) if k!=j]
  free2=list(range(j+1,5))
  for values in product(range(P),repeat=len(free1)+len(free2)):
   x=[0]*5;y=[0]*5;x[i]=y[j]=1
   for k,v in zip(free1,values[:len(free1)]):x[k]=v
   for k,v in zip(free2,values[len(free1):]):y[k]=v
   # normalized pencil members: x+t*y for t=0..4, and y
   allforms=[tuple(x[k]+t*y[k] for k in range(5)) for t in range(P)]+[tuple(y)]
   if all(D(f)!=0 for f in allforms):
    pencils.append((tuple(x),tuple(y)))
print('RREF_ALL',[sum(P**((5-i-1-1)+(5-j-1)) for i,j in combinations(range(5),2))],flush=True)
print('RREF_SMOOTH',len(pencils),flush=True)
assert len(pencils)==3820

# Degree of gcd of quartics, including potential infinity factor.
def clean(x):
 x=list(x)
 while x and not x[-1]:x.pop()
 return x

def rem(f,g):
 f=clean(f);g=clean(g)
 if not g:raise ArithmeticError
 while len(f)>=len(g):
  k=len(f)-len(g);v=f[-1]*pow(g[-1],-1,P)%P
  for i in range(len(g)):f[i+k]=(f[i+k]-v*g[i])%P
  f=clean(f)
 return f

def gcddeg(f,g):
 f=clean(f);g=clean(g)
 while g:f,g=g,rem(f,g)
 return len(f)-1

def degree_hom_gcd(f,g):
 a=clean(list(f[::-1]));b=clean(list(g[::-1]))
 return gcddeg(a,b)+4-max(len(a)-1,len(b)-1)
G=Counter(degree_hom_gcd(a,b) for a,b in pencils)
print('RREF_BASE_DIVISOR',sorted(G.items()),flush=True)
assert G=={0:3710,2:70,3:40}

# Independently form each induced Sym^4 action using the binomial theorem.
def transformed(m,coeff):
 a,b,c,d=m
 v=[0]*5
 for i,v0 in enumerate(coeff):
  if not v0:continue
  for r in range(5-i):
   for s in range(i+1):
    k=4-r-s
    v[k]=(v[k]+v0*comb(4-i,r)*comb(i,s)*pow(a,r,P)*pow(b,4-i-r,P)*pow(c,s,P)*pow(d,i-s,P))%P
 return tuple(v)

def rowreduce(rows):
 a=[list(row) for row in rows]
 r=0
 for c in range(5):
  pivot=next((j for j in range(r,2) if a[j][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  u=pow(a[r][c],-1,P)
  a[r]=[u*z%P for z in a[r]]
  for s in range(2):
   if s!=r and a[s][c]:
    v=a[s][c]
    a[s]=[(x-v*y)%P for x,y in zip(a[s],a[r])]
  r+=1
  if r==2:break
 assert r==2
 return tuple(map(tuple,a))

allp=set(pencils)
assert len(allp)==3820
matrices={normalize(m) for m in product(range(P),repeat=4) if (m[0]*m[3]-m[1]*m[2])%P}
assert len(matrices)==120
orbits=[]
remaining=set(allp)
while remaining:
 rep=min(remaining)
 orb={rowreduce((transformed(m,rep[0]),transformed(m,rep[1]))) for m in matrices}
 assert orb<=allp
 remaining.difference_update(orb)
 orbits.append((rep,len(orb),120//len(orb),degree_hom_gcd(*rep)))
print('RREF_ORBITS',len(orbits),Counter(t[1] for t in orbits),flush=True)
assert len(orbits)==47
assert Counter(size for _,size,_,_ in orbits)=={120:20,60:21,40:3,20:1,10:2}

# Alternative irreducible-factor table for splitting profiles.
def is_irred(f):
  d=len(f)-1
  for k in range(1,d//2+1):
   for cs in product(range(P),repeat=k):
    if not rem(f,list(cs)+[1]):return False
  return True
IRR=[]
for d in range(1,5):
 for cs in product(range(P),repeat=d):
  f=list(cs)+[1]
  if is_irred(f):IRR.append(f)
assert Counter(len(f)-1 for f in IRR)=={1:5,2:10,3:40,4:150}

def split(f):
 a=clean(list(f[::-1]))
 inf=4-(len(a)-1)
 assert inf in (0,1)
 types=[1]*inf
 for g in IRR:
  while len(a)>1 and not rem(a,g):
   types.append(len(g)-1)
   # monic div quotient
   x=clean(a);q=[0]*(len(x)-len(g)+1)
   while len(x)>=len(g):
    k=len(x)-len(g);v=x[-1];q[k]=v
    for j in range(len(g)):x[j+k]=(x[j+k]-v*g[j])%P
    x=clean(x)
   assert not x
   a=clean(q)
 assert len(a)==1 and sum(types)==4,(f,types,a)
 return tuple(sorted(types))
profiles=Counter()
for a,b in pencils:
 members=[tuple((a[i]+t*b[i])%P for i in range(5)) for t in range(P)]+[b]
 profiles[tuple(sorted(split(f) for f in members))]+=1
print('RREF_PROFILES',len(profiles),sorted(profiles.values()),flush=True)
assert len(profiles)==14
with open('verify_reference.generated.json','w') as out:
 json.dump({'n_pencils':len(pencils),'base_degrees':dict(sorted(G.items())),'orbit_size_counts':dict(sorted(Counter(v[1] for v in orbits).items())),'orbits':orbits,'profiles':[{'profile':p,'count':n} for p,n in sorted(profiles.items())]},out,indent=2)
print('INDEPENDENT_VERIFY_PASS',flush=True)
