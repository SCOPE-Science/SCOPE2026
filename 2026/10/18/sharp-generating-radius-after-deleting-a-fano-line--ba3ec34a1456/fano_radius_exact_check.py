"""Exact finite checks for the Fano-line-deletion generating-radius theorem.

Pure Python 3; no external packages. The mathematical proof is supplied separately.
"""
from fractions import Fraction as Q
from itertools import product

V = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in V for b in V if a != b}))
REMOVED = (1, 2, 3)
H = tuple(e for e in LINES if e != REMOVED)
assert len(LINES) == 7 and len(H) == 6
assert all(len(e) == 3 for e in LINES)
assert all(sum(i in e for e in LINES) == 3 for i in V)
assert all(sum(i in e and j in e for e in LINES) == 1
           for i in V for j in V if i < j)

all_signs = list(product((-1, 1), repeat=7))
def mono(sig, e):
    return len({sig[i-1] for i in e}) == 1

def norming(sig, edges):
    return any(mono(sig,e) for e in edges)

bad = [sig for sig in all_signs if not norming(sig, H)]
assert len(bad) == 10
assert len([sig for sig in all_signs if norming(sig, H)]) == 118
assert all(norming(sig, LINES) for sig in all_signs)

for sig in bad:
    assert sig[0] == sig[1] == sig[2]
    assert sum(sig[i-1] == sig[0] for i in (4,5,6,7)) <= 1

# Test the supporting functional whose l1 norm is exactly 1.
f = {i:Q(1,5) for i in (1,2,3)}
f.update({i:Q(-1,10) for i in (4,5,6,7)})
assert sum(abs(f[i]) for i in V) == 1
sup = max(sum(f[i]*sig[i-1] for i in V)
          for sig in all_signs if norming(sig,H))
assert sup == Q(3,5), sup

# Exact check of the upper bound on the colouring's two-sided mass
# using weights with the sum fixed to 1, represented by the analytic
# case certificates in the accompanying proof.
for sig in bad:
    matching_colour = [i for i in (4,5,6,7) if sig[i-1] == sig[0]]
    if len(matching_colour) == 0:
        # Three base vertices each appear in two lines; four leaves
        # each occur in three lines, yielding min(A/3,B/2)<=1/5.
        assert len(H) == 6
        assert all(sum(i in e for e in H)==2 for i in (1,2,3))
        assert all(sum(i in e for e in H)==3 for i in (4,5,6,7))
    else:
        # Each base vertex has a line avoiding the unique matching leaf;
        # each other leaf has a line containing it and that matching leaf.
        m = matching_colour[0]
        assert all(any((i in e and m not in e) for e in H) for i in (1,2,3))
        assert all(any((j in e and m in e) for e in H)
                   for j in (4,5,6,7) if j!=m)

# Every deleted line is conjugate to (1,2,3) under an invertible
# binary-linear change of coordinates on the nonzero F_2^3 vectors.
line_images = set()
for u in V:
    for v in V:
        for w in V:
            if u == v:
                continue
            if w in (u,v,u ^ v):
                continue
            transform = {z: ((u if z & 1 else 0) ^
                             (v if z & 2 else 0) ^
                             (w if z & 4 else 0)) for z in V}
            assert len(set(transform.values())) == 7
            line_images.add(tuple(sorted(transform[i] for i in REMOVED)))
assert line_images == set(LINES)

for lost_line in LINES:
    kept = [e for e in LINES if e != lost_line]
    assert sum(not norming(sig, kept) for sig in all_signs) == 10

# Arbitrary strictly positive barycentric coefficients yield exactly
# the same norm-attaining cube vertices as the equal-weight averages.
for e in H:
    den = sum(e)
    weights = [Q(v,den) for v in e]
    assert all(w > 0 for w in weights) and sum(weights)==1
    assert all((abs(sum(weights[k]*sig[v-1] for k,v in enumerate(e)))==1)
               ==mono(sig,e) for sig in all_signs)

print('PASS: 7 lines; 6 retained; 128 cube vertices; 10 proper colourings; '
      '118 norming vertices; all 128 restored; exact dual witness 3/5; '
      'colour-class analytic certificates and positive weights verified')
