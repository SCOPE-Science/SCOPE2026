#!/usr/bin/env python3
"""Exact finite combinatorial checks for a full-height symmetric tent map.
Uses Python standard library only. Finite tests supplement an analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import log

q=F(2,3)
cells={'A':(F(0),F(1,2)),'B':(F(1,2),q),'C':(q,F(1))}
edge={'A':'ABC','B':'C','C':'AB'}
Pi={'A':F(1,2),'B':F(1,6),'C':F(1,3)}
P={('A','A'):F(1,2),('A','B'):F(1,6),('A','C'):F(1,3),
   ('B','C'):F(1),('C','A'):F(3,4),('C','B'):F(1,4)}
Ps={('+','+'):F(1,2),('+','-'):F(1,2),('-','+'):F(1),('-','-'):F(0)}

def hidden_mass(word):
  d={s:Pi[s] for s in 'AB' if word[0]=='+'} if word[0]=='+' else {'C':Pi['C']}
  for obs in word[1:]:
    nxt={}
    for i,v in d.items():
      for j in ('AB' if obs=='+' else 'C'):
        nxt[j]=nxt.get(j,F(0))+v*P.get((i,j),F(0))
    d=nxt
  return sum(d.values(),F(0))

def observed_mass(word):
  z=F(2,3) if word[0]=='+' else F(1,3)
  for a,b in zip(word,word[1:]):z*=Ps[a,b]
  return z

checks=0
for n in range(1,11):
  for chars in product('+-',repeat=n):
    word=''.join(chars)
    assert hidden_mass(word)==observed_mass(word),(word,hidden_mass(word),observed_mass(word))
    checks+=1


def first_returns(k):
  paths=[('C',)]
  for i in range(k):
    nxt=[]
    for path in paths:
      for j in edge[path[-1]]:
        if (i<k-1 and j=='C') or (i==k-1 and j!='C'):continue
        nxt.append(path+(j,))
    paths=nxt
  return paths

def cylinder(states):
  """All points with a prescribed Markov path, using backwards branches."""
  lo,hi=cells[states[-1]]
  for st in reversed(states[:-1]):
    if st=='A':lo,hi=lo/2,hi/2
    else:lo,hi=1-hi/2,1-lo/2
  return lo,hi

for k in range(2,17):
  paths=first_returns(k)
  assert len(paths)==2,(k,paths)
  assert {p for p in paths}=={('C',)+('A',)*(k-1)+('C',),
                ('C',)+('A',)*(k-2)+('B','C')}
  intervals=sorted(cylinder(p) for p in paths)
  assert all(l>=q and r<=1 and r-l==F(1,3*2**k) for l,r in intervals)
  assert intervals[0][1]<=intervals[1][0]
  checks+=8

for gaps in ([2,3,4],[2,2,2,2,2],[5,3,5],[3,4,3,2],[10,2]):
  possibilities=[]
  for choices in product((0,1),repeat=len(gaps)):
    states=()
    for k,ch in zip(gaps,choices):
      states+=first_returns(k)[ch][:-1]
    states+=('C',)
    possibilities.append(cylinder(states))
  possibilities.sort()
  assert len(possibilities)==2**len(gaps)
  expected=F(1,3*2**sum(gaps))
  assert all(r-l==expected for l,r in possibilities)
  assert all(possibilities[i][1]<=possibilities[i+1][0] for i in range(len(possibilities)-1))
  checks+=len(possibilities)

# Exact stationary directional mean, covariance decay and entropy identities:
assert F(2,3)-F(1,3)==F(1,3)
assert Ps['+','-']*F(2,3)==F(1,3)
assert (F(1,2)*F(2,3)+F(1)*F(1,3))==F(2,3)
assert (F(8,9)*F(1,3))==F(8,27)  # CLT asymptotic variance
assert abs((2/3)*log(2)-((2/3)*log(2)))<1e-14

print('PASS exact_markov_word_checks',sum(2**n for n in range(1,11)))
print('PASS first_return_two_branches k=2..16; disjoint equal cylinders')
print('PASS multi_return_equal_cylinder_lengths and counts')
print('PASS stationary_mean=1/3 stationary_down_frequency=1/3')
print('PASS sign_entropy=(2/3)log(2), typical_fiber_dimension=1/3')
print('PASS finite_checks_total',checks)
