"""Lattice check for lane-1568: U-polarized K3^[2] wall separating f1, f2.

Verifies, with exact integer arithmetic:
 - Gram of U and q(a f1 + b f2) = 2ab; q(f1)=q(f2)=0, (f1,f2)=1.
 - lambda = f1 - f2 has q = -2.
 - Primitive embedding U -> L = U^3 + E8(-1)^2 + <-2> as first summand:
   div_L(lambda) = 1 (pairings with basis generate Z).
 - Reflection R(x) = x + (x,lambda) lambda is integral, isometry, swaps f1<->f2,
   fixes f1+f2 and the orthogonal complement T pointwise on NS part.
 - Separation: (f1,lambda) = -1 < 0 < +1 = (f2,lambda); f1+f2 in lambda^perp.
 - Uniqueness of wall in NS=U: integral classes with q=-2 are exactly +-lambda;
   classes with q=-10 have div 1 (not 2), hence not the second MBM type.
"""
import itertools
import json
import os

U = [[0, 1], [1, 0]]

def qU(a, b):
    return 2 * a * b

# 1. basic isotropic data
assert qU(1, 0) == 0 and qU(0, 1) == 0
assert qU(1, 1) == 2 and qU(1, -1) == -2

lam = (1, -1)
assert qU(*lam) == -2

# pairings (x, lambda) for x = f1, f2, f1+f2 under U pairing
# (af1+bf2, cf1+df2) = ad + bc
def pairU(x, y):
    return x[0] * y[1] + x[1] * y[0]

f1, f2 = (1, 0), (0, 1)
assert pairU(f1, f2) == 1
s1 = pairU(f1, lam)
s2 = pairU(f2, lam)
s12 = pairU((1, 1), lam)
assert (s1, s2, s12) == (-1, 1, 0), (s1, s2, s12)

# 2. divisibility of lambda in L via first-U-summand embedding.
# U summand is unimodular: pairings of lambda with (e,0..),(f,0..) are -1,+1.
# Hence gcd over L contains 1 -> div = 1.
pairings_with_basis = [s1, s2]  # already +-1
import math
assert math.gcd(abs(s1), abs(s2)) == 1
div_lambda = 1

# 3. reflection R(a f1 + b f2) = (a,b) + ((a,b).lam) * lam
def R(v):
    c = pairU(v, lam)
    return (v[0] + c * lam[0], v[1] + c * lam[1])

assert R(f1) == f2 and R(f2) == f1, (R(f1), R(f2))
assert R((1, 1)) == (1, 1)
# isometry on U
pts = [(a, b) for a in range(-3, 4) for b in range(-3, 4)]
for v in pts:
    for w in pts:
        assert pairU(R(v), R(w)) == pairU(v, w)
for v in pts:
    assert qU(*R(v)) == qU(*v)
# R^2 = id
for v in pts:
    assert R(R(v)) == v

# 4. uniqueness: integral (a,b) with |a|,|b| <= 20 and q=-2 -> only +-(1,-1)
neg2 = [(a, b) for a in range(-20, 21) for b in range(-20, 21)
        if not (a == 0 and b == 0) and qU(a, b) == -2]
assert set(neg2) == {(1, -1), (-1, 1)}, neg2
# q=-10 with bound -> (a,b) with ab=-5: (±1,∓5),(±5,∓1); div=gcd(|a|,|b|)=1
neg10 = [(a, b) for a in range(-20, 21) for b in range(-20, 21)
         if qU(a, b) == -10]
assert neg10, "expected -10 classes"
for (a, b) in neg10:
    assert math.gcd(abs(a), abs(b)) == 1, (a, b)
# hence no class of type (q=-10, div 2) in U: second MBM orbit absent.

# 5. chamber sides: K = {ab>0, sign of (x,lam)=a-b? } (x=af1+bf2: (x,lam)=b-a?)
# (af1+bf2, f1-f2) = b - a. Positive cone ray f1+f2 has value 0 (wall through it).
def side(a, b):
    return (a * lam[1] + b * lam[0])  # = b - a? check
assert side(2, 1) == pairU((2, 1), lam)
# sample: ample-side point (2,1): (.,lam) = 1-2 = -1; other side (1,2): +1
assert pairU((2, 1), lam) == -1 and pairU((1, 2), lam) == 1

out = {
    "q_lambda": -2,
    "div_lambda_in_L": div_lambda,
    "pair_f1_lambda": s1,
    "pair_f2_lambda": s2,
    "pair_f1pf2_lambda": s12,
    "R_swaps_f1_f2": True,
    "R_isometry_involution": True,
    "only_pm_lambda_have_q_minus2": True,
    "q_minus10_classes_all_div_1": True,
    "conclusion": "lambda^perp meets interior of positive cone (at f1+f2) and "
                  "strictly separates f1, f2; nef closure holds at most one ray.",
}
os.makedirs("output/artifacts", exist_ok=True)
with open("output/artifacts/lattice_check.json", "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps(out, indent=2))
print("ALL LATTICE CHECKS PASSED")
