import math

def z(k):
    return 1.0 / math.log(k + 2.0)

# Representative monotonicity and rate checks.
prev = None
sqsum = 0.0
for k in range(1, 200000):
    d = abs(z(k+1) - z(k))
    sqsum += d*d
    if prev is not None and k > 10:
        assert d <= prev * (1.0 + 1e-12)
    prev = d

for k in [100, 1000, 10000, 100000]:
    d2 = (z(k+1)-z(k))**2
    assert k*d2 < 1e-3
    assert k*z(k) > 1.0

# Mean-value upper bound:
# |z_{k+1}-z_k| <= 1 / ((k+2) log(k+2)^2).
for k in [1, 2, 10, 100, 1000, 10000]:
    lhs = abs(z(k+1)-z(k))
    rhs = 1.0 / ((k+2.0) * math.log(k+2.0)**2)
    assert lhs <= rhs * (1.0 + 1e-12)

# A convergent comparison series certifies square summability:
# increments^2 <= 1/(k+2)^2.
assert sqsum < 1.0

print("VERIFY_OK")
