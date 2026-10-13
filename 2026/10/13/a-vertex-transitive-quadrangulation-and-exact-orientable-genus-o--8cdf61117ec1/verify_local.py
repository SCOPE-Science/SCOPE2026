#!/usr/bin/env python3
"""Small independent group-identity check for the H(8,3) quadrangular rotation."""
from itertools import permutations
poly = 0b1011
def mul(x,y):
    z=0
    while y:
        if y&1:z^=x
        x <<= 1
        if x & 8:x ^=poly
        y >>= 1
    return z
def times(g,h):return (mul(g[0],h[0]),mul(g[0],h[1])^g[1])
e=(1,0)
G=[(a,b) for a in range(1,8) for b in range(8)]
def inv(g):return next(h for h in G if times(g,h)==times(h,g)==e)
def apply(g,x):return mul(g[0],x)^g[1]
P={0,1,2}
S={g for g in G if P.isdisjoint({apply(g,x) for x in P})}
order=[(1,4),(1,5),(1,6),(5,6),(3,5),(1,7),(2,7),(4,7),(7,3),(6,3)]
assert set(order)==S and len(order)==10
rho=dict(zip(order,order[1:]+order[:1])); rev={b:a for a,b in rho.items()}
print('s0 -> s1,s2,s3; Q1 product is identity; Q2 closes:')
for s0 in order:
    # Four-dart identity of the source paper, checked without tracing graph faces.
    s1=rev[inv(s0)]
    s2=rho[inv(s1)]
    s3=rev[inv(s2)]
    assert times(times(times(s0,s1),s2),s3)==e
    assert rho[inv(s3)]==s0
    print(f'{s0} -> {s1},{s2},{s3}; OK')
print('LOCAL_IDENTITIES_OK: 10/10 Q1 and Q2')
