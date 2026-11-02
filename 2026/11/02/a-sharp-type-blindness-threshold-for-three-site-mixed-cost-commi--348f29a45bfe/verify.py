"""Exact finite checks supplementing the analytic three-site classification.

Run: python3 verify.py
The general theorem follows from the identities in RESULT.md, not this enumeration.
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random

PAIRS = ((0, 1), (1, 2), (0, 2))

def costs_triangle(p, r, q, types):
    """Three sites: distances d01=p, d12=r, d02=q; type 1=max, 0=average."""
    d = ((F(0), p, q), (p, F(0), r), (q, r, F(0)))
    return tuple(sum((max(d[i][j] for j in pair) if types[i]
                      else sum((d[i][j] for j in pair), F(0))/2)
                     for i in range(3)) for pair in PAIRS)

def costs_general(points, types):
    return {pair: sum((max(abs(points[i]-points[j]) for j in pair) if types[i]
                       else sum((abs(points[i]-points[j]) for j in pair), F(0))/2)
                       for i in range(len(points)))
            for pair in combinations(range(len(points)), 2)}

def check_triangle(p, r, q):
    assert 0 < p <= r <= q <= p+r
    rows = [costs_triangle(p, r, q, t) for t in product((0,1), repeat=3)]
    universal = {j for j in range(3) if all(row[j] == min(row) for row in rows)}
    assert bool(universal) == (3*p <= q+r), (p,r,q,universal)
    if 3*p <= q+r:
        assert 0 in universal
    # Both homogeneous preference configurations choose a shortest edge.
    assert rows[0][0] == min(rows[0])
    assert rows[-1][0] == min(rows[-1])
    # Verify critical affine differences for each binary type vector.
    for t,row in zip(product((0,1),repeat=3), rows):
        t0,t1,t2=t
        twice_AB=(p-r)+(2*p-q)*t0+(p-r)*t1+(q-2*r)*t2
        twice_AC=(p-q)+(p-q)*t0+(2*p-r)*t1-r*t2
        assert 2*(row[0]-row[1])==twice_AB
        assert 2*(row[0]-row[2])==twice_AC

integer_cases=0
for p in range(1,45):
    for r in range(p,45):
        for q in range(r,min(44,p+r)+1):
            check_triangle(F(p),F(r),F(q))
            integer_cases += 1
rng=Random(20626074)
rational_cases=0
for _ in range(12000):
    triples=sorted((F(rng.randrange(1,65),rng.randrange(1,12)) for _ in range(3)))
    p,r,q=triples
    if q <= p+r:
        check_triangle(p,r,q)
        rational_cases += 1

p,r,q=F(3),F(4),F(4)
assert costs_triangle(p,r,q,(0,0,0))==(F(7),F(15,2),F(15,2))
assert costs_triangle(p,r,q,(1,0,0))==(F(17,2),F(8),F(19,2))
assert costs_triangle(p,r,q,(0,0,0))[0] < min(costs_triangle(p,r,q,(0,0,0))[1:])
assert costs_triangle(p,r,q,(1,1,1))[0] < min(costs_triangle(p,r,q,(1,1,1))[1:])
assert costs_triangle(p,r,q,(1,0,0))[1] < costs_triangle(p,r,q,(1,0,0))[0]

points=(F(0),F(1),F(3),F(4))
sum_costs=costs_general(points,(0,0,0,0))
max_costs=costs_general(points,(1,1,1,1))
assert {p for p,v in sum_costs.items() if v==min(sum_costs.values())}=={(1,2)}
assert {p for p,v in max_costs.items() if v==min(max_costs.values())}=={(0,1),(2,3)}
assert sum_costs[(1,2)]==F(6)
assert max_costs[(1,2)]==F(10)
assert max_costs[(0,1)]==F(9)
print('PASS:',integer_cases,'integer triangles;',rational_cases,'rational triangles; all 8 types;',
      'affine identities; 3,4,4 metric witness; 0,1,3,4 line witness')
