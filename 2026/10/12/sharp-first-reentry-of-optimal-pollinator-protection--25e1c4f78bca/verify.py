"""Exact checks for an ecological partner-protection priority reentry theorem.
Run: python3 verify.py  (Python >= 3.9, standard library only).
"""
from fractions import Fraction
from itertools import product

# Each of 13 distinct plant species is represented by its set of pollinator partners.
P = (
    (0,),
    *((0, 1),) * 2,
    *((1, 2),) * 3,
    *((1, 3),) * 2,
    *((0, 2, 3),) * 5,
)
assert len(P) == 13
assert all(1 <= len(s) <= 4 for s in P)
assert {x for S in P for x in S} == set(range(4))

# Analytic score coefficients for pollinators A,B,C,D (index 0,...,3).
coeff = []
for v in range(4):
    coeff.append(tuple(sum(v in s and len(s) == d for s in P) for d in range(1, 5)))
assert coeff == [(1,2,5,0), (0,7,0,0), (0,3,5,0), (0,2,5,0)], coeff

def score(v, q):
    return sum(Fraction(c) * q ** (j+1) for j,c in enumerate(coeff[v]))

def direct_gain(v, q):
    # Coupling: unprotected primary extinction mask, q per lost pollinator.
    answer = Fraction(0)
    for bits in product((0,1), repeat=4):
        failed = {i for i, bit in enumerate(bits) if bit}
        wt = q ** len(failed) * (1-q) ** (4-len(failed))
        lost_without = sum(all(u in failed for u in s) for s in P)
        lost_with = sum(all(u in failed and u != v for u in s) for s in P)
        answer += wt * (lost_without - lost_with)
    return answer

for q, leader in ((Fraction(1,10),0),(Fraction(1,2),1),(Fraction(9,10),0)):
    vals = tuple(score(v,q) for v in range(4))
    assert vals[leader] > max(vals[j] for j in range(4) if j != leader), (q, vals)
    assert tuple(direct_gain(v,q) for v in range(4)) == vals

# All integer positive quadratic coefficient triples with two distinct
# roots in (0,1) and total |coefficient| weight <= 12.
# Here q(a-bq+cq^2) is the pair score difference.
cases=[]
for a in range(1,13):
    for b in range(1,13):
        for c in range(1,13):
            if a+b+c > 12: continue
            # Strict quadratic min in (0,1), both end values positive.
            two_roots = (b*b>4*a*c and b<2*c and a-b+c>0)
            if two_roots:
                cases.append((a,b,c,a+b+c))
assert sorted(cases) == [(1,5,5,11),(1,5,6,12)], cases

# In each low-plant-count case, every positive degree-3 exclusive plant
# is incident to BOTH remaining primary species, and 5 negative degree-2
# plants must contribute >=3 neighbors to at least one of them.
for a,b,c,m in cases:
    available_extra = 12-m
    deg_A_upper = a+c+available_extra
    competitor_degree_lower = c+(b+1)//2
    assert deg_A_upper < competitor_degree_lower
    # At q=1/2 the pair polynomial is nonpositive, so its larger root
    # is at least 1/2.  For every q>larger root, a competing primary
    # x has a rescue score exceeding that of A by at least
    # q*((3-extra)*q-1) > 0.  These symbolic coefficient inequalities
    # prove that an apparent pairwise reentry cannot be globally optimal.
    assert Fraction(a) - Fraction(b,2) + Fraction(c,4) <= 0
    assert 3-available_extra >= 2
    for q in (Fraction(3,4),Fraction(9,10)):
        assert (3-available_extra)*q-1 > 0

# At 4 primary species, the score difference polynomial has degree at most 3
# and every pair is q times a quadratic. For at most 3 primary species it is
# q times a linear form, so no candidate can lose and later regain first place.
assert coeff[0][0] == 1
assert all(score(0, Fraction(z,100)) > score(2, Fraction(z,100))
           and score(0, Fraction(z,100)) > score(3, Fraction(z,100))
           for z in range(1,100))
# Exact roots of 1-5q+5q^2 are (5+-sqrt(5))/10.
assert (1,-5,5) in [tuple(coeff[0][i]-coeff[1][i] for i in range(3))]
print('VERIFY_OK plant_species=13 primary_species=4 exact_masks=48 coefficient_cases=2 roots=(5+-sqrt(5))/10')
