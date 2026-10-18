#!/usr/bin/env python3
"""Exact finite checks for edge dependence in a cactus random-cluster law."""
from fractions import Fraction
from itertools import product
from math import cos, sin, pi

def rc_distribution(n_vertices,edges,weights,q):
    states=list(product((0,1),repeat=len(edges)))
    unnormalized=[]
    for s in states:
        par=list(range(n_vertices))
        def find(x):
            while par[x]!=x: x=par[x]
            return x
        for b,(u,v) in zip(s,edges):
            if b: par[find(u)]=find(v)
        k=len({find(x) for x in range(n_vertices)})
        w=q**k
        for b,v in zip(s,weights):
            if b:w*=v
        unnormalized.append(w)
    z=sum(unnormalized,Fraction(0))
    return {s:w/z for s,w in zip(states,unnormalized)}

def cycle_factor(s,indices,weights,q):
    r=[weights[e]/(weights[e]+q) for e in indices]
    a=Fraction(1)
    for v in r: a*=v
    z=1-(1-q)*a
    w=Fraction(1)
    for e,re in zip(indices,r):
        w*=re if s[e] else 1-re
    return w*(q if all(s[e] for e in indices) else 1)/z

def ex(d,f):return sum((mass*f(s) for s,mass in d.items()),Fraction(0))

# Two three-edge cycles sharing exactly one vertex, plus a bridge.
edges=[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(4,5)]
weights=list(map(Fraction,[1,2,3,4,5,6,7]))
assertions=0
for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
  d=rc_distribution(6,edges,weights,q)
  for s,pr in d.items():
    val=cycle_factor(s,[0,1,2],weights,q)*cycle_factor(s,[3,4,5],weights,q)
    rr=weights[6]/(weights[6]+q)
    val*=rr if s[6] else 1-rr
    assert val==pr
    assertions+=1
  # Disjoint-support Boolean AND/OR observables. Exhaust every pair of edge masks.
  for marks in product((0,1,2),repeat=7):
    A=[i for i,z in enumerate(marks) if z==1]
    B=[i for i,z in enumerate(marks) if z==2]
    if not A or not B:continue
    for mode1,mode2 in product(('all','any'),repeat=2):
      def obs(s,inds,mode):
        return int(all(s[i] for i in inds)) if mode=='all' else int(any(s[i] for i in inds))
      ea=ex(d,lambda s:obs(s,A,mode1))
      eb=ex(d,lambda s:obs(s,B,mode2))
      eab=ex(d,lambda s:obs(s,A,mode1)*obs(s,B,mode2))
      assert eab<=ea*eb, (q,marks,mode1,mode2)
      assertions+=1
  # Exact rank-one covariance on first cyclic block for every disjoint subset pair.
  r=[weights[i]/(weights[i]+q) for i in (0,1,2)]
  a=r[0]*r[1]*r[2]
  z=1-(1-q)*a
  for i,j in ((0,1),(0,2),(1,2)):
    xi=ex(d,lambda s:s[i]);xj=ex(d,lambda s:s[j])
    cov=ex(d,lambda s:s[i]*s[j])-xi*xj
    expected=-(1-q)*a*(1-r[i])*(1-r[j])/z**2
    assert cov==expected
    assertions+=1

# One-cycle rank-one identity for arbitrary distinct increasing Boolean functions.
def monotone_functions(k):
  states=list(product((0,1),repeat=k))
  for vals in product((0,1),repeat=len(states)):
    if all(not(all(a[i]<=b[i] for i in range(k)) and vals[ia]>vals[ib])
           for ia,a in enumerate(states) for ib,b in enumerate(states)):
      yield dict(zip(states,vals))

for q in (Fraction(1,3),Fraction(2,3)):
  for a_bits in range(1,1<<4):
    Ai=[i for i in range(4) if a_bits>>i&1]
    for b_bits in range(1,1<<4):
      if a_bits&b_bits:continue
      Bi=[i for i in range(4) if b_bits>>i&1]
      for fa in monotone_functions(len(Ai)):
        for fb in monotone_functions(len(Bi)):
          r=[Fraction(i+1,i+3) for i in range(4)]
          t=Fraction(1)
          for x in r:t*=x
          Z=1-(1-q)*t
          base={s:Fraction(1) for s in product((0,1),repeat=4)}
          for s in base:
            for b,x in zip(s,r):base[s]*=x if b else (1-x)
          u=sum(w*fa[tuple(s[i] for i in Ai)] for s,w in base.items())
          v=sum(w*fb[tuple(s[i] for i in Bi)] for s,w in base.items())
          c=sum(w*(q if all(s) else 1)*fa[tuple(s[i] for i in Ai)]*fb[tuple(s[i] for i in Bi)]/Z for s,w in base.items())
          ea=(u-(1-q)*t*fa[tuple([1]*len(Ai))])/Z
          eb=(v-(1-q)*t*fb[tuple([1]*len(Bi))])/Z
          asserted=-(1-q)*t*(fa[tuple([1]*len(Ai))]-u)*(fb[tuple([1]*len(Bi))]-v)/Z**2
          assert c-ea*eb==asserted and asserted<=0
          assertions+=1
print('PASS: %d exact rational assertions for two-cycle cactus and rank-one covariance' % assertions)
