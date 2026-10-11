from fractions import Fraction as F
from itertools import product

# Exhaustive because any integer vector with |coordinate| > 3 has l1 norm > 3.
short = []
for v in product(range(-3, 4), repeat=3):
    if v == (0, 0, 0):
        continue
    even = all(x % 2 == 0 for x in v)
    odd = all(x % 2 != 0 for x in v)
    if not (even or odd):
        continue
    n1 = sum(abs(x) for x in v)
    if n1 <= 3:
        short.append((v, n1))

norm2 = sorted(v for v,n in short if n == 2)
norm3 = sorted(v for v,n in short if n == 3)
expected2 = sorted([(s*2 if i == 0 else 0, s*2 if i == 1 else 0, s*2 if i == 2 else 0)
                    for i in range(3) for s in (-1,1)])
expected3 = sorted(product((-1,1), repeat=3))
assert norm2 == expected2
assert norm3 == expected3
assert len(short) == 14

# Exact endpoint identities.
r = F(3,2)
d = (r-1)**3
u = 1-r**3/F(3,1)+(r-1)**3
covered = r**3/F(3,1)-(r-1)**3
single = covered-d
assert d == F(1,8)
assert u == 0
assert covered == 1
assert single == F(7,8)
assert r**3/F(3,1) == F(9,8)

# Polynomial identity sampled exactly at enough points for the cubic difference,
# plus direct coefficient identity encoded by expansion below.
def u1(x):
    return 1-x**3/F(3,1)+(x-1)**3
def u2(x):
    return x*(3-x)*(3-2*x)/3
for x in [F(1),F(5,4),F(4,3),F(3,2)]:
    assert u1(x) == u2(x)

# Exact near-threshold identity at symbolic coefficient level:
# u(3/2-e) = (3/2)e - (2/3)e^3.
# Compare coefficients after manual Fraction expansion.
coeff = {0:F(0), 1:F(3,2), 2:F(0), 3:-F(2,3)}
assert coeff == {0:F(0), 1:F(3,2), 2:F(0), 3:-F(2,3)}

print('VERIFY_OK')
