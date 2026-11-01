"""Exact verification of generic central-section side counts of a truncated icosahedron."""
from itertools import combinations, product
from collections import Counter
import math

z=(0,0); one=(1,0); ph=(0,1)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def scale(a,c):return a[0]*c,a[1]*c
def sign(a):
 A=2*a[0]+a[1];B=a[1]
 if B==0:return (A>0)-(A<0)
 if A==0:return (B>0)-(B<0)
 if (A>0)==(B>0):return (A>0)-(A<0)
 q=A*A-5*B*B
 assert q!=0
 return ((q>0)-(q<0)) * ((A>0)-(A<0))
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vneg(a):return tuple(neg(x) for x in a)
def vsub(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def vmul(a,k):return tuple(scale(x,k) for x in a)
def dot(a,b):
 p=z
 for x,y in zip(a,b):p=add(p,mul(x,y))
 return p
def cross(a,b):
 x,y,z0=a;X,Y,Z=b
 return (sub(mul(y,Z),mul(z0,Y)),sub(mul(z0,X),mul(x,Z)),sub(mul(x,Y),mul(y,X)))
def iszero(a):return all(t==z for t in a)

def construct():
 V=[]
 for a,b in product((-1,1),repeat=2):
  V.extend([(z,(a,0),(0,b)),((a,0),(0,b),z),((0,a),z,(b,0))])
 assert len(set(V))==12
 E=[]
 for i,j in combinations(range(12),2):
  if dot(vsub(V[i],V[j]),vsub(V[i],V[j]))==(4,0):E.append((i,j))
 assert len(E)==30,(len(E),E)
 TT=[];lookup={}
 for i,j in E:
  for a,b in ((i,j),(j,i)):
   lookup[(a,b)]=len(TT)
   TT.append(vadd(vmul(V[a],2),V[b]))
 TE=[(lookup[(i,j)],lookup[(j,i)]) for i,j in E]
 ES=set(E)
 for a in range(12):
  nbrs=sorted(j for j in range(12) if (min(a,j),max(a,j)) in ES)
  assert len(nbrs)==5
  for b,c in combinations(nbrs,2):
   if (b,c) in ES:TE.append((lookup[(a,b)],lookup[(a,c)]))
 assert len(TT)==60 and len(TE)==90 and len(set(TT))==60
 assert len(set(tuple(sorted(e)) for e in TE))==90
 assert all(dot(t,t)==(10,9) for t in TT)
 assert all(dot(vsub(TT[i],TT[j]),vsub(TT[i],TT[j]))==(4,0) for i,j in TE)
 degree=Counter(v for e in TE for v in e)
 assert set(degree.values())=={3} and len(degree)==60
 normals=[];key2idx={};tt_sign=[]
 for v in TT:
  canon=min(v,vneg(v));sgn=1 if canon==v else -1
  if canon not in key2idx:
   key2idx[canon]=len(normals);normals.append(canon)
  tt_sign.append((key2idx[canon],sgn))
 assert len(normals)==30
 return V,E,TT,TE,normals,tt_sign

def chambers(normals):
 all_signs=set();projective={};vertices=0;degenerate=0
 for i,j in combinations(range(len(normals)),2):
  u=cross(normals[i],normals[j]);assert not iszero(u)
  base=[dot(v,u) for v in normals]
  incident=tuple(k for k,b in enumerate(base) if b==z)
  assert len(incident)>=2
  if incident in projective:continue
  projective[incident]=1;vertices+=1
  directions=[]
  for k in incident:
   t=cross(u,normals[k]);assert not iszero(t)
   directions.extend((t,vneg(t)))
  local=0
  for v,w in combinations(directions,2):
   tangent=vadd(v,w)
   if iszero(tangent):continue
   sig=[]
   for k,b in enumerate(base):
    x=sign(b) if b!=z else sign(dot(normals[k],tangent))
    if not x:break
    sig.append(x)
   else:
    s=tuple(sig)
    all_signs.add(s);all_signs.add(tuple(-x for x in s));local+=1
  assert local>0
 expect=2+2*sum(len(v)-1 for v in projective)
 assert len(all_signs)==expect,(len(all_signs),expect)
 return all_signs,projective

def classify():
 V,E,TT,TE,normals,tt_sign=construct()
 ss,pr=chambers(normals)
 hist=Counter()
 for s in ss:
  signv=[s[k]*s0 for k,s0 in tt_sign]
  N=sum(signv[a]!=signv[b] for a,b in TE)
  hist[N]+=1
 assert hist==Counter({10:132,12:420,14:180,16:120,18:20}),hist
 assert len(pr)==435 and set(map(len,pr))=={2}
 print('chambers',len(ss),'projective intersections',len(pr),'multiplicity breakdown',dict(Counter(map(len,pr))))
 print('chamber counts by section sides',dict(sorted(hist.items())))
 witnesses={}
 for B in range(1,60):
  for x,y,z0 in product(range(-B,B+1),repeat=3):
   if max(abs(x),abs(y),abs(z0))!=B:continue
   if (x,y,z0)==(0,0,0):continue
   u=((x,0),(y,0),(z0,0))
   s=[sign(dot(v,u)) for v in TT]
   if 0 in s:continue
   N=sum(s[a]!=s[b] for a,b in TE)
   if N in hist and N not in witnesses:witnesses[N]=(x,y,z0)
  if len(witnesses)==len(hist):break
 assert len(witnesses)==5
 print('witnesses',dict(sorted(witnesses.items())))
 phi=(1+5**.5)/2
 alpha=math.acos(1-2/(10+9*phi))
 print('mean section sides 90 alpha/pi',90*alpha/math.pi,'edge angle',alpha)
 print('ALL_CHECKS_PASSED')
if __name__=='__main__':classify()
