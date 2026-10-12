#!/usr/bin/env python3
"""Finite sanity checks of the collision witnesses, not a substitute for the proof."""
from itertools import product
from collections import Counter
pairs=[(0,0),(0,1),(1,0),(1,1)]
# Every collision has an aperiodic witness and an axis reflecting its color output.
cases={
 (0,1):('single_one',0), # 00 == 01
 (0,2):('single_one',-2), # 00 == 10
 (0,3):('step',0),       # 00 == 11
 (1,2):('single_one',-1),# 01 == 10, axis at -1/2
 (1,3):('single_zero',-2),
 (2,3):('single_zero',0),
}
def digit(kind,j):
 if kind=='single_one': return int(j==0)
 if kind=='single_zero':return int(j!=0)
 if kind=='step':return int(j>0)
 raise ValueError(kind)
def output(rule,kind,j):
 return rule[2*digit(kind,j)+digit(kind,j+1)]
for i,j in cases:
 kind,t=cases[i,j]
 for rule in product(range(4), repeat=4):
  if rule[i]!=rule[j]: continue
  for k in range(-30,31):
   assert output(rule,kind,k)==output(rule,kind,t-k), (i,j,rule,kind,t,k)
print('ALL_COLLISION_CASES_PASS: 6 cases, 256 rules, -30..30')
for k in (1,2,3,4):
 rules=list(product(range(k),repeat=4))
 count=Counter('injective' if len(set(rule))==4 else 'noninjective' for rule in rules)
 print(k,dict(count))
 assert (count['injective'] if 'injective' in count else 0)==(24 if k==4 else 0)
print('VERIFY_OK')
