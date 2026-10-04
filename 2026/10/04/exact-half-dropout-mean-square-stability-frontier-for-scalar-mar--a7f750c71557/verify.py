from fractions import Fraction
from math import comb, sqrt

def z_moments(n):
    probs = [Fraction(comb(n,k), 2**n) for k in range(n+1)]
    zs = [Fraction(2*k, n) for k in range(n+1)]
    m1 = sum(p*z for p,z in zip(probs,zs))
    m2 = sum(p*z*z for p,z in zip(probs,zs))
    return m1,m2

def cycle_moments(n,s):
    s = Fraction(s)
    m1z,m2z = z_moments(n)
    assert m1z == 1
    assert m2z == Fraction(n+1,n)
    er = 1-s
    er2 = 1-2*s+s*s*m2z
    m = 1 / (1-Fraction(1,2)*er)
    Q = (1 + er*m) / (1-Fraction(1,2)*er2)
    psi = 1-2*s*m+s*s*Q
    return m,Q,psi,er2

for n in range(1,8):
    m1,m2 = z_moments(n)
    assert m1 == 1
    assert m2 == Fraction(n+1,n)

# Exact algebraic identity for rational test steps.
for n in range(1,8):
    for s in (Fraction(1,10), Fraction(1,2), Fraction(9,10), Fraction(6,5)):
        m,Q,psi,er2 = cycle_moments(n,s)
        den = (1+s) * (n + 2*n*s - (n+1)*s*s)
        if den != 0:
            rhs = Fraction(2)*s*((n+2)*s*s-n*s-2*n)/den
            assert psi-1 == rhs

# Boundary checks and monotonicity.
prev = 0.0
for n in range(1,101):
    sn = (n + sqrt(9*n*n + 16*n))/(2*(n+2))
    assert sn > prev
    assert 1.0 <= sn < 2.0
    prev = sn
    for fac, stable in ((0.8,True),(0.999,True),(1.001,False),(1.2,False)):
        s = fac*sn
        er2 = 1-2*s+(1+1/n)*s*s
        if stable:
            assert er2/2 < 1
        # floating form of cycle factor
        m = 2/(1+s)
        Q = (1+(1-s)*m)/(1-er2/2)
        psi = 1-2*s*m+s*s*Q
        if stable:
            assert psi < 1
        else:
            assert psi > 1

assert abs((1 + sqrt(25))/6 - 1.0) < 1e-15

# Large-n expansion check.
for n in (1000,5000,10000):
    sn = (n + sqrt(9*n*n + 16*n))/(2*(n+2))
    approx = 2 - 8/(3*n) + 128/(27*n*n)
    assert abs(sn-approx) < 1e-8

print("verification passed")
