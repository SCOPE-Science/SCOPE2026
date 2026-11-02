"""Exact rational and independent finite checks for an edge--isolate covariance theorem.

Run with Python 3.9+: python verify.py. This program is supplemental to the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, sqrt

checks = 0

def check(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)


def q_pair(radius):
    # Two free points in the arc left after forbidding a radius-neighborhood.
    length = 1 - 2 * radius
    if radius >= length:
        return F(1)
    return 1 - (1 - radius / length) ** 2


def covariance(n, radius):
    assert n >= 2 and 0 < radius < F(1, 2)
    p_isolated = (1 - 2 * radius) ** (n - 1)
    return n * (n-1) * p_isolated * (
        -2 * radius + F(n - 2, 2) * (q_pair(radius) - 2 * radius))


def q_area(radius):
    # Independent geometric square-area integration of |X-Y| <= radius.
    length = 1 - 2 * radius
    forbidden_side = max(F(0), length - radius)
    return (length**2 - forbidden_side**2) / length**2


# Conditional two-point integration, independent of the final covariance formula.
for denominator in (11, 37, 103):
    for k in range(1, (denominator + 1) // 2):
        rr = F(k, denominator)
        check(q_area(rr) == q_pair(rr), ('area identity', rr))

# Rational simplification on both geometric regimes.
for n in range(2, 151):
    for j in range(1, 50):
        rr = F(j, 101)
        actual = covariance(n, rr)
        ll = 1 - 2*rr
        if rr <= F(1, 3):
            prediction = n*(n-1)*ll**(n-1)*rr * (
                -4 + (3*n+10)*rr - 8*n*rr**2) / (2 * ll**2)
        else:
            prediction = n*(n-1)*ll**(n-1) * (F(n-2, 2) - n*rr)
        check(actual == prediction, ('two regimes', n, rr))
        if n <= 5:
            check(actual < 0, ('small n', n, rr))

# At six vertices the complete sign window is (1/4, 1/3).
for j in range(1, 500):
    rr = F(j, 1000)
    if rr == F(1, 4) or rr == F(1, 3):
        expected = 0
    else:
        expected = int(F(1, 4) < rr < F(1, 3))*2-1
    actual = covariance(6, rr)
    check((actual > 0) - (actual < 0) == expected, ('n=6', rr))

# Each higher-order first root solves a quadratic, the second is 1/2-1/n.
for n in range(7, 101):
    discriminant = (3*n+10)**2 - 128*n
    lower = ((3*n+10) - sqrt(discriminant)) / (16*n)
    upper = .5 - 1/n
    check(0 < lower < 1/3 < upper < .5, ('root location', n))
    for j in range(1, 500):
        rr = F(j, 1000)
        sign = (covariance(n, rr) > 0) - (covariance(n, rr) < 0)
        predicted = 1 if lower < float(rr) < upper else -1
        # avoid machine roundoff near a zero by strict separation
        if abs(float(rr)-lower) > 1e-9 and abs(float(rr)-upper)>1e-9:
            check(sign == predicted, ('n>=7', n, rr, sign, predicted))

# An independent small finite-configuration grid model is a Riemann approximation
# to the continuum calculation (the discrete model permits repeated positions).
def direct_grid_cov(n, m, rr):
    sum_i = sum_e = sum_ie = 0
    count = m**n
    for tup in product(range(m), repeat=n):
        degree=[0]*n
        edges=0
        for a in range(n):
            for b in range(a+1,n):
                d = F(abs(tup[a]-tup[b]),m)
                if min(d,1-d) <= rr:
                    edges+=1
                    degree[a]+=1
                    degree[b]+=1
        isolates=sum(d==0 for d in degree)
        sum_i+=isolates
        sum_e+=edges
        sum_ie+=isolates*edges
    return F(sum_ie,count)-F(sum_i*sum_e,count*count)

for n,m,r in ((3,23,F(1,5)),(3,23,F(2,5)),
              (4,25,F(1,5)),(4,25,F(7,20))):
    discrete=direct_grid_cov(n,m,r)
    continuous=covariance(n,r)
    check(abs(discrete-continuous) < F(1,2), ('Riemann grid', n,m,r,discrete,continuous))

# A sparse-scale limit follows from the exact formula, checked numerically.
for c in (F(1,2),F(1),F(4,3),F(2),F(4)):
    target=exp(-2*float(c))*(1.5*float(c)**2-2*float(c))
    for n in (5000,10000):
        rr=F(c,n)
        val=float(covariance(n,rr)/n)
        check(abs(val-target)<.003, ('sparse limit', n,c,val,target))

print(f'VERIFY_OK {checks} checks')
