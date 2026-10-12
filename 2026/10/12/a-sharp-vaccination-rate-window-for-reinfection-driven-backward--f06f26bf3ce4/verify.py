from fractions import Fraction as F


def f(x, sigma):
    return F(1) - (F(1) - sigma) * x / (F(1) + x) ** 2


def source_ratio(x, sigma):
    return (F(1) + x * x + x * (F(1) + sigma)) / (F(1) + x) ** 2

# Exact normalization on several rational values.
for sigma in (F(1, 5), F(1, 2), F(4, 5)):
    for x in (F(1, 7), F(1, 2), F(1), F(3), F(11, 2)):
        assert f(x, sigma) == source_ratio(x, sigma)

# Exact minimum identity at x=1.
for sigma in (F(1, 5), F(1, 2), F(4, 5)):
    assert f(F(1), sigma) == (F(3) + sigma) / F(4)

# Nontrivial window example: sigma=1/2 and r=8/9.
sigma = F(1, 2)
r = F(8, 9)
x_minus = F(1, 2)
x_plus = F(2)
assert f(x_minus, sigma) == r
assert f(x_plus, sigma) == r
assert x_minus * x_plus == 1
assert f(F(1), sigma) < r
assert f(F(1, 4), sigma) > r
assert f(F(4), sigma) > r

print('VERIFY_OK')
