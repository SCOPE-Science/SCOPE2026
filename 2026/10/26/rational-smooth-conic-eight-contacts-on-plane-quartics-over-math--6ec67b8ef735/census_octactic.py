#!/usr/bin/env python3
"""Exact small-field quartic and smooth-conic contact census; all operations in F2."""
import itertools, collections, json, time
from pathlib import Path
from sympy import symbols,groebner,Poly, sympify

N=3
mons4=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
mons2=[(a,b,2-a-b) for a in range(2,-1,-1) for b in range(2-a,-1,-1)]
x,y,z=symbols('x y z'); vars=(x,y,z)
assert len(mons4)==15 and len(mons2)==6

def evalmask(mask, mons, p):
 return sum((mask>>i&1) * (p[0]**a)*(p[1]**b)*(p[2]**c) for i,(a,b,c) in enumerate(mons))%2

def polysmooth(F,exps):
 fx=[]
 for j in range(3):
  fx.append(sum((e[j]%2)*vars[0]**e[0]*vars[1]**e[1]*vars[2]**e[2]/vars[j] if False else (e[j]%2)*vars[0]**(e[0]-(j==0))*vars[1]**(e[1]-(j==1))*vars[2]**(e[2]-(j==2)) for e in exps if e[j]%2))
 for j in range(3):
  vv=[v for k,v in enumerate(vars) if k!=j]
  polys=[sympify(q).subs(vars[j],1) for q in [F]+fx]
  G=groebner(polys,*vv,order='lex',modulus=2)
  if not (len(G.polys)==1 and G.polys[0].as_expr()==1):return False
 return True

def polyprod(p,q):
 o=set()
 for e in p:
  for f in q:
   a=tuple(u+v for u,v in zip(e,f))
   if a in o:o.remove(a)
   else:o.add(a)
 return o

def trans_monom(e,mat):
 # mat row i is linear form replaced for xi
 P={(0,0,0)}
 for j,n in enumerate(e):
  L={(0,0,0)} # no, linear form
  L={(i==0,i==1,i==2) for i in range(3) if mat[j][i]}
  for _ in range(n):P=polyprod(P,L)
 return P

def rank3(mat):
 a=[sum(v<<j for j,v in enumerate(row)) for row in mat]
 for k in range(3):
  ii=next((i for i in range(k,3) if (a[i]>>k)&1),None)
  if ii is None:return False
  a[k],a[ii]=a[ii],a[k]
  for i in range(3):
   if i!=k and ((a[i]>>k)&1):a[i]^=a[k]
 return True

mats=[tuple(tuple(b[(3*i)+j] for j in range(3)) for i in range(3)) for b in itertools.product((0,1),repeat=9) if rank3([b[:3],b[3:6],b[6:]])]
assert len(mats)==168
basis=[]
ind4={e:i for i,e in enumerate(mons4)}
for mat in mats:
 bs=[]
 for e in mons4:
  s=trans_monom(e,mat)
  bs.append(sum(1<<ind4[v] for v in s))
 basis.append(bs)

def transform(mask,bs):
 out=0
 while mask:
  k=(mask &-mask).bit_length()-1
  out^=bs[k]
  mask&=mask-1
 return out

def orbit(mask):return {transform(mask,bs) for bs in basis}

def bivar_terms(mask,mons,p,j,swap):
 # Affine local f(t,s) at p, chart xj=1, remaining coords q0 and q1, swap chooses which is t
 js=[k for k in range(3) if k!=j]
 if swap:js=js[::-1]
 a,b=p[js[0]],p[js[1]]
 # Generate polynomial in (t,s) via expansion on F2 of (a+t)^u (b+s)^v
 out=set()
 from math import comb
 for k,e in enumerate(mons):
  if not (mask>>k&1):continue
  u,v=e[js[0]],e[js[1]]
  for i in range(u+1):
   if comb(u,i)%2 and (a or i==u):
    for h in range(v+1):
     if comb(v,h)%2 and (b or h==v):
      d=(i,h)
      if d in out:out.remove(d)
      else:out.add(d)
 return out

def prod_t(a,b):
 o=0
 while b:
  low=b & -b;k=low.bit_length()-1
  o^=a<<k
  b-=low
 return o&255

def powers(s,lim):
 o=[1]
 for _ in range(lim):o.append(prod_t(o[-1],s))
 return o

def evaluate_bivar(terms,s):
 sp=powers(s,4)
 o=0
 for i,j in terms:o^=(sp[j]<<i)
 return o&255

def local_series(mask,p):
 j=next(i for i in range(3) if p[i]);
 terms=bivar_terms(mask,mons4,p,j,False)
 der_s=(0,1) in terms;der_t=(1,0) in terms
 assert der_s or der_t
 sw=not der_s
 if sw:terms=bivar_terms(mask,mons4,p,j,True)
 assert (0,1) in terms
 s=0
 for k in range(1,8):
  err=(evaluate_bivar(terms,s)>>k)&1
  if err:s^=1<<k
 assert evaluate_bivar(terms,s)==0
 return j,sw,s

def smoothconic(mask):
 # Determine the polar radical and its quadratic value
 co={e:(mask>>i)&1 for i,e in enumerate(mons2)}
 A=co[(1,1,0)];B=co[(1,0,1)];C=co[(0,1,1)]
 if not (A or B or C):return False
 r=(C,B,A)
 return evalmask(mask,mons2,r)==1

def contact8(mask,p,spec):
 j,sw,s=spec
 Q=[]
 for k in range(6):
  terms=bivar_terms(1<<k,mons2,p,j,sw)
  Q.append(evaluate_bivar(terms,s))
 hits=[]
 for q in range(1,64):
  v=0
  for k,a in enumerate(Q):
   if q>>k&1:v^=a
  if v==0 and smoothconic(q):hits.append(q)
 return hits

def main():
 st=time.monotonic();seen=bytearray(32768);orbits=[]
 pts=list(itertools.product((0,1),repeat=3));pts=[p for p in pts if p!=(0,0,0)]
 for mask in range(1,32768):
  if seen[mask]:continue
  orb=orbit(mask)
  for i in orb:seen[i]=1
  exps=[e for i,e in enumerate(mons4) if mask>>i&1]
  F=sum(vars[0]**e[0]*vars[1]**e[1]*vars[2]**e[2] for e in exps)
  is_smooth=polysmooth(F,exps)
  data={'mask':mask,'size':len(orb),'smooth':is_smooth}
  if is_smooth:
   events=[]
   for p in pts:
    if evalmask(mask,mons4,p):continue
    spec=local_series(mask,p)
    hits=contact8(mask,p,spec)
    if hits:events.append({'point':p,'conic_masks':hits,'s':spec})
   data['count']=len(events);data['events']=events
  orbits.append(data)
  if len(orbits)%30==0:print('progress',len(orbits),'time',round(time.monotonic()-st,2),flush=True)
 dist=collections.Counter();nm=0
 for r in orbits:
  if r['smooth']:
   nm+=r['size'];dist[r['count']]+=r['size']
 print('orbits',len(orbits),'smooth orbits',sum(r['smooth'] for r in orbits),'smooth forms',nm,'dist',dict(sorted(dist.items())),'time',round(time.monotonic()-st,2))
 print('positive orbits',[(r['mask'],r['size'],r['count'],r['events']) for r in orbits if r['smooth'] and r['count']])
 with open(str(Path(__file__).resolve().parent / 'conic_census.json'),'w') as f:json.dump({'orbits':orbits,'histogram':dict(dist),'smooth_forms':nm},f,indent=2)

if __name__=='__main__':main()
