from fractions import Fraction
from math import log2

v = [3, -1, -1, 1]
assert sum(a*a for a in v) == 12
# Unnormalized two-qubit Walsh matrix; H tensor H is W/2.
W = [
    [1, 1, 1, 1],
    [1,-1, 1,-1],
    [1, 1,-1,-1],
    [1,-1,-1, 1],
]
w = [sum(row[j]*v[j] for j in range(4)) for row in W]
assert all(x % 2 == 0 for x in w)
hv = [x//2 for x in w]
assert hv == [1,1,1,3]
assert sum(a*a for a in hv) == 12

def collision(intamps):
    n = sum(a*a for a in intamps)
    return sum(Fraction(a*a, n)**2 for a in intamps)

cz = collision(v)
cx = collision(hv)
assert cz == Fraction(7,12)
assert cx == Fraction(7,12)
assert cz*cx == Fraction(49,144)
product_ceiling = Fraction(81,256)
assert cz*cx > product_ceiling
assert 49*256 - 81*144 == 880
# Coefficient determinant before the common normalization factor sqrt(12).
assert v[0]*v[3] - v[1]*v[2] == 2
entropy_sum = -log2(float(cz*cx))
product_lower = -log2(float(product_ceiling))
assert entropy_sum < product_lower
print('VERIFY_OK')
print('collision_each=', cz)
print('counterexample_product=', cz*cx)
print('product_ceiling=', product_ceiling)
print('entropy_sum=', entropy_sum)
print('product_lower=', product_lower)
