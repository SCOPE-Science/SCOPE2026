from fractions import Fraction as F

k = F(4)
eps = F(1, 10)
t = eps * eps

alpha0 = (1 + t) / (1 + k * t)
alpha_long = alpha0
alpha_short = (1 + k * t) / (1 + k * k * t)

assert alpha0 == F(101, 104)
assert alpha_long == F(101, 104)
assert alpha_short == F(26, 29)
assert alpha_short <= alpha_long

# The short endpoint gives the largest shift theta in the interval.
theta_short = 1 / alpha0 + 1 / alpha_short
poly = k * k * t * t + (k + 1) * t + 2 - k
assert poly < 0
assert (theta_short - k) * (1 + t) * (1 + k * t) == poly
assert theta_short < k

def second(alpha1):
    x1_0 = alpha0
    x1_1 = alpha0 * eps
    g1_0 = x1_0 - 1
    g1_1 = k * x1_1 - eps
    return x1_0 - alpha1 * g1_0, x1_1 - alpha1 * g1_1

xs = second(alpha_short)
xl = second(alpha_long)
assert xs == (F(3007, 3016), F(-4871, 30160))
assert xl == (F(10807, 10816), F(-4949, 27040))
assert xs[1] < 0 and xl[1] < 0

# Midpoint corroboration: the whole interval proof itself is analytic.
mid = (alpha_short + alpha_long) / 2
xm = second(mid)
assert xm[1] < 0

print('VERIFY_OK')
