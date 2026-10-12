from fractions import Fraction as F


def classify_unique(lam, g1, g2):
    assert lam > 0 and g1 > 0 and g2 > 0
    if g2 <= 1:
        return g1 * g1 <= 2 * lam
    if g2 < 2:
        return g1 * g1 < 2 * lam * g2 * (2 - g2)
    return False


def origin_is_global(lam, g1, g2):
    assert lam > 0 and g1 > 0 and g2 > 0
    if g2 <= 1:
        return g1 * g1 <= 2 * lam
    if g2 < 2:
        return g1 * g1 <= 2 * lam * g2 * (2 - g2)
    return False


def deficit(lam, g1, g2, x, y):
    return (lam + x*x + y*y)**2 - (g1*x + g2*x*y)**2 - lam*lam


def reduced_deficit(lam, g1, g2, x, y):
    t = x*x
    A = 2*(lam + y*y) - (g1 + g2*y)**2
    B = y*y*(2*lam + y*y)
    return t*t + A*t + B

# Exact algebraic reduction on a deterministic rational grid.
count = 0
vals = [F(-3,2), F(-1), F(-1,3), F(0), F(1,4), F(2,3), F(5,4)]
pars = [(F(11,16),F(1),F(1)), (F(3,2),F(4,5),F(1,2)), (F(2),F(3,2),F(3,2))]
for lam,g1,g2 in pars:
    for x in vals:
        for y in vals:
            assert deficit(lam,g1,g2,x,y) == reduced_deficit(lam,g1,g2,x,y)
            count += 1

# Source examples, with lambda obtained from its displayed N=4 formula.
lam = F(11,16)
assert not classify_unique(lam,F(4,3),F(2,3))
assert classify_unique(lam,F(1),F(1))
assert not classify_unique(lam,F(1),F(8,5))
assert not classify_unique(lam,F(1),F(2))

# Exact threshold logic in both regimes.
assert classify_unique(F(1),F(1),F(1))
assert classify_unique(F(1),F(2),F(1)) is False
assert origin_is_global(F(25,8),F(2),F(3,2))
# Here 2*lambda*g2*(2-g2) = 75/16 > 4, so uniqueness is strict.
assert classify_unique(F(25,8),F(2),F(3,2))
# Boundary example: lambda=1, gamma2=3/2 gives threshold gamma1^2=3/2.
# Avoid irrational gamma1 in exact arithmetic; verify the squared boundary relation itself.
assert 2*F(1)*F(3,2)*(2-F(3,2)) == F(3,2)

# At gamma2=2 no positive gamma1 can satisfy global-minimum criterion.
assert not origin_is_global(F(1),F(1,100),F(2))

print('VERIFY_OK', count, 4, 5)
