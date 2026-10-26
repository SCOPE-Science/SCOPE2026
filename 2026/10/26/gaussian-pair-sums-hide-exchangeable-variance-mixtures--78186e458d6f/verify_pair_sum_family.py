from fractions import Fraction as F

def summary(weighted_support):
    assert sum(weight for _, weight in weighted_support) == 1
    mean_v = sum(v * weight for v, weight in weighted_support)
    mean_v2 = sum(v * v * weight for v, weight in weighted_support)
    var_v = mean_v2 - mean_v * mean_v
    marginal_variance = F(1, 4) + mean_v / 2
    pair_covariance = F(1, 4) - mean_v / 2
    fourth_moment = 3 * (F(1, 16) + mean_v / 4 + mean_v2 / 4)
    fourth_cumulant = fourth_moment - 3 * marginal_variance**2
    return mean_v, var_v, marginal_variance, pair_covariance, fourth_moment, fourth_cumulant

rho_gaussian = [(F(1, 4), F(1, 1))]
rho_mixture = [(F(1, 8), F(1, 2)), (F(3, 8), F(1, 2))]
g = summary(rho_gaussian)
m = summary(rho_mixture)

assert g[0] == m[0] == F(1, 4)
assert g[2] == m[2] == F(3, 8)
assert g[3] == m[3] == F(1, 8)
assert g[4] == F(27, 64)
assert m[4] == F(111, 256)
assert g[5] == 0
assert m[5] == F(3, 256)
for v in (F(1, 8), F(1, 4), F(3, 8)):
    assert 1 - 2 * v + 2 * v == 1

print("Exact rational moment and covariance checks passed.")
