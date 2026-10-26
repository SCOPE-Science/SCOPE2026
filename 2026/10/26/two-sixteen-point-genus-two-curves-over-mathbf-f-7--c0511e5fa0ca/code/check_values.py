#!/usr/bin/env python3
"""Exact finite-field enumeration of completely split smooth genus-two models over F7.
Only standard-library arithmetic is used. Run: python3 code/check_values.py
"""
from itertools import product
import json
Q=7
S=(1,2,4)

def trim(a):
 a=[int(x)%7 for x in a]
 while a and a[-1]==0:a.pop()
 return a

def mul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  for j,bj in enumerate(b):z[i+j]=(z[i+j]+ai*bj)%7
 return trim(z)

def rem(a,b):
 a=trim(a); b=trim(b)
 assert b
 while len(a)>=len(b) and a:
  factor=a[-1]*pow(b[-1],-1,7)%7
  shift=len(a)-len(b)
  for j,x in enumerate(b):a[shift+j]=(a[shift+j]-factor*x)%7
  a=trim(a)
 return a

def gcd(a,b):
 a=trim(a);b=trim(b)
 while b:a,b=b,rem(a,b)
 if a:
  z=pow(a[-1],-1,7)
  a=[(x*z)%7 for x in a]
 return a

def squarefree(a):
 return gcd(a,[(i*a[i])%7 for i in range(1,len(a))])==[1]

# Explicit Lagrange basis on all seven finite base points.
lagranges=[]
for j in range(7):
 p=[1]
 for k in range(7):
  if k!=j:p=mul(p,[(-k)%7,1])
 denominator=1
 for k in range(7):
  if k!=j:denominator=denominator*(j-k)%7
 inv=pow(denominator,-1,7)
 lagranges.append([(c*inv)%7 for c in p])

def interpolate(v):
 a=[sum(v[j]*lagranges[j][i] for j in range(7))%7 for i in range(7)]
 assert a[6]==v[7]
 return tuple(a)

split_sequences=[v for v in product(S,repeat=8) if sum(v)%7==0]
assert len(split_sequences)==924
smooth_seqs={v:interpolate(v) for v in split_sequences if squarefree(interpolate(v))}
assert len(smooth_seqs)==588

# Explicit PGL2(F7) action on 8 rational points, with homogeneity-six
# factors equal to 1 by Fermat's theorem.
points=[(x,1) for x in range(7)]+[(1,0)]
matrices=set()
for v in product(range(7),repeat=4):
 a,b,c,d=v
 if (a*d-b*c)%7==0:continue
 t=pow(next(x for x in v if x),-1,7)
 matrices.add(tuple(t*x%7 for x in v))
assert len(matrices)==336
perms=[]
for a,b,c,d in sorted(matrices):
 perm=[]
 for x,z in points:
  u=(a*x+b*z)%7; w=(c*x+d*z)%7
  if w:perm.append((u*pow(w,-1,7))%7)
  else:perm.append(7)
 perms.append(tuple(perm))
assert len(set(perms))==336

def action_orbit(v):
 return {tuple(s*v[p]%7 for p in perm) for perm in perms for s in S}

unseen=set(smooth_seqs)
orbits=[]
while unseen:
 v=min(unseen)
 orbit=action_orbit(v)
 assert orbit<=smooth_seqs.keys()
 unseen.difference_update(orbit)
 orbits.append({'orbit_size':len(orbit),'min_value_sequence':v,'min_model':smooth_seqs[v]})
assert sorted(d['orbit_size'] for d in orbits)==[84,504]

# The simple models are in distinct orbits.
models=[(1,0,0,0,0,0,1),(4,0,3,0,3,0,1)]
# second polynomial f(x)=x^6+3x^4+3x^2+4
models=[(1,0,0,0,0,0,1),(4,0,3,0,3,0,1)]

def eval_model(a,x):
 v=0
 for c in a[::-1]:v=(v*x+c)%7
 return v

def values(a):return tuple(eval_model(a,x) for x in range(7))+(a[-1],)
res=[]
for a in models:
 v=values(a)
 assert v in smooth_seqs
 orb=action_orbit(v)
 assert len(orb) in (84,504)
 # GF49=F7[u]/(u^2-3), 3 nonsquare in F7.
 def multiply(z,w):return ((z[0]*w[0]+3*z[1]*w[1])%7,(z[0]*w[1]+z[1]*w[0])%7)
 def evaluate49(x):
  y=(0,0)
  for c in a[::-1]:
   y=multiply(y,x)
   y=((y[0]+c)%7,y[1])
  return y
 n49=2 # both points at infinity
 for x in product(range(7),repeat=2):
  z=evaluate49(x)
  norm=(z[0]*z[0]-3*z[1]*z[1])%7
  n49+=2 if norm in S else 1 if norm==0 else 0
 a2=(14+n49)//2
 res.append({'coefficients_low_first':a,'orbit_size':len(orb),'automorphisms':2*1008//len(orb),'points_F7':16,'points_F49':n49,'Weil_coefficients_descending':[1,8,a2,56,49]})
assert sorted(x['orbit_size'] for x in res)==[84,504]
assert sorted(x['points_F49'] for x in res)==[44,46]
print(json.dumps({'split_polynomials':len(split_sequences),'smooth_polynomials':len(smooth_seqs),'projective_matrices':len(matrices),'orbits':sorted(res,key=lambda r:r['orbit_size'])},sort_keys=True,indent=2))
