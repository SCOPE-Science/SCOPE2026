"""Reproduce finite combinatorial identities for the six-stake Bernoulli theorem.

All fractions and comparisons use exact Python integer arithmetic. The mathematical
proof of the unrestricted theorem appears in RESULT.md; finite tests are corroboration.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

V=range(6)
PAIRS=list(combinations(V,2))
TRIPLES=list(combinations(V,3))
ALL_MATCHINGS=set()
def perfect_matchings(points):
    points=tuple(points)
    if not points:
        yield ()
    else:
        a=points[0]
        for b in points[1:]:
            for rest in perfect_matchings(tuple(x for x in points[1:] if x!=b)):
                yield tuple(sorted(((a,b),)+rest))
ALL_MATCHINGS=set(perfect_matchings(V))
assert len(ALL_MATCHINGS)==15
for e in PAIRS:
    assert sum(e in m for m in ALL_MATCHINGS)==3
for e,f in combinations(PAIRS,2):
    if set(e).isdisjoint(f):
        assert any(e in m and f in m for m in ALL_MATCHINGS)

# Exact extremal 2-intersecting triple-family cardinality. Small finite lemma.
max_2int=0
for mask in range(1<<len(TRIPLES)):
    chosen=[TRIPLES[i] for i in range(20) if (mask>>i)&1]
    if len(chosen)<=max_2int:
        continue
    if all(len(set(a)&set(b))>=2 for a,b in combinations(chosen,2)):
        max_2int=len(chosen)
assert max_2int==4

# Independent check of admissible weight vectors and exact probability.
def weighted_tail(weights,p):
    assert len(weights)==6 and sum(weights)==1 and 0<p<=F(1,3)
    tot=F(0)
    accepted=[0]*7
    for k in range(7):
        for s in combinations(V,k):
            if sum((weights[i] for i in s),F(0))>=p:
                accepted[k]+=1
                tot+=p**k*(1-p)**(6-k)
    return tot,accepted

def T(r,p):
    return sum(F(comb(r,k))*p**k*(1-p)**(r-k) for k in range(2,r+1))

examples=[
    (F(9,50),[F(1,6)]*6,6),
    (F(9,40),[F(199,1000)]*5+[F(1,200)],5),
    (F(3,10),[F(499,2000)]*4+[F(1,1000)]*2,4),
    (F(1,5),[F(1,6)]*6,6),
    (F(1,4),[F(199,1000)]*5+[F(1,200)],5),
    (F(1,3),[F(499,2000)]*4+[F(1,1000)]*2,4)
]
for p,w,r in examples:
    assert sum(w)==1
    assert max(w)<p
    z,counts=weighted_tail(w,p)
    assert z==T(r,p), (p,r,z,T(r,p),counts)
    assert z>p

# Polynomial identities from the pair/triple counts; degree at most 6.
for num in range(1,12):
    p=F(num,13)
    if 0<p<1:
        tail_ge4=sum(F(comb(6,k))*p**k*(1-p)**(6-k) for k in range(4,7))
        E5=10*p*p*(1-p)**4+20*p**3*(1-p)**3+tail_ge4
        E4=6*p*p*(1-p)**4+16*p**3*(1-p)**3+tail_ge4
        assert E5==T(5,p), (p,E5,T(5,p))
        assert E4==T(4,p), (p,E4,T(4,p))
        assert (5*p*p*(1-p)**4+20*p**3*(1-p)**3+tail_ge4)-E4==p*p*(1-p)**3*(5*p-1)

# Independent finite rational grid test beyond the constructed extremizers.
for p in (F(9,50),F(9,40),F(3,10),F(1,3)):
    threshold=6 if p<=F(1,5) else (5 if p<=F(1,4) else 4)
    for a in range(1,20):
      for b in range(1,20):
        for c in range(1,20):
          w=[F(a,a+b+c+3),F(b,a+b+c+3),F(c,a+b+c+3)]+[F(1,a+b+c+3)]*3
          if max(w)<p:
            z,_=weighted_tail(w,p)
            assert z>=T(threshold,p)
print('PASS: 15 perfect matchings, pair incidence, exact 2-intersection maximum, six extremizers, polynomial identities, rational witness-grid checks')
