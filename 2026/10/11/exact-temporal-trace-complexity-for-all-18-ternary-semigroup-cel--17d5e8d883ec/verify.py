#!/usr/bin/env python3
"""Exact finite-window checks for semigroup CA single-site temporal histories.

Run with Python 3 standard library only: python verify.py
All infinite-time statements require the separate mathematical proof.
"""
from itertools import product
from math import comb

TABLES = {
 1:((0,1,2),(1,2,0),(2,0,1)),
 2:((1,2,1),(2,1,2),(1,2,1)),
 3:((1,2,2),(2,2,2),(2,2,2)),
 4:((2,1,0),(1,1,1),(0,1,2)),
 5:((2,0,0),(0,1,2),(0,2,2)),
 6:((2,0,0),(0,2,2),(0,2,2)),
 7:((2,2,2),(2,2,2),(2,2,2)),
 8:((2,2,2),(2,1,2),(2,2,2)),
 9:((2,1,2),(1,1,1),(2,1,2)),
 10:((2,0,2),(0,1,2),(2,2,2)),
 11:((2,2,2),(1,1,1),(2,2,2)),
 12:((2,2,2),(0,1,2),(2,2,2)),
 13:((0,1,2),(1,1,2),(2,2,2)),
 14:((0,2,2),(2,1,2),(2,2,2)),
 15:((0,0,0),(1,1,1),(0,0,2)),
 16:((0,0,2),(1,1,2),(2,2,2)),
 17:((0,0,0),(1,1,1),(2,2,2)),
 18:((0,0,0),(1,1,1),(0,1,2)),
}

def closed_formula(i,n):
 assert 1<=i<=18 and n>=1
 if i==1: return 3**n
 if i in (2,6): return 3*2**(n-1)
 if i==3: return 3 if n==1 else 4
 if i in (4,5): return 2**(n+1)-1
 if i in (7,11,17): return 3
 if i in (8,15): return n+2
 if i in (9,12,14,16,18): return 2*n+1
 if i==10: return 3*n
 if i==13: return comb(n+2,2)
 raise AssertionError(i)

def trace_word(initial,table):
 state=initial
 output=[]
 for _ in range(len(initial)):
  output.append(state[0])
  state=tuple(table[a][b] for a,b in zip(state,state[1:]))
 return tuple(output)

def check():
 assert sorted(TABLES)==list(range(1,19))
 structural_checks=0
 for i,table in TABLES.items():
  for a,b,c in product(range(3),repeat=3):
   assert table[table[a][b]][c]==table[a][table[b][c]],(i,a,b,c)
   structural_checks+=1
 # All configurations on the finite backward-light-cone interval are enumerated;
 # outside this interval the global configuration can be extended arbitrarily.
 trace_formula_checks=0
 for n in range(1,10):
  for i,table in TABLES.items():
   observed=set()
   for initial in product(range(3),repeat=n):
    observed.add(trace_word(initial,table))
   assert len(observed)==closed_formula(i,n),(i,n,len(observed),closed_formula(i,n))
   trace_formula_checks+=1
 # More demanding length-10 check on all 18 classes.
 n=10
 for i,table in TABLES.items():
  observed={trace_word(initial,table) for initial in product(range(3),repeat=n)}
  assert len(observed)==closed_formula(i,n),(i,n,len(observed),closed_formula(i,n))
  trace_formula_checks+=1
 print('PASS associativity',structural_checks,'triples')
 print('PASS exact finite trace cardinalities',trace_formula_checks,'rule-length cases')
 print('PASS boundary n=1, n=2 and length-10; finite evidence only')

if __name__=='__main__': check()
