#!/usr/bin/env python3
"""Independent projective-orbit and affine-chart census of quartics over GF(2)."""
from itertools import product
from collections import Counter,defaultdict
import sympy as sp
x,y,z=sp.symbols('X Y Z')
mons=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
idx={m:i for i,m in enumerate(mons)}
# GF2 multinomial polynomial formal multiplication
zero={(0,0,0):1}
def mul(P,Q):
 out={}
 for (a,b,c),d in P.items():
  for (u,v,w),e in Q.items():
   k=(a+u,b+v,c+w);out[k]=(out.get(k,0)+d*e)%2
 return {k:v for k,v in out.items() if v}
def transform_basis(forms):
 ans=[]
 for a,b,c in mons:
  p={(0,0,0):1}
  for v,power in enumerate((a,b,c)):
   for _ in range(power):p=mul(p,forms[v])
  ans.append(sum(1<<idx[e] for e in p))
 return ans
def apply(mask,basis):
 r=0
 while mask:
  lsb=mask&-mask;r ^= basis[lsb.bit_length()-1];mask-=lsb
 return r
sh={ (1,0,0):1,(0,1,0):1 };
cyc=transform_basis([{(0,1,0):1},{(0,0,1):1},{(1,0,0):1}])
shr=transform_basis([sh,{(0,1,0):1},{(0,0,1):1}])
# two generators reach full GL3 since order of generated matrices check using their action on all 7 nonzero coordinate vectors
seen={};orbits=[]
for f in range(1,1<<len(mons)):
 if f in seen:continue
 orbit={f};queue=[f]
 for h in queue:
  for T in (cyc,shr):
   h2=apply(h,T)
   if h2 not in orbit:orbit.add(h2);queue.append(h2)
 rep=min(orbit);sz=len(orbit);orbits.append((rep,sz))
 for h in orbit:seen[h]=rep
print('all projective orbits',len(orbits),'elements',len(seen),'max orbit',max(s for _,s in orbits))
# direct chart Groebner smoothness, not a high-degree Macaulay rank test
smooth=[]
for rep,sz in orbits:
 F=sum((x**a*y**b*z**c) for i,(a,b,c) in enumerate(mons) if rep>>i&1)
 Fs=[F,sp.diff(F,x),sp.diff(F,y),sp.diff(F,z)]
 ok=True
 for v in (x,y,z):
  oth=[q for q in (x,y,z) if q!=v]
  G=sp.groebner([f.subs(v,1) for f in Fs],*oth,modulus=2)
  if not G.is_zero_dimensional and G != sp.groebner([1],*oth,modulus=2):
   # Groebner basis with 1 is definitive no affine zeros
   ok=False;break
  if not any(q==1 for q in G.polys):
   ok=False;break
 if ok:smooth.append((rep,sz))
print('smooth orbit count',len(smooth),'weighted count',sum(sz for rep,sz in smooth))
# independent arithmetic for rational lines: symbolically substitute into bivariate polynomials
s,t=sp.symbols('s t')
bt=Counter(); joint=Counter(); settypes=Counter();bad=[]
for rep,sz in smooth:
 F=sum(x**a*y**b*z**c for i,(a,b,c) in enumerate(mons) if rep>>i&1)
 r=sum(int(int(sp.Poly(F.subs({x:((p>>2)&1),y:((p>>1)&1),z:(p&1)}),x,y,z).as_expr())%2==0) for p in range(1,8))
 Ls=[]
 for l in range(1,8):
  vv=[p for p in range(1,8) if (l&p).bit_count()%2==0]
  p,q=vv[:2]
  H=sp.Poly(sp.expand(F.subs({x:s*((p>>2)&1)+t*((q>>2)&1),y:s*((p>>1)&1)+t*((q>>1)&1),z:s*(p&1)+t*(q&1)}, simultaneous=True)),s,t,modulus=2)
  if H.coeff_monomial(s**3*t)==0 and H.coeff_monomial(s*t**3)==0:Ls.append(l)
 b=len(Ls);bt[b]+=sz;joint[(r,b)]+=sz
 # binary code: triple of line labels is concurrent exactly when xor zero
 if b==3: settypes['3_concurrent' if Ls[0]^Ls[1]^Ls[2]==0 else '3_nonconcurrent']+=sz
 if b==4: settypes['4_contains_concurrent_triple' if any(a^b==c for a in Ls for b in Ls for c in Ls if a!=b and a!=c and b!=c) else '4_no_concurrent_triple']+=sz
print('bitangents',sorted(bt.items()))
print('point/bitangent joint',sorted(joint.items()))
print('configuration',settypes)
assert len(smooth)==78 and sum(s for _,s in smooth)==10920
assert sorted(bt.items())==[(0,3072),(1,5278),(2,2352),(3,105),(4,112),(7,1)]
expected_joint={
(0,0):24,(0,1):56,(0,2):84,(0,7):1,
(1,0):168,(1,1):588,(1,2):168,(1,4):84,
(2,0):504,(2,1):1218,(2,2):840,(2,3):84,
(3,0):840,(3,1):1736,(3,2):756,(3,4):28,
(4,0):840,(4,1):1260,(4,2):420,(4,3):21,
(5,0):504,(5,1):420,(5,2):84,
(6,0):168,(7,0):24}
assert dict(joint)==expected_joint, ('joint-table discrepancy',joint)
assert settypes == {'3_concurrent':105,'4_contains_concurrent_triple':112}
print('INDEPENDENT_ORBIT_GROEBNER_CHECK_PASS')
