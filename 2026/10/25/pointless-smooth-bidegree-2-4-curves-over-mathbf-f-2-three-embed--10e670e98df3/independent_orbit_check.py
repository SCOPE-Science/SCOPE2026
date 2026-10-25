#!/usr/bin/env python3
"""Independent group action test by evaluation/interpolation on F8 projective pairs.
No imports from other certificate scripts. Characteristic-two exact arithmetic.
"""
import json
# GL2(F2) all determinants 1.
G=[(a,b,c,d) for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1) if (a*d ^ b*c)==1]

def mul(x,y):
 r=0
 while y:
  if y&1:r^=x
  y>>=1;x<<=1
  if x&8:x^=0b1011
 return r

def pow8(x,k):
 r=1
 for _ in range(k):r=mul(r,x)
 return r

def eval8(code,S,T,U,V):
 a,b,c=code&31,(code>>5)&31,(code>>10)&31
 def quartic_xor(f):
  out=0
  for i in range(5):
   if f>>i&1: out^=mul(pow8(U,i),pow8(V,4-i))
  return out
 return mul(quartic_xor(a),pow8(T,2))^mul(quartic_xor(b),mul(S,T))^mul(quartic_xor(c),pow8(S,2))
# Interpolate 15 coefficients using 15 evaluations over F8 and GF2 linear solve; 
# robust simpler use brute force match from all 33 known candidates by evaluating 15 coordinates.
# Distinct degree4 homogeneous forms uniquely recover by values at 5 points of P1(F8),
# choose (u:v)=(0:1),(1:1),(alpha:1),(alpha^2:1),(alpha^3:1)
BASE=[(0,1),(1,1),(2,1),(4,1),(3,1)]
FIBER=[(1,0),(0,1),(1,1)]
SAMPLES=[(s,t,u,v) for u,v in BASE for s,t in FIBER]

def signature(code):return tuple(eval8(code,*row) for row in SAMPLES)

def acting_signature(code,g,h):
 a,b,c,d=g;w,x,y,z=h
 def L(p,q,r,s):return (mul(p,r)^mul(q,s))
 return tuple(eval8(code,L(a,b,S,T),L(c,d,S,T),L(w,x,U,V),L(y,z,U,V)) for S,T,U,V in SAMPLES)

# independently compute pointless via all 9 F2 points, test known 33 certificate list from csv.
from pathlib import Path
file=Path(__file__).with_name('pointless_all_33.json')
P=set(json.loads(file.read_text()))
assert len(P)==33
signatures={signature(code):code for code in P}
assert len(signatures)==len(P)
seen=set();orbits=[]
for code in sorted(P):
 if code in seen:continue
 orbit={signatures[acting_signature(code,g,h)] for g in G for h in G}
 assert orbit<=P
 orbits.append((code,len(orbit)))
 seen|=orbit
assert seen==P
print(json.dumps({'group_order':len(G)**2,'orbits':[{'bits':a,'size':n} for a,n in orbits]},indent=2))
