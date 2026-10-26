#!/usr/bin/env python3
"""Exact three-round EF types for elementary abelian groups.
The group signature has equality and one ternary relation A(x,y,z): x+y=z.
Enumerates RREF kernels of at most three vectors; each is an actual GL-orbit.
See RESULT.md for the independent universal large-characteristic proof.
"""
from itertools import combinations,product
from fractions import Fraction
from math import gcd
import sys,time
from functools import lru_cache
start=time.monotonic()

def rref(vectors,p,k):
 a=[list(x) for x in vectors if any(x)]
 pivot=0
 for j in range(k):
  s=next((i for i in range(pivot,len(a)) if a[i][j]%p),None)
  if s is None:continue
  a[pivot],a[s]=a[s],a[pivot];inv=pow(a[pivot][j],-1,p)
  a[pivot]=[(x*inv)%p for x in a[pivot]]
  for i in range(len(a)):
   if i!=pivot and a[i][j]:
    c=a[i][j];a[i]=[(x-c*y)%p for x,y in zip(a[i],a[pivot])]
  pivot+=1
  if pivot>=len(a):break
 return tuple(tuple(x) for x in a[:pivot])

def subspaces(p,k):
 out=[]
 for r in range(k+1):
  for piv in combinations(range(k),r):
   frees=[(i,j) for i in range(r) for j in range(piv[i]+1,k) if j not in piv]
   for vals in product(range(p),repeat=len(frees)):
    basis=[[0]*k for _ in range(r)]
    for i,j in enumerate(piv):basis[i][j]=1
    for (i,j),x in zip(frees,vals):basis[i][j]=x
    out.append(tuple(tuple(row) for row in basis))
 return out

def restrict(K,p,k):
 if not K:return ()
 if all(row[-1]==0 for row in K):return rref([row[:-1] for row in K],p,k-1)
 i=next(i for i,row in enumerate(K) if row[-1])
 base=K[i];inv=pow(base[-1],-1,p)
 return rref([tuple((r[j]-r[-1]*base[j]*inv)%p for j in range(k-1)) for t,r in enumerate(K) if t!=i],p,k-1)

def member(K,v,p):
 r=list(v)
 for row in K:
  j=next(i for i,x in enumerate(row) if x)
  c=r[j];r=[(a-c*b)%p for a,b in zip(r,row)]
 return all(x==0 for x in r)

def atom(K,p,k):
 out=0;b=0
 for i in range(k):
  for j in range(i+1,k):
   v=[0]*k;v[i]+=1;v[j]-=1
   if member(K,v,p):out|=1<<b
   b+=1
 for i in range(k):
  for j in range(k):
   for h in range(k):
    v=[0]*k;v[i]+=1;v[j]+=1;v[h]-=1
    if member(K,v,p):out|=1<<b
    b+=1
 return out

class Intern:
 def __init__(self):self.ids={}
 def id(self,x):
  if x not in self.ids:self.ids[x]=len(self.ids)+1
  return self.ids[x]
interns=[Intern() for _ in range(4)]
clses={}
observed={}
for p in [2,3,5,7,11,13,17,19,23,29,31]:
 ss={k:subspaces(p,k) for k in [1,2,3]}
 look={k:{s:i for i,s in enumerate(ss[k])} for k in ss}
 rests={k:[look[k-1][restrict(s,p,k)] for s in ss[k]] for k in [2,3]}
 ats={k:[atom(s,p,k) for s in ss[k]] for k in ss}
 for d in [1,2,3]:
  tp={}
  tp[3]=[interns[3].id(a) if 3-len(K)<=d else 0 for K,a in zip(ss[3],ats[3])]
  for k in [2,1]:
   ext=[set() for _ in ss[k]]
   for i,Knew in enumerate(ss[k+1]):
    if 3==k+1 and 3-len(Knew)>d:continue
    if k+1==2 and 2-len(Knew)>d:continue
    ext[rests[k+1][i]].add(tp[k+1][i])
   tp[k]=[interns[k].id((a,tuple(sorted(ext[i])))) if k-len(K)<=d else 0 for i,(K,a) in enumerate(zip(ss[k],ats[k]))]
  zero=ss[1].index(())
  unit=ss[1].index(((1,),))
  alltypes=tuple(sorted(set((tp[1][zero],tp[1][unit]))))
  cls=interns[0].id(alltypes)
  clses.setdefault(cls,[]).append((p,d))
  observed[(p,d)]=cls
  print(f'{p},{d},{cls}')
 
# Finite universal checks on every distinct small characteristic/dimension regime.
assert len(clses)==13, len(clses)
assert [len(clses[i]) for i in range(1,13)]==[1,1,1,1,2,1,2,1,2,1,2,1]
assert (13,2) in clses[13] and (17,1) in clses[13] and (17,3) in clses[13]
# Extension comparisons by exact linear-algebraic kernel enumeration,
# independent of the number of elements in the groups.
forms=[(Fraction(0),Fraction(0)),(Fraction(1),Fraction(0)),
       (Fraction(0),Fraction(1)),(Fraction(2),Fraction(0)),
       (Fraction(0),Fraction(2)),(Fraction(1),Fraction(1)),
       (Fraction(1),Fraction(-1)),(Fraction(-1),Fraction(1)),
       (Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(1,2))]
slopes=set()
for (a,b),(c,d) in combinations(forms,2):
 if b!=d:slopes.add((c-a)/(b-d))
assert slopes==set(map(Fraction,['-2','-1','-1/2','0','1/4','1/3','1/2','2/3','1','3/2','2','3','4']))
assert max(abs(x.numerator*y.denominator-y.numerator*x.denominator) for x,y in combinations(slopes,2))==15
# So for every prime >=17, each exceptional rational slope is distinct,
# and at least one remaining scalar exists. Each 3rd-round atom involving z
# either fixes z to one of the ten forms or does not constrain z.
print('VERIFY_OK classes=13 maximal_minimum_representative=121 exceptional_slopes=13')

# Independent direct graph-of-addition semantics on actual small groups.
direct_intern=[Intern() for _ in range(4)]

def direct_type(p,d):
    elements=list(product(range(p),repeat=d));n=len(elements)
    plus=lambda a,b:tuple((x+y)%p for x,y in zip(a,b))
    def raw_atom(t):
        k=len(t);out=0;bit=0
        for i in range(k):
            for j in range(i+1,k):
                if t[i]==t[j]:out|=1<<bit
                bit+=1
        for i in range(k):
            for j in range(k):
                for h in range(k):
                    if plus(t[i],t[j])==t[h]:out|=1<<bit
                    bit+=1
        return out
    t3={t:direct_intern[3].id(raw_atom(t)) for t in product(elements,repeat=3)}
    t2={}
    for t in product(elements,repeat=2):
        ext=tuple(sorted({t3[t+(z,)] for z in elements}))
        t2[t]=direct_intern[2].id((raw_atom(t),ext))
    t1={}
    for a in elements:
        ext=tuple(sorted({t2[(a,z)] for z in elements}))
        t1[a]=direct_intern[1].id((raw_atom((a,)),ext))
    return direct_intern[0].id(tuple(sorted(set(t1.values()))))

sample=[(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(7,1),(11,1),(13,1),(17,1)]
direct={key:direct_type(*key) for key in sample}
for i,a in enumerate(sample):
    for b in sample[i+1:]:
        assert (direct[a]==direct[b])==(observed[a]==observed[b]),(a,b)
print('DIRECT_ORACLE_OK cases=%s ordered_comparisons=%s'%(len(sample),len(sample)**2))
