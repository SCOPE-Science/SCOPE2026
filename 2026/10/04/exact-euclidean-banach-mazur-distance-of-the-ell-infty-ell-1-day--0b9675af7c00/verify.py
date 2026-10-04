from fractions import Fraction

# Exact replay of algebraic identities and sharp equality witnesses.
def norm_sq(x, y):
    if x * y >= 0:
        return max(abs(x), abs(y)) ** 2
    return (abs(x) + abs(y)) ** 2

def q_star(x, y):
    return x*x - x*y + y*y

witnesses = [(1, 1, Fraction(1, 1)), (1, 0, Fraction(1, 1)), (1, -1, Fraction(4, 3))]
for x, y, expected in witnesses:
    ratio = Fraction(norm_sq(x, y), q_star(x, y))
    assert ratio == expected, (x, y, ratio, expected)

# Orthogonal-coordinate identity after clearing the factor sqrt(2):
# u^2 + 3 v^2 = 2 (x^2 - x y + y^2).
for x, y in [(1, 2), (2, -3), (5, 0), (-4, -1)]:
    lhs_cleared = (x + y)**2 + 3*(x - y)**2
    rhs_cleared = 4*(x*x - x*y + y*y)
    assert lhs_cleared == rhs_cleared

# The two distortion branches meet at t=3 with value 4/3.
t = Fraction(3, 1)
left = Fraction(4, 1) / t
right = (t + 1)**2 / (4*t)
assert left == right == Fraction(4, 3)
print('VERIFY_OK d2=4/3')
