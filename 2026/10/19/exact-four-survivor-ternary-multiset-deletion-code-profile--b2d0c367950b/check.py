"""Stand-alone reproducibility checks for the four-survivor ternary multiset theorem.

Python >=3.9; standard library only. Checks the finite certificates and
uses a separate direct compatibility-graph search for small lengths.
"""
from itertools import combinations

TRIPLES = [
 ((1,3,1),(2,2,1),(2,3,0)),
 ((2,2,1),(2,3,0),(3,2,0)),
 ((0,2,3),(1,1,3),(1,2,2)),
 ((0,3,2),(1,2,2),(1,3,1)),
 ((0,2,3),(0,3,2),(1,2,2)),
 ((2,0,3),(2,1,2),(3,0,2)),
 ((2,1,2),(3,0,2),(3,1,1)),
 ((1,1,3),(2,0,3),(2,1,2)),
 ((2,2,1),(3,1,1),(3,2,0)),
]
WITNESSES = {
 5: [(0,0,5),(0,2,3),(0,5,0),(1,3,1),(3,0,2),(3,2,0),(5,0,0)],
 6: [(0,0,6),(0,3,3),(0,6,0),(3,0,3),(3,3,0),(6,0,0)],
 7: [(0,0,7),(0,7,0),(1,3,3),(7,0,0)],
 8: [(0,0,8),(0,8,0),(2,3,3),(8,0,0)],
 9: [(0,0,9),(0,9,0),(3,3,3),(9,0,0)],
 10: [(0,0,10),(0,10,0),(10,0,0)],
}
EXPECTED = {5:7,6:6,7:4,8:4,9:4,10:3}

def vectors(n):
 return [(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)]

def meet(x,y):
 return sum(min(a,b) for a,b in zip(x,y))

def valid(code,n):
 return len(set(code)) == len(code) and all(len(v)==3 and min(v)>=0 and sum(v)==n for v in code) and all(meet(x,y)<=3 for x,y in combinations(code,2))

def clique_exists(n,target):
 """Independent finite check: find target mutually compatible codewords."""
 V=vectors(n); N=len(V)
 # Neighbours to the right only: code pairs require meet<=3.
 nbr=[0]*N
 for i in range(N):
  for j in range(i+1,N):
   if meet(V[i],V[j])<=3:nbr[i] |= 1 << j
 nodes=(1<<N)-1
 def search(remaining,need):
  if need == 0:return True
  if remaining.bit_count()<need:return False
  while remaining and remaining.bit_count()>=need:
   low=remaining & -remaining; i=low.bit_length()-1
   remaining ^= low
   if search(remaining & nbr[i],need-1):return True
  return False
 return search(nodes,target)

B5=[v for v in vectors(5) if max(v)<=3]
assert len(B5)==12 and len(TRIPLES)==9
assert all(all(meet(x,y)>=4 for x,y in combinations(c,2)) for c in TRIPLES)
assert min(sum(v in c for c in TRIPLES) for v in B5)>=2
print('n=5: 12 light vectors, 9 incompatible triples, >=2 incidences each: PASS')
B6=[v for v in vectors(6) if max(v)<=3]
FOUR_RECEIVED=[(2,2,0),(2,0,2),(0,2,2)]
assert len(B6)==10
assert all(any(all(v_i>=r_i for v_i,r_i in zip(v,r)) for r in FOUR_RECEIVED) for v in B6)
print('n=6: 10 light vectors all contain one of three receiver certificates: PASS')
for n in range(7,10):
 L=[v for v in vectors(n) if max(v)<=3]
 assert all(meet(x,y)>=4 for x,y in combinations(L,2))
 print('n=%s: pairwise incompatible light vectors (%s): PASS'%(n,len(L)))
for n in EXPECTED:
 assert len(WITNESSES[n])==EXPECTED[n] and valid(WITNESSES[n],n)
 # Search independently for any code larger than the claimed optimal code.
 assert not clique_exists(n,EXPECTED[n]+1),n
 print('n=%2d: independently excluded size %d, witness size %d: PASS'%(n,EXPECTED[n]+1,EXPECTED[n]))
for n in (11,12,17,32):
 witness=[(n,0,0),(0,n,0),(0,0,n)]
 assert valid(witness,n)
 assert all(max(v)>=4 for v in vectors(n))
 print('n=%2d: pure-vector witness and all-heavy certificate check: PASS'%n)
print('VERIFICATION_OK')
