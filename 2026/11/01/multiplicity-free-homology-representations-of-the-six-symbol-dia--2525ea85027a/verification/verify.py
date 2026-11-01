#!/usr/bin/env python3
"""Exact rational cellular character verification for a six-symbol rook complex.

Run: python3 verify.py
Requires only Python standard library.
"""
import itertools
import math
import functools
import collections
from fractions import Fraction
n=6
faces={}
for r in range(1,n+1):
 faces[r-1]=[]
 for rows in itertools.combinations(range(n),r):
  for cols in itertools.permutations(range(n),r):
   if all(i!=j for i,j in zip(rows,cols)):
    faces[r-1].append(tuple(sorted(i*n+j for i,j in zip(rows,cols))))
assert [len(faces[k]) for k in range(6)] == [30,315,1420,2715,1854,265]
rows={a:i for i,a in enumerate(faces[3])};base=[];pivot={};coords=[]

for idx,f in enumerate(faces[4]):
 v={rows[f[:i]+f[i+1:]]:Fraction(1 if i%2==0 else -1) for i in range(len(f))}
 coeff={idx:1}
 while v:
  q=min(v);c=v[q]
  if q not in pivot:
   inv=1/c;pivot[q]=({j:z*inv for j,z in v.items()},{j:z*inv for j,z in coeff.items()})
   base.append(idx);coords.append(None);break
  pv,pc=pivot[q]
  for j,z in pv.items():
   w=v.get(j,0)-c*z
   if w:v[j]=w
   elif j in v:del v[j]
  for j,z in pc.items():
   w=coeff.get(j,0)-c*z
   if w:coeff[j]=w
   elif j in coeff:del coeff[j]
 else:
  coeff.pop(idx, None)
  coords.append({j:-z for j,z in coeff.items() if z})

assert len(base)==1557
for j,b in enumerate(base):coords[b]={b:1}
four_index={f:i for i,f in enumerate(faces[4])}
from math import factorial

def partitions(n,maxv=None):
 if n==0:yield ();return
 if maxv is None:maxv=n
 for k in range(min(n,maxv),1-1,-1):
  for rest in partitions(n-k,k):yield(k,)+rest

def permtype(typ):
 x=[None]*n;off=0
 for k in typ:
  for i in range(k):x[off+i]=off+(i+1)%k
  off+=k
 return x

def parity(t):
 return -1 if sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))%2 else 1

def mapped(f,sigma,sw):
 g=[]
 for a in f:
  i,j=divmod(a,n);g.append(n*sigma[j]+sigma[i] if sw else n*sigma[i]+sigma[j])
 order=sorted(range(len(g)),key=lambda i:g[i]);return tuple(g[i] for i in order),parity(order)

def ctr(k,sigma,sw):
 idx={f:i for i,f in enumerate(faces[k])};out=0
 for f in faces[k]:
  nf,sg=mapped(f,sigma,sw)
  if nf==f:out+=sg
 return out
records=[]
for typ in partitions(n):
 sig=permtype(typ)
 for sw in (0,1):
  traces=[ctr(k,sig,sw) for k in range(6)]
  chi_red_euler=sum((-1)**k*traces[k] for k in range(6))-1
  chi_im=0
  for b in base:
   nf,sg=mapped(faces[4][b],sig,sw)
   j=four_index[nf]
   chi_im=chi_im+sg*coords[j].get(b,0)
  chi4=traces[4]-chi_im-traces[5]
  chi3=chi4-chi_red_euler
  records.append((typ,sw,chi3,chi4,tuple(traces),chi_red_euler))
  assert chi3.denominator == chi4.denominator == 1
  print('CHAR',typ,sw,'H3',int(chi3),'H4',int(chi4),'Euler',chi_red_euler)



# Direct reduced-chain modular ranks, independently of rational image-basis selection.
def rank_mod(k,p):
    face_index={f:i for i,f in enumerate(faces[k-1])}
    piv={}
    for f in faces[k]:
        vec={face_index[f[:j]+f[j+1:]]:(1 if j%2==0 else p-1) for j in range(len(f))}
        while vec:
            q=min(vec); coef=vec[q]
            if q not in piv:
                inv=pow(coef,-1,p)
                piv[q]={i:x*inv%p for i,x in vec.items()}
                break
            for i,x in piv[q].items():
                val=(vec.get(i,0)-coef*x)%p
                if val:vec[i]=val
                else:vec.pop(i,None)
    return len(piv)

for prime in (1009,65521):
    ranks=[rank_mod(k,prime) for k in range(1,6)]
    assert ranks==[29,286,1134,1557,265]
    print('MODULAR_RANKS',prime,ranks)

# Chain property: all two-step faces cancel with opposite incidence signs.
for k in range(2,6):
    for f in faces[k]:
        by_low=collections.Counter()
        for i in range(len(f)):
            for j in range(len(f)):
                if j==i:continue
                l=f[:min(i,j)]+f[min(i,j)+1:max(i,j)]+f[max(i,j)+1:]
                pos=j if j<i else j-1
                by_low[l]+=(-1)**(i+pos)
        assert all(x==0 for x in by_low.values())
print('BOUNDARY_SQUARE_ZERO')

# Murnaghan--Nakayama, independent of the chain reduction.
def partitions(z,upper=None):
    if z==0:
        yield ()
        return
    if upper is None:upper=z
    for j in range(min(z,upper),0,-1):
        for rest in partitions(z-j,j):
            yield (j,)+rest

P=list(partitions(6))
def subpart(lam,size):
    for mu in partitions(size):
        if all(i<len(lam) and mu[i]<=lam[i] for i in range(len(mu))):yield mu

def rim_height(lam,mu):
    cells={(r,c) for r,L in enumerate(lam) for c in range(L) if c>=(mu[r] if r<len(mu) else 0)}
    if any({(r,c),(r+1,c),(r,c+1),(r+1,c+1)}<=cells for r,c in cells):return None
    seen={next(iter(cells))};stack=list(seen)
    while stack:
        r,c=stack.pop()
        for q in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if q in cells and q not in seen:seen.add(q);stack.append(q)
    return len({r for r,c in cells})-1 if len(seen)==len(cells) else None

@functools.lru_cache(None)
def specht(lam,cyc):
    if not cyc:return int(not lam)
    val=0
    for mu in subpart(lam,sum(lam)-cyc[0]):
        h=rim_height(lam,mu)
        if h is not None:val+=(-1)**h*specht(mu,cyc[1:])
    return val

def centralizer(cyc):
    return math.prod(k**a*math.factorial(a) for k,a in collections.Counter(cyc).items())

assert all(sum(Fraction(specht(a,t)*specht(b,t),centralizer(t)) for t in P)==(1 if a==b else 0) for a in P for b in P)
D={(t,sw):(int(h3),int(h4)) for t,sw,h3,h4,*_ in records}
assert D[((1,)*6,0)]==(24,32)
assert D[((1,)*6,1)]==(-4,-20)
for deg in (0,1):
    result=[]
    for lam in P:
        for e in (1,-1):
            val=sum(Fraction(specht(lam,t)*(D[t,0][deg]+e*D[t,1][deg]),2*centralizer(t)) for t in P)
            assert val.denominator==1 and val>=0
            if val:result.append((lam,e,int(val)))
    want=({0:[((4,2),-1,1),((3,1,1,1),1,1),((2,2,2),-1,1)],
           1:[((6,),1,1),((4,1,1),-1,1),((3,2,1),-1,1),((2,1,1,1,1),1,1)]})[deg]
    assert sorted(result)==sorted(want),(deg,result)
    print('SPECHT_DEGREE',3+deg, sorted(result))
print('VERIFY_OK')
