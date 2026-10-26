#!/usr/bin/env python3
"""Reproduce Gaussian moment and comb-power diagnostics (stdlib only)."""
import math
import random

n = 512
kappa = 0.8
reps = 9000
seed = 103117
pi = math.pi
sigma2 = 8 / 3 + 4 * (math.sqrt(3) - 3) / pi
sigma = math.sqrt(sigma2)
rho = math.sqrt(2) / (sigma * math.sqrt(pi))
c_d = 2 / (sigma * math.sqrt(pi))
c_p = 1 / math.sqrt(2)
coefficient_ratio = (c_d / c_p) ** 2
assert 1.0522 < sigma2 < 1.0523
assert 0.7777 < rho < 0.7780
assert 2.42 < coefficient_ratio < 2.421
assert 1 - 2 * rho * rho < 0

# Rebuild each Gaussian edge variance and adjacent covariance independently.
var_edge = 2 - 4 / pi
adj_cov = 1 / 3 + (2 * math.sqrt(3) - 4) / pi
assert abs(var_edge + 2 * adj_cov - sigma2) < 1e-13

# Independent evaluations of the folded-normal mean and its second derivative.
def folded_mean(a):
    return (2 / math.sqrt(pi)) * math.exp(-a * a / 4) + a * math.erf(a / 2)
for a in [0.1, 0.05, 0.025]:
    remainder = folded_mean(a) - 2 / math.sqrt(pi) - a * a / (2 * math.sqrt(pi))
    assert abs(remainder) < 0.1 * a ** 4

w1, w2 = rho, 1 - 2 * rho * rho
var_linear = w1 * w1 + w2 * w2 + 2 * rho * w1 * w2
mean_linear = w1 * c_d + w2 * c_p
assert abs(var_linear - (1 - rho * rho)) < 1e-12
assert abs(mean_linear - 1 / math.sqrt(2)) < 1e-12
assert abs(mean_linear / math.sqrt(var_linear) -
           1 / math.sqrt(2 * (1 - rho * rho))) < 1e-12

rng = random.Random(seed)
mu0 = (n - 1) / math.sqrt(n) * 2 / math.sqrt(pi)
def run(k):
    sums = [0.0, 0.0]
    sums2 = [0.0, 0.0]
    cross = 0.0
    eta = k * n ** (-0.25)
    for _ in range(reps):
        x = [rng.gauss(0.0, 1.0) for _ in range(n)]
        xbar = sum(x) / n
        rough = sum(abs(x[j+1] - x[j] + 2 * eta * (-1)**(j+1))
                    for j in range(n-1)) / math.sqrt(n)
        pearson = sum((xj - xbar + eta*(-1)**j)**2
                      for j, xj in enumerate(x))
        u = (rough - mu0) / sigma
        v = (pearson - (n - 1)) / math.sqrt(2*n)
        sums[0] += u; sums[1] += v
        sums2[0] += u*u; sums2[1] += v*v; cross += u*v
    means = [z/reps for z in sums]
    variances = [sums2[i]/reps - means[i]**2 for i in (0,1)]
    covariance = cross/reps - means[0]*means[1]
    return means,variances,covariance

null_mean,null_variance,null_cov=run(0.0)
alt_mean,alt_variance,alt_cov=run(kappa)
assert abs(null_mean[0]) < .07 and abs(null_mean[1]) < .07
assert abs(null_variance[0] - 1) < .12
assert abs(null_variance[1] - 1) < .12
assert abs(null_cov - rho) < .07
assert abs(alt_mean[0] - c_d*kappa*kappa) < .12
assert abs(alt_mean[1] - c_p*kappa*kappa) < .12

print(f"sigma_squared={sigma2:.15f}")
print(f"rho={rho:.15f}")
print(f"squared_signal_coefficient_ratio={coefficient_ratio:.15f}")
print(f"optimal_combination_weights=(rho,{1-2*rho*rho:.15f})")
print(f"null n={n} reps={reps}: mean={null_mean}, variance={null_variance}, covariance={null_cov:.12f}")
print(f"alternative kappa={kappa}: mean={alt_mean}, predicted={[c_d*kappa*kappa,c_p*kappa*kappa]}")
print("PASS: Gaussian-moment identities, optimal-weight identities, seeded numerical checks")
