from fractions import Fraction as F

# Exact orthogonal-frame witness.  The normalized vectors are
# a=(1,80,50)/sqrt(8901), b=(80,-1,0)/sqrt(6401),
# c=(50,4000,-6401)/sqrt(8901*6401).
a = (1, 80, 50)
b = (80, -1, 0)
c = (50, 4000, -6401)

def dot(x, y):
    return sum(xi*yi for xi, yi in zip(x, y))

def norm2(x):
    return dot(x, x)

na, nb, nc = norm2(a), norm2(b), norm2(c)
assert dot(a,b) == dot(a,c) == dot(b,c) == 0
assert nc == na*nb

a2 = [F(x*x, na) for x in a]
b2 = [F(x*x, nb) for x in b]
c2 = [F(x*x, nc) for x in c]
assert sum(a2) == sum(b2) == sum(c2) == 1

# For two-stage MSARP (one pivot at each stage), r_i is the first-stage
# mass at i normalized by the rank-two leverage score at i.
r = [a2[i] / (a2[i] + b2[i]) for i in range(3)]

# Probability that the final two-column set omits l.
p_ms = [c2[l] * sum(r[i] for i in range(3) if i != l) for l in range(3)]
assert sum(p_ms) == 1

# The expected oblique interpolation error, divided by the optimal rank-two
# tail energy eta^2, is independent of eta.
R_oblique = 2 * sum(r)
assert R_oblique < 4

# Finite full-rank witness A = diag(2,1,eta) O^T with eta=10^{-4}.
# If column l is omitted, the optimal orthogonal CSS residual squared is
# eta^2 / (c_l^2 + eta^2 b_l^2 + eta^2 a_l^2/4).
eta2 = F(1, 10_000**2)
css_ratio_if_omit = [
    1 / (c2[l] + eta2*b2[l] + eta2*a2[l]/4)
    for l in range(3)
]
R_ms_css = sum(p_ms[l] * css_ratio_if_omit[l] for l in range(3))
R_one_css = sum(c2[l] * css_ratio_if_omit[l] for l in range(3))

assert R_ms_css > 3
assert R_one_css < 3
assert R_ms_css > R_one_css

print('norms_squared =', na, nb, nc)
print('r =', *r)
print('omission_probabilities_msarp =', *p_ms)
print('oblique_ratio_exact =', R_oblique)
print('oblique_ratio_decimal =', float(R_oblique))
print('msarp_css_ratio_exact =', R_ms_css)
print('msarp_css_ratio_decimal =', float(R_ms_css))
print('oneshot_css_ratio_exact =', R_one_css)
print('oneshot_css_ratio_decimal =', float(R_one_css))
print('msarp_over_oneshot_decimal =', float(R_ms_css/R_one_css))
