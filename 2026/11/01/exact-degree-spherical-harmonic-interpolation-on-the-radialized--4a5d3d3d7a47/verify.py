#!/usr/bin/env python3
"""Exact algebraic and modular checks for radial harmonic sampling."""
from fractions import Fraction as Q
from math import isqrt

class F:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a=Q(a);self.b=Q(b)
    def __add__(u,v):
        if not isinstance(v,F):v=F(v)
        return F(u.a+v.a,u.b+v.b)
    __radd__=__add__
    def __neg__(u):return F(-u.a,-u.b)
    def __sub__(u,v):return u+-v if isinstance(v,F) else u+F(-v)
    def __rsub__(u,v):return -u+v
    def __mul__(u,v):
        if not isinstance(v,F):v=F(v)
        return F(u.a*v.a+u.b*v.b, u.a*v.b+u.b*v.a+u.b*v.b)
    __rmul__=__mul__
    def inv(u):
        den=u.a*u.a+u.a*u.b-u.b*u.b
        assert den
        return F((u.a+u.b)/den,-u.b/den)
    def __truediv__(u,v):return u*(v.inv() if isinstance(v,F) else F(v).inv())
    def __eq__(u,v):
        if not isinstance(v,F):v=F(v)
        return u.a==v.a and u.b==v.b
    def __hash__(u):return hash((u.a,u.b))
    def __repr__(u):return str((u.a,u.b))

PH=F(0,1); THREE=F(3); B2=3*(PH+2)

class K:
    __slots__=('u','v')
    def __init__(self,u=0,v=0):self.u=u if isinstance(u,F) else F(u);self.v=v if isinstance(v,F) else F(v)
    def __add__(a,b):
        if not isinstance(b,K):b=K(b)
        return K(a.u+b.u,a.v+b.v)
    __radd__=__add__
    def __neg__(a):return K(-a.u,-a.v)
    def __sub__(a,b):return a+-b if isinstance(b,K) else a+K(-b)
    def __rsub__(a,b):return -a+b
    def __mul__(a,b):
        if not isinstance(b,K):b=K(b)
        return K(a.u*b.u+B2*a.v*b.v,a.u*b.v+a.v*b.u)
    __rmul__=__mul__
    def inv(a):
        den=(a.u*a.u-B2*a.v*a.v).inv()
        return K(a.u*den,-a.v*den)
    def __truediv__(a,b):return a*(b.inv() if isinstance(b,K) else K(b).inv())
    def __eq__(a,b):
        if not isinstance(b,K):b=K(b)
        return a.u==b.u and a.v==b.v
    def __hash__(a):return hash((a.u,a.v))
    def __repr__(a):return str((a.u,a.v))

Z=F(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
I=[];D=[]
for s in (-1,1):
 for t in (-1,1):
  I.extend(((Z,F(s),t*PH),(F(s),t*PH,Z),(s*PH,Z,F(t))))
edges={(i,j) for i in range(12) for j in range(i+1,12) if dot(tuple(I[i][h]-I[j][h] for h in range(3)),tuple(I[i][h]-I[j][h] for h in range(3)))==4}
assert len(edges)==30
def edge(i,j):return (min(i,j),max(i,j)) in edges
faces=[(i,j,k) for i in range(12) for j in range(i+1,12) for k in range(j+1,12) if edge(i,j) and edge(i,k) and edge(j,k)]
assert len(faces)==20
D=[tuple(I[i][h]+I[j][h]+I[k][h] for h in range(3)) for i,j,k in faces]
DSQ=dot(D[0],D[0]); assert all(dot(v,v)==DSQ for v in D)
B2=(PH+2)*DSQ
assert len(I)==12 and len(D)==20 and len(set(I))==12 and len(set(D))==20

def reps(points):
 seen=set();out=[]
 for x in points:
  if x in seen:continue
  assert neg(x) in points
  seen.add(x);seen.add(neg(x));out.append(x)
 return out
U=reps(I);V=reps(D)
assert len(U)==6 and len(V)==10
Y=U+V
T=[]
for i,a in enumerate(Y):
 row=[]
 for j,b in enumerate(Y):
  c=dot(a,b)
  if i<6 and j<6:row.append(K(c/(PH+2)))
  elif i>=6 and j>=6:row.append(K(c/DSQ))
  else:row.append(K(0,c/B2))
 T.append(row)
assert all(T[i][i]==1 for i in range(16))
assert all(T[i][j]==T[j][i] for i in range(16) for j in range(16))

def exact_rank(M):
 m=[row[:] for row in M];R=0
 for j in range(len(m[0])):
  ix=next((i for i in range(R,len(m)) if m[i][j]!=0),None)
  if ix is None:continue
  m[R],m[ix]=m[ix],m[R]
  z=m[R][j];m[R]=[v/z for v in m[R]]
  for i in range(R+1,len(m)):
   z=m[i][j]
   if z!=0:
    m[i]=[a-z*b for a,b in zip(m[i],m[R])]
  R+=1
  if R==len(m):break
 return R

def legendre_matrices(L=14):
 p0=[[K(1)]*16 for _ in range(16)]
 yield 0,p0
 p1=T
 if L==0:return
 yield 1,p1
 for n in range(1,L):
  nxt=[[( (2*n+1)*T[i][j]*p1[i][j]-n*p0[i][j])/(n+1) for j in range(16)] for i in range(16)]
  yield n+1,nxt
  p0,p1=p1,nxt

def primes(a,b):
 for n in range(a,b):
  if n<2:continue
  if all(n%d for d in range(2,isqrt(n)+1)):yield n

def mod_sqrt(a,p):
 if a%p==0:return 0
 if pow(a,(p-1)//2,p)!=1:return None
 if p%4==3:return pow(a,(p+1)//4,p)
 # Tonelli-Shanks
 q=p-1;s=0
 while q%2==0:q//=2;s+=1
 z=2
 while pow(z,(p-1)//2,p)!=p-1:z+=1
 c=pow(z,q,p); x=pow(a,(q+1)//2,p);t=pow(a,q,p);m=s
 while t!=1:
  i=1;tt=t*t%p
  while tt!=1:tt=tt*tt%p;i+=1
  b=pow(c,1<<(m-i-1),p)
  x=x*b%p;t=t*b*b%p;c=b*b%p;m=i
 return x

def prime_roots(p):
 r=mod_sqrt(5,p)
 if r is None:return None
 for sr in (r,(-r)%p):
  ph=(1+sr)*pow(2,-1,p)%p
  be=mod_sqrt((rationalmod(B2.a,p)+rationalmod(B2.b,p)*ph)%p,p)
  if be is not None and be:return ph,be
 return None

def determinant(A,p):
 M=[row[:] for row in A];z=1;n=len(A)
 for j in range(n):
  i=next((i for i in range(j,n) if M[i][j]%p),None)
  if i is None:return 0
  if i!=j:M[i],M[j]=M[j],M[i];z=-z%p
  d=M[j][j];z=z*d%p;inv=pow(d,p-2,p)
  for i in range(j+1,n):
   fac=M[i][j]*inv%p
   if fac:
    for k in range(j+1,n):M[i][k]=(M[i][k]-fac*M[j][k])%p
 return z

def rationalmod(a,p):return (a.numerator%p)*pow(a.denominator,-1,p)%p

def Kmod(t,p,ph,be):return (rationalmod(t.u.a,p)+rationalmod(t.u.b,p)*ph+be*(rationalmod(t.v.a,p)+rationalmod(t.v.b,p)*ph))%p

def determinants_through(maxdegree=1099,verbose=True,min_degree=15):
 ps=[]
 for p in primes(1201,25000):
  if prime_roots(p):ps.append(p)
  if len(ps)>=8:break
 print('split primes',ps,flush=True)
 good={};need=set(range(min_degree,maxdegree+1))
 for p in ps:
  ph,be=prime_roots(p);Tmod=[[Kmod(t,p,ph,be) for t in row] for row in T]
  p0=[[1]*16 for _ in range(16)];p1=Tmod
  goodcount=0
  for n in range(1,maxdegree):
   inv=pow(n+1,-1,p)
   nxt=[[( (2*n+1)*Tmod[i][j]*p1[i][j]-n*p0[i][j])*inv%p for j in range(16)] for i in range(16)]
   if n+1 in need:
    d=determinant(nxt,p)
    if d:
     good[n+1]=(p,d);goodcount+=1
   p0,p1=p1,nxt
  need-=set(good)
  print('prime',p,'new full rank',goodcount,'remaining',len(need),'sample holes',sorted(need)[:30],flush=True)
  if not need:break
 if need:raise RuntimeError('Uncertified degrees: '+str(sorted(need)))
 if verbose:
  from collections import Counter
  print('counts by prime',Counter(p for p,d in good.values()))
 return good

def interval_bounds():
    rlo=Q(2236067977,10**9);rhi=Q(2236067978,10**9)
    assert rlo*rlo < 5 < rhi*rhi
    phlo=(1+rlo)/2;phhi=(1+rhi)/2
    blo=Q(8625260660,10**9);bhi=Q(8625260680,10**9)
    b2lo,b2hi=(B2.a+min(B2.b*phlo,B2.b*phhi),B2.a+max(B2.b*phlo,B2.b*phhi))
    assert blo*blo < b2lo and b2hi < bhi*bhi
    def fint(f):
        return (f.a+min(f.b*phlo,f.b*phhi),f.a+max(f.b*phlo,f.b*phhi))
    def kint(k):
        ul,uh=fint(k.u); vl,vh=fint(k.v)
        ps=[v*b for v in (vl,vh) for b in (blo,bhi)]
        return ul+min(ps),uh+max(ps)
    closest=[]
    for i in range(16):
        for j in range(16):
            if i!=j:
                lo,hi=kint(T[i][j]);assert -Q(4,5)<lo and hi<Q(4,5),(i,j,lo,hi)
                closest.append(max(abs(lo),abs(hi)))
    return float(max(closest))

def full_certificate():
    # Exact field evaluation gives this complete low-degree table.
    ranks=[1,3,5,7,9,6,10,10,14,10,15,13,15,13,14,13,15,
           16,15,16,15,16,15,16,15,16,15,16,15,16,16,16,
           15,16,15,16,16,16,15,16,16,16,16,16,15]
    assert len(ranks)==45
    assert interval_bounds()<0.8
    actual=[exact_rank(G) for n,G in legendre_matrices(44)]
    assert actual==ranks,(actual,ranks)
    modular=determinants_through(249,min_degree=45,verbose=False)
    assert len(modular)==205
    assert modular[86][0]==1229 and modular[174][0]==1229
    assert all((p==1201 if n not in (86,174) else p==1229)
                and residue for n,(p,residue) in modular.items())
    # For |t|<4/5, sin(theta)>3/5; Bernstein-Legendre with pi>3
    # gives |P_l(t)|<sqrt(10/(9*(l+1/2))). 15 off-diagonals
    # yield row-sum < sqrt(250/(l+1/2))<1 for every l>=250.
    assert Q(250)<Q(501,2)
    return ranks,modular

if __name__=='__main__':
    import sys, time
    begin=time.monotonic()
    ranks,cert=full_certificate()
    print('PASS: exact ranks degrees 0..44:',ranks)
    print('PASS: degrees 45..249, modular determinant witnesses:',len(cert))
    print('PASS: strict diagonal dominance for degrees >=250')
    if '--write-certificate' in sys.argv:
        with open('determinants.csv','w',encoding='utf-8',newline='') as f:
            f.write('degree,prime,determinant_mod_prime\n')
            for n in sorted(cert):
                p,r=cert[n];f.write(f'{n},{p},{r}\n')
    print('Elapsed seconds:',round(time.monotonic()-begin,3))
