#!/usr/bin/env python3
"""Exact finite illustration of simultaneous deletions from square summands."""
from math import isqrt
U=(5,37,89)
B=2*max(U)**2
S={n*n for n in range(isqrt(B)+1)}
T={n*n for n in range(isqrt(B)+1) if n not in U}
all_sums={a+b for a in S for b in S if a+b<=B}
new_sums={a+b for a in T for b in S if a+b<=B}
assert all_sums == new_sums, sorted(all_sums-new_sums)
assert len(U)==3 and len(set(U))==3
for i,a in enumerate(U):
 for b in U[i:]:
  n=a*a+b*b
  pairs={(x,isqrt(n-x*x)) for x in range(isqrt(n)+1) if n-x*x>=0 and isqrt(n-x*x)**2==n-x*x and x<=isqrt(n-x*x)}
  assert len(pairs)>=2,(a,b,pairs)
print('CERTIFICATE_OK', 'primes=',U, 'cutoff=',B, 'sumset_size=',len(all_sums), 'deleted_squares=',len(U))
