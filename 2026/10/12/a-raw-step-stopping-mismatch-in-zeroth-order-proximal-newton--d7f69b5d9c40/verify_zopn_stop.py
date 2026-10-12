from fractions import Fraction as Q

# Normalize epsilon to 1; the witness is homogeneous in epsilon.
eps = Q(1)
Lf = Q(1)
c1 = Q(1, 4)
c2 = Q(1)
beta = Q(1, 2)
gamma = Q(1)
underline_kappa = Q(1)
bar_kappa = Q(4)
kappa_eg = Q(1)
n = Q(1)

lower_t = beta * min(
    Q(1),
    underline_kappa * gamma * (Q(1) - 2 * c1) / Lf,
    2 * underline_kappa * gamma * n * c2 / (kappa_eg * kappa_eg),
)
assert lower_t == Q(1, 4)

# sqrt(c1 * lower_t * underline_kappa * gamma) = 1/4 exactly.
sqrt_term = Q(1, 4)
radius_ceiling = sqrt_term * eps / (
    2 * ((Lf + (2 - gamma) * bar_kappa) + sqrt_term * kappa_eg)
)
assert radius_ceiling == Q(1, 42)
Delta = eps / 100
assert Delta <= radius_ceiling

def f(x):
    return x * x / 2

x0 = 2 * eps
# Central difference with the theorem-compatible radius.
g0 = (f(x0 + Delta) - f(x0 - Delta)) / (2 * Delta)
assert g0 == x0 == 2 * eps

H0 = Q(4)
alpha = 1 / H0
y01 = x0 - alpha * g0
d0 = y01 - x0
assert y01 == Q(3, 2) * eps
assert d0 == -Q(1, 2) * eps

subproblem_residual = g0 + H0 * d0
assert subproblem_residual == 0
assert abs(d0) <= eps

returned = x0 + d0
stationarity = abs(returned)  # f'(x)=x and h=0
assert returned == Q(3, 2) * eps
assert stationarity == Q(3, 2) * eps
assert stationarity > eps

# Lemma 2.5 gives a sufficient scaled stopping certificate.
scaled_bound = (Lf + (2 - gamma) * bar_kappa) * abs(d0) + kappa_eg * Delta
assert scaled_bound > eps

print('VERIFY_OK')
