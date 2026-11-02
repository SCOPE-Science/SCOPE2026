#!/usr/bin/env python3
"""Standalone finite checks for consecutive Motzkin residues modulo five."""
from collections import Counter
from math import comb
W = (1, 1, 3, 2, 4)
EXPECTED = (
    (0, 2, 2, 2, 2),
    (2, 6, 6, 2, 2),
    (2, 2, 6, 2, 6),
    (2, 6, 2, 6, 2),
    (2, 2, 2, 6, 6),
)
EXPECTED_FG = (
    ((1,1),(1,1),(1,1),(1,1)),
    ((1,2),(1,2),(1,2),(1,2)),
    ((2,4),(2,1),(2,3),(2,0)),
    ((4,4),(1,2),(3,0),(0,3)),
    ((4,1),(2,2),(0,3),(3,4)),
)

def trinomial(n):
    return sum(comb(n, 2*j)*comb(2*j,j) for j in range(n//2+1))

def motzkin(n):
    return sum(comb(n,2*j)*(comb(2*j,j)//(j+1)) for j in range(n//2+1))

def u(q):
    a=1
    while q:
        a=a*W[q%5]%5
        q//=5
    return a

def ratio(q):
    return u(q+1)*pow(u(q),-1,5)%5

def fg(d,r):
    a=[W[(d+i)%5]*(r if d+i>=5 else 1)%5 for i in range(4)]
    return ((3*(3*a[0]+2*a[1]-a[2]))%5,
            (3*(3*a[1]+2*a[2]-a[3]))%5)

assert tuple(trinomial(i)%5 for i in range(5))==W
assert all(fg(d,r)==EXPECTED_FG[d][r-1] for d in range(5) for r in range(1,5))
C=Counter(((z*f)%5,(z*g)%5)
          for d in range(5) for r in range(1,5)
          for z in range(1,5) for f,g in [fg(d,r)])
assert sum(C.values())==80
assert tuple(tuple(C[(j,k)] for k in range(5)) for j in range(5))==EXPECTED
assert C[(0,0)]==0

for n in range(256):
    T=(trinomial(n),trinomial(n+1),trinomial(n+2))
    assert 2*motzkin(n)==3*T[0]+2*T[1]-T[2]
    assert u(n)==T[0]%5
    q,d=divmod(n,5)
    a,b=fg(d,ratio(q))
    assert (motzkin(n)%5,motzkin(n+1)%5)==((u(q)*a)%5,(u(q)*b)%5)

# Exhaustive recurrence-level and residue-pair checks at base-five cutoffs.
for k in range(1,8):
    N=5**k
    obs=Counter()
    for n in range(N):
        q,d=divmod(n,5)
        a,b=fg(d,ratio(q))
        obs[(u(q)*a%5,u(q)*b%5)]+=1
    assert obs[(0,0)]==0
    assert sum(obs.values())==N
    assert max(abs(80*obs[(j,l)]-N*EXPECTED[j][l])
               for j in range(5) for l in range(5)) < 80*(k+2)**2

# Check the central four-valued group-product induction on a finite range.
for r in range(9):
    counts=Counter(u(q) for q in range(5**r))
    assert counts[1]==(5**r+3)//4
    assert all(counts[z]==(5**r-1)//4 for z in (2,3,4))
print('VERIFY_OK')
