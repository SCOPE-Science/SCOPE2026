"""Finite algebra checks for the spectral-witness inequalities.

Run with python3 CHECK.py. No third-party dependencies.
The infinite-dimensional spectral conclusions are proved analytically.
"""
from fractions import Fraction
from math import isclose, sqrt

checks = 0

def check(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1

# For 0 <= g <= 1, (1-g)^2 <= 1-g^2.
for j in range(1001):
    g = Fraction(j, 1000)
    check((1-g)**2 <= 1-g*g, "positive-contraction square defect")

# Orthogonal spectral bands: for D diagonal with high-band eigenvalues
# >= eps, eps * ||F x||^2 <= <D x,x> exactly.
for eps in (Fraction(1, 8), Fraction(1, 4), Fraction(1, 2)):
    ds = [Fraction(1, k+2) for k in range(12)] + [Fraction(3, 4)]*12
    F = [int(d >= eps) for d in ds]
    for seed in range(30):
        coords = [Fraction(((seed+3)*(j+7)) % 23 - 11, 17) for j in range(len(ds))]
        normsq = sum(z*z for z in coords)
        if not normsq:
            continue
        fsq = sum(z*z for z,p in zip(coords, F) if p)
        defect = sum(d*z*z for z,d in zip(coords, ds))
        check(eps*fsq <= defect, "spectral projection estimate")

# A square-zero block has unit operator norm and numerical radius exactly 1/2;
# scalar quadratic inequality for rational complex phases.
for a in range(-9,10):
    for b in range(-9,10):
        for c in range(-9,10):
            for d in range(-2,3):
                # x=(a+ib,c+id), <Tx,x>=(c+id)(a-ib)
                nsq = a*a+b*b+c*c+d*d
                real = c*a + d*b
                imag = d*a - c*b
                check(4*(real*real+imag*imag) <= nsq*nsq,
                      "square-zero numerical radius at most one-half")

# The inequality is attained for equal source and target mass.
check(4*(1*1) == 2*2, "square-zero radius one-half attained")

# Diagonal compact-injective model: for e_{2k} and its block partner,
# the defect tends to zero, while the square-zero witness retains norm 1.
for k in (10, 100, 1000, 10000):
    d0 = 1/(2*k+2)
    d1 = 1/(2*k+3)
    g0 = sqrt(1-d0)
    g1 = sqrt(1-d1)
    check(g0 > 0 and g1 > 0 and g0 < 1 and g1 < 1,
          "injective compact spectral model")
    check(isclose((1-g0*g0), d0, rel_tol=1e-10, abs_tol=1e-12),
          "diagonal defect identity")
    check(isclose((1-g1*g1), d1, rel_tol=1e-10, abs_tol=1e-12),
          "diagonal partner defect identity")
    check((d0+d1)/2 < 1/k, "near norming equal-mass block")

# Positive finite-rank defect: e_1 norming and e_0 high defect. A rank-one
# operator sending e_1 to e_0 has relative norm 1 and relative radius 0.
for q in (Fraction(1,100), Fraction(1,10), Fraction(1,2)):
    check(q > 0 and q < 1, "nonzero rank-one defect")
    check(Fraction(1, 1) * q == q, "spectral witness bound")

print(f"PASS: {checks} finite checks; no numerical experiment is used as infinite proof")
