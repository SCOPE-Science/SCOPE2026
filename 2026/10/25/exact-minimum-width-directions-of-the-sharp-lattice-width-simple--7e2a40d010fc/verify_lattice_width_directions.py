from itertools import product, permutations
from fractions import Fraction

# The equality simplex from Aliev's reverse-isodiametric theorem.
# For u=(a,b,c), put s=a+b+c and x_i=s+u_i. Then sum(x_i)=4s.
# This script checks the finite equality shell; the infinite lower bound is
# proved analytically in RESULT.md, not inferred from bounded enumeration.

def map_back(x):
    total = sum(x)
    assert total % 4 == 0
    s = total // 4
    return tuple(v - s for v in x)

def width_twice_from_x(x):
    values = (0,) + tuple(x)
    return max(values) - min(values)

xs = []
for x in product(range(-2, 3), repeat=3):
    if sum(x) % 4 == 0 and width_twice_from_x(x) == 2:
        xs.append((x, map_back(x)))

directions = {u for _, u in xs}
expected = set()
for i in range(3):
    for sign in (-1, 1):
        u = [0, 0, 0]
        u[i] = sign
        expected.add(tuple(u))
for p in permutations((1, -1, 0)):
    expected.add(p)
    expected.add(tuple(-v for v in p))
for p in permutations((1, 1, -1)):
    expected.add(p)
    expected.add(tuple(-v for v in p))

assert directions == expected
assert len(directions) == 18
assert all(width_twice_from_x(tuple(sum(u) + v for v in u)) == 2 for u in directions)

# Exact determinant of [[1,1/2,1/2],[1/2,1,1/2],[1/2,1/2,1]].
a = Fraction(1, 1); b = Fraction(1, 2)
det = a*(a*a-b*b) - b*(b*a-b*b) + b*(b*b-a*b)
assert det == Fraction(1, 2)
volume = abs(det) / 6
assert volume == Fraction(1, 12)
print(f"verified {len(directions)} oriented directions; volume={volume}")
