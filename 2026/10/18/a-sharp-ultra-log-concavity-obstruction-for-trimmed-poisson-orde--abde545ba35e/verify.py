"""Exact coefficient checks for low tails of top-r Poisson sums.

Run with Python 3 standard library: python verify.py
Computations certify finite enumerated parameter ranges only; general claims
follow from the proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp


def top_r_sum(x, r):
    return sum(sorted(x, reverse=True)[:r])


def lowtail_coefficients(m, r):
    """Return exact coefficients of exp(m lambda) P(Y=k), 0<=k<=r."""
    out = [dict() for _ in range(r + 1)]
    for sample in product(range(r + 1), repeat=m):
        v = top_r_sum(sample, r)
        if v > r:
            continue
        total = sum(sample)
        denom = 1
        for x in sample:
            denom *= factorial(x)
        out[v][total] = out[v].get(total, Fraction(0)) + Fraction(1, denom)
    return out


def target_coefficients(m, r):
    out = [{k: Fraction(m**k, factorial(k))} for k in range(r + 1)]
    for j in range(r + 1, m + 1):
        out[r][j] = Fraction(comb(m, j))
    return out


def poly_product(a, b):
    z = {}
    for x, u in a.items():
        for y, v in b.items():
            z[x + y] = z.get(x + y, Fraction(0)) + u * v
    return {k:v for k,v in z.items() if v}


def poly_scaled_diff(a, x, b, y):
    z = {}
    for k,v in a.items():
        z[k] = z.get(k,Fraction(0))+x*v
    for k,v in b.items():
        z[k] = z.get(k,Fraction(0))-y*v
    return {k:v for k,v in z.items() if v}


def evaluate(a, x):
    return sum(v*x**k for k,v in a.items())


checks = 0
for m in range(3, 7):
    for r in range(2, m):
        got = lowtail_coefficients(m, r)
        want = target_coefficients(m, r)
        assert got == want, (m,r,got,want)
        checks += r+1
        ulc = poly_scaled_diff(poly_product(got[r-1], got[r-1]), r-1,
                               poly_product(got[r-2], got[r]), r)
        excess = {j:Fraction(comb(m,j)) for j in range(r+1,m+1)}
        proof_ulc = {j+r-2: -Fraction(r*m**(r-2),factorial(r-2))*v
                     for j,v in excess.items()}
        assert ulc == proof_ulc, (m,r,ulc,proof_ulc)
        checks += len(proof_ulc)
        assert all(v < 0 for v in proof_ulc.values())
        checks += len(proof_ulc)
        ordinary = poly_scaled_diff(poly_product(got[r-1],got[r-1]), 1,
                                    poly_product(got[r-2],got[r]), 1)
        for rate in (Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5),Fraction(10),Fraction(50)):
            sign1 = evaluate(ordinary,rate)
            rhs = Fraction(m**r,factorial(r)*(r-1))
            lhs = sum(Fraction(comb(m,j))*rate**(j-r) for j in range(r+1,m+1))
            assert (sign1>0)-(sign1<0) == (rhs>lhs)-(rhs<lhs)
            checks+=1

# Independent finite checks of the published maximum-order-statistic closure
# at two rational intensities. The full infinite theorem is cited in RESULT.md.
for m in range(2, 7):
    for rate in (Fraction(1, 2), Fraction(1), Fraction(3)):
        cdf_unscaled = []
        total = Fraction(0)
        for k in range(15):
            total += rate**k / factorial(k)
            cdf_unscaled.append(total)
        q = [cdf_unscaled[0]**m] + [cdf_unscaled[k]**m-cdf_unscaled[k-1]**m for k in range(1,15)]
        for k in range(1,14):
            assert k*q[k]**2 >= (k+1)*q[k-1]*q[k+1]
            checks+=1

# An independent small example (m=3, r=2):
# q0=exp(-3 lambda), q1=3 lambda exp(-3 lambda),
# q2=(9 lambda^2 /2 + lambda^3) exp(-3 lambda).
assert target_coefficients(3,2)[2] == {2:Fraction(9,2),3:Fraction(1)}
checks+=1
print('PASS: %d exact checks on polynomial coefficients, ULC defects, and local LC signs' % checks)
