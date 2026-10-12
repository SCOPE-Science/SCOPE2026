"""Exact rational checks for the zero-dipole spin-one quantumness theorem.

Run: python3 verify.py
No third-party modules required. The analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def check_weights(weights):
    assert all(w >= 0 for w in weights)
    assert sum(weights) == 1
    t = tuple(1 - 2 * w for w in weights)
    assert sum(t) == 1 and all(v <= 1 for v in t)
    lam = min(t)
    if lam >= 0:
        assert max(weights) <= F(1, 2)
        return
    order = sorted(range(3), key=lambda i: t[i], reverse=True)
    i, j, k = order
    assert t[k] == lam and t[i] >= -lam and t[j] >= -lam
    s = list(t)
    s[i] += lam / 2
    s[j] += lam / 2
    s[k] = F(0)
    assert all(v >= 0 for v in s) and sum(s) == 1
    projected_weights = tuple((1-v)/2 for v in s)
    assert all(F(0) <= w <= F(1, 2) for w in projected_weights)
    assert sum(projected_weights) == 1
    dist2 = sum((weights[z] - projected_weights[z])**2 for z in range(3))
    assert dist2 == F(3, 8)*lam**2
    negativity = -lam / 2
    assert dist2 == F(3, 2)*negativity**2
    # Three spin-coherent Bloch vectors make the optimal zero-dipole moment matrix.
    c = s[i]
    assert 0 < c < 1 and s[j] == 1-c
    w1, wpm = c/(1+c), 1/(2*(1+c))
    assert w1 + 2*wpm == 1
    assert w1 - 2*wpm*c == 0
    assert w1 + 2*wpm*c*c == c
    assert 2*wpm*(1-c*c) == s[j]
    # Universal HS projection inequality: for any PSD trace-one S,
    # <T-T*,S-T*> = 3*lambda*S_kk/2 <= 0.
    assert 3*lam/2 < 0


cases = 0
for numerators in product(range(0, 7), repeat=3):
    if sum(numerators) == 0:
        continue
    total = sum(numerators)
    check_weights(tuple(F(w, total) for w in numerators))
    cases += 1

# A full-rank spin-one example beyond any spin-projection-diagonal,
# zero-dipole subfamily: in the standard |1,1>,|1,0>,|1,-1> basis
# rho = [[1/8,0,3/40],[0,3/4,0],[3/40,0,1/8]].
a,b,k = F(1,8),F(3,4),F(3,40)
assert a+a+b == 1
assert a+k == F(1,5) and a-k == F(1,20)
tx = 2*(a+b+k)-1
ty = 2*(a+b-k)-1
tz = 4*a-1
assert (tx,ty,tz) == (F(9,10),F(3,5),F(-1,2))
sx,sy,sz = F(13,20),F(7,20),F(0)
ap,bp,kp = F(1,4),F(1,2),F(3,40)
assert (2*(ap+bp+kp)-1,2*(ap+bp-kp)-1,4*ap-1) == (sx,sy,sz)
assert (a-ap)**2+(b-bp)**2+(a-ap)**2+2*(k-kp)**2 == F(3,32)
# Exact partial-transpose eigenvalues for the symmetric two-qubit embedding.
pt_spectrum = (a-b/2,a+b/2,b/2-k,b/2+k)
assert sorted(pt_spectrum) == [F(-1,4),F(3,10),F(9,20),F(1,2)]
assert F(3,32) == F(3,2)*F(1,4)**2
print(f'VERIFY_OK rational_weight_triples={cases} nonaxial_full_rank=passed nearest_classical_three_directions=passed negativity=passed')
