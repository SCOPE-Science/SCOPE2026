#!/usr/bin/env python3
"""Exact classification of rational tangent-contact orders of smooth quartics over F2."""
import itertools,collections,json,sys
from pathlib import Path
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
xs=(X,Y,Z)
exps=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
assert len(exps)==15
inds={e:i for i,e in enumerate(exps)}
pts=tuple(p for p in itertools.product(range(2),repeat=3) if any(p))

def mul(p,q):
 out=0
 for a in range(3):
  if p>>a&1:
   for b in range(3):
    if q>>b&1:
     out^=1<<(a+b)
 return out

def rank3(cols):
 def det(m):
  a,b,c=m
  return ((a[0]&b[1]&c[2])^(a[0]&b[2]&c[1])^(a[1]&b[0]&c[2])^(a[1]&b[2]&c[0])^(a[2]&b[0]&c[1])^(a[2]&b[1]&c[0]))
 return det([[cols[j][i] for j in range(3)] for i in range(3)])

GL=[cs for cs in itertools.product(pts,repeat=3) if rank3(cs)]
assert len(GL)==168

def multpoly(a,b):
 c=collections.Counter()
 for x,y,z in a:
  for X0,Y0,Z0 in b: c[(x+X0,y+Y0,z+Z0)]^=1
 return {k for k,v in c.items() if v%2}

def prod3(sets):
 r={(0,0,0)}
 for st in sets:r=multpoly(r,st)
 return r

def mat_action(cs):
 # cs are column images of input coordinate vectors. substituting linear forms L_i= sum cs[j][i] xi
 ls=[{tuple(1 if t==j else 0 for t in range(3)) for j in range(3) if cs[j][i]} for i in range(3)]
 table=[]
 for a,b,c in exps:
  f=prod3([ls[0]]*a+[ls[1]]*b+[ls[2]]*c)
  table.append(sum(1<<inds[e] for e in f))
 return table

ACTIONS=[mat_action(cs) for cs in GL]
assert len(set(tuple(t) for t in ACTIONS))==168

def action(mask,table):
 out=0
 while mask:
  bit=mask&-mask;out^=table[bit.bit_length()-1];mask^=bit
 return out

def poly(mask):
 return sp.Add(*(xs[0]**a*xs[1]**b*xs[2]**c for i,(a,b,c) in enumerate(exps) if mask>>i&1))

def smooth(mask):
 f=poly(mask)
 for k in range(3):
  ff=sp.Poly(f.subs(xs[k],1),*[xs[j] for j in range(3) if j!=k],modulus=2).as_expr()
  xx=[xs[j] for j in range(3) if j!=k]
  if not sp.groebner([ff,sp.diff(ff,xx[0]),sp.diff(ff,xx[1])],*xx,modulus=2).contains(sp.Integer(1)):return False
 return True

def eval_monomial(exp,p):return all(not e or p[j] for j,e in enumerate(exp))

def tangent_contact(mask,p):
 active=[exps[i] for i in range(15) if mask>>i&1]
 if sum(eval_monomial(e,p) for e in active)%2:return None
 grad=[]
 for j in range(3):
  grad.append(sum((e[j]%2)*eval_monomial(tuple(e[t]-int(j==t) for t in range(3)),p) for e in active if e[j]%2)%2)
 if not any(grad):return 'singular'
 linept=[q for q in pts if q!=p and not sum(grad[j]*q[j] for j in range(3))%2][0]
 # F(P+t*Q); coefficient t^k via binomial parity
 coeff=[0]*5
 for e in active:
  choices=[]
  for j in range(3):
   v=[]
   for k in range(e[j]+1):
    if (k&e[j])==k and (e[j]==k or p[j]) and (not k or linept[j]):v.append(k)
   choices.append(v)
  for triple in itertools.product(*choices):coeff[sum(triple)]^=1
 assert coeff[0]==0 and coeff[1]==0, (mask,p,coeff)
 return next((k for k in range(2,5) if coeff[k]),'line')

def calc():
 unseen=set(range(1,1<<15)); reps=[]
 while unseen:
  m=min(unseen); orbit={action(m,A) for A in ACTIONS};unseen.difference_update(orbit)
  reps.append((m,len(orbit)))
 print('orbits total',len(reps),flush=True)
 accepted=[];prof=collections.Counter(); smoothforms=0
 for i,(m,n) in enumerate(reps):
  if smooth(m):
   counts=collections.Counter(tangent_contact(m,p) for p in pts)
   assert set(counts).issubset({None,2,3,4})
   sig=(counts[2]+counts[3]+counts[4],counts[2],counts[3],counts[4])
   prof[sig]+=n;smoothforms+=n
   accepted.append({'mask':m,'orbit_size':n,'N':sig[0],'contacts':[sig[1],sig[2],sig[3]]})
  if i%50==0: print('progress',i,flush=True)
 print('smooth',len(accepted),smoothforms,'profiles',len(prof),flush=True)
 print('hist',sorted([(k,v) for k,v in prof.items()]),flush=True)
 obj={'total_orbits':len(reps),'total_forms':(1<<15)-1,'smooth_orbits':len(accepted),'smooth_forms':smoothforms,'profiles':[{'N':k[0],'ordinary':k[1],'flex':k[2],'hyperflex':k[3],'forms':v} for k,v in sorted(prof.items())],'representatives':accepted}
 with open(Path(__file__).resolve().parent/'flex_quartics_data.json','w') as f:json.dump(obj,f,indent=2)

if __name__=='__main__':calc()
