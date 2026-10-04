from fractions import Fraction

x = [Fraction(1), Fraction(3, 8)]
for _ in range(1, 84):
    x.append(Fraction(1, 2) * x[-1] - Fraction(1, 8) * x[-2])

assert x[:5] == [Fraction(1), Fraction(3,8), Fraction(1,16), Fraction(-1,64), Fraction(-1,64)]
for k in range(0, 80):
    assert x[k+4] == -x[k] / 64

ratios = [abs(x[k+1] / x[k]) for k in range(0, 80)]
pattern = [Fraction(3,8), Fraction(1,6), Fraction(1,4), Fraction(1)]
for k, r in enumerate(ratios):
    assert r == pattern[k % 4]
    assert r <= 1

# Objective is a positive multiple of x^2, so strict function restart never fires.
for k in range(0, 80):
    assert x[k+1] * x[k+1] <= x[k] * x[k]

# Since x_{k+1}=(3/8)y_k, the gradient-restart sign equals sign(x_{k+1}(x_{k+1}-x_k)).
signs = [x[k+1] * (x[k+1] - x[k]) for k in range(0, 8)]
assert signs[0] < 0
assert signs[1] < 0
assert signs[2] > 0

# Characteristic discriminant: (-1/2)^2 - 4*(1/8) = -1/4 < 0.
disc = Fraction(1,4) - Fraction(1,2)
assert disc == Fraction(-1,4)
print('VERIFY_OK')
