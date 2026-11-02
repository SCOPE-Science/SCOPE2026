"""Finite, exact-arithmetic verification for a sharp rational 2x2 semigroup example.

This is a reproducibility check of the explicit 31-element semigroup and a finite
combinatorial lemma used in its mathematical upper-bound proof. The all-semigroup
upper bound is symbolic and is not inferred from experiments.
"""
from itertools import product, combinations
from collections import deque
from fractions import Fraction
from math import gcd, lcm

def mul(a,b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])

def outer(u,v):
    return (u[0]*v[0], u[0]*v[1], u[1]*v[0], u[1]*v[1])

def neg(a): return tuple(-x for x in a)

def generated_group(gens):
    ident=(1,0,0,1)
    seen={ident}; pending=deque([ident])
    while pending:
        x=pending.popleft()
        for gen in gens:
            y=mul(x,gen)
            if y not in seen:
                seen.add(y);pending.append(y)
                assert len(seen)<1000
    return seen

U=[(1,0),(0,1),(1,1)]
V=[(1,0),(0,1),(1,-1)]
R=(0,-1,1,-1)
F=(0,1,1,0)
minus=(-1,0,0,-1)
units=generated_group([R,F,minus])
rankone={z for u in U for v in V for z in (outer(u,v),neg(outer(u,v)))}
zero=(0,0,0,0)
S=units|rankone|{zero}
assert (len(units),len(rankone),len(S))==(12,18,31)
assert all(mul(a,b) in S for a in S for b in S)
assert all(outer(u,v) in S for u in U[:2] for v in V[:2])
assert all(sum(a*b for a,b in zip(u,v)) in (-1,0,1) for u in U for v in V)

def primitive_direction(a,b):
    den=lcm(a.denominator,b.denominator)
    x,y=int(a*den),int(b*den)
    k=gcd(abs(x),abs(y))
    assert k>0
    x,y=x//k,y//k
    return (-x,-y) if x<0 or (x==0 and y<0) else (x,y)

# Every nonzero signed two-coordinate column vector has one of four directions.
# For each subset of directions U, every potential row functional v is fixed by
# its two pairings with any independent columns of U. Enumerate all 3^2 pairs
# of allowed pairings, solve over Q exactly, and retain v iff ALL pairings are
# 0 or +/-1. This enumerates all possible row directions, including fractions.
four=((1,0),(0,1),(1,1),(1,-1))
maximum=0
for k in (2,3,4):
    for us in combinations(four,k):
        p,q=us[:2]
        determinant=p[0]*q[1]-p[1]*q[0]
        if determinant==0:
            raise AssertionError('unexpected dependent signed directions')
        admissible=set()
        for ep,eq in product((-1,0,1),repeat=2):
            if (ep,eq)==(0,0):continue
            a=Fraction(ep*q[1]-eq*p[1],determinant)
            b=Fraction(p[0]*eq-q[0]*ep,determinant)
            if all(a*x+b*y in (-1,0,1) for x,y in us):
                admissible.add(primitive_direction(a,b))
        assert len(admissible) <= {2:4,3:3,4:2}[k],(us,admissible)
        maximum=max(maximum,k*len(admissible))
assert maximum==9
print('VERIFY_OK')
print('units',len(units),'signed_rank_one',len(rankone),'total',len(S))
print('multiplications_checked',len(S)**2)
print('maximum_signed_incidence_projective_pair_count',maximum)
print('actual_support_pairings',[[sum(a*b for a,b in zip(u,v)) for u in U] for v in V])
