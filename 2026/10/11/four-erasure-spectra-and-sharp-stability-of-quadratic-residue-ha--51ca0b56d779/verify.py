#!/usr/bin/env python3
"""Exact integer-ring checks for quadratic-residue harmonic-frame four-erasures.

No external libraries. A polynomial A(p)+i*sqrt(p)*B(p) is a pair of
integer-coefficient polynomials, with (i*sqrt(p))**2 = -p. This permits
formal verification of the three characteristic polynomials for every p.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, isqrt

# Canonical skew adjacency representatives: rows/columns ordered 0,1,2,3.
MATS = {
 'T': ((0,1,1,1),(-1,0,-1,1),(-1,1,0,1),(-1,-1,-1,0)),
 'O': ((0,1,-1,-1),(-1,0,1,-1),(1,-1,0,-1),(1,1,1,0)),
 'I': ((0,1,-1,1),(-1,0,1,1),(1,-1,0,1),(-1,-1,-1,0)),
 'S': ((0,1,-1,1),(-1,0,1,-1),(1,-1,0,1),(-1,1,-1,0)),
}

def poly_add(a,b):
 c = dict(a)
 for k,v in b.items(): c[k] = c.get(k,0)+v
 return {k:v for k,v in c.items() if v}

def poly_mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
 return {k:v for k,v in c.items() if v}

def poly_shift(a):return {k+1:-v for k,v in a.items()}

def add(a,b):return (poly_add(a[0],b[0]),poly_add(a[1],b[1]))

def neg(a):return ({k:-v for k,v in a[0].items()}, {k:-v for k,v in a[1].items()})

def mul(a,b):
 return (poly_add(poly_mul(a[0],b[0]),poly_shift(poly_mul(a[1],b[1]))),
         poly_add(poly_mul(a[0],b[1]),poly_mul(a[1],b[0])))

def sign_of(perm):return -1 if sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2 else 1

def determinant(M):
 n=len(M)
 total=({}, {})
 for perm in permutations(range(n)):
  term=({0:sign_of(perm)}, {})
  for i,j in enumerate(perm):term=mul(term,M[i][j])
  total=add(total,term)
 return total

def characteristic(M):
 # Characteristic polynomial det(y I - H) via principal minors.
 ans=[]
 for r in range(5):
  coef=({}, {})
  for J in combinations(range(4),r):
   sub=[[M[i][j] for j in J] for i in J]
   val=determinant(sub)
   coef=add(coef,neg(val) if r%2 else val)
  assert not coef[1], ('nonreal char coefficient',coef)
  ans.append(coef[0])
 return ans

def expected(pat):
 c={
  'T': [{0:1},{},{1:-6,0:-6},{1:8,0:8},{2:1,1:-2,0:-3}],
  'O': [{0:1},{},{1:-6,0:-6},{0:8},{2:9,1:6,0:-3}],
  'I': [{0:1},{},{1:-6,0:-6},{0:8},{2:9,1:6,0:-3}],
  'S': [{0:1},{},{1:-6,0:-6},{1:-8,0:8},{2:1,1:14,0:-3}],
 }
 return c[pat]

# Exact worst-type polynomial comparisons in descending powers of y.
def subtract(A,B):
 return [poly_add(a,{k:-v for k,v in b.items()}) for a,b in zip(A,B)]
assert subtract(expected('T'), expected('S')) == [{},{},{},{1:16},{1:-16}]
assert subtract(expected('O'), expected('S')) == [{},{},{},{1:8},{2:8,1:-8}]
print('FORMAL_DOMINANCE_IDENTITIES_OK')
for key,S in MATS.items():
 M=[[({0:-1},{0:S[i][j]}) if i!=j else ({},{}) for j in range(4)] for i in range(4)]
 got=characteristic(M)
 assert got==expected(key),(key,got,expected(key))
print('SYMBOLIC_CHARPOLYS_OK: T, O, I, S for arbitrary indeterminate p')

# Check all prime-indexed four-point subsets, with exact integer counts.
CASES=(7,11,19,23,31)
for p in CASES:
 assert all(p%d for d in range(2,isqrt(p)+1)) and p%4==3
 Q={v*v%p for v in range(1,p)}
 counts=Counter()
 for B in combinations(range(p),4):
  signs=tuple(tuple(0 if a==b else (1 if (B[b]-B[a])%p in Q else -1) for b in range(4)) for a in range(4))
  degrees=tuple(sorted(sum(signs[a][b]==1 for b in range(4)) for a in range(4)))
  type_key={
   (0,1,2,3):'T', (1,1,1,3):'O', (0,2,2,2):'I', (1,1,2,2):'S'
  }[degrees]
  canonical=MATS[type_key]
  # Verify that the sorted outdegree sequence really identifies
  # an isomorphism class, not merely a coarse numerical statistic.
  assert any(all(signs[a][b]==canonical[perm[a]][perm[b]] for a in range(4) for b in range(4))
             for perm in permutations(range(4))), (p,B,type_key)
  counts[degrees]+=1
 expected_counts={
  (0,1,2,3):p*(p-1)*(p-3)*(p-7)//64,
  (1,1,1,3):p*(p-1)*(p-3)*(p+1)//192,
  (0,2,2,2):p*(p-1)*(p-3)*(p+1)//192,
  (1,1,2,2):p*(p-1)*(p-3)*(p+1)//64,
 }
 assert counts == {key:value for key,value in expected_counts.items() if value},(p,counts,expected_counts)
 assert sum(counts.values())==comb(p,4)
 print('CENSUS_OK:',p,'four-subsets',comb(p,4),dict(sorted(counts.items())))
print('ALL_EXACT_CHECKS_PASSED')
