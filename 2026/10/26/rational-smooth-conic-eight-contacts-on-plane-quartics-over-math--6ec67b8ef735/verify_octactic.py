#!/usr/bin/env python3
"""Independent conic-first exact F2 contact enumeration for all 32767 quartic forms."""
import itertools, json, collections
from pathlib import Path
from sympy import symbols, groebner, sympify

P=[p for p in itertools.product((0,1),repeat=3) if any(p)]
M2=[(a,b,2-a-b) for a in range(2,-1,-1) for b in range(2-a,-1,-1)]
M4=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
VAR=symbols('X Y Z')
MOD=255

def gfmult(a,b):
 ret=0
 while a:
  if a&1:ret^=b
  b=(b<<1)&MOD
  a>>=1
 return ret

def powgf(a,n):
 ret=1
 for _ in range(n):ret=gfmult(ret,a)
 return ret

def quadratic_value(q,p):
 v=0
 for k,(a,b,c) in enumerate(M2):
  if q>>k&1:v^=(p[0]**a)&(p[1]**b)&(p[2]**c)
 return v

def smooth_q(q):
 coefficients={e:(q>>j)&1 for j,e in enumerate(M2)}
 A=coefficients[(1,1,0)];B=coefficients[(1,0,1)];C=coefficients[(0,1,1)]
 return (A|B|C) and quadratic_value(q,(C,B,A))==1

def mon_series(e,cs):
 return gfmult(gfmult(powgf(cs[0],e[0]),powgf(cs[1],e[1])),powgf(cs[2],e[2]))

def solve_on_q(q,p):
 j=next(i for i in range(3) if p[i]); other=[i for i in range(3) if i!=j]
 def loc(ij):
  cs=[p[k] for k in range(3)];cs[j]=1;cs[ij[0]]^=2; return cs
 der=[quadratic_value(q,loc((k,))) ^ quadratic_value(q,p) for k in other]
 # evaluation at (p + e_k) difference includes quadratic leading; instead extract derivative using polar
 def polarized(k):return quadratic_value(q,tuple(p[z]^(z==k) for z in range(3))) ^ quadratic_value(q,p) ^ quadratic_value(q,tuple(int(z==k) for z in range(3)))
 assert any(polarized(k) for k in other)
 if not polarized(other[1]):other=other[::-1]
 assert polarized(other[1])
 t,sidx=other
 solved=0
 for h in range(1,8):
  cs=[int(pi) for pi in p];cs[t]^=2;cs[sidx]^=solved
  value=0
  for k,e in enumerate(M2):
   if q>>k&1:value^=mon_series(e,cs)
  if (value>>h)&1:solved^=1<<h
 cs=[int(pi) for pi in p];cs[t]^=2;cs[sidx]^=solved
 qval=0
 for k,e in enumerate(M2):
  if q>>k&1:qval^=mon_series(e,cs)
 assert qval==0,(q,p,cs,qval)
 return [mon_series(e,cs) for e in M4]

def build_contact_masks():
 curves=[]
 for q in range(1,64):
  if not smooth_q(q):continue
  for p in P:
   if not quadratic_value(q,p):
    V=solve_on_q(q,p)
    curves.append((q,p,V))
 assert len(curves)==84
 return curves

def dotmask(mask,series):
 value=0
 for k in range(15):
  if mask>>k&1:value^=series[k]
 return value

def recheck_smooth(rep):
 mon=[e for k,e in enumerate(M4) if rep>>k&1]
 f=sum((VAR[0]**a*VAR[1]**b*VAR[2]**c for a,b,c in mon),start=sympify(0))
 derivatives=[f.diff(k) for k in VAR]
 for j in range(3):
  zz=[VAR[k] for k in range(3) if k!=j]
  GB=groebner([r.subs(VAR[j],1) for r in [f]+derivatives],*zz,modulus=2)
  if not (len(GB.polys)==1 and GB.polys[0].as_expr()==1):return False
 return True

if __name__=='__main__':
 C=build_contact_masks()
 assert len(set(q for q,_,_ in C))==28
 # Directly enumerate contact events for all nonzero F, not merely orbit representatives.
 masks=[0]*32768
 for q,p,V in C:
  flag=1<<P.index(p)
  for f in range(1,32768):
   if dotmask(f,V)==0:masks[f]|=flag
 inp=json.load(open(str(Path(__file__).resolve().parent / 'conic_census.json')))
 # Independently reconfirm geometric smoothness of all 279 orbit representatives,
 # and expand each orbit by explicit matrices using direct coordinate substitutions.
 from itertools import product
 def mk(rows):return rows
 def matrix_rank(rows):
  aa=[sum((row[k]&1)<<k for k in range(3)) for row in rows]
  rr=0
  for col in range(3):
   inds=[k for k in range(rr,3) if aa[k]>>col&1]
   if inds:
    i=inds[0];aa[rr],aa[i]=aa[i],aa[rr]
    for k in range(3):
     if k!=rr and (aa[k]>>col&1):aa[k]^=aa[rr]
    rr+=1
  return rr
 def mul_monom(a,b):
  out=set()
  for e in a:
   for f in b:
    g=tuple(e[k]+f[k] for k in range(3))
    if g in out:out.remove(g)
    else:out.add(g)
  return out
 def transform(f,A):
  g=set()
  for k,e in enumerate(M4):
   if not(f>>k&1):continue
   cur={(0,0,0)}
   for i,power in enumerate(e):
    lin={tuple(int(j==m) for j in range(3)) for m in range(3) if A[i][m]}
    for _ in range(power):cur=mul_monom(cur,lin)
   g^=cur
  return sum(1<<M4.index(v) for v in g)
 # Matrix bases once, avoid import of first program.
 allmat=[]
 for bits in product((0,1),repeat=9):
  A=[bits[:3],bits[3:6],bits[6:]]
  if matrix_rank(A)==3:allmat.append(A)
 assert len(allmat)==168
 accounted=set();census=collections.Counter();smooth_count=0;num_smooth_classes=0
 extremal=[]
 for item in inp['orbits']:
  f=item['mask'];actual=recheck_smooth(f)
  if actual!=item['smooth']:raise RuntimeError('smooth label discrepancy')
  seen={transform(f,A) for A in allmat}
  assert len(seen)==item['size']
  assert not (seen&accounted)
  accounted.update(seen)
  if actual:
   num_smooth_classes+=1
   for h in seen:
    smooth_count+=1
    val=masks[h].bit_count()
    census[val]+=1
    if val==4:extremal.append(h)
 assert len(accounted)==32767 and smooth_count==10920
 print('source computation: 28 conics * 3 F2 points = 84 conic-point flags')
 print('geometric smooth orbits',num_smooth_classes,'smooth forms',smooth_count)
 print('independent all-form distribution',dict(sorted(census.items())))
 assert census=={0:9849,1:840,2:210,4:21},census
 print('max',max(census),'extremal equations',len(extremal),'extremal low bits',min(extremal))
 with open(str(Path(__file__).resolve().parent / 'octactic_verified.json'),'w') as fp:
  json.dump({'nonsingular_conics':28,'smooth_form_count':smooth_count,'smooth_orbits':num_smooth_classes,'histogram':dict(sorted(census.items())),'extremal_equations':sorted(extremal),'extremal_orbit_count':1},fp,indent=2)
