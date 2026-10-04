from fractions import Fraction as F

# Exact witness parameters.
alpha = F(1, 2)
mu = F(1)
varphi = [F(1), F(1)]
mu_j = [F(1), F(1)]
gamma_j = [F(1), F(1)]
delta1 = F(1)
gamma = F(1)
beta = F(5)

phi = sum(varphi, F(0))
aE = mu + phi
aj = [mu + m + g for m, g in zip(mu_j, gamma_j)]
b = mu + delta1 + gamma

A = beta * (1-alpha) * phi / (b*aE)
B = [beta * alpha * v / (a*aE) for v, a in zip(varphi, aj)]
R_true = A + sum(B, F(0))
R_print_sq = max(A + x for x in B)

assert aE == 3 and aj == [3, 3] and b == 3
assert A == F(5, 9)
assert B == [F(5, 18), F(5, 18)]
assert R_true == F(10, 9) > 1
assert R_print_sq == F(5, 6) < 1

# For the infected matrix, write q = z+3. The downstream equations give
# I1=E/(2q), I2=E/(2q), C=E/q. Substitution in the E equation gives
# q E = 5(I1+I2+C) = 10 E/q, hence q^2=10.
branch_weight = alpha*varphi[0] + alpha*varphi[1] + (1-alpha)*phi
assert branch_weight == 2
assert beta * branch_weight == 10
# q=sqrt(10)>3, so z=q-3 is strictly positive.
assert 10 > 9

# General threshold decomposition for the witness matches the rank-one first-column formula.
rank_one_entry = beta/aE * (alpha*sum((v/a for v,a in zip(varphi,aj)), F(0)) + (1-alpha)*phi/b)
assert rank_one_entry == R_true

print('VERIFY_OK')
