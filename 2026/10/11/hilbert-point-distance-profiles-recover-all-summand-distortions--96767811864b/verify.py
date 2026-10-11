from fractions import Fraction
import math

def r_of_p(p):
    if p == 2:
        return math.inf
    return 2*p/abs(p-2)

# Exact rational algebra for p_r and one-sided reciprocal exponents.
for r in (3, 4, 5, 10, 37, 100):
    rr = Fraction(r, 1)
    p = 2*rr/(rr-2)
    assert r_of_p(p) == rr

for n in (5, 10, 37, 101):
    h = Fraction(1, n)
    rp = r_of_p(Fraction(2,1)+h)
    rm = r_of_p(Fraction(2,1)-h)
    assert 1/rp == h/(2*(Fraction(2,1)+h))
    assert 1/rm == h/(2*(Fraction(2,1)-h))

def profile(ds, p):
    if p == 2.0:
        return max(ds)
    r = 2.0*p/abs(p-2.0)
    logs = [r*math.log(d) for d in ds]
    M = max(logs)
    return math.exp((M + math.log(sum(math.exp(x-M) for x in logs)))/r)

# Cusp test for a tied maximum.
ds = [1.4, 1.4, 1.1]
D = 1.4
want = math.log(2.0)/4.0
for h in (0.05, 0.02, 0.01, 0.005):
    right = (math.log(profile(ds, 2.0+h))-math.log(D))/h
    left = (math.log(profile(ds, 2.0-h))-math.log(D))/(-h)
    assert abs(right-want) < 0.01
    assert abs(left+want) < 0.01

# Unique maximum: the normalized slope is rapidly flat.
ds = [1.4, 1.2, 1.1]
for h in (0.05, 0.02):
    right = abs((math.log(profile(ds,2.0+h))-math.log(1.4))/h)
    assert right < 1e-5

# Dominant-exponential recovery for a sample multiset.
ds = [1.7, 1.7, 1.3, 1.1]
for r in (40.0, 80.0, 160.0):
    S = sum(d**r for d in ds)
    Dhat = math.exp(math.log(S)/r)
    mhat = S/(1.7**r)
    assert Dhat >= 1.7 and Dhat < 1.75
    assert abs(mhat-2.0) < 1e-4

print('VERIFY_OK')
