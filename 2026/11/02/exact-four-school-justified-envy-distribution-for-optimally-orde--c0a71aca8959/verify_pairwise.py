#!/usr/bin/env python3
"""Reproduce four-school priority-aggregation counts using independent pairwise margins."""
import itertools,collections
import numpy as np
from fractions import Fraction
perms=np.asarray(list(itertools.permutations(range(4))),dtype=np.int8)
pairs=list(itertools.combinations(range(4),2))
pos=np.argsort(perms,axis=1)
# For each ranking, d[pair] = 1 if larger-labeled agent is ranked ABOVE smaller one.
bit=np.column_stack([(pos[:,b]<pos[:,a]).astype(np.int16) for a,b in pairs]);assert bit.shape==(24,6)
counts=collections.Counter(); ties=collections.Counter(); allhist=collections.Counter()
# For lex order of four school permutations, grouped over first two and broadcast second two.
for i in range(24):
 for j in range(24):
  prefix=(bit[i]+bit[j]).reshape(1,1,6)
  # shape 24,24,6: # of school rankings placing b above a
  m=prefix+bit[:,None,:]+bit[None,:,:]
  # If chosen serial ranking puts b above a, # disagreements=4-m, else m.
  # candidate rows 24 x 6
  cost=np.sum(np.where(bit[:,None,None,:].astype(bool), 4-m[None,:,:,:],m[None,:,:,:]),axis=3)
  minimum=np.min(cost,axis=0)
  nopt=np.sum(cost==minimum[None,:,:],axis=0)
  for val,num in zip(*np.unique(minimum,return_counts=True)):counts[int(val)]+=int(num)
  for val,num in zip(*np.unique(nopt,return_counts=True)):ties[int(val)]+=int(num)
  for a,b in zip(minimum.ravel(),nopt.ravel()):allhist[(int(a),int(b))]+=1
assert sorted(counts.items()) == [(0,24),(1,288),(2,1560),(3,5472),(4,14232),(5,28800),(6,46896),(7,62208),(8,66744),(9,56160),(10,34056),(11,12960),(12,2376)]
assert sum(counts.values())==24**4
assert sorted(ties.items())==[(1,51192),(2,74232),(3,74592),(4,37224),(5,25200),(6,26136),(8,26784),(12,14040),(24,2376)]
assert sum(ties.values())==24**4
assert counts[12]==ties[24]==2376
print('hist',sorted(counts.items()))
print('ties',sorted(ties.items()))
print('total_score',sum(k*v for k,v in counts.items()))
print('mean fair envy',Fraction(sum(k*v for k,v in counts.items()),4*24**4))
print('gain_vs_random',Fraction(3*4*24**4-sum(k*v for k,v in counts.items()),4*24**4))
print('unique',Fraction(ties[1],24**4),'neutral',Fraction(counts[12],24**4))
# Direct independent mechanism expectation check for one asymmetric priority profile.
pri=[(0,1,2,3),(0,1,3,2),(0,2,1,3),(3,2,1,0)]
order=(1,2,0,3)
N=0
for commonpref in itertools.permutations(range(4)):
 assigned={order[t]:commonpref[t] for t in range(4)}
 for t in range(4):
  for u in range(t+1,4):
   agent_earlier, agent_later=order[t],order[u]
   if pri[commonpref[t]].index(agent_later) < pri[commonpref[t]].index(agent_earlier):N+=1
# each common ranking equally likely, score must equal school-wise pair inversions
score=0
for s in range(4):
 ps=pri[s]
 for t in range(4):
  for u in range(t+1,4):score+=(ps.index(order[u])<ps.index(order[t]))
assert N==6*score
print('mechanism direct example score',score,'total envy across 24 common prefs',N)
print('PASS: independently formulated pairwise-margin enumeration')
