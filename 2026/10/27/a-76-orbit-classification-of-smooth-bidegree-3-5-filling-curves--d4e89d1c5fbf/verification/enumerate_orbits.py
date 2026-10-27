import itertools,time,json
from collections import Counter
A,B=3,5
M=(A+1)*(B+1)
terms=[(i,j) for i in range(A+1) for j in range(B+1)]
pts=((1,0),(1,1),(0,1))
def bit(v,ex):return v**ex

def mono_eval(i,j,p,q,dx=0,dy=0):
 x0,x1=p; y0,y1=q
 if dx==0: u=(x0**(A-i))*(x1**i)
 elif dx==1: u=(i%2)*x0**(A-i)*x1**(i-1) if i else 0
 elif dx==2: u=((A-i)%2)*x0**(A-i-1)*x1**i if A-i else 0
 if dy==0: v=y0**(B-j)*y1**j
 elif dy==1: v=(j%2)*y0**(B-j)*y1**(j-1) if j else 0
 elif dy==2: v=((B-j)%2)*y0**(B-j-1)*y1**j if B-j else 0
 return u*v&1

def mask(p,q,dx=0,dy=0):return sum(mono_eval(i,j,p,q,dx,dy)<<n for n,(i,j) in enumerate(terms))
constraints=[]; deriv=[]
for p in pts:
 for q in pts:
  constraints.append(mask(p,q))
  deriv.append((mask(p,q,2 if p==(0,1) else 1,0),mask(p,q,0,2 if q==(0,1) else 1)))
def ker_basis(ms):
 rows=ms[:]; piv={}
 for v in rows:
  while v:
   k=v.bit_length()-1
   if k not in piv: piv[k]=v;break
   v^=piv[k]
 free=[i for i in range(M) if i not in piv]
 vec=[]
 for j in free:
  v=1<<j
  for k in sorted(piv):
   if (piv[k]&v).bit_count()%2:v ^=1<<k
  assert all((v&m).bit_count()%2==0 for m in rows)
  vec.append(v)
 return vec
basis=ker_basis(constraints)
print('rank',M-len(basis),'dim',len(basis),flush=True)
valid=[];allcand=[]
for k in range(1<<len(basis)):
 v=0
 for i,z in enumerate(basis):
  if k>>i&1:v^=z
 allcand.append(v)
 if all(any((v&m).bit_count()%2 for m in pair) for pair in deriv):valid.append(v)
print('total',len(allcand),'rationally smooth',len(valid),flush=True)
# transformations basis x->(x1,x0) swap, x->(x0,x0+x1) translation
# in char2 polynomial expansion tensor. generate 24 bit linear transforms.
from math import comb
def x_transform(swap,translation):
 outs=[]
 for n,(i,j) in enumerate(terms):
  # monomial x0^(A-i) x1^i transforms
  if swap:
   poly={(i,A-i):1} # powers x0,x1 after swap
  elif translation:
   poly={}
   for t in range(i+1):
    if comb(i,t)%2:poly[(A-i+i-t,t)]=1
  else:poly={(A-i,i):1}
  mask0=0
  for (a,b),c in poly.items():
   if c:mask0^=1<<terms.index((b,j))
  outs.append(mask0)
 return outs

def y_transform(swap,translation):
 outs=[]
 for n,(i,j) in enumerate(terms):
  if swap: poly={(j,B-j):1}
  elif translation: poly={(B-t,t):1 for t in range(j+1) if comb(j,t)%2}
  else:poly={(B-j,j):1}
  mask0=0
  for (a,b),c in poly.items():
   if c:mask0^=1<<terms.index((i,b))
  outs.append(mask0)
 return outs
maps=[x_transform(1,0),x_transform(0,1),y_transform(1,0),y_transform(0,1)]
def apply(v,T):
 out=0
 while v:
  z=v&-v;out ^= T[z.bit_length()-1];v^=z
 return out
V=set(valid)
for v in valid[:200]:
 for t in maps:assert apply(v,t) in V,(v,apply(v,t))
unseen=set(valid);orbits=[]
while unseen:
 v=min(unseen);unseen.remove(v);orb={v};front=[v]
 while front:
  w=front.pop()
  for T in maps:
   u=apply(w,T)
   if u not in orb:
    assert u in V
    orb.add(u);front.append(u);unseen.remove(u)
 orbits.append(sorted(orb))
print('rational-smooth orbit sizes',Counter(map(len,orbits)),'n=',len(orbits),flush=True)
with open('orbits.json','w') as f:json.dump({'A':A,'B':B,'terms':terms,'all_candidates':len(allcand),'rational_smooth_count':len(valid),'orbits':[[len(q),min(q)] for q in orbits]},f)
