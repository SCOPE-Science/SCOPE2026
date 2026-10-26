#!/usr/bin/env python3
"""Finite corroboration of exact two-noun syllogistic spectrum witnesses.
Not a proof for all sizes: the symbolic compression lemma proves the universal upper bound.
"""
from itertools import product

def models(n):
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                d = n-a-b-c
                yield (a,b,c,d)

def sat_witness(m, kind):
    a,b,c,d=m
    allfour=all(t>0 for t in m)
    eqp=a+b==c+d
    pxq=b>c
    pxnq=a>d
    nq_xq=b+d>a+c
    some3=a>0 and b>0 and c>0
    some2=a>0 and b>0
    return {
      'EMPTY':False,'T1':True,'T2':some2,'T3':some3,
      'T4':allfour,'T5':allfour and pxq,
      'T6':allfour and pxq and pxnq,
      'T7':allfour and pxnq and nq_xq,
      'E2':eqp,'E4':eqp and allfour,
      'E6':eqp and allfour and pxq
    }[kind]

names=['EMPTY']+[f'T{i}' for i in range(1,8)]+['E2','E4','E6']
for n in range(1,15):
    truths={x:False for x in names}
    for m in models(n):
      checks={x: sat_witness(m,x) for x in names}
      for name,val in checks.items(): truths[name]|=val
    for name in names:
      expected=(name!='EMPTY' and ((name.startswith('T') and n>=int(name[1:])) or (name.startswith('E') and n>=int(name[1:]) and n%2==0)))
      assert truths[name]==expected,(n,name,truths[name],expected)
print('All eleven spectrum witnesses agree with their specified membership at sizes 1..14.')

sg=lambda z:(z>0)-(z<0)
def profile(a,b,c,d):
    u=b-c;v=a-d
    return (tuple(int(t>0) for t in (a,b,c,d)), tuple(sg(z) for z in (u,v,u+v,v-u)))
def normalized(m):
    a,b,c,d=m;u=b-c;v=a-d
    if u and v:
      ru=1+(abs(u)>abs(v)); rv=1+(abs(v)>abs(u))
      un=sg(u)*ru;vn=sg(v)*rv
    else:un=sg(u);vn=sg(v)
    def pair(x,y,k):
      if x and y: return (1+max(k,0),1+max(-k,0))
      if x: assert k>0;return (k,0)
      if y: assert k<0;return (0,-k)
      assert k==0;return (0,0)
    aa,dd=pair(a,d,vn)
    bb,cc=pair(b,c,un)
    return (aa,bb,cc,dd)
num=0; pset=set(); highest=(0,None)
for n in range(1,36):
  for m in models(n):
    out=normalized(m)
    assert 1<=sum(out)<=7,(m,out)
    assert profile(*m)==profile(*out),(m,out)
    pset.add(profile(*out)); num+=1
    if sum(out)>highest[0]:highest=(sum(out),out)
print('Normal-form compression checked for',num,'models (all total sizes 1..35).')
print('Number of four-cell Boolean/cardinality profiles:',len(pset))
print('Largest compressed model size:',highest)
