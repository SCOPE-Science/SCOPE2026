"""Pure-Python independent GF(2) Groebner verifier for bivariate polynomial ideals."""
import json,time
from collections import Counter
D=json.load(open('orbits.json'))
terms=D['terms'];a,b=D['A'],D['B']

def add(p,q):return p.symmetric_difference(q)
def mul_mon(p,m):return {(i+m[0],j+m[1]) for i,j in p}
def lead(p):return max(p) # lex u>v

def div_remainder(f,G):
 f=set(f);r=set()
 while f:
  h=lead(f)
  for g in G:
   k=lead(g)
   if h[0]>=k[0] and h[1]>=k[1]:
    f ^=mul_mon(g,(h[0]-k[0],h[1]-k[1]));break
  else:
   f.remove(h);r.add(h)
 return r

def unitideal(gens):
 G=[]
 for f in gens:
  if f:
   rem=div_remainder(f,G)
   if rem:
    if rem=={(0,0)}:return True
    G.append(rem)
 pairs={(i,j) for i in range(len(G)) for j in range(i)}
 while pairs:
  i,j=pairs.pop();fi,fj=G[i],G[j];li,lj=lead(fi),lead(fj)
  # coprime leading monomials criterion
  if li[0]+lj[0]==max(li[0],lj[0]) and li[1]+lj[1]==max(li[1],lj[1]):continue
  l=(max(li[0],lj[0]),max(li[1],lj[1]))
  sp=mul_mon(fi,(l[0]-li[0],l[1]-li[1]))^mul_mon(fj,(l[0]-lj[0],l[1]-lj[1]))
  rem=div_remainder(sp,G)
  if rem:
   if rem=={(0,0)}:return True
   j0=len(G)
   for k in range(j0):pairs.add((j0,k))
   G.append(rem)
 return False

def gen_poly(mask,xc,yc):
 p=set()
 for k,(i,j) in enumerate(terms):
  if mask>>k&1:
   e=(i if xc==0 else a-i, j if yc==0 else b-j)
   if e in p:p.remove(e)
   else:p.add(e)
 return p

def deriv(p,which):
 if which==0:return {(i-1,j) for i,j in p if i%2==1}
 return {(i,j-1) for i,j in p if j%2==1}

def is_smooth(mask):
 for xc in range(2):
  for yc in range(2):
   f=gen_poly(mask,xc,yc)
   if not unitideal([f,deriv(f,0),deriv(f,1)]):return False
 return True
start=time.monotonic();count=0;sizecounter=Counter();bad=0
for n,(size,mask) in enumerate(D['orbits']):
 v=is_smooth(mask)
 if v:count+=size;sizecounter[size]+=1
 if n%20==0:print('processed',n,'time',round(time.monotonic()-start,1),flush=True)
print('TOTAL',count,'ORBIT_COUNTS',dict(sizecounter),'elapsed',round(time.monotonic()-start,1))
assert count==2304 and sizecounter=={36:55,18:15,12:3,6:3}
